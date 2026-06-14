# Ghost(Pro) hosted publishing

This vault publishes to two Ghost instances from the same `article.md` files:

| Target   | Where                              | Key (`.env`)            | Use for                          |
|----------|------------------------------------|-------------------------|----------------------------------|
| `local`  | `http://100.119.32.88:2368` (LAN)  | `GHOST_LOCAL_API_KEY`   | Previewing drafts before they go live |
| `hosted` | your Ghost(Pro) site               | `GHOST_HOSTED_API_KEY`  | The real, public blog            |

`local` is the default, so every existing command and the cron pipeline keep working untouched. Add `--target hosted` (or use the `make` targets below) to push to the public site.

## 1. Get a Ghost Admin API key

The hosted Admin API is identical to self-hosted Ghost — same `/ghost/api/admin/` endpoints, same JWT auth, same lexical format. Only the URL and key differ.

1. Log in to your site admin: `https://yoursite.ghost.io/ghost/`.
2. **Settings → Advanced → Integrations → Add custom integration.** Name it e.g. `vault-publisher`.
3. Copy the **Admin API Key**. It looks like `653f...a1:9c4e...77` — an `id:secret` pair separated by a colon. (Do **not** use the Content API Key; that one is read-only.)
4. Note your site URL. This is the public root, e.g. `https://thef1rstpancake.ghost.io` — **without** a trailing `/ghost`.

> [!warning] Custom domains
> If you've mapped a custom domain (e.g. `https://blog.example.com`), use whatever URL your admin panel actually loads at for `GHOST_HOSTED_URL`. The API lives under that same origin.

## 2. Populate `.env`

`.env` is gitignored (the vault repo is public — never commit keys). Edit it to fill the two hosted placeholders:

```
GHOST_HOSTED_URL=https://thef1rstpancake.ghost.io
GHOST_HOSTED_API_KEY=653f0000000000000000a1:9c4e00000000000000000000000000000000000000000000000000000000000077
```

The scripts refuse to run against `hosted` while either value is still `FILL_ME_IN` / `https://yoursite.ghost.io`, so a half-configured `.env` fails loudly instead of posting somewhere wrong.

## 3. The push/update cycle

Typical flow for one article:

```sh
# 1. Edit drafts/<slug>/article.md locally.

# 2. Preview as a draft on the LAN Ghost — check rendering, callouts, the point card.
make preview SLUG=<slug>

# 3. Happy? Publish to the public site.
make publish SLUG=<slug>
```

If you'd rather stage it as a hosted draft first (review inside the Ghost Pro editor before it goes public):

```sh
make push-draft SLUG=<slug>     # draft on hosted
# ...review at https://yoursite.ghost.io/ghost/ ... then:
make publish SLUG=<slug>        # flips it to published
```

### All the make targets

| Command | Effect |
|---------|--------|
| `make preview SLUG=<slug>`        | Upload as **draft** to **local** (review) |
| `make push-draft SLUG=<slug>`     | Upload as **draft** to **hosted** |
| `make publish SLUG=<slug>`        | Upload as **published** to **hosted** |
| `make push-page FILE=drafts/about/article.md` | Upload a **page** to **hosted** |
| `make publish-all`                | Upload every article with `status: ready` to hosted as **published** |
| `make sync-all`                   | Upload every article (any status) to hosted as **drafts** |
| `make help`                       | List the commands |

Under the hood these just call the scripts directly, so you can always drop down a level:

```sh
python3 ghost-upload.py drafts/<slug>/article.md --target hosted          # published
python3 ghost-upload.py drafts/<slug>/article.md --draft --target hosted   # draft
python3 ghost-upload-page.py drafts/about/article.md --target hosted       # a page
```

Omitting `--target` (or passing `--target local`) is the original local behavior.

## 4. How updates work — idempotency

Both scripts **upsert by slug**:

- They `GET /posts/slug/<slug>/` (pages: `/pages/slug/<slug>/`) first.
- If a post/page with that slug exists, they `PUT` an update (passing the server's `updated_at` for Ghost's collision check).
- Otherwise they `POST` a new one.

So **re-running is safe and idempotent** — edit the article, run `make publish SLUG=...` again, and the live post is updated in place. The slug in frontmatter is the identity key; don't change it after publishing or you'll create a second post.

The `point:` callout card and `> [!type]` callouts are rebuilt from source each run, so the rendered output always matches the current `article.md`.

## 5. Gotchas

- **Slug is identity.** Renaming `slug:` orphans the old post and creates a new one. The old one stays live until you delete it in the admin.
- **Tags are created on demand.** Posting with `tags: [foo, bar]` makes any missing tags automatically. Existing tags are matched by name (Ghost is case-sensitive-ish on tag names — reuse exact spellings to avoid near-duplicate tags).
- **Images.** The scripts upload HTML/lexical only; they do **not** upload image files. Any `![](…)` must already point at a publicly reachable URL (e.g. an image you uploaded in the Ghost editor, or an external host). Relative paths to local files won't resolve on the hosted site.
- **Footnote anchors.** Posts are written as lexical `html` cards on purpose, bypassing Ghost's `?source=html` sanitizer which strips footnote `id=`/`href=#` anchors. Don't switch posts back to `source=html`.
- **Pages: mobiledoc vs lexical.** `ghost-upload-page.py` detects whether an existing page is legacy mobiledoc (`lexical` is null) and, if so, updates it via `?source=html`; new/lexical pages get lexical written directly. This only matters for the About page and similar — posts are always lexical.
- **JWT clock.** Auth tokens are signed with a 5-minute expiry from your machine's clock. If pushes fail with 401, check the system time is correct.
- **`status: published` on the API publishes immediately** — there's no separate "send newsletter" step triggered here, but if your Ghost site has email newsletters enabled, double-check the integration/post settings so a republish doesn't email subscribers unexpectedly.
