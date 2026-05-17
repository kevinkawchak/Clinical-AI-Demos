# Image Instruction 06-05: Tele-Surgical Per-Procedure Margin Waterfall

[![Demo](https://img.shields.io/badge/Demo-06-brightgreen.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/blob/main/demo-projects/06-humanoid-tele-surgical-assistant.md)
[![Image](https://img.shields.io/badge/Image-05%20of%2010-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/tree/main/demo-projects/image-instruct/06-tele-surgical-assistant)
[![Orientation](https://img.shields.io/badge/Orientation-Portrait-orange.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)
[![DPI](https://img.shields.io/badge/DPI-300-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)

## Output Filename

`demo-projects/06-humanoid-tele-surgical-assistant-output/figures/06-05-financial-assessment-waterfall.png`

## Page Size and DPI

- Letter portrait, 8.5 x 11.0 inches, 300 dpi, 2550 x 3300 pixels, white facecolor.

## Chart Type

Vertical waterfall, 14 bars. Per-procedure (Whipple) revenue to contribution margin.

## Title and Subtitle

- Title: `Apollo + Claude Opus 4.7 1M Tele-Whipple Per-Procedure Margin Waterfall`.
- Subtitle: `Per-Procedure Revenue to Contribution Margin - Critical-Access Rural Site - USD Thousands`.

## Header and Footer

- Header right: `Demo 06 / Image 05 of 10 / Portrait`.
- Footer left: `Clinical-AI-Demos v0.2.0 / Demo 06 Tele-Surgical Assistant`.
- Footer right: `DOI: 10.5281/zenodo.18445179 / MIT License`.

## Bars (14)

1. `Per-Procedure CMS Reimbursement` (Gold positive starting).
2. `- da Vinci SP Per-Case Disposable` (Forest Green negative).
3. `- Surgical Tray and Reload COGS` (Forest Green negative).
4. `- Critical-Access Hospital OR Allocation` (Forest Green negative).
5. `- Anesthesia and PACU Allocation` (Forest Green negative).
6. `- Apollo Per-Procedure Amortization` (Deep Navy negative).
7. `- Claude Opus 4.7 1M On-Prem Inference Per-Procedure` (Teal negative).
8. `- DOD-Grade Tele-Link Subscription Per-Procedure` (Burgundy negative).
9. `- Remote Surgeon Tele-Time` (Slate negative).
10. `- Operator-In-Loop Console Per-Procedure` (Slate negative).
11. `- Open-Conversion Reserve Per-Procedure` (Burgundy darker negative).
12. `+ Avoided 220-Mile Patient Transfer Cost Offset` (Forest Green positive).
13. `+ Same-Day Surgery Premium` (Gold positive).
14. `Per-Procedure Contribution Margin` (Deep Navy total).

## Annotations

- Break-even reference line at 0.
- Callout: `Avoided 220-mile patient transfer cost offset is the largest single contributor to margin at v0.2.0 reference.`

## Layout and matplotlib Recipe

Same conventions as prior waterfall instructions.

## Validation Checklist

1. PNG is 2550 x 3300 pixels.
2. 14 bars with connectors.
3. Break-even line.
4. Callout.
5. Title, subtitle, header, footer present.
6. No em dash, no double dash, no triple dash.
7. No color outside palette.
8. No emoji.
9. Bar labels unclipped.
10. Cumulative bar last.
