"""pancake-review — a local article annotation tool.

Pulls articles from the local Ghost instance, renders them in a clean,
mobile-friendly reader view, and lets you highlight text + leave notes.
Annotations are stored in ~/.hermes/annotations.json so that Hermes can
fetch unresolved ones, edit the markdown source, re-push to Ghost, and
mark them resolved.

Ghost auth note
---------------
The local Ghost instance only exposes an **Admin API key** (id:secret),
stored in ~/obsidian-vault/.env as GHOST_LOCAL_API_KEY. There is no
separate Content API key in this setup, so we authenticate every read
with a short-lived JWT against the Admin API — exactly like the sibling
ghost-upload.py script. Ghost listens on the Tailscale IP, not localhost,
so the default base URL is http://100.119.32.88:2368 (override with the
GHOST_LOCAL_URL env var).

Run:
    uv run uvicorn main:app --host 0.0.0.0 --port 4242 --reload
"""
from __future__ import annotations

import json
import os
import time
import uuid
from datetime import datetime, timezone
from pathlib import Path

import httpx
import jwt as pyjwt
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

GHOST_URL = os.environ.get("GHOST_LOCAL_URL", "http://100.119.32.88:2368").rstrip("/")
GHOST_KEY = os.environ.get("GHOST_LOCAL_API_KEY", "")

ANNOTATIONS_PATH = Path(
    os.environ.get("PANCAKE_ANNOTATIONS", str(Path.home() / ".hermes" / "annotations.json"))
)
DRAFTS_DIR = VAULT_ROOT / "drafts"

templates = Jinja2Templates(directory=str(HERE / "templates"))
app = FastAPI(title="pancake-review")


# --------------------------------------------------------------------------- #
# Ghost Admin API (JWT auth)
# --------------------------------------------------------------------------- #
def _admin_token() -> str:
    if ":" not in GHOST_KEY:
        raise HTTPException(
            500,
            "GHOST_LOCAL_API_KEY missing or not in id:secret form. "
            "Check ~/obsidian-vault/.env.",
        )
    kid, secret = GHOST_KEY.split(":", 1)
    now = int(time.time())
    return pyjwt.encode(
        {"iat": now, "exp": now + 300, "aud": "/admin/"},
        bytes.fromhex(secret),
        algorithm="HS256",
        headers={"kid": kid},
    )


def _ghost_get(path: str, params: dict | None = None) -> dict:
    headers = {"Authorization": f"Ghost {_admin_token()}", "Accept-Version": "v5.0"}
    try:
        with httpx.Client(timeout=15) as client:
            r = client.get(f"{GHOST_URL}{path}", params=params, headers=headers)
    except httpx.HTTPError as e:
        raise HTTPException(502, f"Cannot reach Ghost at {GHOST_URL}: {e}")
    if r.status_code != 200:
        raise HTTPException(r.status_code, f"Ghost {path} -> {r.status_code}: {r.text[:300]}")
    return r.json()


def list_articles() -> list[dict]:
    """All posts (any status), newest first, with the fields the UI needs."""
    data = _ghost_get(
        "/ghost/api/admin/posts/",
        {
            "limit": "all",
            "order": "updated_at desc",
            "fields": "id,slug,title,status,updated_at,published_at,excerpt,reading_time",
        },
    )
    return data.get("posts", [])


def get_article(slug: str) -> dict:
    data = _ghost_get(f"/ghost/api/admin/posts/slug/{slug}/", {"formats": "html"})
    posts = data.get("posts") or []
    if not posts:
        raise HTTPException(404, f"No Ghost article with slug '{slug}'")
    return posts[0]


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
    articles = list_articles()
    counts = _unresolved_counts()
    for a in articles:
        a["unresolved"] = counts.get(a["slug"], 0)
    return templates.TemplateResponse(
        request, "index.html", {"articles": articles}
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
    try:
        n = len(list_articles())
        return JSONResponse({"ok": True, "ghost": GHOST_URL, "articles": n})
    except HTTPException as e:
        return JSONResponse({"ok": False, "ghost": GHOST_URL, "error": e.detail}, status_code=502)
