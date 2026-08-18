# Sidecar Prompt 102A - Cross-list CS1 Online (1414) into CS1 (1415)

**Status:** READY
**Scope:** Exactly one Canvas cross-list operation. No content writes.
**Owner:** Foreman
**Mode:** pre-write re-check -> single write -> read-back verification -> report -> stop before 103

## Mission

Supersedes Prompt 102's deployment topology per Jeremy's 2026-08-18 decision:
CS1 Online (section 1414) and CS1 face-to-face (section 1415) form one shared
Canvas learning community — one gradebook, one Discussions board, one Zoom
LTI context, so students in both sections see each other's shared work
(reasoning odysseys, paired reasoning reports) while private per-student
submissions (resume, unofficial transcript) remain private as Canvas already
guarantees regardless of section.

Read-only audit (2026-08-17/18, in chat, not yet a committed report) found:

- `74029` (COMSC-1033-1415, face-to-face): **available/published**, 20
  students, real student page-view/participation activity already present
  this week.
- `74033` (COMSC-1033-1414, online): **unpublished**, 21 students, no
  possible student activity yet (unpublished), already carries a partial
  standalone content push (Week 1 kickoff + partial Week 2).
- Historical precedent: the last 3 Fall CS1 section pairs were all
  cross-listed (never left as two independent shells), and the most
  recent year with this exact 1414/1415 pairing (2025FA) cross-listed
  1414 into 1415 (`69067` -> `69068`).

Decision: `74029` (1415) is the parent. Section 1414 (Canvas section id
`76388`, currently native to course `74033`) is cross-listed into `74029`.

## Preconditions (re-check immediately before write)

1. Re-fetch section `76388`: confirm it is still native to course `74033`
   (`nonxlist_course_id` is still `None`) and still named
   `COMSC-1033-1414`.
2. Re-fetch course `74029`: confirm it is still `available`, still the
   `COMSC-1033-1415` Fall 2026 course, still has its own native section
   (`76384`) with `nonxlist_course_id: None`.
3. Re-fetch course `74033`: confirm it is still `unpublished`, still the
   `COMSC-1033-1414` Fall 2026 course, still has exactly one section
   (`76388`).
4. If any of the above has changed since the chat-recorded audit, stop
   before writing and report the discrepancy.

## The write

Exactly one Canvas API call:

```
POST /api/v1/sections/76388/crosslist/74029
```

No other Canvas object is created, updated, or deleted by this prompt.
Do not touch modules, pages, assignments, files, discussion topics,
publish state, or enrollments beyond what the cross-list call itself
does.

## Read-back verification (required, not optional)

After the write, independently re-fetch (do not trust the write response
alone):

1. `GET /api/v1/courses/74029/sections` — expect exactly two sections:
   the native `76384` (`nonxlist_course_id: None`) and the newly merged
   `76388` (`nonxlist_course_id: 74033`).
2. `GET /api/v1/courses/74033/sections` — expect zero sections.
3. `GET /api/v1/courses/74029/enrollments?type[]=StudentEnrollment` —
   expect enrollment count to reflect both sections' students (roughly
   20 + 21, allowing for any real overlap/withdrawals).
4. `GET /api/v1/courses/74033` — confirm the course object itself still
   exists, is unchanged in name/workflow_state, and was not deleted.
   Its authored content (modules/pages/assignments) is expected to still
   sit there unused — that migration is explicitly out of scope for this
   prompt (it becomes part of the amended Prompt 103).
5. Confirm no modules/pages/assignments/files/discussion topics were
   created, updated, or deleted on either course as a side effect —
   counts before and after must match exactly except for the section/
   enrollment topology itself.

## Done when / stop condition

GREEN only when the read-back independently proves: `74029` now has two
sections including the merged `76388`, `74033` has zero sections, no
content was touched anywhere, and `74033` itself still exists untouched.

Stop here. Do not proceed to Prompt 103. Prompt 103 needs to be amended
to target `74029` (not `74033`) and to account for migrating `74033`'s
already-pushed Week 1/2 content into the new shared shell — that
amendment is separate, deliberate follow-up work, not part of this
prompt.

## Required report

`sidecar/reports/102A_cs1_online_cross_list_into_1415.md`: pre-write
re-check results, the exact write made, full read-back evidence, before/
after content-count comparison proving no content drift, and final GREEN/
RED verdict.
