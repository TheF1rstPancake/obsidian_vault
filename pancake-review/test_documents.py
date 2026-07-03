"""Lightweight verification for the document registry / hub adapter.

No pytest / httpx dependency — run directly:

    uv run python test_documents.py

It builds a throwaway hub tree in a temp dir, points ``PANCAKE_HUB_ROOT`` at
it, and checks listing, id round-trip, traversal guards, direct writes, and
the main app's route/local-write wiring.
"""
from __future__ import annotations

import importlib
import os
import sys
import tempfile
from pathlib import Path

FINDING = """\
---
title:   Codex + Cursor PR Orchestration
slug:    codex-cursor-pr-orchestration
project: shared
type:    finding
status:  final
updated: 2026-07-03 09:35
summary: |
  A PR-first workflow is a durable orchestration model.
---
# Finding
Body text.
"""

PROJECT_DOC = """\
---
title:  Firecrawl Setup
project: obsidian-vault
type:    doc
status:  living
updated: 2026-06-15
---
# Setup
Living doc.
"""

NO_FRONTMATTER = "# Bare markdown\n\nNo frontmatter here.\n"


def _build_hub(root: Path) -> None:
    shared = root / "shared" / "findings"
    shared.mkdir(parents=True)
    (shared / "2026-07-03-codex-cursor-pr-orchestration.md").write_text(FINDING)
    proj = root / "projects" / "obsidian-vault" / "docs"
    proj.mkdir(parents=True)
    (proj / "firecrawl-setup.md").write_text(PROJECT_DOC)
    bare = root / "projects" / "cliphouse" / "reports"
    bare.mkdir(parents=True)
    (bare / "2026-06-14-bare.md").write_text(NO_FRONTMATTER)
    # A file outside browsable areas — must be ignored by the listing.
    (root / "INDEX.md").write_text("# not browsable\n")


def main() -> int:
    tmp = tempfile.mkdtemp(prefix="pancake-hub-test-")
    root = Path(tmp)
    _build_hub(root)
    os.environ["PANCAKE_HUB_ROOT"] = tmp

    # Fresh import so HUB_ROOT picks up the env override.
    for mod in ("documents", "main"):
        sys.modules.pop(mod, None)
    documents = importlib.import_module("documents")

    failures: list[str] = []

    def check(cond: bool, msg: str) -> None:
        if not cond:
            failures.append(msg)

    docs = documents.list_hub_documents()
    by_id = {d["doc_id"]: d for d in docs}

    check(len(docs) == 3, f"expected 3 hub docs, got {len(docs)}")

    fid = "hub:shared/findings/2026-07-03-codex-cursor-pr-orchestration.md"
    check(fid in by_id, f"finding doc_id missing: got {list(by_id)}")
    if fid in by_id:
        f = by_id[fid]
        check(f["kind"] == "hub_finding", f"finding kind: {f['kind']}")
        check(f["project"] == "shared", f"finding project: {f['project']}")
        check(f["status"] == "final", f"finding status: {f['status']}")
        check(f["title"] == "Codex + Cursor PR Orchestration", f"title: {f['title']}")

    did = "hub:projects/obsidian-vault/docs/firecrawl-setup.md"
    if did in by_id:
        d = by_id[did]
        check(d["kind"] == "hub_doc", f"doc kind: {d['kind']}")
        check(d["project"] == "obsidian-vault", f"doc project: {d['project']}")

    # No-frontmatter file: kind derived from folder, project from path.
    bid = "hub:projects/cliphouse/reports/2026-06-14-bare.md"
    if bid in by_id:
        b = by_id[bid]
        check(b["kind"] == "hub_report", f"bare kind: {b['kind']}")
        check(b["project"] == "cliphouse", f"bare project: {b['project']}")
        check(b["title"] == "2026-06-14-bare", f"bare title fallback: {b['title']}")

    # doc_id round-trip resolves back to the file.
    if fid in by_id:
        resolved = documents.resolve_hub_path(fid)
        check(resolved.is_file(), "resolve_hub_path did not return a real file")
        check(documents.hub_doc_id(resolved) == fid, "doc_id round-trip mismatch")

    # Path-traversal / out-of-bounds guards.
    for bad in (
        "hub:../etc/passwd",
        "hub:shared/../../etc/passwd",
        "hub:INDEX.md",              # outside browsable areas
        "hub:shared/findings/x.txt", # not markdown
        "not-a-hub-id",
    ):
        try:
            documents.resolve_hub_path(bad)
            failures.append(f"expected rejection for {bad!r}")
        except (ValueError, FileNotFoundError):
            pass

    # is_hub_doc_id discriminates article slugs from hub ids.
    check(documents.is_hub_doc_id(fid), "is_hub_doc_id false negative")
    check(not documents.is_hub_doc_id("my-article-slug"), "is_hub_doc_id false positive")

    # get_hub_document returns render-ready content.
    if fid in by_id:
        doc = documents.get_hub_document(fid)
        check("Body text." in doc["content"], "get_hub_document lost body")
        check(doc["title"] == "Codex + Cursor PR Orchestration", "get_hub_document title")

    # Hub edits write the exact raw markdown and cannot create/escape targets.
    edited_hub = FINDING.replace("Body text.", "Edited body.")
    documents.save_hub_document(fid, edited_hub)
    check(documents.resolve_hub_path(fid).read_text() == edited_hub,
          "save_hub_document did not write exact source")
    for bad_id, bad_content in (("hub:../escape.md", "# nope\n"), (fid, " \n")):
        try:
            documents.save_hub_document(bad_id, bad_content)
            failures.append(f"expected save rejection for {bad_id!r}")
        except (ValueError, FileNotFoundError):
            pass

    # ---- main app wiring ------------------------------------------------- #
    main_mod = importlib.import_module("main")
    check(main_mod.app.title == "pancake-review", "app title changed")
    check(main_mod._default_file(fid) == main_mod.HUB_DOC_FILE,
          "hub doc_id should default to the hub file bucket")
    paths = {r.path for r in main_mod.app.routes}
    for expected in (
        "/doc/{doc_id:path}", "/edit/doc/{doc_id:path}",
        "/article/{slug}", "/edit/article/{slug}",
        "/api/documents", "/healthz",
    ):
        check(expected in paths, f"route missing: {expected} (have {sorted(paths)})")

    # Local article/guide writes retain the selected file and reject traversal
    # and empty bodies. Point the module constants at a throwaway vault.
    vault = root / "vault"
    draft = vault / "drafts" / "test-article"
    draft.mkdir(parents=True)
    article_path = draft / "article.md"
    article_path.write_text("---\ntitle: Test\n---\nOriginal.\n")
    guide = vault / "guides" / "test-guide"
    guide.mkdir(parents=True)
    (guide / "overview.md").write_text("---\ntitle: Guide\n---\nOverview.\n")
    content_path = guide / "content.md"
    content_path.write_text("# Content\n\nOriginal content.\n")
    main_mod.DRAFTS_DIR = vault / "drafts"
    main_mod.GUIDES_DIR = vault / "guides"

    article_edit = "---\ntitle: Test\n---\nEdited.\n"
    main_mod._save_local_markdown("test-article", "article", article_edit)
    check(article_path.read_text() == article_edit, "article save wrote wrong target/content")
    guide_edit = "# Content\n\nEdited content.\n"
    main_mod._save_local_markdown("test-guide", "content", guide_edit)
    check(content_path.read_text() == guide_edit, "guide content save wrote wrong target/content")
    check("Overview." in (guide / "overview.md").read_text(),
          "guide content save changed overview")
    for slug, fname, body in (
        ("test-article", "../escape", "# nope\n"),
        ("..", "article", "# nope\n"),
        ("test-article", "article", " \n"),
        ("missing", "article", "# nope\n"),
    ):
        try:
            main_mod._save_local_markdown(slug, fname, body)
            failures.append(f"expected local save rejection for {slug!r}/{fname!r}")
        except main_mod.HTTPException:
            pass

    if failures:
        print("FAIL:")
        for msg in failures:
            print("  -", msg)
        return 1
    print(f"ok — {len(docs)} hub docs, all adapter + wiring checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
