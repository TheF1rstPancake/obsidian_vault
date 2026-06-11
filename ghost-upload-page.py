#!/usr/bin/env python3
"""Upload/update a Ghost page (not post) from a markdown file.

Usage:
    python3 ghost-upload-page.py drafts/<slug>/article.md [--draft]

Reads GHOST_LOCAL_API_KEY from .env.
"""
import sys, os, re, json, time, hmac, hashlib, base64, html as htmlmod
import urllib.request, urllib.error
import markdown as md_lib

API_URL = "http://100.119.32.88:2368"


def load_key():
    for line in open(os.path.join(os.path.dirname(__file__), ".env")):
        if line.startswith("GHOST_LOCAL_API_KEY="):
            return line.split("=", 1)[1].strip()
    raise SystemExit("GHOST_LOCAL_API_KEY not found in .env")


raw_key = load_key()
KID, KSECRET = raw_key.split(":")


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
    if len(sys.argv) < 2:
        raise SystemExit(__doc__)
    path = sys.argv[1]
    status = "draft" if "--draft" in sys.argv[1:] else "published"
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

    print(f"{action} [{page['status']}] {page.get('url')}")


if __name__ == "__main__":
    main()
