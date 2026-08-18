# Sidecar Prompt 104 - Student-view launch closeout for Computer Science I Online

**Status:** READY AFTER 103 DEPLOYED  
**Scope:** Final launch verification and surgical repair of the exact Fall 2026 Computer Science I Online course  
**Owner:** Foreman  
**Mode:** inspect as student -> exercise launch path -> verify visibility -> repair only proven defects -> final read-back -> report -> stop

## Mission

Prompt 103 performed the production reconcile. This prompt decides whether the course is actually ready for a student to use.

Do not treat "the API returned 200" as launch readiness.

The governing question is:

> If a real student opens Computer Science I Online now, can they understand where to begin, reach the required work, submit what they are supposed to submit, and move through the semester without encountering broken or contradictory course structure?

Use Canvas test-student/student-view mechanisms where available and safe. If the API cannot model a specific student-view behavior, inspect the exact visibility/prerequisite/module metadata that controls it and disclose the limitation.

---

# Preconditions

Read:

- `sidecar/reports/102_cs1_online_launch_recon_and_target_lock.md`
- `sidecar/reports/103_cs1_online_full_production_imprint.md`

Require Prompt 103 verdict = `DEPLOYED` before proceeding.

Reconfirm the same exact production course id. Do not discover a new target in this prompt.

---

# 1. Opening-minute test

Inspect the course as a student from the landing page.

A new student should be able to answer within the first minute:

- What course is this?
- Where do I start?
- What do I do in Week 1?
- What is due first?
- Where do I find the syllabus/course policies?
- How do I move to the next week?

Verify the course home/landing behavior, visible navigation menu, Start Here/Week 1 path, and module ordering.

Repair only concrete usability defects. Do not redesign the visual identity tonight.

---

# 2. Visibility and publish-state audit

For every module and managed student-facing object, verify the intended visibility state.

Find and classify:

- unpublished modules that should be available;
- published modules whose child items are unavailable;
- published assignments/pages hidden by availability dates;
- module items pointing to unpublished targets;
- instructor-only pages exposed to students;
- required pages accidentally omitted from modules;
- stale prerequisites/requirements inherited from an older shell;
- accidental sequential locks that prevent normal weekly navigation.

The course may intentionally stage future material. Preserve intentional release strategy. The requirement is that the current launch window and intended preview/navigation behavior are coherent.

---

# 3. Submission-path audit

Inspect every assignment category represented in the active grading model.

For representative assignments across the semester, verify:

- submission type matches the assignment instructions;
- online text/file/URL/no-submission settings are intentional;
- points possible are correct;
- assignment group is correct;
- due date is correct;
- availability dates do not contradict the due date;
- assignment body tells the student what successful submission looks like;
- external-tool/link assignments point to the intended system;
- no object is marked graded when its instructions describe a reflection/page-only activity that should not be submitted.

Exercise at least one representative assignment from each distinct submission pattern.

Do not manufacture submissions in a real student's account. Use test-student/student-view facilities only.

---

# 4. Gradebook structure audit

Read back the production gradebook as configured.

Verify:

- assignment groups total 100%;
- each managed graded assignment belongs to an intended group;
- no substantial graded orphan objects exist;
- drop-lowest rules are present exactly where policy says they should be;
- bonus practice cannot reduce a student's grade;
- no retired/historical assignment is contributing points;
- attendance/course evaluation/final reflection/professional pathway objects have the intended gradebook behavior;
- Week 16 contains no forbidden graded weekly-category zombies.

If Canvas UI/API behavior around extra credit or weighted groups differs from the intended mathematical behavior, test the configuration with a harmless synthetic/test-student calculation if available and document the result.

---

# 5. Link and content integrity audit

Check student-facing links in the launch-critical course surface, then broaden mechanically where tooling permits.

At minimum verify:

- internal Canvas links stay within the locked production course;
- no Savnac localhost/192.168.x.x URLs are exposed;
- no old Canvas course ids are embedded in active links;
- required GitHub/open-source resource links resolve to intended public destinations;
- Professional Minds and AI Fluency links/content are present where required;
- file links resolve and students have permission to download/view them;
- PDFs/decks/assets expected by the compiled course are actually reachable;
- no placeholder/TODO text is visible in required student-facing content unless deliberately pedagogical.

Repair deterministic broken links/content references now.

---

# 6. Sentinel-week walkthroughs

Perform a structured student-path walkthrough for these weeks:

## Week 1

Verify shared kickoff ownership and the Survive the Semester / Survive the Degree / Enjoy the Career flow expected by the current shared kickoff design.

## Week 2

Verify the technical on-ramp is complete and the first required programming/Odyssey work is reachable with correct instructions and due dates.

## Weeks 6 and 9

Verify checkpoint behavior and grading placement.

## Week 14

Verify Git/professional-pathway/checkpoint structure does not accidentally become a new build sprint.

## Week 15

Verify fully asynchronous Thanksgiving-week behavior and the intended professional-pathway submission.

## Week 16

Verify the Farkle/ML payoff week is accessible, fun, and dead-days safe: no retired Odyssey Checkpoint 4, no unintended graded weekly categories, no broken shared Farkle assets.

## Week 17

Verify reflection/finals closure, with no zombie chapter exam.

---

# 7. Duplicate and zombie sweep

Search production Canvas for historical or duplicate remnants, including terms associated with superseded course designs:

- `Checkpoint 4`;
- `chapter exam`;
- required ZyBooks language;
- required Deitel language;
- duplicate module/page/assignment titles;
- old Week 16 final-project/show-and-tell requirements;
- stale 2025 or Spring 2026 due dates;
- Savnac references;
- placeholder content.

Do not delete a surprising instructor-created object unless ownership and obsolescence are clear. Managed zombies with clear replacements should be cleaned up through the existing reconcile mechanism where possible.

---

# 8. Final repair loop

For every launch-blocking defect found:

1. determine whether source Git, compiler, or Canvas state is wrong;
2. fix the correct layer;
3. add a regression test when the defect is in shared code/compiler behavior;
4. commit source/compiler fixes intentionally;
5. rerun production reconcile if needed;
6. read back again;
7. rerun the affected student-view check.

Do not patch Canvas manually in a way that immediately reverts on the next imprint unless there is a documented emergency-only reason.

---

# 9. Final launch verdict

Use only these verdicts:

- `READY FOR STUDENTS`
- `READY WITH NON-BLOCKING YELLOWS`
- `NOT READY`

A yellow is non-blocking only if a student can still complete the intended course path safely and correctly.

Examples of possible non-blocking yellows:

- an instructor-only cosmetic issue;
- a future-week enrichment asset not yet published but not required;
- a platform limitation with a documented manual workaround that does not affect current students.

Broken Week 1 navigation, wrong gradebook weights, inaccessible required assignments, wrong course target, duplicate graded assignments, or incorrect due dates are blockers.

---

# Required report

Create:

`sidecar/reports/104_cs1_online_student_view_launch_closeout.md`

Include:

- exact course id/name/section verified;
- opening-minute test result;
- navigation/visibility findings;
- submission-path matrix;
- gradebook audit;
- link/file integrity result;
- sentinel-week walkthrough results;
- duplicate/zombie sweep;
- defects repaired and the layer repaired;
- tests/commands run;
- commits created;
- final production reconcile/read-back receipt after repairs;
- final launch verdict;
- concise remaining yellows, if any.

---

# Done when

This prompt is done when the Foreman can truthfully say:

> The course is not merely populated. I walked the student path, proved the grading and dates, repaired the launch defects at the correct source layer, and Computer Science I Online is ready to teach.

Then stop. Do not roll into Computer Architecture from inside this repo; Jeremy will move the campaign to the next course deliberately.
