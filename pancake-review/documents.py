"""Document registry / adapters for pancake-review.

Pancake Review started as an article-only reviewer (Ghost drafts under
``drafts/*/article.md``).  This module widens it into a general local
*document* review console: alongside article drafts it can browse and open
durable documents from the Hermes hub (``~/hermes-hub``) — findings, reports,
and living docs that shape future project decisions.

The concept is a small **registry of adapters**.  Each adapter knows how to:

* ``list_*`` — enumerate documents of one kind as plain dicts, and
* resolve a stable ``doc_id`` back to a concrete file on disk for rendering.

Every document exposes the same stable fields so the UI and annotation store
can treat them uniformly::

    doc_id   stable, unambiguous id (also used as the annotation ``slug``)
    kind     article | hub_finding | hub_report | hub_doc | markdown
    title    human-readable title
    path     absolute path on disk
    project  registry slug / "shared" when derivable, else ""
    status   lifecycle status when present in frontmatter, else ""

Article ``doc_id`` values stay equal to the existing folder slug (so old
annotations keep matching).  Hub documents use a ``hub:<relpath>`` convention,
e.g. ``hub:shared/findings/2026-07-03-codex-cursor-pr-orchestration.md`` — the
relative path is unique within the hub and never collides with an article slug.

Hub files can also be directly edited, but only after resolving through the
same existing-file and in-bounds guards used for reads.
"""
from __future__ import annotations

import os
from pathlib import Path

import frontmatter

# --------------------------------------------------------------------------- #
# Config
# --------------------------------------------------------------------------- #
HUB_ROOT = Path(os.environ.get("PANCAKE_HUB_ROOT", "/home/giovanni/hermes-hub")).resolve()

# Only these top-level areas of the hub are browsable / reviewable.
HUB_AREAS = ("shared", "projects")

HUB_PREFIX = "hub:"

# hermes-hub frontmatter `type:` -> pancake `kind`.
_HUB_TYPE_TO_KIND = {
    "finding": "hub_finding",
    "report": "hub_report",
    "doc": "hub_doc",
}
# folder name -> pancake `kind`, used when frontmatter `type:` is missing.
_HUB_DIR_TO_KIND = {
    "findings": "hub_finding",
    "reports": "hub_report",
    "docs": "hub_doc",
}


# --------------------------------------------------------------------------- #
# doc_id helpers
# --------------------------------------------------------------------------- #
def is_hub_doc_id(doc_id: str) -> bool:
    """True if ``doc_id`` addresses a hub document (vs. a legacy article slug)."""
    return doc_id.startswith(HUB_PREFIX)


def hub_doc_id(path: Path) -> str:
    """Stable ``hub:<relpath>`` id for a file inside the hub."""
    rel = path.resolve().relative_to(HUB_ROOT)
    return HUB_PREFIX + rel.as_posix()


def resolve_hub_path(doc_id: str) -> Path:
    """Map a hub ``doc_id`` back to a concrete, in-bounds markdown file.

    Guards against path traversal and restricts reads to markdown files under
    the allowed hub areas.  Raises ``ValueError`` / ``FileNotFoundError`` for
    anything invalid so callers can turn it into a 400/404.
    """
    if not is_hub_doc_id(doc_id):
        raise ValueError(f"not a hub doc_id: {doc_id!r}")
    rel = doc_id[len(HUB_PREFIX):]
    target = (HUB_ROOT / rel).resolve()

    # Must stay inside the hub root (no ../ escapes).
    if target != HUB_ROOT and HUB_ROOT not in target.parents:
        raise ValueError(f"path escapes hub root: {doc_id!r}")

    rel_parts = target.relative_to(HUB_ROOT).parts
    if not rel_parts or rel_parts[0] not in HUB_AREAS:
        raise ValueError(f"path outside browsable hub areas: {doc_id!r}")
    if target.suffix != ".md":
        raise ValueError(f"not a markdown document: {doc_id!r}")
    if not target.is_file():
        raise FileNotFoundError(f"no hub document at {doc_id!r}")
    return target


# --------------------------------------------------------------------------- #
# Hub adapter
# --------------------------------------------------------------------------- #
def _hub_project(path: Path, meta: dict) -> str:
    """Derive the project association for a hub file.

    Frontmatter ``project:`` is canonical per the hub SCHEMA; fall back to the
    path (``projects/<slug>/...`` -> ``<slug>``, anything under ``shared/`` ->
    ``shared``).
    """
    proj = meta.get("project")
    if proj:
        return str(proj)
    parts = path.relative_to(HUB_ROOT).parts
    if parts and parts[0] == "projects" and len(parts) > 1:
        return parts[1]
    if parts and parts[0] == "shared":
        return "shared"
    return ""


def _hub_kind(path: Path, meta: dict) -> str:
    """Classify a hub file as finding / report / doc, else generic markdown."""
    t = str(meta.get("type", "")).lower()
    if t in _HUB_TYPE_TO_KIND:
        return _HUB_TYPE_TO_KIND[t]
    # Fall back to the containing folder name (findings/reports/docs).
    for part in path.relative_to(HUB_ROOT).parts:
        if part in _HUB_DIR_TO_KIND:
            return _HUB_DIR_TO_KIND[part]
    return "markdown"


def list_hub_documents() -> list[dict]:
    """Enumerate reviewable hub documents under ``shared/`` and ``projects/``."""
    docs: list[dict] = []
    if not HUB_ROOT.exists():
        return docs
    for area in HUB_AREAS:
        area_dir = HUB_ROOT / area
        if not area_dir.is_dir():
            continue
        for path in sorted(area_dir.rglob("*.md")):
            if not path.is_file():
                continue
            try:
                post = frontmatter.load(str(path))
            except Exception:
                continue
            meta = post.metadata
            updated = meta.get("updated") or meta.get("created") or ""
            docs.append({
                "doc_id": hub_doc_id(path),
                "slug": hub_doc_id(path),  # annotation store keys on this
                "kind": _hub_kind(path, meta),
                "title": meta.get("title") or path.stem,
                "path": str(path),
                "project": _hub_project(path, meta),
                "status": str(meta.get("status", "")),
                "updated": str(updated),
                "summary": str(meta.get("summary", "") or "").strip(),
                "unresolved": 0,  # filled in by the index route
            })
    docs.sort(key=lambda d: d["updated"], reverse=True)
    return docs


def get_hub_document(doc_id: str) -> dict:
    """Load + parse a hub document for rendering.  Renders via ``render`` fn.

    Returns a dict shaped like the article template's ``post`` object so the
    existing reader/annotation UI can display it unchanged.  ``render`` is the
    markdown->HTML function passed in by the caller (kept here to avoid a hard
    dependency on main's renderer).
    """
    path = resolve_hub_path(doc_id)
    post = frontmatter.load(str(path))
    meta = post.metadata
    return {
        "doc_id": doc_id,
        "path": path,
        "content": post.content,
        "title": meta.get("title") or path.stem,
        "kind": _hub_kind(path, meta),
        "project": _hub_project(path, meta),
        "status": str(meta.get("status", "")),
    }


def save_hub_document(doc_id: str, content: str) -> Path:
    """Write ``content`` to a hub markdown file identified by ``doc_id``.

    Reuses ``resolve_hub_path`` for all path-traversal and in-bounds guards —
    the same restrictions that apply to reads apply to writes.  Raises
    ``ValueError`` for empty content or an invalid ``doc_id``, and
    ``FileNotFoundError`` if the document does not already exist (creates are
    not supported; only edits to files already browsable by the app).
    """
    if not content.strip():
        raise ValueError("content must not be empty")
    path = resolve_hub_path(doc_id)
    path.write_text(content, encoding="utf-8")
    return path
