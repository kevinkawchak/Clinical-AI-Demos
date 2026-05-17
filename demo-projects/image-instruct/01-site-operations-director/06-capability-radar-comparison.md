# Image Instruction 01-06: Atlas + Claude Opus Capability Radar Comparison

[![Demo](https://img.shields.io/badge/Demo-01-brightgreen.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/blob/main/demo-projects/01-humanoid-site-operations-director.md)
[![Image](https://img.shields.io/badge/Image-06%20of%2010-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/tree/main/demo-projects/image-instruct/01-site-operations-director)
[![Orientation](https://img.shields.io/badge/Orientation-Portrait-orange.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)
[![DPI](https://img.shields.io/badge/DPI-300-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)

## Output Filename

`demo-projects/01-humanoid-site-operations-director-output/figures/01-06-capability-radar-comparison.png`

## Page Size and DPI

- Letter portrait, 8.5 x 11.0 inches, 300 dpi, 2550 x 3300 pixels, white facecolor.

## Chart Type

Radar (spider) chart with 8 axes. Four overlapping translucent polygons compare the Atlas + Claude Opus 4.7 stack against three baselines on the same axes.

## Title and Subtitle

- Title: `Atlas Electric + Claude Opus 4.7 1M Site Director Capability Radar`.
- Subtitle: `Atlas + Claude vs. Optimus + Claude vs. Figure + GPT vs. Human Director - PAT-SITE-001 8-Hour Shift`.

## Header and Footer

- Header right: `Demo 01 / Image 06 of 10 / Portrait`.
- Footer left: `Clinical-AI-Demos v0.2.0 / Demo 01 Site Operations Director`.
- Footer right: `DOI: 10.5281/zenodo.18445179 / MIT License`.

## Axes (8 dimensions, scored 0 to 100)

1. `Decision Cadence` (LLM tick frequency in Hz, normalized so 1 Hz scores 80).
2. `E-Stop Latency Performance` (lower latency higher score; 50 ms scores 80, 5 ms scores 100).
3. `Cross-Bay Coordination` (number of simultaneous bays managed).
4. `IRB and 21 CFR § 312 Compliance` (audit pass rate).
5. `AE Response Time` (lower seconds higher score).
6. `Cumulative Force Safety Margin` (further below the 15 N limit higher score).
7. `Cost Efficiency 5-Year TCO` (lower TCO higher score).
8. `Patient Experience NPS` (Net Promoter Score for the shift).

## Series (4 polygons)

1. `Atlas Electric + Claude Opus 4.7 1M` (Deep Navy fill at 0.35 alpha, Deep Navy outline 1.5 pt).
2. `Tesla Optimus Gen 3 + Claude Opus 4.7 1M` (Teal fill 0.30 alpha, Teal outline 1.2 pt).
3. `Figure 03 + GPT-5.5 Thinking` (Gold fill 0.30 alpha, Gold outline 1.2 pt).
4. `Human Director (Baseline)` (Slate fill 0.25 alpha, Slate outline 1.2 pt dashed).

## Layout Specification

- Radar plotted in polar projection at the center, occupying y 0.15 to 0.78, x 0.10 to 0.90.
- Title at the top, subtitle below.
- Legend in the bottom area y 0.06 to 0.13 spanning the full width with 4 entries in a single row, each entry showing a small fill swatch and the series name in 9 pt.
- Axis labels just outside the radar at the 8 axis endpoints, 10 pt regular Slate, with the dimension name on one line and a short unit hint on a second line.

## Annotations

- Three radial reference rings at scores 25, 50, 75 with light gray dashed lines.
- The outer ring at 100 with a slightly heavier Slate line.
- A central black dot at the origin labeled with the iteration count `n = 32` in 8 pt italic.
- Callout text above the legend: `Atlas + Claude Opus leads on Decision Cadence, E-Stop Latency, Compliance, AE Response, Force Safety. Human Director leads on Patient Experience NPS at v0.2.0 freeze.`

## matplotlib Recipe

- Use `fig.add_subplot(projection='polar')`.
- Compute angles: `theta = np.linspace(0, 2*np.pi, 8, endpoint=False)`.
- For each series, close the polygon by appending the first value to the end and `theta[0]` to the theta array.
- Use `ax.fill(theta_closed, values_closed, color=fill_color, alpha=fill_alpha)`.
- Use `ax.plot(theta_closed, values_closed, color=outline_color, lw=outline_lw, linestyle=linestyle)`.
- Use `ax.set_theta_offset(np.pi / 2)` and `ax.set_theta_direction(-1)` so the first axis points up and labels rotate clockwise.
- Use `ax.set_xticks(theta)` and `ax.set_xticklabels(axis_labels, fontsize=10)`.
- Use `ax.set_ylim(0, 100)` and `ax.set_yticks([25, 50, 75, 100])`.

## Data Structure Future Author Provides

CSV `capability_radar.csv` with columns:

| Column | Type |
|--------|------|
| `series` | string (one of the 4 series names) |
| `axis` | string (one of the 8 axis names) |
| `score` | float (0 to 100) |

## Validation Checklist

1. PNG is 2550 x 3300 pixels.
2. Radar shows 4 distinct polygons with the assigned fill colors and alphas.
3. 8 axis labels visible, unclipped.
4. Reference rings at 25, 50, 75, 100 visible.
5. Legend at the bottom with 4 entries.
6. Callout text present above the legend.
7. Title, subtitle, header, footer present.
8. `§` appears in `21 CFR § 312`.
9. No em dash, no double dash, no triple dash.
10. No color outside palette.
