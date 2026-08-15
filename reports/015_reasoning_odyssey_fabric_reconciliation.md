# Prompt 015 — Reasoning Odyssey fabric reconciliation

## Result

The durable, student-facing course concept is now **Reasoning Odyssey**.
`assignments/A2-coding-odyssey-project.md` is explicitly the Week-2 kickoff
and home base: it introduces the persistent project, explains that weekly
learning returns to the same world, and defines the World Bible as its living
record. The World Bible remains inside the gates/checkpoints; it was not
renamed or made into a separate assignment track.

## Changed files

| File(s) | Why changed |
|---|---|
| `assignments/A2-coding-odyssey-project.md` | Retitled and reframed as the Week-2 Reasoning Odyssey kickoff/home base; clarified the World Bible and recast Weeks 6/9/14 as synthesis checkpoints. |
| `assignments/A1-weekly-coding-practice.md`, `assignments/A5-final-reflection.md`, `assignments/W16-farkle-ml-experiment-receipt.md` | Replaced current student-facing doctrine references with Reasoning Odyssey. |
| `assignments/odyssey_gates/week-05.md`, `week-08.md`, `week-16.md`, `week-17.md` | Replaced current student-facing references with Reasoning Odyssey. |
| `assignments/odyssey_gates/week-06.md` | Renamed the active task and made it a no-new-concept, paid synthesis checkpoint: submit, explain, demonstrate, and reflect. |
| `assignments/odyssey_gates/week-09.md` | Renamed the active task and removed the new collections requirement; it now consolidates prior work, with a paid submit/explain/demonstrate/reflect contract. |
| `assignments/odyssey_gates/week-14.md` | Renamed the active task and explicitly identifies it as a deeper synthesis/consolidation checkpoint, not a new feature deadline. |
| `rubrics/odyssey_gates/week-06_rubric.md`, `week-09_rubric.md`, `week-14_rubric.md` | Renamed the checkpoint rubrics; Weeks 6 and 9 now assess synthesis/reflection rather than a newly introduced concept. Point totals remain 25. |
| `lessons/02-variables-expressions-types.md`, `lessons/09-projects-tools-and-reflection.md` | Replaced student-facing doctrine labels. |
| `docs/syllabus.md`, `docs/course-ethos.md`, `docs/grading-model.md`, `docs/curriculum/course-sequence.md`, `docs/curriculum/recommended-resources.md`, `docs/curriculum/unit-map.md`, `docs/philosophy/teaching-patterns.md` | Replaced current-course/student-facing doctrine labels and synchronized the Week 6/9/14 synthesis description. |

## Gate and rubric audit

All 16 files in `assignments/odyssey_gates/` have matching files in
`rubrics/odyssey_gates/`. Active gate/checkpoint weeks have guidance, an
assignment task, a paired rubric, a submission path (`online_text_entry` and
`online_upload` in the grading model), and 25 points through the existing
weekly-reinforcement or checkpoint structure. Weeks 6, 9, and 14 are now
explicitly synthesis/checkpoint weeks, retain their submission and rubric
contracts, and retain 25 points each.

Two pre-existing exceptions remain and were not changed because assigning
points would require inventing a grading allocation contrary to the pinned
gradebook:

- `assignments/odyssey_gates/week-15.md` and its rubric deliberately define
  an optional, ungraded buffer week; the required graded work is A6.
- `assignments/odyssey_gates/week-16.md` and its rubric deliberately retire
  the Odyssey gate/checkpoint; the Farkle/ML receipt is explicitly ungraded.

These exceptions conflict with the broad “every week” paid-check-in doctrine,
but changing them would create a new paid requirement without a corresponding
existing gradebook allocation. They are left for an explicit grading-model
decision rather than guessed changes.

## Coding Odyssey hit audit

Changed: all current, student-facing/doctrine hits in the files listed under
“Changed files,” including A2, A1/A5/W16 receipt, active gate/checkpoint
files, their affected rubrics, lessons, syllabus, current curriculum/ethos,
and grading-model documentation.

Deliberately left:

- `assignments/A2-coding-odyssey-project.md` (Design history) and
  `assignments/odyssey_gates/week-06.md` (quoted historical provenance):
  archival record of the old name.
- `docs/reports/curriculum-history-synthesis.md`: explicit curriculum-history
  report.
- Every remaining hit in `planning/`: instructor-only planning/provenance,
  including the expressly confirmed archival
  `planning/coding-odyssey-arc-map.md`; this includes `block-map.md`,
  `fall-2026-course-design.md`, `week-01.md` through `week-17-finals.md`,
  and `zybooks-assignment-map.md` where applicable.

## Grading and verification

No grade weights, point values, grading categories, or
`course_metadata.yaml` grading block were changed. Existing 25% weekly
reinforcement and 15% Reasoning Odyssey checkpoint weights remain intact.

No content-structure test suite exists; the repository's available tests are
Farkle engine/learner tests, not assignment-content tests. The full available
suite was run successfully: `pytest -q` — **27 passed**.
