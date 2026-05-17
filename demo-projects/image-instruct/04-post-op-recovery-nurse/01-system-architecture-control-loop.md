# Image Instruction 04-01: Digit V5 + Claude Haiku/Sonnet + Llama 4 PACU Recovery Nurse Architecture

[![Demo](https://img.shields.io/badge/Demo-04-brightgreen.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/blob/main/demo-projects/04-humanoid-post-op-recovery-nurse.md)
[![Image](https://img.shields.io/badge/Image-01%20of%2010-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/tree/main/demo-projects/image-instruct/04-post-op-recovery-nurse)
[![Orientation](https://img.shields.io/badge/Orientation-Landscape-orange.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)
[![DPI](https://img.shields.io/badge/DPI-300-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)

## Output Filename

`demo-projects/04-humanoid-post-op-recovery-nurse-output/figures/04-01-system-architecture-control-loop.png`

## Page Size and DPI

- Letter landscape, 11.0 x 8.5 inches, 300 dpi, 3300 x 2550 pixels, white facecolor.

## Chart Type

System architecture flowchart with a tiered LLM stack. Digit V5 humanoid is the patient-side caregiver; the LLM control loop uses Claude Haiku 4.5 default for fast routine ticks, escalates to Claude Sonnet 4.6 for complex reasoning, and routes PHI-bearing inference to Ollama Llama 4 70B running locally. Right one-third renders the PACU recovery room with the 2 m perimeter the Digit V5 must stay within.

## Title and Subtitle

- Title: `Agility Digit V5 + Claude Haiku 4.5 / Sonnet 4.6 / Ollama Llama 4 70B PACU Recovery Nurse Loop`.
- Subtitle: `PAT-REC-0001 Stage IIIB NSCLC Day 0 Post-Op - 24-Hour PACU Night Shift, 1 Hz LLM Cadence`.

## Header and Footer

- Header right: `Demo 04 / Image 01 of 10 / Landscape`.
- Footer left: `Clinical-AI-Demos v0.2.0 / Demo 04 Post-Op Recovery Nurse`.
- Footer right: `DOI: 10.5281/zenodo.18445179 / MIT License`.

## Layout Specification

- Left two-thirds (x 0.0 to 0.66): architecture flowchart with three swimlanes.
- Right one-third (x 0.66 to 1.0): PACU recovery room layout with Digit V5 silhouette and 2 m perimeter.

## Inbound Lane (top)

Six rounded rectangles:

1. `Patient Vitals Bedside Monitors` (Teal).
2. `Chest Tube Drainage Rate Sensor` (Mauve).
3. `IV Pump Telemetry` (Mauve).
4. `Bed Pressure Mat (Braden Inputs)` (Slate).
5. `Pain Self-Report Pad` (Slate).
6. `Companion Repository Inputs` (Slate) annotated `patient-journey/stage_06_recovery.py, examples-new/`.

## Middle Lane (LLM + Digit V5 Loop)

Seven rounded rectangles in tiered order:

1. `Digit V5 Humanoid` (Deep Navy). Sub-label: `16 DOF, 1.8 m, 80 kg, IP54, 12-hour battery hot-swap`.
2. `Bedside State Aggregator (state.py)` (Slate).
3. `Tier 1 Claude Haiku 4.5 Default` (Teal). Sub-label: `50 ms latency, routine ticks`.
4. `Tier 2 Claude Sonnet 4.6 Escalation` (Teal darker). Sub-label: `500 ms, complex reasoning`.
5. `Tier 3 Ollama Llama 4 70B Local PHI Inference` (Teal darkest). Sub-label: `on-prem only, no PHI egress`.
6. `Safety Arbiter` (Burgundy). Sub-label: `IEC 80601-2-77; 100 ms E-stop; 12 N cumulative force`.
7. `Digit V5 Dispatcher` (Deep Navy).

Tier escalation arrows from Tier 1 to Tier 2 to Tier 3 labeled `escalate on confidence < 0.85`, `escalate if PHI required`.

Closed-loop arrow from Dispatcher back to Digit V5.

## Outbound Lane (bottom)

Six rounded rectangles:

1. `Braden 2-Hour Reposition Command` (Forest Green).
2. `Pain Score Re-Check Prompt` (Mauve).
3. `Chest Tube Removal Window Alert (Surgeon Activated)` (Burgundy).
4. `IV Pump Bolus Approval Request` (Burgundy).
5. `Audit Append (shift_llm_decisions.jsonl)` (Slate).
6. `On-Call Physician Activation if CTCAE Grade 3 or 4` (Burgundy darker).

## PACU Recovery Room Overlay (right one-third)

Stylized 4 m x 5 m PACU bay with:

- Patient bed centered.
- 2 m perimeter circle around the bed in Light Gray dashed line labeled `Digit V5 stays within 2 m`.
- Digit V5 silhouette at the patient head with sub-label `PACU Night-Shift Nurse`.
- Crash cart, IV pole, and monitoring rack along the perimeter.
- Exit door marked.

## Annotations

- Pinned to Tier 3 Llama 4 box: `On-prem Ollama-style. PHI-bearing inference only. Zero PHI egress. Wraps Tier 1 and Tier 2 outputs for PHI safety.`
- Pinned to Digit V5 box: `Stays within 2 m of patient at all times. Any 2 m excursion triggers immediate return-to-bedside with priority 1.0.`
- Pinned to Safety Arbiter: `100 ms patient-interaction grade E-stop. 12 N cumulative cross-arm force.`

## Color Mapping

Standard palette: humanoid Deep Navy, LLM tiers Teal (lighter to darker), safety Burgundy, audit Slate, output Forest Green, patient input Mauve.

## matplotlib Recipe

Same conventions as 01-01. Three swimlanes plus right one-third PACU bay overlay.

## Validation Checklist

1. PNG is 3300 x 2550 pixels.
2. Three-tier LLM stack visible.
3. PACU bay overlay with 2 m perimeter circle.
4. Digit V5 silhouette inside the bay.
5. Tier escalation arrows labeled.
6. Closed-loop return arrow.
7. Title, subtitle, header, footer present.
8. No em dash, no double dash, no triple dash.
9. No color outside palette.
10. No emoji.
