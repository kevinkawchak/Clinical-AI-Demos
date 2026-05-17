# Authoring Instructions for `notebooks/run_log.ipynb`

The future session writes this Jupyter notebook during Commit 4 of 7.

## Purpose

The canonical run log. Documents one full 168-hour 4-site 32-iteration run including command counts, AE counts, escalation counts, and camaraderie metrics. Read by humans for post-hoc analysis.

## Required Cells

1. Title and overview markdown.
2. Iteration parameter table from `data/iterations/index.jsonl`.
3. Aggregate metrics from `data/aggregate.duckdb`.
4. Per-site response time histograms (matplotlib).
5. Camaraderie invariants pass-rate barplot.
6. Role rotation timeline for a representative AE.
7. Peer handoff p95 distribution.
8. Footnotes referencing relevant FDA RTCT and HR 9504/9505 sources.

## Notebook Conventions

- Python 3.10 compatible.
- Imports: `duckdb`, `pandas`, `matplotlib`, `pyarrow`.
- Backend: `matplotlib.use("Agg")` so the notebook can run headless.
- All figures saved to `reports/figures/` at 300 dpi.

## Validation Rules

- Notebook runs end to end with `nbconvert --execute`.
- All figures rendered to PNG.
- No PHI in any cell output.

## Notes

- The notebook also acts as a smoke test in commit 6: `jupyter nbconvert --execute notebooks/run_log.ipynb`.
- The notebook is the entry point for the comparison framework in commit 5.
