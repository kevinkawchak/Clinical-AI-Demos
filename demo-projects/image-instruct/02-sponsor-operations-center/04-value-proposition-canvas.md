# Image Instruction 02-04: Sponsor Operations Center Value Proposition Canvas

[![Demo](https://img.shields.io/badge/Demo-02-brightgreen.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/blob/main/demo-projects/02-sponsor-humanoid-operations-center.md)
[![Image](https://img.shields.io/badge/Image-04%20of%2010-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/tree/main/demo-projects/image-instruct/02-sponsor-operations-center)
[![Orientation](https://img.shields.io/badge/Orientation-Portrait-orange.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)
[![DPI](https://img.shields.io/badge/DPI-300-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)

## Output Filename

`demo-projects/02-sponsor-humanoid-operations-center-output/figures/02-04-value-proposition-canvas.png`

## Page Size and DPI

- Letter portrait, 8.5 x 11.0 inches, 300 dpi, 2550 x 3300 pixels, white facecolor.

## Chart Type

Strategyzer-style Value Proposition Canvas (square on right, circle on left, three panels each).

## Title and Subtitle

- Title: `5x Tesla Optimus Gen 3 + Sonnet/Opus Sponsor Operations Center Value Proposition Canvas`.
- Subtitle: `Stakeholder: Sponsor Head of Clinical Operations, Regulatory Affairs Lead, Pharmacovigilance Officer`.

## Header and Footer

- Header right: `Demo 02 / Image 04 of 10 / Portrait`.
- Footer left: `Clinical-AI-Demos v0.2.0 / Demo 02 Sponsor Humanoid Operations Center`.
- Footer right: `DOI: 10.5281/zenodo.18445179 / MIT License`.

## Value Map Panels (right square, top to bottom)

1. **Products and Services** (Deep Navy header):
   - `5x Tesla Optimus Gen 3 humanoids at the SPO-2026-001 40th-floor bench, 24/7 on-shift in 12-hour rotations`.
   - `Claude Sonnet 4.6 on-prem default planner (no PHI egress)`.
   - `Claude Opus 4.7 1M cloud failover gated by Safe Harbor`.
   - `Daily DSMB summary author, weekly FDA RTCT submission packet author, real-time IRB amendment co-pilot`.
2. **Pain Relievers** (Burgundy header):
   - `Eliminates the manual document aggregation latency that delays 21 CFR § 312 IND amendments`.
   - `Prevents Safe Harbor leakage via on-prem Sonnet default`.
   - `Reduces SAE narrative authoring time from 6 to 8 hours per event to 12 minutes`.
   - `Bounds inter-humanoid distance at 8 mm to maintain bench density without collisions`.
3. **Gain Creators** (Forest Green header):
   - `Compresses end-of-week DSMB review cycle from 3 days to 4 hours`.
   - `Increases CRA call summary fidelity by capturing all 5 sites in parallel`.
   - `Auto-tags every document with 21 CFR § 11 electronic-signature provenance`.
   - `Closes the loop on HR 9505 1-hour SAE sponsor acknowledgment SLA`.

## Customer Profile Sectors (left circle)

1. **Customer Jobs** (top sector, Deep Navy):
   - `Manage 5 active oncology trials in parallel`.
   - `Author and publish 8 document classes per week per trial`.
   - `Track DSMB charter and FDA RTCT submission windows`.
2. **Pains** (bottom-left sector, Burgundy):
   - `Document aggregation across 5 site CRAs creates serial bottleneck`.
   - `Safe Harbor de-identification is manual and error-prone`.
   - `End-of-week DSMB summary forces overtime weekend work`.
3. **Gains** (bottom-right sector, Forest Green):
   - `Continuous, audit-ready document trail`.
   - `Failover transparency: every Opus 4.7 cloud trip logged with PHI gate verdict`.
   - `Per-trial regulatory exposure dashboard refreshed at 1 Hz`.

## Color and matplotlib Recipe

Same conventions as 01-04. Use Off-White panel backgrounds, colored header bars, Strategyzer-style circle subdivided into 120-degree sectors via `matplotlib.patches.Wedge`.

## Validation Checklist

1. PNG is 2550 x 3300 pixels.
2. Both shapes present with 3 panels and 3 sectors each.
3. `Fit` arrow between shapes.
4. Title, subtitle, header, footer present.
5. `§` appears in `21 CFR § 312`, `21 CFR § 11`, `HR 9505` reference.
6. No em dash, no double dash, no triple dash.
7. No color outside palette.
8. No emoji.
9. Text wraps inside panels without clipping.
10. Sub-panel headers in matching colors (Deep Navy, Burgundy, Forest Green).
