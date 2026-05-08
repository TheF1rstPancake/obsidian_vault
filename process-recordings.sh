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

    # Load schema once per audio file (cheap and keeps the prompt in sync with SCHEMA.md)
    schema_doc=""
    if [ -f "$VAULT/SCHEMA.md" ]; then
        schema_doc=$(cat "$VAULT/SCHEMA.md")
    fi

    # Build context: list existing drafts (folder-per-slug) with the first few lines of article.md
    existing_drafts=""
    for draft_dir in "$DRAFTS"/*/; do
        [ -d "$draft_dir" ] || continue
        article="${draft_dir}article.md"
        [ -f "$article" ] || continue
        draft_name=$(basename "$draft_dir")
        draft_preview=$(head -20 "$article")
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
        draft_file="$DRAFTS/${draft_slug}/article.md"

        if [ ! -f "$draft_file" ]; then
            echo "Warning: Claude matched '$draft_slug' but article not found. Treating as new."
            match_result="NEW: $draft_slug"
        fi
    fi

    # Append the raw transcript to notes.md for a given slug. Creates notes.md
    # with frontmatter on first call. notes.md is append-only and never rewritten.
    append_to_notes() {
        local slug="$1" filename="$2" text="$3"
        local notes="$DRAFTS/$slug/notes.md"
        mkdir -p "$DRAFTS/$slug"
        if [ ! -f "$notes" ]; then
            cat > "$notes" <<EOF
---
slug: $slug
---

EOF
        fi
        {
            printf '## %s — %s\n\n' "$(date '+%Y-%m-%d %H:%M')" "$filename"
            printf '%s\n\n---\n\n' "$text"
        } >> "$notes"
    }

    # Run Claude into a temp file, validate, then atomically install.
    # Returns 0 on success, 1 on failure (empty / too-short / non-markdown output).
    run_claude_to_file() {
        local prompt="$1" target="$2" min_bytes="${3:-40}"
        local tmp
        tmp=$(mktemp "${target}.new.XXXXXX")
        if ! claude -p --output-format json "$prompt" 2>/tmp/claude-err.log \
                | jq -r '.result // .text // empty' > "$tmp"; then
            echo "Warning: claude/jq failed. stderr: $(cat /tmp/claude-err.log)" >&2
            rm -f "$tmp"
            return 1
        fi
        if [ ! -s "$tmp" ] || [ "$(wc -c < "$tmp")" -lt "$min_bytes" ]; then
            echo "Warning: claude output too short ($(wc -c < "$tmp" 2>/dev/null || echo 0) bytes). Keeping existing $target." >&2
            rm -f "$tmp"
            return 1
        fi
        mv "$tmp" "$target"
        return 0
    }

    if [[ "$match_result" == NEW:* ]]; then
        draft_slug=$(echo "$match_result" | sed 's/^NEW: *//')
        draft_dir="$DRAFTS/${draft_slug}"
        draft_file="$draft_dir/article.md"
        mkdir -p "$draft_dir"

        # Preserve the raw transcript first — lossless source, independent of Claude success.
        append_to_notes "$draft_slug" "$filename" "$raw_text"

        gen_prompt="You are turning a raw voice recording transcript into a Substack article draft.

Follow the vault schema below for frontmatter and conventions:

<schema>
$schema_doc
</schema>

The transcript is a rambling voice recording — extract the key ideas and reorganize them into a coherent, readable article draft in markdown. Keep the author's voice and intent. Mark any unclear sections with [?].

Output the complete article.md file (YAML frontmatter + body). Set status to 'raw', target to 'substack', slug to '$draft_slug', and fill in created/updated with today's date ($(date +%Y-%m-%d)).

<transcript>
$raw_text
</transcript>"

        if run_claude_to_file "$gen_prompt" "$draft_file"; then
            echo "=== Created new draft: $draft_file ==="
        else
            echo "=== Draft generation failed; raw transcript preserved in $draft_dir/notes.md ==="
        fi

    elif [[ "$match_result" == MATCH:* ]]; then
        draft_slug=$(echo "$match_result" | sed 's/^MATCH: *//')
        draft_dir="$DRAFTS/${draft_slug}"
        draft_file="$draft_dir/article.md"

        # Append raw transcript to notes.md FIRST so it's preserved even if Claude fails.
        append_to_notes "$draft_slug" "$filename" "$raw_text"

        # Snapshot the existing article so a bad Claude response can't lose work.
        backup="${draft_file}.bak.$(date +%Y%m%d-%H%M%S)"
        cp "$draft_file" "$backup"

        existing_draft=$(cat "$draft_file")
        update_prompt="You are updating a Substack article draft with new information from a voice recording.

Follow the vault schema below for frontmatter and conventions:

<schema>
$schema_doc
</schema>

Here is the current draft:

<current_draft>
$existing_draft
</current_draft>

Here is a new transcript that belongs to this article:

<new_transcript>
$raw_text
</new_transcript>

Update the draft by incorporating the new information. Merge ideas, resolve contradictions (prefer the newer transcript), expand sections, and keep it coherent. Reorganize if warranted. Keep the author's voice. Mark unclear sections with [?].

Preserve the existing slug, created date, and any populated fields (title, tags, substack_url). Bump 'updated' to today ($(date +%Y-%m-%d)). Do not lower the 'status' field.

Output the complete updated article.md file (YAML frontmatter + body)."

        if run_claude_to_file "$update_prompt" "$draft_file"; then
            echo "=== Updated draft: $draft_file (backup: $backup) ==="
        else
            echo "=== Update failed; original draft preserved, backup at $backup ==="
        fi
    else
        echo "Warning: Unexpected Claude response: $match_result"
        echo "Skipping draft generation, transcript saved at: $transcript_file"
    fi

    # Move processed audio to archive
    mv "$audio" "$ARCHIVE/"
    echo "=== Archived: $filename ==="
done

echo "Done. Processed ${#audio_files[@]} recording(s)."
