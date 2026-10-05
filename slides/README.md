# Slides

This directory holds instructor presentation source for COMSC-1033.

## Convention

- `NN_topic_slug.tex` — presentation source associated with `lessons/NN-topic-slug.md`.
- `_template.tex` — small compile-ready Beamer chassis. Copy its structure rather than growing it into a second lesson source.
- `build.sh` — one-command local compile helper.

The canonical teaching content stays in `lessons/`. Slides are a presentation layer and should not become the only place an explanation exists.

## Design defaults

- 16:9
- large type
- sparse slides
- one question, example, diagram, or punchline per frame when practical
- Python code uses `listings`, not `minted`, so normal LaTeX compilation does not require shell escape
- add `[fragile]` to frames containing code listings
- prefer live coding to dense code walls

## Build

From the repository root:

```bash
bash slides/build.sh
```

That compiles `slides/_template.tex` by default.

To compile a lesson deck:

```bash
bash slides/build.sh slides/06_strings_are_objects.tex
```

The script prefers `latexmk` and falls back to two `pdflatex` passes.

Generated PDFs and LaTeX build debris should not be treated as canonical source.
