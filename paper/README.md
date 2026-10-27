# Paper (TACL format)

Target: *Transactions of the ACL*, regular paper. Template `tacl2021v1.sty` + `acl_natbib.bst`, the
official files from https://transacl.org/tacl-submission-templates/ (still the latest, Dec 2021; the
copy on direct.mit.edu is the older 2018 version). The untouched template, sample .bib and the submission and
final-version formatting instructions are not redistributed here; download them from that page.

Length rules (TACL announcement of 2024-02-16, effective 2024-03-01, which supersedes the template's
"appendices count" rule): 10 pages of content; references don't count; appendices go after the
references, outside the limit: up to 5 pages of replication details (prompts, parameters, protocol)
and up to 3 pages of complementary tables/figures referenced from the paper; no free text in
appendices beyond replication details; appendices are not reviewed.

## Build

```bash
.venv/bin/python scripts/make_tables.py        # from the project root: tables + numbers from the stored runs
.venv/bin/python scripts/plot_cascade.py                  # also writes paper/figures/cascade_cost_accuracy.pdf
cd paper && pdflatex main && bibtex main && pdflatex main && pdflatex main
```

No number in the text is typed by hand: tables come from `generated/tab_*.tex`, numbers from
`generated/numbers.tex` (macros such as `\dmaccmax`), prompts from `generated/*.txt`.

## Three versions from one source

| Version | Command | Shows |
|---|---|---|
| TACL submission | `cd paper && pdflatex main && bibtex main && pdflatex main && pdflatex main` | anonymous, line numbers, "Confidential" header |
| Camera-ready preview | `cd paper && pdflatex -jobname=main_final "\def\taclfinal{}\input{main}"` (+ bibtex `main_final`) | authors |
| arXiv preprint | `scripts/make_arxiv.sh` (from the project root) | authors, no line numbers or header |

`scripts/make_arxiv.sh` writes `arxiv/arxiv_source.tar.gz` (the upload, with the pre-built `.bbl`
arXiv needs and LaTeX comments stripped, since arXiv publishes the source), `arxiv/preprint.pdf` (what arXiv should produce) and `arxiv/metadata.txt` (title,
authors, plain-text abstract, categories). It stops on any LaTeX error or unresolved reference and
warns about remaining `\todo` placeholders.

Authors, in order: Parv Khatri (first and lead author), Harshul Jain, Mehak Kapoor, Tanya Sah.

## Fonts

BasicTeX lacks Helvetica, which the TACL style uses for the review line numbers. Installed in user
mode (no sudo) into ~/Library/texmf:

```bash
tlmgr init-usertree && tlmgr --usermode install helvetic courier
```

## Before submission

- Re-check https://transacl.org/index.php/tacl/about/submissions for rule changes.
- For each cited preprint, check whether a peer-reviewed version has appeared (a listed TACL desk-reject reason).
- The anonymous build sets only the PDF title, no authors (checked). Name the file
  `<submission number>-<1-3 title words>.pdf`.
- No supplementary material or links to it: state anonymously that code and data will be released.
- Authors stay anonymous in the submission format; switch to `\usepackage[acceptedWithA]{tacl2021v1}` for the final version.
- Re-check arXiv for new work on decision models and knowledge conflicts.
- TACL allows an arXiv preprint during review, but it must be disclosed in "Comments to the Editor",
  and the submission must not cite it.
