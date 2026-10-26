#!/usr/bin/env python3
"""Publish the Week 11 Rock-Paper-Scissors dictionary-of-dictionaries example to CS1 Canvas.

Additive and idempotent: uploads three files to Files/week11/dictionary_example
and week11/slides, then edits ONLY the Week 11 Overview page (Monday line plus one new
section). Target-locked to course 74029 (id AND name). Backs the page up first and
reads it back after writing.

    python3 scripts/publish_week11_rps_example.py            # dry run, no writes
    python3 scripts/publish_week11_rps_example.py --apply    # upload + edit page

Needs harbor and the usual Canvas env. Sets the course allowlist to 74029 for this process.
"""
import os
import sys
import json
import time
from pathlib import Path

os.environ["CANVAS_ALLOWED_COURSE_IDS"] = "74029"
sys.path.insert(0, str(Path.home() / "git" / "harbor"))
from harbor import api
from harbor.client import CanvasClient
from harbor.config import load_env, read_canvas_config

COURSE_ID = 74029
COURSE_NAME_PREFIX = "Fall 2026 Computer Science I"
PAGE = "week-11-overview-lists-and-dictionaries-continued"
BASE = "https://swosu.instructure.com/courses/74029"
ROOT = Path(__file__).resolve().parents[1]
BACKUP = ROOT / "sidecar" / "reports" / "week11_rps_backup"
FILES = [  # (key, local path, canvas folder, content type, label)
    ("py", "dictionary_example/rps_dict_of_dicts.py", "week11/dictionary_example", "text/x-python", "rps_dict_of_dicts.py (run it)"),
    ("md", "dictionary_example/README.md", "week11/dictionary_example", "text/markdown", "walkthrough (README)"),
    ("pdf", "presentations/beamer/week11_mon_dicts_rps/week11_mon_dicts_rps.pdf", "week11/slides", "application/pdf", "Monday slides (PDF)"),
]
MON_OLD = "<p>Monday (Oct 26): Monday Moments, AI I Lens 11: Verify."
MON_NEW = "<p>Monday (Oct 26): <strong>Today we learn dictionaries</strong>: looking a value up by its key. Monday Moments, AI I Lens 11: Verify."
ANCHOR = "<h2>Optional reading and listening</h2>"
MARK = "rps-dict-of-dicts-example"
STYLE = ("display:inline-block;margin-top:8px;margin-right:8px;padding:4px 10px;border:1px solid #17335c;"
         "border-radius:4px;text-decoration:none;color:#17335c;background:#eaf1fb;")


def die(msg):
    print("STOP:", msg)
    sys.exit(2)


def section(ids):
    links = "".join(
        f'<a href="{BASE}/files/{ids[k]}" style="{STYLE}" data-api-endpoint="https://swosu.instructure.com/api/v1/courses/74029/files/{ids[k]}" data-api-returntype="File">{label} →</a>'
        for k, _p, _f, _c, label in FILES
    )
    return (
        f'<h2 id="{MARK}">Worked example: Rock-Paper-Scissors with a dictionary of dictionaries</h2>'
        "<p>The rules of the game are stored as data: <code>rules[player][opponent]</code> gives "
        "<em>win</em>, <em>lose</em>, or <em>tie</em>. The first key picks the row, the second picks the column. "
        "A second dictionary keeps the score. Run the Python file, then read the walkthrough, then think about "
        "this week's Decide/Compare question: why a dictionary of dictionaries here, and not nine if statements?</p>"
        f"<p>{links}</p>"
    )


def main():
    apply = "--apply" in sys.argv
    load_env()
    client = CanvasClient(read_canvas_config(enforce_course_allowlist=True))
    course = client.get(f"/api/v1/courses/{COURSE_ID}").json()
    if course.get("id") != COURSE_ID or not course.get("name", "").startswith(COURSE_NAME_PREFIX):
        die("course identity mismatch: %r" % course.get("name"))
    print("target:", course["id"], course["name"])
    page = client.get(f"/api/v1/courses/{COURSE_ID}/pages/{PAGE}").json()
    body = page["body"] or ""
    if MARK in body:
        die("example section already on the page (idempotent guard)")
    if MON_OLD not in body or ANCHOR not in body:
        die("expected page content not found; page changed since this script was written")
    for _k, p, *_ in FILES:
        if not (ROOT / p).is_file():
            die("missing local file: " + p)
    if not apply:
        print("DRY RUN ok: would upload", [f[1] for f in FILES], "and edit page", PAGE)
        return
    BACKUP.mkdir(parents=True, exist_ok=True)
    stamp = time.strftime("%Y%m%dT%H%M%S")
    (BACKUP / f"{PAGE}.{stamp}.pre-apply.html").write_text(body, encoding="utf-8")
    ids = {}
    for key, p, folder, ctype, _label in FILES:
        a = api.upload_course_file(client, COURSE_ID, ROOT / p, folder_path=folder, content_type=ctype)
        rb = client.get(f"/api/v1/courses/{COURSE_ID}/files/{a['id']}").json()
        ids[key] = a["id"]
        print("uploaded", rb["display_name"], rb["size"], f"{BASE}/files/{a['id']}")
    new_body = body.replace(MON_OLD, MON_NEW, 1).replace(ANCHOR, section(ids) + ANCHOR, 1)
    api.update_page(client, COURSE_ID, PAGE, {"wiki_page[body]": new_body})
    live = client.get(f"/api/v1/courses/{COURSE_ID}/pages/{PAGE}").json()["body"]
    if live != new_body and (MARK not in live or "Today we learn dictionaries" not in live):
        die("readback mismatch")
    (BACKUP / "uploaded_file_ids.json").write_text(json.dumps(ids, indent=1))
    print("readback OK; page:", f"{BASE}/pages/{PAGE}")
    print(json.dumps({k: f"{BASE}/files/{v}" for k, v in ids.items()}, indent=1))


if __name__ == "__main__":
    main()
