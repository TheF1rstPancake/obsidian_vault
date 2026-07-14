# Vault context for Claude

This is a personal writing vault. The pipeline: voice memo on phone → Syncthing to `recordings/` → persistent Whisper worker (`scripts/transcribe_worker.py` / `obsidian-transcribe.service`) transcribes to `transcripts/` → cron `process-recordings.sh` enriches into `drafts/<slug>/article.md` (**Ghost** target) → LinkedIn snippets generated from `ready`/`published` articles. See SETUP.md for start/stop/status (`scripts/transcribe-ctl`).

**The publishing target is Ghost** (`thefirstpancake.ghost.io`, local preview at `http://100.119.32.88:2368`). Substack was the original target; treat any lingering `target: substack` / `substack_url:` in older drafts as legacy to migrate. The blog's editorial identity is **The Burnt Pancake** — humility, experiments, frameworks that held until they didn't, not chest-thumping.

**Read [SCHEMA.md](./SCHEMA.md) before creating or editing any file under `drafts/`,** and **[STYLE.md](./STYLE.md) before shaping or editing any `article.md`.** SCHEMA.md defines the folder layout and frontmatter for `article.md`, `notes.md`, and `linkedin/*.md`. STYLE.md is the canonical voice/editing guide (and the spine of the editor pass in `scripts/article_pipeline.py`). The enrichment cron in `process-recordings.sh` inlines SCHEMA.md into its prompts, so keeping SCHEMA.md current keeps both interactive and automated paths in sync. Transcription is a separate persistent worker (not cron).

## Editorial pipeline tooling

Deterministic helpers live in `scripts/` and are wired into the Makefile:

- `make article-context SLUG=<slug>` → build a context bundle (CLAUDE.md + SCHEMA.md + STYLE.md + notes + article + unresolved annotations + voice samples) at `drafts/<slug>/.pipeline/context.md`.
- `make article-edit SLUG=<slug>` → run an editor-only AI pass against STYLE.md and write `drafts/<slug>/.pipeline/editor-report.md`. It never mutates `article.md`.
- `make article-preview SLUG=<slug>` → upload the local Ghost draft and print the preview URL.
- `python3 scripts/article_pipeline.py annotations <slug>` → list unresolved pancake-review annotations and the verify-before-resolve guidance.

## Conventions

- `drafts/<slug>/notes.md` is **append-only**. Never rewrite or summarize it; it's the lossless record of raw transcripts.
- `drafts/<slug>/article.md` is the polished Ghost draft. Status field gates the workflow (see SCHEMA.md).
- LinkedIn snippets are derived *from* a near-final article, not written independently.
- Slugs are kebab-case, 2–5 words.

## Writing principles

Default to including **tactical artifacts a reader can steal** — decision matrices, checklists, question banks, frameworks, before/after examples. The reframe earns attention; the artifact earns the share. Don't strip a tactical section just to make a piece feel punchier or more contrarian — if both fit, include both. Pure-thesis pieces are fine when the article genuinely is about the idea (e.g. a short opinion essay), but if you find yourself cutting tactical content to sound smarter, that's the wrong instinct.

**Typed callouts are available** for asides, notes, and tactical artifacts you want set off from the prose — author them as `> [!note]` / `> [!tip]` / `> [!warning]` blockquotes (the publish step renders them as styled callouts). See SCHEMA.md → Callouts for syntax and types. Don't hand-write callout HTML.

**Each claim must support itself.** Every statement should be factually grounded or logically derivable from a stated premise. Avoid editorialized sweeping assertions ("most teams enormously underinvest", "this is where X really earns its keep", "that part doesn't get taught anywhere"). Replace with conditional logic the reader can follow: "If a team does X without Y, the result tends to be Z." The article's authority comes from the reader being able to *follow the logic chain*, not from the writer asserting confidence. Acknowledge that conclusions are intuitive given the framework, not the only valid ones.

## External sources

When the user asks for outside takes on an article, or drops a URL with framing like "is this relevant?", use the `sources` skill. It stages source files under `drafts/<slug>/sources/` — never inserts them into `article.md`. The user decides what to riff on. Each source has structured frontmatter (url, author, stance, relevance) plus a "My notes" section left blank for the user to fill in.

## Roadmap & ideas

Project work, ideas, and bugs are tracked as GitHub Issues in this repo (the `roadmap` skill is the interface). When the user asks "what's next?" or "what were we going to build?", run `gh issue list --label roadmap --state open` before answering. When they say "let's not do this now," file it as a roadmap issue.

## When updating an article

- Bump the `updated:` field in frontmatter.
- Don't lower `status` (raw → shaping → ready → published is one-way absent explicit user instruction).
- Mark unclear sections with `[?]` rather than guessing.
- Populate the `point:` field once the article's argument is clear (typically at `shaping` or later, and required for articles >1500 words). See SCHEMA.md for format. This is the source of truth for the article's compressed summary — used by templates, the publish pipeline, LinkedIn snippet generation, etc. Don't render it as a body callout; the publish step does that.
