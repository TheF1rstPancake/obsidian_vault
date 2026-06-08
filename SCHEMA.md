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

### Callouts

Use markdown blockquotes with a bolded label for callouts. Substack renders these as left-bordered indented blocks. Same convention for every callout type — consistency is the point.

```markdown
> **The label**
>
> Body content. Can be multiple paragraphs or include lists:
>
> - bullet
> - bullet
```

Standard callout types in the body:

- **Tactical artifacts** — frameworks, decision matrices, checklists the reader will want to steal. Labeled with what the artifact is (e.g., `The three questions`, `Hiring scorecard`).
- **Definitions** — only when a load-bearing term needs to be set off from prose.
- **Asides** — short tangents that don't belong in the main flow but are too brief for a footnote.

`The point` is **not** an inline callout — it lives in the frontmatter `point:` field. At publish time, render the `point:` field into a body callout at the top of the article (after the H1, before the opener), using the same blockquote convention. The frontmatter is the source of truth; the body callout is a derived rendering for Substack.

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
