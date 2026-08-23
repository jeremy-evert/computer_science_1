# Sidecar Prompt 108B — Adversarial Review of the Staged CS1 Local AI Website

**Status:** READY after 108A `STAGED`

## Mission

Attack the staged CS1 Local AI website before anyone merges or publishes it.

Assume the 108A worker was competent but optimistic. Review the exact pushed `swosu-computing` campaign branch, not a local approximation.

Required posture question:

> What could a student click, misunderstand, or be told on Monday that would make this page embarrassing or unsafe?

## Review targets

Read:

- the owner decision file;
- 107A / 107B / any 107R reports;
- 108A report;
- current read-only Local AI package source and Mission 004 AAR;
- exact changed website files on `campaign/week2-local-ai-launch`.

Independently test:

## 1. Route clarity

Prove a student can distinguish:

- CS1: build/verify your own local lab;
- CS2/DSCT: use the managed classroom lab.

Flag any wording that blends the two environments or causes a CS1 student to follow managed-lab instructions that assume pre-provisioned tools.

## 2. No dead release path

Prove the staged website does not expose a clickable final ZIP/download URL that does not exist yet.

The release placeholder must be visible to maintainers but not masquerade as a live student asset.

## 3. Canonical sequence

Check that the public CS1 route names the exact current `00` through `09` sequence and exact model `qwen3:8b` without stale numbering or filenames.

If the page repeats exact commands, compare them byte-for-byte/semantically to canonical package source. Prefer removing duplicate command prose over maintaining two manuals.

## 4. Student safety and recovery

Prove the page does not tell students to:

- elevate/admin themselves casually;
- globally change execution policy;
- weaken security;
- repair PATH broadly;
- use cloud API keys;
- choose an unapproved fallback model;
- expose Ollama beyond loopback;
- invent GitHub/SSH steps in Week 2.

Prove `NOT READY` is framed as useful evidence and the course route tells the student where graded submission/help lives.

## 5. Existing site regression

Prove:

- root navigation still works;
- Bootstrap/office-hours/slides/examples paths are not broken by the change;
- CS2 and DSCT Local AI routes still work and retain managed-lab language;
- the CS1 Canvas link is current;
- no accidental Architecture inclusion was introduced.

## 6. Publication hygiene

Sweep changed public files for:

- credentials/tokens;
- internal hostnames/IPs;
- private repository URLs that students cannot access;
- Savnac-only links;
- localhost URLs presented as website destinations;
- TODO/placeholder text visible to students;
- unsupported claims of Windows acceptance;
- claims that the final ZIP has been tested.

## Required report

Write on the CS1 campaign branch:

`sidecar/reports/108B_cs1_local_ai_website_adversarial_review.md`

Use one of exactly these verdicts:

- `PASS`
- `REPAIR REQUIRED`
- `HARD STOP`

For each finding include exact path/evidence and smallest repair.

If repair is required, the chain controller may apply the smallest website-only repair and rerun this review once. Do not use the review itself to redesign the site.

## Git / durability

Commit/push the review report and verify the remote CS1 campaign branch.

## Hard stops

No merge to `swosu-computing/main`. No public release. No final ZIP. No production Canvas credential use/restoration. No TinyURL mutation.

## Done when

The staged website either survives independent prosecution or has a precise bounded repair list.