# Sidecar Prompt 107R — Repair Only the Defects Proven by 107B

**Status:** CONDITIONAL  
**Run only if:** `sidecar/reports/107B_week2_local_ai_adversarial_review.md` verdict is `REPAIR REQUIRED`

## Mission

Repair the smallest set of material defects explicitly proven by Prompt 107B. Do not use this repair round as permission to redesign Week 2 or add improvements that the adversarial review did not require.

Work on the existing campaign branches created by Prompt 107A.

## Authority

Read, in order:

1. `sidecar/raw/2026-08-22_week2_local_ai_launch_owner_decision.md`
2. `sidecar/reports/107A_week2_local_ai_curriculum_integration.md`
3. `sidecar/reports/107B_week2_local_ai_adversarial_review.md`
4. exact current campaign diffs/commits

The 107B repair list controls this round. If a requested repair conflicts with the owner-decision file, stop with `HARD STOP` rather than choosing a new pedagogy.

## Required behavior

For each material 107B finding:

- identify the smallest source/compiler change that closes it;
- add or strengthen the narrow test that would have caught it;
- rerun the relevant focused validation;
- preserve every unrelated accepted 107A behavior;
- keep grading weights and standing assignments unchanged unless the 107B defect is specifically about the non-denominator exit-ticket contract.

Do not opportunistically clean unrelated files.

## Re-review requirement

After repairs, rerun the exact material checks from Prompt 107B that failed.

Do not simply state that the code changed.

## Required report

Write/update a new report, leaving 107B historical evidence intact:

`sidecar/reports/107R_week2_local_ai_repair.md`

Use one of exactly these verdicts:

- `REPAIRED`
- `STILL BLOCKED`
- `HARD STOP`

Include:

- 107B findings addressed;
- exact repair commits/files;
- tests and re-review evidence;
- remaining defects;
- exact pushed campaign branch heads.

## Git / durability

Commit/push verified repairs and the repair report to the appropriate campaign branches. Never force-push and never merge to main.

## Hard stops

Do not:

- use/restore production Canvas credentials;
- publish/merge the public website;
- create the final ZIP;
- change Local AI package architecture;
- import Week 3 Work First material;
- widen this into A10 or another semester repair.

## Done when

Every material 107B defect is either independently closed with evidence or precisely remains blocked. Control then returns to the chain controller for one more 107B prosecution pass before website staging.