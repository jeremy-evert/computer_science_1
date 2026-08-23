# Sidecar Prompt 107B — Adversarial Review of the CS1 Week 2 Local AI Integration

**Status:** READY  
**Depends on:** Prompt 107A report and campaign commits  
**Mode:** prosecute the implementation, do not protect it

## Mission

Assume Prompt 107A was implemented by a competent but optimistic worker. Attack its claims before any public or Canvas-facing promotion.

Work against the exact pushed campaign state produced by 107A. Do not review an uncommitted local approximation.

Required posture question:

> What could Jeremy discover during the Windows dry run, first student week, or later gradebook review that would make the 107A completion report embarrassing?

## Review targets

Read:

- `sidecar/raw/2026-08-22_week2_local_ai_launch_owner_decision.md`
- `sidecar/reports/107A_week2_local_ai_curriculum_integration.md`
- the exact changed CS1 files/commits
- any exact Course Foundry campaign commit used by 107A
- current read-only `local_ai_lab_setup` package/Mission 004 AAR
- current Week 2 grading/source truth

Independently test the material claims below.

## 1. One story, not two piles

Can a student tell what to do Monday, Wednesday, and Friday without bouncing between an old Week 2 and a second AI onboarding track?

Look for:

- duplicate starts;
- contradictory ordering;
- repeated assignments that test the same thing;
- links that send students backward or to internal repository paths;
- course prose that assumes tools before the setup step that acquires/verifies them.

## 2. Learning objectives survived

Prove the integration did not accidentally erase or bury:

- run/read/change Python;
- `print` / `input`;
- variables, expressions, types;
- Gather Context;
- *Make It Stick*;
- *Mindset*;
- Coding Odyssey genre/founding charter/gate.

Also prove Aider is not being used to outsource the student's genre choice, founding condition, or evidence explanation.

## 3. Exit-ticket grading safety

For all three new exit tickets, prove from desired-state/source behavior that:

- they are student-submittable in the intended way;
- they do not enlarge a weighted grade denominator;
- they do not change assignment-group weights;
- they do not change standing drop rules;
- a legitimate `NOT READY` machine result can still satisfy Monday's evidence requirement.

A title saying "0 points" is not proof. Inspect the compiled/desired object behavior.

## 4. Module reachability and ordering

Inspect compiled/desired module state and prove:

- Monday content precedes Monday Exit Ticket;
- Wednesday Aider/Toys content precedes Wednesday Exit Ticket;
- Friday Toy/Odyssey content precedes Friday Exit Ticket;
- existing weekly graded items remain reachable;
- no stale link token, bare internal path, Savnac-only URL, localhost URL, placeholder, or TODO leaks into student content;
- any literal lesson-path references required by scanners remain intact.

## 5. Online / face-to-face parity

The Local AI core path must work for both sections.

Flag any instruction that requires:

- a physical classroom-only asset without an online equivalent;
- a human partner for the core Local AI setup;
- instructor intervention where the package already defines a safe recovery path;
- production-only credentials or campus-only assumptions.

## 6. Week boundary discipline

Prove Week 2 did not silently absorb:

- Git add/commit/remotes/SSH/push/pull instruction;
- Sidecar doctrine;
- Work First progressive scripts;
- Codex/Claude onboarding;
- cloud credentials;
- broad hardware promises.

Those belong later or remain out of scope.

## 7. Evidence claims

Check every strong claim in the 107A report against actual tests/compiled state.

Look specifically for:

- tests that prove less than the report says;
- source files created but not discovered by Course Foundry;
- desired objects that exist but land in the wrong module/group;
- hidden dependence on a live website route that is not yet published;
- accidental changes outside Week 2;
- dirty/unpushed campaign state;
- branch pointers that do not match the report.

## Required report

Write on the CS1 campaign branch:

`sidecar/reports/107B_week2_local_ai_adversarial_review.md`

Use one of exactly these verdicts:

- `PASS`
- `REPAIR REQUIRED`
- `HARD STOP`

For every finding, include:

- severity;
- exact file/object/claim;
- evidence;
- smallest repair required;
- whether the defect blocks website staging.

If `REPAIR REQUIRED`, produce a bounded repair list suitable for Prompt 107R. Do not quietly fix implementation defects inside this review except for a report-only typo that cannot affect behavior.

## Git / durability

Commit/push the review report to the CS1 campaign branch and verify the remote commit.

## Hard stops

Do not use or restore production Canvas credentials. Do not merge campaign work to main. Do not publish the CS1 website. Do not create the final ZIP.

## Done when

The integration has either survived independent prosecution or has a precise smallest-possible repair list. Finding a real defect is a successful review.