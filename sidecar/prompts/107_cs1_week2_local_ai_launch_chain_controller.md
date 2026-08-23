# Sidecar Prompt 107 — CS1 Week 2 Local AI Launch Chain Controller

**Status:** READY FOR OWNER-AUTHORIZED SOURCE CAMPAIGN  
**Owner decision:** Option A, Local AI Lab is the Week 2 spine  
**Production Canvas posture:** credentials intentionally unavailable; no production Canvas work is authorized

## Mission

Run a small bounded chain that gets CS1 Week 2 as prepared as it can be **before** Jeremy's owner Windows dry run.

Do not make Jeremy the clipboard or the clock pulse between rounds.

Control loop:

`integrate curriculum -> adversarial review -> repair if needed -> stage website -> adversarial review -> repair if needed -> reconcile launch manifest -> stop at owner dry-run gate`

This is inspired by the Foreman chain-gun pattern, but intentionally much smaller. The purpose is not throughput. The purpose is to remove unnecessary human reloads while preserving hard release and production boundaries.

## Owning project

Repository:

`jeremy-evert/computer_science_1`

Local checkout expected on Maise:

`/mnt/nora/git/computer_science_1`

If the actual current checkout lives at another already-established path, resolve it from current Git/workspace truth rather than cloning a duplicate blindly.

## Read before starting

Read:

1. `START_FOREMAN.md` / current Foreman Interface rules relevant to a scoped Luna job.
2. `sidecar/raw/2026-08-22_week2_local_ai_launch_owner_decision.md`.
3. current `computer_science_1/main` and Week 2 truth.
4. current read-only `local_ai_lab_setup/main`, especially `reports/piper/2026-08-22_mission_004_after_action_report.md` and `packages/cs1_online/`.
5. current `swosu-computing/main` Local AI/CS1 pages.
6. current `course_foundry/main` only as needed for source compilation and desired-state behavior.
7. the Foreman raw S'MOOR chain-gun briefing as **context only** if it is locally available. Its useful principle here is execute -> self-AAR -> smallest repair -> reconcile, not its S'MOOR-specific branch/mission authority.

## Campaign branches

Do not move accepted `main` branches underneath this source campaign.

Preferred implementation branches:

- `computer_science_1`: `campaign/week2-local-ai-launch`
- `swosu-computing`: `campaign/week2-local-ai-launch`
- `course_foundry`: `campaign/cs1-week2-local-ai-launch` **only if Prompt 107A proves a compiler change is necessary**

Create from current fetched main only when needed.

Never force-push.

Never merge these branches to main during this controller.

`local_ai_lab_setup` is read-only for this campaign. Its next vote is the owner Windows dry run, not another speculative package edit.

## Recovery state

On first campaign write, create on the CS1 campaign branch:

`sidecar/reports/107_week2_local_ai_chain_progress.md`

Keep it thin. Record only durable gates:

- campaign start with accepted main base SHA(s);
- each round STARTED with exact prompt path and execution branch head;
- each round LANDED with report path/verdict/commit;
- inserted repair rounds;
- final stop reason.

No heartbeat spam, secrets, tokens, student data, or hidden model reasoning.

If the session is interrupted, reconstruct from GitHub branch heads, this progress file, and committed round reports. Do not guess where the chain was from conversational memory.

## Round 1 — 107A curriculum integration

Execute exactly:

`sidecar/prompts/107A_week2_local_ai_curriculum_integration.md`

Required landing verdict: `INTEGRATED`.

If `BLOCKED`, stop only if the blocker meets a hard-stop rule. Otherwise resolve ordinary repository/test friction and finish the bounded round.

Commit/push before advancing.

## Round 2 — 107B adversarial curriculum review

Execute exactly:

`sidecar/prompts/107B_week2_local_ai_adversarial_review.md`

If verdict is `PASS`, advance.

If verdict is `REPAIR REQUIRED`:

1. execute `sidecar/prompts/107R_week2_local_ai_repair_from_self_aar.md`;
2. require `REPAIRED`;
3. rerun 107B against the new exact campaign state;
4. allow at most **two repair/re-review cycles** before declaring `HARD STOP` for repeated material failure.

If 107B returns `HARD STOP`, stop the chain.

Finding a defect is progress. Do not hide a 107B defect inside website work.

## Round 3 — 108A website staging

Only after the curriculum review passes, execute:

`sidecar/prompts/108A_stage_cs1_local_ai_website.md`

Required landing verdict: `STAGED`.

This round stages `swosu-computing` on a non-production branch. It does not publish the final CS1 path.

## Round 4 — 108B adversarial website review

Execute:

`sidecar/prompts/108B_cs1_local_ai_website_adversarial_review.md`

If `PASS`, advance.

If `REPAIR REQUIRED`:

1. execute `sidecar/prompts/108R_cs1_local_ai_website_repair.md`;
2. require `REPAIRED`;
3. rerun 108B;
4. allow at most **two repair/re-review cycles** before `HARD STOP`.

Do not protect a pretty page from criticism.

## Round 5 — 109 launch-readiness reconcile

Execute:

`sidecar/prompts/109_week2_local_ai_launch_readiness_reconcile.md`

Target verdict:

`READY FOR OWNER WINDOWS DRY RUN`

The manifest should prove that the curriculum source, exit tickets, and website are actually staged and tested, not merely described.

## Production / release hard stops

**STOP. DO NOT INFER PERMISSION.** before any of the following:

- restoring, sourcing, requesting, or using production SWOSU Canvas credentials;
- reading/writing live Canvas as part of this campaign;
- merging CS1, website, or Course Foundry campaign branches to main;
- publishing the staged CS1 website route;
- altering TinyURL;
- creating the final student ZIP before the owner Windows dry run;
- claiming Windows acceptance without that dry run;
- importing Week 3 Work First/Sidecar/Git-push curriculum into Week 2;
- changing grading weights or standing grading policy;
- modifying `local_ai_lab_setup` package architecture;
- unrelated semester/course work.

The absence of production Canvas credentials is intentional and should make this source campaign safer. It is not a reason to ask Jeremy to restore them tonight.

## Existing A10 blocker

Do not execute the live A10 repair in this chain.

Prompt 109 must preserve it on the final launch checklist. The existing 104A prompt remains the bounded production repair path after production Canvas access is deliberately restored/authorized.

## Git / evidence doctrine

For every writable repository:

- inspect status before work;
- protect unrelated/dirty state;
- fetch current origin;
- branch from current accepted main when creating a campaign branch;
- stage only in-scope changes;
- run required tests before commits;
- use forward commits only;
- push each landed round;
- verify remote branch/commit durability;
- record exact pointers in reports/progress.

A source file existing locally is not proof it is in the compiled course. A desired object existing is not proof its grading behavior is safe. A website file existing is not proof its links work. Require the evidence each child prompt asks for.

## Human nudge threshold

A HUMAN NUDGE is valid only for a genuine owner preference/authority decision, physical Windows dry run, credential/production boundary, destructive/safety issue, unresolved consequential ambiguity, unsafe repository state, or hard capability/resource gate with no authorized fallback.

Do not stop after a successful round merely because Jeremy is not at the keyboard.

Do not ask Jeremy to relay files, paste prompts, compare branches, or manually inspect Git state that Luna can inspect.

## Final stop

When Prompt 109 lands with `READY FOR OWNER WINDOWS DRY RUN`:

record in the progress file:

`CHAIN STOPPED: OWNER WINDOWS DRY RUN REQUIRED`

Then stop.

Do not automatically continue into ZIP creation, website publication, campaign merges, Canvas deployment, or A10 production repair.

## Final handoff

Return a compact handoff containing:

- final chain verdict;
- Prompt 109 manifest path/commit;
- CS1 campaign branch/head;
- website campaign branch/head;
- Course Foundry campaign branch/head if used;
- three exit-ticket source paths;
- intended future public CS1 Local AI URL;
- Local AI source commit/head to dry-run;
- exact remaining hard gates;
- confirmation that production Canvas credentials were not used/restored.

The successful end state is simple: **everything that can responsibly be built before the Windows reality check is built, reviewed, pushed, and waiting at the gate.**