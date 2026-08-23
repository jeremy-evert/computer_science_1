# Sidecar Prompt 108R — Repair Only the Website Defects Proven by 108B

**Status:** CONDITIONAL  
**Run only if:** `sidecar/reports/108B_cs1_local_ai_website_adversarial_review.md` verdict is `REPAIR REQUIRED`

## Mission

Repair only the material website defects proven by Prompt 108B, then rerun the failed review checks.

Use the existing `swosu-computing` `campaign/week2-local-ai-launch` branch and the existing CS1 campaign branch.

## Authority

Read:

1. 108A report;
2. 108B report;
3. exact website campaign diff;
4. owner-decision file;
5. canonical read-only Local AI package source.

The 108B finding list controls this round. Do not redesign the site or add unrelated features.

## Required behavior

For each material finding:

- apply the smallest HTML/navigation/content correction;
- preserve the CS1-vs-managed-lab distinction;
- preserve existing CS2/DSCT behavior;
- keep the final download/release gate un-crossed;
- rerun the exact static/link/hygiene check that exposed the defect.

## Required report

Write:

`sidecar/reports/108R_cs1_local_ai_website_repair.md`

Use one of exactly these verdicts:

- `REPAIRED`
- `STILL BLOCKED`
- `HARD STOP`

Record exact website repair commits, validation, and pushed branch heads.

## Hard stops

No merge to main. No public release. No final ZIP. No Canvas credentials. No TinyURL mutation.

## Done when

Every material 108B finding is either closed with independent evidence or precisely remains blocked. Control returns to the chain controller for one more 108B review pass.