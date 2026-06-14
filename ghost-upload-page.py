#!/usr/bin/env python3
"""Upload/update a Ghost page (not post) from a markdown file.

Usage:
    python3 ghost-upload-page.py drafts/<slug>/article.md [--draft] [--target local|hosted]

Targets:
    local  (default) -> http://100.119.32.88:2368, key from GHOST_LOCAL_API_KEY
    hosted           -> GHOST_HOSTED_URL, key from GHOST_HOSTED_API_KEY
"""
import sys, os, re, json, time, hmac, hashlib, base64, html as htmlmod
import urllib.request, urllib.error
import markdown as md_lib

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
    body = re.sub(r'^#\s+.*\n+', '', body.lstrip("\n"), count=1).strip()
    return title, slug, body


def render_html(body_md):
    extensions = ["footnotes", "tables", "fenced_code", "attr_list", "def_list", "nl2br"]
    return md_lib.markdown(body_md, extensions=extensions)


def html_card(html_str):
    return {"type": "html", "version": 1, "html": html_str}


def build_lexical(html_body):
    return json.dumps({"root": {"children": [html_card(html_body)],
                                "direction": None, "format": "", "indent": 0,
                                "type": "root", "version": 1}})


def find_page_by_slug(slug):
    try:
        r = call("GET", f"/ghost/api/admin/pages/slug/{slug}/")
        return r["pages"][0]
    except SystemExit:
        return None


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
    paths = [a for a in args if not a.startswith("--")]
    if not paths:
        raise SystemExit("no article path given")
    path = paths[0]
    configure(target)
    title, slug, body = parse_article(path)

    html = render_html(body)

    existing = find_page_by_slug(slug) if slug else None

    # If existing page is mobiledoc (pre-lexical Ghost), use source=html to update.
    # New pages get written as lexical directly (no sanitization issues for pages,
    # which don't use footnotes typically).
    if existing:
        is_mobiledoc = existing.get("lexical") is None
        payload = {"title": title, "html": html, "status": status,
                   "updated_at": existing["updated_at"]}
        if slug:
            payload["slug"] = slug
        endpoint = f"/ghost/api/admin/pages/{existing['id']}/"
        if not is_mobiledoc:
            # lexical page — write lexical directly to preserve id= attrs
            payload.pop("html")
            payload["lexical"] = build_lexical(html)
            endpoint_url = endpoint
        else:
            endpoint_url = endpoint + "?source=html"
        page = call("PUT", endpoint_url, {"pages": [payload]})["pages"][0]
        action = "updated"
    else:
        lexical = build_lexical(html)
        payload = {"title": title, "lexical": lexical, "status": status}
        if slug:
            payload["slug"] = slug
        page = call("POST", "/ghost/api/admin/pages/", {"pages": [payload]})["pages"][0]
        action = "created"

    print(f"{action} [{page['status']}] ({target}) {page.get('url')}")


if __name__ == "__main__":
    main()
