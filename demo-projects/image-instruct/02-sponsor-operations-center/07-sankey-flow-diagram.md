# Image Instruction 02-07: Sponsor Operations Center Document and Signal Sankey

[![Demo](https://img.shields.io/badge/Demo-02-brightgreen.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/blob/main/demo-projects/02-sponsor-humanoid-operations-center.md)
[![Image](https://img.shields.io/badge/Image-07%20of%2010-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/tree/main/demo-projects/image-instruct/02-sponsor-operations-center)
[![Orientation](https://img.shields.io/badge/Orientation-Portrait-orange.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)
[![DPI](https://img.shields.io/badge/DPI-300-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)

## Output Filename

`demo-projects/02-sponsor-humanoid-operations-center-output/figures/02-07-sankey-flow-diagram.png`

## Page Size and DPI

- Letter portrait, 8.5 x 11.0 inches, 300 dpi, 2550 x 3300 pixels, white facecolor.

## Chart Type

Sankey diagram with 5 vertical levels. Levels are: per-site CRA inputs, document class buckets, Safe Harbor PHI gate verdict, LLM tier selection, terminal publication channel.

## Title and Subtitle

- Title: `Sponsor Operations Center Weekly Document and Signal Sankey`.
- Subtitle: `5 Site CRAs to FDA, IRB, DSMB, Sponsor SOP, Site Response via Optimus + Sonnet/Opus`.

## Header and Footer

- Header right: `Demo 02 / Image 07 of 10 / Portrait`.
- Footer left: `Clinical-AI-Demos v0.2.0 / Demo 02 Sponsor Humanoid Operations Center`.
- Footer right: `DOI: 10.5281/zenodo.18445179 / MIT License`.

## Levels (5 columns)

1. **Level 1 Per-Site CRA Inputs**: `Site PAT-SITE-001 CRA`, `Site PAT-SITE-002 CRA`, `Site PAT-SITE-003 CRA`, `Site PAT-SITE-004 CRA`, `Site PAT-SITE-005 CRA`.
2. **Level 2 Document Class Bucket**: `CRA Call Summary`, `IMP Manifest`, `AE Report`, `SAE Narrative`, `IRB Amendment Draft`, `DSMB Snapshot`.
3. **Level 3 Safe Harbor PHI Gate Verdict**: `Pass (PHI Free)`, `Pass (Redacted)`, `Hold (Re-Run)`, `Block (Manual Review)`.
4. **Level 4 LLM Tier Selection**: `Sonnet 4.6 On-Prem Default`, `Opus 4.7 1M Cloud Failover`, `Sonnet + Opus Hybrid`.
5. **Level 5 Terminal Publication Channel**: `FDA RTCT Portal`, `IRB Portal`, `DSMB Charter Portal`, `Sponsor SOP Internal`, `Site Response Loop`.

## Flow Rules

Width proportional to document counts per week. Source-level color drives the flow color.

## Color Mapping

- Level 1: Deep Navy variants (5 shades).
- Level 2: Mauve (IMP), Burgundy (AE, SAE, IRB), Slate (CRA Call), Forest Green (DSMB).
- Level 3: Forest Green (Pass), Gold (Hold), Burgundy (Block).
- Level 4: Teal (Sonnet), Teal darker (Opus), Mauve (Hybrid).
- Level 5: Gold (FDA), Burgundy (IRB), Forest Green (DSMB and Sponsor SOP), Slate (Site Response).

## Layout, Annotations, matplotlib Recipe

Same conventions as 01-07. Bezier path patches for flows. Level titles at the top of each column. Callout near the right edge: `100 percent of flows reach a Level 5 channel within the 1-hour HR 9505 SLA budget at v0.2.0 freeze.`

## Validation Checklist

1. PNG is 2550 x 3300 pixels.
2. 5 columns of nodes with all listed entries.
3. Flow widths proportional and colored by source level.
4. Level titles at the top of each column.
5. Pinned callout near right edge.
6. Title, subtitle, header, footer present.
7. No em dash, no double dash, no triple dash.
8. No color outside palette.
9. No emoji.
10. Flow alpha 0.50.
