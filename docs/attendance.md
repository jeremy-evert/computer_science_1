# Attendance & participation (10% of course grade)

Authored 2026-08-06 (course_foundry prompt 026), per Jeremy's decision:
shrunk from 20% to 10% the same day (course_foundry prompt 038 follow-up)
to absorb the professional-pathway rows added by prompt 027 without
over-summing `grading-model.md`'s weight table -- see that file's "Open
decisions" for the full reconciliation record.
this is a gradebook-only Canvas object with no student-submitted artifact
-- attendance is not something a student uploads, it's recorded by the
instructor. This file is the minimal source doc `cs1_desired_course.py`
points at, matching how every other `grading-model.md` category has a
source file it renders from.

## What this represents

`docs/grading-model.md`'s "Attendance & participation" row, 10% of the
course grade, daily cadence. Policy language: `docs/syllabus.md`'s
"Attendance and participation" section -- attendance taken at the start of
class, in person or via approved Zoom arrangement, students expected to
log into Canvas regularly.

## Canvas mechanics

- One Canvas Assignment object, gradebook-only.
- `submission_types`: no-submission state (`["none"]`) -- correct, not a
  bug. No student-submitted artifact exists or should exist; the
  instructor enters a score directly, same as any other Canvas
  gradebook-only column.
- `grading_type`: `"points"`.
- `points_possible`: 10 (traces directly to the 10% weight, scaled by
  this project's 100-raw-point-per-100%-of-course-grade convention -- see
  `docs/grading-model.md`'s "Open decisions" note on assignment groups).
- Assignment group: "Attendance & Participation" (`group_weight: 10`).

## Explicitly out of scope here

No attendance-tracking mechanism (roll sheet, QR check-in, etc.) is
invented by this file or its Canvas object -- per Jeremy's 2026-08-06
decision, only the point allocation itself is in scope. How the instructor
actually determines each week's score remains `docs/syllabus.md`'s policy
prose, to be finalized separately.

**Re-confirmed 2026-08-08** (during prompt 043's full-semester CS1
pipe-integrity check, when this category's lack of a gradable artifact
surfaced as a disclosed skip): this stays instructor-entered by design,
not by oversight. Jeremy considered and explicitly declined to invent a
data-collection mechanism here without checking real Canvas capabilities
first (Canvas login/page-view analytics, a possible Attendance/Roll Call
LTI, video-watch metrics where Canvas Studio-hosted) -- a real, larger
follow-on idea, captured but not started:
`jeremy_task_tracking/plans/
2026-08-08_student_engagement_early_alert_system_proposed.md`. This
category's own point-threshold policy is separately still blocked on the
university-policy confirmation `docs/syllabus.md` already flags -- that
blocker doesn't go away even if the data-collection piece above gets
built.
