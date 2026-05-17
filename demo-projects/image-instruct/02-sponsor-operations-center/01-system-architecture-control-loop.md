# Image Instruction 02-01: 5x Optimus + Sonnet/Opus Failover Sponsor Operations Center Architecture

[![Demo](https://img.shields.io/badge/Demo-02-brightgreen.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/blob/main/demo-projects/02-sponsor-humanoid-operations-center.md)
[![Image](https://img.shields.io/badge/Image-01%20of%2010-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/tree/main/demo-projects/image-instruct/02-sponsor-operations-center)
[![Orientation](https://img.shields.io/badge/Orientation-Landscape-orange.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)
[![DPI](https://img.shields.io/badge/DPI-300-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)

## Output Filename

`demo-projects/02-sponsor-humanoid-operations-center-output/figures/02-01-system-architecture-control-loop.png`

## Page Size and DPI

- Letter landscape, 11.0 x 8.5 inches, 300 dpi, 3300 x 2550 pixels, white facecolor.

## Chart Type

System architecture flowchart for the SPO-2026-001 40th-floor pharmaceutical sponsor Humanoid Operations Center. Five Tesla Optimus Gen 3 humanoids operate in parallel; the LLM control loop is a tiered Claude Sonnet 4.6 on-prem default with a Claude Opus 4.7 1M cloud failover gated by the HIPAA 45 CFR § 164.514(b) Safe Harbor PHI redaction.

## Title and Subtitle

- Title: `5x Tesla Optimus Gen 3 + Claude Sonnet 4.6 / Opus 4.7 1M Failover Sponsor Operations Center`.
- Subtitle: `SPO-2026-001 40th Floor - 5 Active Oncology Trials, 168-Hour Weekly Cycle, 604,800 LLM Ticks at 1 Hz`.

## Header and Footer

- Header right: `Demo 02 / Image 01 of 10 / Landscape`.
- Footer left: `Clinical-AI-Demos v0.2.0 / Demo 02 Sponsor Humanoid Operations Center`.
- Footer right: `DOI: 10.5281/zenodo.18445179 / MIT License`.

## Layout Specification

- Left two-thirds (x 0.0 to 0.66) holds the architecture flowchart.
- Right one-third (x 0.66 to 1.0) holds the 40th-floor map with the 5 humanoid stations labeled.
- Three horizontal swimlanes in the left two-thirds:
  1. Inbound document and signal lane at y 0.70 to 0.92.
  2. Tiered LLM and Optimus humanoid loop lane at y 0.32 to 0.66.
  3. Outbound document and signal lane at y 0.06 to 0.28.

## Inbound Document and Signal Lane (top)

Six rounded rectangles:

1. `5 Site CRA Call Streams` (Slate).
2. `5 IMP Kit Manifests` (Mauve).
3. `IRB Amendment Drafts` (Burgundy).
4. `5 Trial AE Reports` (Burgundy).
5. `SAE Narratives` (Burgundy darker).
6. `DSMB Monthly Summaries` (Forest Green).

## Tiered LLM and Optimus Humanoid Loop Lane (middle)

Six rounded rectangles connected by arrows:

1. `Document Aggregator (doc_ingest.py)` (Slate).
2. `Safe Harbor PHI Gate (privacy/de-identification/)` (Burgundy fill, white text).
3. `Claude Sonnet 4.6 On-Prem Default` (Teal). Sub-label: `100 ms latency, no PHI egress`.
4. `Claude Opus 4.7 1M Cloud Failover` (Teal darker). Sub-label: `200 ms median, PHI-redacted payload only`.
5. `5x Tesla Optimus Gen 3 Bench` (Deep Navy fill). Sub-label: `43 DOF each, 1.73 m, 57 kg, 5-finger hand for vial gripping, 8 mm min inter-humanoid distance`.
6. `Optimus Dispatch and SOP Author` (Deep Navy).

A failover arrow from Sonnet to Opus is annotated `gated by Safe Harbor PHI redaction`. A closed-loop arrow from the Optimus Dispatch back to the 5x Optimus Bench. A second feedback arrow from the dispatcher to the Document Aggregator labeled `published reports recirculate to next tick state`.

## Outbound Document and Signal Lane (bottom)

Six rounded rectangles:

1. `FDA RTCT Submission Packet` (Gold).
2. `IRB Amendment (Approved Final)` (Burgundy).
3. `CRA Call Summary Returned` (Slate).
4. `Updated IMP Kit Manifest` (Mauve).
5. `Sponsor SOP Update Published` (Forest Green).
6. `Per-Tick Audit Log Append` (Slate).

## Facility Map Overlay (right one-third)

A stylized 40th-floor plan with 5 Optimus Gen 3 humanoid stations spaced for the 8 mm minimum inter-humanoid distance plus a 1.5 m operator clearance:

- Station A `Sonnet Console + Optimus 1`.
- Station B `Document Ingest + Optimus 2`.
- Station C `IMP Manifest Bench + Optimus 3`.
- Station D `Safe Harbor Gate + Optimus 4`.
- Station E `FDA RTCT Bench + Optimus 5`.

A center node `Sponsor CRO Hub` and a perimeter callout `Anthropic Cowork Tunnel Endpoint`.

## Annotations

- Pinned to the Safe Harbor PHI Gate box: `45 CFR § 164.514(b) Safe Harbor; 18 identifiers stripped before cloud failover.`
- Pinned to the Claude Opus 4.7 1M Cloud Failover box: `Triggers only when Sonnet returns confidence below 0.85 or token budget exceeded.`
- Pinned to the 5x Optimus Bench: `25 N cumulative cross-arm force limit. 100 ms E-stop budget.`

## Color Mapping

- Humanoid: Deep Navy.
- LLM tiers: Teal (Sonnet lighter, Opus darker).
- Safety / Safe Harbor: Burgundy.
- Document inputs and outputs: Slate (general), Mauve (IMP), Gold (financial/regulatory submission), Forest Green (resolved outputs).

## matplotlib Recipe

- `matplotlib.patches.FancyBboxPatch` for every component (`boxstyle='round,pad=0.02,rounding_size=0.04'`).
- `matplotlib.patches.FancyArrowPatch` for arrows (`arrowstyle='->,head_length=8,head_width=6'`).
- Closed-loop return arrow with `connectionstyle='arc3,rad=0.25'`.
- `ax.set_xlim(0, 1)`, `ax.set_ylim(0, 1)`, `ax.set_axis_off()`.
- Reserve top 0.05 for title, bottom 0.05 for footer.

## Validation Checklist

1. PNG is 3300 x 2550 pixels.
2. All 5 Optimus Gen 3 stations appear on the facility map.
3. Tiered LLM box pair (Sonnet default + Opus failover) clearly distinguished.
4. Safe Harbor gate box prominently in Burgundy.
5. Closed-loop return arrow present.
6. Title, subtitle, header, footer present.
7. `§` appears in `45 CFR § 164.514(b)`.
8. No em dash, no double dash, no triple dash.
9. No color outside palette.
10. No emoji.
