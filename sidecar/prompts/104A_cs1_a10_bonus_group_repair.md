# Sidecar Prompt 104A — Repair A10 bonus assignment group placement

**Status:** READY  
**Owner:** Chaz  
**Foreman:** Flo  
**Scope:** One grading-contract defect in production CS1 course `74029`  
**Mode:** prove source intent -> fix routing at source -> focused tests -> one-object production repair -> read back -> report -> stop

## Why this prompt exists

Owner acceptance of Prompts 103/104 found one blocker Flo had classified as a yellow.

Production currently places:

`A10 (Optional / Bonus) — Success Foundations Reflection`

as a normal 10-point assignment inside the weighted `Semester kickoff week` group (5%), with `omit_from_final_grade: false`.

Current authoritative source at:

`semester_kickoff_week/assignments/A10_success_foundations_reflection.md`

states explicitly that A10 is optional bonus work and that its 10 points belong in Canvas's default, 0%-weighted assignment group rather than a weighted category.

This is not a pedagogy decision. Source intent is already explicit. Repair the source/compiler routing and the one live assignment, then prove the rest of the gradebook did not move.

## Hard boundaries

- Production target is **only Canvas course `74029`**.
- Do not touch cross-list topology.
- Do not read/write orphan course `74033`.
- Do not touch Computer Architecture, DSCT, CS2, Piper, JTT, or Luna's Course Foundry containment work.
- Do not reopen the full 103/104 semester campaign.
- Do not change A10's title, body, rubric, points possible, submission type, due date, availability, published state, or student-facing instructions unless a separate proven defect is discovered and documented. This prompt is about assignment-group routing.
- Do not change any assignment-group weight.
- Do not change any other assignment's group placement.
- Do not delete historical evidence.
- Use an isolated Course Foundry worktree/branch. Do not develop from the dirty shared checkout.

## 1. Prove the mismatch fresh

Before any write:

1. Read the current A10 source and quote/record the sentence establishing:
   - optional/bonus;
   - default 0%-weighted assignment-group placement.
2. Read live production course `74029` and identify A10 by exact title.
3. Record:
   - Canvas assignment id;
   - current assignment-group id/name/weight;
   - points possible;
   - submission types;
   - omit-from-final-grade state;
   - due/availability/publish fields.
4. Resolve the live default `Assignments` group and prove its weight is `0.0`.
5. Snapshot current total group weights and the seven drop-lowest rules.

If source no longer says A10 belongs in the 0%-weighted default group, stop and report `NOT REPAIRED` rather than guessing.

## 2. Fix future routing at the source/compiler layer

Current kickoff routing must not send every kickoff assignment into one weighted group when A10 is explicitly an exception.

Implement the smallest clear mechanism that preserves existing behavior for required kickoff assignments while allowing A10 to remain in/default to the 0%-weighted `Assignments` group.

Acceptance properties:

- A01–A09 and the intended graded kickoff exit tickets retain their existing `Semester kickoff week` group placement.
- A10 is explicitly excluded from that weighted-group routing and resolves to the default 0%-weighted group.
- The mechanism is understandable from source truth, not a title substring hack hidden in live-write code if a semantic/source field is practical.
- Existing callers remain backward-compatible.
- No Architecture/DSCT/other-course contract is changed underneath active work.

Do not port/rewrite the whole kickoff reconciler. This is a one-exception routing fix.

## 3. Add focused regression tests

At minimum prove:

- A10's desired routing is the default/0%-weighted path;
- a representative required kickoff assignment remains routed to `Semester kickoff week`;
- no group weight changes are introduced;
- existing kickoff/content-map/load-adapter focused tests remain green.

Run only the relevant test surface plus any directly affected deployment tests. Do not turn unrelated pre-existing full-suite failures into this prompt's project.

## 4. Promote the source fix safely

Rebase/merge against current `course_foundry` main without overwriting concurrent work.

Record the exact final Course Foundry commit used for production repair.

If current main has advanced through Luna containment or Piper-related deterministic deployment work, preserve it and adapt cleanly. Do not enter their project scope.

## 5. Repair only A10 in production

Because CS1 Week 1 currently lacks a standing production-safe kickoff reconcile tool, a single scoped Canvas assignment update is authorized for this prompt **only after the source/compiler fix is merged and tests pass**.

Update only A10's `assignment_group_id` in course `74029` to the live default `Assignments` group id.

Do not alter any other assignment field.

Before sending the write, capture the outbound body. After the write, independently read A10 back.

## 6. Focused post-repair acceptance

Prove all of the following:

- A10 now belongs to `Assignments` with group weight `0.0`;
- A10 remains 10 points and retains its original submission/body/rubric/date/publish behavior;
- A10 is absent from `Semester kickoff week`;
- the `Semester kickoff week` group remains weight `5.0`;
- total assignment-group weights remain exactly `100%`;
- all seven intended `drop_lowest: 1` rules remain present;
- no other assignment changed group as part of this repair;
- topology remains section `76384` + merged `76388` under `74029`;
- no write touched `74033` or another course.

A full Prompt 104 re-walk is unnecessary. Preserve Flo's previously accepted evidence and rerun only the affected gradebook/readback checks.

## Required receipts

Use a new durable receipt directory under:

`sidecar/runs/104A_a10_bonus_group_repair/<UTC_TIMESTAMP>/`

Include:

- source SHA(s);
- pre-write A10 JSON/readback;
- assignment-group snapshot;
- focused test output;
- exact write body/receipt;
- post-write A10 readback;
- post-write group/drop-rule verification;
- topology readback.

Do not record secrets/tokens.

## Required report

Create:

`sidecar/reports/104A_cs1_a10_bonus_group_repair.md`

Use one of exactly these verdicts:

- `REPAIRED`
- `NOT REPAIRED`

The report must state the exact live A10 assignment id, old group, new group, Course Foundry repair commit, tests run, production write performed, post-write verification, and any remaining blocker.

## Done when

This prompt is complete when A10's live and future compiled group placement matches source truth, the rest of the grading model is proved unchanged, receipts/report are committed and pushed, and control returns to Chaz for final Owner acceptance.

Do not continue into another CS1 improvement after this repair.
