#!/usr/bin/env python3
"""Upload an obsidian draft article.md to local Ghost as a draft post."""
import sys, os, re, json, time, hmac, hashlib, base64, urllib.request

API_URL = "http://100.119.32.88:2368"
KEY = os.environ["GHOST_LOCAL_API_KEY"]
key_id, key_secret = KEY.split(":")

def b64url(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).rstrip(b"=").decode()

def make_jwt():
    header = {"alg": "HS256", "typ": "JWT", "kid": key_id}
    now = int(time.time())
    payload = {"iat": now, "exp": now + 300, "aud": "/admin/"}
    seg = b64url(json.dumps(header).encode()) + "." + b64url(json.dumps(payload).encode())
    sig = hmac.new(bytes.fromhex(key_secret), seg.encode(), hashlib.sha256).digest()
    return seg + "." + b64url(sig)

def parse_article(path):
    raw = open(path).read()
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", raw, re.DOTALL)
    fm, body = (m.group(1), m.group(2)) if m else ("", raw)
    title = re.search(r'^title:\s*"?(.*?)"?\s*$', fm, re.MULTILINE)
    title = title.group(1) if title else "Untitled"
    tagm = re.search(r'^tags:\s*\[(.*?)\]', fm, re.MULTILINE)
    tags = [t.strip() for t in tagm.group(1).split(",")] if tagm else []
    # drop a leading H1 that duplicates the title
    body = body.lstrip("\n")
    body = re.sub(r'^#\s+.*\n+', '', body, count=1)
    return title, tags, body.strip()

def main():
    path = sys.argv[1]
    title, tags, body = parse_article(path)
    mobiledoc = json.dumps({
        "version": "0.3.1",
        "atoms": [], "markups": [],
        "cards": [["markdown", {"markdown": body}]],
        "sections": [[10, 0]],
    })
    post = {"posts": [{
        "title": title,
        "mobiledoc": mobiledoc,
        "status": "draft",
        "tags": [{"name": t} for t in tags],
    }]}
    req = urllib.request.Request(
        API_URL + "/ghost/api/admin/posts/",
        data=json.dumps(post).encode(),
        method="POST",
        headers={
            "Authorization": "Ghost " + make_jwt(),
            "Content-Type": "application/json",
            "Accept-Version": "v5.0",
        },
    )
    try:
        resp = urllib.request.urlopen(req)
        out = json.load(resp)
        p = out["posts"][0]
        print("OK", p["status"], "->", API_URL + "/ghost/" + "#/editor/post/" + p["id"])
        print("PREVIEW", p.get("url"))
        print("TITLE", p["title"])
    except urllib.error.HTTPError as e:
        print("HTTP", e.code, e.read().decode())
        sys.exit(1)

main()
