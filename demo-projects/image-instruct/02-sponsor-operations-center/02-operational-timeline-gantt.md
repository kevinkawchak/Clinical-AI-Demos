# Image Instruction 02-02: 5x Optimus Sponsor 168-Hour Weekly Cycle Gantt Swimlane

[![Demo](https://img.shields.io/badge/Demo-02-brightgreen.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/blob/main/demo-projects/02-sponsor-humanoid-operations-center.md)
[![Image](https://img.shields.io/badge/Image-02%20of%2010-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/tree/main/demo-projects/image-instruct/02-sponsor-operations-center)
[![Orientation](https://img.shields.io/badge/Orientation-Landscape-orange.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)
[![DPI](https://img.shields.io/badge/DPI-300-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)

## Output Filename

`demo-projects/02-sponsor-humanoid-operations-center-output/figures/02-02-operational-timeline-gantt.png`

## Page Size and DPI

- Letter landscape, 11.0 x 8.5 inches, 300 dpi, 3300 x 2550 pixels, white facecolor.

## Chart Type

Gantt swimlane timeline across the 168-hour (7 day) sponsor operations week. 8 horizontal swimlanes. Each lane shows the activity intervals for one Optimus humanoid station or one document-class processing stream. The Claude Sonnet 4.6 tick at 1 Hz and the Opus 4.7 failover bursts overlaid as marker rows at the top.

## Title and Subtitle

- Title: `5x Tesla Optimus Gen 3 Sponsor Operations Center Weekly Gantt`.
- Subtitle: `SPO-2026-001 - 168 Hours, 604,800 LLM Ticks, 5 Active Oncology Trials, 8 mm Inter-Humanoid Spacing`.

## Header and Footer

- Header right: `Demo 02 / Image 02 of 10 / Landscape`.
- Footer left: `Clinical-AI-Demos v0.2.0 / Demo 02 Sponsor Humanoid Operations Center`.
- Footer right: `DOI: 10.5281/zenodo.18445179 / MIT License`.

## Layout Specification

- X axis: time from Monday 00:00 PDT to Sunday 23:59 PDT, ticks every 6 hours, labeled `Mon 00:00`, `Mon 06:00`, ... `Sun 18:00`, `Sun 23:59`.
- Y axis: 8 swimlanes plus a 2-line LLM overlay at the top (Sonnet ticks and Opus failover bursts).
- Light gray vertical separator at the end of each calendar day.

## Swimlanes Top to Bottom

1. `Sonnet 4.6 1 Hz Tick Overlay` (Teal dots/sparks).
2. `Opus 4.7 1M Failover Bursts` (Teal darker triangles).
3. `Optimus 1 - NSCLC Phase IIIA Stream` (Deep Navy).
4. `Optimus 2 - CRC Phase IIB Stream` (Deep Navy slightly lighter).
5. `Optimus 3 - Breast Phase IIC Stream` (Deep Navy slightly lighter again).
6. `Optimus 4 - Prostate Phase IIIA Stream` (Deep Navy lighter).
7. `Optimus 5 - Pancreatic Phase IIA Stream` (Deep Navy lightest).
8. `FDA RTCT Submission Cycles` (Gold).
9. `IRB Amendment Cycles` (Burgundy).
10. `DSMB Monthly Summary Cycle Window` (Forest Green).

(8 task swimlanes plus 2 overlay rows.)

## Time Markers and Annotations

- Vertical dashed Light Gray line at Wednesday 12:00 labeled `Mid-Week DSMB Snapshot`.
- Vertical dashed Light Gray line at Friday 17:00 labeled `End-of-Week Sponsor SOP Update`.
- Highlight a 0.02 normalized tall Gold band across all lanes from Monday 09:00 to Monday 17:00 labeled `Week-Open CRA Sync Window (5 sites)`.
- Pinned annotation near Friday 14:00: `2-week-cumulative FDA RTCT submission batch dispatched. Anthropic Cowork failover triggered 142 times this week (under 0.024 percent of ticks).`

## matplotlib Recipe

- `matplotlib.pyplot.broken_barh` per swimlane.
- `matplotlib.dates` for the X axis: `mdates.DateFormatter('%a %H:%M')`, major locator every 6 hours.
- For Sonnet 1 Hz overlay sample 1 tick per minute and plot as small Teal dots with `ax.scatter`.
- For Opus failover bursts plot as Teal darker triangles `ax.scatter(..., marker='^', s=15)`.

## Data Structure Future Author Provides

Parquet `weekly_humanoid_intervals.parquet`:

| Column | Type |
|--------|------|
| `lane` | string |
| `start_dt` | timestamp |
| `end_dt` | timestamp |
| `trial_id` | string |
| `document_kind` | string |
| `priority` | float |

## Validation Checklist

1. PNG is 3300 x 2550 pixels.
2. 8 task swimlanes plus 2 overlay rows present and labeled.
3. Sonnet ticks visible as Teal dots; Opus failover triangles visible.
4. 7 daily separators present.
5. Two dashed markers (Wed 12:00, Fri 17:00) labeled.
6. Pinned annotation near Friday 14:00 present.
7. Title, subtitle, header, footer present.
8. No em dash, no double dash, no triple dash.
9. No color outside palette.
10. No emoji.
