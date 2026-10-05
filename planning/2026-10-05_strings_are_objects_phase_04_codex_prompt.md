# Codex Session 4 — Strings Are Objects Beamer deck

Execute **Phase 4 only**.

## Required reading

Read these before editing:

1. `AGENTS.md`
2. `NAMING.md`
3. `docs/course-ethos.md`
4. `planning/2026-10-05_strings_are_objects_lesson_map.md`
5. `planning/2026-10-05_strings_are_objects_codex_execution_plan.md`
6. `planning/2026-10-05_strings_are_objects_breadcrumb_protocol.md`
7. `planning/2026-10-05_strings_are_objects_phase_01_status.md`
8. `planning/2026-10-05_strings_are_objects_phase_02_status.md`
9. `planning/2026-10-05_strings_are_objects_phase_03_status.md`
10. `planning/2026-10-05_strings_are_objects_phase_04_readiness.md`
11. `lessons/06-strings.md`
12. `lessons/code/strings_mad_lib.py`
13. `lessons/code/string_lab.py`
14. `slides/README.md`
15. `slides/_template.tex`

## Entry gate

Before writing the deck:

- verify Phase 1, Phase 2, and Phase 3 status files exist
- verify all three are COMPLETE
- verify both runnable Python examples exist
- verify the canonical lesson is no longer the old placeholder

If any prerequisite is absent or BLOCKED:

1. create/update `planning/2026-10-05_strings_are_objects_phase_04_status.md`
2. mark Phase 4 BLOCKED
3. record exactly what is missing
4. STOP

Do not reconstruct missing prior work.

## Goal

Create:

`slides/06_strings_are_objects.tex`

Use `slides/_template.tex` as the chassis.

The presentation should support live teaching, not replace the canonical lesson.

## Story arc

Use the canonical lesson as authority, with an arc approximately like:

1. Strings Are Weirdly Powerful
2. Mad Lib opener
3. What is a string?
4. Better question: how does a string behave?
5. The dot
6. `object.method()`
7. string behavior demo
8. What makes something an object?
9. type + state/value + behavior
10. strings are immutable
11. you are not supposed to memorize everything
12. `type()`, `dir()`, `help()`
13. Object Detective preview
14. objects in games
15. objects in networking
16. objects in organizations
17. objects in policy/procedure
18. why object thinking scales
19. return to the Mad Lib
20. exit question: What is this thing, and what can it do?

This is a guide, not a quota. Preserve the lesson's actual story if Phase 3 improved the sequence.

## Slide rules

- 16:9
- large readable type
- sparse frames
- one question, example, diagram, or punchline per frame when practical
- prefer live coding cues over giant code dumps
- code frames must use `[fragile]`
- use the tested Python examples rather than inventing contradictory snippets
- do not claim Cisco IOS itself uses Python dot notation
- conceptual cross-domain examples must be labeled as conceptual when they are not literal Python
- no decorative clutter
- no paragraph walls

## Validation

Run:

```bash
bash slides/build.sh slides/06_strings_are_objects.tex
```

If LaTeX is unavailable, record the exact missing toolchain in the status file.

Also inspect for:

- snippets that disagree with runnable examples
- unreadably dense frames
- missing `[fragile]` on code frames
- technical overclaims
- broken paths

## Breadcrumb

Create/update:

`planning/2026-10-05_strings_are_objects_phase_04_status.md`

Record:

- branch and starting ref
- COMPLETE or BLOCKED
- files changed
- compile command and result
- decisions made
- breadcrumbs for Phase 5
- blockers or NONE

## Hard boundary

Do **not** begin Phase 5.

Do not create the Object Detective assignment.

Do not perform unrelated repository cleanup.

When Phase 4 is validated:

1. update the Phase 4 status file
2. show files changed
3. show validation results
4. commit with a clear Phase 4 message
5. STOP

Do not push or merge.
