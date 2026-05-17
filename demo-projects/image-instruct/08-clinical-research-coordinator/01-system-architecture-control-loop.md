# Image Instruction 08-01: Neo Beta + Multi-Model Ensemble CRC Architecture

[![Demo](https://img.shields.io/badge/Demo-08-brightgreen.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/blob/main/demo-projects/08-humanoid-clinical-research-coordinator.md)
[![Image](https://img.shields.io/badge/Image-01%20of%2010-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/tree/main/demo-projects/image-instruct/08-clinical-research-coordinator)
[![Orientation](https://img.shields.io/badge/Orientation-Landscape-orange.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)
[![DPI](https://img.shields.io/badge/DPI-300-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)

## Output Filename

`demo-projects/08-humanoid-clinical-research-coordinator-output/figures/08-01-system-architecture-control-loop.png`

## Page Size and DPI

- Letter landscape, 11.0 x 8.5 inches, 300 dpi, 3300 x 2550 pixels, white facecolor.

## Chart Type

System architecture flowchart for the 1X Neo Beta humanoid acting as the primary CRC for TRIAL-NSCLC-3A. The center is an ensemble router that dispatches LLM calls to one of three specialty models: Claude Opus 4.7 1M (medical reasoning), Gemini 3 Pro (multi-language consent across English, Spanish, Mandarin, Tagalog, Vietnamese), and GPT-5.5 Thinking (stipend payment guidance).

## Title and Subtitle

- Title: `1X Neo Beta + Claude / Gemini / GPT Ensemble CRC Control Loop`.
- Subtitle: `TRIAL-NSCLC-3A Enrollment Cohort - 12 Patients - 8-Hour Shift - 28,800 LLM Ticks at 1 Hz`.

## Header and Footer

- Header right: `Demo 08 / Image 01 of 10 / Landscape`.
- Footer left: `Clinical-AI-Demos v0.2.0 / Demo 08 Clinical Research Coordinator`.
- Footer right: `DOI: 10.5281/zenodo.18445179 / MIT License`.

## Layout

- Left two-thirds: 3-swimlane flowchart with central ensemble router.
- Right one-third: CRC interview room layout with Neo Beta silhouette and patient chair.

## Inbound Lane (top)

1. `12 Prospective Patients (8 New, 4 Follow-Up)` (Mauve).
2. `5 Patient Language Preferences (EN, ES, ZH, TL, VI)` (Slate).
3. `Patient Self-Selection Form (HR 9501)` (Burgundy).
4. `Humanoid Choice Form (HR 9502)` (Burgundy).
5. `Procedural Modification Form (HR 9503)` (Burgundy).
6. `Data Self-Custody Election (HR 9507)` (Burgundy darker).

## Middle Lane (Neo Beta + Ensemble Loop)

Six rectangles plus central ensemble router:

1. `1X Neo Beta Humanoid` (Deep Navy). Sub-label: `28 DOF, 1.65 m, 35 kg, soft tendon-driven joints, compliant skin, 20 N contact force max`.
2. `Patient Interview State Aggregator` (Slate).
3. **`Ensemble Router (ensemble_router.py)`** (Mauve fill, larger central box).
4. `Claude Opus 4.7 1M (Medical Reasoning)` (Teal).
5. `Gemini 3 Pro (EN, ES, ZH, TL, VI)` (Teal lighter).
6. `GPT-5.5 Thinking (Stipend Payment)` (Teal darker).
7. `Safety Arbiter + HR 9501 to 9507 Enforcer` (Burgundy).
8. `Neo Beta Dispatcher` (Deep Navy).

Arrows from the Ensemble Router fan to all three LLMs labeled with the routing rule.

## Outbound Lane (bottom)

1. `Informed Consent Documents (Multilingual)` (Forest Green).
2. `Stipend Payment Authorization Request` (Gold).
3. `Procedural Modification Acceptance Letter` (Mauve).
4. `Site CRA Daily Roll-Up` (Slate).
5. `IRB Consent Audit Log` (Burgundy).
6. `Per-Tick Audit Append` (Slate lighter).

## CRC Interview Room Overlay (right one-third)

Stylized 4 m x 4 m interview room with:
- Patient chair (Mauve).
- Neo Beta silhouette across from patient with 20 N contact-force ring.
- Tablet display (multilingual consent form mockup).
- Translation reference screen (5 language toggle).
- Privacy curtain.

## Annotations

- Pinned to Ensemble Router: `Medical reasoning routes to Claude Opus. Language tasks route to Gemini 3 Pro. Stipend payment routes to GPT-5.5 Thinking. Routing rule logged for IRB audit per tick.`
- Pinned to Neo Beta: `Soft tendon-driven joints; compliant skin reduces patient discomfort. Max 20 N contact force during escort handoff and gentle touch.`
- Pinned to Safety Arbiter: `HR 9501 to 9507 patient rights are hard-gates. Neo Beta refuses any action that violates patient self-selection, humanoid choice, procedural modification, or data self-custody.`

## Color Mapping

Humanoid Deep Navy. Ensemble Router Mauve. LLMs Teal variants. Safety Burgundy. Outputs Forest Green / Gold. Patient inputs Mauve. Audit Slate.

## matplotlib Recipe

Same conventions as prior architecture instructions.

## Validation Checklist

1. PNG is 3300 x 2550 pixels.
2. Ensemble router prominent in middle.
3. 3 LLM boxes with routing arrows from ensemble.
4. CRC interview room overlay.
5. HR 9501-9507 references present.
6. Closed-loop return arrow.
7. Title, subtitle, header, footer present.
8. No em dash, no double dash, no triple dash.
9. No color outside palette.
10. No emoji.
