# Do We Need an LLM to Know Why Sources Conflict?

Code, prompts and all model outputs for *Do We Need an LLM to Know Why Sources Conflict? Decision Models for Knowledge-Conflict Typing in RAG*
(Parv Khatri, Harshul Jain, Mehak Kapoor, Tanya Sah), [arXiv:2610.36915](https://arxiv.org/abs/2610.36915).

We evaluate every typed decision model served by one inference gateway (11 models from 7 providers) as a
classifier of knowledge-conflict types among retrieved sources on CONFLICTS
([Cattan et al., 2025](https://arxiv.org/abs/2506.08500)), using the original paper's prompt verbatim and comparing
against Gemini models on identical inputs.

| Test split, n = 406 | Accuracy | $ / 1k queries | Latency |
|---|---|---|---|
| 11 decision models, direct question | 50.0–67.0% (10 of 11 tie or beat Gemini 2.5 Flash) | 0–0.41 | 0.26–0.72 s |
| Gemini 2.5 Flash, paper's prompt | 61.3% | 1.66 | 1.55 s |
| Gemini 3.8 Flash, paper's prompt | 70.0% | 3.65 | 2.18 s |
| Decision model → Gemini 3.8 Flash cascade, 25% escalated | tied with Gemini 3.8 for 8 of 11 models | 25–37% of Gemini's | |

End to end, Gemini 2.5 Flash answers each query given a predicted conflict type, and an LLM judge (92% agreement
with two human annotators on 100 answers) checks the answer against the expected behaviour of the gold type:

| Type given to the generator | Answers with the expected behaviour |
|---|---|
| None (Vanilla) | 87.9% |
| Gemini 2.5 Flash's type (the original Pipeline) | 91.6% |
| A decision model's type | 87.7–92.4%; 10 of 11 models tied with the Pipeline |
| Gold type (Oracle) | 95.3% |

Per-model results are in `paper/generated/` and `runs/`.

Every setting and its evidence, including what was fixed before each run, is logged in
[`NOTES.md`](NOTES.md).

## What is in the repository

| Path | Contents |
|---|---|
| `src/dmconflict/` | Data and split, prompts, model clients, methods, cascade, perturbations, metrics, CLI |
| `runs/` | Every model output used in the paper, one JSON line per query (`<model>/<split>/<method>[@<perturbation>].jsonl`), the end-to-end answers and judge verdicts, and the generated result tables. Stored as `runs.nosync/` (the suffix keeps it out of iCloud sync); `runs` is a symlink to it |
| `data/splits.json`, `data/plants.json` | Frozen dev/test split; the wrong answers used for the planted-source diagnostic |
| `human_eval/` | Judge validation: the blind 100-answer sheet, the instructions given to annotators, and the two annotators' labels |
| `scripts/` | Data download, paper tables, figure, arXiv package |
| `paper/` | LaTeX source (TACL format); every number is generated from `runs/` |
| `tests/` | Unit tests (offline) |

## Reproduce the numbers without any API call

```bash
uv venv --python 3.11 .venv && uv pip install --python .venv -e ".[dev,plot]"
scripts/download_data.sh                                  # CONFLICTS, checksum-verified
.venv/bin/dmconflict evaluate --split test               # -> runs/comparison_test.md
.venv/bin/dmconflict cascade --split test                # -> runs/cascade_test.md
.venv/bin/dmconflict diagnose --split test               # -> runs/diagnostics_test.md
.venv/bin/dmconflict endtoend --split test               # -> runs/endtoend_test.md
.venv/bin/dmconflict agreement human_eval/behaviour_sample_1.csv human_eval/behaviour_sample_2.csv
.venv/bin/python scripts/make_tables.py                   # paper tables and numbers
.venv/bin/python -m pytest -q
```

## Rerun the models

Requests go through Vercel AI Gateway (decision models on `/v1/evaluate`, Gemini on the
OpenAI-compatible chat endpoint). Put `AI_GATEWAY_API_KEY=...` in `.env`, then for example:

```bash
.venv/bin/dmconflict run --method flat --model liquid/d1-ultra --split test   # any decision model, direct question
.venv/bin/dmconflict run --method tree --model liquid/d1-ultra --split test   # the same model, yes/no tree
.venv/bin/dmconflict run --method paper_llm_low --model google/gemini-3.8-flash --split test
.venv/bin/dmconflict run --method flat --model liquid/d1-ultra --split test --perturb shuffle1   # a diagnostic
.venv/bin/dmconflict generate --split test && .venv/bin/dmconflict judge --split test          # end to end
```

Runs resume, and new outputs go to `runs/`. Hosted models change over time and are not fully
deterministic (identical requests changed up to 9.4% of a decision model's predictions in our runs), so a rerun will not match
the released outputs exactly; the released outputs are the ones the paper reports.

## License

Code, prompts and model outputs are released under the [Apache License 2.0](LICENSE).
The CONFLICTS dataset keeps its own licence (below).

## Data

CONFLICTS is © Google, released under Apache-2.0 at
[google-research-datasets/rag_conflicts](https://github.com/google-research-datasets/rag_conflicts).
It is not redistributed here; `scripts/download_data.sh` fetches it and verifies its checksum.

## Citation

```bibtex
@misc{khatri2026needllm,
  title         = {Do We Need an {LLM} to Know Why Sources Conflict? Decision Models for Knowledge-Conflict Typing in {RAG}},
  author        = {Khatri, Parv and Jain, Harshul and Kapoor, Mehak and Sah, Tanya},
  year          = {2026},
  eprint        = {2610.36915},
  archivePrefix = {arXiv},
  primaryClass  = {cs.CL},
  doi           = {10.48550/arXiv.2610.36915},
  url           = {https://arxiv.org/abs/2610.36915}
}
```
