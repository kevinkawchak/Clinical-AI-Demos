# Image Instruction 06-01: Apollo + Claude Opus 4.7 1M Tele-Surgical Architecture

[![Demo](https://img.shields.io/badge/Demo-06-brightgreen.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/blob/main/demo-projects/06-humanoid-tele-surgical-assistant.md)
[![Image](https://img.shields.io/badge/Image-01%20of%2010-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/tree/main/demo-projects/image-instruct/06-tele-surgical-assistant)
[![Orientation](https://img.shields.io/badge/Orientation-Landscape-orange.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)
[![DPI](https://img.shields.io/badge/DPI-300-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)

## Output Filename

`demo-projects/06-humanoid-tele-surgical-assistant-output/figures/06-01-system-architecture-control-loop.png`

## Page Size and DPI

- Letter landscape, 11.0 x 8.5 inches, 300 dpi, 3300 x 2550 pixels, white facecolor.

## Chart Type

System architecture flowchart with a 1,100-mile tele-link bridge in the middle. Patient-side OR on the left half shows the Apollo humanoid and da Vinci SP. Remote surgeon console on the right half. The on-prem Claude Opus 4.7 1M planner sits patient-side with operator-in-the-loop confirmation gating every instrument exchange.

## Title and Subtitle

- Title: `Apptronik Apollo + Claude Opus 4.7 1M Tele-Surgical Assistant Control Loop`.
- Subtitle: `1,100-Mile Rural Whipple, PAT-TELE-0001 Stage IIA Pancreatic Adenocarcinoma - 90 Minutes, 10 kHz Motion, 1 kHz LLM Planning`.

## Header and Footer

- Header right: `Demo 06 / Image 01 of 10 / Landscape`.
- Footer left: `Clinical-AI-Demos v0.2.0 / Demo 06 Tele-Surgical Assistant`.
- Footer right: `DOI: 10.5281/zenodo.18445179 / MIT License`.

## Layout Specification

- Left half (x 0.0 to 0.45): Big Timber, Montana patient-side OR with Apollo, da Vinci SP, Claude Opus 4.7 1M on-prem planner, safety arbiter, IV stack, anesthesia console.
- Center (x 0.45 to 0.55): 1,100-mile DOD-grade encrypted tele-link bridge (Burgundy band labeled `Tele-Link 50 ms baseline, up to 100 ms jitter`).
- Right half (x 0.55 to 1.0): University of Minnesota Masonic remote surgeon console with da Vinci SP master controls, audio/video, operator confirmation pad.

## Patient-Side OR (left half)

Rounded rectangles:

1. `Apptronik Apollo Humanoid (Patient-Side Assistant)` (Deep Navy). Sub-label: `40 DOF, 1.73 m, 73 kg, 25 kg per-arm, 0.5 mm RMS, IP54`.
2. `da Vinci SP (Single-Port Robot)` (Mauve). Sub-label: `4 arms, 8 mm instruments, da Vinci SP master tunneled over 1,100 mi`.
3. `Claude Opus 4.7 1M On-Prem Planner` (Teal). Sub-label: `200 ms median, 1 kHz planning cadence, 1 sec confirmation roundtrip`.
4. `Safety Arbiter + Operator-In-Loop Gate` (Burgundy). Sub-label: `IEC 80601-2-77; 5 ms surgical-grade E-stop; 5 N tip force max`.
5. `Open-Conversion Planner` (Burgundy darker). Sub-label: `Tele-link loss > 3 s triggers 5-minute manual open-conversion plan`.

## Center Tele-Link Band

A vertical Burgundy band labeled `DOD-Grade Encrypted Tele-Link / 50 ms baseline / 100 ms jitter / 32-iter latency sweep`. Two arrows: forward (right to left) labeled `Surgeon Command + Confirmation`; reverse (left to right) labeled `Apollo Vision + da Vinci Telemetry`.

## Remote Surgeon Console (right half)

1. `University of Minnesota Masonic Surgeon Console` (Slate).
2. `da Vinci SP Master Controls` (Mauve darker).
3. `Live 4K Apollo Head-Mounted Stereo Feed` (Slate lighter).
4. `Operator Confirmation Pad (1 sec roundtrip per exchange)` (Forest Green).
5. `Sponsor Observer Window (CRA + IRB)` (Gold).

## Annotations

- Pinned to Operator-In-Loop Gate: `Every instrument exchange requires 1 sec roundtrip confirmation from surgeon. Failure to confirm holds Apollo in safe pose.`
- Pinned to Open-Conversion Planner: `Tele-link loss > 3 s triggers 5-minute manual open-conversion plan. Apollo is the only entity that can perform manual conversion. Remote surgeon cannot.`
- Pinned to Apollo: `25 kg per-arm payload allows lifting laparoscopic stapler reloads. 5 N tip force ceiling for instrument exchanges.`

## Color Mapping

- Humanoid Deep Navy. LLM Teal. Safety + Tele-link Burgundy. da Vinci Mauve. Audit Slate. Surgeon confirmation Forest Green. Sponsor observers Gold.

## matplotlib Recipe

Same conventions as prior architecture instructions.

## Validation Checklist

1. PNG is 3300 x 2550 pixels.
2. Left half = patient-side OR with Apollo and da Vinci SP.
3. Center vertical Burgundy tele-link band with bidirectional arrows.
4. Right half = remote surgeon console.
5. Operator confirmation pad prominent.
6. Open-conversion planner visible.
7. Title, subtitle, header, footer present.
8. No em dash, no double dash, no triple dash.
9. No color outside palette.
10. No emoji.
