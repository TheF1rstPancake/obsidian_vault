#!/usr/bin/env python3
"""Upload and activate the Ghost theme zip via the Admin API.

Usage:
    python3 ghost-theme-upload.py [--target local|hosted]

Targets:
    hosted (default) -> GHOST_HOSTED_URL, key from GHOST_HOSTED_API_KEY
    local            -> http://100.119.32.88:2368, key from GHOST_LOCAL_API_KEY
"""
import sys, os, json, time, hmac, hashlib, base64, uuid
import urllib.request, urllib.error

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
THEME_ZIP  = os.path.join(SCRIPT_DIR, "ghost-theme", "pancake.zip")
THEME_NAME = "pancake"
LOCAL_URL  = "http://100.119.32.88:2368"

API_URL = LOCAL_URL
KID = KSECRET = None


def env_val(name):
    try:
        for line in open(os.path.join(SCRIPT_DIR, ".env")):
            if line.startswith(name + "="):
                return line.split("=", 1)[1].strip()
    except FileNotFoundError:
        pass
    return None


def configure(target):
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


def upload_theme():
    boundary = uuid.uuid4().hex
    filename = os.path.basename(THEME_ZIP)
    with open(THEME_ZIP, "rb") as f:
        file_data = f.read()
    body = (
        f"--{boundary}\r\n"
        f'Content-Disposition: form-data; name="file"; filename="{filename}"\r\n'
        "Content-Type: application/zip\r\n"
        "\r\n"
    ).encode() + file_data + f"\r\n--{boundary}--\r\n".encode()
    req = urllib.request.Request(
        API_URL + "/ghost/api/admin/themes/upload",
        data=body,
        method="POST",
        headers={
            "Authorization": "Ghost " + jwt(),
            "Content-Type": f"multipart/form-data; boundary={boundary}",
            "Accept-Version": "v5.0",
        },
    )
    try:
        return json.load(urllib.request.urlopen(req))
    except urllib.error.HTTPError as e:
        raise SystemExit(f"upload failed {e.code}: {e.read().decode()[:400]}")


def activate_theme():
    req = urllib.request.Request(
        API_URL + f"/ghost/api/admin/themes/{THEME_NAME}/activate",
        data=b"",
        method="PUT",
        headers={
            "Authorization": "Ghost " + jwt(),
            "Accept-Version": "v5.0",
        },
    )
    try:
        return json.load(urllib.request.urlopen(req))
    except urllib.error.HTTPError as e:
        raise SystemExit(f"activate failed {e.code}: {e.read().decode()[:400]}")


def main():
    args = sys.argv[1:]
    target = "hosted"
    if "--target" in args:
        i = args.index("--target")
        if i + 1 >= len(args):
            raise SystemExit("--target requires a value (local|hosted)")
        target = args[i + 1]
        if target not in ("local", "hosted"):
            raise SystemExit(f"unknown target '{target}'")

    if not os.path.exists(THEME_ZIP):
        raise SystemExit(f"theme zip not found: {THEME_ZIP}\nRun ./ghost-theme-pack.sh first.")

    configure(target)

    zip_size = os.path.getsize(THEME_ZIP)
    print(f"uploading {THEME_ZIP} ({zip_size // 1024}KB) -> {API_URL} ...")
    result = upload_theme()
    themes = result.get("themes", [])
    if themes:
        t = themes[0]
        ver = (t.get("package") or {}).get("version", "?")
        print(f"  uploaded: {t.get('name')} v{ver}")

    print(f"activating theme '{THEME_NAME}' ...")
    result = activate_theme()
    themes = result.get("themes", [])
    active = next((t for t in themes if t.get("active")), None)
    if active:
        ver = (active.get("package") or {}).get("version", "?")
        print(f"  active: {active.get('name')} v{ver}")

    print("done.")


if __name__ == "__main__":
    main()
