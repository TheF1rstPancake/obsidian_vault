# Task: Expand Pancake Review to review durable documents

Implement the first slice of turning Pancake Review from an article-only review app into a general local document review console.

## Project context

Repo/worktree root is the obsidian-vault repo. The app lives in `pancake-review/`.

Pancake Review currently reviews Ghost article drafts and stores annotations in `/home/giovanni/.hermes/annotations.json`. Preserve existing article behavior.

Giovanni wants to review/comment on findings and other durable documents, especially files in `~/hermes-hub`, because findings shape future project decisions. This should eventually support articles, guides, findings, reports, docs, and generic markdown, but this PR should be a safe first slice.

## Goal for this PR

Add a document registry/adapters concept and support browsing/opening hub findings/reports/docs in Pancake Review, alongside existing article drafts.

Minimum useful behavior:

1. Keep existing article review routes working.
2. Add a document list/browse page or extend index to show multiple document sources:
   - existing article drafts from `drafts/*/article.md`
   - hub findings/reports/docs from `/home/giovanni/hermes-hub/shared/**` and `/home/giovanni/hermes-hub/projects/**`
3. Each document should have stable fields:
   - `doc_id`
   - `kind` (`article`, `hub_finding`, `hub_report`, `hub_doc`, maybe `markdown`)
   - `title`
   - `path`
   - `project` when available from frontmatter/path
   - `status` when available
4. Add a route to render a selected hub markdown document for review.
5. Existing annotation UX should work for hub docs too, using `slug`/document id that is stable and unambiguous. If existing annotation model is article-slug-shaped, introduce a safe `doc_id` convention like `hub:shared/findings/2026-07-03-codex-cursor-pr-orchestration.md` while preserving old article slugs.
6. Do not implement automated edits to hub documents yet. This slice is read/review/comment, not agent resolution.
7. Add tests or at least lightweight verification helpers if the app has no test suite.
8. Update `pancake-review/README.md` with how to run and how hub document review works.

## Constraints

- Do not rewrite `~/hermes-hub` files in this PR.
- Do not move the annotation store.
- Do not break existing `/healthz` behavior or annotation PATCH proof enforcement.
- Avoid overbuilding. Document adapters can be simple Python classes/functions.
- Use absolute default `/home/giovanni/hermes-hub`, but make it overrideable via env var if straightforward.
- Keep it local-only.

## Verification

Run from repo root/worktree:

```bash
cd pancake-review
uv run python -m py_compile main.py
uv run python - <<'PY'
from main import app
print('app ok', app.title if hasattr(app, 'title') else 'fastapi')
PY
```

If you add tests, run them too.

If practical, start the app briefly and verify `/healthz` and the document index route with curl.

## PR requirements

- Commit changes.
- Push branch.
- Open PR against `master`.
- Print exactly: `PR_URL=<url>`

If blocked, print exactly: `BLOCKED=<reason>`.