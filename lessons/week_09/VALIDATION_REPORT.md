# Validation report

Validated on 2026-10-12 using Python 3. All seven scripts passed. No validation failures were found.

## Independent execution

Each script was launched in its own process using `python3` with an absolute script path and `/tmp` as its working directory. This verifies independence from the lesson directory and prior lesson executions. All exited normally, produced labeled output, required no input, and wrote no files. None contains imports or file reads.

| Script | Exit code | Stderr | Output lines |
| --- | --- | --- | --- |
| 01_strings_are_objects.py | 0 | None | 14 |
| 02_objects_have_behavior.py | 0 | None | 21 |
| 03_exploring_objects.py | 0 | None | 24 |
| 04_exploring_the_string_class.py | 0 | None | 25 |
| 05_building_a_dragon_class.py | 0 | None | 18 |
| 06_creating_dragon_objects.py | 0 | None | 32 |
| 07_making_objects_discoverable.py | 0 | None | 31 |

Full captured output is preserved in [VALIDATION_OUTPUT.txt](VALIDATION_OUTPUT.txt). Identity numbers are evidence from one run, not expected constants.

## Structure and accuracy review

- All requested fifteen files exist, with the exact requested filenames.
- Every script begins with a module docstring covering lesson/title, goal, prerequisites, three ideas, and previous-lesson connection.
- Every guide has nine required sections, no more than four vocabulary entries, two or three challenges, and explicit references to its script.
- Automated checks matched script output section headings to guide experiment headings and checked local Markdown links.
- Reviewed the guide predictions and expected outputs against all seven captured runs.
- Confirmed strings remain unchanged after method calls and that reassignment is explained separately.
- Confirmed class/instance distinctions, initialization versus creation, self, data versus methods, and returned values versus state changes.
- Confirmed Clay's energy changes from 3 to 2 while Tsunami remains at 3; both instances remain alive with distinct identities and matching classes.
- Confirmed the final public attributes include data and methods; the public-method filter returns introduce and train.
- Confirmed help tours are interactive exercises, while normal output uses compact documentation excerpts. Full dir output is also available interactively.
- Reviewed dir/hasattr limitations, type-hint limitations, representation explanations, and the class/instance string call comparison.
- Checked the practice/shared-discussion framing against course rules.

## Reproduce execution

From week_09, run the seven commands listed in 00_README.md, or use this standard-library snippet for independent runs:

```python
from pathlib import Path
import subprocess

for script in sorted(Path.cwd().glob("[0-9][0-9]_*.py")):
    result = subprocess.run(
        ["python3", str(script)], cwd="/tmp",
        capture_output=True, text=True, timeout=10,
    )
    assert result.returncode == 0, result.stderr
    assert not result.stderr
    print(script.name, "PASS")
```

To reproduce interactive documentation checks, use the mini-labs in guides 03, 04, and 07. The normal-run validation does not automate a terminal pager session.

## Durable artifact inventory

- 00_README.md, plus seven numbered .py scripts and seven matching .md learning guides.
- README.md: local/GitHub entry point.
- AUTHORING_PROMPT.md: original user request and follow-up publication authorization.
- COURSE_CONTEXT.md: instruction provenance and design decisions.
- VALIDATION_REPORT.md and VALIDATION_OUTPUT.txt: review results and execution evidence.
