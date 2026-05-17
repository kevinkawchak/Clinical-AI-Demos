# Image Instruction 10-01: Figure 03 Field Edition + Claude Haiku 4.5 Edge Home DCT Architecture

[![Demo](https://img.shields.io/badge/Demo-10-brightgreen.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/blob/main/demo-projects/10-humanoid-decentralized-home-care.md)
[![Image](https://img.shields.io/badge/Image-01%20of%2010-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/tree/main/demo-projects/image-instruct/10-decentralized-home-care)
[![Orientation](https://img.shields.io/badge/Orientation-Landscape-orange.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)
[![DPI](https://img.shields.io/badge/DPI-300-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)

## Output Filename

`demo-projects/10-humanoid-decentralized-home-care-output/figures/10-01-system-architecture-control-loop.png`

## Page Size and DPI

- Letter landscape, 11.0 x 8.5 inches, 300 dpi, 3300 x 2550 pixels, white facecolor.

## Chart Type

System architecture flowchart for the home DCT scenario. The Figure 03 Field Edition humanoid runs Claude Haiku 4.5 on the onboard NVIDIA Orin AGX 64GB with zero PHI egress. A federated learning aggregator on the sponsor side receives only de-identified per-cycle summaries. Right one-third shows the rural Iowa single-floor home layout and the van transport for between-visit relocation.

## Title and Subtitle

- Title: `Figure 03 Field Edition + Claude Haiku 4.5 on NVIDIA Orin AGX 64GB Home DCT Loop`.
- Subtitle: `PAT-DCT-0001 Stage IV mCRPC - 24-Hour Cycle - 4-Hour Active Visit at 1 Hz + 20-Hour Ambient at 0.1 Hz`.

## Header and Footer

- Header right: `Demo 10 / Image 01 of 10 / Landscape`.
- Footer left: `Clinical-AI-Demos v0.2.0 / Demo 10 Decentralized Home Care`.
- Footer right: `DOI: 10.5281/zenodo.18445179 / MIT License`.

## Layout

- Left two-thirds: 3-swimlane edge-deployed control loop with a prominent PHI Egress Boundary line separating edge from federated aggregator.
- Right one-third: rural Iowa 90 m^2 single-floor home overlay with Figure 03 silhouette and overnight charging dock, plus the van for between-visit transport.

## Inbound Lane (top, edge side)

1. `Patient Vitals Wearable + Bedside Monitor` (Mauve).
2. `Patient Daily Self-Report Tablet` (Slate).
3. `Olaparib Pill Box RFID` (Mauve darker).
4. `Lu-177 PSMA-617 Infusion Reminder` (Burgundy).
5. `Patient Family Caregiver Note` (Gold).
6. `HR 9507 Data Self-Custody Election Token` (Burgundy darker).

## Middle Lane (Figure 03 Field Edition + Edge LLM Loop)

Six rectangles, all on the edge side of the boundary:

1. `Figure 03 Field Edition Humanoid` (Deep Navy). Sub-label: `32 DOF, 1.68 m, 28 kg lightweight, IP65, foldable, 18-hour battery`.
2. `Home State Aggregator (state.py)` (Slate).
3. `Claude Haiku 4.5 on Orin AGX 64GB` (Teal). Sub-label: `50 ms edge latency, ZERO PHI egress`.
4. `Safety Arbiter` (Burgundy). Sub-label: `100 ms patient-interaction E-stop; 12 N cumulative force`.
5. `Figure 03 Dispatcher` (Deep Navy).
6. `Per-Cycle De-Identification + Federation Encoder` (Slate lighter).

A vertical dashed Burgundy line labeled `PHI Egress Boundary - HR 9507 Hard-Gate`.

## Sponsor Lane (right side of boundary)

3 boxes:

1. `Federated Learning Aggregator (sponsor side)` (Teal lighter).
2. `Sponsor Claude Opus 4.7 1M (de-identified summaries only)` (Teal darker).
3. `Cross-Patient Cohort Insights` (Forest Green).

## Outbound Lane (bottom, edge side)

1. `Per-Visit Vitals Log (Edge-Only)` (Mauve).
2. `Pill Adherence Log (Edge-Only)` (Slate).
3. `Lu-177 Infusion Confirmation (Edge-Only)` (Burgundy).
4. `Family Caregiver Update (Patient Approved Only)` (Gold).
5. `Per-Cycle De-Identified Summary (to Aggregator)` (Slate lighter).
6. `HR 9507 Patient Revocation Flag` (Burgundy darker).

## Home Layout Overlay (right one-third)

Stylized 90 m^2 single-floor home with:
- Patient bedroom with bed and bedside vitals monitor.
- Living room with patient recliner.
- Kitchen with pill box dock.
- Bathroom (Figure 03 stays outside without explicit invitation).
- Overnight charging dock for Figure 03.
- Driveway with van transport visible.

## Annotations

- Pinned to Claude Haiku on Orin: `Edge-deployed. 50 ms latency. ZERO PHI egress. Sponsor side never sees raw PHI.`
- Pinned to PHI Egress Boundary: `HR 9507 Data Self-Custody is the primary right. Patient may revoke aggregator submission for any cycle in real time.`
- Pinned to Figure 03 Field Edition: `Foldable for van transport between patient homes. 18-hour battery with overnight charging dock.`

## Color Mapping

Humanoid Deep Navy. Edge LLM Teal. Safety Burgundy. Patient inputs Mauve. PHI boundary Burgundy. Federation aggregator Teal lighter. Sponsor cross-cohort Forest Green. Audit Slate.

## matplotlib Recipe

Same conventions as prior architecture instructions. Use a vertical dashed line drawn with `ax.axvline(x_boundary, linestyle='--', color='#8B2E3F', lw=1.5)` and annotate.

## Validation Checklist

1. PNG is 3300 x 2550 pixels.
2. PHI Egress Boundary line visible.
3. Edge side and federated aggregator side clearly separated.
4. Home layout overlay with charging dock and van.
5. HR 9507 references present.
6. Title, subtitle, header, footer present.
7. `m^2` notation correct.
8. No em dash, no double dash, no triple dash.
9. No color outside palette.
10. No emoji.
