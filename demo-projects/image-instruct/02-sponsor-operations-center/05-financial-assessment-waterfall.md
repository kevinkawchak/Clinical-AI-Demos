# Image Instruction 02-05: 5x Optimus + Sonnet/Opus Sponsor Center 5-Year TCO Waterfall

[![Demo](https://img.shields.io/badge/Demo-02-brightgreen.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/blob/main/demo-projects/02-sponsor-humanoid-operations-center.md)
[![Image](https://img.shields.io/badge/Image-05%20of%2010-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/tree/main/demo-projects/image-instruct/02-sponsor-operations-center)
[![Orientation](https://img.shields.io/badge/Orientation-Portrait-orange.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)
[![DPI](https://img.shields.io/badge/DPI-300-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)

## Output Filename

`demo-projects/02-sponsor-humanoid-operations-center-output/figures/02-05-financial-assessment-waterfall.png`

## Page Size and DPI

- Letter portrait, 8.5 x 11.0 inches, 300 dpi, 2550 x 3300 pixels, white facecolor.

## Chart Type

Vertical waterfall chart, 16 bars. Buildup from baseline sponsor operations cost through humanoid acquisition, LLM inference, Safe Harbor infrastructure, and offsets to the 5-year cumulative TCO.

## Title and Subtitle

- Title: `Sponsor Operations Center 5-Year Total Cost of Ownership Waterfall`.
- Subtitle: `5x Optimus + Sonnet/Opus Failover vs. Manual Clinical Ops Baseline - SPO-2026-001 - USD Thousands`.

## Header and Footer

- Header right: `Demo 02 / Image 05 of 10 / Portrait`.
- Footer left: `Clinical-AI-Demos v0.2.0 / Demo 02 Sponsor Humanoid Operations Center`.
- Footer right: `DOI: 10.5281/zenodo.18445179 / MIT License`.

## Bars (16, left to right)

1. `Year 0 Baseline Manual Clinical Ops` (Slate).
2. `+ 5x Optimus Gen 3 Acquisition` (Deep Navy).
3. `+ 5-Year Optimus Service Contract` (Deep Navy).
4. `+ On-Prem Sonnet 4.6 Cluster (Anthropic Cowork)` (Teal).
5. `+ Claude Opus 4.7 1M Cloud Failover Subscription` (Teal darker).
6. `+ Safe Harbor De-Identification Gate Infrastructure` (Burgundy).
7. `+ 40th-Floor Bench Build-Out and HVAC` (Slate).
8. `+ FDA RTCT Submission Automation Cluster` (Gold).
9. `+ DSMB Charter Automation` (Forest Green).
10. `- Manual CRA Aggregation Salary Offset` (Forest Green negative).
11. `- Manual SAE Narrative Authoring Offset` (Forest Green negative).
12. `- IRB Amendment Cycle Time Cost Offset` (Forest Green negative).
13. `- HR 9505 SLA Penalty Offset` (Forest Green negative).
14. `+ Annual Maintenance and Spare Parts` (Gold).
15. `+ Cyber Insurance and Regulatory Reserve` (Burgundy).
16. `Cumulative 5-Year TCO` (Deep Navy total bar).

## Color Mapping and Layout

Same conventions as 01-05. Connector lines 0.8 pt Slate dashed between bar tops. Y axis label `USD Thousands`. Bar labels rotated 30 degrees.

## Annotations

- Horizontal dashed reference line at the baseline (bar 1 height) labeled `Manual Clinical Ops Baseline`.
- Callout box top right: `5x Optimus + Sonnet/Opus failover delivers projected ROI breakeven in Year 1 from SAE narrative cycle time alone. HR 9505 SLA penalty offset alone repays Cloud Failover subscription.`

## matplotlib Recipe

Same as 01-05 (`ax.bar` with `bottom` parameter for floating bars, connector lines via `ax.plot`).

## Validation Checklist

1. PNG is 2550 x 3300 pixels.
2. 16 bars visible with connectors.
3. Cumulative bar at far right from 0 to total.
4. Baseline dashed reference line present and labeled.
5. Callout box top right.
6. Title, subtitle, header, footer present.
7. No em dash, no double dash, no triple dash.
8. No color outside palette.
9. No emoji.
10. Bar labels readable, rotated, unclipped.
