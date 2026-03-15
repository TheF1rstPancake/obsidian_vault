#!/usr/bin/env bash
set -euo pipefail

# Sync vault to Google Drive (excludes raw audio archive to save space)
# Run: rclone config  (one-time setup to create "gdrive" remote)

VAULT="$HOME/obsidian-vault"

rclone sync "$VAULT" gdrive:obsidian-vault \
    --exclude "archive/**" \
    --exclude ".obsidian/workspace*.json" \
    --exclude "process-recordings.sh" \
    --exclude "sync-to-gdrive.sh" \
    --exclude ".gitignore" \
    -v
