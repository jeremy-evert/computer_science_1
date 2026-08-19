# Chaz Independent Acceptance Checklist — CS1 Prompts 103/104

**Owner:** Chaz  
**Purpose:** Independent Owner acceptance instrument for Flo's CS1 production closeout.  
**Scope:** Evidence review only. This checklist does not authorize production writes and is not Flo's self-evaluation.

## Evidence package required before acceptance

- [ ] `sidecar/reports/103_cs1_online_full_production_imprint.md`
- [ ] `sidecar/reports/104_cs1_online_student_view_launch_closeout.md` when 103 is `DEPLOYED`
- [ ] `sidecar/reports/103_104_flo_foreman_completion.md`
- [ ] One durable `sidecar/runs/103_104_flo_closeout/<UTC_TIMESTAMP>/` receipt directory
- [ ] Exact CS1 SHA and exact Course Foundry SHA used for the final accepted reconcile
- [ ] Any source/compiler repair commits referenced by Flo exist and are inspectable

## A. Target identity and cross-list topology

- [ ] Production target is exactly Canvas course `74029`
- [ ] No evidence of reads/writes/migration from `74033` except the permitted `nonxlist_course_id: 74033` field read from section `76388`
- [ ] Fresh pre-write section readback proves exactly the intended two-section topology
- [ ] Native section `76384` is present
- [ ] Merged section `76388` is present with `nonxlist_course_id: 74033`
- [ ] No topology mutation was attempted by Flo

## B. Enrollment sanity

- [ ] Fresh enrollment readback includes students from both `76384` and `76388`
- [ ] Enrollment count drift is explainable as ordinary add/drop activity
- [ ] Neither section has disappeared or become empty unexpectedly
- [ ] No acceptance claim depends on the historical 41-student count remaining exact

## C. Current source truth

- [ ] Final CS1 SHA is recorded
- [ ] Final Course Foundry SHA is recorded
- [ ] Flo reconciled against the current CS1 source state, not the pre-launch historical SHA by assumption
- [ ] Any source changes after the earlier production push were included in the final dry-run/reconcile
- [ ] Course Foundry two-commit yellow is treated as resolved by Chaz's independent note, not silently inherited as ambiguity

## D. Production dry-run and reconcile

- [ ] Pre-write Canvas snapshot exists and is sufficient to distinguish pre-existing instructor/native content from Flo's mutations
- [ ] Current production dry-run exists before mutation
- [ ] Create/update/unchanged-or-skip/delete counts are recorded and explainable
- [ ] Unexpected Canvas-only objects were classified before deletion/retirement
- [ ] No duplicate-object explosion occurred
- [ ] Any repair was made at the owning layer: CS1 source, shared compiler, or Canvas state, with rationale

## E. Gradebook contract

- [ ] Assignment-group weights sum to exactly 100%
- [ ] Each managed graded assignment is in the intended group
- [ ] `drop_lowest` / drop rules are actually present on every group where current policy requires them
- [ ] No group has a drop rule Canvas rejected or silently omitted
- [ ] Points possible and grading type match current `docs/grading-model.md` / compiler truth
- [ ] Bonus practice cannot reduce a student's grade
- [ ] Attendance, course evaluation, final reflection, and professional-pathway objects have intended gradebook behavior
- [ ] No retired/historical assignment contributes points
- [ ] Week 16 contains no forbidden graded weekly-category zombies

**Acceptance rule:** the prior Canvas error `Drop rules cannot be higher than the number of assignments` is not cosmetic. If required drop rules are missing, 103 cannot be accepted as `DEPLOYED`.

## F. Due dates and availability

- [ ] Full date audit uses Fall 2026 course/calendar truth
- [ ] No due date precedes course start
- [ ] Monday/Wednesday/Friday cadence is coherent where intended
- [ ] Week 15 is fully asynchronous
- [ ] Week 16 complies with dead-days policy
- [ ] Week 17/finals timing is coherent
- [ ] No stale 2025 or Spring 2026 dates remain
- [ ] `available_from` / `lock_at` do not make required published work inaccessible
- [ ] Timezone behavior is documented and coherent

## G. Module visibility and navigation

- [ ] Intended modules are present and ordered chronologically
- [ ] Required launch-window modules are published/visible as intended
- [ ] Published module items do not point to unpublished or unavailable targets
- [ ] No accidental prerequisite/sequential lock blocks ordinary navigation
- [ ] Start/landing path is obvious
- [ ] Week 1 flows cleanly into Week 2
- [ ] No dangling or duplicate module items remain

## H. Assignment and submission paths

- [ ] Representative assignment from every distinct submission pattern was exercised or inspected under student/test-student conditions
- [ ] Submission type matches instructions
- [ ] Points, group, due date, and availability are coherent
- [ ] Assignment body tells the student what successful submission means
- [ ] External-tool/link assignments point to intended systems
- [ ] Page-only/reflection-only activities are not accidentally configured as graded submissions
- [ ] No real-student account was used to manufacture test submissions

## I. Links and assets

- [ ] Internal Canvas links stay inside production course `74029`
- [ ] No Savnac localhost / `192.168.x.x` references are student-facing
- [ ] No old Canvas course ids are embedded in active required links
- [ ] Week 2 lesson/slides token is resolved, not literal `{{link:week02_monday_slides}}`
- [ ] Required Professional Minds and AI Fluency content is reachable
- [ ] Required PDFs/decks/files are reachable by students
- [ ] No required placeholder/TODO text remains unless deliberately pedagogical

## J. Harbor CDN false-positive separation

- [ ] Flo distinguishes Harbor's production CDN redirect/download verifier defect from real Canvas file absence
- [ ] File correctness is proved with direct Canvas metadata/readback or another bounded direct proof where Harbor is unreliable
- [ ] Valid files were not needlessly churned/reuploaded merely to satisfy a broken verifier
- [ ] Any residual Harbor limitation is documented as infrastructure yellow, not disguised as student success/failure

## K. Sentinel weeks

- [ ] Week 1: shared kickoff flow and start path
- [ ] Week 2: technical on-ramp, first Odyssey/programming work, correct links/dates
- [ ] Week 6: checkpoint behavior and grading placement
- [ ] Week 9: checkpoint behavior and grading placement
- [ ] Week 14: professional pathway / Git structure, no accidental new build sprint
- [ ] Week 15: fully asynchronous Thanksgiving-week behavior and intended pathway submission
- [ ] Week 16: Farkle/ML payoff, dead-days safe, no retired Checkpoint 4, no unintended graded weekly categories, assets reachable
- [ ] Week 17: reflection/finals closure, no zombie chapter exam

## L. Duplicate/zombie sweep

- [ ] No duplicate managed module/page/assignment titles remain
- [ ] No retired `Checkpoint 4`
- [ ] No retired chapter exam
- [ ] No required ZyBooks language
- [ ] No required Deitel language
- [ ] No stale Week 16 final-project/show-and-tell requirement
- [ ] No stale Savnac references
- [ ] Surprising instructor-created objects were preserved unless ownership/obsolescence was proved

## M. Idempotency

- [ ] Post-repair production readback exists
- [ ] Final dry-run/reconcile against unchanged desired state produces zero unintended creates
- [ ] Zero duplicate objects
- [ ] Zero oscillating deterministic updates
- [ ] Any excluded/noisy API fields are named and justified
- [ ] If a second run changes the same object again without a source change, acceptance stops until the imprint bug is resolved

## N. Prompt 103 acceptance

- [ ] 103 report includes exact target identity, SHAs, snapshot, reconcile counts, grading readback, date audit, sentinel weeks, navigation/link audit, idempotency receipt, and yellows
- [ ] Verdict is exactly `DEPLOYED` or `NOT DEPLOYED`
- [ ] If student usability is not actually proved, Chaz rejects `DEPLOYED`

## O. Prompt 104 student-path acceptance

- [ ] 104 ran only after a truthful 103 `DEPLOYED`
- [ ] Opening-minute test passed
- [ ] Visibility/publish-state audit passed or has only non-blocking yellows
- [ ] Submission-path matrix is complete enough to cover each distinct pattern
- [ ] Gradebook audit independently supports readiness
- [ ] Link/file integrity is proved
- [ ] Sentinel walkthroughs are documented
- [ ] Duplicate/zombie sweep is documented
- [ ] Verdict is exactly `READY FOR STUDENTS`, `READY WITH NON-BLOCKING YELLOWS`, or `NOT READY`
- [ ] Any yellow labeled non-blocking genuinely leaves the intended student path safe and completable

## P. Online/asynchronous invariant

- [ ] Online students are never required to attend face-to-face meetings/interactions
- [ ] Classroom/Zoom interaction, if present, is optional enrichment rather than a completion dependency
- [ ] Any in-class activity has an asynchronous completion path
- [ ] The online course can be completed without physical campus presence
- [ ] No student-facing instruction contradicts this invariant

## Q. Remaining yellows and boundary discipline

- [ ] Every remaining yellow has: evidence, owner/layer, student impact, and blocker/non-blocker classification
- [ ] Flo did not touch Computer Architecture, DSCT, CS2, Piper, or JTT
- [ ] Flo did not change cross-list topology
- [ ] Flo protected unrelated dirty/shared state
- [ ] Flo did not write or self-accept Chaz's Owner AAR

## Chaz final gate

Chaz may close the CS1 production-closeout job only when the evidence supports the actual student outcome, not merely successful API activity. Any failed item above must either be repaired before closure or explicitly classified as a truly non-blocking yellow with evidence.