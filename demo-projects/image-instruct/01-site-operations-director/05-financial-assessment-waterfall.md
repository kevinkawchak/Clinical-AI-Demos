# Image Instruction 01-05: Atlas Site Director 5-Year Total Cost of Ownership Financial Waterfall

[![Demo](https://img.shields.io/badge/Demo-01-brightgreen.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/blob/main/demo-projects/01-humanoid-site-operations-director.md)
[![Image](https://img.shields.io/badge/Image-05%20of%2010-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/tree/main/demo-projects/image-instruct/01-site-operations-director)
[![Orientation](https://img.shields.io/badge/Orientation-Portrait-orange.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)
[![DPI](https://img.shields.io/badge/DPI-300-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)

## Output Filename

`demo-projects/01-humanoid-site-operations-director-output/figures/01-05-financial-assessment-waterfall.png`

## Page Size and DPI

- Letter portrait, 8.5 x 11.0 inches, 300 dpi, 2550 x 3300 pixels, white facecolor.

## Chart Type

Vertical waterfall chart with 14 bars. The leftmost bar is the starting baseline cost; intermediate bars show incremental positive or negative contributions; the rightmost bar is the cumulative 5-year TCO. Connector horizontal lines link the top of each bar to the bottom of the next.

## Title and Subtitle

- Title: `Atlas Electric + Claude Opus 4.7 1M Site Director 5-Year Total Cost of Ownership Waterfall`.
- Subtitle: `Per-Site Cost Buildup vs. Baseline Human Director Coverage at PAT-SITE-001 - USD Thousands`.

## Header and Footer

- Header right: `Demo 01 / Image 05 of 10 / Portrait`.
- Footer left: `Clinical-AI-Demos v0.2.0 / Demo 01 Site Operations Director`.
- Footer right: `DOI: 10.5281/zenodo.18445179 / MIT License`.

## Bars (14, left to right)

1. `Year 0 Baseline Human Director Coverage` (Slate, starts at 0, positive contribution).
2. `+ Atlas Electric Humanoid Acquisition` (Deep Navy, positive).
3. `+ Atlas Electric Service Contract 5-Year` (Deep Navy, positive).
4. `+ Claude Opus 4.7 1M On-Prem Inference Cluster` (Teal, positive).
5. `+ Claude Opus 4.7 1M Anthropic Cowork Subscription` (Teal, positive).
6. `+ Safety Arbiter Certification (IEC 80601-2-77)` (Burgundy, positive).
7. `+ Audit and Hash-Chain Infrastructure` (Slate, positive).
8. `- Human Director Salary Offset (5-Year)` (Forest Green, negative).
9. `- Overtime and Night-Cover Offset` (Forest Green, negative).
10. `- AE Misclassification Cost Reduction` (Forest Green, negative).
11. `- IRB Audit Finding Reduction` (Forest Green, negative).
12. `+ Annual O and M Plus Spare Parts` (Gold, positive).
13. `+ Cyber and Regulatory Reserve` (Burgundy, positive).
14. `Cumulative 5-Year TCO` (Deep Navy total bar, full height from 0).

## Color Mapping

- Positive contributions (cost adders) above 0 in their category color.
- Negative contributions (cost offsets) below 0 in Forest Green.
- The starting baseline and the final cumulative bar in Deep Navy.
- Connector lines in 0.8 pt Slate.

## Annotations

- Each bar shows its delta value centered above the bar in 9 pt regular Slate (`+$320` or `-$185`).
- The cumulative bar shows its total value in 11 pt bold Deep Navy.
- A horizontal dashed reference line at the baseline human director cost (the value of bar 1) spans the full chart width, labeled `Baseline Human Coverage Cost`.
- Callout box at top right: `Net 5-Year TCO Delta vs. Baseline: see cumulative bar. ROI breakeven projected in Year 2 from AE misclassification cost reduction alone.`

## Layout Specification

- Chart area y 0.10 to 0.85, x 0.10 to 0.95.
- Bar width 0.65 of slot width.
- X labels rotated 30 degrees, wrapped to 2 lines.
- Y axis label: `USD Thousands`.
- Y axis grid lines Light Gray dashed every 100 USD thousand.

## Data Structure Future Author Provides

The future Claude Code Opus 4.7 1M Max session will produce a CSV `tco_waterfall.csv` with columns:

| Column | Type | Description |
|--------|------|-------------|
| `step` | string | one of the 14 bar labels |
| `category` | string | `humanoid`, `llm`, `safety`, `offset`, `om`, `reserve`, `baseline`, `total` |
| `delta_usd_thousands` | float | positive or negative |
| `cumulative_usd_thousands` | float | running total after this step |

The future author plugs the actual numbers from the v0.2.0 simulation; the figure script must not hardcode example numbers.

## matplotlib Recipe

- Use `ax.bar(x, height=abs(delta), bottom=bar_bottom, color=color, edgecolor='#1F3A68', lw=0.5)`.
- Compute `bar_bottom` per bar by tracking the running cumulative.
- Use `ax.plot([x1, x2], [top1, top1], color='#4A5568', lw=0.8, linestyle='--')` for connector lines between consecutive bars.
- Use `ax.axhline(baseline, linestyle='--', color='#8B6B8B', lw=0.8)` for the baseline reference line.
- Use `ax.text(x, top + small, f'{delta:+.0f}', ha='center', va='bottom', fontsize=9, color='#4A5568')` for delta labels.

## Validation Checklist

1. PNG is 2550 x 3300 pixels.
2. 14 bars visible with connectors between them.
3. Cumulative bar at the far right with a 0-to-top height.
4. Baseline reference line labeled and dashed.
5. Callout box visible.
6. Title, subtitle, header, footer present.
7. No em dash, no double dash, no triple dash.
8. No color outside palette.
9. No emoji.
10. All bar labels readable, rotated 30 degrees, unclipped at the bottom margin.
