#!/usr/bin/env python3
"""Publish an obsidian draft (drafts/<slug>/article.md) to the local Ghost.

- Renders the markdown body to clean HTML (via Ghost's own converter).
- Upserts by slug (updates the existing post, else creates it).
- If the frontmatter has a `point:` field, injects it as a stylized
  "The point" callout (an HTML card) at the very top of the article.
  Idempotent — re-running replaces the existing point card.

Usage:
    python3 ghost-upload.py drafts/<slug>/article.md [--draft] [--page] [--target local|hosted]

Targets:
    local  (default) -> http://100.119.32.88:2368, key from GHOST_LOCAL_API_KEY
    hosted           -> GHOST_HOSTED_URL, key from GHOST_HOSTED_API_KEY

Flags:
    --page  publish to /ghost/api/admin/pages/ instead of /posts/ (standalone resources)

Both keys are id:secret Ghost Admin API keys read from .env.

Paywall:
    Frontmatter `visibility: public|members|paid` (default public) sets post-level access.
    A `---paywall---` line on its own in the body splits the article: everything below it
    is gated to members via an injected <!--members-only--> Ghost card.
"""
import sys, os, re, json, time, hmac, hashlib, base64, html as htmlmod
import urllib.request, urllib.error

LOCAL_URL = "http://100.119.32.88:2368"

# Set by configure() once the --target flag is parsed.
API_URL = LOCAL_URL
KID = KSECRET = None


def env_val(name):
    """Return the value of `name` from .env, or None if absent."""
    try:
        for line in open(os.path.join(os.path.dirname(__file__), ".env")):
            if line.startswith(name + "="):
                return line.split("=", 1)[1].strip()
    except FileNotFoundError:
        pass
    return None


def configure(target):
    """Resolve API URL + admin key for the chosen target and set globals."""
    global API_URL, KID, KSECRET
    if target == "hosted":
        url = env_val("GHOST_HOSTED_URL")
        key = env_val("GHOST_HOSTED_API_KEY")
        if not url or url in ("FILL_ME_IN", "https://yoursite.ghost.io"):
            raise SystemExit("GHOST_HOSTED_URL not set in .env (still a placeholder)")
        if not key or key == "FILL_ME_IN":
            raise SystemExit("GHOST_HOSTED_API_KEY not set in .env (still a placeholder)")
        API_URL = url.rstrip("/")
    else:
        key = env_val("GHOST_LOCAL_API_KEY")
        if not key:
            raise SystemExit("GHOST_LOCAL_API_KEY not found in .env")
        API_URL = LOCAL_URL
    if ":" not in key:
        raise SystemExit(f"key for target '{target}' is not in id:secret form")
    KID, KSECRET = key.split(":")


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
    visibility = field("visibility") or "public"
    if visibility not in ("public", "members", "paid"):
        raise SystemExit(f"invalid visibility '{visibility}' (use public|members|paid)")
    tagm = re.search(r'^tags:\s*\[(.*?)\]', fm, re.MULTILINE)
    tags = [t.strip() for t in tagm.group(1).split(",") if t.strip()] if tagm else []
    # point: folded (>) or plain scalar
    pm = re.search(r'^point:\s*>\s*\n(.*?)(?=\n\S|\Z)', fm + "\n", re.S | re.M)
    if pm:
        point = " ".join(l.strip() for l in pm.group(1).splitlines() if l.strip())
    else:
        point = field("point")
    # drop a leading H1 that duplicates the title
    body = re.sub(r'^#\s+.*\n+', '', body.lstrip("\n"), count=1).strip()
    return title, slug, tags, point, visibility, body


def split_paywall(body):
    """Split the body on a lone `---paywall---` marker line.

    Returns (before_md, after_md). If no marker is present, after_md is None.
    Only the first marker is honored. The marker line itself is dropped."""
    m = re.search(r'^[ \t]*---paywall---[ \t]*$', body, re.MULTILINE)
    if not m:
        return body, None
    before = body[:m.start()].rstrip()
    after = body[m.end():].lstrip("\n")
    return before, after


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


def find_by_slug(slug, resource="posts"):
    try:
        r = call("GET", f"/ghost/api/admin/{resource}/slug/{slug}/")
        return r[resource][0]
    except SystemExit:
        return None


def html_card(html_str):
    """Wrap an HTML string as a Ghost lexical html card node."""
    return {"type": "html", "version": 1, "html": html_str}


def build_children(body_md, point=None):
    """Render a markdown body segment to a list of lexical child nodes.

    Extracts `> [!type]` callouts, renders the remaining markdown to HTML, and
    splits on CALLOUTCARDPLACEHOLDER lines — replacing each with its callout
    card. Optionally prepends the point card. Uses html cards throughout so Ghost
    never sanitizes the content (preserving footnote id= anchors etc).
    """
    body, callouts = extract_callouts(body_md)
    html_body = render_html(body)
    # Split on placeholder paragraphs: <p>CALLOUTCARDPLACEHOLDER0</p>
    parts = re.split(r'<p>CALLOUTCARDPLACEHOLDER(\d+)</p>', html_body)
    children = []
    if point:
        children.append(point_card(point))
    i = 0
    while i < len(parts):
        chunk = parts[i].strip()
        if chunk:
            children.append(html_card(chunk))
        if i + 1 < len(parts):
            idx = int(parts[i + 1])
            children.append(callout_card(callouts[idx]))
            i += 2
        else:
            i += 1
    return children


def lexical_doc(children):
    """Wrap a list of lexical child nodes in a Ghost lexical root document."""
    return json.dumps({"root": {"children": children, "direction": None,
                                "format": "", "indent": 0, "type": "root", "version": 1}})


def main():
    args = sys.argv[1:]
    if not args:
        raise SystemExit(__doc__)
    target = "local"
    if "--target" in args:
        i = args.index("--target")
        if i + 1 >= len(args):
            raise SystemExit("--target requires a value (local|hosted)")
        target = args[i + 1]
        if target not in ("local", "hosted"):
            raise SystemExit(f"unknown target '{target}' (use local|hosted)")
        del args[i:i + 2]
    status = "draft" if "--draft" in args else "published"
    resource = "pages" if "--page" in args else "posts"
    paths = [a for a in args if not a.startswith("--")]
    if not paths:
        raise SystemExit("no article path given")
    path = paths[0]
    configure(target)
    title, slug, tags, point, visibility, body = parse_article(path)

    # split on the paywall marker (before callouts are extracted), then build
    # the lexical doc from the segment(s) — injecting a members-only card between
    # the public (above) and gated (below) content when a marker is present.
    before_md, after_md = split_paywall(body)
    children = build_children(before_md, point)
    if after_md is not None:
        children.append(html_card("<!--members-only-->"))
        children += build_children(after_md)
    lexical = lexical_doc(children)

    payload = {"title": title, "lexical": lexical, "status": status,
               "visibility": visibility}
    if tags:
        payload["tags"] = [{"name": t} for t in tags]
    if slug:
        payload["slug"] = slug

    existing = find_by_slug(slug, resource) if slug else None
    if existing:
        payload["updated_at"] = existing["updated_at"]
        post = call("PUT", f"/ghost/api/admin/{resource}/{existing['id']}/",
                    {resource: [payload]})[resource][0]
        action = "updated"
    else:
        post = call("POST", f"/ghost/api/admin/{resource}/",
                    {resource: [payload]})[resource][0]
        action = "created"

    print(f"{action} [{post['status']}] ({target}/{resource}) {post.get('url')}")
    print(f"  point: {'yes' if point else 'none'} | visibility: {visibility} | "
          f"paywall: {'yes' if after_md is not None else 'no'} | tags: {', '.join(tags) or 'none'}")


if __name__ == "__main__":
    main()
