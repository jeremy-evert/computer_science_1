# Prompt 109 — CS1 Week 2 Local AI launch-readiness manifest

## Verdict

`READY FOR OWNER WINDOWS DRY RUN`

The source campaign is built, adversarially reviewed, pushed, and deliberately
stopped before the empirical Windows/release/production gates.

## Curriculum source

- CS1 branch/head: `campaign/week2-local-ai-launch` at
  `503e2d0135ce381e70347ac98d6b9dfa9aca2f0b`
- Course Foundry branch/head:
  `campaign/cs1-week2-local-ai-launch` at
  `f292c185f13c6fc6fce03f1312da80c7a758ad6b`
- CS1 107A verdict: `INTEGRATED`; 107B verdict: `PASS`
- Website 108A verdict: `STAGED`; 108B verdict: `PASS`

The student arc is one Week 2 story: Monday `00`–`05` inventory/readiness,
Ollama, approved model, and hello; Wednesday `06`–`08` Aider/Git visibility
and Toys 1–2; Friday Toy 3, *Mindset*, Coding Odyssey founding charter and
Week 2 gate, then reflection.

Exit-ticket source paths:

- `assignments/week02-local-ai-exit-ticket-monday.md`
- `assignments/week02-local-ai-exit-ticket-wednesday.md`
- `assignments/week02-local-ai-exit-ticket-friday.md`

The Course Foundry campaign preserves textual module/source order and compiles
these three named checkpoints as `online_text_entry`, `0` points, in the
existing Weekly Reinforcement Assignment group. No assignment-group weight,
standing graded item, or drop rule was changed; therefore the checkpoints do
not enlarge the weighted denominator. Monday explicitly accepts a preserved
`NOT READY` diagnostic.

Validation is green for source/reference assertions, Python bytecode
compilation, and `git diff --check`. The focused Course Foundry pytest suite
could not run on this host because no `.venv` exists and system Python lacks
`pytest`, `pydantic`, and the package runtime dependencies. This is a recorded
environment limitation, not an observed source defect; rerun the focused suite
in the promotion environment before merging the compiler branch.

## Public website staging

- Repository: `jeremy-evert/swosu-computing`
- Branch/head: `campaign/week2-local-ai-launch` at
  `11dcbe10f941544cfdaae5913ba17e1a8046e563`
- Intended future URL:
  `https://jeremy-evert.github.io/swosu-computing/local-ai-lab/cs1/`
- Staged page: `local-ai-lab/cs1/index.html`
- Course entry point: `cs1/index.html`
- Hub chooser/managed route: `local-ai-lab/index.html`

The page names the exact `00`–`09` package sequence, routes graded work to
Canvas, and keeps CS1's build-your-own model distinct from CS2/DSCT's managed
classroom lab. The final ZIP does not exist. The maintainer-only marker
`FINAL DOWNLOAD INSERTED AFTER OWNER WINDOWS DRY RUN` must be replaced with the
tested release link after the owner gate. Static links, HTTP 200 route smoke
tests, safety scans, and 108B review passed.

## Local AI package

Accepted source head: `local_ai_lab_setup` `5843352c97ca0e16cb237963687dc5d83003df6c`.
Mission 004 records the final `00`–`09` sequence, model/config consistency,
static and toy-test evidence, and explicitly leaves live Windows PowerShell,
Ollama, Aider, and inference untested. It identifies the owner Windows dry run
as the correct next gate. This manifest does not upgrade that source-ready
verdict into Windows acceptance.

## Deliberate remaining gates

1. Owner performs the Windows dry run against the exact package/source heads.
2. Repair only defects observed in that dry run, if any; rerun focused checks.
3. Create the final student ZIP only after the dry run, then test that exact ZIP
   on the intended Windows path.
4. Replace the website release marker and merge/promote the staged website only
   after the exact artifact is tested.
5. Merge/promote the CS1 and Course Foundry campaign branches only after the
   dependency-backed focused tests and owner acceptance are complete.
6. Deliberately restore/authorize production Canvas access before reconciling
   CS1 Canvas from accepted source. No production Canvas credential was
   restored or used in this campaign.
7. Execute the separate 104A A10 live assignment-group repair: its prompt is
   present and remains `READY`, but no live read/write or repair was attempted.

The dirty `swosu-computing` `main` checkout is pre-existing and was preserved;
its isolated campaign worktree is clean, committed, and pushed. No campaign
branch was merged, no website route was published, no TinyURL was changed, no
ZIP was created, and no Week 3/A10 work was imported into Week 2.

## Safe promotion sequence after a clean dry run

1. Record the Windows evidence and repair only observed defects.
2. Re-run CS1/source and dependency-backed Course Foundry checks.
3. Build and test the exact ZIP; record its name/checksum in the release
   evidence.
4. Insert the tested artifact link on the website campaign branch and rerun
   link/HTTP/publication scans.
5. Merge/promote the website, CS1, and Course Foundry campaign branches through
   the normal review path; do not self-merge this assistant campaign.
6. Only after explicit credential restoration/authorization, reconcile
   production Canvas and read back the accepted source state; handle A10 via
   its separate bounded prompt.

## Chain stop

`CHAIN STOPPED: OWNER WINDOWS DRY RUN REQUIRED`
