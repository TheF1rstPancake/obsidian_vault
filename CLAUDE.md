# Vault context for Claude

This is a personal writing vault. The pipeline: voice memo on phone → Syncthing to `recordings/` → Whisper transcribes to `transcripts/` → Claude shapes drafts into `drafts/<slug>/article.md` (Substack target) → LinkedIn snippets generated from `ready`/`published` articles.

**Read [SCHEMA.md](./SCHEMA.md) before creating or editing any file under `drafts/`.** It defines the folder layout and frontmatter for `article.md`, `notes.md`, and `linkedin/*.md`. The cron pipeline in `process-recordings.sh` inlines SCHEMA.md into its prompts, so keeping SCHEMA.md current keeps both interactive and automated paths in sync.

## Conventions

- `drafts/<slug>/notes.md` is **append-only**. Never rewrite or summarize it; it's the lossless record of raw transcripts.
- `drafts/<slug>/article.md` is the polished Substack draft. Status field gates the workflow (see SCHEMA.md).
- LinkedIn snippets are derived *from* a near-final article, not written independently.
- Slugs are kebab-case, 2–5 words.

## Writing principles

Default to including **tactical artifacts a reader can steal** — decision matrices, checklists, question banks, frameworks, before/after examples. The reframe earns attention; the artifact earns the share. Don't strip a tactical section just to make a piece feel punchier or more contrarian — if both fit, include both. Pure-thesis pieces are fine when the article genuinely is about the idea (e.g. a short opinion essay), but if you find yourself cutting tactical content to sound smarter, that's the wrong instinct.

**Each claim must support itself.** Every statement should be factually grounded or logically derivable from a stated premise. Avoid editorialized sweeping assertions ("most teams enormously underinvest", "this is where X really earns its keep", "that part doesn't get taught anywhere"). Replace with conditional logic the reader can follow: "If a team does X without Y, the result tends to be Z." The article's authority comes from the reader being able to *follow the logic chain*, not from the writer asserting confidence. Acknowledge that conclusions are intuitive given the framework, not the only valid ones.

## External sources

When the user asks for outside takes on an article, or drops a URL with framing like "is this relevant?", use the `sources` skill. It stages source files under `drafts/<slug>/sources/` — never inserts them into `article.md`. The user decides what to riff on. Each source has structured frontmatter (url, author, stance, relevance) plus a "My notes" section left blank for the user to fill in.

## Roadmap & ideas

Project work, ideas, and bugs are tracked as GitHub Issues in this repo (the `roadmap` skill is the interface). When the user asks "what's next?" or "what were we going to build?", run `gh issue list --label roadmap --state open` before answering. When they say "let's not do this now," file it as a roadmap issue.

## When updating an article

- Bump the `updated:` field in frontmatter.
- Don't lower `status` (raw → shaping → ready → published is one-way absent explicit user instruction).
- Mark unclear sections with `[?]` rather than guessing.
