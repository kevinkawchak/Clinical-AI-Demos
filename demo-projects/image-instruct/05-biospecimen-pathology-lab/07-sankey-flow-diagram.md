# Image Instruction 05-07: Pathology Specimen Lifecycle Sankey

[![Demo](https://img.shields.io/badge/Demo-05-brightgreen.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/blob/main/demo-projects/05-humanoid-biospecimen-pathology-lab.md)
[![Image](https://img.shields.io/badge/Image-07%20of%2010-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/tree/main/demo-projects/image-instruct/05-biospecimen-pathology-lab)
[![Orientation](https://img.shields.io/badge/Orientation-Portrait-orange.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)
[![DPI](https://img.shields.io/badge/DPI-300-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)

## Output Filename

`demo-projects/05-humanoid-biospecimen-pathology-lab-output/figures/05-07-sankey-flow-diagram.png`

## Page Size and DPI

- Letter portrait, 8.5 x 11.0 inches, 300 dpi, 2550 x 3300 pixels, white facecolor.

## Chart Type

Sankey with 4 vertical levels covering specimen lifecycle.

## Title and Subtitle

- Title: `Phoenix Gen 8 Pathology Lab 12-Hour Specimen Lifecycle Sankey`.
- Subtitle: `8 Specimens from Surgical Pickup to Pathology Report (CAP-Accredited)`.

## Header and Footer

- Header right: `Demo 05 / Image 07 of 10 / Portrait`.
- Footer left: `Clinical-AI-Demos v0.2.0 / Demo 05 Biospecimen Pathology Lab`.
- Footer right: `DOI: 10.5281/zenodo.18445179 / MIT License`.

## Levels (4)

1. **Level 1 Specimen Type**: `Lung Wedge`, `Breast Core Bx`, `Colon Polypectomy`, `Prostate Needle Bx`, `Pancreas FNA`, `Lymph Node`, `Liver Core Bx`, `Skin Punch`.
2. **Level 2 MCP Tool Used**: `gross_examine`, `formalin_fix`, `process_tissue`, `embed_paraffin`, `microtome_section`, `stain_he`, `stain_ihc`.
3. **Level 3 LLM Verdict**: `Pass (Phoenix Continue)`, `Hold for Pathologist Review`, `Re-Process Specimen`.
4. **Level 4 Terminal**: `Pathology Report Drafted`, `Pathologist Co-Signed`, `LIS Update`, `Specimen Archive`.

## Color, Layout, Annotations, matplotlib Recipe

Same conventions as prior sankey instructions. Mauve for specimen types, Slate for MCP tool calls, Teal for LLM verdicts, Forest Green / Gold / Slate for terminals. Pinned callout: `8 specimens reach Pathologist Co-Sign within the 12-hour shift. 1 specimen typically Re-Processed (IHC bleed-through).`

## Validation Checklist

1. PNG is 2550 x 3300 pixels.
2. 4 columns of nodes.
3. Flow widths proportional.
4. Level titles.
5. Callout.
6. Title, subtitle, header, footer present.
7. No em dash, no double dash, no triple dash.
8. No color outside palette.
9. No emoji.
10. Flow alpha 0.50.
