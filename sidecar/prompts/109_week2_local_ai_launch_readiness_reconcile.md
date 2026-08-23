# Sidecar Prompt 109 — Reconcile CS1 Week 2 Local AI Launch Readiness

**Status:** READY after curriculum and website reviews pass

## Mission

Produce the final source-side launch manifest for CS1 Week 2.

This is a reconciliation/reporting round, not another feature sprint.

The goal is to leave Jeremy with a very small owner gate tomorrow:

`Windows dry run -> repair only observed defects -> exact ZIP -> test exact ZIP -> promote website/source -> Canvas reconcile when credentials are deliberately restored`

## Read current durable truth

Read:

- `sidecar/raw/2026-08-22_week2_local_ai_launch_owner_decision.md`
- 107A/107B and any 107R reports
- 108A/108B reports and exact website campaign branch
- current `local_ai_lab_setup` Mission 004 AAR + package tree
- current `computer_science_1` campaign branch and grading/source state
- current relevant `course_foundry` campaign branch if 107A required one
- existing `sidecar/prompts/104A_cs1_a10_bonus_group_repair.md` and latest Owner A10 report

Do not assume any report is current if a branch advanced after it. Reconcile exact branch heads.

## Required launch manifest

Write:

`sidecar/reports/109_week2_local_ai_launch_readiness_manifest.md`

The report must answer these questions plainly.

### 1. Is the Week 2 curriculum source ready?

State:

- exact CS1 campaign branch/head;
- exact Course Foundry campaign branch/head if any;
- exact Week 2 student arc;
- exact exit-ticket source paths;
- grading-denominator proof;
- test status;
- any unresolved source defect.

### 2. Is the public CS1 website ready to publish after dry run?

State:

- exact `swosu-computing` campaign branch/head;
- exact intended future URL;
- page paths;
- current release-placeholder state;
- static/adversarial review result;
- the exact one or two edits still required when the final ZIP exists.

### 3. Is the Local AI package ready for the owner dry run?

Reference current `local_ai_lab_setup` evidence and state the exact accepted source commit/head.

Do not upgrade Mission 004's source-ready verdict into Windows acceptance.

### 4. What is still blocked by deliberate owner gates?

At minimum distinguish:

- owner Windows dry run;
- any dry-run-derived repair;
- final ZIP creation;
- exact ZIP Windows test;
- merge/publication of staged website;
- merge/promotion of campaign curriculum/compiler branches;
- production Canvas reconciliation after credentials are deliberately restored;
- known A10 live assignment-group repair.

The revoked/removed production Canvas credential is a **deliberate safety boundary**, not a reason to ask Jeremy to restore it tonight.

### 5. What can be promoted automatically after a clean dry run?

Give a precise promotion plan, by repo/branch, with no secrets:

- source branches to merge;
- website branch to finalize/merge;
- release asset location/name to create after the dry run;
- validation to rerun after release insertion;
- production Canvas deployment/readback step that must wait for explicit credential restoration/authorization.

Do not perform those promotions in this prompt.

## A10 handling

Do not mix the A10 live gradebook repair into Week 2 content.

Record its current status accurately. If source/compiler repair already exists, cite it. If only Prompt 104A exists, say so.

Because production Canvas credentials are intentionally unavailable, do not attempt the live A10 read/write. The manifest should make the remaining one-object production repair visible so it cannot disappear from the launch checklist.

## Campaign cleanliness

Verify all campaign repositories used are:

- committed;
- pushed;
- not carrying unrelated dirty work;
- traceable from report pointers.

Do not discard pre-existing local work to make a status look prettier.

## Verdict

Use exactly one:

- `READY FOR OWNER WINDOWS DRY RUN`
- `SOURCE REPAIR REQUIRED`
- `HARD STOP`

A clean result should mean that **other than the empirical Windows/release/production gates, the course is prepared rather than merely planned.**

## Git / durability

Commit/push the manifest to the CS1 campaign branch and verify the remote commit.

## Hard stops

Do not:

- restore/use production Canvas credentials;
- merge campaign branches to main;
- publish the website;
- create the final ZIP;
- claim Windows acceptance;
- alter TinyURL;
- import Week 3 work.

## Done when

Jeremy can read one report tomorrow and know exactly what is already built, what branch contains it, what the Windows dry run must prove, and the shortest safe sequence from dry-run success to Monday-ready production.