# Image Instruction 01-08: Atlas + Claude Opus 4.7 LLM Tick Decision Funnel

[![Demo](https://img.shields.io/badge/Demo-01-brightgreen.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/blob/main/demo-projects/01-humanoid-site-operations-director.md)
[![Image](https://img.shields.io/badge/Image-08%20of%2010-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/tree/main/demo-projects/image-instruct/01-site-operations-director)
[![Orientation](https://img.shields.io/badge/Orientation-Portrait-orange.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)
[![DPI](https://img.shields.io/badge/DPI-300-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)

## Output Filename

`demo-projects/01-humanoid-site-operations-director-output/figures/01-08-process-funnel-chart.png`

## Page Size and DPI

- Letter portrait, 8.5 x 11.0 inches, 300 dpi, 2550 x 3300 pixels, white facecolor.

## Chart Type

Vertical process funnel chart with 7 trapezoidal stages. Each stage narrows downward from the prior stage by an amount proportional to filtered-out items. The funnel filters Claude Opus 4.7 1M LLM ticks from the full per-second pool down to the subset that produces an Atlas Electric humanoid motion command in the next 60 seconds.

## Title and Subtitle

- Title: `Atlas Electric + Claude Opus 4.7 1M Decision Funnel: 28,800 Ticks to Humanoid Actions`.
- Subtitle: `8-Hour Day Shift at PAT-SITE-001 - From Raw LLM Tick to Committed Atlas Motion Command`.

## Header and Footer

- Header right: `Demo 01 / Image 08 of 10 / Portrait`.
- Footer left: `Clinical-AI-Demos v0.2.0 / Demo 01 Site Operations Director`.
- Footer right: `DOI: 10.5281/zenodo.18445179 / MIT License`.

## Stages (7, top to bottom)

1. **Raw LLM Ticks Total** (Teal `#2E8B8B`): 28,800. The full 8-hour shift at 1 Hz.
2. **Ticks With New Site State Delta** (Teal slightly darker): the subset where at least one bay, room, imaging suite, or patient vitals changed.
3. **Ticks Passing Pre-Plan Guard** (Slate `#4A5568`): the subset whose context window stayed within 1M tokens after pre-chunking.
4. **Ticks Producing a Candidate Atlas Action** (Deep Navy `#1F3A68`): the subset where Claude Opus 4.7 emitted at least one candidate humanoid action JSON.
5. **Candidate Actions Passing Safety Arbiter** (Burgundy `#8B2E3F`): the subset cleared by IEC 80601-2-77 plus cumulative force budget.
6. **Actions Within E-Stop Window** (Gold `#C18A2C`): the subset confirmed to fit the 50 ms E-stop response budget.
7. **Committed Atlas Motion Commands** (Forest Green `#2F6B3E`): the subset dispatched to the Atlas Dispatcher and executed.

## Layout Specification

- Funnel area x 0.15 to 0.85, y 0.10 to 0.85.
- Each stage occupies a vertical band of (height / 7) units.
- Top stage width 0.70 normalized. Subsequent widths shrink linearly toward the cumulative pass-through rate.
- Stage labels centered inside the trapezoid in 10 pt regular white text.
- Stage count and percentage to the right of the funnel at the vertical midpoint of each stage in 9 pt Slate.

## Annotations

- Left margin column labeled `Filter Applied` lists the rule that filters each stage:
  1. -
  2. `site_state.delta != empty`
  3. `prompt_tokens <= 1,000,000`
  4. `len(candidate_actions) >= 1`
  5. `safety_arbiter.pass == True`
  6. `predicted_estop_ms <= 50`
  7. `dispatcher.commit == True`
- Right margin column labeled `Cumulative Pass Rate` shows running pass-through percentage at each stage.
- Bottom note: `Approximately 1,440 committed Atlas motion commands per 8-hour shift, equating to 3 actions per minute averaged across the 12 bays.`

## Color Mapping

- Trapezoid fill per stage as listed above.
- Trapezoid outline 1.2 pt darker shade of the same hue.
- Text inside trapezoids: white if fill is dark, Deep Navy if fill is Gold (for contrast).

## matplotlib Recipe

- Compute trapezoid coordinates for each stage given prior bottom width and current bottom width.
- Use `matplotlib.patches.Polygon` for each trapezoid.
- Use `ax.text` for stage labels (centered inside) and side annotations (left and right margins).
- Set `ax.set_xlim(0, 1)`, `ax.set_ylim(0, 1)`, `ax.set_axis_off()`.

## Data Structure Future Author Provides

CSV `funnel_stages.csv`:

| Column | Type |
|--------|------|
| `stage` | string |
| `count` | int |
| `cumulative_pass_rate` | float (0 to 1) |
| `filter_rule` | string |

## Validation Checklist

1. PNG is 2550 x 3300 pixels.
2. 7 trapezoidal stages stacked vertically, narrowing downward.
3. Stage labels centered inside, count and percentage on the right.
4. Left `Filter Applied` margin column populated.
5. Bottom note present.
6. Title, subtitle, header, footer present.
7. No em dash, no double dash, no triple dash.
8. No color outside palette.
9. No emoji.
10. Stage 1 widest at top, stage 7 narrowest at bottom.
