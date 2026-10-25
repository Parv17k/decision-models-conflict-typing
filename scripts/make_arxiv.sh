#!/usr/bin/env bash
# Builds the arXiv preprint from paper/: authors shown, no line numbers or "Confidential" header.
#
#   scripts/make_arxiv.sh
#
# Output in arxiv/:
#   source/            flat source tree, exactly what is uploaded (compiled once here to check it)
#   arxiv_source.tar.gz  the upload: main.tex sets \arxivversion itself, so arXiv needs no flags
#   preprint.pdf       the PDF arXiv should produce from the tarball
#   metadata.txt       title, authors, abstract (plain text, macros expanded), categories, comments
#
# arXiv does not run BibTeX reliably, so the .bbl is included; it must come from the same .bib.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
OUT="$ROOT/arxiv"
SRC="$OUT/source"

"$ROOT/.venv/bin/python" "$ROOT/scripts/make_tables.py"
rm -rf "$SRC" && mkdir -p "$SRC/sections" "$SRC/generated" "$SRC/figures"
cp "$ROOT/paper/tacl2021v1.sty" "$ROOT/paper/acl_natbib.bst" "$ROOT/paper/refs.bib" "$SRC/"
cp "$ROOT"/paper/sections/*.tex "$SRC/sections/"
cp "$ROOT"/paper/generated/*.tex "$ROOT"/paper/generated/*.txt "$SRC/generated/"
cp "$ROOT/paper/figures/cascade_cost_accuracy.pdf" "$SRC/figures/"
# The arXiv main.tex is the paper's main.tex with \arxivversion defined on its first line.
{ echo '\def\arxivversion{}'; cat "$ROOT/paper/main.tex"; } > "$SRC/main.tex"

cd "$SRC"
pdflatex -interaction=nonstopmode main >/dev/null 2>&1 || true
bibtex main >/dev/null
pdflatex -interaction=nonstopmode main >/dev/null 2>&1 || true
pdflatex -interaction=nonstopmode main > build.log 2>&1 || true
if grep -qE "^! " build.log; then grep -E "^! " build.log; echo "build failed"; exit 1; fi
if grep -qiE "undefined (references|citations)|Citation .* undefined|Reference .* undefined" build.log; then
  grep -iE "undefined" build.log; echo "unresolved references"; exit 1
fi
TODOS="$(grep -n '\\todo{' main.tex sections/*.tex | grep -v 'newcommand' || true)"
if [ -n "$TODOS" ]; then echo "WARNING: placeholders remain (orange [TODO] text in the PDF):"; echo "$TODOS"; fi
cp main.pdf "$OUT/preprint.pdf"
rm -f build.log main.aux main.blg main.log main.out main.pdf missfont.log

tar -czf "$OUT/arxiv_source.tar.gz" -C "$SRC" .
"$ROOT/.venv/bin/python" "$ROOT/scripts/arxiv_metadata.py" > "$OUT/metadata.txt"
echo "arXiv package: $OUT/arxiv_source.tar.gz ($(du -h "$OUT/arxiv_source.tar.gz" | cut -f1)), preview $OUT/preprint.pdf"
