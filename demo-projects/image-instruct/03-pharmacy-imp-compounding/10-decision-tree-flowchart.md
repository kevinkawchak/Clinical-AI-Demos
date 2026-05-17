# Image Instruction 03-10: Pharmacy CAR-T Particle Excursion Decision Tree

[![Demo](https://img.shields.io/badge/Demo-03-brightgreen.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/blob/main/demo-projects/03-humanoid-pharmacy-imp-compounding.md)
[![Image](https://img.shields.io/badge/Image-10%20of%2010-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/tree/main/demo-projects/image-instruct/03-pharmacy-imp-compounding)
[![Orientation](https://img.shields.io/badge/Orientation-Portrait-orange.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)
[![DPI](https://img.shields.io/badge/DPI-300-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)

## Output Filename

`demo-projects/03-humanoid-pharmacy-imp-compounding-output/figures/03-10-decision-tree-flowchart.png`

## Page Size and DPI

- Letter portrait, 8.5 x 11.0 inches, 300 dpi, 2550 x 3300 pixels, white facecolor.

## Chart Type

Top-down decision tree flowchart for an ISO 14644-1 particle excursion event during compounding.

## Title and Subtitle

- Title: `Figure 03 + GPT-5.5 Thinking Particle Excursion Decision Tree`.
- Subtitle: `ISO 14644-1 Class 5 Excursion Detected -> Triage -> Recover or Abort Batch`.

## Header and Footer

- Header right: `Demo 03 / Image 10 of 10 / Portrait`.
- Footer left: `Clinical-AI-Demos v0.2.0 / Demo 03 Pharmacy IMP Compounding`.
- Footer right: `DOI: 10.5281/zenodo.18445179 / MIT License`.

## Tree Structure

```
            [Particle Excursion Detected]
                        |
              <Particle Count vs. Threshold>
                  |              |
            <= 3520/m^3    > 3520/m^3 (Class 5 ceiling)
                  |              |
        [Log + Continue]   [Figure 03 Halt-In-Place]
                                  |
                          <Duration > 30 s?>
                              |        |
                            No        Yes
                              |        |
                       [Resume After  [Abort Batch -
                        Re-Test]       USP 800 Disposal]
                              |              |
                       [GPT-5.5 Append   [Cryo Re-Store
                        Reason Log]      Patient T Cells]
                                            |
                                  [Schedule Re-Compounding]
```

## Node Types and Colors

- Diamonds (Slate): decision points.
- Forest Green rectangles: pass-through resume.
- Burgundy rectangles: abort batch and disposal.
- Mauve rectangles: cryo re-store and re-compounding.
- Teal rectangles: GPT-5.5 Thinking log append.

## Annotations

- Pinned to Particle Count diamond: `ISO 14644-1 Class 5 ceiling 3520 particles per m^3 at >= 0.5 micron.`
- Pinned to Halt-In-Place: `5 ms surgical-grade E-stop. Cumulative tip force frozen at last reading.`
- Pinned to Abort Batch: `USP 800 hazardous-disposal chain-of-custody. Patient T cells re-cryo within 8 minutes.`

## Layout, matplotlib Recipe

Same conventions as 01-10 and 02-10.

## Validation Checklist

1. PNG is 2550 x 3300 pixels.
2. Root node at top, leaves at bottom.
3. 3 decision diamonds, 5+ action rectangles.
4. All edges labeled.
5. Three pinned annotations.
6. Title, subtitle, header, footer present.
7. `m^3` notation appears correctly.
8. No em dash, no double dash, no triple dash.
9. No color outside palette.
10. No emoji.
