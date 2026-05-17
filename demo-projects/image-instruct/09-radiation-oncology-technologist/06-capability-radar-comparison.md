# Image Instruction 09-06: Radiation Oncology Capability Radar

[![Demo](https://img.shields.io/badge/Demo-09-brightgreen.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/blob/main/demo-projects/09-humanoid-radiation-oncology-technologist.md)
[![Image](https://img.shields.io/badge/Image-06%20of%2010-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/tree/main/demo-projects/image-instruct/09-radiation-oncology-technologist)
[![Orientation](https://img.shields.io/badge/Orientation-Portrait-orange.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)
[![DPI](https://img.shields.io/badge/DPI-300-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)

## Output Filename

`demo-projects/09-humanoid-radiation-oncology-technologist-output/figures/09-06-capability-radar-comparison.png`

## Page Size and DPI

- Letter portrait, 8.5 x 11.0 inches, 300 dpi, 2550 x 3300 pixels, white facecolor.

## Chart Type

Radar (spider) chart, 8 axes, 4 polygons.

## Title and Subtitle

- Title: `Atlas + Optimus + GR00T/Cosmos/Claude LINAC Capability Radar`.
- Subtitle: `Reference vs. Single Humanoid Atlas Only vs. Optimus Only vs. Human RT Tech Team Baseline`.

## Header and Footer

- Header right: `Demo 09 / Image 06 of 10 / Portrait`.
- Footer left: `Clinical-AI-Demos v0.2.0 / Demo 09 Radiation Oncology Technologist`.
- Footer right: `DOI: 10.5281/zenodo.18445179 / MIT License`.

## Axes (8)

1. `Setup-to-Beam-On Time (lower better)`.
2. `Per-Fraction Throughput`.
3. `Sub-Millimeter Alignment Reproducibility`.
4. `Claude Opus Arbiter Gate Adherence`.
5. `NRC 10 CFR § 35 Compliance Confidence`.
6. `AAPM TG-100 + TG-142 QA Completeness`.
7. `1.5 m Inter-Humanoid Distance Maintenance`.
8. `Per-Fraction Cost Efficiency`.

## Series (4)

1. `Atlas + Optimus + GR00T/Cosmos/Claude Arbiter (Reference)` Deep Navy.
2. `Atlas Only + Claude Opus 4.7 1M` Teal.
3. `Optimus Only + Claude Opus 4.7 1M` Gold.
4. `Human RT Tech Team (Baseline)` Slate dashed.

## Layout, Annotations, matplotlib Recipe, Validation

Same conventions as prior radar instructions. Callout: `Dual-humanoid reference stack leads on Throughput and Setup-to-Beam-On Time thanks to parallel Atlas patient handling and Optimus machine operation. Single humanoid loses parallelism.`

## Validation Checklist

1. PNG is 2550 x 3300 pixels.
2. 4 polygons.
3. 8 axis labels.
4. Reference rings.
5. Legend.
6. Title, subtitle, header, footer present.
7. `§` in `NRC 10 CFR § 35`.
8. No em dash, no double dash, no triple dash.
9. No color outside palette.
10. No emoji.
