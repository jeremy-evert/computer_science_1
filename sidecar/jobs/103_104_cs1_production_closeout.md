# Flo Job — CS1 Production Closeout (Prompts 103 → 104)

**Owner:** Chaz  
**Foreman:** Flo  
**Worksite:** `jeremy-evert/computer_science_1`  
**Shared implementation dependency allowed when necessary:** `jeremy-evert/course_foundry`  
**Production target:** SWOSU Canvas course `74029` only  
**Mode:** current-truth sync → topology gate → dry-run → bounded reconcile → Prompt 103 proof → Prompt 104 student-path proof → durable handoff

## Mission

Finish the Fall 2026 Computer Science 1 production closeout.

This is one job. Do not select work from JTT, do not take work from Computer Architecture, DSCT, CS2, Piper, or any neighboring campaign, and do not invent a broader orchestration system.

The human act of launching `./sidecar/launch_flo.sh` is explicit authority for the **bounded production content/configuration writes to Canvas course `74029` that are required by Prompts 103 and 104**, but only after the fresh topology gate below passes. It is **not** authority to change cross-list topology, touch another production course, delete unexplained instructor work, rewrite shared history, or widen scope.

Flo executes. Chaz evaluates afterward. Do not write Chaz's Owner after-action report.

## Read first

Read only the current truth needed for this job, beginning with:

1. `README.md`
2. `START_HERE.md`
3. `sidecar/reports/102A_cs1_online_cross_list_into_1415.md`
4. `sidecar/prompts/103_cs1_online_full_production_imprint.md`
5. `sidecar/prompts/104_cs1_online_student_view_launch_closeout.md`
6. `sidecar/reports/105_week2_lesson_entry_point.md`
7. current relevant `course_foundry` production-deploy implementation/report evidence, including `reports/106_production_deploy_skip_files.md` when still applicable.

The launcher separately points you at the canonical `foreman_interface` Owner/Foreman and Foreman/Worker contracts. Follow them. When dispatching bounded Wandas/workers, also read the current dispatch/golem spell material named by the launcher or contract. Do not make Jeremy relay commands or worker results.

## Known prior evidence: verify, do not trust blindly

Prior accepted evidence says:

- section `76388` / COMSC-1033-1414 was cross-listed into shared host course `74029`;
- native section `76384` / COMSC-1033-1415 also lives in `74029`;
- there were 41 students at the 102A verification point, split 20 + 21;
- Weeks 2–17 were later pushed to `74029`;
- all 16 newly created weekly modules were subsequently repaired to `published=true`;
- the Week 2 gate body/link was repaired;
- assignment-group weights were checked at 100%;
- drop-lowest rules previously failed to apply;
- Harbor's production file verification can falsely report file-content drift because its attachment downloader mishandles Canvas's external `*.canvas-user-content.com` redirect and may read zero bytes even when Canvas reports the correct nonzero file size;
- CS1 source has changed since earlier dry-run evidence, including the Week 1 reset message and categorical online-section invariant.

These are leads, not current proof.

## Hard boundary

### Allowed

- Read and safely sync current `computer_science_1` truth.
- Read and safely sync current `course_foundry` truth.
- Use an isolated Course Foundry worktree/branch when the shared checkout contains unrelated live/dirty state.
- Dispatch bounded Wandas/workers with isolated worktrees when useful.
- Read production Canvas course `74029`.
- After the topology gate passes, perform only the production mutations required to reconcile and verify CS1 under Prompts 103 and 104.
- Repair CS1 source or Course Foundry when evidence proves that is the correct owning layer.
- Commit and push accepted CS1/Course Foundry changes using the normal Git safety belt.
- Create durable CS1 reports/receipts.

### Forbidden

- Do not read from, write to, migrate from, or otherwise operate on Canvas course `74033`. Seeing `74033` as the `nonxlist_course_id` value returned on section `76388` under `74029` is expected and allowed.
- Do not alter cross-list/section topology.
- Do not touch any other production Canvas course.
- Do not modify JTT.
- Do not work on Computer Architecture, DSCT, CS2, Piper, or unrelated research.
- Do not reset, clean, stash, or overwrite unexplained shared-worktree dirt for convenience.
- Do not turn the known Harbor CDN verification defect into a side project. Read Harbor if useful. Mutate Harbor only if a bounded, evidenced repair is strictly necessary to make the CS1 acceptance claim truthful and no narrower direct-Canvas proof can do so.
- Do not write `sidecar/reports/103_104_chaz_owner_after_action.md`. Chaz owns that judgment.

## Execution

### 1. Sync and lock current source truth

Before judging production:

- identify current branch/remote/worktree state for CS1 and Course Foundry;
- fetch current remote truth;
- fast-forward safely when possible;
- preserve unexplained local work;
- if Course Foundry's shared checkout is dirty or occupied, create/use an isolated clean worktree instead of disturbing it;
- record exact CS1 and Course Foundry SHAs used for every production check.

Because CS1 has changed since earlier dry runs, rerun the current compiler/dry-run rather than assuming an earlier plan is still authoritative.

### 2. Fresh cross-list topology gate — before any production content write

Independently query production course `74029`.

Require:

- `GET /courses/74029/sections` shows exactly the intended two CS1 sections:
  - native `76384`;
  - merged `76388` with `nonxlist_course_id: 74033`;
- student enrollments on `74029` include students from both section ids;
- add/drop drift from the old 20 + 21 count is acceptable, but disappearance of either section population or a topology mismatch is not.

**If this topology is wrong or cannot be proved, STOP before production writes.**

Leave the evidence, write the Prompt 103 report with an honest `NOT DEPLOYED` verdict and the precise topology blocker, write the Flo completion report, and stop. Do not attempt to repair cross-list topology.

### 3. Snapshot and current production dry-run

If the topology gate passes:

- capture a pre-write production snapshot/read-back sufficient for Prompt 103;
- run the current CS1 production dry-run against course `74029`;
- classify every create/update/delete/skip or semantic difference;
- explicitly compare current Git/compiled truth to production rather than replaying stale counts.

No blind push. Know what the run intends to change.

### 4. Reconcile real drift at the correct layer

Resolve deterministic, student-relevant drift required by Prompt 103.

Pay particular attention to:

- assignment groups sum to 100%;
- drop-lowest rules are actually present where current policy requires them;
- points, grading type, submission types, dates, availability windows, and assignment-group placement;
- module order and `published` state;
- duplicate/zombie managed objects;
- Week 1, 2, 6, 9, 14, 15, 16, and 17 sentinel behavior;
- the current online-section invariant: an online student must never require physical presence, and any "in-class" requirement must have an asynchronous path;
- current source changes that landed after the previous production push.

For the known Harbor file-verification defect:

- distinguish **verification-tool failure** from **real Canvas/student file failure**;
- use direct Canvas metadata/read-back or another bounded direct check to establish whether required files actually exist, have nonzero expected size, and are reachable;
- do not churn/reupload valid production files merely because Harbor's downloader returned zero bytes;
- if Harbor prevents a truthful 103/104 conclusion and a small bounded fix is genuinely necessary, isolate that repair, test it, and return immediately to CS1.

### 5. Read back, repair, and prove idempotency

After any reconcile:

- independently read production back;
- rerun the semantic/dry-run comparison;
- require zero unintended creates, no duplicate explosions, no oscillating deterministic updates, and no unexplained grading/date/navigation drift;
- if full file equality is still polluted solely by the known Harbor CDN verifier defect, prove the real Canvas file state directly and disclose the verifier limitation rather than fabricating a clean result.

Continue authorized repair loops until Prompt 103 is truthfully `DEPLOYED` or a concrete real gate remains.

### 6. Write Prompt 103 report

Write exactly:

`sidecar/reports/103_cs1_online_full_production_imprint.md`

Follow Prompt 103's required report contract. Its verdict is only:

- `DEPLOYED`
- `NOT DEPLOYED`

Flo owns this Foreman execution verdict. Chaz will independently evaluate it later.

### 7. If and only if 103 = DEPLOYED, continue directly into Prompt 104

Do not wait for Jeremy.

Execute the intent of:

`sidecar/prompts/104_cs1_online_student_view_launch_closeout.md`

Walk the student path using test-student/student-view facilities where safe and available. Verify opening-minute usability, navigation, visibility, submissions, grading, due dates, links/files, sentinel weeks, duplicates/zombies, and the online asynchronous path.

Repair proven defects at the correct source/compiler/Canvas layer, rerun production reconcile/read-back when required, and re-walk affected student paths.

Write exactly:

`sidecar/reports/104_cs1_online_student_view_launch_closeout.md`

Use only Prompt 104's allowed verdicts:

- `READY FOR STUDENTS`
- `READY WITH NON-BLOCKING YELLOWS`
- `NOT READY`

If Prompt 103 is `NOT DEPLOYED`, do not execute 104.

## Receipts

Create a run directory under:

`sidecar/runs/103_104_flo_closeout/<UTC_TIMESTAMP>/`

Keep compact, useful raw/structured evidence there, including at minimum:

- source SHAs;
- topology read-back;
- pre-write snapshot pointer/receipt;
- first current dry-run;
- production mutation receipts if any;
- post-write read-back;
- idempotency/diff result;
- grading/drop-rule evidence;
- file-verification evidence;
- student-view evidence if 104 runs;
- worker/Wanda handoff evidence when used.

Do not dump secrets or tokens into receipts.

## Flo completion report

Before stopping, write:

`sidecar/reports/103_104_flo_foreman_completion.md`

It must be a thin handoff to Chaz containing:

- what Flo attempted;
- exact CS1 and Course Foundry SHAs used/promoted;
- topology-gate result;
- production mutations actually made;
- Prompt 103 verdict and report path;
- Prompt 104 verdict and report path, or `NOT RUN — 103 NOT DEPLOYED`;
- receipt directory;
- commits pushed;
- remaining yellows;
- exact human gate, if any;
- explicit statement that Flo is **not** making the final Owner closeout judgment.

## Real human gates

Return to Jeremy only for a true gate, reduced to the smallest action:

- cross-list topology is wrong and changing it would require a new production topology write;
- required credentials/privilege are unavailable;
- a destructive or production action outside the explicit `74029` content/configuration authority above is required;
- current source truth contains a real pedagogical/policy conflict that evidence cannot resolve;
- unexplained repository state cannot be isolated safely.

Routine worker dispatch, Git safety-belt operations, tests, direct production read-back, and the bounded `74029` reconcile authorized by this launch are not human gates.

## DONE means

Flo's job is complete when one of these is true:

### Successful closeout
- fresh topology proof passed;
- current Git was reconciled against production `74029`;
- Prompt 103 report exists with `DEPLOYED`;
- Prompt 104 ran and its report exists with a truthful launch verdict;
- receipts are durable;
- accepted source/shared-tool changes are committed and pushed;
- `sidecar/reports/103_104_flo_foreman_completion.md` points Chaz at the evidence.

### Safe blocked closeout
- a real stop condition above is proved;
- no unauthorized production write occurred;
- Prompt 103 truthfully says `NOT DEPLOYED` when applicable;
- Flo completion report and receipts identify the smallest exact gate.

Do **not** declare the CS1 campaign closed. That is Chaz's Owner decision after independent review.
