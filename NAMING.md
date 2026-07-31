# NAMING.md — CS1 content naming conventions

This file exists so anyone (Jeremy, a future session, the `course_foundry`
adapter that reads this repo) can tell what a filename means without having
to ask. Update it when a new content category is added; don't let naming
drift ahead of what's written here.

## Numbered content already consistent — unchanged

- `lessons/NN-topic-slug.md` — the nine-lesson technical sequence.
- `planning/week-NN.md` (+ `week-17-finals.md`) — the 17-week Fall 2026 plan.
- `prompts/NNN_slug.md` ↔ `reports/NNN_slug.md` — a documented 1:1 contract
  per `START_HERE.md`, going forward from `005` (see the collision note
  below for why `005` and not `002`).

## Free-text content — `A<n>`/`Q<n>`/`T<n>` numbering (added 2026-07-20)

- `assignments/A<n>-slug.md` — reusable assignment *templates*, numbered in
  first-introduced order (by which week's `planning/week-NN.md` first
  references them), not per-week instances:
  - `A1-weekly-coding-practice.md` (first used Week 2)
  - `A2-coding-odyssey-project.md` (Week 9)
  - `A3-pair-programming.md` (Week 10)
  - `A4-show-and-tell-reflection.md` (Week 14)
  - `A5-final-reflection.md` (Week 16/17)
  - `A6-professional-pathway-artifacts.md` (Week 16)
- `quizzes/Q<n>-slug.md` — same pattern: `Q1-getting-to-know-you.md` (Week 1),
  `Q2-chapter-exam.md` (Week 17, optional/historical per its own text).
- `templates/T<n>-slug.md` — same pattern: `T1-assignment-template.md`,
  `T2-rubric-template.md`, `T3-syllabus-template.md`.
- Per-week *instances* of these are not separate files — `planning/week-NN.md`'s
  "Due this week" line linking to the specific `A<n>`/`Q<n>` file *is* the
  instance record. This already matches how `lessons/` is referenced inline;
  the new numbering just makes `assignments/`/`quizzes/`/`templates/`
  consistent with that pattern instead of using free-text slugs with no
  ordering signal.

## `templates/T<n>-slug.md` — orientation templates are now two kinds (added 2026-07-31)

`T1`-`T3` (assignment/rubric/syllabus) are human-facing fill-in-the-blank
guides — a person copies the shape and writes the content by hand. `T4` and
`T5` (added by `course_foundry/prompts/022_cs1_savnac_layout_and_navigation_template.md`)
are a different kind: **script-fillable** templates, meant to be read and
populated programmatically, not copy-pasted by a person. Both still use the
same `T<n>-slug.md` numbering — the distinction is in each file's own header,
not a separate numbering scheme:

- `T4-module-overview.md` — the per-module Overview page (first item in
  every weekly Canvas module, per `docs/canvas-module-checklist.md`'s
  "Overview page" line). `{{DOUBLE_BRACE}}` placeholders are filled in by
  `course_foundry/cs1_savnac_layout_and_navigation.py` from that week's
  actual `DesiredCourse` module contents (`cs1_desired_course.py`) — the
  page regenerates itself as content changes, no separate weekly upkeep.
- `T5-start-here.md` — the one-time, richer week-1 orientation page,
  linked from inside Module 1, never set as `default_view`/front page.
  Its factual content (weekly rhythm, six weekly artifacts, A1-A6
  canonical-week table) traces to `docs/course-ethos.md` and
  `cs1_desired_course.py`'s already-decided placement, not re-derived.

Both are written to be reusable by CS2/DSCT/SE/ML's own version later
(`docs/repo-map.md`'s "promote reusable patterns up to `swosu_cs_curriculum`"
note), not one-off pages that only make sense for CS1 week 1.

## `reports/` — a known, accepted numbering collision (grandfathered)

`reports/002`, `003`, and `004` each have **two different files sharing the
same numeric prefix** (`002_pre_semester_readiness_and_literature_audit.md`
vs. `002_repo_inventory_and_gap_report.md`, and so on for 003/004). Each
file's own `# Report NNN — ...` heading and cross-referencing prose
("Report 002 found that...") is part of its content, not just its filename —
several reports refer to *each other* by number in running text, including
`004_source_reconciliation_and_slurp_status.md`'s extensive references to
"Report 002." A rename would require rewriting that historical analysis
prose throughout, which risks introducing new inconsistencies for no real
benefit — grandfathered as-is, per this project's standing "don't rewrite a
trail that already happened" doctrine (`jeremy_task_tracking/AGENTS.md`,
"Run evidence" section).

**Going forward: the next new report is `005_slug.md`** (the first unused
number) — do not reuse 002/003/004 again, and do not attempt to retrofit the
existing six files into a clean sequence.

## `monday_moments/` — canonical home is `ai_fluency`, not here

`computer_science_1/monday_moments/` holds only `README.md` and
`template.md` — **it is not where Monday Moment content lives.** The
canonical copy is `ai_fluency/ai_i/monday_moments/week_NN_<slug>/` (CS1
carries the "AI I" level of the shared five-course AI sequence; confirmed
2026-07-20). Each real week there is a folder, not a single file:
`monday_moment.md`, `instructor_guide.md`, `student_activity.md`,
`assessment_rubric.md`, `portfolio_artifact_*.md`. As of 2026-07-20, weeks
1–3 are written (`week_01_define_the_problem`, `week_02_gather_context`,
`week_03_plan_the_work`); weeks 4–16 are not yet written. This repo's own
`monday_moments/` folder should not gain real content — see its `README.md`
for the pointer.

**Exception: Week 1 is universal**, not sourced from `ai_fluency` — its
Monday Moment topic ("Getting the most out of this class and this
semester") is authored directly inline in `planning/week-01.md`, per that
file's own note that Week 1 supersedes the AI-lens pairing for every course.

## The `course_foundry` / harness bridge — two unrelated `course_id`s

Anyone writing or reading a `course_foundry` adapter for this repo needs to
keep two different things straight, both called `course_id` in different
parts of that codebase:

- **Pipeline layer** (`load_adapters.py`, `sync_adapters.py`, `state.py`,
  nodes `n001`–`n003`): `course_id: int` — a real numeric **Canvas** course
  id. Savnac's CS1 test course is `1`; the old UCS101 sandbox was `24298`.
  `register_load_adapter(course_id: int, adapter)` keys off this number.
- **Harness/benchmark layer** (`harness/guidepost_student_fn.py`,
  `personas/`, `storage/build_pvc.py`): `course_id: str` — a short label
  like `"CS1"`, paired with `fixture_id: str` like `"F1"`. Used only for
  fixture storage paths (`fixtures/CS1/F1/fixture.json`) and rubric cache
  filenames (`CS1-F1_rubric.json`); reusable across the five-course
  portfolio (`CS1`/`CS2`/`DSCT`/`SE`/`ML`) per `personas/README.md`. Never
  touches Canvas and is unrelated to the numeric id above.

Do not merge these two ideas — a Savnac load adapter registers under the
numeric `1`, never the string `"CS1"`.
