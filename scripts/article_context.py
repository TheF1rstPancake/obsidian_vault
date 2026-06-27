#!/usr/bin/env python3
"""Build a deterministic editorial context bundle for an article slug.

The bundle gives a writer/editor pass everything it needs in one file:
the vault conventions (CLAUDE.md), the schema (SCHEMA.md), the voice/style
guide (STYLE.md), the lossless source (notes.md), the current draft
(article.md), the open and past pancake-review annotations for the slug,
and a bounded set of voice-sample snippets.

Usage:
    python3 scripts/article_context.py <slug> [--output PATH]

Defaults to writing drafts/<slug>/.pipeline/context.md. Stdlib only, so it
runs under /usr/bin/python3 with no dependencies. Never fails because the
annotations file is missing or empty.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

# Repo layout: this file lives at <vault>/scripts/article_context.py.
VAULT_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_ANNOTATIONS_PATH = Path.home() / ".hermes" / "annotations.json"

# Bounds so a giant transcript or sample set can't produce an unusable bundle.
VOICE_SAMPLE_SNIPPET_CHARS = 1200
VOICE_SAMPLES_TOTAL_CHARS = 6000
NOTES_MAX_CHARS = 40000


# --------------------------------------------------------------------------
# Annotations
# --------------------------------------------------------------------------
def load_annotations(path: os.PathLike | str | None = None) -> list[dict]:
    """Load the flat annotation list. Returns [] if the file is missing or bad.

    pancake-review stores a flat JSON array at ~/.hermes/annotations.json.
    This must never raise — a missing or malformed file just means "no
    annotations", not a crash.
    """
    path = Path(path) if path is not None else DEFAULT_ANNOTATIONS_PATH
    try:
        raw = path.read_text(encoding="utf-8")
    except (FileNotFoundError, NotADirectoryError, OSError):
        return []
    try:
        data = json.loads(raw)
    except (json.JSONDecodeError, ValueError):
        return []
    if not isinstance(data, list):
        return []
    return [a for a in data if isinstance(a, dict)]


def annotation_fields(a: dict) -> tuple[str, str]:
    """Return (highlighted_text, comment), tolerating the legacy field names.

    Newer annotations use highlighted_text + comment; pre-June-2026 ones used
    quote + note. Prefer the new names, fall back to the old.
    """
    highlighted = a.get("highlighted_text") or a.get("quote") or ""
    comment = a.get("comment") or a.get("note") or ""
    return highlighted, comment


def filter_annotations(
    annotations: list[dict], slug: str, resolved: bool | None = False
) -> list[dict]:
    """Annotations for `slug`. resolved=False -> open, True -> resolved, None -> all."""
    out = []
    for a in annotations:
        if a.get("slug") != slug:
            continue
        if resolved is None:
            out.append(a)
        elif bool(a.get("resolved")) == resolved:
            out.append(a)
    return out


def _render_annotations(annotations: list[dict], slug: str) -> str:
    open_anns = filter_annotations(annotations, slug, resolved=False)
    resolved_anns = filter_annotations(annotations, slug, resolved=True)

    lines: list[str] = []
    lines.append(f"### Unresolved annotations ({len(open_anns)})")
    lines.append("")
    if not open_anns:
        lines.append("_None. No open pancake-review annotations for this slug._")
    else:
        lines.append(
            "Each is a direct instruction from Giovanni. Address it or, if "
            "unclear, surface it (do not silently skip)."
        )
        lines.append("")
        for a in open_anns:
            highlighted, comment = annotation_fields(a)
            anno_id = str(a.get("id", ""))[:8]
            blocked = a.get("blocked_reason")
            lines.append(f"- **[{anno_id}]** on {highlighted!r}")
            lines.append(f"  - wants: {comment}")
            if blocked:
                lines.append(f"  - previously blocked: {blocked}")
    lines.append("")

    # Resolved annotations are kept as "lessons" — proof of what Giovanni
    # actually wanted, useful as regression examples for the editor.
    lines.append(f"### Resolved annotation lessons ({len(resolved_anns)})")
    lines.append("")
    if not resolved_anns:
        lines.append("_None recorded._")
    else:
        lines.append(
            "Past corrections on this article. Treat as confirmed preferences; "
            "do not reintroduce what was already cut."
        )
        lines.append("")
        for a in resolved_anns:
            highlighted, comment = annotation_fields(a)
            anno_id = str(a.get("id", ""))[:8]
            proof = a.get("proof")
            lines.append(f"- **[{anno_id}]** on {highlighted!r} → {comment}")
            if proof:
                lines.append(f"  - resolved with: {proof}")
    lines.append("")
    return "\n".join(lines)


# --------------------------------------------------------------------------
# Files
# --------------------------------------------------------------------------
def _read_text(path: Path, max_chars: int | None = None) -> str | None:
    try:
        text = path.read_text(encoding="utf-8")
    except (FileNotFoundError, NotADirectoryError, OSError):
        return None
    if max_chars is not None and len(text) > max_chars:
        text = text[:max_chars] + f"\n\n_[truncated at {max_chars} chars]_\n"
    return text


def _render_voice_samples(vault_root: Path) -> str:
    samples_dir = vault_root / "vault-meta" / "voice-samples"
    lines = ["### Voice samples (bounded snippets)", ""]
    if not samples_dir.is_dir():
        lines.append("_No voice-samples directory found._")
        lines.append("")
        return "\n".join(lines)

    files = sorted(p for p in samples_dir.glob("*.md") if p.is_file())
    if not files:
        lines.append("_No voice samples found._")
        lines.append("")
        return "\n".join(lines)

    lines.append(
        "Calibration anchors for Giovanni's voice. Snippets only — open the "
        "full file in `vault-meta/voice-samples/` for the complete sample."
    )
    lines.append("")
    budget = VOICE_SAMPLES_TOTAL_CHARS
    for f in files:
        text = _read_text(f) or ""
        snippet = text[:VOICE_SAMPLE_SNIPPET_CHARS].rstrip()
        if budget <= 0:
            lines.append(f"- `{f.name}` _(omitted — snippet budget exhausted)_")
            continue
        if len(snippet) > budget:
            snippet = snippet[:budget].rstrip()
        budget -= len(snippet)
        lines.append(f"#### `{f.name}`")
        lines.append("")
        lines.append("```markdown")
        lines.append(snippet)
        lines.append("```")
        lines.append("")
    return "\n".join(lines)


def _section(title: str, body: str | None, missing_msg: str) -> str:
    out = [f"## {title}", ""]
    if body is None or body.strip() == "":
        out.append(f"_{missing_msg}_")
    else:
        out.append(body.rstrip())
    out.append("")
    return "\n".join(out)


# --------------------------------------------------------------------------
# Bundle
# --------------------------------------------------------------------------
def build_context(
    slug: str,
    vault_root: Path | str = VAULT_ROOT,
    annotations_path: os.PathLike | str | None = None,
) -> str:
    """Assemble the full context.md text for `slug`. Pure function — no writes."""
    vault_root = Path(vault_root)
    draft_dir = vault_root / "drafts" / slug

    annotations = load_annotations(annotations_path)

    parts: list[str] = []
    parts.append(f"# Editorial context — `{slug}`")
    parts.append("")
    parts.append(
        "Generated by `scripts/article_context.py`. This is a disposable "
        "bundle for an editor/writer pass; it is not published. Order matters: "
        "source and intent first, conventions second, voice last."
    )
    parts.append("")

    parts.append(
        _section(
            "notes.md (lossless source — the author's actual intent)",
            _read_text(draft_dir / "notes.md", NOTES_MAX_CHARS),
            "No notes.md for this slug.",
        )
    )
    parts.append(
        _section(
            "article.md (current draft)",
            _read_text(draft_dir / "article.md"),
            "No article.md for this slug yet.",
        )
    )

    parts.append("## Annotations (pancake-review)")
    parts.append("")
    parts.append(_render_annotations(annotations, slug))

    parts.append(
        _section(
            "STYLE.md (voice + editing guide — required)",
            _read_text(vault_root / "STYLE.md"),
            "STYLE.md not found.",
        )
    )
    parts.append(
        _section(
            "SCHEMA.md (frontmatter + folder layout)",
            _read_text(vault_root / "SCHEMA.md"),
            "SCHEMA.md not found.",
        )
    )
    parts.append(
        _section(
            "CLAUDE.md (vault conventions)",
            _read_text(vault_root / "CLAUDE.md"),
            "CLAUDE.md not found.",
        )
    )

    parts.append("## Voice")
    parts.append("")
    parts.append(_render_voice_samples(vault_root))

    return "\n".join(parts).rstrip() + "\n"


def default_output_path(slug: str, vault_root: Path | str = VAULT_ROOT) -> Path:
    return Path(vault_root) / "drafts" / slug / ".pipeline" / "context.md"


def write_context(
    slug: str,
    output: os.PathLike | str | None = None,
    vault_root: Path | str = VAULT_ROOT,
    annotations_path: os.PathLike | str | None = None,
) -> Path:
    text = build_context(slug, vault_root=vault_root, annotations_path=annotations_path)
    out_path = Path(output) if output else default_output_path(slug, vault_root)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(text, encoding="utf-8")
    return out_path


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("slug", help="article slug (drafts/<slug>/)")
    parser.add_argument(
        "--output", "-o", default=None, help="output path (default: drafts/<slug>/.pipeline/context.md)"
    )
    parser.add_argument(
        "--vault-root", default=str(VAULT_ROOT), help="vault root (default: repo root)"
    )
    parser.add_argument(
        "--annotations", default=None, help="annotations.json path (default: ~/.hermes/annotations.json)"
    )
    args = parser.parse_args(argv)

    draft_dir = Path(args.vault_root) / "drafts" / args.slug
    if not draft_dir.is_dir():
        print(f"warning: {draft_dir} does not exist — building context anyway", file=sys.stderr)

    out_path = write_context(
        args.slug,
        output=args.output,
        vault_root=args.vault_root,
        annotations_path=args.annotations,
    )
    print(str(out_path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
