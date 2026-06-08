# Vault schema

Source of truth for frontmatter and folder layout. Referenced by CLAUDE.md and inlined into the cron prompts in `process-recordings.sh`. Update this file when the schema changes; both code paths will pick it up.

## Folder layout

```
drafts/<slug>/
  article.md          # the Substack draft (the polished output)
  notes.md            # append-only raw transcripts, timestamped (lossless source)
  linkedin/           # generated LinkedIn snippets, one per file
    01-<short-name>.md
    02-<short-name>.md
```

`<slug>` is kebab-case, 2–5 words, derived from the topic.

## article.md

The Substack draft. Regenerated/refined by Claude as new recordings arrive.

```yaml
---
title: "Working title for the article"
slug: my-article-slug
status: raw          # raw | shaping | ready | published
target: substack
created: 2026-05-07
updated: 2026-05-07
tags: [optional, kebab-case, tags]
point: >            # the compressed argument, ~50–100 words. Required for articles >1500 words; optional below that.
  One-paragraph summary of the article's argument. Use YAML folded
  scalar (>) so newlines fold into spaces. This is the source of
  truth for template renderings — LinkedIn snippets, RSS descriptions,
  site indexes, and the body callout at publish time all derive from
  this field.
substack_url:        # filled in after publishing
---
```

`status` lifecycle:
- **raw** — first transcript landed, draft is unshaped
- **shaping** — actively iterating, multiple transcripts merged
- **ready** — publishable; LinkedIn snippet generation can fire
- **published** — live on Substack; `substack_url` populated

Body is markdown. Use `[?]` to mark unclear sections that need a follow-up recording.

### Callouts (admonitions)

Use **typed callouts** for asides, notes, tips, and tactical artifacts you want set off from the main flow. The syntax is the Obsidian / GitHub "alert" convention — a blockquote whose first line is `[!type]` with an optional title:

```markdown
> [!note] Worth noting
> Body content. Inner markdown works — *emphasis*, [links](…), and:
> - bullets
> - more bullets

> [!tip] Steal this
> A framework / checklist / decision matrix the reader can lift.

> [!warning]
> A caveat or watch-out. Title defaults to "Warning" when omitted.
```

Types (more can be added in the theme + publisher):

- `[!note]` — neutral aside / "worth noting." Teal. For tangents too important to cut but off the main spine.
- `[!tip]` — a technique or **tactical artifact the reader should steal** (framework, matrix, checklist). Maple.
- `[!warning]` — a caveat or failure mode. Brick red.

Text after `[!type]` overrides the title; omit it for the default (Note / Tip / Warning). Aliases: `info`/`example`/`quote` → note; `hint` → tip; `caution`/`danger` → warning.

**Author the syntax, not HTML — rendering is the publish step's job.** `ghost-upload.py` extracts each block, renders its inner markdown, and injects it as a styled callout card. Custom HTML/classes do **not** survive Ghost's markdown→lexical conversion (hand-written `<div>`s get flattened), so always use the `> [!type]` syntax. It also renders natively in Obsidian and degrades to a plain blockquote anywhere that doesn't understand it (e.g. a raw Substack paste).

`The point` is **not** an inline callout — it lives in the frontmatter `point:` field, and the publish step renders it as the callout at the very top of the article (after the H1, before the opener). The frontmatter is the source of truth; don't hand-write it into the body.

## notes.md

Append-only. Never rewritten by Claude. This is the lossless record of what was actually said.

```yaml
---
slug: my-article-slug
---
```

Body is a sequence of timestamped transcript blocks:

```markdown
## 2026-05-07 14:23 — recording-filename.m4a

(verbatim transcript text)

---

## 2026-05-08 09:11 — another-recording.m4a

(verbatim transcript text)

---
```

## linkedin/NN-<short-name>.md

One snippet per file. Generated from a `ready` or `published` article. Numeric prefix controls drip order.

```yaml
---
parent_slug: my-article-slug
type: hook           # hook | lesson | snippet | quote
status: draft        # draft | ready | scheduled | published
scheduled_for:       # YYYY-MM-DD, optional
linkedin_url:        # filled in after publishing
---
```

Body is the post text. Keep under ~1300 characters (LinkedIn's "see more" cutoff).
