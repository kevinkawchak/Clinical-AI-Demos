# Image Instruction 01-02: Atlas 8-Hour Shift Operational Timeline Gantt Swimlane Chart

[![Demo](https://img.shields.io/badge/Demo-01-brightgreen.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/blob/main/demo-projects/01-humanoid-site-operations-director.md)
[![Image](https://img.shields.io/badge/Image-02%20of%2010-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/tree/main/demo-projects/image-instruct/01-site-operations-director)
[![Orientation](https://img.shields.io/badge/Orientation-Landscape-orange.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)
[![DPI](https://img.shields.io/badge/DPI-300-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)

## Output Filename

`demo-projects/01-humanoid-site-operations-director-output/figures/01-02-operational-timeline-gantt.png`

## Page Size and DPI

- Letter landscape, 11.0 x 8.5 inches, 300 dpi, 3300 x 2550 pixels, white facecolor.

## Chart Type

Gantt swimlane timeline with 7 horizontal swimlanes covering the 8-hour day shift (08:00 to 16:00 PDT). Each swimlane is one operational stream. The Atlas Electric humanoid is the actor in every lane; the Claude Opus 4.7 1M LLM tick is overlaid as a 1 Hz spark at the top of the timeline.

## Title and Subtitle

- Title: `Atlas Electric 8-Hour Day Shift Gantt: PAT-SITE-001 San Francisco`.
- Subtitle: `28,800 LLM Ticks at 1 Hz x 287,520 Humanoid Motion Ticks at 10 Hz x 10 Active Patients`.

## Header and Footer

- Header right: `Demo 01 / Image 02 of 10 / Landscape`.
- Footer left: `Clinical-AI-Demos v0.2.0 / Demo 01 Site Operations Director`.
- Footer right: `DOI: 10.5281/zenodo.18445179 / MIT License`.

## Layout Specification

- X axis: time of day from 08:00 to 16:00 PDT, ticks every 30 minutes (16 ticks plus end), labeled `HH:MM`.
- Y axis: 7 swimlanes from top to bottom, each 0.10 normalized units tall with a 0.02 unit gap, occupying y from 0.10 to 0.92.
- Top sliver from 0.92 to 0.97 holds the LLM 1 Hz tick spark.
- Left margin 1.5 inches wide for swimlane labels.

## Swimlanes Top to Bottom

1. `LLM Tick Heartbeat` (Teal `#2E8B8B`) - a dense 1 Hz vertical tick spark plotted with `ax.vlines` at 60-second intervals.
2. `Surgical Bay Ops` (Deep Navy `#1F3A68`) - 12 bay reassignment intervals across the shift.
3. `Recovery Room Repositioning` (Mauve `#8B6B8B`) - Braden 2-hour reposition for 24 rooms (Atlas walks the floor every 2 hours).
4. `Imaging Suite Choreography` (Gold `#C18A2C`) - 8 imaging suites with CT and MR slots.
5. `Pharmacy Clean Room Visits` (Forest Green `#2F6B3E`) - IMP pick-up windows for surgical bays.
6. `IRB and 21 CFR § 312 Compliance Checkpoints` (Burgundy `#8B2E3F`) - audit log entries triggered by Claude Opus 4.7 every 30 minutes.
7. `AE Escalation Slots` (Slate `#4A5568`) - on-call physician calls; expected approximately 1 to 3 per shift.

Each swimlane uses `matplotlib.pyplot.broken_barh` with the lane color. Lane label on the far left in 11 pt semi-bold Deep Navy.

## Time Markers and Annotations

- Vertical dashed Light Gray line at 12:00 labeled `Lunch Window for Human Staff (Atlas Continues)`.
- Vertical dashed Light Gray line at 14:00 labeled `Shift-Midpoint Audit Snapshot`.
- Three pinned annotations:
  - `Cumulative force budget reset (15 N)` at 11:00 with leader to the Surgical Bay Ops lane.
  - `Mandatory Atlas charge swap window` at 12:30 with leader to the LLM Tick Heartbeat lane.
  - `Pre-shift handoff to PACU night shift (Demo 04)` at 16:00 with leader to the Recovery Room lane.

## Data Structure Future Author Provides

The future Claude Code Opus 4.7 1M Max session will produce a Parquet file `shift_humanoid_commands.parquet` (287,520 rows). The figure aggregates that file into intervals per lane using the schema:

| Column | Type | Description |
|--------|------|-------------|
| `lane` | string | one of the 7 swimlane names |
| `start_iso` | string | ISO 8601 PDT timestamp |
| `end_iso` | string | ISO 8601 PDT timestamp |
| `bay_or_room_id` | string | e.g., `BAY-03` or `REC-12` |
| `priority` | float | 0.0 to 1.0 |

## Annotations and Color Mapping

- Use lane-specific color from the section above for the broken_barh blocks.
- Pinned annotations use `ax.annotate` with `arrowprops=dict(arrowstyle='->', lw=0.8, color='#4A5568')`.
- Vertical reference lines use `ax.axvline(linestyle='--', color='#E2E8F0', lw=0.8)`.

## matplotlib Recipe

- Use `matplotlib.dates` to format the X axis as `%H:%M`.
- For the LLM tick heartbeat, generate 28,800 timestamps at 1 second intervals; render every 60th with `ax.vlines(t, y_min, y_max, color=teal, lw=0.4, alpha=0.6)`.
- Set `ax.set_xlim(start_dt, end_dt)`, `ax.set_ylim(0, 1)`.
- Use `ax.invert_yaxis()` if labeling top to bottom is easier in your loop.
- Save with `fig.savefig(out_path, dpi=300, facecolor='white')`.

## Validation Checklist

1. PNG is 3300 x 2550 pixels.
2. 7 swimlanes visible, each with label, color block, and at least one interval.
3. LLM tick spark visible at the top.
4. Vertical dashed lines at 12:00 and 14:00 with labels unclipped.
5. Three pinned annotations present with leaders.
6. Title, subtitle, header, footer text present.
7. No em dash, no double dash, no triple dash. `§` appears in `21 CFR § 312`.
8. No color outside palette.
9. No emoji.
