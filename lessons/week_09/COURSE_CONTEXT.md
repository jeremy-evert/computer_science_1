# Course context and authoring decisions

## Applicable instructions

The user supplied week_09 AGENTS.md instructions: follow shared instructions, prepare student-facing CS1 (COMSC-1033) Canvas source, and treat student deliverables as shared graded discussions. Peers must know they can see shared work. Do not reveal student names or personal details when quoting work elsewhere.

The literal `../AGENTS.md` path from week_09 was absent. The repository-level instructions were read at `../../AGENTS.md`, containing the same course rule. Their parent shared-instruction path was also absent. The referenced design rules were found and read at `../../../../jeremy_task_tracking/COURSE_DESIGN_RULES.md`.

The design rules specify one unmistakable graded target per week (the CS1 programming gate), with practice and other supporting activities ungraded. They also require preserving prior weeks. These materials implement supporting practice without creating new graded targets or replacing the existing Canvas discussion prompt.

## Design decisions

- Begin with the familiar string "Clay" and introduce terminology after observed behavior.
- Connect each lesson with the requested closing question and an original training-roster story.
- Use established tribe details; Sunny is described as a SandWing with NightWing ancestry in the overview. Training energy is explicitly invented, and all dialogue is original.
- Redefine Dragon locally in 05, 06, and 07 so each script is independent.
- Use labeled top-level sections to keep code accessible to beginners.
- Print short dir samples and docstring excerpts; place full help calls in shell exercises to avoid long normal output or interactive blocking.
- Explain that the underscore filter hides all leading-underscore names temporarily, not only double-underscore names.
- Separate variable references, object identities, method retrieval, method calls, returned values, and state changes.
- Use per-instance energy initialized to 3. Training changes the Dragon attribute, not the immutable integer stored there; strings retain immutable contents.
- Keep type hints simple and explain that they are not runtime enforcement.
- Make repr informative about current state without claiming it is executable constructor code.
- Treat public-method filtering as appropriate for this simple class; explain that attribute access on arbitrary classes can run code.

## Scope and publication

All durable materials live in lessons/week_09. No other week is modified, no dependencies are installed, and no external APIs are used by the lab. The user's follow-up expressly authorizes committing and pushing these artifacts to GitHub main; the original prompt and that authorization are preserved in AUTHORING_PROMPT.md.
