# Sidecar Prompt 103 - Fully imprint Computer Science I Online into production Canvas

**Status:** READY AFTER 102 GREEN  
**Scope:** One exact Fall 2026 Computer Science I Online production Canvas course  
**Owner:** Foreman  
**Mode:** verify target lock -> snapshot -> reconcile -> read back -> repair -> rerun -> report

## Mission

Prompt 102 proved the exact production Canvas target and the desired Git-compiled state.

Now **fully deploy Computer Science I Online** into that exact Fall 2026 shell.

This is not a migration experiment. It is a production reconcile. The desired state comes from Git and the active Course Foundry compiler; Canvas is the deployed representation.

The governing rule is:

> Make the locked course match the intended course, then prove that it matches.

Do not touch any other Canvas course.

---

# Preconditions

Before any write:

1. Read `sidecar/reports/102_cs1_online_launch_recon_and_target_lock.md`.
2. Require a GREEN verdict.
3. Extract the exact locked production Canvas course id from that report.
4. Re-query that course read-only and verify its identity again immediately before write.
5. Confirm the current repository/compiler SHAs still match the state Prompt 102 validated, or rerun the relevant dry run/diff if they changed.
6. Create a pre-write Canvas snapshot/read-back artifact sufficient to reconstruct what existed before this run.

If the course identity no longer matches the target-lock evidence, stop before writes.

---

# 1. Reconcile the complete course

Use the existing Harbor/Course Foundry/Imprint path. Improve shared infrastructure only when required to express an already-decided CS1 behavior.

Reconcile all intended content, including:

- shared Week 1 kickoff composition from `semester_kickoff_week`;
- Weeks 2-17 CS1 modules and module ordering;
- lesson/pages;
- Monday Moment content;
- Professional Minds / Wednesday / Friday content used by CS1;
- AI Fluency content used by CS1;
- Coding Odyssey gates/checkpoints;
- assignment bodies;
- rubrics where the current architecture represents them;
- files/assets/decks that the desired course contract includes;
- assignment groups;
- assignment-group weights;
- finalized drop-lowest rules;
- grading type and points possible;
- due dates and availability dates;
- submission types;
- publish/unpublish state according to the intended launch model;
- gradebook-only objects such as attendance/course evaluation where already decided;
- Week 14 professional-pathway update;
- Week 15 fully asynchronous structure;
- Week 16 dead-days-safe Farkle/ML payoff week;
- Week 17 reflection/finals structure.

Do not resurrect retired chapter exams, retired Week 16 Odyssey Checkpoint 4, required ZyBooks, required Deitel, or any other superseded historical content.

---

# 2. Preserve identity and avoid duplicate-object explosions

The reconcile must be idempotent by stable semantic identity.

Do not create a second copy of an object merely because its existing Canvas body differs.

For every intended object, prefer:

1. match the existing managed object;
2. update it in place when needed;
3. create only when genuinely absent.

For unexpected Canvas-only objects:

- do not delete blindly;
- classify whether they are obsolete managed artifacts, legitimate instructor additions, or unknown;
- delete/retire only when source ownership and replacement are clear;
- otherwise preserve and report them as yellow.

A production course with duplicate weekly pages/assignments is not a successful deployment.

---

# 3. Week 1 must be composed, not copied from stale inline content

Week 1 is shared kickoff infrastructure.

Verify that the deployed Week 1 comes from the active `semester_kickoff_week` composition path and that CS1-specific wrapping/navigation is correct.

Do not silently fall back to an old inline `planning/week-01.md` interpretation if the current compiler contract says otherwise.

---

# 4. Grading contract must be exact

Read the current `docs/grading-model.md` and active compiler constants rather than copying numbers from this prompt.

As a known reference, the finalized model documented 2026-08-12 included these categories totaling 100%:

- Monday Moment quiz;
- Wacky Wednesday reflection;
- Fun Friday reflection;
- Paired-programming report (A3);
- Friday feedback report (A7);
- Show-and-Tell reflection (A4);
- Weekly reinforcement assignment;
- Coding Odyssey checkpoints;
- Final reflection paper (A5);
- Professional pathway Week 14 update;
- Professional pathway Week 15 submission;
- Attendance & participation;
- Course evaluation.

Current Git wins if later intentional changes exist.

Verify in the real Canvas gradebook:

- assignment groups sum to 100%;
- points/weights align with the active model;
- drop-lowest rules are actually present on the intended groups;
- bonus practice is represented as intended without distorting base points;
- attendance and course-evaluation objects land in the correct groups;
- checkpoint weeks are correct;
- no Week 16 graded weekly-category zombie survives the dead-days rule.

---

# 5. Due dates, time zones, and launch chronology

Run a full date audit against the Fall 2026 calendar and current course metadata.

Check:

- no due date accidentally lands before course start;
- weekly Monday/Wednesday/Friday cadence is coherent;
- Week 15 is fully asynchronous as intended;
- Week 16 complies with dead-days policy;
- Week 17/finals reflection timing is coherent;
- Canvas stores/displays times in the expected timezone;
- no stale 2025/Spring 2026 dates survived;
- no hidden `available_from`/`lock_at` fields make published assignments inaccessible.

Repair deterministic date defects during this prompt.

---

# 6. Navigation and student path

A course can be technically populated and still be unusable.

Read back the module graph and verify the student path:

- course landing/start-here entry is obvious;
- Week 1 flows into Week 2;
- modules are ordered chronologically;
- module items point to the intended objects;
- no dangling or duplicated module items;
- internal Canvas links resolve to this course, not Savnac or an old course id;
- external links use intended current destinations;
- students are not routed to GitHub source files when a Canvas-native page/assignment is expected;
- unavailable instructor-only artifacts are not exposed as student requirements.

Repair broken navigation now.

---

# 7. Production read-back after imprint

After the first reconcile, do not trust the write receipt alone.

Read the course back from Canvas and compare it again to the desired state.

Produce machine-readable or structured evidence for:

- modules and ordering;
- pages;
- assignments;
- files;
- assignment groups/weights/drop rules;
- due dates;
- publish state;
- submission types;
- module-item links.

If the semantic diff is non-empty for deterministic managed fields, repair and rerun until clean or until a concrete platform limitation is proved.

---

# 8. Idempotency proof

Run the same production reconcile again against the same desired state.

Acceptance target:

- zero unintended creates;
- zero duplicate objects;
- zero oscillating updates;
- stable semantic diff;
- only genuinely unavoidable/noisy API fields excluded from equality.

If a second run updates the same objects again without a source change, treat that as an imprint bug and fix it before declaring success.

---

# 9. Scope boundaries

Do not:

- touch CS1 face-to-face;
- touch Computer Architecture;
- touch Discrete Structures;
- touch CS2;
- redesign course content;
- introduce a new LMS abstraction;
- change grading policy to make deployment easier;
- delete instructor-created Canvas objects whose ownership is unknown;
- publish a different course because its name looks similar;
- use Savnac course id 1 or Harbor 24298 as the production destination.

Shared Course Foundry/Harbor repairs are allowed when they are necessary to complete CS1 correctly and are covered by tests.

---

# Required report

Create:

`sidecar/reports/103_cs1_online_full_production_imprint.md`

Include:

- exact production course id/name/code/section;
- pre-write repo SHAs;
- pre-write Canvas snapshot location/receipt;
- first-run create/update/unchanged/delete/skip counts;
- any shared-infrastructure fixes and commits;
- complete grading-contract read-back;
- date audit result;
- sentinel-week read-back for 1, 2, 6, 9, 14, 15, 16, 17;
- navigation/link audit;
- second-run idempotency receipt;
- remaining yellows, if any;
- clear verdict: DEPLOYED or NOT DEPLOYED.

If the course is not actually usable by a student, the verdict is NOT DEPLOYED even if API writes succeeded.

---

# Done when

This prompt is complete when the exact Fall 2026 Computer Science I Online production course has been reconciled from Git, read back, and rerun idempotently, with no known launch-blocking mismatch.
