#!/usr/bin/env bash
set -euo pipefail

cd "$HOME/obsidian-vault"

# Skip if nothing changed
if git diff --quiet && git diff --cached --quiet && [ -z "$(git ls-files --others --exclude-standard)" ]; then
    exit 0
fi

git add -A
git commit -m "vault auto-backup $(date +%Y-%m-%d_%H:%M)"
git push
