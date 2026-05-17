# Image Instruction 04-02: Digit V5 24-Hour PACU Night-Shift Gantt Swimlane

[![Demo](https://img.shields.io/badge/Demo-04-brightgreen.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/blob/main/demo-projects/04-humanoid-post-op-recovery-nurse.md)
[![Image](https://img.shields.io/badge/Image-02%20of%2010-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/tree/main/demo-projects/image-instruct/04-post-op-recovery-nurse)
[![Orientation](https://img.shields.io/badge/Orientation-Landscape-orange.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)
[![DPI](https://img.shields.io/badge/DPI-300-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)

## Output Filename

`demo-projects/04-humanoid-post-op-recovery-nurse-output/figures/04-02-operational-timeline-gantt.png`

## Page Size and DPI

- Letter landscape, 11.0 x 8.5 inches, 300 dpi, 3300 x 2550 pixels, white facecolor.

## Chart Type

Gantt swimlane timeline across the 24-hour PACU shift starting at 18:00 PDT. 8 task swimlanes plus 3 LLM overlay rows (one per tier).

## Title and Subtitle

- Title: `Agility Digit V5 24-Hour PACU Night-Shift Gantt`.
- Subtitle: `PAT-REC-0001 Day 0 Post-Op - 86,400 LLM Ticks 1 Hz - Tier 1 Haiku, Tier 2 Sonnet, Tier 3 Llama 4 70B`.

## Header and Footer

- Header right: `Demo 04 / Image 02 of 10 / Landscape`.
- Footer left: `Clinical-AI-Demos v0.2.0 / Demo 04 Post-Op Recovery Nurse`.
- Footer right: `DOI: 10.5281/zenodo.18445179 / MIT License`.

## Swimlanes Top to Bottom

LLM overlays (top 3 rows):

1. `Claude Haiku 4.5 Tier 1 Tick (1 Hz)` (Teal sparks).
2. `Claude Sonnet 4.6 Tier 2 Escalations` (Teal darker triangles).
3. `Ollama Llama 4 70B Tier 3 PHI Inferences` (Teal darkest squares).

Task lanes:

4. `Braden 2-Hour Reposition (12 events)` (Forest Green).
5. `Vitals Check (every 15 min, 96 events)` (Mauve).
6. `IV Pump Adjustment Requests` (Burgundy).
7. `Pain Score Re-Check Prompts` (Mauve darker).
8. `Chest Tube Drainage Read` (Slate).
9. `Companion Caregiver Update Calls` (Gold).
10. `Hand-Off to Day-Shift Nurse Window 06:00` (Forest Green).
11. `On-Call Physician Escalations` (Burgundy darker).

## Annotations

- Vertical dashed Light Gray lines every 4 hours from 18:00 to 18:00 next day.
- Highlight Braden 2-hour bands as Forest Green bands across the Reposition lane.
- Pinned annotation at 02:00: `Pain peak window typical. Haiku confidence threshold drops to 0.80 to trigger Sonnet review more aggressively.`
- Pinned annotation at 06:00: `Hand-off to Day-Shift Nurse. Digit V5 transfers per-shift summary plus 12 Braden timestamps plus 96 vitals reads.`

## matplotlib Recipe

Same conventions as 01-02, 02-02, 03-02.

## Validation Checklist

1. PNG is 3300 x 2550 pixels.
2. 8 task lanes + 3 LLM overlay rows present.
3. Braden bands visible.
4. 4-hour separators.
5. Pinned annotations at 02:00 and 06:00.
6. Title, subtitle, header, footer present.
7. No em dash, no double dash, no triple dash.
8. No color outside palette.
9. No emoji.
10. X axis labels in `Day HH:MM` format covering 18:00 PDT to 18:00 PDT next day.
