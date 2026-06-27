"""Lightweight wiring tests for article_pipeline.py (no real AI/Ghost calls)."""
import json
from pathlib import Path

import article_pipeline as pipe


def make_vault(tmp_path: Path, slug: str = "my-slug") -> Path:
    (tmp_path / "STYLE.md").write_text("# STYLE\nSTYLE_MARKER_XYZ\n")
    (tmp_path / "SCHEMA.md").write_text("# SCHEMA\n")
    (tmp_path / "CLAUDE.md").write_text("# CLAUDE\n")
    draft = tmp_path / "drafts" / slug
    draft.mkdir(parents=True)
    (draft / "notes.md").write_text("notes body\n")
    (draft / "article.md").write_text("---\ntitle: T\n---\nbody\n")
    (tmp_path / "vault-meta" / "voice-samples").mkdir(parents=True)
    return tmp_path


def test_editor_prompt_loads_style_and_structured_fields(tmp_path):
    vault = make_vault(tmp_path)
    import article_context as ctx
    context_text = ctx.build_context("my-slug", vault_root=vault,
                                     annotations_path=tmp_path / "none.json")
    prompt = pipe.build_editor_prompt(context_text, "my-slug")

    # Loads the style guide content (via the bundled context).
    assert "STYLE_MARKER_XYZ" in prompt
    assert "STYLE.md" in prompt
    # Produces the structured report contract.
    assert "approved | needs_revision" in prompt
    assert "Blocking issues" in prompt
    assert "Revision notes" in prompt
    assert "AI-framing risks" in prompt
    assert "## Scores" in prompt
    # Slug is substituted into the report header instruction.
    assert "Editor report — my-slug" in prompt
    # Must instruct against mutating files.
    assert "not to touch any files" in prompt or "Do not edit files" in prompt


def test_find_ai_cli_returns_none_for_unknown():
    assert pipe.find_ai_cli(["definitely-not-a-real-binary-xyz"]) is None


def test_find_ai_cli_finds_known_binary():
    # `python3`-like always-present binary check via a guaranteed one.
    import shutil
    real = next((n for n in ("sh", "ls", "cat") if shutil.which(n)), None)
    assert real is not None
    assert pipe.find_ai_cli([real]) == real


def test_cli_command_shapes():
    assert pipe._cli_command("claude") == ["claude", "-p"]
    assert pipe._cli_command("clauded") == ["clauded", "-p"]
    assert pipe._cli_command("codex")[:2] == ["codex", "exec"]


def test_cmd_context_writes_file(tmp_path, capsys):
    vault = make_vault(tmp_path)
    out_path = pipe.cmd_context("my-slug", vault_root=vault,
                                annotations_path=tmp_path / "none.json")
    assert out_path.is_file()
    printed = capsys.readouterr().out.strip()
    assert printed == str(out_path)


def test_cmd_edit_dry_run_writes_prompt_not_report(tmp_path, capsys):
    vault = make_vault(tmp_path)
    rc = pipe.cmd_edit("my-slug", vault_root=vault, dry_run=True,
                       annotations_path=tmp_path / "none.json")
    assert rc == 0
    pipeline_dir = vault / "drafts" / "my-slug" / ".pipeline"
    assert (pipeline_dir / "editor-prompt.md").is_file()
    # Dry run must NOT call the AI, so no report is written.
    assert not (pipeline_dir / "editor-report.md").exists()
    out = capsys.readouterr().out
    assert "[dry-run]" in out


def test_cmd_edit_never_mutates_article(tmp_path):
    vault = make_vault(tmp_path)
    article = vault / "drafts" / "my-slug" / "article.md"
    before = article.read_text()
    pipe.cmd_edit("my-slug", vault_root=vault, dry_run=True,
                  annotations_path=tmp_path / "none.json")
    assert article.read_text() == before


def test_cmd_annotations_lists_unresolved(tmp_path, capsys):
    anns = [
        {"id": "open1234", "slug": "my-slug", "highlighted_text": "HL_OPEN",
         "comment": "CMT_OPEN", "resolved": False},
        {"id": "done1234", "slug": "my-slug", "highlighted_text": "HL_DONE",
         "comment": "CMT_DONE", "resolved": True},
    ]
    apath = tmp_path / "annotations.json"
    apath.write_text(json.dumps(anns))
    rc = pipe.cmd_annotations("my-slug", annotations_path=apath)
    assert rc == 0
    out = capsys.readouterr().out
    assert "HL_OPEN" in out
    assert "CMT_OPEN" in out
    assert "HL_DONE" not in out  # resolved excluded
    assert "proof" in out  # guidance present


def test_cmd_annotations_empty(tmp_path, capsys):
    apath = tmp_path / "annotations.json"
    apath.write_text("[]")
    rc = pipe.cmd_annotations("no-such-slug", annotations_path=apath)
    assert rc == 0
    assert "None" in capsys.readouterr().out


def test_parser_requires_command():
    import pytest
    with pytest.raises(SystemExit):
        pipe.build_parser().parse_args([])
