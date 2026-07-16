# Roadmap

This file tracks the ongoing, big-picture state of `computer_science_1` —
what's built, what's open, and what the next concrete step is. Update it as
work lands; don't let it drift into a stale planning doc nobody reads.

This is a new file (created 2026-07-16) — there was no roadmap before this,
only a point-in-time snapshot in `reports/001_planning_status.md`. Treat that
report as history, and this file as the living version going forward.

## Where the course stands (2026-07-16)

- The 17-week Fall 2026 plan (`planning/week-01.md` … `week-17-finals.md`)
  and the nine-lesson technical sequence (`lessons/`) exist and are
  internally consistent.
- The course starts **Monday, Aug 17, 2026** (`COMSC-1033-1415`).

## Real gaps (not just "unreviewed")

1. **Pre-semester readiness decisions are still not made.**
   `reports/002_pre_semester_readiness_and_literature_audit.md` (completed
   2026-07-16) ran the full readiness review and literature audit from
   `prompts/001_pre_semester_readiness_and_literature_audit.md` Sections
   1–4. Sections 1–3 still need Jeremy's read/decide pass — the report
   surfaces six concrete decisions (Weeks 5–6 pacing, Week 9 checkpoint
   placement, Week 16 overload, Thanksgiving holiday-skip policy,
   content-authoring cadence, AI I doc fidelity, section scope) but does
   not and should not decide them.
2. **Literature-grounded audit is done.** Section 4 ran successfully
   against `curriculum_rag_supporter` (corpus already ingested, 29 books;
   no blockers) — see Report 002's Literature Audit Findings section for
   all seven queries, their sources, and their strength of evidence.
3. **Professional Minds lesson content doesn't exist.** Confirmed again in
   Report 002: all 16 `professional_minds/lessons/week01/`…`week16/`
   folders are still `.gitkeep`-only; only one book (*Make It Stick*) has
   even a first-stage slurp, no DNA card or lesson for any book.
4. **Monday Moments entries don't exist.** Confirmed again in Report 002:
   `monday_moments/` still has only `README.md` and `template.md` — 0 of
   16 week entries written.
5. **Two planner source documents can't currently be located.** The "AI I:
   Thinking with AI" course doc and `professional_minds/professional_minds.csv`
   (both named as inputs in `course_foundry/planning/course-development-flow.md`)
   are not found anywhere under `/data/git` as of the Report 002 audit —
   this blocks verifying the existing Monday/Wednesday/Friday anchors in
   `planning/` against their stated sources. New gap surfaced by Report 002,
   not previously tracked here.

## Next step

Jeremy reads `reports/002_pre_semester_readiness_and_literature_audit.md`
and works through its "Decisions Jeremy Must Make" section (six items,
including the Week 6 and Week 16 pacing risks and the Thanksgiving holiday
policy). Once those land, a follow-up prompt applies any approved changes
to `planning/` — Report 002 deliberately made no changes there itself.
Locating gap 5's missing source documents (or confirming they were
intentionally superseded) should happen alongside that decision pass.

## After that

Once readiness decisions are made: start filling Professional Minds lesson
content and Monday Moments entries, at the lead-time cadence Jeremy
chooses (Report 002 recommends 2–3 weeks ahead of each week taught, not
full front-loading or strict just-in-time). Canvas population
(`reports/003_canvas_capability_planning.md`) stays sequenced after this,
per that report's own recommendation.
