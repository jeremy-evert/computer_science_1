# 016 — CS1 "Strings Are Objects": Phases 1-3 landed, Phase 4 prep reconciled (2026-10-05)

Run de45afbdfadd4667ee71cffa9e71de8f (Flo, seat claude-top, Brandy).

## Found
- Phases 1-3 existed ONLY as local worktrees on Maise (`/mnt/nora/git/computer_science_1-strings-p{1,2,3}`), not on GitHub. Only `codex/strings-phase4-prep` was on origin. `origin/main` was at `f647e1f` (an ancestor of the prep branch).
- Phase 3 (`codex/strings-phase3`, tip `4a9134a`) already contains Phase 1 and 2 by cherry-pick (`0ff9626`, `e0d3856`; it also keeps an earlier "Phase 3 blocked by missing prerequisites" commit `0a4c1c4` and a first Phase 2 build `63ed7a0`, as history). Treated as canonical for Phases 1-3; the three phase branches were NOT independently merged.

## Done
- Pushed `codex/strings-phase1` (b63c980), `codex/strings-phase2` (60f5228 on Maise's p2 tip), `codex/strings-phase3` (4a9134a) to origin from Maise, unmodified, so nothing is stranded.
- Branch `flo/strings-landing` = phase3 + merge of `origin/codex/strings-phase4-prep` (clean, no conflicts; adds `slides/_template.tex`, `slides/README.md`, `slides/build.sh`, Phase 4 readiness + Codex prompt). All breadcrumb/status files preserved.
- Fast-forwarded `main` to the result (main was an ancestor).

## Validation
- `py_compile` OK for `lessons/code/strings_mad_lib.py`, `string_lab.py`; `strings_mad_lib.py` ran end-to-end with scripted input; `string_lab.py` ran and printed its demos. `git diff --check` clean.
- Beamer: `bash slides/build.sh` (pdflatex, TeX Live 2025 on Brandy; no latexmk) built `slides/_template.pdf`, 5 pages, PASS. Build artifacts deleted, not committed.
- Not re-run by Flo: Phase 3's own claimed validation of fenced snippets/links/terminology; `lessons/06-strings.md` is 292 lines.

## Not done / remains
- The Phase 4 deck `slides/06_strings_are_objects.tex` does NOT exist yet. Instructions: `planning/2026-10-05_strings_are_objects_phase_04_codex_prompt.md`. One phase, one session, breadcrumb, validate, commit, stop. Phase 5 not started.
- Canvas: the repo lesson is not itself on Canvas; the live Canvas page `06-strings` (module 218511) is still the old stub. Publishing is a separate Anna step.
- Wilbur breadcrumb sidequest (`jeremy_task_tracking/tasks/2026-10-05_wilbur_phase_breadcrumb_sidecar.md`) not touched; evidence preserved in the status files.
