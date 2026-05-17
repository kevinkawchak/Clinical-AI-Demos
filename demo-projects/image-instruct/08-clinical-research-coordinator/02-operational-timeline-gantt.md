# Image Instruction 08-02: Neo Beta 8-Hour CRC Shift Gantt Swimlane

[![Demo](https://img.shields.io/badge/Demo-08-brightgreen.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/blob/main/demo-projects/08-humanoid-clinical-research-coordinator.md)
[![Image](https://img.shields.io/badge/Image-02%20of%2010-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/tree/main/demo-projects/image-instruct/08-clinical-research-coordinator)
[![Orientation](https://img.shields.io/badge/Orientation-Landscape-orange.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)
[![DPI](https://img.shields.io/badge/DPI-300-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)

## Output Filename

`demo-projects/08-humanoid-clinical-research-coordinator-output/figures/08-02-operational-timeline-gantt.png`

## Page Size and DPI

- Letter landscape, 11.0 x 8.5 inches, 300 dpi, 3300 x 2550 pixels, white facecolor.

## Chart Type

Gantt swimlane across the 8-hour CRC shift (09:00 to 17:00 PDT). 9 task lanes + 3 LLM ensemble overlay rows.

## Title and Subtitle

- Title: `Neo Beta + Multi-Model Ensemble CRC 8-Hour Shift Gantt`.
- Subtitle: `TRIAL-NSCLC-3A - 12 Patients (8 New, 4 Follow-Up) - 28,800 LLM Ticks at 1 Hz`.

## Header and Footer

- Header right: `Demo 08 / Image 02 of 10 / Landscape`.
- Footer left: `Clinical-AI-Demos v0.2.0 / Demo 08 Clinical Research Coordinator`.
- Footer right: `DOI: 10.5281/zenodo.18445179 / MIT License`.

## Swimlanes Top to Bottom

LLM overlays:

1. `Claude Opus 4.7 Calls (Medical Reasoning)` (Teal sparks).
2. `Gemini 3 Pro Calls (Multi-Language)` (Teal lighter triangles).
3. `GPT-5.5 Thinking Calls (Stipend Payment)` (Teal darker squares).

Task lanes:

4. `New-Patient Consult Slots (8 x 30 min)` (Mauve).
5. `Follow-Up Consult Slots (4 x 15 min)` (Mauve darker).
6. `Multi-Language Consent Recital Per-Patient` (Forest Green).
7. `HR 9501 Patient Self-Selection Capture` (Burgundy).
8. `HR 9502 Humanoid Choice Capture` (Burgundy darker).
9. `HR 9503 Procedural Modification Capture` (Burgundy darkest).
10. `HR 9507 Data Self-Custody Capture` (Burgundy mid).
11. `Stipend Payment Authorization Window` (Gold).
12. `IRB Daily Audit Log Append` (Slate).

## Time Markers and Annotations

- Vertical dashed Light Gray lines every 1 hour.
- Highlight the lunch window 12:00 to 13:00 as Light Gray band labeled `Lunch (Neo Beta Charge)`.
- Pinned annotation at 11:30: `8 new patient consents completed by mid-day. 5 language distributions logged.`
- Pinned annotation at 16:30: `End-of-day stipend payment batch authorized. IRB consent audit log sealed.`

## matplotlib Recipe

Same conventions as prior gantt instructions. X axis 09:00 to 17:00.

## Validation Checklist

1. PNG is 3300 x 2550 pixels.
2. 9 task lanes + 3 LLM overlay rows.
3. Hourly separators.
4. Lunch window highlighted.
5. Pinned annotations.
6. Title, subtitle, header, footer present.
7. No em dash, no double dash, no triple dash.
8. No color outside palette.
9. No emoji.
10. HR 9501 to 9507 references correct.
