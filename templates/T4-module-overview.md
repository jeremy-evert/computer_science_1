# Module Overview template

Per-module orientation page — the first item in every weekly Canvas module
(`docs/canvas-module-checklist.md`'s "Overview page" line, first proposed
2026-07-15, built by `course_foundry`'s `cs1_savnac_layout_and_navigation.py`
2026-07-30). Short, answers "what happens this week and what's due," and
regenerates itself from that week's actual pushed content — no separate
weekly upkeep once the pipeline runs.

`{{DOUBLE_BRACE}}` placeholders below are filled in by
`course_foundry/cs1_savnac_layout_and_navigation.py`, sourced from the
same `DesiredCourse` `cs1_desired_course.cs1_savnac_desired_course()`
already computes for this week's real module — this template never
invents a week's content; it only formats what that module already
contains.

---

# {{MODULE_TITLE}} — Overview

Quick orientation for this module: what's here, and what's due.

## This week's material

{{MATERIAL_LIST}}

## Due this week

{{DUE_LIST}}

## The weekly rhythm

Every class period is 10–15 minutes presented, then 35–40 minutes of
active work:

| Day | Strand | Active work |
|---|---|---|
| **Monday** | Monday Moment — AI fluency | Main topic of the week — lecture with live worked examples |
| **Wednesday** | Wacky Wednesday — professional minds | Paired programming |
| **Friday** | Fun Friday — professional minds | Show-and-tell |

New to this course? Read the **Start Here** page in Module 1 first — the
full weekly rhythm, the six standing weekly artifacts, and what a
supportive class structure means here all live there
(`docs/course-ethos.md` in the `computer_science_1` repo is the source of
record if this page and that one ever disagree).
