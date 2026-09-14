#!/usr/bin/env python3
"""Fix CS1's front page: the week-rail and H1 already correctly say Week 5,
but the "This week" summary and "Go here first" box were never advanced
past Week 4 -- confirmed live before writing this script. Narrow,
single-purpose, idempotent-guarded, matches the pattern already used in
computing_commons/scripts/advance_current_week_to_5.py.
"""
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path.home() / "git" / "harbor"))
from harbor import api
from harbor.client import CanvasClient
from harbor.config import load_env, read_canvas_config

COURSE_ID = 74029
EVIDENCE = Path.home() / "git" / "computer_science_1" / "sidecar" / "reports" / "advance_current_week_to_5.md"

OLD_SUMMARY = "<p>This week: deepen last week's single <code>if</code> into a real decision with at least three distinct outcomes — branching and decision-making.</p>"
NEW_SUMMARY = "<p>This week: add a loop that processes an unknown or variable number of events in your world — sentinel-controlled or range-driven.</p>"

OLD_GO_HERE = '''<div style="margin: 18px 0; padding: 10px 14px; border: 1px solid #999; border-radius: 6px; background: #f4f4f4;">
  <h2 style="margin-top: 0;">Go here first</h2>
  <a href="https://swosu.instructure.com/courses/74029/pages/week-4-branching-and-decision-making" style="display: inline-block; margin-top: 6px; padding: 3px 10px; border: 1px solid #17335c; border-radius: 4px; text-decoration: none; color: #17335c; background: #eaf1fb;" data-api-endpoint="https://swosu.instructure.com/api/v1/courses/74029/pages/week-4-branching-and-decision-making" data-api-returntype="Page">Week 4 overview →</a>
  <a href="https://swosu.instructure.com/courses/74029/discussion_topics/542893" style="display: inline-block; margin-top: 6px; margin-left: 8px; padding: 3px 10px; border: 1px solid #17335c; border-radius: 4px; text-decoration: none; color: #17335c; background: #eaf1fb;" data-api-endpoint="https://swosu.instructure.com/api/v1/courses/74029/discussion_topics/542893" data-api-returntype="Discussion">Week 4 gate discussion — 25 pts, due 9/11 →</a>
</div>'''
NEW_GO_HERE = '''<div style="margin: 18px 0; padding: 10px 14px; border: 1px solid #999; border-radius: 6px; background: #f4f4f4;">
  <h2 style="margin-top: 0;">Go here first</h2>
  <a href="https://swosu.instructure.com/courses/74029/discussion_topics/543062" style="display: inline-block; margin-top: 6px; padding: 3px 10px; border: 1px solid #17335c; border-radius: 4px; text-decoration: none; color: #17335c; background: #eaf1fb;" data-api-endpoint="https://swosu.instructure.com/api/v1/courses/74029/discussion_topics/543062" data-api-returntype="Discussion">Week 5 gate discussion — 25 pts, due 9/19 →</a>
</div>'''

SUBSTITUTIONS = [
    ("this-week summary", OLD_SUMMARY, NEW_SUMMARY),
    ("go-here-first box", OLD_GO_HERE, NEW_GO_HERE),
]


def die(msg):
    print("STOP:", msg)
    sys.exit(2)


def main():
    load_env()
    client = CanvasClient(read_canvas_config(enforce_course_allowlist=True))
    ev = ["", "## CS1 front page: advance This-week/Go-here-first to Week 5 — %s UTC" % time.strftime("%Y-%m-%dT%H:%M:%S")]

    if not client.config.api_base_url.startswith("https://swosu.instructure.com"):
        die("base_url not SWOSU")
    course = client.get(f"/api/v1/courses/{COURSE_ID}").json()
    if course.get("id") != COURSE_ID:
        die("course identity mismatch: %r" % course.get("name"))
    ev.append("- course: %s / %s" % (course["id"], course["name"]))

    fp_before = client.get(f"/api/v1/courses/{COURSE_ID}/front_page").json()
    body = fp_before.get("body") or ""
    page_url = fp_before["url"]

    if "discussion_topics/543062" in body and "week-4-branching-and-decision-making" not in body:
        die("front page already advanced -- nothing to do (idempotent guard)")

    for label, old, new in SUBSTITUTIONS:
        if old not in body:
            die("expected content for %r not found -- front page changed since this script was written" % label)
        body = body.replace(old, new)
        ev.append("- applied: %s" % label)

    status, _ = api.update_page(client, COURSE_ID, page_url, {"wiki_page[body]": body})
    ev.append("- update_page status %s" % status)

    fp_after = client.get(f"/api/v1/courses/{COURSE_ID}/front_page").json()
    live_body = fp_after.get("body") or ""
    if live_body != body:
        die("readback mismatch: live front page body does not match what was sent")
    ev.append("- readback OK: live front page body matches exactly what was sent")

    EVIDENCE.parent.mkdir(parents=True, exist_ok=True)
    with EVIDENCE.open("a", encoding="utf-8") as f:
        f.write("\n".join(ev) + "\n")
    print("\n".join(ev))
    print("\nDONE. Evidence appended to %s" % EVIDENCE)


if __name__ == "__main__":
    main()
