#!/usr/bin/env bash
set -euo pipefail

cd "$HOME/obsidian-vault"

# Skip if nothing changed
if git diff --quiet && git diff --cached --quiet && [ -z "$(git ls-files --others --exclude-standard)" ]; then
    exit 0
fi

git add -A
git commit -m "vault auto-backup $(date +%Y-%m-%d_%H:%M)"

if ! git push; then
    msg="vault sync: git push failed at $(date -Iseconds). See /tmp/vault-sync.log."
    echo "$msg" >&2
    # Best-effort desktop notification; ignore if not available (e.g. cron without DBUS).
    command -v notify-send >/dev/null && \
        DISPLAY="${DISPLAY:-:0}" \
        DBUS_SESSION_BUS_ADDRESS="${DBUS_SESSION_BUS_ADDRESS:-unix:path=/run/user/$(id -u)/bus}" \
        notify-send -u critical "Obsidian vault sync failed" "$msg" || true
    exit 1
fi
