# Imagegen for the Triple Humanoid 4-Site Paper (v0.8.0)

[![Demo](https://img.shields.io/badge/Demo-07-brightgreen.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/blob/main/demo-projects/07-humanoid-24-7-adverse-event-response.md)
[![Release](https://img.shields.io/badge/Release-v0.8.0-brightgreen.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)
[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.18445179-blue)](https://doi.org/10.5281/zenodo.18445179)
[![Prior DOI](https://img.shields.io/badge/Prior%20DOI-10.5281%2Fzenodo.18029100-blue)](https://doi.org/10.5281/zenodo.18029100)
[![Images](https://img.shields.io/badge/Images-17%20at%20300%20dpi-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/tree/main/demo-projects/07-humanoid/paper/imagegen)
[![Instructions](https://img.shields.io/badge/Instructions-10%20of%2010-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/tree/main/demo-projects/image-instruct/07-adverse-event-response)
[![Figures](https://img.shields.io/badge/Figures-7%20of%207-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/tree/main/demo-projects/07-humanoid/paper/full-paper)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-3.10-blue.svg)](https://matplotlib.org)
[![Python](https://img.shields.io/badge/Python-3.10%20|%203.11%20|%203.12-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![CI](https://img.shields.io/badge/CI-ruff%20+%20format%20+%20yamllint-brightgreen.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/blob/main/.github/workflows/ci.yml)

This folder carries the 17 publication-quality matplotlib scripts and 300 dpi PNG renders that the v0.8.0 release adds to the Demo 07 paper tree. The renders polish the paper "Triple Humanoid 24/7 Adverse Event Oncology Trial Response Team: 4-Site Rotation" by Kevin Kawchak (ORCID 0009-0007-5457-8667).

## Coverage

- 10 image-instruct renders at `instructions/` that materialize the 10 image briefs at `demo-projects/image-instruct/07-adverse-event-response/`.
- 7 paper-figure replacements at `figures/` that supersede the verbatim ASCII figures previously inlined in `paper/full-paper/sections/` (Figure 3 was authored with extra detail since the ASCII version lacked impact).

The v0.8.0 release does not modify `paper/full-paper/`. The PNGs are reference-quality drop-ins so a future paper edit can swap `\begin{Verbatim} ... \end{Verbatim}` for `\includegraphics[width=\textwidth]{imagegen/figures/fig-XX-...}`.

## Output Inventory

### Instructions (10 images, image-instruct-aligned)

| # | Script | PNG | Orientation | Subject |
|---|--------|-----|-------------|---------|
| 01 | [`instructions/07-01-system-architecture-control-loop.py`](instructions/07-01-system-architecture-control-loop.py) | [`07-01-...png`](instructions/07-01-system-architecture-control-loop.png) | Landscape | 4-site PAT-NET-001 system architecture + SLA timeline |
| 02 | [`instructions/07-02-operational-timeline-gantt.py`](instructions/07-02-operational-timeline-gantt.py) | [`07-02-...png`](instructions/07-02-operational-timeline-gantt.png) | Landscape | 168-hour Gantt: per-site LLM ticks + H2 rotation + AE events |
| 03 | [`instructions/07-03-regulatory-compliance-heatmap.py`](instructions/07-03-regulatory-compliance-heatmap.py) | [`07-03-...png`](instructions/07-03-regulatory-compliance-heatmap.png) | Landscape | 10 AE phases x 14 frameworks heatmap + 4-site sub-heatmap |
| 04 | [`instructions/07-04-value-proposition-canvas.py`](instructions/07-04-value-proposition-canvas.py) | [`07-04-...png`](instructions/07-04-value-proposition-canvas.png) | Portrait | Strategyzer-style value-fit canvas + metrics table |
| 05 | [`instructions/07-05-financial-assessment-waterfall.py`](instructions/07-05-financial-assessment-waterfall.py) | [`07-05-...png`](instructions/07-05-financial-assessment-waterfall.png) | Portrait | 16-bar 5-year network TCO waterfall (USD thousands) |
| 06 | [`instructions/07-06-capability-radar-comparison.py`](instructions/07-06-capability-radar-comparison.py) | [`07-06-...png`](instructions/07-06-capability-radar-comparison.png) | Portrait | 8-axis radar across 4 humanoid + LLM configurations |
| 07 | [`instructions/07-07-sankey-flow-diagram.py`](instructions/07-07-sankey-flow-diagram.py) | [`07-07-...png`](instructions/07-07-sankey-flow-diagram.png) | Portrait | 4-level Sankey: source site to terminal action |
| 08 | [`instructions/07-08-process-funnel-chart.py`](instructions/07-08-process-funnel-chart.py) | [`07-08-...png`](instructions/07-08-process-funnel-chart.png) | Portrait | 7-stage AE lifecycle funnel + per-stage pass rate |
| 09 | [`instructions/07-09-strategic-quadrant-matrix.py`](instructions/07-09-strategic-quadrant-matrix.py) | [`07-09-...png`](instructions/07-09-strategic-quadrant-matrix.png) | Portrait | 2x2 strategic quadrant + 8 bubble configurations |
| 10 | [`instructions/07-10-decision-tree-flowchart.py`](instructions/07-10-decision-tree-flowchart.py) | [`07-10-...png`](instructions/07-10-decision-tree-flowchart.png) | Portrait | Cross-site rotation decision tree with transit modality |

### Figures (7 images, full-paper replacements)

| # | Script | PNG | Orientation | Replaces |
|---|--------|-----|-------------|----------|
| 1 | [`figures/fig-01-network-layout.py`](figures/fig-01-network-layout.py) | [`fig-01-network-layout.png`](figures/fig-01-network-layout.png) | Landscape | `introduction.tex` PAT-NET-001 continental network ASCII |
| 2 | [`figures/fig-02-execution-sequence.py`](figures/fig-02-execution-sequence.py) | [`fig-02-execution-sequence.png`](figures/fig-02-execution-sequence.png) | Landscape | `introduction.tex` 4-site execution sequence ASCII |
| 3 | [`figures/fig-03-swarm-dance.py`](figures/fig-03-swarm-dance.py) | [`fig-03-swarm-dance.png`](figures/fig-03-swarm-dance.png) | Landscape | `methods.tex` Camarade Swarm Dance ASCII (extra detail authored) |
| 4 | [`figures/fig-04-iteration-funnel.py`](figures/fig-04-iteration-funnel.py) | [`fig-04-iteration-funnel.png`](figures/fig-04-iteration-funnel.png) | Portrait | `methods.tex` 32-iteration sweep funnel ASCII |
| 5 | [`figures/fig-05-module-dependency.py`](figures/fig-05-module-dependency.py) | [`fig-05-module-dependency.png`](figures/fig-05-module-dependency.png) | Portrait | `methods.tex` per-site module dependency ASCII |
| 6 | [`figures/fig-06-ae-response-flow.py`](figures/fig-06-ae-response-flow.py) | [`fig-06-ae-response-flow.png`](figures/fig-06-ae-response-flow.png) | Landscape | `methods.tex` AE response swimlane ASCII |
| 7 | [`figures/fig-07-comparison-radar.py`](figures/fig-07-comparison-radar.py) | [`fig-07-comparison-radar.png`](figures/fig-07-comparison-radar.png) | Landscape | `results.tex` weighted comparison radar ASCII |

## Shared Conventions

- 300 dpi, white facecolor, DejaVu Sans typography, no dark mode.
- Letter portrait 8.5 x 11.0 in (2550 x 3300 px) and letter landscape 11.0 x 8.5 in (3300 x 2550 px) per the image-instruct briefs.
- Color palette: Deep Navy `#1F3A68`, Teal `#2E8B8B`, Burgundy `#8B2E3F`, Gold `#C18A2C`, Forest Green `#2F6B3E`, Slate `#4A5568`, Mauve `#8B6B8B`, Light Gray `#E2E8F0`, Off-White `#F7FAFC`. Variants (lt, dk, md) carry small luminance shifts of the base color.
- Single dashes only. No em dash, no double dash, no triple dash. `§` used for HIPAA, CFR, and similar references.
- Every figure carries a top-right tag (image number for instructions, figure number for paper figures), a footer-left repository attribution, and a footer-right DOI plus License.
- Black body text for readability against the white background.

## Pipeline

```
demo-projects/image-instruct/07-adverse-event-response/      v0.2.0 image briefs (10 MD files)
            |
            v
demo-projects/07-humanoid/paper/imagegen/instructions/       v0.8.0 (10 .py + 10 .png) renders
demo-projects/07-humanoid/paper/imagegen/figures/            v0.8.0 (7 .py + 7 .png) replacements
            |
            v
demo-projects/07-humanoid/paper/full-paper/                  v0.7.0 LaTeX (consumes PNGs in a future edit)
```

## Reproduce Locally

```bash
# From repository root, with Python 3.10 / 3.11 / 3.12 + matplotlib 3.10
pip install matplotlib numpy
for f in demo-projects/07-humanoid/paper/imagegen/instructions/*.py \
         demo-projects/07-humanoid/paper/imagegen/figures/*.py; do
  python3 "$f"
done

# CI compliance check
pip install ruff yamllint
ruff check .
ruff format --check .
yamllint -d relaxed .github/
```

## Layout Notes

Each script is single-file standalone (no shared helper imports across the imagegen tree). The palette is duplicated at the top of every script so each script can be run alone from its own directory without breaking. The matplotlib backend is forced to `Agg` so the scripts render headless on Linux, MacOS, and Windows CI runners.

## Style and Formatting Notes

- Section sign `§` is used for HIPAA Safe Harbor `45 CFR § 164.514(b)`, CFR Title 21 sections (`21 CFR § 312`, `§ 314.80`, `§ 50`), and IEC standards. No `SS` digraph anywhere.
- Single dashes only throughout titles, callouts, legends, and annotations.
- Time markers use single-letter prefixes `t+0s`, `t+30s` for the AE swimlane; no `t-` style markers.
- Money amounts use the `$N,Nk` convention (USD thousands) so the bar labels stay short.
- 1 commit per image landed inside the single v0.8.0 PR. The 2nd-to-last commit is reserved for ruff format pass and placeholder cleanup. The last commit is reserved for repository-wide documentation updates.

## License

MIT License (see [LICENSE](../../../../LICENSE)).
