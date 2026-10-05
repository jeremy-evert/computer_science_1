# Strings Are Objects — Phase 1 Status

**Phase:** 1 — Build the Mad Lib demo
**Branch:** codex/strings-phase1
**Status:** COMPLETE
**Started from:** codex/strings-phase1 at `f9dce2f42e69aac1b03069597873b1d8e8d6715c`
**Last updated:** 2026-10-05

## Goal

Build and validate one playful, beginner-readable Python Mad Lib that uses
string methods and invites questions about dot notation.

## Files changed

- `lessons/code/strings_mad_lib.py`
- `planning/2026-10-05_strings_are_objects_phase_01_status.md`

## Commands / validation

- `python3 lessons/code/strings_mad_lib.py` — PASS, interactive run,
  six answers accepted, exit status 0.
- `git diff --check` — PASS before staging; untracked files were not covered.
- `git diff --cached --check` — initially flagged trailing spaces in the
  validation note's sample inputs. Quoted the samples to preserve visible
  input spaces without trailing file whitespace; final staged check PASS.

Interactive answers (quotes delimit the input and were not typed):

```text
"  cAPTAIN nOODLE  "
"  WOBBLY  "
"  ToAsTeR  "
"  the MOON  "
"  DANCE  "
"  a COMMITTEE of RUBBER ducks  "
```

The before/after display changed `"  cAPTAIN nOODLE  "` to `"Captain Noodle"`.
The story used `The Moon`, `wobbly`, `toaster`, `dance`, and
`a committee of rubber ducks`, confirming whitespace cleanup and case
transformations. A campus goose appointed the toaster dean and moved classes
to the duck pond. The story was reviewed for coherence and live-demo humor.

## Decisions made

- Used the established `lessons/code/` location, following the runnable
  Week 2 companions and their references in the variables lesson.
  No new top-level content category was needed.
- Used six inputs, `.strip()`, `.title()`, `.lower()`, and an f-string.
  Kept the code to straight-line input, assignment, and printing.
- Displayed the raw and cleaned name to make transformations visible.
- The referenced `../AGENTS.md` was absent. Read the repository's
  `AGENTS.md` and sibling `jeremy_task_tracking/COURSE_DESIGN_RULES.md`.
- Staging initially failed because the worktree Git index lives outside
  the writable workspace. Retried staging with approved escalation.
- This status file replaces the temporary Phase 1 validation note.

## Breadcrumbs for the next phase

Put the future String Laboratory in `lessons/code/` alongside the Mad Lib.
The demo saves method results; Phase 2 can explain why saving the returned
string matters through its planned immutability example. The before/after
name display provides a transition to dot notation.

Phase 2 has not begun. No String Laboratory, lesson expansion, or slides
were created. This phase is committed locally; nothing was pushed or merged.

## Blockers

NONE
