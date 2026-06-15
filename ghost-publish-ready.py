#!/usr/bin/env python3
"""Batch-push all ready Ghost articles as drafts.

Scans drafts/*/article.md for status:ready + target:ghost and uploads each
as a draft via ghost-upload.py. Prints a summary with the returned URLs.

Usage:
    python3 ghost-publish-ready.py [--target local|hosted] [--dry-run]
"""
import sys, os, re, glob, subprocess

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DRAFTS_DIR = os.path.join(SCRIPT_DIR, "drafts")
UPLOADER   = os.path.join(SCRIPT_DIR, "ghost-upload.py")


def parse_frontmatter(path):
    raw = open(path).read()
    m = re.match(r"^---\n(.*?)\n---\n", raw, re.DOTALL)
    if not m:
        return {}
    fm = m.group(1)
    result = {}
    for line in fm.splitlines():
        mm = re.match(r'^(\w[\w-]*):\s*(.*)$', line)
        if mm:
            result[mm.group(1)] = mm.group(2).strip().strip('"')
    return result


def find_ready_ghost_articles():
    articles = []
    for path in sorted(glob.glob(os.path.join(DRAFTS_DIR, "*/article.md"))):
        fm = parse_frontmatter(path)
        if fm.get("status") == "ready" and fm.get("target") == "ghost":
            slug = os.path.basename(os.path.dirname(path))
            articles.append({"path": path, "slug": slug, "title": fm.get("title", slug)})
    return articles


def main():
    args = sys.argv[1:]
    dry_run = "--dry-run" in args
    if dry_run:
        args = [a for a in args if a != "--dry-run"]

    target = "hosted"
    if "--target" in args:
        i = args.index("--target")
        if i + 1 >= len(args):
            raise SystemExit("--target requires a value (local|hosted)")
        target = args[i + 1]
        if target not in ("local", "hosted"):
            raise SystemExit(f"unknown target '{target}'")

    articles = find_ready_ghost_articles()
    if not articles:
        print("no articles with status:ready + target:ghost found")
        return

    print(f"found {len(articles)} article(s) ready for Ghost:")
    for a in articles:
        print(f"  {a['slug']}: {a['title']}")

    if dry_run:
        print("\n[dry-run] no uploads performed")
        return

    print()
    pushed, failed = [], []
    for a in articles:
        print(f"==> {a['slug']}")
        cmd = [sys.executable, UPLOADER, a["path"], "--draft", "--target", target]
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode != 0:
            err = (result.stderr.strip() or result.stdout.strip())[:200]
            print(f"  FAILED: {err}")
            failed.append(a["slug"])
        else:
            for line in result.stdout.strip().splitlines():
                print(f"  {line}")
            first = result.stdout.strip().splitlines()[0] if result.stdout.strip() else ""
            parts = first.split()
            url = parts[-1] if parts and parts[-1].startswith("http") else "(no url)"
            pushed.append({"slug": a["slug"], "title": a["title"], "url": url})

    print(f"\n--- summary: {len(pushed)} pushed, {len(failed)} failed ---")
    for p in pushed:
        print(f"  ok   {p['slug']}")
        print(f"       {p['url']}")
    for s in failed:
        print(f"  err  {s}")


if __name__ == "__main__":
    main()
