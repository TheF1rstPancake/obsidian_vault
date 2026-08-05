#!/usr/bin/env bash
# Enrichment-only cron entrypoint.
#
# Transcription is handled by the persistent worker:
#   scripts/transcribe_worker.py  (systemd: obsidian-transcribe.service)
#   scripts/transcribe-ctl status|queued|logs|...
#
# This script only turns transcripts/ (without a drafted: stamp) into drafts/.
# Audio in recordings/ is left alone — never claim GPU from cron.
set -euo pipefail

VAULT="$HOME/obsidian-vault"
TRANSCRIPTS="$VAULT/transcripts"
DRAFTS="$VAULT/drafts"
LOCKFILE="/tmp/process-recordings-enrich.lock"

# Prevent concurrent enrichment runs (safe to overlap with the transcribe worker).
if [ -f "$LOCKFILE" ]; then
    pid=$(cat "$LOCKFILE")
    if kill -0 "$pid" 2>/dev/null; then
        echo "Enrichment already running (pid $pid), exiting."
        exit 0
    fi
fi
echo $$ > "$LOCKFILE"
trap 'rm -f "$LOCKFILE"' EXIT

# ─────────────────────────────────────────────────────────────────────────────
# Helpers
# ─────────────────────────────────────────────────────────────────────────────

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

# Run Claude into a temp file, validate, sanitize, then atomically install.
# Returns 0 on success, 1 on failure (empty / too-short / truncated / non-markdown output).
#
# Sanitization (defense-in-depth, since LLMs occasionally ignore prompt instructions):
#   - Strip a leading ```<lang> fence and a trailing ``` fence if Claude wrapped the
#     whole response as a code block.
#   - Strip a trailing meta-commentary paragraph (e.g. "I added ..." / "Added a new ...")
#     if — and only if — it is the LAST paragraph in the file. This used to be a
#     greedy `pattern,$d` sed range-delete, which silently truncated everything
#     after the FIRST matching line anywhere in the file — including legitimate
#     article content (e.g. a body paragraph that happens to start with "Note:").
#     Scoping the check to the last paragraph only fixes that.
# The article body itself must start with `---` (YAML frontmatter), so any content
# before the first `---` line is safe to drop.
#
# source_text (optional 4th arg): the raw transcript this article was generated
# from. When given, the generated output is rejected if its word count is
# suspiciously low relative to the transcript's — catches a model that stops
# generating partway through instead of covering the whole transcript (which
# passes the min_bytes check trivially since it produces well-formed output,
# just incomplete output).
run_claude_to_file() {
    local prompt="$1" target="$2" min_bytes="${3:-40}" source_text="${4:-}"
    local tmp tmp2
    tmp=$(mktemp "${target}.new.XXXXXX")
    if ! claude -p --output-format json "$prompt" 2>/tmp/claude-err.log \
            | jq -r '.result // .text // empty' > "$tmp"; then
        echo "Warning: claude/jq failed. stderr: $(cat /tmp/claude-err.log)" >&2
        rm -f "$tmp"
        return 1
    fi

    # Sanitize: drop anything before the first '---' (frontmatter start), strip
    # a single matching pair of code fences if present, and drop trailing fences/commentary.
    tmp2=$(mktemp "${target}.clean.XXXXXX")
    awk '
        BEGIN { started = 0 }
        # Skip everything until we see the YAML frontmatter opener.
        !started && /^---[[:space:]]*$/ { started = 1; print; next }
        !started { next }
        # Once started, drop any line that is a bare code fence.
        started && /^```[[:alnum:]]*[[:space:]]*$/ { next }
        started { print }
    ' "$tmp" > "$tmp2"

    # Drop a trailing meta-commentary paragraph, but only check the LAST
    # paragraph (the block of lines after the last blank line) — never a range
    # delete from an arbitrary matching line to end-of-file.
    last_para_start=$(awk 'BEGIN{p=0} /^[[:space:]]*$/{p=NR} END{print p+1}' "$tmp2")
    if [ "$last_para_start" -gt 1 ] && \
       sed -n "${last_para_start}p" "$tmp2" | grep -qE '^(Added |I added |Here is |Here'\''s |Note: |Summary: )'; then
        head -n $((last_para_start - 1)) "$tmp2" > "${tmp2}.trim"
        mv "${tmp2}.trim" "$tmp2"
    fi
    # Trim trailing blank lines.
    sed -i -e :a -e '/^[[:space:]]*$/{$d;N;ba' -e '}' "$tmp2"

    rm -f "$tmp"

    if [ ! -s "$tmp2" ] || [ "$(wc -c < "$tmp2")" -lt "$min_bytes" ]; then
        echo "Warning: claude output too short after sanitize ($(wc -c < "$tmp2" 2>/dev/null || echo 0) bytes). Keeping existing $target." >&2
        rm -f "$tmp2"
        return 1
    fi

    # Completeness check: reject output that's suspiciously short relative to
    # the source transcript — a sign the model stopped generating partway
    # through instead of covering the whole thing. Well-formed but incomplete
    # output otherwise sails through every check above.
    if [ -n "$source_text" ]; then
        local source_words body_words min_words
        source_words=$(printf '%s' "$source_text" | wc -w)
        body_words=$(wc -w < "$tmp2")
        min_words=$(( source_words * 3 / 10 ))
        [ "$min_words" -lt 120 ] && min_words=120
        if [ "$body_words" -lt "$min_words" ]; then
            echo "Warning: claude output looks truncated ($body_words words vs ~$source_words-word transcript, need >=$min_words). Keeping existing $target." >&2
            rm -f "$tmp2"
            return 1
        fi
    fi

    # Final sanity: must begin with YAML frontmatter.
    if ! head -1 "$tmp2" | grep -qE '^---[[:space:]]*$'; then
        echo "Warning: sanitized output does not start with YAML frontmatter. Keeping existing $target." >&2
        rm -f "$tmp2"
        return 1
    fi
    mv "$tmp2" "$target"
    return 0
}

# Extract the source audio filename recorded in a transcript's frontmatter.
transcript_source() {
    sed -n 's/^source: //p' "$1" | head -1
}

# Extract the raw transcript text: everything after the "# Transcript:" heading,
# dropping the single blank line that follows the heading.
transcript_body() {
    awk 'started { print } /^# Transcript: /{ started = 1 }' "$1" | sed '1{/^[[:space:]]*$/d;}'
}

# Stamp a transcript as enriched so Phase 2 won't reprocess it on later runs.
mark_drafted() {
    grep -q '^drafted:' "$1" || sed -i "/^transcribed:/a drafted: $(date -Iseconds)" "$1"
}

# Turn one transcript into a new draft, or fold it into a matching existing draft.
# Args: raw_text, source_filename, transcript_file
# Returns 0 if enrichment ran (caller stamps it 'drafted'); returns 1 if Claude was
# unavailable, leaving the transcript unstamped so a later run retries it.
enrich_transcript() {
    local raw_text="$1" filename="$2" transcript_file="$3"

    # Load schema once (keeps the prompt in sync with SCHEMA.md)
    local schema_doc=""
    if [ -f "$VAULT/SCHEMA.md" ]; then
        schema_doc=$(cat "$VAULT/SCHEMA.md")
    fi

    # Load the style guide so the automated writer path matches Giovanni's voice
    # (keeps the cron prompt in sync with STYLE.md). Bounded — the file is short.
    local style_doc=""
    if [ -f "$VAULT/STYLE.md" ]; then
        style_doc=$(cat "$VAULT/STYLE.md")
    fi

    # Build context: list existing drafts (folder-per-slug) with the first few lines of article.md
    local existing_drafts="" draft_dir article draft_name draft_preview
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

    local match_result match_prompt slug_prompt
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

        match_result=$(claude -p --output-format json "$match_prompt" 2>/dev/null | jq -r '.result // .text // .' | head -1 || true)
    else
        # No existing drafts, ask Claude for a slug
        slug_prompt="Given this transcript from a voice recording, suggest a short kebab-case filename slug (2-5 words) that captures the main topic. Respond with EXACTLY one line like: NEW: my-topic-slug

<transcript>
$raw_text
</transcript>"

        match_result=$(claude -p --output-format json "$slug_prompt" 2>/dev/null | jq -r '.result // .text // .' | head -1 || true)
    fi

    echo "=== Claude says: $match_result ==="

    # An empty response means Claude was unavailable (e.g. logged out). Do NOT stamp
    # the transcript — return non-zero so the next run retries enrichment. The audio
    # is already archived, so this is the only path by which the draft ever gets made.
    if [ -z "$match_result" ]; then
        echo "=== Claude unavailable — leaving '$(basename "$transcript_file")' unstamped for retry ==="
        return 1
    fi

    local draft_slug draft_file draft_dir backup existing_draft gen_prompt update_prompt
    if [[ "$match_result" == MATCH:* ]]; then
        draft_slug=$(echo "$match_result" | sed 's/^MATCH: *//')
        draft_file="$DRAFTS/${draft_slug}/article.md"

        if [ ! -f "$draft_file" ]; then
            echo "Warning: Claude matched '$draft_slug' but article not found. Treating as new."
            match_result="NEW: $draft_slug"
        fi
    fi

    if [[ "$match_result" == NEW:* ]]; then
        draft_slug=$(echo "$match_result" | sed 's/^NEW: *//')
        draft_dir="$DRAFTS/${draft_slug}"
        draft_file="$draft_dir/article.md"
        mkdir -p "$draft_dir"

        # Preserve the raw transcript first — lossless source, independent of Claude success.
        append_to_notes "$draft_slug" "$filename" "$raw_text"

        gen_prompt="You are turning a raw voice recording transcript into a Ghost article draft.

Follow the vault schema below for frontmatter and conventions:

<schema>
$schema_doc
</schema>

Match the author's voice using the style guide below. The most load-bearing rules: keep the author's actual ideas and ordering, prefer conditional claims over universal doctrine, reduce em dashes (a staccato period-driven style is fine), don't invent ceremony or fake authority, and keep concrete specifics over generic business prose.

<style_guide>
$style_doc
</style_guide>

The transcript is a rambling voice recording — extract the key ideas and reorganize them into a coherent, readable article draft in markdown. Keep the author's voice and intent. Mark any unclear sections with [?].

Output the complete article.md file (YAML frontmatter + body). Set status to 'raw', target to 'ghost', slug to '$draft_slug', and fill in created/updated with today's date ($(date +%Y-%m-%d)).

CRITICAL OUTPUT RULES (the output is written verbatim to a .md file by a script):
- Begin your response with the literal characters \`---\` on line 1 (the YAML frontmatter opener). Nothing before it.
- End your response with the final line of the article body. No trailing commentary, summary, or 'Added X' note.
- Do NOT wrap the response in code fences (no \`\`\`markdown opener, no \`\`\` closer). Output raw markdown.
- Do NOT prefix or suffix the article with any meta-text about what you did.

<transcript>
$raw_text
</transcript>"

        if run_claude_to_file "$gen_prompt" "$draft_file" 40 "$raw_text"; then
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
        update_prompt="You are updating a Ghost article draft with new information from a voice recording.

Follow the vault schema below for frontmatter and conventions:

<schema>
$schema_doc
</schema>

Match the author's voice using the style guide below. The most load-bearing rules: keep the author's actual ideas and ordering, prefer conditional claims over universal doctrine, reduce em dashes (a staccato period-driven style is fine), don't invent ceremony or fake authority, and keep concrete specifics over generic business prose.

<style_guide>
$style_doc
</style_guide>

Here is the current draft:

<current_draft>
$existing_draft
</current_draft>

Here is a new transcript that belongs to this article:

<new_transcript>
$raw_text
</new_transcript>

Update the draft by incorporating the new information. Merge ideas, resolve contradictions (prefer the newer transcript), expand sections, and keep it coherent. Reorganize if warranted. Keep the author's voice. Mark unclear sections with [?].

Preserve the existing slug, created date, and any populated fields (title, tags, point, substack_url). Bump 'updated' to today ($(date +%Y-%m-%d)). Do not lower the 'status' field. Do not invent a 'point' field if the existing draft doesn't have one — that's an interactive shaping step, not an automated one.

Output the complete updated article.md file (YAML frontmatter + body).

CRITICAL OUTPUT RULES (the output is written verbatim to a .md file by a script):
- Begin your response with the literal characters \`---\` on line 1 (the YAML frontmatter opener). Nothing before it.
- End your response with the final line of the article body. No trailing commentary, summary, or 'Added X' note.
- Do NOT wrap the response in code fences (no \`\`\`markdown opener, no \`\`\` closer). Output raw markdown.
- Do NOT prefix or suffix the article with any meta-text about what you did."

        if run_claude_to_file "$update_prompt" "$draft_file" 40 "$raw_text"; then
            echo "=== Updated draft: $draft_file (backup: $backup) ==="
        else
            echo "=== Update failed; original draft preserved, backup at $backup ==="
        fi
    else
        echo "Warning: Unexpected Claude response: $match_result"
        echo "Skipping draft generation, transcript saved at: $transcript_file"
    fi

    return 0
}

# ─────────────────────────────────────────────────────────────────────────────
# Enrich every transcript that hasn't been turned into a draft yet.
# The transcribe worker archives audio as soon as a transcript lands, so a
# Claude outage never re-queues audio. Transcripts left unstamped by a previous
# Claude outage get retried until they succeed — self-healing, never dropped.
# ─────────────────────────────────────────────────────────────────────────────
enriched=0
awaiting=0
shopt -s nullglob
for transcript_file in "$TRANSCRIPTS"/*.md; do
    # Already enriched? Skip.
    if grep -q '^drafted:' "$transcript_file"; then
        continue
    fi

    src=$(transcript_source "$transcript_file")
    [ -n "$src" ] || src=$(basename "$transcript_file")
    body=$(transcript_body "$transcript_file")
    if [ -z "$body" ]; then
        echo "Skipping empty transcript: $(basename "$transcript_file")"
        continue
    fi

    echo "=== Enriching: $(basename "$transcript_file") (source: $src) ==="
    if enrich_transcript "$body" "$src" "$transcript_file"; then
        mark_drafted "$transcript_file"
        enriched=$((enriched + 1))
    else
        awaiting=$((awaiting + 1))
    fi
done
shopt -u nullglob

echo "Done. Enriched $enriched transcript(s); $awaiting awaiting retry."
