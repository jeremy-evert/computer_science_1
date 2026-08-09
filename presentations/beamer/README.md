# Computer Science 1 — Monday lecture Beamer decks

Slides-only compile (2-pass, same as every other deck in this project):

```bash
cd week_02_mon
pdflatex -interaction=nonstopmode -halt-on-error week02_mon.tex
pdflatex -interaction=nonstopmode -halt-on-error week02_mon.tex
```

(run twice — the second pass resolves outline/bookmark references; a
`rerunfilecheck` warning on the first pass alone is harmless and expected.)

Instructor copy with speaker notes on a second screen:

```bash
pdflatex "\PassOptionsToPackage{show}{pgfpages}\input{week02_mon.tex}"
```

All decks share `theme/preamble.tex` — edit it once there, not per-week.
Vendored from `professional_minds/presentations/beamer/theme/preamble.tex`
(the same pattern `semester_kickoff_week/presentations/beamer/` already
uses), kept local so this repo stays self-contained without a
`professional_minds` checkout.

## Build artifacts

`pdflatex` intermediate files (`.aux`, `.log`, `.nav`, `.out`, `.snm`,
`.toc`, and `.vrb` — the last only appears when a deck uses `[fragile]`
frames with literal `verbatim` code blocks, as `week_02_mon` does) are not
committed — only `.tex` source and the compiled `.pdf` are canonical. Clean
a deck's directory with:

```bash
rm -f *.aux *.log *.nav *.out *.snm *.toc *.vrb
```

## Coverage

`week_02_mon/week02_mon.tex` — Week 2's Monday technical lecture,
"Variables, Expressions, and Types" (content source:
`lessons/02-variables-expressions-types.md`). Pilot deck, built
2026-08-08/09 to test the pattern before the other 13 technical weeks'
Monday decks are built — see `jeremy_task_tracking/reports/` for the pilot
report and Jeremy's go/no-go read on greenlighting the rest.

Every other technical week (3–16) has no deck yet — same reason
`professional_minds`' later weeks didn't all launch at once: content gets
built and reviewed one real unit at a time, not 14 weeks blind.
