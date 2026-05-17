# Image Instruction 06-10: Tele-Surgical Link Loss to Open Conversion Decision Tree

[![Demo](https://img.shields.io/badge/Demo-06-brightgreen.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/blob/main/demo-projects/06-humanoid-tele-surgical-assistant.md)
[![Image](https://img.shields.io/badge/Image-10%20of%2010-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/tree/main/demo-projects/image-instruct/06-tele-surgical-assistant)
[![Orientation](https://img.shields.io/badge/Orientation-Portrait-orange.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)
[![DPI](https://img.shields.io/badge/DPI-300-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)

## Output Filename

`demo-projects/06-humanoid-tele-surgical-assistant-output/figures/06-10-decision-tree-flowchart.png`

## Page Size and DPI

- Letter portrait, 8.5 x 11.0 inches, 300 dpi, 2550 x 3300 pixels, white facecolor.

## Chart Type

Top-down decision tree.

## Title and Subtitle

- Title: `Apollo Tele-Link Loss to Open-Conversion Decision Tree`.
- Subtitle: `Link Anomaly -> Hold -> Re-Try -> Conversion Trigger -> Apollo Manual Conversion`.

## Header and Footer

- Header right: `Demo 06 / Image 10 of 10 / Portrait`.
- Footer left: `Clinical-AI-Demos v0.2.0 / Demo 06 Tele-Surgical Assistant`.
- Footer right: `DOI: 10.5281/zenodo.18445179 / MIT License`.

## Tree Structure

```
              [Tele-Link Anomaly Detected]
                        |
              <Latency > 150 ms?>
                  |              |
                Yes             No
                  |              |
        [Apollo Hold-In-     [Continue Normal
         Place Safe Pose]     Operation]
                  |
        <Loss Duration > 3 s?>
                  |              |
                No              Yes
                  |              |
       [Resume After      [Open-Conversion
        Re-Try]            Planner Engaged]
                                  |
                          <Surgeon Authorize?>
                              |        |
                            Yes       No (Timeout 30 s)
                              |        |
                       [Apollo Open  [Apollo Auto-Convert
                        Conversion    + Local Anesthesia
                        Manual         Team Takes Over]
                        Sequence]
```

## Node Types and Colors

- Diamonds Slate.
- Forest Green: continue normal.
- Burgundy: hold and open conversion.
- Deep Navy: Apollo physical action.
- Teal: tele-link state.

## Annotations

- Pinned to Tele-Link Anomaly: `Detection via real-time RTT measurement. 150 ms threshold = baseline plus jitter ceiling.`
- Pinned to Open-Conversion Planner: `5-minute manual conversion plan from Apollo's onboard plan library. Apollo is the only entity on-site authorized.`
- Pinned to Apollo Auto-Convert: `If surgeon timeout 30 s, Apollo proceeds with stored conversion plan. Local anesthesia team takes over patient airway.`

## Layout, matplotlib Recipe, Validation

Same conventions as prior decision tree instructions.

## Validation Checklist

1. PNG is 2550 x 3300 pixels.
2. 3 decision diamonds, 5+ action rectangles.
3. Edges labeled (`Yes`, `No`).
4. Pinned annotations.
5. Title, subtitle, header, footer present.
6. No em dash, no double dash, no triple dash.
7. No color outside palette.
8. No emoji.
9. Tree fits within margins.
10. Root at top.
