# Image Instruction 09-01: Atlas + Optimus Dual-Humanoid LINAC Architecture

[![Demo](https://img.shields.io/badge/Demo-09-brightgreen.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/blob/main/demo-projects/09-humanoid-radiation-oncology-technologist.md)
[![Image](https://img.shields.io/badge/Image-01%20of%2010-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/tree/main/demo-projects/image-instruct/09-radiation-oncology-technologist)
[![Orientation](https://img.shields.io/badge/Orientation-Landscape-orange.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)
[![DPI](https://img.shields.io/badge/DPI-300-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)

## Output Filename

`demo-projects/09-humanoid-radiation-oncology-technologist-output/figures/09-01-system-architecture-control-loop.png`

## Page Size and DPI

- Letter landscape, 11.0 x 8.5 inches, 300 dpi, 3300 x 2550 pixels, white facecolor.

## Chart Type

System architecture flowchart for the dual-humanoid LINAC vault. Atlas Electric is the patient handler (never touches the LINAC), Tesla Optimus Gen 3 is the machine operator (never touches the patient except during emergency E-stop). NVIDIA GR00T N1.6 humanoid foundation model plus NVIDIA Cosmos Reason 2 vision-language model plus Claude Opus 4.7 1M arbiter at 3 decision gates.

## Title and Subtitle

- Title: `Boston Dynamics Atlas + Tesla Optimus Gen 3 + GR00T / Cosmos / Claude Arbiter LINAC Vault Loop`.
- Subtitle: `Varian Edge HyperArc + kV CBCT + 6D Couch - 10 Glioblastoma SRS Patients - 8-Hour Shift, 100 ms LLM Cadence`.

## Header and Footer

- Header right: `Demo 09 / Image 01 of 10 / Landscape`.
- Footer left: `Clinical-AI-Demos v0.2.0 / Demo 09 Radiation Oncology Technologist`.
- Footer right: `DOI: 10.5281/zenodo.18445179 / MIT License`.

## Layout

- Left two-thirds: 4-swimlane flowchart.
- Right one-third: LINAC vault floor plan showing Atlas at the couch and Optimus at the gantry console, with 1.5 m inter-humanoid minimum distance marker.

## Patient-Side Lane (top)

1. `Glioblastoma Patient (Mask Immobilization)` (Mauve).
2. `Atlas Electric (Patient Handler, Never Touches LINAC)` (Deep Navy). Sub-label: `28 DOF, 1.5 m, 89 kg, 11 kg per-arm`.
3. `Patient State Aggregator (vitals, position)` (Slate).
4. `Mask Immobilization Verifier` (Slate).
5. `kV CBCT Alignment Check (sub-millimeter)` (Mauve darker).

## LLM Loop Lane (middle-top)

Four boxes:

1. `NVIDIA GR00T N1.6 Humanoid Foundation Model` (Teal). Sub-label: `DGX SuperPOD on-prem, 100 ms cadence, both humanoid action prediction`.
2. `NVIDIA Cosmos Reason 2 Vision-Language Model` (Teal lighter). Sub-label: `vision plus reasoning, anatomy and machine state`.
3. **`Claude Opus 4.7 1M Arbiter`** (Teal darker, larger). Sub-label: `3 decision gates: treatment authorization, CBCT tolerance, emergency E-stop`.
4. `Safety Arbiter + IEC 80601-2-77 + ISO 10218` (Burgundy). Sub-label: `5 ms surgical-grade E-stop; 22 N cumulative cross-humanoid force`.

## Machine-Side Lane (middle-bottom)

1. `Tesla Optimus Gen 3 (Machine Operator, Never Touches Patient)` (Deep Navy lighter). Sub-label: `43 DOF, 1.73 m, 57 kg`.
2. `Varian Edge LINAC Console` (Mauve darker).
3. `HyperArc Plan Loader (Adaptive RT Plan)` (Forest Green).
4. `6D Couch Controller` (Slate).
5. `LINAC Beam Hold Interlock` (Burgundy).

## Outbound Lane (bottom)

1. `Per-Fraction Dose Report (NRC 10 CFR § 35)` (Gold).
2. `AAPM TG-100 Risk-Informed QM Snapshot` (Burgundy).
3. `AAPM TG-142 LINAC QA Append` (Slate).
4. `Adaptive RT DT Update (Digital Twin)` (Forest Green).
5. `Pre-Treatment to Post-Treatment Audit` (Slate).

## LINAC Vault Floor Plan (right one-third)

Stylized 6 m x 7 m vault:
- LINAC gantry with HyperArc collimator.
- 6D couch with patient mask immobilization.
- Atlas silhouette beside the couch (patient handler).
- Optimus silhouette at the LINAC console (machine operator).
- 1.5 m inter-humanoid minimum distance dashed circle around each.
- Vault door with bunker entry interlock.
- Treatment control room window.

## Annotations

- Pinned to Atlas: `Never touches the LINAC. Strict scope of practice: patient handling + mask verification only.`
- Pinned to Optimus: `Never touches the patient except during emergency E-stop. Strict scope: machine operation only.`
- Pinned to Claude Opus Arbiter: `3 decision gates: (1) Treatment Delivery Authorization, (2) CBCT Alignment Tolerance Escalation, (3) Emergency E-Stop. Each gate hash-chained to LINAC log.`
- Pinned to Safety Arbiter: `1.5 m inter-humanoid minimum distance enforced. 22 N cumulative cross-humanoid force ceiling during patient transfer.`

## Color Mapping

Atlas Deep Navy. Optimus Deep Navy lighter. NVIDIA LLMs Teal lighter and mid. Claude Opus Arbiter Teal darker. Safety Burgundy. LINAC Mauve. Outputs Gold / Forest Green. Audit Slate.

## matplotlib Recipe

Same conventions as prior architecture instructions.

## Validation Checklist

1. PNG is 3300 x 2550 pixels.
2. Both humanoids shown in separate roles.
3. Claude Opus Arbiter prominent with 3 gates labeled.
4. LINAC vault floor plan with 1.5 m distance markers.
5. NRC 10 CFR § 35 reference appears.
6. Title, subtitle, header, footer present.
7. No em dash, no double dash, no triple dash.
8. No color outside palette.
9. No emoji.
10. AAPM TG-100 and TG-142 references correct.
