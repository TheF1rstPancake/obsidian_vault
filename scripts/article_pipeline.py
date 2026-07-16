#!/usr/bin/env python3
"""Editorial pipeline driver for the Ghost blog.

Commands:
    context <slug>      Build the context bundle (-> drafts/<slug>/.pipeline/context.md).
    edit <slug>         Run an editor-only AI pass against STYLE.md and write
                        drafts/<slug>/.pipeline/editor-report.md. Never mutates article.md.
    preview <slug>      Upload the local Ghost draft via ghost-upload.py --draft and print the URL.
    annotations <slug>  Print unresolved pancake-review annotations + verify-before-resolve guidance.

Examples:
    python3 scripts/article_pipeline.py context evaluating-judgement
    python3 scripts/article_pipeline.py edit evaluating-judgement --dry-run
    python3 scripts/article_pipeline.py preview evaluating-judgement
    python3 scripts/article_pipeline.py annotations evaluating-judgement

Stdlib only. The `edit` pass shells out to the first available AI CLI
(claude, then clauded, then codex). Use --dry-run to generate the prompt
without calling the model.
"""
from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

import article_context as ctx

VAULT_ROOT = ctx.VAULT_ROOT

# AI CLIs to try, in order. Each entry: (name, argv-builder) where the builder
# returns the command list; the full prompt is always fed on stdin.
AI_CLIS = ["claude", "clauded", "codex"]


# --------------------------------------------------------------------------
# Editor prompt
# --------------------------------------------------------------------------
EDITOR_INSTRUCTIONS = """\
You are the Editor for Giovanni's blog, **The Burnt Pancake**. Your job is to
critique the current draft — not to rewrite it, and not to touch any files.

The context bundle below contains, in order: the lossless source notes, the
current draft, the open and resolved pancake-review annotations, the STYLE.md
voice guide, the schema, vault conventions, and voice samples. STYLE.md is the
rubric. The annotations are direct instructions from Giovanni and override
generic advice.

Editorial priorities (from STYLE.md and Giovanni's recurring corrections):
- Cut framing, headings, or sections that do not advance the argument.
- Cut interstitial lead-ins and bland transitions ("There's a sharper version…",
  "Start with the assumption underneath…", "in retrospect, a case study…").
  Prefer the direct claim or "We saw this at X."
- Prefer concrete claims over generic scaffolding; delete hedging that restates
  the obvious without naming the thing.
- Flag remakes: if a section already landed a point, a punchier restatement
  later is a cut, not emphasis.
- Reject AI-invented ceremony (revision histories, logs, official-looking process).
- Preserve the real conceptual hierarchy; do not synonym-swap load-bearing terms.
- When two products/systems are in play (e.g. customer-facing paid product vs
  internal SE-owned brain/platform), flag bare "the product" / mushy referents
  as blocking; each needs a short defined name used consistently.
- Prefer conditional/situational claims over universal doctrine. Do not drop
  load-bearing if-clauses ("if you've built a well-defined useful X…").
- Keep concrete, weird analogies; do not sand them into generic business prose.
- Reduce em dashes; staccato is fine. No "it's not X, it's Y".
- Vulnerability should be clinical, not confessional.
- No fabricated authority (fake experts/studies/stats) and no leaked meta-commentary.
- The close must wrap (one new check/inversion), not re-litigate earlier sections.
- Publish from stable observations, not final beliefs. Flag trying-to-be-final
  sprawl: mega-scope, endless flesh-out on already-long drafts, or holding a
  piece because the writer's model might update. Prefer "useful enough to ship"
  (core point real, claims not stronger than evidence) over waiting for doctrine.
- Prefer one clear lens over a bloated total theory. If essay arc and full
  playbook are both load-bearing, flag thought+playbook cram and recommend a
  companion split — stealable artifacts stay; rival operating manuals move out.
- New nuance that only softens or extends the claim should become the next post
  or companion, not a reason to suppress or endlessly rewrite the current piece.

Output a single Markdown report and NOTHING else. Do not edit files. Do not
print the draft back. Use exactly this structure:

# Editor report — {slug}

**Status:** approved | needs_revision

## Scores (1-5)
- Conceptual fidelity: N — one line of justification
- Voice & AI tells: N — one line
- Conditionality (no over-claiming): N — one line
- Structure (every section earns its place): N — one line
- Tactical/concrete specificity: N — one line

## Blocking issues
For each, quote the offending text verbatim and say what is wrong and the fix.
If none, write "None."

## Revision notes
Narrow, actionable notes the writer can apply. Tie each to STYLE.md or an
annotation where possible. Do not rewrite whole sections.

## AI-framing risks
Specific tells you found (em dashes, invented ceremony, fabricated authority,
"it's not X it's Y", doctrine, meta-commentary). Quote them. If clean, say so.

## Open annotations
For each unresolved annotation, state whether the current draft already
addresses it and, if not, what is needed. Do NOT mark anything resolved — that
requires verified proof and is out of scope for this pass.
"""


def build_editor_prompt(context_text: str, slug: str) -> str:
    """Compose the full editor prompt. Pure function (testable)."""
    instructions = EDITOR_INSTRUCTIONS.replace("{slug}", slug)
    return (
        instructions
        + "\n\n---\n\n# CONTEXT BUNDLE\n\n"
        + context_text
    )


# --------------------------------------------------------------------------
# AI CLI discovery / invocation
# --------------------------------------------------------------------------
def find_ai_cli(candidates: list[str] | None = None) -> str | None:
    """Return the first available AI CLI name on PATH, or None."""
    for name in candidates or AI_CLIS:
        if shutil.which(name):
            return name
    return None


def _cli_command(name: str) -> list[str]:
    """Argv for a CLI that takes its prompt on stdin and prints to stdout."""
    if name in ("claude", "clauded"):
        # Headless print mode: reads the prompt from stdin, prints the result.
        return [name, "-p"]
    if name == "codex":
        # codex exec runs non-interactively; "-" reads the prompt from stdin.
        return [name, "exec", "-"]
    return [name]


def run_editor(prompt: str, cli: str, timeout: int = 900) -> tuple[bool, str]:
    """Run the editor pass through `cli`. Returns (ok, output_or_error)."""
    cmd = _cli_command(cli)
    try:
        proc = subprocess.run(
            cmd,
            input=prompt,
            capture_output=True,
            text=True,
            timeout=timeout,
            cwd=str(VAULT_ROOT),
        )
    except FileNotFoundError:
        return False, f"AI CLI '{cli}' not found on PATH."
    except subprocess.TimeoutExpired:
        return False, f"AI CLI '{cli}' timed out after {timeout}s."
    if proc.returncode != 0:
        return False, f"AI CLI '{cli}' exited {proc.returncode}.\nstderr:\n{proc.stderr.strip()}"
    out = proc.stdout.strip()
    if not out:
        return False, f"AI CLI '{cli}' produced no output.\nstderr:\n{proc.stderr.strip()}"
    return True, out


# --------------------------------------------------------------------------
# Commands
# --------------------------------------------------------------------------
def cmd_context(slug: str, vault_root: Path = VAULT_ROOT, output: str | None = None,
                annotations_path: str | None = None) -> Path:
    out_path = ctx.write_context(
        slug, output=output, vault_root=vault_root, annotations_path=annotations_path
    )
    print(str(out_path))
    return out_path


def cmd_edit(slug: str, vault_root: Path = VAULT_ROOT, dry_run: bool = False,
             annotations_path: str | None = None) -> int:
    pipeline_dir = Path(vault_root) / "drafts" / slug / ".pipeline"
    # Always (re)build context so the editor sees the current draft + annotations.
    context_path = ctx.write_context(slug, vault_root=vault_root, annotations_path=annotations_path)
    context_text = context_path.read_text(encoding="utf-8")
    prompt = build_editor_prompt(context_text, slug)

    pipeline_dir.mkdir(parents=True, exist_ok=True)
    prompt_path = pipeline_dir / "editor-prompt.md"
    prompt_path.write_text(prompt, encoding="utf-8")

    if dry_run:
        cli = find_ai_cli() or "(none found)"
        print(f"[dry-run] context: {context_path}")
        print(f"[dry-run] prompt:  {prompt_path} ({len(prompt)} chars)")
        print(f"[dry-run] would run AI CLI: {cli}")
        print(f"[dry-run] would write report: {pipeline_dir / 'editor-report.md'}")
        return 0

    cli = find_ai_cli()
    if not cli:
        print(
            "error: no AI CLI found (looked for claude, clauded, codex).\n"
            f"The editor prompt was written to {prompt_path} — run it manually,\n"
            "or re-run with --dry-run.",
            file=sys.stderr,
        )
        return 1

    print(f"running editor pass via '{cli}' (this can take a minute)...", file=sys.stderr)
    ok, output = run_editor(prompt, cli)
    if not ok:
        print(f"error: {output}", file=sys.stderr)
        print(f"the prompt is saved at {prompt_path} — you can run it manually.", file=sys.stderr)
        return 1

    report_path = pipeline_dir / "editor-report.md"
    report_path.write_text(output + "\n", encoding="utf-8")
    print(str(report_path))
    return 0


def cmd_preview(slug: str, vault_root: Path = VAULT_ROOT, dry_run: bool = False) -> int:
    article = Path(vault_root) / "drafts" / slug / "article.md"
    if not article.is_file():
        print(f"error: {article} not found", file=sys.stderr)
        return 1
    cmd = [sys.executable, "ghost-upload.py", str(article.relative_to(vault_root)),
           "--draft", "--target", "local"]
    if dry_run:
        cmd.append("--dry-run")
    print("running:", " ".join(cmd), file=sys.stderr)
    proc = subprocess.run(cmd, cwd=str(vault_root))
    return proc.returncode


# Annotation guidance. Full resolution (editing article.md + PATCHing the
# pancake-review server with proof) is deliberately NOT automated here: it is
# the highest-risk path (10/29 annotations were once marked resolved without the
# edit landing), and the verify-before-resolve rule must be enforced by a human
# or a careful interactive agent. This command surfaces the work; it does not
# fake it.
ANNOTATION_GUIDANCE = """\
To resolve these (interactive / careful agent only):
  1. Apply each edit to drafts/{slug}/article.md.
  2. Re-read the edited section and confirm the change landed.
  3. PATCH localhost:4242/annotations/<id> with resolved:true AND a `proof`
     field quoting the changed text. The server rejects resolve-without-proof.
  4. If an instruction is unclear, PATCH with `blocked_reason` instead of
     skipping — G is fine being asked questions.
TODO: a `--resolve` path that automates 1-3 with the proof rule is intentionally
not implemented in this first pass; doing it without verification is the exact
failure mode the proof rule exists to prevent.
"""


def cmd_annotations(slug: str, annotations_path: str | None = None) -> int:
    annotations = ctx.load_annotations(annotations_path)
    open_anns = ctx.filter_annotations(annotations, slug, resolved=False)
    print(f"# Unresolved annotations for '{slug}': {len(open_anns)}\n")
    if not open_anns:
        print("None. Nothing to resolve (or annotations were never created — "
              "check the pancake-review server before assuming).")
        return 0
    for a in open_anns:
        highlighted, comment = ctx.annotation_fields(a)
        anno_id = str(a.get("id", ""))[:8]
        print(f"[{anno_id}] on {highlighted!r}")
        print(f"        wants: {comment}")
        if a.get("blocked_reason"):
            print(f"        blocked: {a['blocked_reason']}")
        print()
    print(ANNOTATION_GUIDANCE.replace("{slug}", slug))
    return 0


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------
def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Editorial pipeline driver", formatter_class=argparse.RawDescriptionHelpFormatter
    )
    sub = parser.add_subparsers(dest="command", required=True)

    p_ctx = sub.add_parser("context", help="build the context bundle")
    p_ctx.add_argument("slug")
    p_ctx.add_argument("--output", "-o", default=None)

    p_edit = sub.add_parser("edit", help="run an editor-only AI pass")
    p_edit.add_argument("slug")
    p_edit.add_argument("--dry-run", action="store_true", help="write the prompt, don't call the AI")

    p_prev = sub.add_parser("preview", help="upload local Ghost draft")
    p_prev.add_argument("slug")
    p_prev.add_argument("--dry-run", action="store_true", help="parse frontmatter only, don't publish")

    p_ann = sub.add_parser("annotations", help="list unresolved annotations")
    p_ann.add_argument("slug")

    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.command == "context":
        cmd_context(args.slug, output=args.output)
        return 0
    if args.command == "edit":
        return cmd_edit(args.slug, dry_run=args.dry_run)
    if args.command == "preview":
        return cmd_preview(args.slug, dry_run=args.dry_run)
    if args.command == "annotations":
        return cmd_annotations(args.slug)
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
