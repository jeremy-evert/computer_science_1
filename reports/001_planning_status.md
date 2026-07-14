# Report 001 — Planning Status (2026-07-14)

## Summary

`planning/` (17 week files, Fall 2026 `COMSC-1033-1415`) and the paired
`course_foundry/planning/course-development-flow.md` workflow doc are
written and reviewed for date accuracy (one bug caught and fixed: Week 16's
Monday/Wednesday were both mislabeled Dec 2; Monday is now correctly Nov
30). `prompts/001_pre_semester_readiness_and_literature_audit.md` lays out
what's left before Aug 17 and has **not been run** — it requires a human
decision pass (Sections 1–3) and a live `curriculum_rag_supporter` query
run (Section 4, needs ChromaDB + Ollama running locally) that hasn't
happened yet.

## What exists now

- `course_foundry/planning/course-development-flow.md` — the reusable
  8-step method (calendar → AI-level mapping → AI lens pull → Professional
  Minds CSV pull → technical unit interleave → holiday-adjustment policy →
  per-week file emission → review), written so it can be re-run for CS
  II/AI II or Discrete Structures/AI III later.
- `computer_science_1/planning/week-01.md` … `week-17-finals.md` — the
  applied result: Status, Weekly Focus, Monday Moments (AI I lens +
  technical tie-in), Wacky Wednesday / Fun Friday (Professional Minds book
  + question), and Due items, for all 16 instructional weeks plus finals.
- `computer_science_1/prompts/001_pre_semester_readiness_and_literature_audit.md`
  — the not-yet-run task list and literature-audit spec described above.

## What does not exist yet (real gaps, not just unreviewed)

- **Professional Minds lesson content.** `professional_minds/lessons/week01/`
  … `week16/` are empty except `.gitkeep`. Only one book (*Make It Stick*)
  has a slurp anywhere in the production pipeline. The planner's Wed/Fri
  anchors point at book titles and questions that have no fifteen-minute
  lesson written yet.
- **Monday Moments entries.** `monday_moments/` still only has `README.md`
  and `template.md` — no week-by-week entries exist, even though the
  planner now anchors each Monday to a specific AI I lens.
- **The literature audit itself.** Section 4 of prompt 001 has not been run
  against `curriculum_rag_supporter` — none of the seven pedagogy questions
  have answers yet, so no literature-grounded verdict exists on the
  planner's pacing, cadence, or holiday policy.

## Concurrent work observed in sibling repos

While this work was happening, other in-flight activity was visible on
disk in adjacent repos (not run or reviewed by me — noted here for
awareness, not audited):

- `ai_fluency/` — new, no commits yet; `ai_i/ ai_ii/ ai_iii/ ai_iv/ ai_v/`
  directories and a `prompts/` folder now exist. This appears to be scaffolding
  for the AI IV (Software Engineering) / AI V (Machine Learning) levels
  referenced in conversation but not yet built.
- `drive_raw_pull_2026-07-14/` — a fresh export of Google Drive planning
  docs (AI I/II/III course docs, course blueprints, the Professional Minds
  integrated plan, teaching philosophy/blueprint docs), timestamped ~17:21,
  contemporaneous with this session.
- `computer_science_1/prompts/001_course_development_source_walk.md` and
  `computer_science_1/prompts/README.md` — written by another process, not
  by me, and already present in this repo's working tree alongside my own
  `001_pre_semester_readiness_and_literature_audit.md`.
- `professional_minds/` picked up an untracked `professional_minds.csv`
  (previously present but never committed), a modified `prompts/README.md`,
  and a new `prompts/009_course_development_source_walk.md` — left
  untouched here since it's outside this repo and appears to be another
  agent's in-progress work.

## Recommended next step

Work `prompts/001_pre_semester_readiness_and_literature_audit.md` — Sections
1–3 need Jeremy's decisions, Section 4 needs `curriculum_rag_supporter`
running locally. Given the concurrent activity in `ai_fluency/` and
`professional_minds/`, it's also worth reconciling prompt-numbering
conventions across repos before more `001_*.md` files accumulate with
different slugs across `computer_science_1`, `professional_minds`, and
`ai_fluency`.
