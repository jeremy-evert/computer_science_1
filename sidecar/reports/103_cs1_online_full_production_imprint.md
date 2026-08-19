# Sidecar Report 103 — CS1 online full production imprint

**Date:** 2026-08-18/19
**Prompt:** `sidecar/prompts/103_cs1_online_full_production_imprint.md`
**Foreman:** Flo
**Production target:** SWOSU Canvas course `74029`, `COMSC-1033-1415.2026FA`
(shared host for native section `76384` and merged section `76388`,
`nonxlist_course_id: 74033`)
**Receipts:** `sidecar/runs/103_104_flo_closeout/20260819T031550Z/`

## Verdict: DEPLOYED

---

## 1. Source SHAs used

- `computer_science_1`: `a27e791666032b6a4cf0b14da3573e49bd8130e1` (branch
  `main`, clean, up to date with `origin/main`).
- `course_foundry`: `a49b658f3a230ad74787757cb0ed66ba24d1c7e5` (`origin/main`
  tip at fetch time). The shared `course_foundry` checkout was dirty with
  unrelated in-flight work (submission-listener state, DSCT/other-course
  experiment reports), so an isolated worktree
  (`course_foundry.worktrees/flo-103-104-cs1-closeout`, branch
  `flo/103-104-cs1-closeout`) was created from `origin/main` rather than
  disturbing it. No changes were made to the shared checkout.
- Prompt 105's Week 2 link-token fix (`c99314d`/`22b895a`) and Prompt
  106/107's `--skip-files` flag and DSCT support (`f61f176`/`4b7bd03`) were
  already merged to `course_foundry` `main` before this run — confirmed by
  `git merge-base --is-ancestor`.

## 2. Fresh topology gate (before any write)

Independently queried, not trusted from 102A's report:

- `GET /courses/74029/sections` → exactly two sections: native `76384`
  (`nonxlist_course_id: null`) and merged `76388`
  (`nonxlist_course_id: 74033`). **Matches required topology.**
- `GET /courses/74029/enrollments?type[]=StudentEnrollment` → 39 students
  total, split 20 (`76384`) + 19 (`76388`). Down from 102A's 41 (20 + 21) —
  two fewer on the merged section, ordinary add/drop drift. Neither
  section's population disappeared. **Gate passed.** Receipts:
  `01_sections_74029.json`, `02_student_enrollments_74029.json`.

## 3. Pre-write snapshot and dry-run

- Pre-write content snapshot captured before any write:
  `05_assignment_groups.json` (15 groups, 100% weight),
  `06_modules_with_items.json` (21 modules, all published), and
  `07_assignments_p1.json` (100 assignments returned on page 1).
- First dry-run (`03_dry_run_first.txt`): 324 objects / 16 CS1-managed
  modules / 14 grading groups; `create=0, update=32, skip=306, delete=0`.
- Detailed per-object log (`03b_dry_run_detail.json`) showed the 32
  "updates" were **all** `kind="file"` entries with reason `"content
  changed"` — every Wednesday/Friday Professional Minds deck and the
  Week 2 Monday/Monday-PM decks across weeks 2–16, plus 16 module-metadata
  "refreshed unconditionally" entries (not counted in the tally; Imprint
  always PUTs module metadata since there is no cheap pre-write diff for
  it, per `imprint/reconcile.py`'s documented discipline — this is expected
  noise, not drift).

## 4. Harbor file-verification defect — confirmed tool failure, not real drift

The known defect from prior evidence: `harbor.api.download_attachment`
rewrites the redirect `Location` from Canvas's real production file host
(a `*.canvas-user-content.com` CDN) back onto the configured
`swosu.instructure.com` host while sending the CDN hostname as an explicit
`Host` header — a fix that is correct for Savnac's internal Docker
redirect quirk but wrong for real Canvas's external CDN redirect, and can
silently return content that does not hash-match the real file.

Independently verified this is exactly what happened, rather than
assuming it: wrote a bypass script
(`/tmp/.../scratchpad/verify_files.py`, not committed anywhere) that reads
each flagged file's live Canvas metadata and downloads its bytes with a
plain `requests.get(..., allow_redirects=True)` — no host rewrite — then
SHA-256-hashes the result against the local source PDF.

Result (`04_file_verify_direct.json`): **32/32 files hash-matched exactly.**
Every flagged file is byte-identical to source on production Canvas
already. This is Harbor's downloader misbehaving against real Canvas, not
a real content mismatch.

Consequence: did **not** reupload/delete-and-recreate 32 already-correct
production files. Pushed with `--skip-files` per the prompt's explicit
guidance ("do not churn/reupload valid production files merely because
Harbor's downloader returned zero bytes").

## 5. Production push

```
python -m course_foundry.production_deploy push --course cs1 \
  --git-parent /mnt/brandy_nvme/jevert/git --skip-files --confirm-live
```

Result (`08_push_run.txt`): `create=0, update=0, skip=306, delete=0`.
Assignment-group self-check: **100% across 15 groups.**

No file, page, assignment, or module was created, updated, or deleted by
this push. The course was already correctly reconciled; this run's only
effect was proving that fact against live Canvas rather than trusting the
first (file-verification-polluted) dry-run's raw update count.

## 6. Grading-contract read-back

Independently read `74029`'s live assignment groups
(`05_assignment_groups.json` pre-write, `11_post_write_assignment_groups.json`
post-write — identical):

- 15 assignment groups, weights sum to exactly **100%**.
- Drop-lowest (`drop_lowest: 1`) present on: Monday Moment quiz, Wacky
  Wednesday reflection, Fun Friday reflection, Paired-programming report,
  Friday feedback report, Show-and-Tell reflection, Weekly reinforcement
  assignment — matching the finalized grading model.
- The default `Assignments` group carries weight `0.0` and holds exactly
  the 7 intentionally `not_graded` Week 16/17 objects (Farkle/ML
  experiment receipt, Week 16 Wed/Fri reading+slides, Week 16 Monday
  Moment reflect-and-improve, `week-17`) — all confirmed
  `grading_type=not_graded`, `submission_types=["not_graded"]`. This is
  the intended dead-days-safe Week 16 design, not a graded zombie.
- Coding Odyssey checkpoints (15%) and Final reflection paper (8%) present
  as separate ungrouped-drop categories per the finalized model.

## 7. Date audit

Scanned all 100 assignments returned (`07_assignments_p1.json`):

- no due date before course start (2026-08-17);
- no non-2026 or stale 2025 due dates;
- no assignment where `lock_at` precedes `due_at` (which would hide a
  still-due assignment).

## 8. Sentinel-week and module read-back

`06_modules_with_items.json` (21 modules total, all `published: true`, in
chronological position order 1–21, zero unpublished child items):

- Weeks 1 (kickoff, 3 modules: Monday/Wednesday/Friday) through 17
  present, correctly ordered.
- Week 1 is composed from the shared kickoff path: module names "Monday:
  Survive This Semester", "Wednesday: Thrive In Your Degree", "Friday:
  Entering Your Career" match the shared `semester_kickoff_week`
  Survive-the-Semester/Survive-the-Degree/Enjoy-the-Career design, not a
  stale inline `week-01.md` interpretation.
- Week 2 carries 28 items including the four decks verified in §4 and the
  Odyssey Gate (Prompt 105's token-resolved link wired through
  `production_deploy.py` as of the merged 105 tiny-fix).
- Week 6/9 present as checkpoint weeks; Week 14 (Communication /
  professional-pathway), Week 15 (Modern AI, fully async per
  `planning/week-15.md`), Week 16 (Farkle/ML, dead-days-safe per §6), and
  Week 17 (Finals) all present with no missing structure.
- Duplicate/zombie sweep across every module item title
  (`06_modules_with_items.json`): **zero duplicate titles**; zero hits for
  `checkpoint 4`, `chapter exam`, `zybooks`, `deitel`, `savnac`,
  `192.168.`, `TODO`, or `placeholder`.

## 9. Online-section invariant

`planning/week-01.md` (current source, this SHA) states the invariant
explicitly: "students enrolled in an online section are never required to
attend a face-to-face class meeting... Any activity described as
'in-class' must have an asynchronous path for online students." Checked
this against `docs/grading-model.md`'s attendance policy, which credits
attendance for being "present and engaged (in person **or via the
approved Zoom arrangement**)" — the async path exists. No source text
found requiring in-person-only presence anywhere in `planning/`,
`assignments/`, or `docs/`.

## 10. Idempotency proof (second run)

Re-ran the identical dry-run against the same desired state after the
push:

```
python -m course_foundry.production_deploy dry-run --course cs1 \
  --git-parent /mnt/brandy_nvme/jevert/git --skip-files
```

Result (`12_idempotency_dry_run_second.txt`): `create=0, update=0,
skip=306, delete=0` — identical shape to the push result itself. Zero
oscillating updates, zero unintended creates, zero duplicate explosions.

## 11. Post-write read-back

Independently re-fetched (not trusting the push's own success claim):

- `09_post_write_sections.json`: same two sections, same
  `nonxlist_course_id` relationship.
- `10_post_write_student_enrollments.json`: same 20 + 19 = 39 split.
- `11_post_write_assignment_groups.json`: same 100% weight total.

## Remaining yellows

- The 32 file objects still show as Harbor-downloader false positives on
  any future dry-run against real production Canvas until Harbor's
  redirect-rewrite logic is fixed for the external CDN case (it currently
  only handles Savnac's internal Docker redirect correctly). This run
  worked around it with `--skip-files` plus an independent direct-bytes
  verification rather than fixing Harbor itself, per the prompt's
  instruction not to turn this into a side project unless a bounded fix is
  strictly necessary — it was not necessary here, since a narrower direct
  verification fully established the truth. Future CS1 production runs
  should either repeat the same bypass check or fix
  `harbor.api.download_attachment`'s redirect handling for
  non-Savnac hosts.
- `74033` remains an orphaned, un-migrated shell per the Prompt 103
  amendment; untouched by this run, as required.

## Scope discipline

No read or write ever targeted course `74033`. No cross-list/topology
write was made (102A's cross-list is unchanged, re-verified pre- and
post-write). No other production course was touched. The shared
`course_foundry` checkout's pre-existing dirt (submission-listener state,
other-course experiment reports/worktrees) was left untouched; all work
happened in an isolated worktree.
