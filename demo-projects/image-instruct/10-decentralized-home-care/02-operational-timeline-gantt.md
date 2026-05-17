# Image Instruction 10-02: Figure 03 Field Edition 24-Hour Home DCT Gantt

[![Demo](https://img.shields.io/badge/Demo-10-brightgreen.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/blob/main/demo-projects/10-humanoid-decentralized-home-care.md)
[![Image](https://img.shields.io/badge/Image-02%20of%2010-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/tree/main/demo-projects/image-instruct/10-decentralized-home-care)
[![Orientation](https://img.shields.io/badge/Orientation-Landscape-orange.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)
[![DPI](https://img.shields.io/badge/DPI-300-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)

## Output Filename

`demo-projects/10-humanoid-decentralized-home-care-output/figures/10-02-operational-timeline-gantt.png`

## Page Size and DPI

- Letter landscape, 11.0 x 8.5 inches, 300 dpi, 3300 x 2550 pixels, white facecolor.

## Chart Type

Gantt swimlane covering 24 hours, split into 4-hour active visit window plus 20-hour ambient monitoring window. 9 task lanes + 2 LLM overlay rows.

## Title and Subtitle

- Title: `Figure 03 Field Edition + Claude Haiku 4.5 Edge 24-Hour Home DCT Gantt`.
- Subtitle: `PAT-DCT-0001 - 4-Hour Active Visit at 1 Hz (14,400 ticks) + 20-Hour Ambient at 0.1 Hz (7,200 ticks)`.

## Header and Footer

- Header right: `Demo 10 / Image 02 of 10 / Landscape`.
- Footer left: `Clinical-AI-Demos v0.2.0 / Demo 10 Decentralized Home Care`.
- Footer right: `DOI: 10.5281/zenodo.18445179 / MIT License`.

## Swimlanes Top to Bottom

LLM overlays:

1. `Claude Haiku 4.5 1 Hz Active Visit Ticks` (Teal sparks during 4-hour visit only).
2. `Claude Haiku 4.5 0.1 Hz Ambient Monitoring Ticks` (Teal lighter sparks during 20-hour ambient).

Task lanes:

3. `Patient Vitals Capture` (Mauve).
4. `Olaparib Pill Adherence Check` (Slate).
5. `Lu-177 Infusion Reminder Window` (Burgundy).
6. `ECOG 2 Mobility Assist` (Deep Navy).
7. `Patient Self-Report Tablet Round-Up` (Slate lighter).
8. `Family Caregiver Update Push (Patient Approved Only)` (Gold).
9. `Per-Cycle Federated Aggregator Submission` (Forest Green).
10. `HR 9507 Revocation Check (Per-Cycle)` (Burgundy darker).
11. `Figure 03 Charge Dock Window (Overnight)` (Slate).

## Time Markers and Annotations

- Vertical dashed Light Gray line at end of 4-hour active visit window labeled `Active Visit -> Ambient Monitoring`.
- Vertical dashed Light Gray line at midnight labeled `Overnight Charge Dock + Ambient Cadence Continues`.
- Pinned annotation at hour 3 (active visit): `Lu-177 infusion reminder window. Patient self-administers; Figure 03 verifies via pill box RFID and bedside camera.`
- Pinned annotation at hour 23: `End-of-cycle de-identified summary encoded and queued for federated aggregator. HR 9507 revocation flag checked one last time.`

## matplotlib Recipe

Same conventions as prior gantt instructions. X axis: 00:00 to 24:00 spanning 24 hours.

## Validation Checklist

1. PNG is 3300 x 2550 pixels.
2. 9 task lanes + 2 LLM overlay rows.
3. Active visit vs ambient split visible.
4. Overnight charge dock window labeled.
5. Pinned annotations at hour 3 and hour 23.
6. Title, subtitle, header, footer present.
7. No em dash, no double dash, no triple dash.
8. No color outside palette.
9. No emoji.
10. HR 9507 reference correct.
