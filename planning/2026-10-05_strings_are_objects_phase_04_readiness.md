# Strings Are Objects — Phase 4 Beamer readiness

**Purpose:** Pre-stage the presentation chassis while Phase 3 writes the canonical lesson.

**Branch:** `codex/strings-phase4-prep`

## What is safe to prepare early

- a `slides/` convention
- a portable 16:9 Beamer template
- readable Python `listings` defaults
- a one-command compile helper
- the Phase 4 dependency and validation checklist

## What must wait for Phase 3

Do not write the actual `06_strings_are_objects.tex` teaching content until the Phase 3 canonical lesson is COMPLETE.

Phase 4 should consume, not compete with:

- the completed Mad Lib
- the completed String Laboratory
- the completed canonical `lessons/06-strings.md`
- Phase 1, 2, and 3 status receipts

## Phase 4 entry gate

Before building the real deck, verify these paths exist in the Phase 4 branch:

```
lessons/code/strings_mad_lib.py
lessons/code/string_lab.py
lessons/06-strings.md
planning/2026-10-05_strings_are_objects_phase_01_status.md
planning/2026-10-05_strings_are_objects_phase_02_status.md
planning/2026-10-05_strings_are_objects_phase_03_status.md
slides/_template.tex
slides/build.sh
```

Read all three phase status files.

If Phase 3 is BLOCKED or absent, Phase 4 should not invent the missing lesson.

## Fast start for Phase 4

Use the template as a chassis, then create:

`slides/06_strings_are_objects.tex`

The deck should remain a presentation layer over the canonical lesson.

Target roughly 20 slides, but story and pacing beat a numeric quota.

## Validation

Phase 4 should run:

```bash
bash slides/build.sh slides/06_strings_are_objects.tex
```

If the host lacks LaTeX, record that exact toolchain blocker in the Phase 4 status receipt rather than pretending the deck compiled.

Also verify:

- every code frame is `[fragile]`
- copied snippets agree with the runnable Python files
- the Cisco/networking comparison stays technically honest
- text remains readable at projector distance
- no slide becomes a paragraph dump

## Phase 4 breadcrumb

Create:

`planning/2026-10-05_strings_are_objects_phase_04_status.md`

Use the shared breadcrumb protocol and STOP when Phase 4 is complete.
