# Image Instruction 05-05: Pathology Lab Per-Specimen Margin Waterfall

[![Demo](https://img.shields.io/badge/Demo-05-brightgreen.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/blob/main/demo-projects/05-humanoid-biospecimen-pathology-lab.md)
[![Image](https://img.shields.io/badge/Image-05%20of%2010-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/tree/main/demo-projects/image-instruct/05-biospecimen-pathology-lab)
[![Orientation](https://img.shields.io/badge/Orientation-Portrait-orange.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)
[![DPI](https://img.shields.io/badge/DPI-300-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)

## Output Filename

`demo-projects/05-humanoid-biospecimen-pathology-lab-output/figures/05-05-financial-assessment-waterfall.png`

## Page Size and DPI

- Letter portrait, 8.5 x 11.0 inches, 300 dpi, 2550 x 3300 pixels, white facecolor.

## Chart Type

Vertical waterfall chart, 14 bars. Per-specimen revenue down through reagents, humanoid amortization, MCP cluster cost, and offsets to contribution margin.

## Title and Subtitle

- Title: `Phoenix Gen 8 + Gemini/Qwen MCP Pathology Per-Specimen Margin Waterfall`.
- Subtitle: `CAP-Accredited Lab - Per-Specimen Revenue to Contribution Margin - USD`.

## Header and Footer

- Header right: `Demo 05 / Image 05 of 10 / Portrait`.
- Footer left: `Clinical-AI-Demos v0.2.0 / Demo 05 Biospecimen Pathology Lab`.
- Footer right: `DOI: 10.5281/zenodo.18445179 / MIT License`.

## Bars (14)

1. `Per-Specimen List Revenue (Pathology Bundle)` (Gold positive starting).
2. `- Reagent COGS (Fixative, Paraffin, HE Stain, IHC Antibody Panel)` (Forest Green negative).
3. `- Slide and Coverslip Materials` (Forest Green negative).
4. `- Lab Bench Allocation` (Forest Green negative).
5. `- Pathologist Co-Sign Time Allocation` (Forest Green negative).
6. `- Phoenix Gen 8 Per-Specimen Amortization` (Deep Navy negative).
7. `- Gemini 3 Pro Cloud Per-Specimen Inference` (Teal negative).
8. `- Qwen3 72B On-Prem Per-Specimen Inference Share` (Teal darker negative).
9. `- MCP Server Per-Specimen Overhead` (Mauve negative).
10. `- CAP Q-Probes Audit Append Per-Specimen` (Burgundy negative).
11. `- Reagent Waste and Re-Stain Reserve` (Slate negative).
12. `+ Turnaround Time Premium` (Gold positive).
13. `+ Sponsor Trial IHC Surcharge` (Gold positive).
14. `Per-Specimen Contribution Margin` (Deep Navy total).

## Annotations, Layout, matplotlib Recipe, Validation

Same conventions as prior waterfall instructions. Baseline at 0 labeled `Break-Even`. Callout: `Turnaround premium and Sponsor IHC surcharge offset Phoenix amortization within first 100 specimens at v0.2.0.`

## Validation Checklist

1. PNG is 2550 x 3300 pixels.
2. 14 bars with connectors.
3. Break-even reference line.
4. Callout box.
5. Title, subtitle, header, footer present.
6. No em dash, no double dash, no triple dash.
7. No color outside palette.
8. No emoji.
9. Bar labels readable, unclipped.
10. Final margin bar from 0 to total.
