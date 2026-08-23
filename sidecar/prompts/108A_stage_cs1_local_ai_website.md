# Sidecar Prompt 108A — Stage the CS1 Local AI Student Website

**Status:** READY after 107B PASS  
**Owning course:** `jeremy-evert/computer_science_1`  
**Public implementation repo:** `jeremy-evert/swosu-computing`

## Mission

Stage the public CS1 Local AI student route so that, after the owner Windows dry run and exact ZIP release, publishing becomes a small promotion step rather than another design project.

Do **not** publish the CS1 route to the live GitHub Pages branch in this prompt.

Work in `swosu-computing` on:

`campaign/week2-local-ai-launch`

Create it from current `main` if absent. If it exists, resume only after proving its state is unambiguous and safe.

## Read first

Read current truth:

- CS1 owner decision: `computer_science_1/sidecar/raw/2026-08-22_week2_local_ai_launch_owner_decision.md`
- accepted 107A implementation + 107B PASS report, plus any 107R repair report
- current `swosu-computing` root, `/cs1/`, `/local-ai-lab/`, Bootstrap, CS2, and DSCT pages
- current read-only `local_ai_lab_setup/packages/cs1_online/00_START_HERE.md` through `09_AIDER_TOY_EXERCISES.md`
- current Local AI Mission 004 Piper AAR

The Local AI package owns the detailed setup truth. The public page should orient students and route them into the package without creating a second divergent manual.

## Required public architecture

Preserve the existing managed-lab path for CS2/DSCT while adding a distinct CS1 path.

Preferred staged shape:

- `/local-ai-lab/` becomes a clear chooser/landing page with:
  - **CS1: Build Your Own Local AI Lab**
  - **CS2 + DSCT: Managed Classroom Lab**
- new `/local-ai-lab/cs1/` is the CS1 Week 2 student page
- `/cs1/` gains a clear Week 2 Local AI Lab entry point
- existing CS2/DSCT routes continue to work and retain their managed-classroom safety language

If the current site structure suggests an even smaller compatible implementation, use it, but the two operating models must remain unmistakably separate.

## CS1 page content

The CS1 page should communicate, in student language:

### This week's goal

Get from an unknown Windows machine to:

`PowerShell + Python + Git + Ollama + qwen3:8b + Aider`

and make/test a few tiny code changes.

### The numbered path

Show the accepted source order exactly:

1. `00 START HERE`
2. `01 INVENTORY`
3. `02 VERIFY WINDOWS FOUNDATION`
4. `03 GET/VERIFY OLLAMA`
5. `04 GET/VERIFY qwen3:8b`
6. `05 HELLO OLLAMA`
7. `06 GET/VERIFY AIDER`
8. `07 PREPARE TINY GIT WORKTREE`
9. `08 HELLO AIDER`
10. `09 AIDER TOY EXERCISES`

Use the package for exact commands. Do not silently retype long command sequences into HTML if that creates drift risk.

### Evidence doctrine

Make these ideas visible:

- inventory answers FOUND/MISSING;
- readiness answers PASS/FAIL;
- `NOT READY` with preserved evidence is useful, not shameful;
- Ollama/model/Aider running does not prove an AI-generated answer is correct;
- inspect Git state/diff and run independent tests.

### Course route

Make Canvas prominent as the authoritative location for graded work, due dates, exit tickets, and submissions.

The page should link clearly back to CS1 Canvas using the existing production course URL already present in `swosu-computing`.

## Release/download placeholder

The final student ZIP does **not** exist yet by design.

Stage the website so release insertion is obvious but does not create a dead public link. Use a clearly marked source-level placeholder/comment or non-clickable campaign-only release note such as:

`FINAL DOWNLOAD INSERTED AFTER OWNER WINDOWS DRY RUN`

The campaign branch may contain that marker. The final launch manifest must treat its removal/replacement as a publication gate.

Do not fabricate a ZIP URL, release tag, checksum, Windows acceptance result, or download button.

## Keep Week 3 out

Do not put Sidecar, Work First, motorcycle-vs-garage doctrine, progressive Git scripts, SSH, push/pull, Codex, or Claude onboarding on the CS1 Week 2 website.

## Validation

At minimum:

- inspect all changed internal links/relative paths;
- run any existing static/site checks;
- serve the campaign branch locally if useful and verify the relevant pages with machine-readable HTTP requests;
- prove existing CS2/DSCT managed-lab content remains reachable and semantically intact;
- prove CS1 links do not point to a missing final ZIP;
- grep/sweep for credentials, PII, localhost/internal-only paths, TODOs, accidental Savnac links, unsupported admin/elevation guidance, and stale model names;
- run `git diff --check`.

## Required report

Write on the CS1 campaign branch:

`sidecar/reports/108A_stage_cs1_local_ai_website.md`

Use one of exactly these verdicts:

- `STAGED`
- `BLOCKED`

Record:

- `swosu-computing` campaign branch/base/head;
- exact pages changed/created;
- intended future live URL;
- how CS1 and CS2/DSCT paths are separated;
- release-placeholder mechanism;
- validation run/results;
- exact remaining publish gate.

## Git / durability

Commit/push website work to `campaign/week2-local-ai-launch`. Commit/push the report to the CS1 campaign branch. Verify both remote branch heads.

## Hard stops

Do not:

- merge `swosu-computing` campaign work to main;
- create the final ZIP;
- use/restore Canvas production credentials;
- alter TinyURL;
- change Local AI package source;
- publish a fake/untested download.

## Done when

The entire CS1 student website experience is staged and tested on a non-production branch, with only the owner Windows dry run, exact release artifact, and later promotion separating it from live publication.