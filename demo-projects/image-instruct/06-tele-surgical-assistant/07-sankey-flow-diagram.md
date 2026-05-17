# Image Instruction 06-07: Tele-Surgical Command and Confirmation Sankey

[![Demo](https://img.shields.io/badge/Demo-06-brightgreen.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/blob/main/demo-projects/06-humanoid-tele-surgical-assistant.md)
[![Image](https://img.shields.io/badge/Image-07%20of%2010-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/tree/main/demo-projects/image-instruct/06-tele-surgical-assistant)
[![Orientation](https://img.shields.io/badge/Orientation-Portrait-orange.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)
[![DPI](https://img.shields.io/badge/DPI-300-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)

## Output Filename

`demo-projects/06-humanoid-tele-surgical-assistant-output/figures/06-07-sankey-flow-diagram.png`

## Page Size and DPI

- Letter portrait, 8.5 x 11.0 inches, 300 dpi, 2550 x 3300 pixels, white facecolor.

## Chart Type

Sankey with 4 vertical levels.

## Title and Subtitle

- Title: `Apollo Tele-Whipple Command and Confirmation Sankey`.
- Subtitle: `Surgeon Console to Apollo Action to Audit - 90-Minute Procedure`.

## Header and Footer

- Header right: `Demo 06 / Image 07 of 10 / Portrait`.
- Footer left: `Clinical-AI-Demos v0.2.0 / Demo 06 Tele-Surgical Assistant`.
- Footer right: `DOI: 10.5281/zenodo.18445179 / MIT License`.

## Levels (4)

1. **Level 1 Surgeon Console Input**: `Master Manipulator Stroke`, `Voice Command`, `Confirmation Press`, `Open-Conversion Trigger`.
2. **Level 2 Tele-Link Path**: `Forward Tunnel (50 ms baseline)`, `Reverse Tunnel`, `Lost Packet Re-Try`, `Tele-Link Loss > 3 s`.
3. **Level 3 Apollo Action**: `Instrument Exchange`, `Stapler Reload`, `Irrigation Refill`, `Hold-In-Place (Safe Pose)`, `Open Conversion Setup`.
4. **Level 4 Terminal**: `Action Completed and Audited`, `Action Held Pending Confirmation`, `Open-Conversion Executed`.

## Color, Layout, Annotations, matplotlib Recipe

Same conventions as prior sankey instructions. Mauve for surgeon inputs, Slate for tele-link paths, Deep Navy for Apollo actions, Forest Green / Burgundy for terminals. Pinned callout: `100 percent of Apollo instrument exchanges gated by operator confirmation. Open-conversion executed 0 times at v0.2.0 reference iteration set.`

## Validation Checklist

1. PNG is 2550 x 3300 pixels.
2. 4 columns with all listed nodes.
3. Flow widths proportional.
4. Level titles.
5. Callout present.
6. Title, subtitle, header, footer present.
7. No em dash, no double dash, no triple dash.
8. No color outside palette.
9. No emoji.
10. Flow alpha 0.50.
