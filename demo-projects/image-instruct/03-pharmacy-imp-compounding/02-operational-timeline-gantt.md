# Image Instruction 03-02: Figure 03 4-Hour CAR-T Compounding Gantt Swimlane

[![Demo](https://img.shields.io/badge/Demo-03-brightgreen.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/blob/main/demo-projects/03-humanoid-pharmacy-imp-compounding.md)
[![Image](https://img.shields.io/badge/Image-02%20of%2010-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/tree/main/demo-projects/image-instruct/03-pharmacy-imp-compounding)
[![Orientation](https://img.shields.io/badge/Orientation-Landscape-orange.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)
[![DPI](https://img.shields.io/badge/DPI-300-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)

## Output Filename

`demo-projects/03-humanoid-pharmacy-imp-compounding-output/figures/03-02-operational-timeline-gantt.png`

## Page Size and DPI

- Letter landscape, 11.0 x 8.5 inches, 300 dpi, 3300 x 2550 pixels, white facecolor.

## Chart Type

Gantt swimlane timeline of the 4-hour CAR-T compounding session at 1 minute Gantt block resolution. Overlay the 10 Hz GPT-5.5 Thinking tick spark across the top. 7 swimlanes covering biosafety cabinet activity, reagent handling, particle count audit, biosafety cabinet airflow audit, IEC 62304 verification gates, USP 800 hazardous-handling gates, and 21 CFR § 211 batch record append.

## Title and Subtitle

- Title: `Figure 03 + GPT-5.5 Thinking 4-Hour CAR-T Compounding Gantt`.
- Subtitle: `PAT-IMP-0001 - 14,400 s, 144,000 LLM Ticks, 1,440,000 Humanoid Motion Ticks at 100 Hz`.

## Header and Footer

- Header right: `Demo 03 / Image 02 of 10 / Landscape`.
- Footer left: `Clinical-AI-Demos v0.2.0 / Demo 03 Pharmacy IMP Compounding`.
- Footer right: `DOI: 10.5281/zenodo.18445179 / MIT License`.

## Swimlanes Top to Bottom

1. `GPT-5.5 Thinking 10 Hz Tick Overlay` (Teal sparks, sampled).
2. `Biosafety Cabinet Manipulation` (Deep Navy).
3. `Reagent Aliquot Transfers` (Mauve).
4. `Particle Count Sampling (ISO 14644-1)` (Slate).
5. `Biosafety Cabinet Airflow Audit` (Slate lighter).
6. `IEC 62304 Verification Gates` (Burgundy).
7. `USP 800 Hazardous-Handling Gates` (Burgundy darker).
8. `21 CFR § 211 Batch Record Append` (Gold).

(7 task lanes plus 1 overlay row.)

## Time Markers and Annotations

- Vertical dashed Light Gray lines every 30 minutes (8 ticks across 4 hours).
- Highlight CAR-T expansion window (typically minute 60 to 180) as a Forest Green band labeled `T-Cell Expansion Window`.
- Pinned annotation at minute 200: `Compounded bag verified, batch record sealed, IMP manifest sent to Sponsor (Demo 02) at minute 240.`

## matplotlib Recipe

- `broken_barh` per swimlane.
- X axis from 00:00 to 04:00 in HH:MM format.
- GPT-5.5 Thinking ticks sampled at 1 per second and plotted as Teal vertical sparks.

## Validation Checklist

1. PNG is 3300 x 2550 pixels.
2. 7 task swimlanes + 1 LLM overlay row.
3. 30-minute dashed separators visible.
4. T-Cell Expansion Forest Green band visible from minute 60 to 180.
5. Title, subtitle, header, footer present.
6. `§` in `21 CFR § 211`.
7. No em dash, no double dash, no triple dash.
8. No color outside palette.
9. No emoji.
10. Pinned annotation present at minute 200.
