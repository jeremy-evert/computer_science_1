# Sidecar Report 102A — CS1 Online cross-list into 1415

**Date:** 2026-08-18
**Prompt:** `sidecar/prompts/102A_cs1_online_cross_list_into_1415.md`
**Scope:** One Canvas cross-list write. No content writes made.

## Verdict: GREEN

Section `76388` (`COMSC-1033-1414`, CS1 Online) is now cross-listed into
course `74029` (`COMSC-1033-1415`). Two doors, one classroom, verified by
independent read-back, not by trusting the write response.

---

## Pre-write re-check (immediately before write)

- Section `76388`: native to course `74033`, `nonxlist_course_id: None`. Unchanged from the 2026-08-17/18 chat audit.
- Course `74029`: `available`, `COMSC-1033-1415.2026FA`, native section `76384` (`nonxlist_course_id: None`).
- Course `74033`: `unpublished`, `COMSC-1033-1414.2026FA`, exactly one section (`76388`).
- Content counts recorded pre-write: `74029` = 5 modules / 7 pages / 13 assignments / 0 files / 0 discussion topics. `74033` = 6 / 9 / 17 / 5 / 0.

All preconditions matched the chat-recorded audit. Proceeded.

## The write

```
POST /api/v1/sections/76388/crosslist/74029
```

Exactly one API call. HTTP 200. Response confirmed `course_id: 74029`,
`nonxlist_course_id: 74033` on section `76388`.

## Read-back verification (independent re-fetch, not the write response)

1. `GET /courses/74029/sections` → two sections: native `76384`
   (`nonxlist_course_id: None`) and merged `76388`
   (`nonxlist_course_id: 74033`). **Matches expectation.**
2. `GET /courses/74033/sections` → **403 unauthorized** (see below —
   explained, not a defect).
3. `GET /courses/74029/enrollments?type[]=StudentEnrollment` → 41 total,
   split exactly 20 (`76384`) + 21 (`76388`). **Matches pre-write
   enrollment counts on both original courses exactly.**
4. `GET /courses/74033` → **403 unauthorized** (see below).
5. Content counts on `74029` after write: 5 modules / 7 pages / 13
   assignments / 0 files / 0 discussion topics — **identical to
   pre-write.** Zero content drift.

### The 403 on `74033`, explained

After the cross-list, `GET /courses/74033` and `GET
/courses/74033/sections` both return `403 unauthorized` for this token.
Investigated rather than dismissed:

`GET /courses/74029/enrollments?type[]=TeacherEnrollment` shows **two**
active TeacherEnrollments for Jeremy Paul Evert on `74029` post-write —
one on section `76384`, one on section `76388`. His instructor enrollment
was section-scoped (consistent with SIS-provisioned enrollments) and
followed section `76388` into `74029` exactly as the student enrollments
did. `74033` now has zero sections and zero enrollments of any kind for
this token, which is why the API (permission-checked via enrollment, not
account-admin — this token was never account-admin; an attempted
`/accounts/1/courses` call also 403s, confirming this is a standing
token-scope limitation, not a new one) returns 403 for a course the
token-holder is no longer enrolled in.

Canvas's cross-list endpoint moves section/enrollment relationships only;
it does not delete or modify course content. `74033`'s authored content
(6 modules / 9 pages / 17 assignments / 5 files, per the pre-write count)
was not the target of any write in this prompt and is understood to still
exist, but is **no longer independently re-verifiable via this API token**
following the enrollment move. This is a disclosed limitation, not a
known defect: if that leftover content ever needs to be inspected or
migrated directly (rather than recreated via a fresh Imprint push), it
will require Canvas admin-level access rather than this instructor
token.

---

## Content-change audit

No modules, pages, assignments, files, or discussion topics were
created, updated, or deleted on either course. `74029`'s content counts
are byte-for-byte identical before and after. `74033`'s content counts
could not be re-checked post-write (see above) but no write API call
ever targeted `74033`'s content — only the single section cross-list
call was made, targeting `74033`'s section, not its content.

## Final verdict: GREEN

- Two sections now live under one course (`74029`): the merge is real,
  proven by independent read-back, not the write receipt.
- Enrollment counts before/after reconcile exactly (20 + 21 = 41).
- Zero content drift on `74029`.
- The one open item (`74033` no longer independently inspectable via
  this token) is fully explained by expected Canvas cross-list/SIS
  enrollment behavior, not a sign of data loss, and is disclosed here
  rather than hidden.

## Stopping here

Per the prompt's scope boundary: not proceeding to Prompt 103. Prompt 103
needs amendment before it can run: retarget the production reconcile at
`74029` (not `74033`), and account for migrating/recreating `74033`'s
already-pushed Week 1/2 content into the now-shared `74029` shell. That
amendment is separate, deliberate follow-up work.
