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

1. **Resolved 2026-07-22: pre-semester readiness decisions have been made
   and applied.** `reports/002_pre_semester_readiness_and_literature_audit.md`
   (completed 2026-07-16) surfaced six items under "Decisions Jeremy Must
   Make." Jeremy answered all six (drafted with ChatGPT, pasted in
   2026-07-22 — treated as concrete-enough-to-apply but **not final/locked**)
   and they've been applied to `planning/` and related files:
   `reports/005_apply_pre_semester_decisions.md` is the application record;
   `jeremy_task_tracking/DECISIONS.md`'s 2026-07-22 entry is the durable
   cross-repo decision log. Summary: (1) Weeks 5–6 — Week 6 is loop
   review/practice with functions as an ungraded preview only, full
   functions instruction stays in Week 7; (2) Thanksgiving (Week 15) is now
   a **fully asynchronous week** (Jeremy traveling), not just the old
   Wed+Fri-holiday skip — material pre-recorded and loaded ~Nov 1; (3)
   content-authoring is scoped to the three Fall 2026 courses only (CS1,
   CS2, Discrete Structures — SE/ML/AI Fluency 2–5 deferred to spring),
   with CS1 Week 2 as the first full pipeline test; (4) the missing AI I
   doc is no longer a blocker — `ai_fluency` is now the authoritative
   source, AI Fluency 1 only for fall; (5) the online section
   (`COMSC-1033-1414`) is in scope, sharing CS1's Canvas structure, with a
   defined-but-not-yet-built attendance/check-in/disengagement-check
   system; (6) the professional-pathway portfolio is staged across the
   semester (Week 1 baseline, Week 14 update, Week 15 completion) instead
   of dumped in Week 16. `reports/006_pre_semester_decisions_recheck.md`
   re-audits the planner against these six decisions. **Resolved
   2026-07-22 (separately, after Report 006):** Report 002's lower-priority
   Week 9 checkpoint-1-timing question. Rather than moving the Week 9
   checkpoint to Week 10 as Report 002 suggested, added a new, lighter
   Coding Odyssey checkpoint 1 ("baby project" / dry run) at Week 6 —
   already the week `planning/block-map.md` scheduled Coding Odyssey
   planning — and renumbered checkpoints 1→2, 2→3, 3→4 at Weeks 9/14/16.
   Week 9's checkpoint is now a genuine second check-in rather than the
   first, so the first-time-submission overhead Report 002 flagged is
   absorbed earlier, in a full week, instead. See
   `reports/007_coding_odyssey_baby_project_checkpoint.md`.
2. **Literature-grounded audit is done.** Section 4 ran successfully
   against `curriculum_rag_supporter` (corpus already ingested, 29 books;
   no blockers) and all seven queries executed — but evidence quality
   varied query to query (moderate for four, weak/inconclusive for two,
   and two answers included content flagged as the model's own synthesis
   rather than a direct citation). See Report 002's Literature Audit
   Findings section for the per-query strength-of-evidence breakdown; do
   not describe this audit as uniformly "strongly literature-grounded."
3. **Correction (2026-07-20): Professional Minds lesson content does exist —
   it just doesn't live in `professional_minds/lessons/weekNN/`.** Those 16
   folders are indeed still `.gitkeep`-only (that part of Report 002/004 was
   right), but real content lives elsewhere in that same repo:
   `professional_minds/readings/week_NN_{wed,fri}_*.md` and
   `presentations/beamer/week_NN_{wed,fri}/` (compiled decks), tracked
   authoritatively in that repo's own
   `indexes/session_coverage_matrix.md`. As of that matrix (built
   2026-07-18/19, with more added same-day 2026-07-20): **weeks 2–11 are
   session-complete** (day-specific reading + presentation + compiled
   Beamer PDF), weeks 12–14 have one shared week-level artifact per week,
   and weeks 15–16 plus 2 unscheduled slots are still genuinely missing.
   Check that matrix directly for current status rather than this file.
4. **Correction (2026-07-20): Monday Moments entries exist, just not in
   this repo.** `monday_moments/` here still has only `README.md` and
   `template.md` — that folder is not, and was never meant to be, the
   canonical home. The canonical copy is
   `ai_fluency/ai_i/monday_moments/week_NN_<slug>/` (CS1 carries the "AI I"
   level) — 3 of 16 weeks are written there as of 2026-07-20
   (`week_01_define_the_problem`, `week_02_gather_context`,
   `week_03_plan_the_work`), each independently quality-audited. See
   `NAMING.md` for the full pointer.
5. **Source-availability gap: resolved by decision, 2026-07-22.**
   Report 002 could not locate either the "AI I: Thinking with AI" course
   doc or `professional_minds/professional_minds.csv` anywhere under
   `/data/git`. Both `professional_minds` and `ai_fluency` were
   subsequently pulled as full repositories and reconciled in Report 004
   (2026-07-16, later same day):
   - `professional_minds.csv` **is now found** (committed 2026-07-14) and
     every one of the 16 weeks in `planning/` matches it exactly — this
     half of the gap is resolved.
   - The AI I: Thinking with AI document **is still not located on disk**
     (unchanged by a 2026-07-20 `ai_fluency` recovery pass, which recovered
     strong candidate source material for AI I–III but not the original
     document itself). **This is no longer being treated as a blocker.**
     Jeremy's 2026-07-22 decision: stop chasing fidelity to a document that
     can't be found; treat `ai_fluency` itself as the authoritative source
     going forward, scoped to AI Fluency 1 only for the three Fall 2026
     courses. See `reports/005_apply_pre_semester_decisions.md`. Not yet
     done: reconciling `ai_fluency`'s own AI II–V architecture reports
     (008–010) against this narrower scope call.

6. **New, 2026-07-22: online-section attendance system — decided in scope,
   not yet built.** `COMSC-1033-1414` shares CS1's Canvas structure (no
   separate authoring). Needed: three brief Mon/Wed/Fri check-ins per week
   for online students (piggybacked on existing activities where possible,
   graded for completion), assigned only to the online section; a rolling
   Mon/Wed/Fri disengagement check (7+ days no qualifying activity →
   auto-reminder → single instructor review report, not per-student daily
   noise). This is a `course_foundry`/Harbor build (new Canvas items +
   automation), not a planning-file change — not started.

## Next step (updated 2026-07-22)

Decisions are landed and applied (see item 1 above). Per Jeremy's
2026-07-22 content-authoring-cadence decision, Fall 2026 production is
scoped to three courses only — **Computer Science 1, Computer Science 2,
Discrete Structures and Critical Thinking** — with Software Engineering,
Machine Learning, and AI Fluency 2–5 deferred to spring. The approved
order:

1. Finish any remaining course-design decisions for each of the three fall
   courses.
2. **CS1 Week 2 is the pipeline test.** Every lecture artifact needs a
   student handout, instructor slides, a paired assignment/practice
   activity, an aligned rubric, and a successful Course Forge test —
   verified as Canvas-ready before multiplying artifacts further.
3. Once Week 2 passes reliably, run the same pipeline through the rest of
   CS1 (weeks 4–16 still need Monday Moments and the remaining Professional
   Minds slots — see items 3–4 above for current per-repo status).
4. Repeat for CS2, then Discrete Structures.
5. Build one shared AI Fluency 1 (not II–V) for use across all three.

`reports/006_pre_semester_decisions_recheck.md` is the current readiness
recheck against these six decisions — read it for the concrete verdict
before treating this repo as ready to load further into Canvas/Savnac.

**Correction (2026-07-20), still accurate:** the book-slurp pass and
content-filling are further along than a from-scratch reading of this file
would suggest — see items 3–4 above. Check
`professional_minds/indexes/session_coverage_matrix.md` and
`ai_fluency/ai_i/monday_moments/README.md` for current status.

## After that

Continue filling Professional Minds' remaining slots and Monday Moments
weeks 4–16, at the lead-time cadence Jeremy chooses (Report 002 recommends
2–3 weeks ahead of each week taught, not full front-loading or strict
just-in-time). A bounded Savnac pilot push (weeks confirmed content-ready
across all three repos) is already in progress — see
`docs/savnac-canvas-access.md` — and continues incrementally as more weeks
become content-ready, per Report 006's readiness verdict, ahead of full
Canvas population (`reports/003_canvas_capability_planning.md`).
