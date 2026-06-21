"""pancake-review — a local article annotation tool.

Reads posts and guides directly from the vault (local markdown files).
Renders them in a clean, mobile-friendly reader view and lets you highlight
text and leave notes.  Annotations are stored in ~/.hermes/annotations.json
so that Hermes can fetch unresolved ones, edit the markdown source, and mark
them resolved.

Run:
    uv run uvicorn main:app --host 0.0.0.0 --port 4242 --reload
"""
from __future__ import annotations

import html as html_mod
import json
import os
import re
import subprocess
import uuid
from datetime import datetime, timezone
from pathlib import Path

import frontmatter
import markdown as md_lib
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Query, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

# --------------------------------------------------------------------------- #
# Paths & config
# --------------------------------------------------------------------------- #
HERE = Path(__file__).resolve().parent
VAULT_ROOT = HERE.parent
load_dotenv(VAULT_ROOT / ".env")

ANNOTATIONS_PATH = Path(
    os.environ.get("PANCAKE_ANNOTATIONS", str(Path.home() / ".hermes" / "annotations.json"))
)
DRAFTS_DIR = VAULT_ROOT / "drafts"
GUIDES_DIR = VAULT_ROOT / "guides"

templates = Jinja2Templates(directory=str(HERE / "templates"))
app = FastAPI(title="pancake-review")


# --------------------------------------------------------------------------- #
# Markdown rendering (with Obsidian-style callout support)
# --------------------------------------------------------------------------- #
_CALLOUT_ALIASES = {
    "info": "note", "example": "note", "quote": "note",
    "hint": "tip",
    "caution": "warning", "danger": "warning",
}


def _render_markdown(text: str) -> str:
    """Render vault markdown to HTML.

    Converts > [!type] callout blocks to styled divs before the main
    markdown pass.  Raw HTML blocks (the converted callouts) are passed
    through unchanged by python-markdown.
    """
    # Strip paywall marker — show as a thematic break for review context
    text = re.sub(r"\n---paywall---\n", "\n\n---\n\n", text)

    lines = text.split("\n")
    out: list[str] = []
    i = 0
    while i < len(lines):
        m = re.match(r"^>\s*\[!([\w]+)\](?:\s+(.+))?$", lines[i])
        if m:
            raw_type = m.group(1).lower()
            call_type = _CALLOUT_ALIASES.get(raw_type, raw_type)
            if call_type not in ("note", "tip", "warning"):
                call_type = "note"
            title = m.group(2) or raw_type.capitalize()
            body_lines: list[str] = []
            i += 1
            while i < len(lines) and lines[i].startswith(">"):
                body_lines.append(lines[i][1:].lstrip())
                i += 1
            body_html = md_lib.markdown("\n".join(body_lines), extensions=["extra"])
            out.append(
                f'<div class="callout callout-{call_type}">'
                f'<span class="callout-title">{html_mod.escape(title)}</span>'
                f'<div class="callout-body">{body_html}</div>'
                f"</div>"
            )
        else:
            out.append(lines[i])
            i += 1

    return md_lib.markdown("\n".join(out), extensions=["extra", "sane_lists"])


# --------------------------------------------------------------------------- #
# Local file readers
# --------------------------------------------------------------------------- #
def list_articles() -> list[dict]:
    """Scan drafts/*/article.md and return metadata for all posts."""
    articles: list[dict] = []
    for path in DRAFTS_DIR.glob("*/article.md"):
        slug = path.parent.name
        try:
            post = frontmatter.load(str(path))
        except Exception:
            continue
        meta = post.metadata
        updated = meta.get("updated") or meta.get("date") or meta.get("created")
        articles.append({
            "slug": slug,
            "title": meta.get("title", slug),
            "status": meta.get("status", "raw"),
            "updated": str(updated) if updated else "",
            "point": meta.get("point", "") or "",
            "kind": "post",
            "unresolved": 0,  # filled in by the index route
        })
    articles.sort(key=lambda a: a["updated"], reverse=True)
    return articles


def list_guides() -> list[dict]:
    """Scan guides/*/ and return metadata from each overview.md."""
    guides: list[dict] = []
    if not GUIDES_DIR.exists():
        return guides
    for guide_dir in GUIDES_DIR.iterdir():
        if not guide_dir.is_dir():
            continue
        overview = guide_dir / "overview.md"
        if not overview.exists():
            continue
        try:
            post = frontmatter.load(str(overview))
        except Exception:
            continue
        meta = post.metadata
        guides.append({
            "slug": guide_dir.name,
            "title": meta.get("title", guide_dir.name),
            "status": meta.get("status", "raw"),
            "visibility": meta.get("visibility", "public"),
            "has_content": (guide_dir / "content.md").exists(),
            "kind": "guide",
            "unresolved": 0,
        })
    guides.sort(key=lambda g: g["title"])
    return guides


def _resolve_dir(slug: str) -> tuple[Path, str, str]:
    """Locate the folder backing a slug.

    Returns (base_dir, kind, default_file).  Drafts take precedence over
    guides, matching the original lookup order.
    """
    draft_dir = DRAFTS_DIR / slug
    guide_dir = GUIDES_DIR / slug
    if draft_dir.is_dir():
        return draft_dir, "post", "article"
    if guide_dir.is_dir():
        return guide_dir, "guide", "overview"
    raise HTTPException(404, f"No local folder for slug '{slug}'")


def _default_file(slug: str) -> str:
    """Default markdown file (without extension) for a slug."""
    return _resolve_dir(slug)[2]


def get_article(slug: str, file: str | None = None) -> dict:
    """Read and render a local markdown file by slug + file.

    `file` is the filename stem (no extension) inside the slug's folder —
    e.g. "article", "overview", "content", "notes".  Defaults to the
    folder's canonical file (article.md for drafts, overview.md for guides).
    """
    base_dir, kind, default_file = _resolve_dir(slug)
    fname = file or default_file
    # Guard against path traversal — only simple filename stems allowed.
    if not re.fullmatch(r"[\w-]+", fname):
        raise HTTPException(400, f"Invalid file name '{fname}'")

    path = base_dir / f"{fname}.md"
    if not path.exists():
        raise HTTPException(404, f"No file '{fname}.md' for slug '{slug}'")

    try:
        post = frontmatter.load(str(path))
    except Exception as e:
        raise HTTPException(500, f"Failed to parse {path}: {e}")

    # Build toggle options for guides that have both overview and content.
    toggle: list[dict] = []
    if kind == "guide" and (base_dir / "content.md").exists():
        toggle = [
            {"file": "overview", "label": "Overview"},
            {"file": "content", "label": "Content"},
        ]

    meta = post.metadata
    return {
        "title": meta.get("title", slug),
        "slug": slug,
        "file": fname,
        "kind": kind,
        "toggle": toggle,
        "html": _render_markdown(post.content),
        "status": meta.get("status", "raw"),
    }


# --------------------------------------------------------------------------- #
# Annotation storage (~/.hermes/annotations.json)
# --------------------------------------------------------------------------- #
def _load_annotations() -> list[dict]:
    if not ANNOTATIONS_PATH.exists():
        return []
    try:
        text = ANNOTATIONS_PATH.read_text()
        return json.loads(text) if text.strip() else []
    except (json.JSONDecodeError, OSError):
        return []


BACKUP_DIR = ANNOTATIONS_PATH.parent / "annotations_backup"


def _save_annotations(items: list[dict]) -> None:
    ANNOTATIONS_PATH.parent.mkdir(parents=True, exist_ok=True)
    tmp = ANNOTATIONS_PATH.with_suffix(".json.tmp")
    payload = json.dumps(items, indent=2, ensure_ascii=False)
    tmp.write_text(payload)
    tmp.replace(ANNOTATIONS_PATH)  # atomic primary write

    # Always keep a timestamped backup so data survives any server restart or
    # diagnostic confusion.  Backups older than 30 days are pruned on write.
    BACKUP_DIR.mkdir(parents=True, exist_ok=True)
    ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    (BACKUP_DIR / f"annotations_{ts}.json").write_text(payload)
    # prune backups older than 30 days
    cutoff = datetime.now(timezone.utc).timestamp() - 30 * 86400
    for f in BACKUP_DIR.glob("annotations_*.json"):
        if f.stat().st_mtime < cutoff:
            f.unlink(missing_ok=True)


class NewAnnotation(BaseModel):
    slug: str
    highlighted_text: str
    comment: str
    file: str | None = None


class AnnotationPatch(BaseModel):
    resolved: bool = True
    proof: str | None = None
    blocked_reason: str | None = None


# --------------------------------------------------------------------------- #
# Page routes
# --------------------------------------------------------------------------- #
@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    counts = _unresolved_counts()
    articles = list_articles()
    guides = list_guides()
    for item in (*articles, *guides):
        item["unresolved"] = counts.get(item["slug"], 0)
    return templates.TemplateResponse(
        request, "index.html", {"articles": articles, "guides": guides}
    )


@app.get("/article/{slug}", response_class=HTMLResponse)
def article(request: Request, slug: str, file: str | None = Query(None)):
    post = get_article(slug, file)
    return templates.TemplateResponse(
        request,
        "article.html",
        {"post": post, "slug": slug, "file": post["file"]},
    )


# --------------------------------------------------------------------------- #
# JSON API
# --------------------------------------------------------------------------- #
@app.get("/api/articles")
def api_articles():
    return {"articles": list_articles()}


def _unresolved_counts() -> dict[str, int]:
    """Unresolved annotation counts per slug (summed across all files)."""
    counts: dict[str, int] = {}
    for a in _load_annotations():
        if not a.get("resolved"):
            counts[a["slug"]] = counts.get(a["slug"], 0) + 1
    return counts


def _anno_file(a: dict) -> str:
    """File a stored annotation belongs to, defaulting for legacy records."""
    f = a.get("file")
    if f:
        return f
    # Legacy annotations predate per-file storage — attribute to the slug's
    # canonical file so they still surface on the default view.
    try:
        return _default_file(a["slug"])
    except HTTPException:
        return "article"


@app.post("/annotations")
def create_annotation(body: NewAnnotation):
    text = body.highlighted_text.strip()
    comment = body.comment.strip()
    if not text:
        raise HTTPException(400, "highlighted_text is required")
    if not comment:
        raise HTTPException(400, "comment is required")
    file = body.file or _default_file(body.slug)
    item = {
        "id": uuid.uuid4().hex,
        "slug": body.slug,
        "file": file,
        "highlighted_text": text,
        "comment": comment,
        "resolved": False,
        "created_at": datetime.now(timezone.utc).isoformat(),
    }
    items = _load_annotations()
    items.append(item)
    _save_annotations(items)
    return item


@app.get("/annotations/{slug}")
def list_annotations(
    slug: str, all: bool = Query(False), file: str | None = Query(None)
):
    items = [a for a in _load_annotations() if a["slug"] == slug]
    if file is not None:
        items = [a for a in items if _anno_file(a) == file]
    if not all:
        items = [a for a in items if not a.get("resolved")]
    items.sort(key=lambda a: a.get("created_at", ""))
    return {"slug": slug, "file": file, "annotations": items}


def _notify_blocked(a: dict) -> None:
    msg = (
        f"🚧 Annotation blocked — needs your input:\n\n"
        f"Article: {a['slug']}\n"
        f"Text: {a.get('highlighted_text', '')}\n"
        f"Comment: {a.get('comment', '')}\n"
        f"Reason: {a.get('blocked_reason', '')}"
    )
    payload = json.dumps({"message": msg, "target": "discord"})
    try:
        subprocess.run(
            ["curl", "-s", "-X", "POST", "http://localhost:8765/send",
             "-H", "Content-Type: application/json",
             "-d", payload],
            timeout=5,
        )
    except Exception as e:
        print(f"Discord notify failed: {e}")


@app.patch("/annotations/{annotation_id}")
def update_annotation(annotation_id: str, patch: AnnotationPatch):
    items = _load_annotations()
    for a in items:
        if a["id"] == annotation_id:
            if patch.blocked_reason is not None:
                a["blocked"] = True
                a["blocked_reason"] = patch.blocked_reason
                a["resolved"] = False
                _save_annotations(items)
                _notify_blocked(a)
                return a
            if patch.resolved and patch.proof is None:
                raise HTTPException(
                    400,
                    "proof required when marking resolved: pass a verbatim quote from the article showing the edited passage in context",
                )
            a["resolved"] = patch.resolved
            a["resolved_at"] = (
                datetime.now(timezone.utc).isoformat() if patch.resolved else None
            )
            if patch.resolved:
                a["proof"] = patch.proof
            _save_annotations(items)
            return a
    raise HTTPException(404, f"No annotation with id '{annotation_id}'")


@app.get("/healthz")
def healthz():
    n_posts = sum(1 for _ in DRAFTS_DIR.glob("*/article.md"))
    n_guides = sum(1 for _ in GUIDES_DIR.glob("*/overview.md")) if GUIDES_DIR.exists() else 0
    all_annos = _load_annotations()
    blocked = [a for a in all_annos if a.get("blocked")]
    unresolved = [a for a in all_annos if not a.get("resolved") and not a.get("blocked")]
    per_slug: dict[str, int] = {}
    for a in unresolved:
        per_slug[a["slug"]] = per_slug.get(a["slug"], 0) + 1
    n_backups = len(list(BACKUP_DIR.glob("annotations_*.json"))) if BACKUP_DIR.exists() else 0
    return JSONResponse({
        "ok": True,
        "posts": n_posts,
        "guides": n_guides,
        "annotations_total": len(all_annos),
        "annotations_unresolved": len(unresolved),
        "annotations_blocked": len(blocked),
        "unresolved_by_slug": per_slug,
        "backups": n_backups,
        "annotations_path": str(ANNOTATIONS_PATH),
    })
