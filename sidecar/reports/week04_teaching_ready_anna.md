# Anna report — CS1 Week 4 teaching-ready source

## Assignment

- Work file: `foreman_interface/jobs/tasks/anna_cs1_week04_ready.md`
- Run: `f3ca7417d4bdf117c002e085d8671172`
- Work-file SHA-256: `393752b706ed6ccd553a20af8eb353f4f1b139bad541ab756f531ae30fbcdec1`
- Branch: `anna/cs1-week04-ready`
- Shared compiler branch: `anna/cs1-week04-links`

## Summary

Week 4 now has a student-facing decision-logic path. The branching lesson
adds decision tables, boundary and invalid-case testing, downstream state
changes, and the explicit AI Fluency Lens 4 (Decompose the Task) connection.
The Week 4 plan gives Wednesday and Friday concrete student paths, and the
Odyssey Gate directs students to the lesson before implementation.

The existing `{{link:...}}` mechanism was extended in the isolated Course
Foundry worktree for the two Week 4 targets: page `03-branching` and
assignment `week-04`. No Canvas or production action was taken.

## Changed files

CS1:

- `lessons/03-branching.md`
- `planning/week-04.md`
- `assignments/odyssey_gates/week-04.md`
- `sidecar/reports/week04_teaching_ready_anna.md`

Course Foundry:

- `course_foundry/cs1_reference_links.py`
- `tests/test_cs1_reference_links.py`

No rubric or points file was changed.

## Pattern match and cross-reference proof

The work follows the existing Weeks 2–3 shape: the weekly plan names the
technical focus and day-by-day Professional Minds path, the lesson carries
the runnable examples and vocabulary, and the Odyssey gate remains the
small, pass/fail assignment with an optional continuation. Week 4 adds the
deeper branching content required by its plan without changing the settled
gate rubric.

The source uses:

- `{{link:week04_branching_lesson}}` -> module item title `03-branching`
- `{{link:week04_odyssey_gate}}` -> module item title `week-04`

The pure resolver test confirms both become real Canvas-relative URLs. The
local desired-course inspection confirmed the Week 4 gate's lesson reference
resolved to `/courses/1/pages/03-branching`, with no raw token remaining.
The lesson is canonically placed once by the existing first-reference rule;
the Week 4 module does not duplicate it. The gate appears once.

The local farm's full CS1 readiness scan currently reports no Week 4 module
because the sibling `professional_minds` and `ai_fluency` Week 4 source
folders are absent in this checkout. That is a YELLOW environmental
limitation, not a reason to invent or copy sibling-course content into CS1.

## Rubric and points

Before/after comparison of the Week 4 gate's `submission_types`,
`grading_type`, `points_possible`, `assignment_group`, `due_at`, and
`rubric_criteria`: identical. The Week 4 rubric remains byte-identical to
the starting tree.

## Validation

- CS1 `pytest -q`: **32 passed**.
- Course Foundry focused suite (`test_cs1_reference_links.py`,
  `test_cs1_content_map.py`, `test_cs1_desired_course.py`): **43 passed**.
- `git diff --check`: passed in both worktrees.
- `make task-check`: unavailable in both repos — `make: *** No rule to make target 'task-check'. Stop.`
- `make check`: unavailable in both repos — `make: *** No rule to make target 'check'. Stop.`
- No Canvas, Instructure, Harbor, or production deploy command run.

## Git and AGENTS status

Effective identity was already configured: `jevert <jeremy.evert@swosu.edu>`.
Shared `AGENTS.md` was read and followed. No repo-local `AGENTS.md` exists in
CS1. The canonical CS1 checkout had pre-existing untracked
`sidecar/runs/104A_owner_repair/`; it was not touched. Both task worktrees
were created through `grace_work_farm.py`.

Commits and push status will be filled below after the atomic commits.

## Proposed student walk

Starting in the Week 4 module, a student opens the branching and
decision-making lesson, writes a decision table for the world, and chooses
representative plus exact-boundary tests. On Wednesday, they use that table
to implement the Week 4 Odyssey Gate before the Professional Minds
conversation. On Friday, they run the gate again with the boundary and an
edge/invalid case, then show the table, branching code, and downstream state
change. The resolved lesson and gate links are module-item links; no repo
path hunting is required.

## Next recommended prompt

Have Flo review and, if accepted, merge the two pushed branches. Then run a
source-only Week 4 readiness rebuild after the missing sibling PM/AI Week 4
folders are available; keep any Savnac review separate and explicitly dry-run
first.

ANNA CS1 W4 READY FOR REVIEW
