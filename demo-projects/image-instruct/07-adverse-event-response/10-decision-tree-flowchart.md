# Image Instruction 07-10: AE Cross-Site Rotation Decision Tree

[![Demo](https://img.shields.io/badge/Demo-07-brightgreen.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/blob/main/demo-projects/07-humanoid-24-7-adverse-event-response.md)
[![Image](https://img.shields.io/badge/Image-10%20of%2010-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/tree/main/demo-projects/image-instruct/07-adverse-event-response)
[![Orientation](https://img.shields.io/badge/Orientation-Portrait-orange.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)
[![DPI](https://img.shields.io/badge/DPI-300-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)

## Output Filename

`demo-projects/07-humanoid-24-7-adverse-event-response-output/figures/07-10-decision-tree-flowchart.png`

## Page Size and DPI

- Letter portrait, 8.5 x 11.0 inches, 300 dpi, 2550 x 3300 pixels, white facecolor.

## Chart Type

Top-down decision tree.

## Title and Subtitle

- Title: `3x H2 + Per-Site Claude Opus AE Cross-Site Rotation Decision Tree`.
- Subtitle: `Cross-Site AE Surge Detected - Local Capacity - Transit - H2 Re-Dispatch`.

## Header and Footer

- Header right: `Demo 07 / Image 10 of 10 / Portrait`.
- Footer left: `Clinical-AI-Demos v0.2.0 / Demo 07 Adverse Event Response`.
- Footer right: `DOI: 10.5281/zenodo.18445179 / MIT License`.

## Tree Structure

```
              [Cross-Site AE Surge Detected]
                        |
              <Local Site Has H2?>
                  |              |
                Yes             No
                  |              |
        [Local H2          <Cross-Site Transit Feasible?>
         Responds]              |              |
                              Yes             No (Severe Weather, NOTAM)
                                |              |
                    <Distance to Nearest H2?>  [Activate Human On-Call
                          |        |            Backup Per Site]
                       < 500 mi  > 500 mi
                          |        |
                 [FAA Drone   [Hospital
                  Transit]     Charter
                              Aircraft]
                                |
                         [H2 Bedside
                          Arrival < 30 min SLA]
```

## Node Types and Colors

- Diamonds Slate.
- Forest Green: local response.
- Deep Navy: H2 actions.
- Mauve: transit modality.
- Burgundy: human on-call backup.

## Annotations

- Pinned to Cross-Site AE Surge: `Detected when per-site Claude Opus reports >= 2 concurrent CTCAE Grade 3+ events.`
- Pinned to FAA Drone Transit: `FAA Part 135 medical drone. H2 folded onto drone platform. Battery hot-swap during transit.`
- Pinned to Hospital Charter Aircraft: `Hospital-charter aircraft from the nearest H2-resident site to the surge site within 30 min SLA.`

## Layout, matplotlib Recipe, Validation

Same conventions as prior decision tree instructions.

## Validation Checklist

1. PNG is 2550 x 3300 pixels.
2. 3 decision diamonds, 5+ action rectangles.
3. Edges labeled (`Yes`, `No`, distance bands).
4. Pinned annotations.
5. Title, subtitle, header, footer present.
6. No em dash, no double dash, no triple dash.
7. No color outside palette.
8. No emoji.
9. Tree fits within margins.
10. Root at top.
