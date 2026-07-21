#!/usr/bin/env python3
"""Persistent Whisper transcription worker for the vault recordings queue.

Queue model: files sitting in recordings/ ARE the queue. The worker loads the
Whisper model on demand, polls for stable audio files, writes transcripts/, then
moves audio to archive/. It never deletes a recording on failure.

GPU policy (default --device auto):
  - Use CUDA only when free VRAM looks sufficient for the configured model.
  - Never call `ollama stop` / never evict other GPU models.
  - If GPU is busy or OOM, fall back to CPU and keep draining the queue.

Inspect state:
  python3 scripts/transcribe_worker.py --status
  scripts/transcribe-ctl status
"""

from __future__ import annotations

import argparse
import fcntl
import gc
import json
import os
import shutil
import signal
import subprocess
import sys
import time
import traceback
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional

AUDIO_EXTS = {".m4a", ".mp3", ".wav", ".ogg", ".opus", ".aac", ".mp4", ".webm"}

# Rough VRAM floor (MiB) before attempting GPU load. medium ≈ 5GB weights + overhead.
VRAM_FLOOR_MIB = {
    "tiny": 1200,
    "base": 1500,
    "small": 2500,
    "medium": 4500,
    "large": 9000,
    "large-v2": 9000,
    "large-v3": 9000,
    "turbo": 7000,
}

DEFAULT_VAULT = Path.home() / "obsidian-vault"
DEFAULT_STATE_DIR = Path.home() / ".local" / "state" / "obsidian-transcribe"
LEGACY_LOCK = Path("/tmp/process-recordings.lock")
WORKER_LOCK = Path("/tmp/obsidian-transcribe-worker.lock")


def now_iso() -> str:
    return datetime.now().astimezone().isoformat(timespec="seconds")


def utc_iso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


@dataclass
class Status:
    updated: str = ""
    pid: int = 0
    state: str = "idle"  # starting|idle|waiting_legacy|transcribing|error|stopped
    device_policy: str = "auto"
    device_active: str = ""
    model_loaded: bool = False
    model: str = "medium"
    current_file: str = ""
    last_file: str = ""
    last_transcript: str = ""
    last_error: str = ""
    queued: list[str] = field(default_factory=list)
    transcribed_total: int = 0
    note: str = ""

    def write(self, path: Path) -> None:
        self.updated = now_iso()
        self.pid = os.getpid()
        path.parent.mkdir(parents=True, exist_ok=True)
        tmp = path.with_suffix(".tmp")
        tmp.write_text(json.dumps(asdict(self), indent=2) + "\n")
        tmp.replace(path)


def list_queued(recordings: Path) -> list[Path]:
    if not recordings.is_dir():
        return []
    files = [
        p
        for p in recordings.iterdir()
        if p.is_file() and p.suffix.lower() in AUDIO_EXTS and not p.name.startswith(".")
    ]
    return sorted(files, key=lambda p: p.stat().st_mtime)


def file_stable(path: Path, settle_s: float = 3.0, checks: int = 2) -> bool:
    """True when size+mtime stay unchanged across settle windows (Syncthing-safe)."""
    try:
        st = path.stat()
    except FileNotFoundError:
        return False
    last = (st.st_size, st.st_mtime_ns)
    for _ in range(checks):
        time.sleep(settle_s)
        try:
            st = path.stat()
        except FileNotFoundError:
            return False
        cur = (st.st_size, st.st_mtime_ns)
        if cur != last or st.st_size == 0:
            return False
        last = cur
    return True


def nvidia_free_mib() -> Optional[int]:
    try:
        out = subprocess.check_output(
            [
                "nvidia-smi",
                "--query-gpu=memory.free",
                "--format=csv,noheader,nounits",
            ],
            text=True,
            timeout=5,
        )
        # Multi-GPU: take the max free on any card (we use device 0 by default).
        vals = [int(x.strip()) for x in out.strip().splitlines() if x.strip()]
        return vals[0] if vals else None
    except (FileNotFoundError, subprocess.SubprocessError, ValueError):
        return None


def ollama_pinned_models() -> list[str]:
    """Best-effort peek via `ollama ps`. Empty if ollama missing/down."""
    try:
        out = subprocess.check_output(["ollama", "ps"], text=True, timeout=5)
    except (FileNotFoundError, subprocess.SubprocessError):
        return []
    lines = [ln.strip() for ln in out.splitlines() if ln.strip()]
    if len(lines) < 2:
        return []
    # Skip header; NAME is first column.
    names = []
    for ln in lines[1:]:
        name = ln.split()[0]
        if name.upper() != "NAME":
            names.append(name)
    return names


def legacy_backlog_running() -> Optional[int]:
    """Return PID of the old process-recordings.sh Phase-1 holder, if live."""
    if not LEGACY_LOCK.is_file():
        return None
    try:
        pid = int(LEGACY_LOCK.read_text().strip())
    except (OSError, ValueError):
        return None
    try:
        os.kill(pid, 0)
    except OSError:
        return None
    # Confirm it still looks like the legacy script (or its parent bash).
    try:
        cmdline = Path(f"/proc/{pid}/cmdline").read_bytes().decode("utf-8", "replace")
    except OSError:
        return None
    if "process-recordings" in cmdline or "whisper" in cmdline:
        return pid
    # Lock held by something else — still treat as busy to be safe.
    return pid


def acquire_worker_lock() -> Any:
    fh = open(WORKER_LOCK, "w")
    try:
        fcntl.flock(fh.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
    except BlockingIOError:
        fh.close()
        raise SystemExit(f"Another transcribe worker holds {WORKER_LOCK}; exiting.")
    fh.write(str(os.getpid()) + "\n")
    fh.flush()
    return fh


def choose_device(policy: str, model: str) -> tuple[str, str]:
    """Return (device, reason). Never evicts Ollama."""
    policy = policy.lower()
    if policy == "cpu":
        return "cpu", "forced by --device cpu"
    if policy not in {"auto", "cuda"}:
        raise SystemExit(f"Unknown device policy: {policy}")

    try:
        import torch
    except ImportError:
        if policy == "cuda":
            raise SystemExit("torch not importable; cannot use --device cuda")
        return "cpu", "torch unavailable"

    if not torch.cuda.is_available():
        if policy == "cuda":
            raise SystemExit("CUDA not available; cannot use --device cuda")
        return "cpu", "CUDA not available"

    free = nvidia_free_mib()
    floor = VRAM_FLOOR_MIB.get(model, 4500)
    pinned = ollama_pinned_models()
    pinned_note = f"; ollama pinned: {', '.join(pinned)}" if pinned else ""

    if free is None:
        # Fall through to trying CUDA; OOM handler will demote.
        if policy == "cuda":
            return "cuda", f"nvidia-smi unavailable; forcing CUDA{pinned_note}"
        return "cuda", f"nvidia-smi unavailable; trying CUDA{pinned_note}"

    if free < floor:
        msg = (
            f"only {free} MiB free VRAM (need ~{floor} for {model}){pinned_note}. "
            "Not evicting other models — use `ollama stop <model>` manually if you want GPU."
        )
        if policy == "cuda":
            raise SystemExit(f"GPU too full for --device cuda: {msg}")
        return "cpu", msg

    return "cuda", f"{free} MiB free VRAM (>= {floor}){pinned_note}"


def write_transcript(transcripts: Path, audio: Path, text: str) -> Path:
    transcripts.mkdir(parents=True, exist_ok=True)
    stem = audio.stem
    timestamp = datetime.now().strftime("%Y-%m-%d_%H%M%S")
    out = transcripts / f"{stem}_{timestamp}.md"
    body = (
        "---\n"
        f"source: {audio.name}\n"
        f"transcribed: {now_iso()}\n"
        "---\n\n"
        f"# Transcript: {audio.name}\n\n"
        f"{text.rstrip()}\n"
    )
    tmp = out.with_suffix(".md.tmp")
    tmp.write_text(body)
    tmp.replace(out)
    return out


def archive_audio(audio: Path, archive: Path) -> Path:
    archive.mkdir(parents=True, exist_ok=True)
    dest = archive / audio.name
    if dest.exists():
        stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        dest = archive / f"{audio.stem}_{stamp}{audio.suffix}"
    shutil.move(str(audio), str(dest))
    return dest


def print_status(state_path: Path, recordings: Path) -> int:
    queued = [p.name for p in list_queued(recordings)]
    if state_path.is_file():
        data = json.loads(state_path.read_text())
    else:
        data = {"state": "no-status-file", "note": f"missing {state_path}"}
    data["queued_now"] = queued
    data["queued_count"] = len(queued)
    legacy = legacy_backlog_running()
    data["legacy_backlog_pid"] = legacy
    pinned = ollama_pinned_models()
    data["ollama_pinned"] = pinned
    free = nvidia_free_mib()
    data["gpu_free_mib"] = free
    print(json.dumps(data, indent=2))
    return 0


class Worker:
    def __init__(self, args: argparse.Namespace) -> None:
        self.vault = Path(args.vault)
        self.recordings = Path(args.recordings)
        self.transcripts = Path(args.transcripts)
        self.archive = Path(args.archive)
        self.state_path = Path(args.state_file)
        self.model_name = args.model
        self.device_policy = args.device
        self.poll_s = args.poll_seconds
        self.language = args.language
        self.once = args.once
        self.ignore_legacy = args.ignore_legacy
        self.status = Status(model=self.model_name, device_policy=self.device_policy)
        self._stop = False
        self._model = None
        self._device = "cpu"
        self._lock_fh = None

    def request_stop(self, *_: Any) -> None:
        self._stop = True
        self.status.state = "stopping"
        self.status.note = "signal received; finishing current file if any"
        self.status.write(self.state_path)

    def load_model(self) -> None:
        import whisper

        device, reason = choose_device(self.device_policy, self.model_name)
        self.status.state = "starting"
        self.status.note = f"loading whisper {self.model_name} on {device}: {reason}"
        self.status.device_active = device
        self.status.model_loaded = False
        self.status.write(self.state_path)
        print(f"[transcribe] loading model={self.model_name} device={device} ({reason})", flush=True)

        try:
            self._model = whisper.load_model(self.model_name, device=device)
            self._device = device
        except Exception as exc:  # noqa: BLE001 — demote to CPU on any CUDA failure
            if device == "cpu":
                raise
            print(
                f"[transcribe] GPU load failed ({exc!r}); falling back to CPU. "
                "Not evicting Ollama/other GPU users.",
                flush=True,
            )
            self._model = whisper.load_model(self.model_name, device="cpu")
            self._device = "cpu"
            self.status.device_active = "cpu"
            self.status.note = f"fell back to CPU after GPU load failure: {exc}"
            self.status.model_loaded = True
            self.status.write(self.state_path)

        self.status.state = "idle"
        self.status.device_active = self._device
        self.status.model_loaded = True
        self.status.note = f"model ready on {self._device}"
        self.status.write(self.state_path)
        print(f"[transcribe] ready on {self._device}", flush=True)

    def unload_model(self, reason: str) -> None:
        if self._model is None:
            self.status.state = "idle"
            self.status.device_active = ""
            self.status.model_loaded = False
            self.status.note = reason
            self.status.write(self.state_path)
            return

        was_cuda = self._device == "cuda"
        self._model = None
        self._device = "cpu"
        gc.collect()
        if was_cuda:
            try:
                import torch

                if torch.cuda.is_available():
                    torch.cuda.empty_cache()
                    if hasattr(torch.cuda, "ipc_collect"):
                        torch.cuda.ipc_collect()
            except Exception:
                pass
        self.status.state = "idle"
        self.status.device_active = ""
        self.status.model_loaded = False
        self.status.note = reason
        self.status.write(self.state_path)
        print(f"[transcribe] unloaded model ({reason})", flush=True)

    def ensure_model_loaded(self) -> None:
        if self._model is None:
            self.load_model()

    def wait_for_legacy(self) -> None:
        if self.ignore_legacy:
            return
        while not self._stop:
            pid = legacy_backlog_running()
            if pid is None:
                return
            self.status.state = "waiting_legacy"
            self.status.note = (
                f"legacy process-recordings.sh still running (pid {pid}); "
                "not claiming recordings until it exits"
            )
            self.status.queued = [p.name for p in list_queued(self.recordings)]
            self.status.write(self.state_path)
            print(f"[transcribe] waiting for legacy backlog pid={pid}", flush=True)
            time.sleep(min(30, self.poll_s * 2))

    def transcribe_one(self, audio: Path) -> None:
        self.ensure_model_loaded()
        assert self._model is not None
        self.status.state = "transcribing"
        self.status.current_file = audio.name
        self.status.queued = [p.name for p in list_queued(self.recordings)]
        self.status.note = f"transcribing on {self._device}"
        self.status.last_error = ""
        self.status.write(self.state_path)
        print(f"[transcribe] start {audio.name} device={self._device}", flush=True)

        try:
            result = self._model.transcribe(str(audio), language=self.language or None, fp16=(self._device == "cuda"))
            text = (result.get("text") or "").strip()
            if not text:
                raise RuntimeError("whisper returned empty transcript")
            transcript = write_transcript(self.transcripts, audio, text)
            archived = archive_audio(audio, self.archive)
            self.status.transcribed_total += 1
            self.status.last_file = audio.name
            self.status.last_transcript = str(transcript)
            self.status.current_file = ""
            self.status.state = "idle"
            self.status.note = f"archived {archived.name}"
            self.status.queued = [p.name for p in list_queued(self.recordings)]
            self.status.write(self.state_path)
            print(f"[transcribe] done {audio.name} -> {transcript}", flush=True)
        except Exception as exc:  # noqa: BLE001
            # Leave the file in recordings/ so nothing is dropped.
            self.status.state = "error"
            self.status.last_error = f"{exc!r}"
            self.status.note = (
                f"failed on {audio.name}; left in recordings/ for retry. {traceback.format_exc(limit=3)}"
            )
            self.status.current_file = ""
            self.status.write(self.state_path)
            print(f"[transcribe] ERROR on {audio.name}: {exc!r}", flush=True)

            # One-shot CUDA demotion for subsequent files if this looks like OOM.
            msg = str(exc).lower()
            if self._device == "cuda" and ("out of memory" in msg or "cuda" in msg):
                print("[transcribe] demoting session to CPU after CUDA failure", flush=True)
                import whisper

                self._model = whisper.load_model(self.model_name, device="cpu")
                self._device = "cpu"
                self.status.device_active = "cpu"
                self.status.model_loaded = True
                self.status.write(self.state_path)

    def run(self) -> int:
        self._lock_fh = acquire_worker_lock()
        signal.signal(signal.SIGTERM, self.request_stop)
        signal.signal(signal.SIGINT, self.request_stop)

        self.wait_for_legacy()
        if self._stop:
            self.status.state = "stopped"
            self.status.model_loaded = False
            self.status.write(self.state_path)
            return 0

        processed_this_invocation = 0
        while not self._stop:
            self.wait_for_legacy()
            if self._stop:
                break

            queued = list_queued(self.recordings)
            self.status.queued = [p.name for p in queued]
            if not queued:
                self.status.current_file = ""
                self.unload_model("queue empty; model unloaded")
                if self.once:
                    break
                time.sleep(self.poll_s)
                continue

            # Pick oldest stable file.
            target = None
            for candidate in queued:
                if file_stable(candidate):
                    target = candidate
                    break
            if target is None:
                self.status.state = "idle"
                self.status.note = "files present but not yet stable (still syncing?)"
                self.status.write(self.state_path)
                time.sleep(self.poll_s)
                continue

            self.transcribe_one(target)
            processed_this_invocation += 1
            if self.once:
                break

        self.status.state = "stopped"
        self.status.note = f"clean stop after {processed_this_invocation} file(s) this run"
        self.status.current_file = ""
        self.status.queued = [p.name for p in list_queued(self.recordings)]
        self.status.device_active = ""
        self.status.model_loaded = False
        self.status.write(self.state_path)
        return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--vault", default=str(DEFAULT_VAULT))
    p.add_argument("--recordings", default=None, help="defaults to <vault>/recordings")
    p.add_argument("--transcripts", default=None, help="defaults to <vault>/transcripts")
    p.add_argument("--archive", default=None, help="defaults to <vault>/archive")
    p.add_argument("--state-file", default=str(DEFAULT_STATE_DIR / "status.json"))
    p.add_argument("--model", default=os.environ.get("WHISPER_MODEL", "medium"))
    p.add_argument(
        "--device",
        default=os.environ.get("WHISPER_DEVICE", "auto"),
        choices=["auto", "cpu", "cuda"],
        help="auto=GPU if enough free VRAM else CPU; never evicts Ollama",
    )
    p.add_argument("--language", default="en")
    p.add_argument("--poll-seconds", type=float, default=15.0)
    p.add_argument("--once", action="store_true", help="process at most one stable file then exit")
    p.add_argument(
        "--ignore-legacy",
        action="store_true",
        help="do not wait for /tmp/process-recordings.lock (smoke tests / isolated dirs)",
    )
    p.add_argument("--status", action="store_true", help="print queue/worker status JSON and exit")
    return p


def main(argv: Optional[list[str]] = None) -> int:
    args = build_parser().parse_args(argv)
    vault = Path(args.vault)
    args.recordings = args.recordings or str(vault / "recordings")
    args.transcripts = args.transcripts or str(vault / "transcripts")
    args.archive = args.archive or str(vault / "archive")

    if args.status:
        return print_status(Path(args.state_file), Path(args.recordings))

    return Worker(args).run()


if __name__ == "__main__":
    sys.exit(main())
