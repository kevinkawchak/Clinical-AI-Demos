# Image Instruction 03-05: Pharmacy CAR-T Per-Batch Margin Waterfall

[![Demo](https://img.shields.io/badge/Demo-03-brightgreen.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/blob/main/demo-projects/03-humanoid-pharmacy-imp-compounding.md)
[![Image](https://img.shields.io/badge/Image-05%20of%2010-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/tree/main/demo-projects/image-instruct/03-pharmacy-imp-compounding)
[![Orientation](https://img.shields.io/badge/Orientation-Portrait-orange.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)
[![DPI](https://img.shields.io/badge/DPI-300-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)

## Output Filename

`demo-projects/03-humanoid-pharmacy-imp-compounding-output/figures/03-05-financial-assessment-waterfall.png`

## Page Size and DPI

- Letter portrait, 8.5 x 11.0 inches, 300 dpi, 2550 x 3300 pixels, white facecolor.

## Chart Type

Vertical per-batch margin waterfall, 14 bars. Walks from CAR-T list price down through cost-of-goods, compounding overhead, regulatory reserve, batch failure reserve, and offsets from Figure 03 + GPT-5.5 Thinking efficiency to the per-batch contribution margin.

## Title and Subtitle

- Title: `Figure 03 + GPT-5.5 Thinking CAR-T Per-Batch Margin Waterfall`.
- Subtitle: `Per-Patient List Price to Pharmacy Contribution Margin - PAT-IMP-0001 - USD Thousands`.

## Header and Footer

- Header right: `Demo 03 / Image 05 of 10 / Portrait`.
- Footer left: `Clinical-AI-Demos v0.2.0 / Demo 03 Pharmacy IMP Compounding`.
- Footer right: `DOI: 10.5281/zenodo.18445179 / MIT License`.

## Bars (14, left to right)

1. `CAR-T Per-Patient List Price` (Gold positive starting bar).
2. `- Lentiviral Vector COGS` (Forest Green negative).
3. `- Apheresis Service Fee` (Forest Green negative).
4. `- Cytokine Cocktail COGS` (Forest Green negative).
5. `- Class 5 Clean Room Allocation` (Forest Green negative).
6. `- Pharmacist Oversight (Reduced)` (Forest Green negative).
7. `- Figure 03 Per-Batch Amortization` (Deep Navy negative).
8. `- GPT-5.5 Thinking Per-Batch Inference Cost` (Teal negative).
9. `- IEC 62304 Class C Verifier Per-Batch Cost` (Burgundy negative).
10. `- USP 800 Hazardous Disposal Per-Batch` (Burgundy negative).
11. `- Batch Failure Reserve (Modeled)` (Slate negative).
12. `+ Cell Viability Premium (vs. Manual)` (Forest Green positive).
13. `+ FDA RTCT Accelerated Reimbursement` (Gold positive).
14. `Per-Batch Contribution Margin` (Deep Navy total).

## Annotations

- Horizontal dashed reference line at `+0` labeled `Break-Even`.
- Callout box top-right: `Cell viability premium and FDA RTCT accelerated reimbursement together more than offset the Figure 03 amortization. Net per-batch margin positive at v0.2.0 reference.`

## Layout and matplotlib Recipe

Same conventions as 01-05 and 02-05.

## Validation Checklist

1. PNG is 2550 x 3300 pixels.
2. 14 bars with connectors.
3. Final margin bar from 0 to total.
4. Break-even dashed reference line.
5. Callout box top-right.
6. Title, subtitle, header, footer present.
7. No em dash, no double dash, no triple dash.
8. No color outside palette.
9. No emoji.
10. Bar labels readable, unclipped.
