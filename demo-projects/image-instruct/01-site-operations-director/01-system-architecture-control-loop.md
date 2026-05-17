# Image Instruction 01-01: Atlas + Claude Opus 4.7 Site Operations System Architecture Control Loop

[![Demo](https://img.shields.io/badge/Demo-01-brightgreen.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/blob/main/demo-projects/01-humanoid-site-operations-director.md)
[![Image](https://img.shields.io/badge/Image-01%20of%2010-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/tree/main/demo-projects/image-instruct/01-site-operations-director)
[![Orientation](https://img.shields.io/badge/Orientation-Landscape-orange.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)
[![DPI](https://img.shields.io/badge/DPI-300-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)

## Output Filename

`demo-projects/01-humanoid-site-operations-director-output/figures/01-01-system-architecture-control-loop.png`

## Page Size and DPI

- Letter landscape, 11.0 x 8.5 inches.
- 300 dots per inch.
- Output pixel dimensions: 3300 x 2550.
- White facecolor (`#FFFFFF`).

## Chart Type

Multi-pane architecture flowchart. Top-down structured layout with three horizontal swimlanes: sensors and inputs at the top, the Atlas humanoid plus the Claude Opus 4.7 1M planner control loop in the middle, and actuators plus outputs at the bottom. The full PAT-SITE-001 facility (12 surgical bays, 24 recovery rooms, 8 imaging suites, 1 pharmacy clean room) is rendered as a labeled region overlay on the right one-third of the page.

## Title and Subtitle

- Title (16 pt bold Deep Navy, centered at the top): `Atlas Electric + Claude Opus 4.7 1M Site Operations Control Loop`.
- Subtitle (12 pt regular Slate, centered one line below the title): `PAT-SITE-001 San Francisco - 8-Hour Day Shift, 1 Hz LLM Cadence, 10 Hz Humanoid Motion Cadence`.

## Header and Footer

- Header right-aligned in the top margin (8 pt italic Slate): `Demo 01 / Image 01 of 10 / Landscape`.
- Footer left-aligned (8 pt italic Slate): `Clinical-AI-Demos v0.2.0 / Demo 01 Site Operations Director`.
- Footer right-aligned (8 pt italic Slate): `DOI: 10.5281/zenodo.18445179 / MIT License`.

## Layout Specification

- Left two-thirds (0.0 to 0.66 normalized width) is the control loop schematic.
- Right one-third (0.66 to 1.0 normalized width) is the facility map overlay with the four zones color-coded.
- 0.3 inch margin on all sides.
- Three swimlanes top to bottom in the left two-thirds:
  1. Sensors and Inputs lane at y = 0.70 to 0.92.
  2. Atlas + Claude Opus 4.7 control loop lane at y = 0.32 to 0.66.
  3. Actuators and Outputs lane at y = 0.06 to 0.28.
- Each lane has a 12 pt semi-bold Deep Navy lane label on the far left.

## Components in the Sensors and Inputs Lane (top)

Six rounded rectangles, equal-spaced left to right:

1. `Bay Cameras 12 x` (Teal `#2E8B8B`).
2. `Patient Vitals Streams 10 x` (Teal).
3. `IMP Pharmacy RFID Scanner` (Mauve `#8B6B8B`).
4. `IRB and 21 CFR § 312 Gate` (Burgundy `#8B2E3F`).
5. `Atlas Onboard IMU and Force` (Deep Navy `#1F3A68`).
6. `Companion Repository Inputs` (Slate `#4A5568`) annotated `new-trial/site/, patient-journey/, regulatory/ich-gcp/`.

## Components in the Atlas + Claude Opus 4.7 Control Loop Lane (middle)

Five rounded rectangles in a left-to-right sequence with arrows:

1. `Atlas Electric Humanoid` (Deep Navy fill, white text). Sub-label: `28 DOF, 1.5 m, 89 kg, 11 kg per-arm payload, IP67`.
2. `Site State Aggregator (site_state.py)` (Slate). Sub-label: `12 bays + 24 rooms + 8 imaging + 1 pharmacy`.
3. `Claude Opus 4.7 1M Planner (llm_planner.py)` (Teal). Sub-label: `on-prem, 200 ms median round-trip, 1 Hz tick`.
4. `Safety Arbiter (safety_arbiter.py)` (Burgundy). Sub-label: `IEC 80601-2-77 + ISO 10218, E-stop 50 ms`.
5. `Atlas Dispatcher (atlas_dispatcher.py)` (Deep Navy). Sub-label: `10 Hz humanoid motion control, 11 kg per-arm cap`.

A closed-loop arrow returns from the Atlas Dispatcher back to the Atlas Electric Humanoid to make the cycle explicit. All arrows are 1.2 pt Slate with `FancyArrowPatch`, head style `->` size 12.

## Components in the Actuators and Outputs Lane (bottom)

Six rounded rectangles, equal-spaced left to right:

1. `Bay Reassignment Commands` (Forest Green `#2F6B3E`).
2. `Recovery Room Reposition Commands` (Forest Green).
3. `IMP Compounding Trigger` (Mauve).
4. `AE Escalation to On-Call Physician` (Burgundy).
5. `Audit Log Append (shift_llm_decisions.jsonl)` (Slate).
6. `Per-Tick Bay Status Parquet Write` (Slate).

Arrows from the Atlas Dispatcher fan out to all six.

## Facility Map Overlay (right one-third)

A stacked rectangle stylization of the 4-floor PAT-SITE-001 facility from `new-trial/site/10-site-operations/`:

- Floor 4 (top, Forest Green light fill): `Pharmacy Clean Room (1)`.
- Floor 3 (Gold light fill): `Imaging Suites (8)`.
- Floor 2 (Teal light fill): `Surgical Bays (12)`.
- Floor 1 (Mauve light fill): `Recovery Rooms (24)`.

A small Atlas Electric silhouette icon at the center labeled `Shift Director`. Use a simple stick-figure with a rectangular head to indicate humanoid form; do not import external icons.

## Annotations

Four pinned annotations with leader lines from the control loop to the margin:

- `1 Hz LLM tick = 28,800 ticks per 8-hour shift` (top right of LLM Planner box).
- `10 Hz motion = 287,520 motion ticks per shift` (top right of Atlas Dispatcher box).
- `E-stop budget: 50 ms site-grade` (right of Safety Arbiter box).
- `Cumulative force limit: 15 N across both arms` (left of Atlas Electric box).

## Color Mapping

- Humanoid platform components: Deep Navy `#1F3A68`.
- LLM components: Teal `#2E8B8B`.
- Safety and regulatory: Burgundy `#8B2E3F`.
- Data and audit: Slate `#4A5568`.
- Output and success: Forest Green `#2F6B3E`.
- Pharmacy and IMP: Mauve `#8B6B8B`.
- Facility floor overlays: Light fills of the same hues at 30 percent opacity.

## matplotlib Recipe

- Use `matplotlib.patches.FancyBboxPatch` with `boxstyle="round,pad=0.02,rounding_size=0.04"` for every component box.
- Use `matplotlib.patches.FancyArrowPatch` with `arrowstyle="->,head_length=8,head_width=6"` and `connectionstyle="arc3,rad=0.0"` for straight arrows, `"arc3,rad=0.2"` for the closed-loop return arrow.
- Use `ax.add_patch` for each rectangle and `ax.text` for each label with `ha="center"` and `va="center"`.
- Set `ax.set_xlim(0, 1)`, `ax.set_ylim(0, 1)`, `ax.set_axis_off()`.
- Reserve top 0.05 of the y range for the title block and bottom 0.05 for the footer block.
- Use `fig.text` for title, subtitle, header, and footer.

## Validation Checklist

1. PNG dimensions are 3300 x 2550 pixels (landscape Letter at 300 dpi).
2. White facecolor at every corner.
3. All 5 boxes in the control loop lane present and labeled.
4. Closed-loop return arrow visible from Atlas Dispatcher back to Atlas Electric Humanoid.
5. Facility map overlay shows all 4 floors with correct counts (12, 24, 8, 1).
6. Title and subtitle present, centered, unclipped.
7. Footer band present with both left and right text.
8. No em dash, no double dash, no triple dash. The section sign `§` appears in `21 CFR § 312`.
9. No color outside the palette table.
10. No emoji.
