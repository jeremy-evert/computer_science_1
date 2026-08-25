#!/usr/bin/env python3
"""Decision 029 cleanup pass for Computer Science I (74029).

Two categories, both gated by a fresh live per-object preflight + immediate
readback, one destructive delete at a time:

1. "shared-defer" -- AI Fluency (Monday Moment Activity) and Professional
   Minds (week NN wed/fri reading + slides) instances that already have a
   verified Commons (24298) destination from the prior Architecture-campaign
   harvest. Near-term due-date guard: 7 days (same as the Architecture pass;
   these have a replacement destination, so deferring a near-term one costs
   nothing).
2. "retire-noguard" -- A3 Paired Programming Report / A4 Show and Tell
   Reflection / A7 Friday Feedback Report. Decision 029
   (`swosu_cs_curriculum/decisions/029_fall_2026_optional_computing_commons_pivot.md`)
   says these in-class-only practices get NO Commons migration and NO online
   equivalent at all -- full retirement, not a move. The decision's own
   migration posture explicitly wants this done *before* students submit,
   so a short 24h near-term guard is used instead of 7 days (protects only
   against a literal same-day race, not against the early-removal the
   decision itself calls for).

A01-A09 (career/degree-planning strand) is explicitly OUT OF SCOPE for this
script -- every one of those already has real student submissions this term
(18-33 each) and Decision 029's gradebook rule says already-submitted
shared/enrichment work stays in the home course as bonus credit. A future
Commons harvest for *next* term's students is a separate, non-blocking
follow-up (see the course-side report), not a live-course safety concern.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, "/home/jevert/git/harbor")

from harbor.api import CanvasApiError, delete_assignment, get_all_submissions, get_assignment, list_assignments  # noqa: E402
from harbor.client import CanvasClient  # noqa: E402
from harbor.config import load_env, read_canvas_config  # noqa: E402

COURSE_ID = 74029
ALLOWED = {74029, 24298}

SHARED_DEFER_GUARD = dt.timedelta(days=7)
RETIRE_GUARD = dt.timedelta(hours=24)

MONDAY_MOMENT = re.compile(r"^Monday Moment Activity", re.I)
WED_PROF_MINDS = re.compile(r"^week\s*0*(\d+)\s*wed\s*(reading|slides)\s*assignment$", re.I)
FRI_PROF_MINDS = re.compile(r"^week\s*0*(\d+)\s*fri\s*(reading|slides)\s*assignment$", re.I)
A3_PAIRED = re.compile(r"^A3\s*[—-]\s*Paired Programming Report", re.I)
A4_SHOWTELL = re.compile(r"^A4\s*[—-]\s*Show and Tell Reflection", re.I)
A7_FEEDBACK = re.compile(r"^A7\s*[—-]\s*Friday Feedback Report", re.I)


def classify(name: str) -> tuple[str, str] | None:
    n = name.strip()
    if MONDAY_MOMENT.match(n):
        return ("shared-defer", "Monday Moment (AI Fluency)")
    if WED_PROF_MINDS.match(n):
        return ("shared-defer", "Professional Minds Wednesday")
    if FRI_PROF_MINDS.match(n):
        return ("shared-defer", "Professional Minds Friday")
    if A3_PAIRED.match(n):
        return ("retire-noguard", "A3 Paired Programming Report")
    if A4_SHOWTELL.match(n):
        return ("retire-noguard", "A4 Show and Tell Reflection")
    if A7_FEEDBACK.match(n):
        return ("retire-noguard", "A7 Friday Feedback Report")
    return None


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    load_env()
    import os

    os.environ["CANVAS_ENFORCE_COURSE_ALLOWLIST"] = "true"
    os.environ["CANVAS_ALLOWED_COURSE_IDS"] = "74029,24298"
    cfg = read_canvas_config()
    if cfg.allowed_course_ids != frozenset(ALLOWED):
        print(f"ABORT: allowlist not exactly {{74029, 24298}}, got {cfg.allowed_course_ids}")
        return 1
    client = CanvasClient(cfg)

    assignments = list_assignments(client, COURSE_ID)
    print(f"Live assignment count at recon: {len(assignments)}")

    candidates = []
    for a in assignments:
        cls = classify(a["name"])
        if cls:
            candidates.append((a, cls[0], cls[1]))

    print(f"Candidate matches: {len(candidates)}")

    receipt = {
        "run_at": dt.datetime.now(dt.timezone.utc).isoformat(),
        "dry_run": args.dry_run,
        "course_id": COURSE_ID,
        "recon_count": len(assignments),
        "candidates_matched": len(candidates),
        "actions": [],
    }

    deleted = 0
    skipped = 0
    for a, guard_cls, label in candidates:
        aid = a["id"]
        _, fresh = get_assignment(client, COURSE_ID, aid)
        if fresh.get("workflow_state") == "deleted":
            skipped += 1
            receipt["actions"].append({"id": aid, "name": a["name"], "cls": label, "result": "ALREADY_DELETED_SKIP"})
            continue

        due_at = fresh.get("due_at")
        guard = SHARED_DEFER_GUARD if guard_cls == "shared-defer" else RETIRE_GUARD
        if due_at:
            due_dt = dt.datetime.fromisoformat(due_at.replace("Z", "+00:00"))
            now = dt.datetime.now(dt.timezone.utc)
            if due_dt - now < guard:
                skipped += 1
                print(f"SKIP (near-term due date guard={guard}) id={aid} name={a['name']!r} due_at={due_at}")
                receipt["actions"].append({
                    "id": aid, "name": a["name"], "cls": label, "due_at": due_at,
                    "result": "SKIP_NEAR_TERM_DUE",
                })
                continue

        subs = get_all_submissions(client, COURSE_ID, aid)
        submitted = [s for s in subs if s.get("workflow_state") not in (None, "unsubmitted")]
        graded = [s for s in subs if s.get("grade") is not None or s.get("score") is not None]

        if submitted or graded:
            skipped += 1
            print(f"SKIP (activity found) id={aid} name={a['name']!r} submitted={len(submitted)} graded={len(graded)}")
            receipt["actions"].append({
                "id": aid, "name": a["name"], "cls": label, "result": "SKIP_ACTIVITY",
                "submitted": len(submitted), "graded": len(graded),
            })
            continue

        if args.dry_run:
            print(f"WOULD DELETE id={aid} name={a['name']!r} cls={label} due_at={due_at} (0 submissions, 0 grades)")
            receipt["actions"].append({"id": aid, "name": a["name"], "cls": label, "due_at": due_at, "result": "WOULD_DELETE"})
            continue

        status = delete_assignment(client, COURSE_ID, aid)
        try:
            _, after = get_assignment(client, COURSE_ID, aid)
            after_state = after.get("workflow_state")
            ok = status == 200 and after_state == "deleted"
        except CanvasApiError as e:
            after_state = "404_CONFIRMED_GONE" if e.status_code == 404 else f"READBACK_ERROR:{e}"
            ok = status == 200 and e.status_code == 404

        deleted += 1 if ok else 0
        print(f"{'DELETED' if ok else 'DELETE_UNVERIFIED'} id={aid} name={a['name']!r} status={status} after_state={after_state}")
        receipt["actions"].append({
            "id": aid, "name": a["name"], "cls": label,
            "result": "DELETED" if ok else "DELETE_UNVERIFIED",
            "delete_status": status, "readback_workflow_state": after_state,
        })

    receipt["deleted"] = deleted
    receipt["skipped"] = skipped

    out_dir = Path(__file__).resolve().parents[1] / "sidecar" / "raw"
    out_dir.mkdir(parents=True, exist_ok=True)
    stamp = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H%M%SZ")
    out_path = out_dir / f"{stamp}__029_shared_strand_cleanup_pass.json"
    out_path.write_text(json.dumps(receipt, indent=2))
    print(f"Receipt written: {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
