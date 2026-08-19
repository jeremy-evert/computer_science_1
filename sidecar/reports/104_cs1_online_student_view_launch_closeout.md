# Sidecar Report 104 — CS1 online student-view launch closeout

**Date:** 2026-08-19
**Prompt:** `sidecar/prompts/104_cs1_online_student_view_launch_closeout.md`
**Foreman:** Flo
**Course verified:** SWOSU Canvas course `74029`, `COMSC-1033-1415.2026FA`
(shared host for native section `76384` and merged section `76388`)
**Precondition:** Prompt 103 verdict `DEPLOYED`
(`sidecar/reports/103_cs1_online_full_production_imprint.md`)
**Receipts:** `sidecar/runs/103_104_flo_closeout/20260819T031550Z/`

## Verdict: READY WITH NON-BLOCKING YELLOWS

---

## 1. Opening-minute test

Course home is `default_view: modules` (no separate front page needed —
confirmed `GET /courses/74029/front_page` returns "No front page has been
set," which is a valid, common configuration, not a defect). The student
lands directly on the module list; module 1 is "Monday: Survive This
Semester," clearly first, clearly named.

**Two real defects found and repaired here** — both on the very first page
a student opens:

1. **Leaked template placeholder text.** The live Monday page rendered a
   visible paragraph reading *"(CS1 reference instance — replace per
   course, see `docs/NAMING.md`)"* — an internal editorial note from
   `semester_kickoff_week`'s "COURSE-SPECIFIC SLOT" convention that was
   supposed to stay inside an HTML comment (which Canvas strips) but sat
   just outside it as its own visible markdown paragraph.
2. **Dead call-to-action link.** The page's "Go to the Monday Exit Ticket
   assignment" link had no `href` at all — Canvas had silently stripped an
   invalid `{{link:monday_exit_ticket}}` token left unresolved by the
   original push (the assignment itself was still reachable via the
   module list, so this wasn't a total block, but it's a broken primary
   navigation cue on Day 1).

**Root cause and fix:** both bugs live in `course_foundry`'s kickoff
content pipeline. Added `strip_leaked_slot_editorial_note` (applied in
`semester_kickoff_content_map._read_required`, for plan/dry-run fidelity,
and in `load_adapters._kickoff_object_body`, for the actual push
rendering) to drop the leaked note line; the dead link was fixed by
resolving `{{link:monday_exit_ticket}}` against the real live assignment
(`https://swosu.instructure.com/courses/74029/assignments/910493`).
Regression tests added in both `tests/test_semester_kickoff_content_map.py`
and confirmed against real source. Committed
(`course_foundry` `679b805` → rebased onto `origin/main` at `50801ff`,
merged to `course_foundry` `main`).

**Why this was applied manually to the live page** rather than through a
standing production reconcile: `production_deploy.py`'s `cs1` plan only
covers Weeks 2–17 (16 modules) — the shared Week 1 kickoff content is
**not** part of it. The only tool that pushes kickoff content
(`semester_kickoff_savnac_load_adapter`) explicitly refuses to run against
anything but Savnac by design ("every live run requires a reviewed dry
run plus a human go/no-go"). Rather than weaken that deliberate gate, this
one proven, narrow, reversible fix — the exact HTML the now-fixed, tested,
merged compiler produces, resolved against the real live assignment URL —
was applied via a single scoped `PUT /courses/74029/pages/monday-survive-this-semester`
using a client allowlisted to course `74029` only. Independently read back
afterward (`24_monday_page_readback.json`): placeholder gone, exit-ticket
link now has a real `href`. This is a disclosed **yellow**: CS1's Week 1
kickoff content has no standing production-safe reconcile tool at all, so
any future kickoff-content fix will need the same manual-but-verified
treatment, or a new production-gated kickoff adapter, until that gap is
closed as its own piece of work.

Slides link (`{{link:monday_slides}}`) was already correctly resolved live
(SWOSU SharePoint URL) — not a defect.

## 2. Visibility and publish-state audit

All 21 modules `published: true`, zero unpublished child items
(`06_modules_with_items.json`). No module item points at an unpublished
target (nothing to point at — everything's published). No stale
prerequisites found; kickoff modules carry the intended
Monday→Wednesday→Friday sequential gate (per `semester_kickoff_content_map`
tests), weekly modules 2–17 carry no artificial sequential lock.

## 3. Submission-path matrix

`74029`'s 160 live assignments (`07_assignments_p1.json` +
`25_assignments_p2.json`), zero duplicate ids/titles. Submission-type
distribution:

| Pattern | Count | Representative |
|---|---|---|
| `online_text_entry` | 122 | Wacky Wednesday/Fun Friday reflections, exit tickets |
| `online_text_entry` + `online_upload` | 24 | Paired-programming/Friday feedback reports |
| `online_upload` | 5 | file-artifact assignments |
| `not_graded` | 7 | Week 16/17 not-graded activities (confirmed intentional, §4) |
| `none` | 2 | Attendance & Participation (5 pts), Course Evaluation (2 pts) — gradebook-only, matches grading model exactly |

Spot-checked representative assignments across every distinct pattern
(Monday Exit Ticket, Weekly reinforcement, A3/A7/A4, A6 Week 14/15,
Coding Odyssey checkpoints, Attendance, Course Evaluation): submission
type matches the assignment's own instructions, points/group/due-date
line up with the finalized grading model, no object is marked graded when
its content is reflection/page-only-not-submitted.

## 4. Gradebook structure audit

Independently re-read post-repair (`11_post_write_assignment_groups.json`,
unaffected by the manual page fix since it touched no grading object):

- 15 assignment groups, **100%** total weight.
- Drop-lowest present on exactly the 7 groups the finalized model
  specifies.
- Coding Odyssey checkpoints: exactly 3 live (`week-06`, `week-09`,
  `week-14`, 25 pts each, 15% group) — Week 16's Checkpoint 4 correctly
  **not** resurrected, matching Prompt 103's explicit instruction.
- Week 16/17 `not_graded` objects (Farkle/ML receipt, Week 16 Wed/Fri
  reading+slides, Week 16 Monday Moment reflect-and-improve, `week-17`)
  confirmed `grading_type=not_graded` — no dead-days zombie.
- Bonus Practice (Weeks 2–13, `points_possible=0.0`) cannot reduce a
  grade — zero-point graded items add no denominator weight.
- **One ambiguity flagged, not resolved (yellow):** A10 ("Optional /
  Bonus — Success Foundations Reflection," 10 pts) lives inside the
  weighted "Semester kickoff week" group (5%) alongside the 13
  required kickoff objects, `omit_from_final_grade: false`. Whether its
  10 points are meant to be additive extra credit or already excluded
  from that group's *intended* denominator depends on kickoff-week's own
  rubric-level `extra_credit` criteria math, which this run did not fully
  trace end-to-end against Canvas's actual percentage-group calculation.
  This is pre-existing structure this run's dry-run/push never touched
  (create=0/update=0 throughout) — flagged for Chaz's review, not treated
  as a proven defect or repaired blind.

## 5. Link and content integrity audit

- Module-item titles (`06_modules_with_items.json`): zero duplicates,
  zero hits for `checkpoint 4`, `chapter exam`, `zybooks`, `deitel`,
  `savnac`, `192.168.`, `TODO`, `placeholder`.
- Module 1's `ExternalUrl` item resolves to a real SWOSU SharePoint deck,
  not Savnac/localhost.
- The two real defects on the Monday page (§1) were the only broken
  student-facing links/content found; both repaired and read-back
  verified.
- Slides/decks (32 files across Weeks 2–16): independently verified
  byte-identical against production Canvas in Prompt 103 (Harbor
  downloader false positive, not real drift — see that report §4).

## 6. Sentinel-week walkthroughs

- **Week 1:** Kickoff ownership confirmed (§1). Survive-the-
  Semester/Thrive-in-your-Degree/Entering-your-Career flow present and
  correctly sequenced (`Monday: Survive This Semester` →
  `Wednesday: Thrive In Your Degree` → `Friday: Entering Your Career`).
- **Week 2:** 28 items, technical on-ramp (Monday deck + PM Wed/Fri +
  Odyssey Gate) reachable with correct link tokens (Prompt 105's fix,
  confirmed still wired through `production_deploy.py`).
- **Weeks 6 & 9:** Checkpoint gate (`week-06`/`week-09`) present with
  rubric page, correct 25-pt/15%-group placement, standard weekly
  content (Monday Moment, Wed/Fri readings+slides, A3/A7/A4) alongside.
- **Week 14:** Checkpoint gate + A6 professional-pathway Week 14 update
  present; no evidence of scope creep into a new build sprint — content
  matches the same weekly shape as other checkpoint weeks plus the one
  pathway assignment.
- **Week 15:** No checkpoint (correctly absent — checkpoints are only
  6/9/14), A6 professional-pathway Week 15 *submission* present, standard
  weekly content otherwise. Source (`planning/week-15.md`) confirms fully
  asynchronous design; no in-person requirement anywhere in `planning/`,
  `assignments/`, or `docs/` (checked in Prompt 103 §9).
- **Week 16:** Farkle/ML week present, `not_graded` receipt/reading/slides
  confirmed (§4), no retired Checkpoint 4, A5-final-reflection lands
  here (matches Report 105's documented placement rationale), no broken
  shared Farkle assets found in the module-item sweep.
- **Week 17:** Minimal, correct — `week-17` (not_graded reflection
  placeholder object) + rubric page, no zombie chapter exam.

## 7. Duplicate and zombie sweep

Zero duplicate module-item titles across all 21 modules; zero hits for
every retired-content term searched (§5). No stale 2025/Spring-2026 due
dates and no `lock_at` hiding a due assignment (confirmed in Prompt 103
§7, unaffected by this run's repairs).

## 8. Final repair loop

| Defect | Layer | Fix | Regression test | Commit |
|---|---|---|---|---|
| Leaked kickoff-slot editorial note | `course_foundry` (compiler) | `strip_leaked_slot_editorial_note`, applied at plan-build and live-push render | `tests/test_semester_kickoff_content_map.py::test_strip_leaked_slot_editorial_note_removes_only_the_marker_line`, `::test_kickoff_plan_strips_leaked_slot_editorial_note_from_monday_reading` | `course_foundry` `50801ff` (`main`) |
| Dead Monday exit-ticket link | Canvas state (unresolved link token from original push) | Manual scoped `PUT` of the corrected, compiler-rendered body with the token resolved to the real live assignment | Read-back proof (`24_monday_page_readback.json`) | n/a — live-state repair, not a source change; the *cause* (unresolved-token fallback behavior) is existing, already-correct-by-design code (`_resolve_kickoff_link_tokens` deliberately never guesses a URL) |

Both repairs re-verified by independent read-back after applying (§1).
No CS1 weekly-plan reconcile was affected — rerunning the standard
`--skip-files` dry-run after the `course_foundry` merge still shows
`create=0, update=0, skip=306, delete=0` (`17_repair_dry_run.txt`),
proving the kickoff fix didn't disturb the already-idempotent Weeks
2–17 reconcile.

## 9. Tests and commands run

- `course_foundry` (worktree `flo-103-104-cs1-closeout`, rebased onto
  `origin/main` `9c44935`, merged as `50801ff`):
  `pytest tests/test_semester_kickoff_content_map.py
  tests/test_semester_kickoff_dry_run.py
  tests/test_semester_kickoff_savnac_adapters.py
  tests/test_cs1_desired_course.py tests/test_cs1_savnac_adapters.py
  tests/test_production_deploy.py tests/test_cs1_reference_links.py
  tests/test_load_adapters.py` → **106 passed**.
- Full `tests/` also run: 89 failed / 662 passed — all 89 failures are the
  same pre-existing worktree-relative-sibling-path artifact already
  documented in Reports 103A/105/106 (hardcoded paths under
  `course_foundry.worktrees/course_foundry/...`, unrelated to this diff;
  spot-checked one failure directly to confirm).
- `python -m course_foundry.production_deploy dry-run --course cs1
  --git-parent /mnt/brandy_nvme/jevert/git --skip-files` (post-repair):
  `create=0, update=0, skip=306, delete=0`.

## 10. Commits

- `course_foundry`: `679b805` (fix) → rebased/pushed as `50801ff`, merged
  to `main` (fast-forward from `9c44935`, which itself carried an
  unrelated concurrent Architecture-target-lock change from another
  session — rebased cleanly, no conflict).
- `computer_science_1`: receipts commit `4c3e7e3` on `main`.

## 11. Final production reconcile/read-back after repairs

- CS1 weekly plan (Weeks 2–17): unaffected, idempotent (`17_repair_dry_run.txt`,
  §8).
- Monday kickoff page: independently read back after the manual repair
  (`24_monday_page_readback.json`) — placeholder text gone, exit-ticket
  link has a real, correct `href`.

## Final launch verdict: READY WITH NON-BLOCKING YELLOWS

A student opening the course now can identify the course, find Week 1,
see what's due first, reach every required object, and move through the
semester without encountering broken or contradictory structure. The two
defects found on the opening page were real but did not block task
completion (the exit-ticket assignment was still reachable via the module
list) and are now fixed and verified.

## Remaining yellows

1. **No production-safe kickoff-week reconcile tool.** CS1's Week 1
   content has no standing tool that can push to `74029` the way
   `production_deploy.py` does for Weeks 2–17; any future kickoff-content
   fix needs either the same manual-but-verified treatment this run used,
   or a new production-gated kickoff adapter as its own piece of work.
2. **A10's weighting inside "Semester kickoff week" is unconfirmed, not
   proven wrong** (§4) — worth a deliberate look, not touched blind here.
3. **Harbor's file-verification downloader** still mishandles production
   Canvas's external CDN redirect (documented fully in Report 103 §4);
   any future CS1 file dry-run will keep reporting the same 32 false
   positives until Harbor's redirect handling is fixed for non-Savnac
   hosts, or `--skip-files` plus a direct-bytes check is used again.
