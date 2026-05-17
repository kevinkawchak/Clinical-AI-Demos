# Image Instruction 03-07: Pharmacy CAR-T Material and Cell Flow Sankey

[![Demo](https://img.shields.io/badge/Demo-03-brightgreen.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/blob/main/demo-projects/03-humanoid-pharmacy-imp-compounding.md)
[![Image](https://img.shields.io/badge/Image-07%20of%2010-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/tree/main/demo-projects/image-instruct/03-pharmacy-imp-compounding)
[![Orientation](https://img.shields.io/badge/Orientation-Portrait-orange.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)
[![DPI](https://img.shields.io/badge/DPI-300-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)

## Output Filename

`demo-projects/03-humanoid-pharmacy-imp-compounding-output/figures/03-07-sankey-flow-diagram.png`

## Page Size and DPI

- Letter portrait, 8.5 x 11.0 inches, 300 dpi, 2550 x 3300 pixels, white facecolor.

## Chart Type

Sankey with 4 vertical levels. Flow widths proportional to cell count or reagent volume per step.

## Title and Subtitle

- Title: `Figure 03 CAR-T Material and Cell Flow Sankey`.
- Subtitle: `Apheresis Bag to Compounded CAR-T Infusion Bag - 4-Hour Session - PAT-IMP-0001`.

## Header and Footer

- Header right: `Demo 03 / Image 07 of 10 / Portrait`.
- Footer left: `Clinical-AI-Demos v0.2.0 / Demo 03 Pharmacy IMP Compounding`.
- Footer right: `DOI: 10.5281/zenodo.18445179 / MIT License`.

## Levels (4 columns)

1. **Level 1 Raw Inputs**: `Apheresis Bag (Patient T Cells)`, `Lentiviral Vector`, `IL-2 Cytokine`, `IL-7 Cytokine`, `IL-15 Cytokine`, `Wash Buffer`.
2. **Level 2 Figure 03 Step**: `Bag Open and Aliquot`, `Vector Co-Culture`, `Cytokine Addition`, `Expansion Bag Transfer`, `Wash Cycle`, `Final Concentration`.
3. **Level 3 GPT-5.5 Thinking Verdict**: `Pass`, `Re-Run Step`, `Escalate to Pharmacist`.
4. **Level 4 Terminal Outputs**: `Compounded CAR-T Infusion Bag`, `Discard (USP 800 Stream)`, `Quality Hold for Manual Review`, `Re-Cryo and Re-Run`.

## Flow Color Mapping

- Mauve flows for T-cell streams.
- Burgundy flows for vector and cytokines.
- Forest Green flows for Pass to Compounded Bag.
- Gold flows for Re-Run.
- Slate flows for Discard / Quality Hold.

## Layout, Annotations, matplotlib Recipe

Same conventions as 01-07 and 02-07. Pinned callout: `Cell viability conserved across expansion thanks to 8 N tip-force ceiling. Approximately 95 percent of Figure 03 steps reach Pass at first attempt.`

## Validation Checklist

1. PNG is 2550 x 3300 pixels.
2. 4 columns with all listed nodes.
3. Flow widths proportional and colored by source.
4. Level titles at top of each column.
5. Pinned callout present.
6. Title, subtitle, header, footer present.
7. No em dash, no double dash, no triple dash.
8. No color outside palette.
9. No emoji.
10. Flow alpha 0.50.
