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


def get_article(slug: str) -> dict:
    """Read and render a local post or guide overview by slug.

    Tries drafts/ first, then guides/.
    """
    post_path = DRAFTS_DIR / slug / "article.md"
    guide_path = GUIDES_DIR / slug / "overview.md"

    if post_path.exists():
        path = post_path
    elif guide_path.exists():
        path = guide_path
    else:
        raise HTTPException(404, f"No local file for slug '{slug}'")

    try:
        post = frontmatter.load(str(path))
    except Exception as e:
        raise HTTPException(500, f"Failed to parse {path}: {e}")

    meta = post.metadata
    return {
        "title": meta.get("title", slug),
        "slug": slug,
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


def _save_annotations(items: list[dict]) -> None:
    ANNOTATIONS_PATH.parent.mkdir(parents=True, exist_ok=True)
    tmp = ANNOTATIONS_PATH.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(items, indent=2, ensure_ascii=False))
    tmp.replace(ANNOTATIONS_PATH)  # atomic


class NewAnnotation(BaseModel):
    slug: str
    highlighted_text: str
    comment: str


class AnnotationPatch(BaseModel):
    resolved: bool = True


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
def article(request: Request, slug: str):
    post = get_article(slug)
    return templates.TemplateResponse(
        request, "article.html", {"post": post, "slug": slug}
    )


# --------------------------------------------------------------------------- #
# JSON API
# --------------------------------------------------------------------------- #
@app.get("/api/articles")
def api_articles():
    return {"articles": list_articles()}


def _unresolved_counts() -> dict[str, int]:
    counts: dict[str, int] = {}
    for a in _load_annotations():
        if not a.get("resolved"):
            counts[a["slug"]] = counts.get(a["slug"], 0) + 1
    return counts


@app.post("/annotations")
def create_annotation(body: NewAnnotation):
    text = body.highlighted_text.strip()
    comment = body.comment.strip()
    if not text:
        raise HTTPException(400, "highlighted_text is required")
    if not comment:
        raise HTTPException(400, "comment is required")
    item = {
        "id": uuid.uuid4().hex,
        "slug": body.slug,
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
def list_annotations(slug: str, all: bool = Query(False)):
    items = [a for a in _load_annotations() if a["slug"] == slug]
    if not all:
        items = [a for a in items if not a.get("resolved")]
    items.sort(key=lambda a: a.get("created_at", ""))
    return {"slug": slug, "annotations": items}


@app.patch("/annotations/{annotation_id}")
def update_annotation(annotation_id: str, patch: AnnotationPatch):
    items = _load_annotations()
    for a in items:
        if a["id"] == annotation_id:
            a["resolved"] = patch.resolved
            a["resolved_at"] = (
                datetime.now(timezone.utc).isoformat() if patch.resolved else None
            )
            _save_annotations(items)
            return a
    raise HTTPException(404, f"No annotation with id '{annotation_id}'")


@app.get("/healthz")
def healthz():
    n_posts = sum(1 for _ in DRAFTS_DIR.glob("*/article.md"))
    n_guides = sum(1 for _ in GUIDES_DIR.glob("*/overview.md")) if GUIDES_DIR.exists() else 0
    return JSONResponse({"ok": True, "posts": n_posts, "guides": n_guides})
