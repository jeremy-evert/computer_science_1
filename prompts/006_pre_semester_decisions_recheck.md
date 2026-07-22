# Prompt 006 — Re-Audit the Planner Against Report 005's Applied Decisions

## Context

`reports/005_apply_pre_semester_decisions.md` applied Jeremy's six pasted
decisions (2026-07-22, not final/locked) to `planning/`,
`assignments/A6-professional-pathway-artifacts.md`, `ROADMAP.md`,
`START_HERE.md`, `prompts/README.md`, and one shared status type in
`course_foundry/planning/course-development-flow.md`. Before treating the
repo as clean enough to resume loading content into Savnac, re-check that
the edits actually landed correctly, are internally consistent with each
other and the rest of the planner, and didn't introduce a new overload or
consistency problem while fixing the old ones.

## Task

For each of Report 002's six original findings, confirm the current state
against the decision that was supposed to resolve it:

1. Weeks 5–6 — does `week-06.md` now read as loop-review + ungraded
   functions preview, with Week 7 still carrying full functions
   instruction?
2. Thanksgiving/holiday policy — does `week-15.md` correctly read as fully
   asynchronous (not just Wed+Fri), with the Nov-1 lead time and the
   "cut weakest content first" framing intact? Does
   `course_foundry/planning/course-development-flow.md` carry the new
   status type generally, not Thanksgiving-hardcoded? Confirm
   Monday-holiday (Week 4), Friday-holiday (Week 9), and finals week
   (Week 17) are genuinely untouched.
3. Content-authoring cadence — is the three-course Fall 2026 scope and the
   CS1-Week-2-pipeline-test-first order recorded in `ROADMAP.md`?
4. AI I doc fidelity — does `ROADMAP.md`/`START_HERE.md`/`prompts/README.md`
   correctly describe this as resolved-by-decision (not still blocked),
   without overclaiming the document was actually found?
5. Online section scope — is the decision and the deliberately-not-built
   system shape recorded in `ROADMAP.md` as a real, scoped gap?
6. Week 16 redistribution — does the Week 1 → Week 14 → Week 15 → Week 16
   chain actually connect (each week's text points at the next), and does
   `week-16.md` no longer carry the 7-artifact due item?

Also check, as new-risk review (not just compliance):

- Does Week 15 (now fully async, formerly lighter) carry an appropriate
  load for an unsupervised week, or did stacking the portfolio-completion
  due item onto it recreate a version of the original Week 16 overload?
- Is Report 002's still-open, lower-priority Week 9 item (Coding Odyssey
  checkpoint 1 timing) still correctly left alone rather than accidentally
  resolved or contradicted?
- Are Weeks 12–13 (previously confirmed fine, no decision needed) still
  unaffected?
- Any stale cross-references left in `README.md`, `docs/curriculum/course-sequence.md`,
  or other untouched files that now contradict the applied decisions?

Do not re-run the Section 4 literature audit from
`prompts/001_pre_semester_readiness_and_literature_audit.md` — none of the
six decisions contradict its findings; note it as still valid, not
re-verified line by line.

## Report

Write `reports/006_pre_semester_decisions_recheck.md`: one subsection per
item above (current state, verdict — landed cleanly / landed with a note /
not landed), a new-risk-review section, an updated readiness verdict table,
and an explicit recommendation on whether the repo is clean enough to
resume the Savnac pilot push for any newly-touched weeks (1, 6, 14, 15, 16)
alongside the already-pushed weeks 1–3.

## Requirements

Read-only audit — do not edit `planning/`, `assignments/`, `ROADMAP.md`, or
any other content file while running this prompt. If something reads as
not-yet-landed or newly inconsistent, report it; a further fix is a
follow-up prompt, same discipline as Report 002 followed.
