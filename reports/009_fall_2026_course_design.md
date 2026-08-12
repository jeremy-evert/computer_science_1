# Report 009 — Fall 2026 CS1 design

Prompt `jeremy_task_tracking/codex_prompts/010_design_the_four_courses.md`
produced a planning-only CS1 design. Evidence: existing CS1 metadata, weekly
plans, block map, assignment map, lessons/assignments, and durable CS1
manifest/TOC at `durable/zybooks_captures/SWOSUCOMSC1033Fall2026`.

The corrected durable manifest has 466 discovered sections, including valid
13.10. `planning/zybooks-section-decisions.csv` classifies all sections exactly
once without copying licensed body content. It keeps the existing Coding
Odyssey/AI Fluency/Professional Minds semester structure and makes the
ZyBooks path a bounded support layer.

Validation: manifest rows, CSV rows, unique section IDs, classifications, and
required-week mappings were checked; `git diff --check` was run. No Makefile,
`make task-check`, `make check`, or application test suite exists for these
planning artifacts. No Canvas, Savnac, ZyBooks, roster, gradebook, or student
data write occurred. Open scope, citation, grading, and vendor-price questions
are stated in the course design.
