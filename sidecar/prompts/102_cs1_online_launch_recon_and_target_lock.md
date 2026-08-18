# Sidecar Prompt 102 - Lock the real Fall 2026 CS1 Online target and prove launch readiness

**Status:** READY  
**Scope:** Fall 2026 Computer Science I Online launch reconnaissance and target lock  
**Owner:** Foreman  
**Mode:** sync -> inspect -> identify exact target -> dry run -> compare against proven Savnac state -> repair shared compiler defects if needed -> report -> continue when green

## Mission

Tonight's priority is to **fully deploy Computer Science I Online**.

Do not redesign the course. Do not start another curriculum project. The source work is substantially mature and the job now is to get the intended Fall 2026 course into the correct Canvas shell safely, completely, and verifiably.

This prompt exists to establish a trustworthy launch state before Prompt 103 performs the production imprint.

The governing rule is:

> Git is authoritative. Savnac is evidence. The real Fall 2026 online Canvas shell is the destination only after its identity is proved.

Do not ask Jeremy to copy/paste routine information that can be discovered from the repos, environment, Canvas API, or existing run evidence. Escalate only if two live Canvas courses remain genuinely indistinguishable after using course name, code, section, term, enrollment role, dates, and prior course metadata.

---

## Read first

In `computer_science_1`, read at minimum:

- `START_HERE.md`
- `README.md`
- `course_metadata.yaml`
- `docs/syllabus.md`
- `docs/grading-model.md`
- `docs/canvas-module-checklist.md`
- `docs/savnac-canvas-access.md`
- `planning/block-map.md`
- `planning/week-01.md`
- `planning/week-02.md`
- `planning/week-15.md`
- `planning/week-16.md`
- `planning/week-17-finals.md`
- `reports/012_pre_savnac_source_reconciliation.md`
- `reports/014_cs1_grading_and_pre_savnac_closeout.md`
- `sidecar/reports/100_harden_week16_farkle_ml_evidence.md`
- `sidecar/reports/101_cs1_shared_farkle_migration.md`

Then inspect the sibling repos that actually implement deployment:

- `course_foundry`
- `harbor`
- `semester_kickoff_week`
- `professional_minds`
- `ai_fluency`

Read their active CS1 adapters/compiler/imprint paths and the most recent CS1 Savnac run evidence before changing anything.

Do not assume July/August documentation is perfectly current. Source code and current run artifacts win.

---

# 1. Sync and establish repository state

Before execution:

1. Record branch and HEAD SHA for every repo used.
2. Fetch/pull safely where appropriate.
3. Refuse to overwrite unrelated dirty local work.
4. If local dirty work is relevant and intentional, preserve it and report it rather than discarding it.
5. Confirm the CS1 source repo is the intended current mainline and not a stale worktree.

Write the starting SHA table into the report.

---

# 2. Reconstruct the known-good Savnac reference state

Savnac course `1`, `Computer Science I (Savnac test)`, has been the proving ground. Use it as a reference surface, not as a substitute for source-of-truth Git.

Establish what the last successful full-semester CS1 Savnac imprint proved, including as available:

- shared Week 1 ownership through `semester_kickoff_week`;
- Weeks 2-17 generated from the active CS1 desired-course compiler;
- assignment groups and weights;
- drop-lowest rules if currently implemented;
- due dates;
- Week 15 async behavior;
- Week 16 dead-days/no-new-graded-work behavior;
- Week 17 reflection/finals behavior;
- idempotency/read-back status;
- files or content types that previously could not be uploaded.

If Savnac is stale relative to Git, note the delta. Do not force Git backward to match Savnac.

---

# 3. Discover and lock the exact production Canvas target

Use Harbor/Canvas API read-only discovery against the real SWOSU Canvas environment.

Find the Fall 2026 **Computer Science I Online** shell by evidence, not guesswork.

For every plausible candidate record:

- Canvas course id;
- course name;
- course code;
- section name/id where available;
- term;
- start/end dates;
- workflow state/published state;
- Jeremy's enrollment/teacher role;
- current object counts (modules/pages/assignments/files/assignment groups) if available.

Reject:

- Savnac course id `1` as the production target;
- Harbor sandbox course `24298`;
- prior-semester CS1 shells;
- face-to-face CS1;
- any course whose section/term evidence does not match the Fall 2026 online section.

Create a **target lock record** in the report with the exact Canvas course id and the evidence that makes it the correct target.

If more than one candidate remains materially plausible after full API inspection, stop before writes and report the ambiguity precisely. This is the only expected human-gate condition in this prompt.

---

# 4. Compile the current desired course with zero production writes

Run the actual Course Foundry dry-run/desired-course path against the current CS1 repo and all sibling content sources.

Do not use an old static export if the compiler can build live state.

Record:

- module count;
- object count by kind;
- assignment groups and weights;
- due-date range;
- Week 1 ownership/result;
- sentinel-week details for Weeks 2, 6, 9, 14, 15, 16, and 17;
- active/optional/retired Odyssey-gate semantics;
- external-link/file objects;
- any compiler warnings or skipped objects.

The previously documented 2026-08-12 dry run was 16 modules / 327 objects, but **do not treat that number as a magic acceptance value**. Current source may legitimately differ. Explain every material delta.

---

# 5. Compare desired state to the locked production target read-only

Build a semantic diff between desired Git-compiled state and the current real Canvas shell.

At minimum classify:

- missing modules;
- missing pages;
- missing assignments;
- stale/obsolete objects;
- mismatched assignment groups/weights;
- mismatched drop rules;
- wrong/missing due dates;
- wrong publish state;
- missing Week 1 shared kickoff objects;
- duplicate objects;
- dangling module items;
- broken internal links;
- missing files/assets;
- objects present in Canvas but not represented by Git.

Do not delete production objects merely because they are unexpected. Classify first. Prompt 103 may update/delete only when the intended behavior is unambiguous and the operation is supported by the existing imprint contract.

---

# 6. Repair launch-blocking compiler defects now

If the current desired-course compiler cannot faithfully represent the already-decided course, repair the smallest correct shared defect in `course_foundry`/`harbor` before proceeding.

Examples of legitimate launch blockers:

- missing drop-lowest imprint support for a finalized grading rule;
- file upload support required by already-decided student materials;
- shared Week 1 composition broken;
- idempotency bug;
- assignment-group mismatch;
- due-date or timezone bug;
- page/assignment body corruption;
- module ordering bug;
- internal-link compilation failure.

Do not use this as permission to redesign CS1 or refactor unrelated infrastructure.

For any shared infrastructure repair:

1. add/adjust tests;
2. run the relevant suite;
3. commit intentionally with a clear message;
4. rerun CS1 dry run;
5. refresh the production semantic diff.

---

# 7. Launch gate

Prompt 102 is GREEN only when all of these are true:

- exact real Fall 2026 CS1 Online Canvas course is locked by evidence;
- current desired state compiles cleanly;
- no unresolved source-of-truth contradiction exists;
- shared Week 1 is represented correctly;
- grading groups sum to 100%;
- finalized drop-lowest behavior is representable or an explicit documented exception is justified;
- sentinel weeks behave correctly;
- production diff is understood;
- no unrelated destructive action is required;
- Prompt 103 can perform a bounded reconcile against one exact course id.

If GREEN, continue directly to Prompt 103 without asking Jeremy for routine approval. His instruction for this run is to fully deploy CS1 Online.

If RED, stop only for a concrete ambiguity or risk that cannot be resolved from available evidence.

---

# Required report

Create:

`sidecar/reports/102_cs1_online_launch_recon_and_target_lock.md`

Include:

- repo/branch/SHA table;
- exact production target lock and evidence;
- Savnac reference summary;
- current dry-run counts;
- desired-vs-production semantic diff summary;
- launch-blocking defects found and repairs made;
- tests run/results;
- commits created;
- final GREEN/RED verdict;
- if RED, the one precise reason human intervention is required.

---

# Done when

The production destination is no longer a guess and the Foreman can say:

> I know exactly which Fall 2026 online shell is ours, I know exactly what Git says should be there, I know the current delta, and the deployment machinery is ready to reconcile it.
