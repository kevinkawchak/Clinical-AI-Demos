# Image Instruction 09-05: Radiation Oncology Per-Fraction Margin Waterfall

[![Demo](https://img.shields.io/badge/Demo-09-brightgreen.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/blob/main/demo-projects/09-humanoid-radiation-oncology-technologist.md)
[![Image](https://img.shields.io/badge/Image-05%20of%2010-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/tree/main/demo-projects/image-instruct/09-radiation-oncology-technologist)
[![Orientation](https://img.shields.io/badge/Orientation-Portrait-orange.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)
[![DPI](https://img.shields.io/badge/DPI-300-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)

## Output Filename

`demo-projects/09-humanoid-radiation-oncology-technologist-output/figures/09-05-financial-assessment-waterfall.png`

## Page Size and DPI

- Letter portrait, 8.5 x 11.0 inches, 300 dpi, 2550 x 3300 pixels, white facecolor.

## Chart Type

Vertical waterfall, 16 bars covering per-fraction margin.

## Title and Subtitle

- Title: `Atlas + Optimus + GR00T/Cosmos/Claude LINAC Per-Fraction Margin Waterfall`.
- Subtitle: `Single-Fraction 16 Gy SRS Per-Patient Revenue to Margin - USD Thousands`.

## Header and Footer

- Header right: `Demo 09 / Image 05 of 10 / Portrait`.
- Footer left: `Clinical-AI-Demos v0.2.0 / Demo 09 Radiation Oncology Technologist`.
- Footer right: `DOI: 10.5281/zenodo.18445179 / MIT License`.

## Bars (16)

1. `Per-Fraction CMS HCPCS Reimbursement` (Gold positive starting).
2. `- Varian Edge LINAC Per-Fraction Amortization` (Forest Green negative).
3. `- HyperArc Plan Per-Patient Cost` (Forest Green negative).
4. `- 6D Couch Per-Patient Maintenance` (Forest Green negative).
5. `- Atlas Electric Per-Fraction Amortization` (Deep Navy negative).
6. `- Optimus Gen 3 Per-Fraction Amortization` (Deep Navy lighter negative).
7. `- NVIDIA DGX SuperPOD Per-Fraction Share (GR00T + Cosmos)` (Teal lighter negative).
8. `- Claude Opus 4.7 1M Arbiter Per-Fraction Inference` (Teal darker negative).
9. `- AAPM TG-100 + TG-142 QA Per-Fraction` (Burgundy negative).
10. `- NRC 10 CFR § 35 Compliance Reserve` (Burgundy darker negative).
11. `- Medical Physicist Co-Sign Per-Fraction` (Slate negative).
12. `+ Throughput Premium (10 vs 6 Patients per Day)` (Forest Green positive).
13. `+ Same-Day Setup-to-Beam-On Premium` (Gold positive).
14. `+ AAPM TG-100 Risk-Informed QM Premium` (Gold positive).
15. `+ Adaptive RT DT Update (Digital Twin Cross-Sell)` (Mauve positive).
16. `Per-Fraction Contribution Margin` (Deep Navy total).

## Annotations

- Break-even reference at 0 labeled.
- Callout: `Throughput Premium and Setup Time Premium together offset NVIDIA DGX SuperPOD share. AAPM TG-100 Premium is the third largest contributor at v0.2.0.`

## Layout and matplotlib Recipe

Same conventions as prior waterfall instructions.

## Validation Checklist

1. PNG is 2550 x 3300 pixels.
2. 16 bars with connectors.
3. Cumulative bar.
4. Break-even reference line.
5. Callout.
6. Title, subtitle, header, footer present.
7. `§` in `NRC 10 CFR § 35`.
8. No em dash, no double dash, no triple dash.
9. No color outside palette.
10. No emoji.
