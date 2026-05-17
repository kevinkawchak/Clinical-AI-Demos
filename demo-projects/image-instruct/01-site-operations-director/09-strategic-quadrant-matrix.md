# Image Instruction 01-09: Atlas Site Director Strategic Quadrant Bubble Matrix

[![Demo](https://img.shields.io/badge/Demo-01-brightgreen.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/blob/main/demo-projects/01-humanoid-site-operations-director.md)
[![Image](https://img.shields.io/badge/Image-09%20of%2010-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/tree/main/demo-projects/image-instruct/01-site-operations-director)
[![Orientation](https://img.shields.io/badge/Orientation-Portrait-orange.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)
[![DPI](https://img.shields.io/badge/DPI-300-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)

## Output Filename

`demo-projects/01-humanoid-site-operations-director-output/figures/01-09-strategic-quadrant-matrix.png`

## Page Size and DPI

- Letter portrait, 8.5 x 11.0 inches, 300 dpi, 2550 x 3300 pixels, white facecolor.

## Chart Type

Strategic 2x2 quadrant bubble matrix. The X axis is `Cross-Bay Coordination Capability` (low to high). The Y axis is `Per-Tick Decision Latency` (slow to fast, axis inverted so faster is up). Bubbles represent different humanoid + LLM configurations. Bubble size proportional to deployment-cost-per-shift in USD thousands.

## Title and Subtitle

- Title: `Atlas Electric + Claude Opus 4.7 1M Site Director Strategic Quadrant`.
- Subtitle: `Cross-Bay Coordination Capability vs. Per-Tick Decision Latency - PAT-SITE-001 8-Hour Shift`.

## Header and Footer

- Header right: `Demo 01 / Image 09 of 10 / Portrait`.
- Footer left: `Clinical-AI-Demos v0.2.0 / Demo 01 Site Operations Director`.
- Footer right: `DOI: 10.5281/zenodo.18445179 / MIT License`.

## Axes

- X axis: `Cross-Bay Coordination Capability` (number of simultaneous bays effectively managed), 0 to 24, ticks every 4.
- Y axis: `Per-Tick Decision Latency (lower is better)`, 1000 ms to 50 ms, inverted (50 ms at top). Use log scale.
- Origin axes drawn as 1.5 pt Slate solid lines at the chart medians (X = 12, Y = 200 ms).
- Light gray gridlines every major tick.

## Quadrant Labels (each corner)

- Top right: `Leaders` (Atlas + Claude Opus stack target).
- Top left: `Latency Specialists` (low coordination, fast).
- Bottom right: `Coordination Specialists` (broad coordination, slow).
- Bottom left: `Legacy` (human-only).
Use 12 pt italic Slate, placed 0.02 normalized inside each corner.

## Bubble Series (8 configurations)

1. `Atlas Electric + Claude Opus 4.7 1M on-prem` (Deep Navy fill) - x=20, y=200 ms, size proportional to per-shift cost.
2. `Atlas Electric + Claude Sonnet 4.6` (Deep Navy lighter fill).
3. `Tesla Optimus Gen 3 + Claude Opus 4.7 1M cloud` (Teal fill).
4. `Figure 03 + GPT-5.5 Thinking on-prem` (Gold fill).
5. `Agility Digit V5 + Claude Sonnet 4.6` (Mauve fill).
6. `Sanctuary Phoenix Gen 8 + Gemini 3 Pro` (Forest Green fill).
7. `Human Shift Director (Baseline)` (Slate fill).
8. `Hybrid Atlas + Human Director` (Burgundy fill).

Each bubble labeled with a 2 or 3 character short code (e.g., `A+O` for Atlas + Opus) next to the bubble.

## Annotations

- Diagonal arrow from `Legacy` quadrant to `Leaders` quadrant labeled `Migration Path 2026 to 2028`.
- Highlight a 0.6 pt dashed Burgundy circle around the Atlas + Claude Opus bubble labeled `v0.2.0 Reference Configuration`.

## Layout Specification

- Chart area y 0.12 to 0.85, x 0.12 to 0.88.
- Legend below the chart, y 0.05 to 0.10, 2 columns of 4 series each, 9 pt regular Slate.

## matplotlib Recipe

- Use `ax.scatter(x, y, s=size, c=color, edgecolors='#1F3A68', linewidths=0.8, alpha=0.75)`.
- Use `ax.set_yscale('log')`, `ax.invert_yaxis()` to put faster latency at the top.
- Use `ax.axvline(12, color='#4A5568', lw=1.5)` and `ax.axhline(200, color='#4A5568', lw=1.5)` for the quadrant medians.
- Use `ax.annotate` for the diagonal migration-path arrow.
- Use `ax.text` for the quadrant corner labels with `transform=ax.transAxes`.

## Data Structure Future Author Provides

CSV `quadrant_bubbles.csv`:

| Column | Type |
|--------|------|
| `series` | string |
| `short_code` | string (2-3 chars) |
| `x_coordination` | float (0 to 24) |
| `y_latency_ms` | float |
| `size_cost_usd_thousands` | float |
| `color_hex` | string |

## Validation Checklist

1. PNG is 2550 x 3300 pixels.
2. 8 distinct bubbles plotted with correct colors and sizes.
3. Quadrant median lines visible.
4. 4 corner labels present.
5. Migration-path arrow visible.
6. Reference circle around Atlas + Claude Opus bubble.
7. Legend at the bottom with 8 entries.
8. Title, subtitle, header, footer present.
9. Y axis inverted with log scale ticks at 1000, 500, 200, 100, 50 ms.
10. No em dash, no double dash, no triple dash. No emoji.
