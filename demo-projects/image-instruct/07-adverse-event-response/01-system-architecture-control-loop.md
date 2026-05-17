# Image Instruction 07-01: 3x Unitree H2 + Per-Site Claude Opus 4.7 1M Adverse Event Response Architecture

[![Demo](https://img.shields.io/badge/Demo-07-brightgreen.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/blob/main/demo-projects/07-humanoid-24-7-adverse-event-response.md)
[![Image](https://img.shields.io/badge/Image-01%20of%2010-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/tree/main/demo-projects/image-instruct/07-adverse-event-response)
[![Orientation](https://img.shields.io/badge/Orientation-Landscape-orange.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)
[![DPI](https://img.shields.io/badge/DPI-300-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)

## Output Filename

`demo-projects/07-humanoid-24-7-adverse-event-response-output/figures/07-01-system-architecture-control-loop.png`

## Page Size and DPI

- Letter landscape, 11.0 x 8.5 inches, 300 dpi, 3300 x 2550 pixels, white facecolor.

## Chart Type

System architecture flowchart spanning a 4-site PAT-NET-001 network (San Francisco, San Diego, Boston, Atlanta) with 3 rotating Unitree H2 humanoids. The 4 per-site Claude Opus 4.7 1M deployments coordinate with a continental cross-site bus.

## Title and Subtitle

- Title: `3x Unitree H2 + Per-Site Claude Opus 4.7 1M 24/7 Adverse Event Response Network`.
- Subtitle: `PAT-NET-001 4-Site Continental Network - 168 Hours, 604,800 LLM Ticks at 1 Hz Per Site`.

## Header and Footer

- Header right: `Demo 07 / Image 01 of 10 / Landscape`.
- Footer left: `Clinical-AI-Demos v0.2.0 / Demo 07 Adverse Event Response`.
- Footer right: `DOI: 10.5281/zenodo.18445179 / MIT License`.

## Layout Specification

- Top half: 4 site cards in a row (San Francisco, San Diego, Boston, Atlanta). Each card shows the per-site Claude Opus 4.7 1M deployment box, the AE inbound channels, the on-call physician outbound, and the 1 active H2 if rotated in.
- Middle: a cross-site coordination bus labeled `Continental AE Coordination Bus`. Three H2 humanoid silhouettes shown rotating between sites; arrows indicate which 2 sites are H2-resident at any time.
- Bottom half: HR 9505 1-hour CTCAE grading SLA timeline plus the cross-site transit SLA (< 30 min).

## Per-Site Card Components (4 cards, identical structure)

For each card:

1. Site name and address (Slate header).
2. `Claude Opus 4.7 1M On-Prem Planner` (Teal box).
3. `Patient Vitals + Sensor Mesh` (Mauve).
4. `AE Inbound (Site Staff + Patients + Family)` (Burgundy).
5. `Unitree H2 (if resident)` (Deep Navy fill; ghosted if absent).
6. `On-Call Physician + Sponsor Notification (HR 9505)` (Burgundy darker).

## Cross-Site Coordination Bus (middle)

Horizontal bar labeled `Continental AE Coordination Bus`. Three H2 humanoid silhouettes positioned along the bar with arrows indicating current rotation assignment. Annotation: `H2 rotation balances load across sites. Cross-site transit SLA under 30 min via FAA-certified medical drone or hospital-charter aircraft.`

## H2 Humanoid Details

In one of the per-site cards (San Francisco), show the H2 specs:
- `Unitree H2 (39 DOF, 1.8 m, 70 kg, 5-hour battery hot-swap, IP65, outdoor-rated)`.
- `Cumulative cross-arm force ceiling: 15 N. E-stop: 5 ms surgical-grade.`

## Bottom Half SLA Diagram

Horizontal time axis from 0 to 60 minutes. Two horizontal bars:

1. `Per-Site SLA: AE-to-Bedside under 90 seconds` (Forest Green band ending at 90 s).
2. `Cross-Site SLA: Transit + Arrival under 30 minutes` (Forest Green band ending at 30 min).
3. `HR 9505 SLA: CTCAE Grading + Sponsor Acknowledgment within 1 hour` (Burgundy band ending at 60 min).

## Annotations

- Pinned to Continental Bus: `Per-site Claude Opus 4.7 1M instances synchronize AE event state at 1 Hz across the bus. No PHI leaves the per-site boundary; only de-identified summaries cross the bus.`
- Pinned to each per-site Claude Opus box: `4 separate deployments. No shared inference cache. Each site has independent IRB.`

## Color Mapping

Standard palette. Humanoid Deep Navy, LLM Teal, AE inbound and on-call Burgundy, SLA bars per stated colors, Slate for headers/audit.

## matplotlib Recipe

Same conventions as prior architecture instructions, but using 4 horizontally-aligned subplots for the per-site cards and an additional subplot below for the SLA timeline.

## Validation Checklist

1. PNG is 3300 x 2550 pixels.
2. 4 per-site cards in a row.
3. Continental coordination bus visible.
4. 3 H2 humanoid silhouettes shown.
5. Bottom SLA timeline with 3 bars.
6. Title, subtitle, header, footer present.
7. No em dash, no double dash, no triple dash.
8. No color outside palette.
9. No emoji.
10. HR 9505 SLA bar correctly colored Burgundy.
