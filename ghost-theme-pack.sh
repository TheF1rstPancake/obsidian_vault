#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")"

SRC="ghost-theme/pancake"
OUT="ghost-theme/pancake.zip"

[ -d "$SRC" ] || { echo "error: $SRC not found" >&2; exit 1; }

rm -f "$OUT"
zip -r "$OUT" "$SRC" \
    -x "*.DS_Store" \
    -x "*__MACOSX*" \
    -x "*.log" \
    -x "*/.git*" \
    -x "*/node_modules/*"

FILE_COUNT=$(unzip -l "$OUT" | tail -1 | awk '{print $(NF-1)}')
ZIP_SIZE=$(du -sh "$OUT" | awk '{print $1}')
echo "$OUT: $FILE_COUNT files, $ZIP_SIZE"
