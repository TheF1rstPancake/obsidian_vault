# Ghost publishing pipeline.
#
# Targets that touch the *hosted* (Ghost Pro) blog require GHOST_HOSTED_URL and
# GHOST_HOSTED_API_KEY to be set in .env (see GHOST_HOSTED.md). The `local`
# target talks to the LAN Ghost at http://100.119.32.88:2368.
#
#   make preview SLUG=evaluating-judgement     # draft -> local Ghost (review)
#   make push-draft SLUG=evaluating-judgement   # draft -> hosted Ghost
#   make publish SLUG=evaluating-judgement      # published -> hosted Ghost
#   make push-page FILE=drafts/about/article.md # page  -> hosted Ghost
#   make publish-all                            # all status:ready -> hosted (published)
#   make sync-all                               # all articles -> hosted (drafts)
#   make theme-pack                             # zip ghost-theme/pancake/ -> ghost-theme/pancake.zip
#   make theme-push                             # pack + upload/activate theme on hosted Ghost
#   make push-ready                             # push all status:ready ghost articles as drafts
#   make push-ready-dry                         # dry-run: list articles that would be pushed
#   make push-ready-local                       # push ready articles to local Ghost
#
# Editorial pipeline (scripts/):
#   make article-context SLUG=evaluating-judgement   # build .pipeline/context.md bundle
#   make article-edit SLUG=evaluating-judgement      # editor-only AI pass -> .pipeline/editor-report.md
#   make article-edit-dry SLUG=evaluating-judgement  # build the editor prompt, don't call the AI
#   make article-preview SLUG=evaluating-judgement   # alias for `make preview` (local Ghost draft)
#   make article-annotations SLUG=evaluating-judgement # list unresolved pancake-review annotations

PY := python3
UPLOAD := $(PY) ghost-upload.py
UPLOAD_PAGE := $(PY) ghost-upload-page.py
PIPELINE := $(PY) scripts/article_pipeline.py
DRAFTS := drafts

.PHONY: preview publish push-draft push-page publish-all sync-all help \
        theme-pack theme-push push-ready push-ready-dry push-ready-local \
        article-context article-edit article-edit-dry article-preview article-annotations test

help:
	@grep -E '^#   make' Makefile | sed 's/^#   /  /'

# Guard: SLUG must be provided and the article must exist.
define need_slug
	@test -n "$(SLUG)" || { echo "error: SLUG=<slug> required"; exit 1; }
	@test -f "$(DRAFTS)/$(SLUG)/article.md" || { echo "error: $(DRAFTS)/$(SLUG)/article.md not found"; exit 1; }
endef

preview:
	$(need_slug)
	$(UPLOAD) $(DRAFTS)/$(SLUG)/article.md --draft --target local

publish:
	$(need_slug)
	$(UPLOAD) $(DRAFTS)/$(SLUG)/article.md --target hosted

push-draft:
	$(need_slug)
	$(UPLOAD) $(DRAFTS)/$(SLUG)/article.md --draft --target hosted

push-page:
	@test -n "$(FILE)" || { echo "error: FILE=<path/to/article.md> required"; exit 1; }
	@test -f "$(FILE)" || { echo "error: $(FILE) not found"; exit 1; }
	$(UPLOAD_PAGE) $(FILE) --target hosted

# Publish every article whose frontmatter status is `ready` to the hosted blog.
publish-all:
	@found=0; \
	for f in $(DRAFTS)/*/article.md; do \
		[ -f "$$f" ] || continue; \
		if grep -Eq '^status:[[:space:]]*ready[[:space:]]*$$' "$$f"; then \
			echo "==> publishing $$f"; \
			$(UPLOAD) "$$f" --target hosted || exit 1; \
			found=1; \
		fi; \
	done; \
	[ "$$found" = 1 ] || echo "no articles with status: ready"

# Push every article (any status) to the hosted blog as a draft.
sync-all:
	@for f in $(DRAFTS)/*/article.md; do \
		[ -f "$$f" ] || continue; \
		echo "==> syncing $$f"; \
		$(UPLOAD) "$$f" --draft --target hosted || exit 1; \
	done

THEME_UPLOAD := $(PY) ghost-theme-upload.py
BATCH := $(PY) ghost-publish-ready.py

theme-pack:
	./ghost-theme-pack.sh

theme-push: theme-pack
	$(THEME_UPLOAD) --target hosted

push-ready:
	$(BATCH) --target hosted

push-ready-dry:
	$(BATCH) --target hosted --dry-run

push-ready-local:
	$(BATCH) --target local

# --- Editorial pipeline ----------------------------------------------------

# Guard for pipeline targets: only the draft folder must exist (article.md is
# optional for `context`, which is useful even on a slug that's still notes-only).
define need_slug_dir
	@test -n "$(SLUG)" || { echo "error: SLUG=<slug> required"; exit 1; }
	@test -d "$(DRAFTS)/$(SLUG)" || { echo "error: $(DRAFTS)/$(SLUG)/ not found"; exit 1; }
endef

article-context:
	$(need_slug_dir)
	$(PIPELINE) context $(SLUG)

article-edit:
	$(need_slug_dir)
	$(PIPELINE) edit $(SLUG)

article-edit-dry:
	$(need_slug_dir)
	$(PIPELINE) edit $(SLUG) --dry-run

article-preview:
	$(need_slug)
	$(PIPELINE) preview $(SLUG)

article-annotations:
	$(need_slug_dir)
	$(PIPELINE) annotations $(SLUG)

# Run the editorial-tooling test suite (uses uvx pytest; falls back to python -m pytest).
test:
	@if command -v uvx >/dev/null 2>&1; then \
		uvx pytest scripts/tests/ -q; \
	else \
		$(PY) -m pytest scripts/tests/ -q; \
	fi
