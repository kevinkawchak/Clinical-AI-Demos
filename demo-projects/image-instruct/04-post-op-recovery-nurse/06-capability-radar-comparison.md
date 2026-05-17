# Image Instruction 04-06: PACU Recovery Capability Radar Comparison

[![Demo](https://img.shields.io/badge/Demo-04-brightgreen.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/blob/main/demo-projects/04-humanoid-post-op-recovery-nurse.md)
[![Image](https://img.shields.io/badge/Image-06%20of%2010-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/tree/main/demo-projects/image-instruct/04-post-op-recovery-nurse)
[![Orientation](https://img.shields.io/badge/Orientation-Portrait-orange.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)
[![DPI](https://img.shields.io/badge/DPI-300-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)

## Output Filename

`demo-projects/04-humanoid-post-op-recovery-nurse-output/figures/04-06-capability-radar-comparison.png`

## Page Size and DPI

- Letter portrait, 8.5 x 11.0 inches, 300 dpi, 2550 x 3300 pixels, white facecolor.

## Chart Type

Radar (spider) chart with 8 axes, 4 polygons.

## Title and Subtitle

- Title: `Digit V5 + Claude Tier Stack PACU Capability Radar`.
- Subtitle: `Digit + Claude/Llama vs. Neo + Claude vs. Optimus + GPT vs. Human Night-Shift Nurse`.

## Header and Footer

- Header right: `Demo 04 / Image 06 of 10 / Portrait`.
- Footer left: `Clinical-AI-Demos v0.2.0 / Demo 04 Post-Op Recovery Nurse`.
- Footer right: `DOI: 10.5281/zenodo.18445179 / MIT License`.

## Axes (8)

1. `Vitals Check On-Time Rate`.
2. `Braden Reposition On-Time Rate`.
3. `Pressure Injury Prevention Outcome`.
4. `Companion Caregiver Satisfaction NPS`.
5. `CTCAE Grade 3+ AE Detection Latency (lower better)`.
6. `Tier Routing Efficiency (Haiku to Sonnet to Llama 4)`.
7. `Patient Comfort Force Margin Below 12 N`.
8. `Per-Bed Annual Cost Efficiency`.

## Series (4)

1. `Digit V5 + Haiku 4.5 / Sonnet 4.6 / Llama 4 70B (Reference)` (Deep Navy).
2. `Neo Beta + Claude Opus 4.7 1M` (Teal).
3. `Optimus Gen 3 + GPT-5.5 Thinking` (Gold).
4. `Human Night-Shift Nurse (Baseline)` (Slate dashed).

## Layout, Annotations, matplotlib Recipe, Validation

Same conventions as prior radar instructions. Callout: `Digit V5 + tier stack leads on On-Time Rate and Tier Routing Efficiency. Neo Beta leads on Patient Comfort thanks to compliant skin. Human nurse leads on adaptive empathy at v0.2.0 freeze.`

## Validation Checklist

1. PNG is 2550 x 3300 pixels.
2. 4 polygons present.
3. 8 axis labels.
4. Reference rings.
5. Legend bottom.
6. Title, subtitle, header, footer present.
7. No em dash, no double dash, no triple dash.
8. No color outside palette.
9. No emoji.
10. Callout text present.
