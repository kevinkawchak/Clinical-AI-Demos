# Image Instruction 05-02: Phoenix Gen 8 12-Hour Pathology Shift Gantt

[![Demo](https://img.shields.io/badge/Demo-05-brightgreen.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/blob/main/demo-projects/05-humanoid-biospecimen-pathology-lab.md)
[![Image](https://img.shields.io/badge/Image-02%20of%2010-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/tree/main/demo-projects/image-instruct/05-biospecimen-pathology-lab)
[![Orientation](https://img.shields.io/badge/Orientation-Landscape-orange.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)
[![DPI](https://img.shields.io/badge/DPI-300-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)

## Output Filename

`demo-projects/05-humanoid-biospecimen-pathology-lab-output/figures/05-02-operational-timeline-gantt.png`

## Page Size and DPI

- Letter landscape, 11.0 x 8.5 inches, 300 dpi, 3300 x 2550 pixels, white facecolor.

## Chart Type

Gantt swimlane covering 12 hours and 8 specimens. 10 swimlanes plus 2 LLM overlay rows.

## Title and Subtitle

- Title: `Phoenix Gen 8 + Gemini / Qwen via MCP 12-Hour Pathology Lab Gantt`.
- Subtitle: `8 Fresh Specimens - 432,000 LLM Ticks 100 ms - CAP Cold Ischemia and Fixation Windows`.

## Header and Footer

- Header right: `Demo 05 / Image 02 of 10 / Landscape`.
- Footer left: `Clinical-AI-Demos v0.2.0 / Demo 05 Biospecimen Pathology Lab`.
- Footer right: `DOI: 10.5281/zenodo.18445179 / MIT License`.

## Swimlanes Top to Bottom

LLM overlays:

1. `Gemini 3 Pro Tool Calls (Cloud, Redacted)` (Teal lighter triangles).
2. `Qwen3 72B Tool Calls (On-Prem, PHI)` (Teal darker squares).

Task lanes (one per MCP tool):

3. `gross_examine` (Mauve).
4. `formalin_fix (6 to 24 hr per CAP)` (Burgundy).
5. `process_tissue` (Slate).
6. `embed_paraffin` (Gold).
7. `microtome_section (4 to 5 micron)` (Deep Navy).
8. `stain_he` (Forest Green).
9. `stain_ihc (antibody panel)` (Forest Green darker).
10. `slide_scan_and_report_draft` (Slate lighter).
11. `LIS Update` (Mauve darker).
12. `CAP Q-Probes Audit Append` (Gold darker).

## Time Markers and Annotations

- Vertical dashed Light Gray lines every 1 hour.
- Highlight per-specimen cold-ischemia 30-minute pre-formalin band in Burgundy across the formalin_fix lane.
- Highlight CAP formalin-fixation 6 to 24 hour window as Forest Green band.
- Pinned annotation: `Phoenix Gen 8 averages 1 tool call every 100 ms across 12 hours = 432,000 LLM ticks. 8 specimens fully reported by end of shift.`

## matplotlib Recipe

Same conventions as prior gantt instructions. 12-hour X axis from 08:00 to 20:00 PDT.

## Validation Checklist

1. PNG is 3300 x 2550 pixels.
2. 10 task swimlanes + 2 LLM overlay rows.
3. Cold ischemia and formalin bands shown per specimen.
4. Hourly separators.
5. Pinned annotation present.
6. Title, subtitle, header, footer present.
7. No em dash, no double dash, no triple dash.
8. No color outside palette.
9. No emoji.
10. Time axis covers 08:00 to 20:00 PDT.
