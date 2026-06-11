#!/usr/bin/env python3
"""Publish an obsidian draft (drafts/<slug>/article.md) to the local Ghost.

- Renders the markdown body to clean HTML (via Ghost's own converter).
- Upserts by slug (updates the existing post, else creates it).
- If the frontmatter has a `point:` field, injects it as a stylized
  "The point" callout (an HTML card) at the very top of the article.
  Idempotent — re-running replaces the existing point card.

Usage:
    python3 ghost-upload.py drafts/<slug>/article.md [--draft]

Reads GHOST_LOCAL_API_KEY from .env (id:secret admin key).
"""
import sys, os, re, json, time, hmac, hashlib, base64, html as htmlmod
import urllib.request, urllib.error

API_URL = "http://100.119.32.88:2368"


def load_key():
    for line in open(os.path.join(os.path.dirname(__file__), ".env")):
        if line.startswith("GHOST_LOCAL_API_KEY="):
            return line.split("=", 1)[1].strip()
    raise SystemExit("GHOST_LOCAL_API_KEY not found in .env")


KID, KSECRET = load_key().split(":")


def b64url(d):
    return base64.urlsafe_b64encode(d).rstrip(b"=").decode()


def jwt():
    now = int(time.time())
    seg = (b64url(json.dumps({"alg": "HS256", "typ": "JWT", "kid": KID}).encode()) + "." +
           b64url(json.dumps({"iat": now, "exp": now + 300, "aud": "/admin/"}).encode()))
    sig = hmac.new(bytes.fromhex(KSECRET), seg.encode(), hashlib.sha256).digest()
    return seg + "." + b64url(sig)


def call(method, path, body=None):
    req = urllib.request.Request(
        API_URL + path,
        data=json.dumps(body).encode() if body else None,
        method=method,
        headers={"Authorization": "Ghost " + jwt(),
                 "Content-Type": "application/json",
                 "Accept-Version": "v5.0"})
    try:
        if method == "DELETE":
            urllib.request.urlopen(req); return {}
        return json.load(urllib.request.urlopen(req))
    except urllib.error.HTTPError as e:
        raise SystemExit(f"{method} {path} -> {e.code}: {e.read().decode()[:400]}")


def parse_article(path):
    raw = open(path).read()
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", raw, re.DOTALL)
    fm, body = (m.group(1), m.group(2)) if m else ("", raw)

    def field(name):
        mm = re.search(rf'^{name}:\s*"?(.*?)"?\s*$', fm, re.MULTILINE)
        return mm.group(1) if mm else None

    title = field("title") or "Untitled"
    slug = field("slug")
    tagm = re.search(r'^tags:\s*\[(.*?)\]', fm, re.MULTILINE)
    tags = [t.strip() for t in tagm.group(1).split(",")] if tagm else []
    # point: folded (>) or plain scalar
    pm = re.search(r'^point:\s*>\s*\n(.*?)(?=\n\S|\Z)', fm + "\n", re.S | re.M)
    if pm:
        point = " ".join(l.strip() for l in pm.group(1).splitlines() if l.strip())
    else:
        point = field("point")
    # drop a leading H1 that duplicates the title
    body = re.sub(r'^#\s+.*\n+', '', body.lstrip("\n"), count=1).strip()
    return title, slug, tags, point, body


def render_html(body_md):
    """Render markdown to HTML locally using python-markdown with footnote support."""
    import markdown as md_lib
    extensions = ["footnotes", "tables", "fenced_code", "attr_list", "def_list", "nl2br"]
    return md_lib.markdown(body_md, extensions=extensions)


def point_card(point):
    txt = htmlmod.escape(point, quote=False)
    return {"type": "html", "version": 1,
            "html": f'<div class="article-point"><span class="ap-label">The point</span>'
                    f'<p class="ap-text">{txt}</p></div>'}


# Obsidian/GitHub callout syntax:  > [!type] Optional Title  /  > body...
CALLOUT_KIND = {"note": "note", "info": "note", "example": "note", "quote": "note",
                "tip": "tip", "hint": "tip",
                "warning": "warning", "caution": "warning", "danger": "warning"}
CALLOUT_TITLE = {"note": "Note", "tip": "Tip", "warning": "Warning"}
PLACEHOLDER = "CALLOUTCARDPLACEHOLDER{}"


def extract_callouts(body):
    """Pull `> [!type]` blocks out of the markdown, leaving a placeholder line
    where each was. Returns (body_with_placeholders, [callout, ...])."""
    lines = body.split("\n")
    out, callouts = [], []
    i = 0
    while i < len(lines):
        m = re.match(r'^>\s*\[!(\w+)\]\s*(.*)$', lines[i])
        if m:
            ctype = m.group(1).lower()
            inner = []
            i += 1
            while i < len(lines) and lines[i].lstrip().startswith(">"):
                inner.append(re.sub(r'^\s*>\s?', '', lines[i]))
                i += 1
            kind = CALLOUT_KIND.get(ctype, "note")
            title = m.group(2).strip() or CALLOUT_TITLE[kind]
            out += ["", PLACEHOLDER.format(len(callouts)), ""]
            callouts.append({"kind": kind, "title": title, "md": "\n".join(inner).strip()})
        else:
            out.append(lines[i]); i += 1
    return "\n".join(out), callouts


def callout_card(c):
    inner = render_html(c["md"]).strip()
    title = htmlmod.escape(c["title"], quote=False)
    return {"type": "html", "version": 1,
            "html": f'<aside class="callout callout-{c["kind"]}">'
                    f'<p class="callout-title">{title}</p>'
                    f'<div class="callout-body">{inner}</div></aside>'}


def node_text(node):
    # Ghost lexical text nodes are type "extended-text" (not "text"), so match
    # on the presence of a string `text` field rather than the node type.
    if isinstance(node.get("text"), str):
        return node["text"]
    return "".join(node_text(ch) for ch in node.get("children", []))


def find_by_slug(slug):
    try:
        r = call("GET", f"/ghost/api/admin/posts/slug/{slug}/")
        return r["posts"][0]
    except SystemExit:
        return None


def main():
    if len(sys.argv) < 2:
        raise SystemExit(__doc__)
    path = sys.argv[1]
    status = "draft" if "--draft" in sys.argv[1:] else "published"
    title, slug, tags, point, body = parse_article(path)
    body, callouts = extract_callouts(body)

    html = render_html(body)
    payload = {"title": title, "html": html, "status": status,
               "tags": [{"name": t} for t in tags]}
    if slug:
        payload["slug"] = slug

    existing = find_by_slug(slug) if slug else None
    if existing:
        payload["updated_at"] = existing["updated_at"]
        post = call("PUT", f"/ghost/api/admin/posts/{existing['id']}/?source=html",
                    {"posts": [payload]})["posts"][0]
        action = "updated"
    else:
        post = call("POST", "/ghost/api/admin/posts/?source=html",
                    {"posts": [payload]})["posts"][0]
        action = "created"

    # second pass on the lexical: swap callout placeholders for cards, prepend the point
    if point or callouts:
        cur = call("GET", f"/ghost/api/admin/posts/{post['id']}/?formats=lexical")["posts"][0]
        doc = json.loads(cur["lexical"])
        if callouts:
            cards = {PLACEHOLDER.format(i): callout_card(c) for i, c in enumerate(callouts)}
            doc["root"]["children"] = [
                cards.get(node_text(n).strip(), n) for n in doc["root"]["children"]]
        if point:
            kids = [n for n in doc["root"]["children"]
                    if not (n.get("type") == "html" and "article-point" in (n.get("html") or ""))]
            doc["root"]["children"] = [point_card(point)] + kids
        post = call("PUT", f"/ghost/api/admin/posts/{post['id']}/",
                    {"posts": [{"lexical": json.dumps(doc), "updated_at": cur["updated_at"]}]})["posts"][0]

    print(f"{action} [{post['status']}] {post.get('url')}")
    print(f"  point: {'yes' if point else 'none'} | callouts: {len(callouts)} | tags: {', '.join(tags) or 'none'}")


if __name__ == "__main__":
    main()
