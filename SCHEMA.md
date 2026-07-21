# Vault schema

Source of truth for frontmatter and folder layout. Referenced by CLAUDE.md and inlined into the enrichment prompts in `process-recordings.sh`. Update this file when the schema changes; both code paths will pick it up. Audio transcription is handled by `scripts/transcribe_worker.py` (see SETUP.md), not by this schema.

**Publishing target is Ghost** (`thefirstpancake.ghost.io`, local preview at `http://100.119.32.88:2368`). Substack was the original target; any `target: substack` / `substack_url:` left in older drafts is legacy and should be migrated to the Ghost fields below. Voice and editing conventions live in [STYLE.md](./STYLE.md) — required reading before shaping or editing any `article.md`.

## Folder layout

```
drafts/<slug>/
  article.md          # the polished Ghost draft (the published output)
  notes.md            # append-only raw transcripts, timestamped (lossless source)
  linkedin/           # generated LinkedIn snippets, one per file
    01-<short-name>.md
    02-<short-name>.md
  .pipeline/          # editorial tooling artifacts (not published); safe to delete/regenerate
    context.md        # built by scripts/article_context.py — the editor's context bundle
    editor-report.md  # built by scripts/article_pipeline.py edit — structured editor critique
```

`<slug>` is kebab-case, 2–5 words, derived from the topic. The `.pipeline/` directory holds generated, disposable artifacts; it is not part of the published output and can be regenerated at any time.

## article.md

The polished Ghost draft. Regenerated/refined by Claude as new recordings arrive.

```yaml
---
title: "Working title for the article"
slug: my-article-slug
status: raw          # raw | shaping | ready | published
target: ghost
created: 2026-05-07
updated: 2026-05-07
tags: [optional, kebab-case, tags]
related: ["other-article-slug"]  # optional. Companion/seed articles this piece links to or from.
visibility: public  # public | members | paid — post-level access on Ghost (default: public)
point: >            # the compressed argument, ~50–100 words. Required for articles >1500 words; optional below that.
  One-paragraph summary of the article's argument. Use YAML folded
  scalar (>) so newlines fold into spaces. This is the source of
  truth for template renderings — LinkedIn snippets, RSS descriptions,
  site indexes, and the body callout at publish time all derive from
  this field.
ghost_url:           # filled in after publishing (legacy drafts may use substack_url)
---
```

`target: ghost` is required for the batch publish path (`ghost-publish-ready.py` only picks up `status: ready` + `target: ghost`). The `ghost_url:`/`substack_url:`/`related:` fields are documentation only — no script parses them. Body text still needs its own plain markdown link to a related piece (`related:` doesn't render anything); it just makes the pairing greppable in frontmatter.

`status` lifecycle:
- **raw** — first transcript landed, draft is unshaped
- **shaping** — actively iterating, multiple transcripts merged; STYLE.md governs the shaping pass
- **ready** — publishable; LinkedIn snippet generation can fire
- **published** — live on Ghost; `ghost_url` populated

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

`point:` is also the source for Ghost's `custom_excerpt` card copy. The pipeline derives the homepage/list-card summary from the same field, trimming to Ghost's 300-character limit when needed. That means you do **not** need a second TL;DR field just for cards.

### Paywall & access control

Two independent levers control who can read a published article on Ghost. Use either or both.

**1. Post-level visibility (frontmatter).** The `visibility:` field gates the *entire* article:

```yaml
visibility: public   # anyone can read (default if the field is absent)
visibility: members  # signed-in members only
visibility: paid     # paid subscribers only
```

`ghost-upload.py` passes this straight to the Ghost Admin API as `visibility`. Absent → `public`. Invalid values are rejected at publish time.

**2. Mid-article paywall (`---paywall---` marker).** To keep an opener public but gate the rest, put `---paywall---` on its own line in the body:

```markdown
Here's the free thesis everyone can read…

---paywall---

## The good stuff

This part is members-only.
```

At publish time the marker is removed and a Ghost `<!--members-only-->` card is injected in its place. Everything **above** the marker stays public; everything **below** is shown only to logged-in members (Ghost's standard mid-post gate). The split happens before callouts are extracted, so callouts work on either side. Only the first marker is honored.

The two levers compose: a `public` article with a `---paywall---` marker shows a free teaser to everyone and gates the rest; a `paid` article gates the whole thing regardless of marker.

### Pages vs posts (`--page` flag)

By default `ghost-upload.py` publishes to `/ghost/api/admin/posts/` (a dated blog post in the feed). Pass `--page` to publish to `/ghost/api/admin/pages/` instead — a standalone, un-feed resource (e.g. a reference template, a landing page). Upsert-by-slug, visibility, and the paywall marker all work identically for pages.

```
python3 ghost-upload.py drafts/solution-design-template/article.md --page
```

## Guides

A **guide** is a standalone reference resource published as Ghost **pages**, independent of any article. The default shape is a public overview plus a paid content page. Some guides also include a public blank template page that readers can copy.

### Folder layout

```
guides/<name>/
  overview.md         # public "product page" — what the guide is, who it's for, what's inside
  content.md          # the full gated content (always paid)
  blank-template.md   # optional public copyable template page
```

`guides/` lives at the root of the vault, alongside `drafts/`.

### Frontmatter

Same schema as `article.md` (see above), with one difference: `target: ghost-page`. Both files carry it.

- **overview.md** — always `visibility: public`. Slug: `guide-<name>`.
- **content.md** — always `visibility: paid`. Slug: `guide-<name>-content`.
- **blank-template.md** — optional. Usually `visibility: public`. Slug: `guide-<name>-blank`.

`parse_article()` reads both with the identical frontmatter parser; `point:`, `tags:`, and callouts all work the same.

### Slug convention

| File | Slug |
|---|---|
| `overview.md` | `guide-<name>` |
| `blank-template.md` | `guide-<name>-blank` |
| `content.md` | `guide-<name>-content` |

Example: `guides/solution-design-template/` → `guide-solution-design-template` (overview), `guide-solution-design-template-blank` (blank template), and `guide-solution-design-template-content` (content).

### overview.md structure

The overview is lean — it's a landing page, not a full article. A short intro (what problem the guide solves, 2–3 sentences), a `## What's inside` bullet list, and a `[!tip]` callout pointing paid subscribers to subscribe. It does **not** restate the content; explaining the idea in depth is an *article's* job.

### Relationship to articles

Guides are **loosely coupled** to articles. An article may link to a guide's public overview by URL (e.g. `[/guide-<name>/](/guide-<name>/)`) — that's the only connection. There is no shared frontmatter, no required pairing; a guide can exist without an article and vice versa. Use a plain markdown link, never a wikilink.

### Publishing

```
python3 ghost-upload.py --guide guides/<name>/ [--target local|hosted]
```

The `--guide` flag publishes `overview.md` first (so its link resolves), then `blank-template.md` if present, then `content.md`, all as Ghost pages. It is mutually exclusive with `--page`. Add `--dry-run` to print the parsed frontmatter (slug/visibility) without publishing.

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
