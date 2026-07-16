# Report 004 — Canvas Follow-up Pull

**Date:** 2026-07-15 (local) · **Captured:** 2026-07-16 UTC

## Result

The authorized read-only follow-up pull completed for all 12 confirmed COMSC
1033 course shells. Fresh timestamped snapshots were added under each
semester's `archive/` directory. The July 14 snapshots were left untouched.

The pull requested the missing historical pieces:

- announcements through `/api/v1/announcements` scoped to each course;
- quiz questions through each quiz's `/questions` endpoint;
- module items through the modules endpoint with `include[]=items`;
- current file manifests and downloadable non-video files.

The tool does not request submissions, quiz submissions, grades, users,
enrollments, or discussion replies.

## What came back

| Historical shell | Announcements | Quiz questions | Module items | Files | Video files skipped |
|---|---:|---:|---:|---:|---:|
| Fall 2021 | 0 | 0 | 0 | 2 | 2 |
| Fall 2022 | 0 | 14 | 0 | 6 | 6 |
| Fall 2023 | 0 | 0 | 25 | 3 | 0 |
| Fall 2024 | 0 | 0 | 0 | 2 | 0 |
| Fall 2025 | 0 | 0 | 0 | 6 | 0 |
| Spring 2021, course 43003 | 0 | 0 | 24 | 3 | 1 |
| Spring 2021, course 43004 | 0 | 0 | 25 | 3 | 1 |
| Spring 2022 | 0 | 14 | 0 | 1 | 1 |
| Spring 2023 | 0 | 0 | 0 | 2 | 0 |
| Spring 2024 | 0 | 0 | 0 | 2 | 0 |
| Spring 2025 | 0 | 0 | 0 | 4 | 0 |
| Spring 2026 | 0 | 0 | 11 | 4 | 0 |

The zero announcement count is now an observed Canvas API result from the
dedicated announcements endpoint, not merely an omission in the first pull.
Likewise, the Spring 2021 quiz records returned no question objects despite
having quiz metadata; the Fall 2022 and Spring 2022 quizzes returned 7
questions each.

The pull also recovered a previously absent ordinary file (`duran cs1.pdf`)
from Fall 2023. Video files were intentionally retained in the manifest but
not downloaded by the tool's safety threshold.

## Provenance

Fresh manifests are named `canvas-<course-id>-snapshot-20260716-*.json`.
They are raw Canvas reference material and should not be edited by hand; new
course design decisions belong in the authored curriculum files under this
repo.
