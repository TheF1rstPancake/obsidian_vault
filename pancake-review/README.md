# 🥞 pancake-review

A lightweight, local-only **document review console**. It renders local
markdown in a clean, mobile-friendly reader view and lets you **highlight any
passage and leave a free-form note**. Notes are stored where Hermes can pick
them up, edit the source markdown, and mark them resolved.

Two document sources are supported today:

1. **Article drafts** — Ghost drafts under `drafts/*/article.md` (the original
   use case). The read → highlight → "resolve annotations for `<slug>`" loop is
   unchanged.
2. **Hub documents** — durable findings, reports, and living docs from the
   Hermes hub (`~/hermes-hub/shared/**` and `~/hermes-hub/projects/**`).
   Because findings shape future project decisions, they're worth reviewing and
   commenting on the same way. **This slice is read / review / comment only —
   there is no automated resolution of hub annotations yet.**

The intended loop: read a draft or finding on your phone (over Tailscale) →
highlight the rough bits → drop notes.

---

## What it does

- **`GET /`** — mobile-friendly index with three tabs: **Posts** (article
  drafts), **Guides**, and **Hub** (findings / reports / docs).
- **`GET /article/{slug}`** — reader view + annotation UI for an article/guide.
- **`GET /doc/{doc_id}`** — reader view + annotation UI for a hub document.
  `doc_id` is URL-encoded (see the hub section below).
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
and living docs under `shared/**` and `projects/<project>/**`. Tap one to open
the same reader/annotation view used for articles.

### Document registry & adapters

`documents.py` is a small **registry of adapters**. Every document — article or
hub file — exposes the same stable fields so the UI and annotation store treat
them uniformly:

| field     | meaning                                                        |
|-----------|----------------------------------------------------------------|
| `doc_id`  | stable, unambiguous id (also the annotation `slug`)            |
| `kind`    | `article` · `hub_finding` · `hub_report` · `hub_doc` · `markdown` |
| `title`   | human-readable title (frontmatter `title:`, else filename)     |
| `path`    | absolute path on disk                                          |
| `project` | frontmatter `project:`, else derived from the path (`shared` / `<project>`) |
| `status`  | frontmatter `status:` when present (`final`, `living`, …)      |

**`doc_id` convention.** Article ids stay equal to the folder slug (so existing
annotations keep matching). Hub ids use a `hub:<relpath>` form, e.g.

```
hub:shared/findings/2026-07-03-codex-cursor-pr-orchestration.md
```

The relative path is unique within the hub and can never collide with an
article slug. Hub `kind` comes from frontmatter `type:` (finding/report/doc),
falling back to the containing folder name.

### How it renders & annotates

- `GET /doc/{doc_id}` resolves the id back to a file (with path-traversal and
  in-bounds guards — reads are restricted to `.md` files under `shared/` and
  `projects/`) and renders it through the same markdown/callout pipeline.
- Annotations on a hub doc are stored with `slug = doc_id` and a single logical
  `file` bucket (`doc`). The annotation store and PATCH/proof flow are
  unchanged; **only the store's `slug` values differ** for hub docs.
- Links in the Hub tab URL-encode the `doc_id` (`hub%3Ashared%2F…`). The route
  uses a `:path` converter, so `GET /annotations/<doc_id>` also accepts the
  slashes in a hub id.

> **Not in this slice:** automated resolution of hub annotations. Hermes can
> *read* open hub notes via `GET /annotations/<doc_id>?all=true`, but this PR
> deliberately does **not** edit `~/hermes-hub` files. This is read / review /
> comment only.

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
