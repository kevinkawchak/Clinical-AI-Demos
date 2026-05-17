# Image Instruction 06-02: Apollo 90-Minute Tele-Whipple Gantt Swimlane

[![Demo](https://img.shields.io/badge/Demo-06-brightgreen.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/blob/main/demo-projects/06-humanoid-tele-surgical-assistant.md)
[![Image](https://img.shields.io/badge/Image-02%20of%2010-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/tree/main/demo-projects/image-instruct/06-tele-surgical-assistant)
[![Orientation](https://img.shields.io/badge/Orientation-Landscape-orange.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)
[![DPI](https://img.shields.io/badge/DPI-300-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)

## Output Filename

`demo-projects/06-humanoid-tele-surgical-assistant-output/figures/06-02-operational-timeline-gantt.png`

## Page Size and DPI

- Letter landscape, 11.0 x 8.5 inches, 300 dpi, 3300 x 2550 pixels, white facecolor.

## Chart Type

Gantt swimlane spanning the 90-minute procedure. X axis in minutes 00 to 90. 9 swimlanes + 2 LLM overlay rows.

## Title and Subtitle

- Title: `Apollo Tele-Whipple 90-Minute Procedure Gantt`.
- Subtitle: `PAT-TELE-0001 Pancreaticoduodenectomy - 5,400,000 LLM Ticks 1 kHz - 54,000,000 Motion Ticks 10 kHz`.

## Header and Footer

- Header right: `Demo 06 / Image 02 of 10 / Landscape`.
- Footer left: `Clinical-AI-Demos v0.2.0 / Demo 06 Tele-Surgical Assistant`.
- Footer right: `DOI: 10.5281/zenodo.18445179 / MIT License`.

## Swimlanes Top to Bottom

LLM overlays:

1. `Claude Opus 4.7 1 kHz Planning Tick` (Teal sparks sampled at 1 per second).
2. `Operator Confirmation Roundtrips (1 sec each)` (Forest Green triangles).

Task lanes:

3. `Apollo Instrument Exchange (~20 to 30 expected)` (Deep Navy).
4. `Apollo Stapler Reload` (Deep Navy lighter).
5. `Apollo Irrigation Refill` (Mauve).
6. `Apollo Fascia Tension Monitoring (Vision)` (Slate).
7. `da Vinci SP Surgeon Console (Remote Master)` (Mauve darker).
8. `Tele-Link Latency Profile (50 to 100 ms)` (Burgundy).
9. `Open-Conversion Planner Standby` (Burgundy darker).
10. `Sponsor Observer (CRA + IRB) Log` (Gold).
11. `Audit Log Append (1 Hz)` (Slate lighter).

## Time Markers and Annotations

- Vertical dashed Light Gray lines every 15 minutes.
- Highlight the 6 main Whipple phases: `Access`, `Mobilization`, `Resection`, `Reconstruction Hepaticojejunostomy`, `Reconstruction Gastrojejunostomy`, `Closure` as Forest Green bands of varying lengths.
- Pinned annotation at minute 40: `Resection phase peak Apollo activity. 6 instrument exchanges within 5 min.`
- Pinned annotation at minute 75: `Closure phase Apollo assists fascia closure. Tele-link jitter monitored < 100 ms throughout.`

## matplotlib Recipe

Same conventions as prior gantt instructions. X axis 00:00 to 90:00 in minutes.

## Validation Checklist

1. PNG is 3300 x 2550 pixels.
2. 9 task lanes + 2 LLM overlay rows.
3. 6 Whipple phase bands.
4. 15-minute separators.
5. Pinned annotations at min 40 and 75.
6. Title, subtitle, header, footer present.
7. No em dash, no double dash, no triple dash.
8. No color outside palette.
9. No emoji.
10. Time axis from 00 to 90 minutes.
