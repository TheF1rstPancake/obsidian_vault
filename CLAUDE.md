# Vault context for Claude

This is a personal writing vault. The pipeline: voice memo on phone → Syncthing to `recordings/` → Whisper transcribes to `transcripts/` → Claude shapes drafts into `drafts/<slug>/article.md` (Substack target) → LinkedIn snippets generated from `ready`/`published` articles.

**Read [SCHEMA.md](./SCHEMA.md) before creating or editing any file under `drafts/`.** It defines the folder layout and frontmatter for `article.md`, `notes.md`, and `linkedin/*.md`. The cron pipeline in `process-recordings.sh` inlines SCHEMA.md into its prompts, so keeping SCHEMA.md current keeps both interactive and automated paths in sync.

## Conventions

- `drafts/<slug>/notes.md` is **append-only**. Never rewrite or summarize it; it's the lossless record of raw transcripts.
- `drafts/<slug>/article.md` is the polished Substack draft. Status field gates the workflow (see SCHEMA.md).
- LinkedIn snippets are derived *from* a near-final article, not written independently.
- Slugs are kebab-case, 2–5 words.

## Roadmap & ideas

Project work, ideas, and bugs are tracked as GitHub Issues in this repo (the `roadmap` skill is the interface). When the user asks "what's next?" or "what were we going to build?", run `gh issue list --label roadmap --state open` before answering. When they say "let's not do this now," file it as a roadmap issue.

## When updating an article

- Bump the `updated:` field in frontmatter.
- Don't lower `status` (raw → shaping → ready → published is one-way absent explicit user instruction).
- Mark unclear sections with `[?]` rather than guessing.
