# Course evaluation (2% of course grade)

Authored 2026-08-06 (course_foundry prompt 026), per Jeremy's decision:
this is a gradebook-only Canvas object with no student-submitted artifact
tracked by this pipeline -- the university's own course-evaluation
instrument (SWOSU's standard end-of-term evaluation, administered outside
this course's own Canvas objects) is what students actually complete;
this Canvas object exists only to hold that credit's point value in the
gradebook, matching how every other `grading-model.md` category has a
source file it renders from.

## What this represents

`docs/grading-model.md`'s "Course evaluation" row, 2% of the course grade,
end of term, "carried from current model" (`docs/syllabus.md`'s existing
"Course evaluation" line item, 2% under the prior 90/10/20/2 model).
Historically, completion credit for the university-administered
evaluation, not a CS1-authored assignment.

## Canvas mechanics

- One Canvas Assignment object, gradebook-only.
- `submission_types`: no-submission state (`["none"]`) -- correct, not a
  bug. The actual evaluation instrument lives outside this course's
  Canvas shell (SWOSU's evaluation system); this object only records
  completion credit.
- `grading_type`: `"points"`.
- `points_possible`: 2 (traces directly to the 2% weight, same
  100-raw-point convention as `docs/attendance.md`).
- Assignment group: "Course Evaluation" (`group_weight: 2`).

## Explicitly out of scope here

No evaluation-completion tracking mechanism (e.g. an API integration with
SWOSU's evaluation system) is invented by this file or its Canvas object
-- per Jeremy's 2026-08-06 decision, only the point allocation itself is
in scope.

**Re-confirmed 2026-08-08** (same discussion as `docs/attendance.md`'s
matching note): stays instructor-entered by design. SWOSU's actual
evaluation platform (likely Watermark, CoursEval, or similar -- not
native Canvas) may expose a completion-roster API gated at a minimum-
respondent anonymity threshold; confirming this requires checking
directly with SWOSU IT/registrar, not something this codebase can
determine on its own. Captured as part of the same follow-on idea:
`jeremy_task_tracking/plans/
2026-08-08_student_engagement_early_alert_system_proposed.md`.
