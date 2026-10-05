#!/usr/bin/env bash
set -euo pipefail

target="${1:-slides/_template.tex}"

if [[ ! -f "$target" ]]; then
  echo "ERROR: Beamer source not found: $target" >&2
  exit 2
fi

outdir="$(dirname "$target")"
name="$(basename "$target" .tex)"

echo "Building $target"

if command -v latexmk >/dev/null 2>&1; then
  latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir="$outdir" "$target"
elif command -v pdflatex >/dev/null 2>&1; then
  pdflatex -interaction=nonstopmode -halt-on-error -output-directory="$outdir" "$target"
  pdflatex -interaction=nonstopmode -halt-on-error -output-directory="$outdir" "$target"
else
  echo "ERROR: neither latexmk nor pdflatex is installed." >&2
  exit 3
fi

pdf="$outdir/$name.pdf"
if [[ ! -s "$pdf" ]]; then
  echo "ERROR: expected PDF was not produced: $pdf" >&2
  exit 4
fi

echo "PASS: $pdf"
