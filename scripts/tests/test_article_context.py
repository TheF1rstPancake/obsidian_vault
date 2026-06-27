"""Tests for article_context.py."""
import json
from pathlib import Path

import article_context as ctx


def make_vault(tmp_path: Path, slug: str = "my-slug") -> Path:
    """Build a minimal fake vault with the files build_context reads."""
    (tmp_path / "STYLE.md").write_text("# STYLE\nReduce em dashes. STYLE_MARKER_XYZ\n")
    (tmp_path / "SCHEMA.md").write_text("# SCHEMA\nSCHEMA_MARKER_XYZ\n")
    (tmp_path / "CLAUDE.md").write_text("# CLAUDE\nCLAUDE_MARKER_XYZ\n")

    draft = tmp_path / "drafts" / slug
    draft.mkdir(parents=True)
    (draft / "notes.md").write_text("---\nslug: my-slug\n---\nNOTES_MARKER_RAW_TRANSCRIPT\n")
    (draft / "article.md").write_text("---\ntitle: T\n---\nARTICLE_MARKER_BODY\n")

    samples = tmp_path / "vault-meta" / "voice-samples"
    samples.mkdir(parents=True)
    (samples / "01-sample.md").write_text("VOICE_SAMPLE_MARKER_ONE\n" + ("x" * 50))
    return tmp_path


def write_annotations(tmp_path: Path, data) -> Path:
    p = tmp_path / "annotations.json"
    p.write_text(json.dumps(data))
    return p


def test_includes_style_md(tmp_path):
    vault = make_vault(tmp_path)
    out = ctx.build_context("my-slug", vault_root=vault, annotations_path=tmp_path / "none.json")
    assert "STYLE_MARKER_XYZ" in out
    assert "STYLE.md" in out


def test_includes_notes_and_article_content(tmp_path):
    vault = make_vault(tmp_path)
    out = ctx.build_context("my-slug", vault_root=vault, annotations_path=tmp_path / "none.json")
    assert "NOTES_MARKER_RAW_TRANSCRIPT" in out
    assert "ARTICLE_MARKER_BODY" in out
    assert "SCHEMA_MARKER_XYZ" in out
    assert "CLAUDE_MARKER_XYZ" in out
    assert "VOICE_SAMPLE_MARKER_ONE" in out


def test_filters_unresolved_annotations_by_slug(tmp_path):
    vault = make_vault(tmp_path)
    anns = [
        {"id": "aaa11111", "slug": "my-slug", "highlighted_text": "HL_MINE",
         "comment": "CMT_MINE", "resolved": False},
        {"id": "bbb22222", "slug": "other-slug", "highlighted_text": "HL_OTHER",
         "comment": "CMT_OTHER", "resolved": False},
        {"id": "ccc33333", "slug": "my-slug", "highlighted_text": "HL_DONE",
         "comment": "CMT_DONE", "resolved": True, "proof": "proven"},
    ]
    apath = write_annotations(tmp_path, anns)
    out = ctx.build_context("my-slug", vault_root=vault, annotations_path=apath)

    # Open annotation for this slug appears in the unresolved section.
    assert "CMT_MINE" in out
    assert "HL_MINE" in out
    # Other slug's annotation must not leak in.
    assert "HL_OTHER" not in out
    assert "CMT_OTHER" not in out
    # Resolved annotation for this slug shows up as a lesson, not unresolved.
    assert "CMT_DONE" in out
    assert "Unresolved annotations (1)" in out
    assert "Resolved annotation lessons (1)" in out


def test_filter_function_directly():
    anns = [
        {"slug": "a", "resolved": False},
        {"slug": "a", "resolved": True},
        {"slug": "b", "resolved": False},
    ]
    assert len(ctx.filter_annotations(anns, "a", resolved=False)) == 1
    assert len(ctx.filter_annotations(anns, "a", resolved=True)) == 1
    assert len(ctx.filter_annotations(anns, "a", resolved=None)) == 2
    assert len(ctx.filter_annotations(anns, "b", resolved=False)) == 1


def test_supports_both_legacy_and_new_field_names():
    new = {"highlighted_text": "NEW_HL", "comment": "NEW_CM"}
    legacy = {"quote": "OLD_HL", "note": "OLD_CM"}
    assert ctx.annotation_fields(new) == ("NEW_HL", "NEW_CM")
    assert ctx.annotation_fields(legacy) == ("OLD_HL", "OLD_CM")


def test_renders_legacy_quote_note_in_bundle(tmp_path):
    vault = make_vault(tmp_path)
    anns = [{"id": "legacy01", "slug": "my-slug", "quote": "LEGACY_HL",
             "note": "LEGACY_NOTE", "resolved": False}]
    apath = write_annotations(tmp_path, anns)
    out = ctx.build_context("my-slug", vault_root=vault, annotations_path=apath)
    assert "LEGACY_HL" in out
    assert "LEGACY_NOTE" in out


def test_no_annotations_file_does_not_crash(tmp_path):
    vault = make_vault(tmp_path)
    missing = tmp_path / "does-not-exist.json"
    out = ctx.build_context("my-slug", vault_root=vault, annotations_path=missing)
    assert "Unresolved annotations (0)" in out
    # And load_annotations returns [] rather than raising.
    assert ctx.load_annotations(missing) == []


def test_malformed_annotations_file_does_not_crash(tmp_path):
    bad = tmp_path / "bad.json"
    bad.write_text("{not valid json")
    assert ctx.load_annotations(bad) == []


def test_missing_draft_files_do_not_crash(tmp_path):
    vault = make_vault(tmp_path)
    out = ctx.build_context("nonexistent-slug", vault_root=vault,
                            annotations_path=tmp_path / "none.json")
    assert "No article.md for this slug yet." in out
    assert "No notes.md for this slug." in out


def test_write_context_creates_pipeline_file(tmp_path):
    vault = make_vault(tmp_path)
    out_path = ctx.write_context("my-slug", vault_root=vault,
                                 annotations_path=tmp_path / "none.json")
    assert out_path == vault / "drafts" / "my-slug" / ".pipeline" / "context.md"
    assert out_path.is_file()
    assert "STYLE_MARKER_XYZ" in out_path.read_text()
