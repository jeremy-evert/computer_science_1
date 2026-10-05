# Strings Are Objects — Phase 2 Status

**Phase:** 2 — String Laboratory
**Branch:** codex/strings-phase2
**Status:** COMPLETE
**Started from:** codex/strings-phase2 / f9dce2f
**Last updated:** 2026-10-05

## Goal

Build a runnable, beginner-friendly demonstration of string methods, dot
notation, immutability, and object discovery using type(), dir(), and help().

## Files changed

- lessons/code/string_lab.py
- planning/2026-10-05_strings_are_objects_phase_02_status.md

## Commands / validation

- `python3 lessons/code/string_lab.py` — PASSED; ran without modification and
  output was inspected for all ten planned methods and discovery tools.
- `git diff --check` — PASSED.
- `git diff --cached --check` — PASSED before the implementation commit.
- Immutability output confirmed: `name.upper()` leaves `name` as `jeremy`;
  `name = name.upper()` makes it `JEREMY`. Original laboratory text also
  retains its spaces and capitalization after the method calls.
- Initial staging/commit attempt encountered a read-only Git metadata path.
  Retrying with approved sandbox escalation succeeded.

## Decisions made

Use the existing `lessons/code/` convention selected by Phase 1. Keep the
program as straightforward statements with labeled output, no dependencies,
no required input, and focused `help(str.replace)` documentation.
Quotes expose surrounding spaces. Mixed capitals make `title()` visible.
Show prefix/suffix checks before and after whitespace cleanup. Explain
string, list, integer, and boolean return values, zero-based positions, and
`find()` returning -1 for a missing match.

## Breadcrumbs for the next phase

Use the tested laboratory as source material for Phase 3. Explain that
reassignment changes what a variable refers to; it does not modify a string's
contents. Start discovery with familiar names in `dir()` and focused help.

This branch did not contain the Phase 1 Mad Lib. It was read from
`../computer_science_1-strings-p1/lessons/code/strings_mad_lib.py`, where it was
untracked at inspection time. Ensure Phase 1 is committed and available
before Phase 3. The shared `../AGENTS.md` referenced by repository rules was
missing; available repository instructions and course design rules were read.

The canonical lesson and presentation remain unchanged. No Phase 3 work was
started. This status file is committed locally; no push or merge was performed
under the session's explicit no-push/no-merge instruction.

## Blockers

NONE
