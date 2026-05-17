# Image Instruction 09-02: LINAC 8-Hour 10-Patient SRS Gantt Swimlane

[![Demo](https://img.shields.io/badge/Demo-09-brightgreen.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/blob/main/demo-projects/09-humanoid-radiation-oncology-technologist.md)
[![Image](https://img.shields.io/badge/Image-02%20of%2010-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/tree/main/demo-projects/image-instruct/09-radiation-oncology-technologist)
[![Orientation](https://img.shields.io/badge/Orientation-Landscape-orange.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)
[![DPI](https://img.shields.io/badge/DPI-300-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)

## Output Filename

`demo-projects/09-humanoid-radiation-oncology-technologist-output/figures/09-02-operational-timeline-gantt.png`

## Page Size and DPI

- Letter landscape, 11.0 x 8.5 inches, 300 dpi, 3300 x 2550 pixels, white facecolor.

## Chart Type

Gantt swimlane covering the 8-hour SRS treatment shift (08:00 to 16:00 PDT). 9 task lanes + 3 LLM overlay rows.

## Title and Subtitle

- Title: `Atlas + Optimus Dual-Humanoid LINAC 8-Hour SRS Gantt`.
- Subtitle: `10 Glioblastoma Patients, Single-Fraction 16 Gy, HyperArc Plan, 100 ms LLM Cadence`.

## Header and Footer

- Header right: `Demo 09 / Image 02 of 10 / Landscape`.
- Footer left: `Clinical-AI-Demos v0.2.0 / Demo 09 Radiation Oncology Technologist`.
- Footer right: `DOI: 10.5281/zenodo.18445179 / MIT License`.

## Swimlanes Top to Bottom

LLM overlays:

1. `GR00T N1.6 Humanoid Foundation Model Calls` (Teal sparks).
2. `Cosmos Reason 2 VLM Calls` (Teal lighter triangles).
3. `Claude Opus 4.7 Arbiter Decisions (3 gates per patient)` (Teal darker squares).

Task lanes (per patient or per device):

4. `Patient Setup and Mask Verification (Atlas)` (Deep Navy).
5. `kV CBCT Alignment Check (Optimus Console)` (Mauve).
6. `Plan Verification and Authorization Gate` (Burgundy).
7. `HyperArc Beam-On` (Forest Green).
8. `6D Couch Re-Position Inter-Arc` (Slate).
9. `Post-Treatment Dose Report Append` (Gold).
10. `AAPM TG-142 LINAC QA Snapshot` (Slate lighter).
11. `Inter-Patient Atlas Patient Egress + Optimus Bay Reset` (Mauve darker).
12. `Lunch Window (12:00 to 12:30, no patient on couch)` (Light Gray).

## Time Markers and Annotations

- Vertical dashed Light Gray lines every 1 hour.
- 10 colored bands across the bottom indicating per-patient slots (typically 45 minutes each).
- Pinned annotation at minute 10:00 elapsed (patient 1 mid-treatment): `Claude Opus Arbiter Gate 1 (Authorization) and Gate 2 (CBCT Tolerance) passed. Beam-on cleared.`
- Pinned annotation at 13:30 PDT: `Mid-afternoon AAPM TG-142 QA snapshot. LINAC output verified within tolerance.`

## matplotlib Recipe

Same conventions as prior gantt instructions.

## Validation Checklist

1. PNG is 3300 x 2550 pixels.
2. 9 task lanes + 3 LLM overlay rows.
3. Hourly separators.
4. 10 per-patient slots labeled.
5. Lunch window highlighted.
6. Pinned annotations.
7. Title, subtitle, header, footer present.
8. No em dash, no double dash, no triple dash.
9. No color outside palette.
10. No emoji.
