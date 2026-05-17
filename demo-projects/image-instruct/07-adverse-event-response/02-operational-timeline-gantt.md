# Image Instruction 07-02: H2 168-Hour 4-Site AE Response Weekly Gantt

[![Demo](https://img.shields.io/badge/Demo-07-brightgreen.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/blob/main/demo-projects/07-humanoid-24-7-adverse-event-response.md)
[![Image](https://img.shields.io/badge/Image-02%20of%2010-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/tree/main/demo-projects/image-instruct/07-adverse-event-response)
[![Orientation](https://img.shields.io/badge/Orientation-Landscape-orange.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)
[![DPI](https://img.shields.io/badge/DPI-300-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)

## Output Filename

`demo-projects/07-humanoid-24-7-adverse-event-response-output/figures/07-02-operational-timeline-gantt.png`

## Page Size and DPI

- Letter landscape, 11.0 x 8.5 inches, 300 dpi, 3300 x 2550 pixels, white facecolor.

## Chart Type

Gantt swimlane spanning 168 hours (1 week). 9 task swimlanes + 4 per-site Claude Opus overlay rows.

## Title and Subtitle

- Title: `3x Unitree H2 + Per-Site Claude Opus 4.7 1M 168-Hour Weekly Gantt`.
- Subtitle: `PAT-NET-001 4-Site Network - 604,800 LLM Ticks Per Site - Cross-Site Rotation Schedule`.

## Header and Footer

- Header right: `Demo 07 / Image 02 of 10 / Landscape`.
- Footer left: `Clinical-AI-Demos v0.2.0 / Demo 07 Adverse Event Response`.
- Footer right: `DOI: 10.5281/zenodo.18445179 / MIT License`.

## Swimlanes Top to Bottom

LLM overlays (1 per site):

1. `Claude Opus 4.7 1M San Francisco` (Teal sparks).
2. `Claude Opus 4.7 1M San Diego` (Teal lighter sparks).
3. `Claude Opus 4.7 1M Boston` (Teal darker sparks).
4. `Claude Opus 4.7 1M Atlanta` (Teal mid sparks).

Task lanes:

5. `H2-1 Rotation Schedule (Site Assignment)` (Deep Navy).
6. `H2-2 Rotation Schedule (Site Assignment)` (Deep Navy lighter).
7. `H2-3 Rotation Schedule (Site Assignment)` (Deep Navy mid).
8. `AE Events Detected (CTCAE Grade Distribution)` (Burgundy).
9. `Cross-Site Transit Events (FAA Drone / Charter)` (Mauve).
10. `H2 Battery Hot-Swap (Every 5 Hours)` (Slate).
11. `On-Call Physician Activations (HR 9505)` (Burgundy darker).
12. `Sponsor Acknowledgment Cycle (HR 9505 1 Hour)` (Gold).
13. `Cross-Site Audit Reconciliation` (Forest Green).

## Time Markers and Annotations

- Vertical dashed Light Gray lines at end of each day (Mon to Sun).
- Highlight night windows (22:00 to 06:00 each day) with Light Gray bands.
- Pinned annotation at Wed 14:00: `Mid-week peak AE detection - H2 cross-site transit triggered SF to LA.`
- Pinned annotation at Fri 10:00: `Sponsor mid-week DSMB digest. All CTCAE grade 3+ events from the week reviewed.`

## matplotlib Recipe

Same conventions as prior gantt instructions. X axis: Mon 00:00 to Sun 23:59 PDT.

## Validation Checklist

1. PNG is 3300 x 2550 pixels.
2. 9 task lanes + 4 per-site Claude Opus overlay rows.
3. Daily separators.
4. Night windows highlighted.
5. Pinned annotations at Wed 14:00 and Fri 10:00.
6. Title, subtitle, header, footer present.
7. No em dash, no double dash, no triple dash.
8. No color outside palette.
9. No emoji.
10. Time axis covers 168 hours.
