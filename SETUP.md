# Voice-to-Article Pipeline Setup

## What's already done
- [x] Vault folder structure: `~/obsidian-vault/{recordings,transcripts,drafts,archive}`
- [x] Whisper installed in `~/.local/share/whisper-venv/` (medium model)
- [x] Persistent transcription worker: `scripts/transcribe_worker.py` + `obsidian-transcribe.service`
- [x] Enrichment cron: `~/obsidian-vault/process-recordings.sh` (draft shaping only)
- [x] Git backup to `git@github.com:TheF1rstPancake/obsidian_vault.git`
- [x] Backup script: `~/obsidian-vault/sync-vault.sh` (auto-commits and pushes)
- [x] Cron jobs installed (enrich drafts every 5 min, git sync every 30 min)
- [x] rclone + syncthing installed

## Transcription worker (persistent Whisper)

Recordings in `recordings/` **are the queue**. A long-lived worker loads the Whisper
model once and drains that directory into `transcripts/`, then moves audio to
`archive/`. Cron no longer shells out to `whisper` per file (that reloaded the
model every run and fought Ollama for VRAM).

### Install / operate

```bash
# one-time (or after editing systemd/obsidian-transcribe.service)
./scripts/transcribe-ctl install
./scripts/transcribe-ctl enable

./scripts/transcribe-ctl status    # JSON: queue, device, current file, errors
./scripts/transcribe-ctl queued    # paths waiting in recordings/
./scripts/transcribe-ctl logs      # journalctl -f
./scripts/transcribe-ctl stop|start|restart
```

Or plain systemd:

```bash
systemctl --user status obsidian-transcribe.service
systemctl --user restart obsidian-transcribe.service
journalctl --user -u obsidian-transcribe.service -f
```

Foreground one-shot (useful for debugging):

```bash
./scripts/transcribe-ctl once
# or:
~/.local/share/whisper-venv/bin/python3 scripts/transcribe_worker.py --once --device auto
```

### GPU / Ollama policy

- Default `--device auto`: use CUDA only if free VRAM looks sufficient for the
  model; otherwise run on CPU and keep draining the queue.
- The worker **never** runs `ollama stop` and never evicts other GPU users.
- To free VRAM yourself: `ollama ps` then `ollama stop <model>`, optionally
  `systemctl --user restart obsidian-transcribe` afterward if you want it to
  re-evaluate GPU.
- Failures leave the audio in `recordings/` (no silent drops).

Runtime status file: `~/.local/state/obsidian-transcribe/status.json`.

## Manual steps remaining

### 1. Expose Syncthing UI via Tailscale (needs sudo)
```bash
sudo tailscale serve --bg --https 8385 http://127.0.0.1:8384
```
Then open `https://<your-tailscale-host>:8385` (find your host with `tailscale status`).

### 2. Start Syncthing and pair phone
```bash
syncthing
```
- Open `https://<your-tailscale-host>:8385` from any device on tailnet
- Add your phone as a device (scan QR code)
- Share `~/obsidian-vault/recordings/` folder with your phone
- On phone: install Syncthing, connect over Tailscale

### 3. Install Obsidian
Download from https://obsidian.md/ (AppImage or Snap)
```bash
sudo snap install obsidian
```
Open Obsidian → "Open folder as vault" → select `~/obsidian-vault/`

## Services & URLs

| Service    | URL / Location                                    |
|------------|---------------------------------------------------|
| Syncthing  | `https://<your-tailscale-host>:8385`              |
| GitHub     | `github.com/TheF1rstPancake/obsidian_vault`       |
| Vault path | `~/obsidian-vault/`                               |
| Transcribe | `systemctl --user status obsidian-transcribe`     |

## Cron jobs (installed)
```cron
# Enrich new transcripts into drafts every 5 minutes (no Whisper / no GPU)
*/5 * * * * /home/giovanni/obsidian-vault/process-recordings.sh >> /tmp/process-recordings.log 2>&1

# Sync vault to GitHub every 30 minutes
*/30 * * * * /home/giovanni/obsidian-vault/sync-vault.sh >> /tmp/vault-sync.log 2>&1
```

## How it works

1. Record voice memo on phone → saved to phone's Syncthing folder
2. Syncthing syncs to `~/obsidian-vault/recordings/` over Tailscale
3. `obsidian-transcribe.service` picks up stable audio files:
   - Whisper (model kept resident) → `transcripts/`
   - Audio moved to `archive/`
4. Cron runs `process-recordings.sh` every 5 min for enrichment only:
   - Claude matches transcript to an existing draft or creates a new one → `drafts/`
5. Open Obsidian, refine drafts
6. Cron syncs vault to GitHub every 30 min

## File naming for multi-recording grouping
Claude auto-detects topic matches, but you can also help it by prefixing recordings:
- `startup-idea-001.m4a`, `startup-idea-002.m4a` → same article
- `random-thought.m4a` → new article
