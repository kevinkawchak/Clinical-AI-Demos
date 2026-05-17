# Image Instructions for Clinical-AI-Demos Demo Projects

[![Image Instructions](https://img.shields.io/badge/Image%20Instructions-100-brightgreen.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/tree/main/demo-projects/image-instruct)
[![Prompts](https://img.shields.io/badge/Prompts-10-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/tree/main/demo-projects)
[![Companion](https://img.shields.io/badge/Companion-physical--ai--oncology--trials-purple.svg)](https://github.com/kevinkawchak/physical-ai-oncology-trials)
[![DPI](https://img.shields.io/badge/DPI-300-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)
[![Format](https://img.shields.io/badge/Format-PNG-orange.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)
[![Library](https://img.shields.io/badge/Library-matplotlib-blueviolet.svg)](https://matplotlib.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Released on 17 May 2026
CEO Kevin Kawchak, ChemicalQDevice

This directory holds 100 image instruction Markdown files. Each instruction is a self-contained specification that a future Claude Code Opus 4.7 1M Max session reads to author one professionally coded matplotlib Python script and emit one 300 dpi PNG output. The instructions cover the 10 demo prompts at `demo-projects/01-...md` through `demo-projects/10-...md`, with 10 instructions per prompt (3 landscape full-page plus 7 portrait letter).

## Purpose

The 10 prompts at `demo-projects/` are not yet executed. The downstream Claude Code Opus 4.7 1M Max sessions that execute those prompts will author Parquet, CSV, JSONL, and Markdown outputs at scale; they will also need a small set of publication-ready figures per demo for the Markdown reports, the comparison decks, and the v0.2.0 through v1.1.0 release notes. This directory provides those figure specifications up front so the future sessions can run the matplotlib authoring step deterministically with no positioning work left to the author.

## Scope Per Prompt

Every prompt receives the same fixed set of 10 chart types, tuned to that prompt's humanoid + LLM context. The fixed set is:

| # | Chart Type | Page | Orientation | Theme Focus |
|---|------------|------|-------------|-------------|
| 01 | System Architecture and Control Loop Diagram | Letter | Landscape | Humanoid + LLM + sensors + actuators + safety arbiter |
| 02 | Operational Timeline / Gantt Swimlane Chart | Letter | Landscape | Shift or procedure timeline with parallel work streams |
| 03 | Regulatory and Risk Compliance Heatmap Matrix | Letter | Landscape | Frameworks x phases x severity |
| 04 | Value Proposition Canvas | Letter | Portrait | Stakeholder jobs, pains, gains; pain relievers, gain creators |
| 05 | Financial Assessment Waterfall Chart | Letter | Portrait | 5-year TCO buildup or per-procedure margin walk |
| 06 | Capability Radar / Spider Chart | Letter | Portrait | Humanoid + LLM stack vs. 3 baselines on 6-8 axes |
| 07 | Sankey Flow Diagram | Letter | Portrait | Inputs to outputs (patient, data, IMP, dose, biospecimen) |
| 08 | Process Funnel Chart | Letter | Portrait | Sequential filter stages with conversion percentages |
| 09 | Strategic Quadrant Bubble Matrix | Letter | Portrait | 2x2 with bubbles sized by deployment scale |
| 10 | Decision Tree Flowchart | Letter | Portrait | Trigger + branches + actions with regulatory exit conditions |

3 of the 10 (01, 02, 03) are full-page landscape Letter at 11 x 8.5 inches. 7 of the 10 (04 through 10) are portrait Letter at 8.5 x 11 inches.

## Directory Structure

```
demo-projects/image-instruct/
  README.md                                          # This file
  01-site-operations-director/                       # Prompt 01 (Atlas + Claude Opus 4.7)
    01-system-architecture-control-loop.md           # Landscape
    02-operational-timeline-gantt.md                 # Landscape
    03-regulatory-compliance-heatmap.md              # Landscape
    04-value-proposition-canvas.md                   # Portrait
    05-financial-assessment-waterfall.md             # Portrait
    06-capability-radar-comparison.md                # Portrait
    07-sankey-flow-diagram.md                        # Portrait
    08-process-funnel-chart.md                       # Portrait
    09-strategic-quadrant-matrix.md                  # Portrait
    10-decision-tree-flowchart.md                    # Portrait
  02-sponsor-operations-center/                      # Prompt 02 (5x Optimus + Sonnet/Opus)
  03-pharmacy-imp-compounding/                       # Prompt 03 (Figure 03 + GPT-5.5 Thinking)
  04-post-op-recovery-nurse/                         # Prompt 04 (Digit V5 + Haiku/Sonnet/Llama 4)
  05-biospecimen-pathology-lab/                      # Prompt 05 (Phoenix Gen 8 + Gemini/Qwen via MCP)
  06-tele-surgical-assistant/                        # Prompt 06 (Apollo + Claude Opus + Operator)
  07-adverse-event-response/                         # Prompt 07 (3x H2 + per-site Claude Opus)
  08-clinical-research-coordinator/                  # Prompt 08 (Neo Beta + Claude+Gemini+GPT)
  09-radiation-oncology-technologist/                # Prompt 09 (Atlas+Optimus pair + GR00T+Cosmos+Claude)
  10-decentralized-home-care/                        # Prompt 10 (Figure Field + Claude Haiku edge)
```

## Output File Naming Convention

Each instruction emits one PNG. Naming convention for the future generated outputs (not generated by this PR):

```
demo-projects/NN-name-output/figures/NN-NN-short-name.png
```

Examples:

- `demo-projects/01-humanoid-site-operations-director-output/figures/01-01-system-architecture-control-loop.png`
- `demo-projects/06-humanoid-tele-surgical-assistant-output/figures/06-05-financial-assessment-waterfall.png`
- `demo-projects/10-humanoid-decentralized-home-care-output/figures/10-10-decision-tree-flowchart.png`

## Python Script Conventions

Each instruction expects a Python script of the form `figures/render_NN_NN_short_name.py`. The future author writes one script per figure. Required conventions for every script:

- Python 3.10+ compatible (matches the CI matrix on 3.10, 3.11, 3.12).
- One import block at the top: `matplotlib`, `matplotlib.pyplot`, `numpy`, `pathlib.Path`. No seaborn, no plotly, no bokeh, no plotnine, no ggplot.
- Set matplotlib backend to `Agg` explicitly via `matplotlib.use("Agg")` before `pyplot` import.
- Use only the matplotlib default font family `DejaVu Sans` (always available on the CI runners). No custom font installs.
- Set the figure DPI to 300 with `fig = plt.figure(figsize=(11, 8.5), dpi=300)` for landscape or `figsize=(8.5, 11)` for portrait.
- Set `plt.rcParams["savefig.dpi"] = 300`, `plt.rcParams["savefig.bbox"] = "tight"`, `plt.rcParams["savefig.pad_inches"] = 0.25`.
- Use `fig.tight_layout()` plus explicit `subplots_adjust` so no manual positioning is required by the human author. Every text label, every legend, every annotation, every header, every footer must align without further intervention.
- Save with `fig.savefig(out_path, dpi=300, facecolor="white")`.
- Close the figure with `plt.close(fig)` to free memory.

## Color Palette

A single shared palette applies across all 100 figures so a viewer can read any figure consistently. All colors are visible against a pure white background. No dark mode.

| Role | Hex | Use |
|------|-----|-----|
| Deep Navy | `#1F3A68` | Humanoid platform elements |
| Teal | `#2E8B8B` | LLM model elements |
| Burgundy | `#8B2E3F` | Safety, risk, regulatory severity |
| Gold | `#C18A2C` | Financial, cost, ROI |
| Forest Green | `#2F6B3E` | Compliance pass, success, gain |
| Slate | `#4A5568` | Neutral, text, secondary lines |
| Mauve | `#8B6B8B` | Data flow, secondary humanoid |
| Light Gray | `#E2E8F0` | Backgrounds, grid lines |
| Off-White | `#F7FAFC` | Card backgrounds, callout boxes |
| Pure White | `#FFFFFF` | Figure facecolor |

For heatmaps use the matplotlib colormap `cividis` (perceptually uniform, colorblind safe). For sequential ramps use `viridis`. For diverging severity use a manual blend from Forest Green at the low end to Burgundy at the high end through a midtone Gold. Never use `jet` or `rainbow`.

## Typography

| Element | Size (pt) | Weight | Color |
|---------|-----------|--------|-------|
| Figure title | 16 | bold | `#1F3A68` |
| Figure subtitle | 12 | regular | `#4A5568` |
| Axis title | 12 | semi-bold | `#1F3A68` |
| Tick label | 9 | regular | `#4A5568` |
| Annotation | 9 | regular | `#4A5568` |
| Legend body | 9 | regular | `#4A5568` |
| Footer (source, DOI, license) | 8 | italic | `#4A5568` |

All text uses the matplotlib default `DejaVu Sans` family. Weight `semi-bold` is approximated by `fontweight="semibold"` (matplotlib accepts this).

## Header and Footer Per Figure

Every figure has:

- Title at the top, centered, 16 pt bold Deep Navy.
- Subtitle one line below, centered, 12 pt regular Slate.
- A footer band 0.4 inches from the bottom containing, left-aligned: `Clinical-AI-Demos v0.2.0 / Demo NN`. Right-aligned: `DOI: 10.5281/zenodo.18445179 / MIT License`. Both 8 pt italic Slate.
- A 0.3 inch margin on all sides between the figure axes and the page edge so text never clips.

## Character Rules

- Use single dashes only. No em dashes (`-` not `-`). No double dashes (`--`). No triple dashes (`---`) outside valid Markdown table separators in the instruction files.
- Use the section sign `§` where the cited regulation uses it (for example `21 CFR § 50.25`). Do not write `SS 50.25` or `Section 50.25` when the source uses `§`.
- Use the multiplication sign `x` (lowercase letter x) for `12 x 24` style grids and `times` for `2 x 10^7` scientific notation when the source writes `times`.
- Use Greek `mu` as `mu` in text (matplotlib supports `$\\mu$` in math contexts only).
- Use `degrees C` not the degree symbol unless the figure uses LaTeX rendering. Default text should write `degC` or `degrees Celsius`.
- Use percentage as `%` directly in text labels.
- Use the ohm sign `Omega` as `Omega` in text labels.
- No emojis in any figure.

## Validation Per Instruction

Every instruction file lists a validation checklist the future author runs after generating the PNG:

1. PNG dimensions equal `figsize * dpi` (3300 x 2550 for landscape Letter at 300 dpi; 2550 x 3300 for portrait Letter at 300 dpi).
2. PNG facecolor is pure white at every page corner.
3. No text label is clipped at any edge (verified by reading the saved PNG and checking the alpha edges with pillow).
4. All character rules above are satisfied (no em dash, no double dash, etc.).
5. Every color used appears in the palette table or the colormap whitelist.
6. The figure title, subtitle, header, footer, and legend are present and unclipped.

## Cross-Reference to Demo Prompts

| Demo | Prompt File | Humanoid | LLM | Image Instructions Subdirectory |
|------|-------------|----------|-----|---------------------------------|
| 01 | `demo-projects/01-humanoid-site-operations-director.md` | Boston Dynamics Atlas Electric | Claude Opus 4.7 1M on-prem | `01-site-operations-director/` |
| 02 | `demo-projects/02-sponsor-humanoid-operations-center.md` | 5x Tesla Optimus Gen 3 | Claude Sonnet 4.6 + Opus 4.7 failover | `02-sponsor-operations-center/` |
| 03 | `demo-projects/03-humanoid-pharmacy-imp-compounding.md` | Figure 03 | GPT-5.5 Thinking on-prem | `03-pharmacy-imp-compounding/` |
| 04 | `demo-projects/04-humanoid-post-op-recovery-nurse.md` | Agility Digit V5 | Claude Haiku 4.5 + Sonnet 4.6 + Ollama Llama 4 70B | `04-post-op-recovery-nurse/` |
| 05 | `demo-projects/05-humanoid-biospecimen-pathology-lab.md` | Sanctuary Phoenix Gen 8 | Gemini 3 Pro + Ollama Qwen3 72B via MCP | `05-biospecimen-pathology-lab/` |
| 06 | `demo-projects/06-humanoid-tele-surgical-assistant.md` | Apptronik Apollo | Claude Opus 4.7 1M + operator-in-the-loop | `06-tele-surgical-assistant/` |
| 07 | `demo-projects/07-humanoid-24-7-adverse-event-response.md` | 3x Unitree H2 (4-site rotation) | Per-site Claude Opus 4.7 1M | `07-adverse-event-response/` |
| 08 | `demo-projects/08-humanoid-clinical-research-coordinator.md` | 1X Neo Beta | Claude Opus 4.7 + Gemini 3 Pro + GPT-5.5 Thinking ensemble | `08-clinical-research-coordinator/` |
| 09 | `demo-projects/09-humanoid-radiation-oncology-technologist.md` | Atlas + Optimus pair | NVIDIA GR00T N1.6 + Cosmos Reason 2 + Claude Opus 4.7 arbiter | `09-radiation-oncology-technologist/` |
| 10 | `demo-projects/10-humanoid-decentralized-home-care.md` | Figure 03 Field Edition | Claude Haiku 4.5 edge on NVIDIA Orin AGX 64GB | `10-decentralized-home-care/` |

## Humanoid + LLM Influence

Every instruction in this directory centers a humanoid platform and an LLM control loop:

- The humanoid platform is the physical agent that performs surgical and patient care tasks at the trial site or for the pharmaceutical sponsor.
- The LLM is the planning and reasoning loop that emits commands to the humanoid, validates safety constraints, and provides audit-grade rationale for every action.
- The combination of humanoid plus LLM is the unit of analysis in every figure: architecture diagrams show the control loop; timelines show the LLM tick alongside humanoid motion ticks; compliance matrices show how each humanoid + LLM pair maps to a regulatory framework; financial waterfalls amortize humanoid acquisition plus LLM inference cost; radar charts compare the humanoid + LLM stack against human-only or competitor humanoid baselines; sankeys trace the data path through LLM tokens and humanoid actions; funnels filter humanoid + LLM task candidates by safety, regulatory, and clinical thresholds; quadrants position the humanoid + LLM stack against competitor configurations on strategic axes; decision trees branch on LLM confidence and humanoid sensor readings.

## Future Generation Pipeline

1. A future Claude Code Opus 4.7 1M Max session reads one instruction file.
2. The session writes one matplotlib script per instruction under `demo-projects/NN-name-output/figures/render_NN_NN_short_name.py`.
3. The session runs the script, emits the 300 dpi PNG to `demo-projects/NN-name-output/figures/NN-NN-short-name.png`.
4. The session adds both the script and the PNG to the commit, runs the validation checklist, and pushes.
5. The PNG is referenced from the demo's README, comparison report, and release notes.

## CI Compliance

This directory adds no Python and no YAML in this PR. The lint-and-format CI workflow on Python 3.10, 3.11, 3.12 remains green:

- `ruff check .` returns 0 because no Python files are added.
- `ruff format --check .` returns 0 because no Python files are added.
- `yamllint -d relaxed .github/` returns 0 because no YAML files are touched.

When the future sessions generate the matplotlib scripts under `demo-projects/NN-name-output/figures/`, the existing `ruff.toml` per-file-ignores entry `demo-projects/**/*.py = ["F401", "F402", "F821"]` covers them. The ruff formatter passes on matplotlib scripts that follow the conventions above.

## Notes

- All instructions follow the same template structure: Filename, Page Size, DPI, Chart Type, Title, Subtitle, Header, Footer, Data Structure, Visual Specification, Color Mapping, Annotations, Validation Checklist.
- Do not modify the 10 prompt files at `demo-projects/01-...md` through `demo-projects/10-...md` while authoring the instructions. The instructions reference those prompts; they do not change them.
- All instructions reference the companion repository `kevinkawchak/physical-ai-oncology-trials` for the source data structure each demo will produce. Do not modify that companion repository.
- The 30 landscape instructions (3 per prompt x 10 prompts) plus 70 portrait instructions (7 per prompt x 10 prompts) total 100. Total expected PNG payload at 300 dpi is approximately 250 MB across all 100 figures.
