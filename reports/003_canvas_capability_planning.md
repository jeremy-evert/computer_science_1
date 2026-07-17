# Report 003 — Canvas Capability Planning (2026-07-16)

## Summary

This report expands `reports/001_planning_status.md` (2026-07-14) with a
Canvas build plan, drawing on Harbor's `canvas-capability-catalog.md`
(live inventory 2026-07-16). The 17-week Fall 2026 plan (`planning/week-01.md`
… `week-17-finals.md`) and the nine-lesson technical sequence (`lessons/`)
are written and internally consistent, and the course's two live Canvas
shells for `COMSC-1033` are real and reachable — but both are empty and
unpublished. Nothing has been written to Canvas yet, and two content gaps
tracked in `ROADMAP.md` (Professional Minds lessons, Monday Moments entries)
still don't exist, so a Canvas build right now would have modules and pages
with no content behind large parts of them. This report lays out which
Canvas building blocks to use, in what order, once those gaps close.

## What exists now (carried forward from 001, updated 2026-07-16)

- `course_foundry/planning/course-development-flow.md` — the reusable
  8-step method (calendar → AI-level mapping → AI lens pull → Professional
  Minds CSV pull → technical unit interleave → holiday-adjustment policy →
  per-week file emission → review). Was briefly missing at the 001 pull
  but landed in `course_foundry` main the same day (commit `0885660`) —
  resolved, no longer a blocker.
- `computer_science_1/planning/week-01.md` … `week-17-finals.md` — the
  applied 17-week plan: Weekly Focus, Monday Moments anchor, Wacky
  Wednesday/Fun Friday Professional Minds anchor, and Due items.
- `computer_science_1/lessons/01-foundations-print-input.md` …
  `09-projects-tools-and-reflection.md` — the nine-lesson technical
  sequence underlying the weekly plan.
- `computer_science_1/prompts/001_pre_semester_readiness_and_literature_audit.md`
  — not yet run. Sections 1–3 need Jeremy's decisions (pacing, holiday
  policy, content-authoring order); Section 4 (literature audit against
  `curriculum_rag_supporter`) hasn't been executed.
- Still missing, per `ROADMAP.md`: Professional Minds 15-minute lesson
  content for any of the 16 books (only `books/slurps/make_it_stick.md`
  exists anywhere in that pipeline), and all `monday_moments/` week entries
  (only `README.md` and `template.md` exist).

## Canvas shell reality check

Per the catalog's live inventory (2026-07-16), Harbor can already see two
real Fall 2026 `COMSC-1033` shells:

| Canvas course | Section | State | Assignments | Modules | Module items | Pages | Quizzes | Discussions | Files | Rubrics |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 74033 | 1414 | unpublished | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 74029 | 1415 | unpublished | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

`1415` is the in-person MWF section the planner is written for
(`docs`/`archive` per prompt 001); `1414` is the parallel online section,
which prompt 001 explicitly flags as a distinct planning exercise (MWF
anchors don't map cleanly to async). This report's Canvas recommendations
target `1415` first.

## Recommended Canvas construction palette for CS1

Mapped to this course's actual materials, using the catalog's status
labels as-is (**Harbor now** / **Canvas/API available** / **needs design**):

- **Modules** — one per week, mirroring `planning/week-01.md` …
  `week-17-finals.md` directly. *Harbor now: list/read; create/update
  partial.*
- **Pages** — lesson content from `lessons/01-foundations-print-input.md`
  … `09-projects-tools-and-reflection.md`, plus Monday Moments and
  Professional Minds 15-minute lessons once those are authored. *Harbor
  now: read, create, and update paths exist.*
- **Assignments** — the weekly Due items already named in the planner.
  Recommended submission types per artifact: `online_upload` for `.py`/zip
  code submissions, `online_url` for repo/deployed-demo links, and
  `online_text_entry` for reflections and debugging narratives. *Harbor
  now: read, create, and update paths exist.*
- **Rubrics** — built to match the course's existing effort-based,
  demonstrative grading norm (per `docs/philosophy/teaching-patterns.md`,
  cited in prompt 001) rather than a stricter standard the planner doesn't
  currently use. *Harbor now: read/create/update paths exist; the review
  gate stays external to Canvas.*
- **Files** — starter code and reference artifacts attached per lesson.
  *Harbor now: read/download support exists; the upload workflow is not
  yet cataloged as ready — this is a dependency to close before Files
  becomes part of the build, not a blocker to planning around it.*
- **Discussions** — weekly reflection/question threads, a natural fit for
  the course's informal, relational tone. *Canvas/API available; read/list
  is reachable through module-item terminology, but there is no dedicated
  Harbor build path yet — flag as a gap to close before relying on this
  for graded interaction.*
- **Quizzes** — recommend using these narrowly, only where retrieval
  practice or an automated checkpoint clearly earns its place (e.g., after
  the loops or functions units), per the catalog's own guidance not to
  reach for quizzes by default. *Not yet exposed in Harbor at all — any
  quiz-based checkpoint needs an explicit decision and Harbor support
  before it can be planned as real.*

Deliberately excluded from this first build — each is either
**Canvas/API available** with no current Harbor path, or explicitly
**needs design** per the catalog, and none is required for a first
meaningful course build: sections, assignment groups, navigation tabs,
syllabus automation, groups/group sets, peer review, outcomes, New
Quizzes content, and external tools/LTI.

## Sequencing recommendation

Canvas population should follow the content work already tracked as gaps
in `ROADMAP.md`, not run ahead of it. Professional Minds lessons and
Monday Moments entries don't exist yet, so building their Canvas pages now
would create modules with nothing behind them. Recommended order:

1. Jeremy completes prompt 001 Sections 1–3 (pacing, holiday-adjustment
   policy, content-authoring order — including whether Monday Moments and
   Professional Minds content are front-loaded or built just-in-time).
2. Content gets authored week by week, per whichever cadence Section 3
   settles on.
3. Canvas modules, pages, and assignments get built in the same weekly
   cadence, staying ahead of the Aug 17, 2026 start — not as one large
   pre-semester import into the empty shells.

## Harbor readiness gaps to close before a real deployment

Directly from the catalog's "Next catalog expansions" and "Safety notes":

- No dedicated create/update helpers yet for module items or file uploads.
- No dry-run course package manifest showing proposed writes before a
  human-approved deployment, and no idempotency receipt per write.
- Student data — enrollments, submissions, grades, comments, PII — must
  stay behind separate, explicit gates from course-content planning. This
  report and the recommended build only concern course structure and
  content, never student records.

## Recommended next step

Two tracks, running in parallel:

1. **Content decisions** — Jeremy works prompt 001 Sections 1–3 end to
   end, per `ROADMAP.md`'s existing "Next step," so week-by-week content
   authoring can start.
2. **Canvas pilot** — once Harbor's module-item/file create helpers and a
   dry-run manifest exist, run a single scoped write (Week 1's module only,
   into shell `74029`/section `1415`) as a validation pilot, reviewed
   before any attempt to populate all 17 weeks.
