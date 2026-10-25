# Fast Judgments on Conflicting Sources

Code, prompts and all model outputs for *Fast Judgments on Conflicting Sources: The Typed Decision
Model Jev as a Knowledge-Conflict Classifier for Retrieval-Augmented Generation*
(Parv Khatri, Harshul Jain, Tanmay Sah, Mehak Kapoor, Tanya Sah).

We evaluate the typed decision model Jev as a classifier of knowledge-conflict types among
retrieved sources on CONFLICTS ([Cattan et al., 2025](https://arxiv.org/abs/2506.08500)), using the
original paper's prompt verbatim and comparing against Gemini models on identical inputs.

| System (test split, n = 406) | Accuracy | $ / 1k queries | Latency |
|---|---|---|---|
| Jev 1.13, direct question | 61.8% | 0.19 | 0.26 s |
| Gemini 2.5 Flash, paper's prompt | 61.3% | 1.66 | 1.55 s |
| Gemini 3.8 Flash, paper's prompt | 70.0% | 3.65 | 2.18 s |
| Jev → Gemini 3.8 Flash cascade, 25% escalated | 68.5% | 1.09 | 0.81 s |

Every setting and its evidence, including what was fixed before each run, is logged in
[`NOTES.md`](NOTES.md).

## What is in the repository

| Path | Contents |
|---|---|
| `src/jevconflict/` | Data and split, prompts, model clients, methods, cascade, perturbations, metrics, CLI |
| `runs/` | Every model output used in the paper, one JSON line per query (`<model>/<split>/<method>[@<perturbation>].jsonl`), and the generated result tables |
| `data/splits.json`, `data/plants.json` | Frozen dev/test split; the wrong answers used for the planted-source diagnostic |
| `scripts/` | Data download, paper tables, figure, arXiv package |
| `paper/` | LaTeX source (TACL format); every number is generated from `runs/` |
| `tests/` | Unit tests (offline) |

## Reproduce the numbers without any API call

```bash
uv venv --python 3.11 .venv && uv pip install --python .venv -e ".[dev,plot]"
scripts/download_data.sh                                  # CONFLICTS, checksum-verified
.venv/bin/jevconflict evaluate --split test               # -> runs/comparison_test.md
.venv/bin/jevconflict cascade --split test                # -> runs/cascade_test.md
.venv/bin/jevconflict diagnose --split test               # -> runs/diagnostics_test.md
.venv/bin/python scripts/make_tables.py                   # paper tables and numbers
.venv/bin/python -m pytest -q
```

## Rerun the models

Requests go through Vercel AI Gateway (decision models on `/v1/evaluate`, Gemini on the
OpenAI-compatible chat endpoint). Put `AI_GATEWAY_API_KEY=...` in `.env`, then for example:

```bash
.venv/bin/jevconflict run --method flat --split test                       # Jev 1.13, direct question
.venv/bin/jevconflict run --method tree --split test                       # Jev 1.13, yes/no tree
.venv/bin/jevconflict run --method paper_llm_low --model google/gemini-3.8-flash --split test
.venv/bin/jevconflict run --method flat --split test --perturb shuffle1   # a diagnostic
```

Runs resume, and new outputs go to `runs/`. Hosted models change over time and are not fully
deterministic (identical requests changed 2–3% of predictions in our runs), so a rerun will not match
the released outputs exactly; the released outputs are the ones the paper reports.

## Data

CONFLICTS is © Google, released under Apache-2.0 at
[google-research-datasets/rag_conflicts](https://github.com/google-research-datasets/rag_conflicts).
It is not redistributed here; `scripts/download_data.sh` fetches it and verifies its checksum.

## Citation

```bibtex
@misc{khatri2026fastjudgments,
  title  = {Fast Judgments on Conflicting Sources: The Typed Decision Model {Jev} as a Knowledge-Conflict Classifier for Retrieval-Augmented Generation},
  author = {Khatri, Parv and Jain, Harshul and Sah, Tanmay and Kapoor, Mehak and Sah, Tanya},
  year   = {2026},
  note   = {arXiv identifier to be added}
}
```
