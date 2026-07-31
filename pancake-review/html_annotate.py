"""Inject pancake-review annotation chrome into full HTML artifacts.

HTML hub docs are served as complete documents (their own CSS/JS) so design
comps keep looking right.  This module splices a namespaced overlay into the
response: Home/Edit topbar, highlight marks, FAB + note sheet, and the same
``/annotations`` API used by the markdown reader.

**Target scheme (HTML):**

* ``highlighted_text`` — required quote (same field as markdown annotations)
* ``locator`` — optional CSS selector for the nearest block containing the
  selection; preferred search scope when re-rendering
* fallback — document-wide first text-node match (markdown behavior)

Anchors are best-effort.  If the HTML is rewritten and the quote/locator no
longer match, the note still persists in the store and shows as unmatched.
"""
from __future__ import annotations

import html as html_mod
import json
import re

# Marker so tests / smoke checks can detect injected chrome without coupling
# to markdown's #article-body.
INJECT_MARKER = "data-pancake-html-annotate"

_HEAD_RE = re.compile(r"(?i)</head\s*>")
_BODY_RE = re.compile(r"(?i)</body\s*>")


def inject_annotation_chrome(raw_html: str, *, slug: str, file: str, edit_url: str) -> str:
    """Return ``raw_html`` with pancake annotation overlay spliced in."""
    css = _ANNOTATE_CSS
    body = _annotate_body(slug=slug, file=file, edit_url=edit_url)

    out = raw_html
    if _HEAD_RE.search(out):
        out = _HEAD_RE.sub(f"<style id=\"pancake-annotate-css\">{css}</style>\n</head>", out, count=1)
    else:
        out = f"<style id=\"pancake-annotate-css\">{css}</style>\n{out}"

    if _BODY_RE.search(out):
        out = _BODY_RE.sub(f"{body}\n</body>", out, count=1)
    else:
        out = f"{out}\n{body}"
    return out


def _annotate_body(*, slug: str, file: str, edit_url: str) -> str:
    slug_js = json.dumps(slug)
    file_js = json.dumps(file)
    edit_esc = html_mod.escape(edit_url, quote=True)
    return f"""
<div id="pancake-ui" {INJECT_MARKER}="1">
  <div class="pr-topbar">
    <a href="/">← Home</a>
    <a class="pr-edit" href="{edit_esc}">Edit source</a>
    <span class="pr-count" id="pr-note-count"></span>
  </div>
  <button id="pr-add-btn" class="idle" type="button" title="Add note to selection">✏️</button>
  <div class="pr-sheet-backdrop" id="pr-sheet">
    <div class="pr-sheet" id="pr-sheet-inner"></div>
  </div>
  <div id="pr-toast"></div>
</div>
<script id="pancake-annotate-js">
(function () {{
  const SLUG = {slug_js};
  const FILE = {file_js};
  const ui = document.getElementById("pancake-ui");
  const addBtn = document.getElementById("pr-add-btn");
  const sheet = document.getElementById("pr-sheet");
  const sheetInner = document.getElementById("pr-sheet-inner");
  const noteCount = document.getElementById("pr-note-count");
  let pendingText = "";
  let pendingLocator = "";

  function searchRoot() {{
    return document.body;
  }}

  function inUi(node) {{
    return !!(node && node.nodeType && (node === ui || (node.nodeType === 1 ? node : node.parentElement)?.closest("#pancake-ui")));
  }}

  let toastTimer;
  function toast(msg) {{
    const t = document.getElementById("pr-toast");
    t.textContent = msg;
    t.classList.add("show");
    clearTimeout(toastTimer);
    toastTimer = setTimeout(() => t.classList.remove("show"), 1800);
  }}

  // CSS path to a stable-enough block for design-review re-anchoring.
  function cssLocator(el) {{
    if (!el || el === document.body || el === document.documentElement) return "";
    if (el.id && !String(el.id).startsWith("pr-") && el.id !== "pancake-ui") {{
      try {{
        if (document.querySelectorAll("#" + CSS.escape(el.id)).length === 1)
          return "#" + CSS.escape(el.id);
      }} catch (e) {{}}
    }}
    const parts = [];
    let cur = el;
    while (cur && cur.nodeType === 1 && cur !== document.body) {{
      if (cur.id === "pancake-ui" || cur.closest && cur.closest("#pancake-ui")) break;
      let part = cur.tagName.toLowerCase();
      const parent = cur.parentElement;
      if (parent) {{
        const siblings = Array.from(parent.children).filter((c) => c.tagName === cur.tagName);
        if (siblings.length > 1) {{
          part += ":nth-of-type(" + (siblings.indexOf(cur) + 1) + ")";
        }}
      }}
      parts.unshift(part);
      if (parts.length >= 8) break;
      cur = parent;
    }}
    return parts.join(" > ");
  }}

  function nearestBlock(node) {{
    let el = node && node.nodeType === 3 ? node.parentElement : node;
    while (el && el !== document.body) {{
      if (el.id === "pancake-ui") return null;
      if (/^(P|H[1-6]|LI|TD|TH|BLOCKQUOTE|FIGCAPTION|LABEL|BUTTON|SUMMARY|DT|DD|ARTICLE|SECTION|DIV)$/i.test(el.tagName)) {{
        // Prefer smaller text-ish blocks over giant layout wrappers.
        if (/^(DIV|SECTION|ARTICLE)$/i.test(el.tagName)) {{
          const text = (el.innerText || "").trim();
          if (text.length > 800) {{
            el = el.parentElement;
            continue;
          }}
        }}
        return el;
      }}
      el = el.parentElement;
    }}
    return node && node.parentElement;
  }}

  function wrapIn(root, text, anno) {{
    if (!text || !root) return false;
    const walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT, {{
      acceptNode: (n) => {{
        if (inUi(n)) return NodeFilter.FILTER_REJECT;
        if (n.parentElement && n.parentElement.closest("mark.pr-anno"))
          return NodeFilter.FILTER_REJECT;
        return NodeFilter.FILTER_ACCEPT;
      }},
    }});
    let node;
    while ((node = walker.nextNode())) {{
      const idx = node.nodeValue.indexOf(text);
      if (idx === -1) continue;
      const range = document.createRange();
      range.setStart(node, idx);
      range.setEnd(node, idx + text.length);
      const mark = document.createElement("mark");
      mark.className = "pr-anno";
      mark.dataset.id = anno.id;
      mark.dataset.comment = anno.comment;
      mark.dataset.resolved = anno.resolved ? "1" : "0";
      if (anno.locator) mark.dataset.locator = anno.locator;
      try {{
        range.surroundContents(mark);
      }} catch (e) {{
        return false;
      }}
      mark.addEventListener("click", (ev) => {{
        ev.stopPropagation();
        showComment(mark);
      }});
      return true;
    }}
    return false;
  }}

  function wrapAnnotation(anno) {{
    const text = anno.highlighted_text || "";
    if (anno.locator) {{
      try {{
        const scoped = document.querySelector(anno.locator);
        if (scoped && !inUi(scoped) && wrapIn(scoped, text, anno)) return true;
      }} catch (e) {{}}
    }}
    return wrapIn(searchRoot(), text, anno);
  }}

  async function loadAnnotations() {{
    try {{
      const res = await fetch("/annotations/" + encodeURIComponent(SLUG) + "?file=" + encodeURIComponent(FILE));
      const data = await res.json();
      const list = data.annotations || [];
      let shown = 0;
      for (const a of list) if (wrapAnnotation(a)) shown++;
      const n = list.length;
      noteCount.textContent = n
        ? n + " note" + (n === 1 ? "" : "s") + (shown < n ? " (" + (n - shown) + " unmatched)" : "")
        : "";
    }} catch (e) {{
      noteCount.textContent = "";
    }}
  }}

  document.addEventListener("selectionchange", () => {{
    const sel = window.getSelection();
    if (!sel || sel.isCollapsed) return;
    const text = sel.toString().trim();
    if (!text) return;
    if (inUi(sel.anchorNode) || inUi(sel.focusNode)) return;
    pendingText = text;
    const block = nearestBlock(sel.anchorNode);
    pendingLocator = block ? cssLocator(block) : "";
    addBtn.classList.remove("idle");
  }});

  addBtn.addEventListener("touchstart", (e) => {{
    e.preventDefault();
    if (!pendingText) {{ toast("Select some text first"); return; }}
    handleAddNote();
  }}, {{ passive: false }});
  addBtn.addEventListener("click", () => {{
    if (!pendingText) {{ toast("Select some text first"); return; }}
    handleAddNote();
  }});

  function openSheet(html) {{
    sheetInner.innerHTML = html;
    sheet.classList.add("open");
  }}
  function closeSheet() {{
    sheet.classList.remove("open");
    sheetInner.innerHTML = "";
    pendingText = "";
    pendingLocator = "";
    addBtn.classList.add("idle");
  }}
  sheet.addEventListener("click", (e) => {{ if (e.target === sheet) closeSheet(); }});

  function handleAddNote() {{
    const text = pendingText;
    const locator = pendingLocator;
    if (!text) return;
    openSheet(
      '<div class="pr-quote">' + escapeHtml(text) + '</div>' +
      (locator ? '<div class="pr-locator">@ ' + escapeHtml(locator) + '</div>' : '') +
      '<textarea id="pr-note-input" placeholder="Your note about this passage…"></textarea>' +
      '<div class="pr-sheet-row">' +
      '<button type="button" id="pr-cancel-btn">Cancel</button>' +
      '<button type="button" id="pr-save-btn" class="primary">Save note</button>' +
      '</div>'
    );
    const ta = document.getElementById("pr-note-input");
    ta.focus();
    document.getElementById("pr-cancel-btn").onclick = closeSheet;
    document.getElementById("pr-save-btn").onclick = () => saveNote(text, ta.value, locator);
  }}

  async function saveNote(text, comment, locator) {{
    comment = (comment || "").trim();
    if (!comment) {{ toast("Write a note first"); return; }}
    const saveBtn = document.getElementById("pr-save-btn");
    if (saveBtn) saveBtn.disabled = true;
    try {{
      const payload = {{ slug: SLUG, file: FILE, highlighted_text: text, comment }};
      if (locator) payload.locator = locator;
      const res = await fetch("/annotations", {{
        method: "POST",
        headers: {{ "Content-Type": "application/json" }},
        body: JSON.stringify(payload),
      }});
      if (!res.ok) throw new Error(await res.text());
      const anno = await res.json();
      closeSheet();
      window.getSelection().removeAllRanges();
      wrapAnnotation(anno);
      await refreshCount();
      toast("Note saved ✓");
    }} catch (e) {{
      if (saveBtn) saveBtn.disabled = false;
      toast("Save failed");
    }}
  }}

  async function refreshCount() {{
    const res = await fetch("/annotations/" + encodeURIComponent(SLUG) + "?file=" + encodeURIComponent(FILE));
    const data = await res.json();
    const n = (data.annotations || []).length;
    noteCount.textContent = n ? n + " note" + (n === 1 ? "" : "s") : "";
  }}

  function showComment(mark) {{
    document.querySelectorAll("mark.pr-anno.active").forEach((m) => m.classList.remove("active"));
    mark.classList.add("active");
    openSheet(
      '<div class="pr-quote">' + escapeHtml(mark.textContent) + '</div>' +
      '<p class="pr-comment-body">' + escapeHtml(mark.dataset.comment) + '</p>' +
      (mark.dataset.resolved === "1" ? '<p class="pr-resolved">✓ resolved</p>' : '') +
      '<div class="pr-sheet-row"><button type="button" id="pr-close-btn" class="primary">Close</button></div>'
    );
    document.getElementById("pr-close-btn").onclick = () => {{
      mark.classList.remove("active");
      closeSheet();
    }};
  }}

  function escapeHtml(s) {{
    const d = document.createElement("div");
    d.textContent = s;
    return d.innerHTML;
  }}

  loadAnnotations();
}})();
</script>
"""


_ANNOTATE_CSS = """
#pancake-ui { all: initial; }
#pancake-ui, #pancake-ui * {
  box-sizing: border-box;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
}
#pancake-ui .pr-topbar {
  position: fixed; top: 0; left: 0; right: 0; z-index: 2147483000;
  background: rgba(255,255,255,.94);
  backdrop-filter: saturate(1.4) blur(8px);
  border-bottom: 1px solid #e9e9ec;
  padding: 10px 16px;
  display: flex; align-items: center; gap: 12px;
  color: #1d1d1f;
  font-size: 14px;
  line-height: 1.3;
}
#pancake-ui .pr-topbar a {
  color: #c47a2c; text-decoration: none; font-weight: 600; font-size: 0.9rem;
}
#pancake-ui .pr-topbar .pr-edit { margin-left: auto; }
#pancake-ui .pr-topbar .pr-count { color: #6b6b70; font-size: 0.82rem; }
mark.pr-anno {
  background: #fff3a0 !important;
  box-shadow: inset 0 -2px 0 #f2d94e;
  border-radius: 2px;
  cursor: pointer;
  padding: 0 1px;
  color: inherit;
}
mark.pr-anno.active { background: #ffe04d !important; }
#pancake-ui #pr-add-btn {
  position: fixed; z-index: 2147483001;
  bottom: calc(28px + env(safe-area-inset-bottom, 0px));
  right: 22px;
  width: 52px; height: 52px; border-radius: 50%;
  background: #1d1d1f; color: #fff; border: none;
  font-size: 1.35rem; line-height: 1;
  box-shadow: 0 4px 14px rgba(0,0,0,.28); cursor: pointer;
  touch-action: none;
  display: flex; align-items: center; justify-content: center;
  opacity: 0.85;
}
#pancake-ui #pr-add-btn.idle { opacity: 0.38; }
#pancake-ui #pr-add-btn:active { transform: scale(0.92); opacity: 1; }
#pancake-ui .pr-sheet-backdrop {
  position: fixed; inset: 0; z-index: 2147483002; background: rgba(0,0,0,.28);
  display: none; align-items: flex-end; justify-content: center;
}
#pancake-ui .pr-sheet-backdrop.open { display: flex; }
#pancake-ui .pr-sheet {
  width: 100%; max-width: 680px; background: #fff; color: #1d1d1f;
  border-radius: 18px 18px 0 0; padding: 18px 18px calc(18px + env(safe-area-inset-bottom, 0px));
  box-shadow: 0 -8px 30px rgba(0,0,0,.18);
}
#pancake-ui .pr-quote {
  font-size: 0.86rem; color: #6b6b70; background: #fff3a0;
  border-radius: 8px; padding: 8px 10px; margin: 0 0 8px; max-height: 5.5em; overflow: auto;
}
#pancake-ui .pr-locator {
  font-size: 0.72rem; color: #8a8a90; font-family: ui-monospace, SFMono-Regular, Menlo, monospace;
  margin: 0 0 10px; word-break: break-all;
}
#pancake-ui .pr-sheet textarea {
  width: 100%; min-height: 96px; border: 1px solid #e9e9ec; border-radius: 10px;
  padding: 10px 12px; font-size: 1rem; font-family: inherit; resize: vertical;
  color: #1d1d1f; background: #fff;
}
#pancake-ui .pr-sheet-row { display: flex; gap: 10px; margin-top: 12px; }
#pancake-ui .pr-sheet button {
  flex: 1; padding: 12px; border-radius: 10px; font-size: 0.95rem; font-weight: 600;
  border: 1px solid #e9e9ec; background: #f4f4f2; color: #1d1d1f; cursor: pointer;
}
#pancake-ui .pr-sheet button.primary { background: #c47a2c; color: #fff; border-color: #c47a2c; }
#pancake-ui .pr-sheet button:disabled { opacity: .5; }
#pancake-ui .pr-comment-body {
  font-size: 1rem; line-height: 1.5; white-space: pre-wrap; margin: 4px 0 0; color: #1d1d1f;
}
#pancake-ui .pr-resolved { font-size: 0.78rem; color: #1f7a3d; }
#pancake-ui #pr-toast {
  position: fixed; left: 50%; bottom: 28px; transform: translateX(-50%) translateY(20px);
  background: #1d1d1f; color: #fff; padding: 10px 18px; border-radius: 999px;
  font-size: 0.88rem; opacity: 0; pointer-events: none;
  transition: opacity .2s, transform .2s; z-index: 2147483003;
}
#pancake-ui #pr-toast.show { opacity: 1; transform: translateX(-50%) translateY(0); }
/* Keep page content clear of the fixed topbar */
body { scroll-padding-top: 52px; }
"""
