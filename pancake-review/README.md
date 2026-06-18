# 🥞 pancake-review

A lightweight, local-only article annotation tool. It pulls articles from the
local Ghost instance, renders them in a clean mobile-friendly reader view, and
lets you **highlight any passage and leave a free-form note**. Notes are stored
where Hermes can pick them up, edit the source markdown, re-push to Ghost, and
mark them resolved.

The intended loop: read a draft on your phone (over Tailscale) → highlight the
rough bits → drop notes → tell Hermes "resolve annotations for `<slug>`".

---

## What it does

- **`GET /`** — mobile-friendly list of all Ghost articles (any status).
- **`GET /article/{slug}`** — reader view with the annotation UI.
- **`POST /annotations`** — save a note `{slug, highlighted_text, comment}`.
- **`GET /annotations/{slug}`** — list notes for an article (unresolved by
  default; `?all=true` for everything).
- **`PATCH /annotations/{id}`** — mark a note resolved (`{resolved: true}`).
- **`GET /api/articles`** — JSON article list for programmatic use.
- **`GET /healthz`** — quick check that Ghost is reachable + article count.

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

## File layout

```
pancake-review/
  README.md            ← this file
  pyproject.toml       ← uv deps
  main.py              ← FastAPI app (routes, Ghost JWT auth, annotation storage)
  templates/
    index.html         ← article list
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
