#!/usr/bin/env bash
set -euo pipefail

VAULT="$HOME/obsidian-vault"
RECORDINGS="$VAULT/recordings"
TRANSCRIPTS="$VAULT/transcripts"
DRAFTS="$VAULT/drafts"
ARCHIVE="$VAULT/archive"
WHISPER_VENV="$HOME/.local/share/whisper-venv"
WHISPER_MODEL="medium"  # good balance of speed/accuracy for 2070 Super
LOCKFILE="/tmp/process-recordings.lock"

# Prevent concurrent runs
if [ -f "$LOCKFILE" ]; then
    pid=$(cat "$LOCKFILE")
    if kill -0 "$pid" 2>/dev/null; then
        echo "Already running (pid $pid), exiting."
        exit 0
    fi
fi
echo $$ > "$LOCKFILE"
trap 'rm -f "$LOCKFILE"' EXIT

# Activate whisper venv
source "$WHISPER_VENV/bin/activate"

# Find audio files (common phone recording formats)
shopt -s nullglob
audio_files=("$RECORDINGS"/*.{m4a,mp3,wav,ogg,opus,aac,mp4,webm})
shopt -u nullglob

if [ ${#audio_files[@]} -eq 0 ]; then
    echo "No recordings to process."
    exit 0
fi

for audio in "${audio_files[@]}"; do
    filename=$(basename "$audio")
    stem="${filename%.*}"
    timestamp=$(date +%Y-%m-%d_%H%M%S)
    transcript_file="$TRANSCRIPTS/${stem}_${timestamp}.md"

    echo "=== Transcribing: $filename ==="

    # Transcribe with whisper
    whisper "$audio" \
        --model "$WHISPER_MODEL" \
        --output_format txt \
        --output_dir /tmp/whisper-out \
        --language en

    raw_text=$(cat "/tmp/whisper-out/${stem}.txt")
    rm -rf /tmp/whisper-out

    # Save raw transcript as markdown
    cat > "$transcript_file" <<EOF
---
source: $filename
transcribed: $(date -Iseconds)
---

# Transcript: $filename

$raw_text
EOF

    echo "=== Transcript saved: $transcript_file ==="

    # Use Claude to match to existing draft or create new one
    # Build context: list existing drafts with their first few lines
    existing_drafts=""
    for draft in "$DRAFTS"/*.md; do
        [ -f "$draft" ] || continue
        draft_name=$(basename "$draft" .md)
        draft_preview=$(head -20 "$draft")
        existing_drafts+="--- DRAFT: $draft_name ---
$draft_preview

"
    done

    # Unset CLAUDECODE to avoid nesting guard
    unset CLAUDECODE 2>/dev/null || true

    if [ -n "$existing_drafts" ]; then
        match_prompt="You are helping organize voice recording transcripts into articles.

Here is a new transcript from a voice recording:

<transcript>
$raw_text
</transcript>

Here are the existing article drafts:

<existing_drafts>
$existing_drafts
</existing_drafts>

Decide: does this transcript belong to one of the existing drafts, or is it a new topic?

Respond with EXACTLY one line in one of these formats:
MATCH: draft-name-here
NEW: suggested-slug-for-new-article

The draft name should be the exact filename (without .md) of the matching draft folder, or a short kebab-case slug for a new topic. Nothing else."

        match_result=$(claude -p --output-format json "$match_prompt" 2>/dev/null | jq -r '.result // .text // .' | head -1)
    else
        # No existing drafts, ask Claude for a slug
        slug_prompt="Given this transcript from a voice recording, suggest a short kebab-case filename slug (2-5 words) that captures the main topic. Respond with EXACTLY one line like: NEW: my-topic-slug

<transcript>
$raw_text
</transcript>"

        match_result=$(claude -p --output-format json "$slug_prompt" 2>/dev/null | jq -r '.result // .text // .' | head -1)
    fi

    echo "=== Claude says: $match_result ==="

    if [[ "$match_result" == MATCH:* ]]; then
        draft_slug=$(echo "$match_result" | sed 's/^MATCH: *//')
        draft_file="$DRAFTS/${draft_slug}.md"

        if [ ! -f "$draft_file" ]; then
            echo "Warning: Claude matched '$draft_slug' but file not found. Treating as new."
            match_result="NEW: $draft_slug"
        fi
    fi

    if [[ "$match_result" == NEW:* ]]; then
        draft_slug=$(echo "$match_result" | sed 's/^NEW: *//')
        draft_file="$DRAFTS/${draft_slug}.md"

        # Generate initial draft from transcript
        gen_prompt="You are turning a raw voice recording transcript into a well-structured article draft.

The transcript is a rambling voice recording — extract the key ideas and reorganize them into a coherent, readable article draft in markdown. Keep the author's voice and intent. Mark any unclear sections with [?]. Add a YAML frontmatter block with title and date.

<transcript>
$raw_text
</transcript>"

        claude -p --output-format json "$gen_prompt" 2>/dev/null | jq -r '.result // .text // .' > "$draft_file"
        echo "=== Created new draft: $draft_file ==="

    elif [[ "$match_result" == MATCH:* ]]; then
        draft_slug=$(echo "$match_result" | sed 's/^MATCH: *//')
        draft_file="$DRAFTS/${draft_slug}.md"

        # Collect ALL transcripts that have been used for this draft
        existing_draft=$(cat "$draft_file")

        update_prompt="You are updating an article draft with new information from a voice recording.

Here is the current draft:

<current_draft>
$existing_draft
</current_draft>

Here is a new transcript that belongs to this article:

<new_transcript>
$raw_text
</new_transcript>

Update the draft by incorporating the new information from the transcript. Merge ideas, resolve any contradictions (prefer the newer transcript), expand sections, and keep it coherent. Maintain the article's structure but feel free to reorganize if the new content warrants it. Keep the author's voice. Mark unclear sections with [?].

Output the complete updated article in markdown with YAML frontmatter."

        claude -p --output-format json "$update_prompt" 2>/dev/null | jq -r '.result // .text // .' > "$draft_file"
        echo "=== Updated draft: $draft_file ==="
    else
        echo "Warning: Unexpected Claude response: $match_result"
        echo "Skipping draft generation, transcript saved at: $transcript_file"
    fi

    # Move processed audio to archive
    mv "$audio" "$ARCHIVE/"
    echo "=== Archived: $filename ==="
done

echo "Done. Processed ${#audio_files[@]} recording(s)."
