# 🥞 pancake-review

A lightweight, local-only **document review console**. It renders local
markdown in a clean, mobile-friendly reader view and lets you **highlight any
passage and leave a free-form note**. Notes are stored where Hermes can pick
them up, edit the source markdown, and mark them resolved.

Two document sources are supported today:

1. **Article drafts** — Ghost drafts under `drafts/*/article.md` (the original
   use case). The read → highlight → "resolve annotations for `<slug>`" loop is
   unchanged.
2. **Hub documents** — durable findings, reports, living docs, and HTML design
   artifacts (storyboards/comps) from the Hermes hub (`~/hermes-hub/shared/**`
   and `~/hermes-hub/projects/**`). Markdown gets the annotation reader; HTML
   is served as a full document so comps keep their own styling.

The intended loop: read a draft or finding on your phone (over Tailscale) →
highlight the rough bits → drop notes.

---

## What it does

- **`GET /`** — mobile-friendly index with three tabs: **Posts** (article
  drafts), **Guides**, and **Hub** (findings / reports / docs).
- **`GET /article/{slug}`** — reader view + annotation UI for an article/guide.
- **`GET /doc/{doc_id}`** — reader view + annotation UI for a hub document.
  `doc_id` is URL-encoded (see the hub section below).
- **`GET|POST /edit/article/{slug}?file=...`** — edit and save the selected
  article or guide Markdown source.
- **`GET|POST /edit/doc/{doc_id}`** — edit and save a hub Markdown source.
- **`POST /annotations`** — save a note `{slug, highlighted_text, comment}`.
  For a hub doc, `slug` is the hub `doc_id`.
- **`GET /annotations/{slug}`** — list notes for a document (unresolved by
  default; `?all=true` for everything). Accepts hub `doc_id`s (which contain
  `/`) as the slug.
- **`PATCH /annotations/{id}`** — mark a note resolved (`{resolved: true}`;
  requires a `proof` quote).
- **`GET /api/articles`** — JSON article list for programmatic use.
- **`GET /api/documents`** — unified registry: article drafts **and** hub docs,
  each with `{doc_id, kind, title, path, project, status, unresolved}`.
- **`GET /healthz`** — quick check: article/guide/hub-doc counts + annotation
  stats.

Annotations are stored in **`~/.hermes/annotations.json`** (a flat JSON list,
outside this repo so the public vault never auto-commits them). The
`annotations.json` file in this directory is a convenience **symlink** to that
real store.

---

## Ghost setup & API keys (read this — it differs from the generic Ghost docs)

This local Ghost only exposes an **Admin API key**, stored in
`~/obsidian-vault/.env` as:

```
GHOST_LOCAL_API_KEY=<id>:<secret>
```

There is **no separate Content API key** in this setup. So pancake-review
authenticates *every* read with a short-lived **JWT** built from the Admin key
(`HS256`, `kid` = the key id, `aud` = `/admin/`, 5-min expiry) and talks to the
**Admin API** (`/ghost/api/admin/...`). This mirrors the sibling
[`ghost-upload.py`](../ghost-upload.py) script, which uses the same key the same
way. PyJWT does the signing.

Ghost listens on the **Tailscale IP**, not `localhost`:

```
GHOST_LOCAL_URL=http://100.119.32.88:2368   # default; override via env if it moves
```

> If you ever add a real Content API key, you could swap the reads to
> `/ghost/api/content/posts/?key=...`. Not needed today — the Admin key already
> grants read + write, which the resolution flow needs anyway.

No app-level auth: this is Tailscale-local only, reachable from your phone on
the tailnet. Don't expose port 4242 to the public internet.

---

## Setup

Requires [`uv`](https://docs.astral.sh/uv/) and the local Ghost running.

```bash
cd ~/obsidian-vault/pancake-review
uv sync          # creates .venv and installs deps (fastapi, uvicorn, httpx, pyjwt, jinja2, python-dotenv)
```

`uv sync` reads `pyproject.toml`. The key is loaded from `../.env` automatically
via `python-dotenv`.

## Run

```bash
cd ~/obsidian-vault/pancake-review
uv run uvicorn main:app --host 0.0.0.0 --port 4242 --reload
```

Then open `http://<this-machine-tailscale-ip>:4242/` on your phone (or
`http://localhost:4242/` on the same box). Verify Ghost connectivity with
`curl -s http://localhost:4242/healthz`.

---

## Using the reader

1. Open an article. Existing **unresolved** notes are highlighted in yellow —
   tap one to read the comment.
2. Select/long-press any text. A floating **"＋ Add note"** button appears.
3. Tap it, type your note, hit **Save**. The passage turns yellow and the note
   is stored. A brief "Note saved ✓" toast confirms.

Highlighting matches the **first occurrence** of the stored passage in the
article body. If a passage can't be matched (e.g. it spanned formatting
boundaries), the note is still saved and counted — the header shows an
"(N unmatched)" hint — it just isn't visually placed. The note is never lost;
Hermes still gets it via the API.

---

## Resolution flow (for Hermes)

When the user says **"resolve annotations for `<slug>`"**, Hermes:

1. **Fetch** the open notes:

   ```bash
   curl -s http://localhost:4242/annotations/<slug>
   ```

   Returns `{ "slug": "...", "annotations": [ {id, highlighted_text, comment, created_at, resolved}, ... ] }`
   (unresolved only by default).

2. **Apply** each note as an edit to the markdown source at
   `~/obsidian-vault/drafts/<slug>/article.md`. Use `highlighted_text` to locate
   the passage and `comment` as the instruction for what to change. Follow the
   vault conventions in `~/obsidian-vault/CLAUDE.md` and `SCHEMA.md` (bump
   `updated:`, don't lower `status`, etc.).

3. **Re-push** to Ghost:

   ```bash
   cd ~/obsidian-vault
   python3 ghost-upload.py drafts/<slug>/article.md          # published
   # or:  python3 ghost-upload.py drafts/<slug>/article.md --draft
   ```

4. **Mark resolved** — one PATCH per applied note:

   ```bash
   curl -s -X PATCH http://localhost:4242/annotations/<id> \
     -H 'Content-Type: application/json' -d '{"resolved": true}'
   ```

After resolution, the reader view stops highlighting those passages (resolved
notes are excluded from the default `GET /annotations/<slug>` response). Use
`?all=true` to audit the full history including resolved ones.

> **Note for the agent:** `<slug>` is the Ghost post slug, which equals the
> draft folder name and the `slug:` frontmatter field. If a note's
> `highlighted_text` is ambiguous (appears multiple times), match on the
> surrounding context from the article body before editing.

---

## Reviewing hub documents

The **Hub** tab lists durable documents from `~/hermes-hub`: findings, reports,
living docs, and HTML artifacts under `shared/**` and `projects/<project>/**`.
Tap one to open it.

### Document registry & adapters

`documents.py` is a small **registry of adapters**. Every document — article or
hub file — exposes the same stable fields so the UI and annotation store treat
them uniformly:

| field     | meaning                                                        |
|-----------|----------------------------------------------------------------|
| `doc_id`  | stable, unambiguous id (also the annotation `slug`)            |
| `kind`    | `article` · `hub_finding` · `hub_report` · `hub_doc` · `hub_html` · `markdown` |
| `format`  | hub only: `markdown` or `html` (how `/doc/...` renders)        |
| `title`   | human-readable title (frontmatter / `<title>`, else filename)  |
| `path`    | absolute path on disk                                          |
| `project` | frontmatter `project:`, else derived from the path (`shared` / `<project>`) |
| `status`  | frontmatter `status:` when present (`final`, `living`, …)      |

**`doc_id` convention.** Article ids stay equal to the folder slug (so existing
annotations keep matching). Hub ids use a `hub:<relpath>` form, e.g.

```
hub:shared/findings/2026-07-03-codex-cursor-pr-orchestration.md
hub:projects/meal-planner/docs/meal-planner-storyboard.html
```

The relative path is unique within the hub and can never collide with an
article slug. Markdown hub `kind` comes from frontmatter `type:`
(finding/report/doc), falling back to the containing folder name. HTML files
always use `kind: hub_html` / `format: html`.

### How it renders & annotates

- `GET /doc/{doc_id}` resolves the id back to a file (with path-traversal and
  in-bounds guards — reads are restricted to `.md` / `.html` files under
  `shared/` and `projects/`).
- **Markdown** hub docs render through the same markdown/callout pipeline and
  annotation UI as articles. Annotations use `slug = doc_id` and a single
  logical `file` bucket (`doc`).
- **HTML** hub artifacts are returned as the full HTML document (not nested in
  the markdown reader chrome). This is the simplest remote-safe path for
  storyboards and design comps; HTML is not sanitized (trusted Tailscale-local
  tool). Use browser Back to return to the Hub tab; `/edit/doc/{doc_id}` still
  edits the raw source.
- Links in the Hub tab URL-encode the `doc_id` (`hub%3Ashared%2F…`). The route
  uses a `:path` converter, so `GET /annotations/<doc_id>` also accepts the
  slashes in a hub id.

### Direct editing and safety

Every article, guide, and hub reader has an **Edit source** control. The edit
page shows the complete raw Markdown, including frontmatter, in a plain
mobile-friendly textarea. Save writes directly to the backing file and returns
to the reader; Cancel returns without writing.

Edits are limited to documents the existing adapters can already resolve:

- Article/guide saves require an existing slug directory and existing
  simple-stem `.md` filename. The active guide `overview`/`content` selection
  is retained.
- Hub saves require an existing `.md` or `.html` file below the configured hub
  `shared/` or `projects/` roots. The existing traversal and resolved-path
  checks apply to writes.
- Empty content is rejected with HTTP 400. Saves never create files, run Git,
  or change/resolve annotations. Use `git status` and `git diff` outside the
  app as the edit audit surface.

---

## Verify / test

No pytest dependency — the adapter has a self-contained checker:

```bash
cd ~/obsidian-vault/pancake-review
uv run python test_documents.py     # builds a temp hub, checks listing/guards/wiring
uv run python -m py_compile main.py documents.py
```

---

## File layout

```
pancake-review/
  README.md            ← this file
  pyproject.toml       ← uv deps
  main.py              ← FastAPI app (routes, Ghost JWT auth, annotation storage)
  documents.py         ← document registry / hub adapter (doc_id, listing, guards)
  test_documents.py    ← dependency-light verification for the adapter + wiring
  templates/
    index.html         ← index with Posts / Guides / Hub tabs
    article.html       ← reader + annotation UI (vanilla JS, no build step)
  annotations.json     ← symlink → ~/.hermes/annotations.json (the real store)
  .gitignore           ← keeps .venv / caches out of the public vault repo
```

## Config (env vars, all optional except the key)

| var                    | default                       | purpose                          |
|------------------------|-------------------------------|----------------------------------|
| `GHOST_LOCAL_API_KEY`  | *(from `../.env`)*            | Ghost Admin key `id:secret`      |
| `GHOST_LOCAL_URL`      | `http://100.119.32.88:2368`   | Ghost base URL (Tailscale IP)    |
| `PANCAKE_ANNOTATIONS`  | `~/.hermes/annotations.json`  | annotation store path            |
| `PANCAKE_HUB_ROOT`     | `/home/giovanni/hermes-hub`   | Hermes hub root for the Hub tab  |
