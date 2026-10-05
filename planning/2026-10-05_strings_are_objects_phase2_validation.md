# Strings Are Objects — Phase 2 validation

Completed Phase 2 only: `lessons/code/string_lab.py` is a directly runnable,
beginner-oriented demonstration of all ten planned methods, dot notation,
immutability, `type(text)`, `dir(text)`, and `help(str.replace)`.

Validation commands (from the repository root):

```bash
python3 lessons/code/string_lab.py
git diff --check
```

Both passed. The output was inspected: `name.upper()` leaves `name` as
`jeremy`; `name = name.upper()` makes it `JEREMY`. The original laboratory
text also retains its surrounding spaces and capitalization after all calls.

For Phase 3: use the tested script as source material. Highlight that methods
return different types (`str`, `list`, `int`, and `bool`), that surrounding
spaces affect prefix/suffix checks, and that reassignment changes what a
variable refers to rather than modifying a string's contents. Mixed capitals
make the effect of `title()` visible. `dir()` includes special names; beginners
can start with familiar method names and consult focused method help.

Context discrepancy: this Phase 2 branch did not contain the Phase 1 Mad Lib.
The completed file was read from the Phase 1 worktree at
`../computer_science_1-strings-p1/lessons/code/strings_mad_lib.py`, where it was
untracked at inspection time. Phase 2 follows its existing `lessons/code/`
placement. Ensure that Phase 1 is committed and available before Phase 3.
The shared `../AGENTS.md` referenced by the repository rules was missing;
the available repository instructions and course design rules were read.

The canonical lesson and presentation were not changed. No Phase 3 work was
started.
