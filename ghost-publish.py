#!/usr/bin/env python3
"""Flip a Ghost post to published (or draft) by id."""
import sys, os, json, time, hmac, hashlib, base64, urllib.request

API_URL = "http://100.119.32.88:2368"
KEY = os.environ["GHOST_LOCAL_API_KEY"]
key_id, key_secret = KEY.split(":")

def b64url(d): return base64.urlsafe_b64encode(d).rstrip(b"=").decode()

def make_jwt():
    now = int(time.time())
    seg = b64url(json.dumps({"alg":"HS256","typ":"JWT","kid":key_id}).encode()) + "." + \
          b64url(json.dumps({"iat":now,"exp":now+300,"aud":"/admin/"}).encode())
    sig = hmac.new(bytes.fromhex(key_secret), seg.encode(), hashlib.sha256).digest()
    return seg + "." + b64url(sig)

def req(method, path, body=None):
    r = urllib.request.Request(API_URL + path,
        data=json.dumps(body).encode() if body else None, method=method,
        headers={"Authorization":"Ghost "+make_jwt(),
                 "Content-Type":"application/json","Accept-Version":"v5.0"})
    return json.load(urllib.request.urlopen(r))

post_id = sys.argv[1]
status = sys.argv[2] if len(sys.argv) > 2 else "published"
cur = req("GET", f"/ghost/api/admin/posts/{post_id}/")["posts"][0]
out = req("PUT", f"/ghost/api/admin/posts/{post_id}/",
          {"posts":[{"status":status,"updated_at":cur["updated_at"]}]})
p = out["posts"][0]
print("OK", p["status"], "->", p.get("url"))
