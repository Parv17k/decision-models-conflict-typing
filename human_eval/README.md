# Judge validation: instructions for annotators

The end-to-end experiment scores generated answers with an automatic judge. Before its scores can be
reported, we check it against human judgements on 100 answers, as Cattan et al. did (their judge agreed
with humans on 89% of 100 answers).

You will label `behaviour_sample.csv`. It is **blind**: it does not show the judge's verdict, which
model or condition produced the answer, or anything else that could bias you. Please don't look at
`runs/human_eval_key_test.csv` or the judge outputs in `runs/` until you have finished.

## What to do

1. Make your own copy of the sheet (`behaviour_sample_1.csv`, `behaviour_sample_2.csv`, ...). Two
   annotators working independently is best (we then also report agreement between you); one is the
   minimum. Spreadsheet software is fine; keep the CSV format and the column names.
2. For each row, read the **query**, the **conflict type and expected behaviour**, and the
   **response**.
3. In `follows (1/0)`, write **1** if the response follows the expected behaviour for that conflict
   type, **0** if it does not. Use `notes` for anything unclear (optional).
4. Return the file. About 100 items at roughly a minute each.

You do not see the search results, and neither does the judge. Decide from the response itself
whether it handles the sources as the expected behaviour describes. Don't judge length, style or
writing quality, and don't check facts against your own knowledge.

## The five expected behaviours, with examples

The examples are from Cattan et al. (2025), Table 3, except No conflict, for which we wrote one pair.

**No conflict.** Give a clear and direct answer, without introducing alternative viewpoints or
uncertainty.
- 0: "Sources differ on when the Titanic set sail: some give 10 April 1912 [1][2], while another
  mentions 11 April 1912 [3]." (presents a related detail as a disagreement)
- 1: "The Titanic set sail from Southampton on its maiden voyage on 10 April 1912 [1][2]."

**Complementary information.** Consolidate and reconcile the different partial answers, without
framing the response as a debate.
- 0: *Who has the biggest airport?* Only the largest airport by land area.
- 1: Explains that "biggest" can mean land area or passenger traffic, and gives both.

**Conflicting opinions or research outcomes.** Explicitly reflect the debate between the sources and
summarise the viewpoints neutrally.
- 0: *Where did the hot dog originate?* Gives only the Chicago-style hot dog's origin.
- 1: Says the origin is debated, with Frankfurt's and Vienna's claims.

**Outdated information.** Prioritise the up-to-date information; mentioning outdated sources is
optional.
- 0: *How many people have been on the ISS?* Gives a 2022 figure and a different figure as if they
  were competing views.
- 1: Leads with the March 2024 figure and labels older figures as older.

**Misinformation.** Disregard inaccurate sources and answer from the reliable ones.
- 0: *When did season 5 of Prison Break come out?* "Premiered on April 4, 2017 [3]. The season was
  released on May 30, 2017 [4]." (tries to reconcile with an incorrect source)
- 1: "Season 5 of Prison Break premiered on April 4, 2017 [2][3]."

## After labelling

From the project root:

```bash
.venv/bin/dmconflict agreement human_eval/behaviour_sample_1.csv human_eval/behaviour_sample_2.csv
```

This prints the judge's accuracy and Cohen's kappa against the human labels (majority label when
there are two annotators), and the agreement between the two annotators.

## Files

| File | Contents |
|---|---|
| `behaviour_sample.csv` | The blind sheet as given to the annotators |
| `behaviour_sample_1.csv`, `behaviour_sample_2.csv` | The two annotators' labels |
| `behaviour_sample_llm_claude-sonnet-5.5.csv` | The same sheet labelled by Claude Sonnet 5.5 from these instructions (a third judge, not an annotator; `scripts/llm_annotator.py`) |

The key linking each item to its query, condition and judge verdict is `runs/human_eval_key_test.csv`.
