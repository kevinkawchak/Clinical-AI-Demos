# Image Instruction 05-01: Phoenix Gen 8 + Gemini 3 Pro / Qwen3 72B via MCP Pathology Lab Architecture

[![Demo](https://img.shields.io/badge/Demo-05-brightgreen.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/blob/main/demo-projects/05-humanoid-biospecimen-pathology-lab.md)
[![Image](https://img.shields.io/badge/Image-01%20of%2010-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/tree/main/demo-projects/image-instruct/05-biospecimen-pathology-lab)
[![Orientation](https://img.shields.io/badge/Orientation-Landscape-orange.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)
[![DPI](https://img.shields.io/badge/DPI-300-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)

## Output Filename

`demo-projects/05-humanoid-biospecimen-pathology-lab-output/figures/05-01-system-architecture-control-loop.png`

## Page Size and DPI

- Letter landscape, 11.0 x 8.5 inches, 300 dpi, 3300 x 2550 pixels, white facecolor.

## Chart Type

System architecture flowchart with explicit MCP (Model Context Protocol) server in the middle exposing 7 tools. Phoenix Gen 8 humanoid acts as the lab assistant; Gemini 3 Pro cloud and Ollama Qwen3 72B on-prem coordinate via MCP.

## Title and Subtitle

- Title: `Sanctuary Phoenix Gen 8 + Gemini 3 Pro / Ollama Qwen3 72B via MCP Server Pathology Lab Loop`.
- Subtitle: `CAP-Accredited Oncology Pathology Lab - 8 Fresh Biopsy Specimens, 12-Hour Shift, 100 ms LLM Cadence`.

## Header and Footer

- Header right: `Demo 05 / Image 01 of 10 / Landscape`.
- Footer left: `Clinical-AI-Demos v0.2.0 / Demo 05 Biospecimen Pathology Lab`.
- Footer right: `DOI: 10.5281/zenodo.18445179 / MIT License`.

## Layout

- Left two-thirds: control loop flowchart with the MCP server at the center.
- Right one-third: lab floor plan with stainer, microtome, embedder, fume hood, formalin tank, and microscope station.

## Inbound Lane (top)

1. `8 Fresh Biopsy Specimens (Surgical Pickup)` (Mauve).
2. `Cold Ischemia Timer (< 30 min)` (Burgundy).
3. `Patient Pathology Order (PHI-Tagged)` (Slate).
4. `CAP Q-Probes Reference SOPs` (Burgundy).
5. `21 CFR § 58 GLP Reference` (Burgundy darker).
6. `Companion Inputs from digital-twins/` (Slate).

## Middle Lane (Phoenix + Gemini + Qwen + MCP Loop)

Six rectangles plus the central MCP server box:

1. `Phoenix Gen 8 Humanoid` (Deep Navy). Sub-label: `24 DOF per hand, 0.5 mm RMS, EM-shielded for stainer electronics`.
2. `Lab State Aggregator` (Slate).
3. **`MCP Server (7 Tools)`** (Mauve fill, larger box centered) - sub-labels: `gross_examine, formalin_fix, process_tissue, embed_paraffin, microtome_section, stain_he, stain_ihc`.
4. `Gemini 3 Pro (Cloud, Safe Harbor Gated)` (Teal lighter).
5. `Ollama Qwen3 72B On-Prem (PHI Inference)` (Teal darker).
6. `Safety Arbiter` (Burgundy). Sub-label: `10 ms benchtop E-stop, 10 N cumulative force`.
7. `Phoenix Gen 8 Dispatcher` (Deep Navy).

Bidirectional arrows between MCP Server and both Gemini and Qwen labeled `tool calls`. Closed-loop return arrow Dispatcher to Phoenix.

## Outbound Lane (bottom)

1. `HE Stained Slide` (Forest Green).
2. `IHC Stained Slide (per antibody panel)` (Forest Green).
3. `Per-Specimen Pathology Report Draft` (Gold).
4. `Slide Image Capture (40x WSI)` (Slate).
5. `LIS Update with Cold Ischemia Timestamp` (Mauve).
6. `CAP Q-Probes Audit Trail Append` (Slate).

## Lab Floor Plan (right one-third)

Stylized 8 m x 6 m lab with Phoenix Gen 8 silhouette near the center. Stations labeled `Gross Examination Bench`, `Formalin Tank`, `Tissue Processor`, `Embedder`, `Microtome`, `HE Stainer`, `IHC Stainer`, `Microscope and Slide Scanner`.

## Annotations

- Pinned to MCP Server box: `7 tools exposed. Each tool call routes to either Gemini (cloud, Safe Harbor pre-redaction) or Qwen3 72B (on-prem, PHI-bearing). Tool selection at LLM discretion bounded by PHI tags.`
- Pinned to Phoenix Gen 8: `24 DOF per hand at 0.5 mm RMS handles paraffin-embedded blocks and microtome ribbons.`
- Pinned to Safety Arbiter: `EM-shielded chassis; 10 ms benchtop E-stop; 10 N cumulative force ceiling for delicate tissue handling.`

## Color Mapping

Humanoid Deep Navy. MCP server Mauve (highlight color). LLMs Teal (lighter Gemini, darker Qwen). Safety Burgundy. Outputs Forest Green or Gold. Slate for state/audit. Mauve for specimens.

## matplotlib Recipe

Same conventions as prior architecture instructions.

## Validation Checklist

1. PNG is 3300 x 2550 pixels.
2. MCP server prominent in the middle.
3. 7 tool names listed inside the MCP box.
4. Bidirectional arrows to Gemini and Qwen.
5. Lab floor plan on right.
6. Closed-loop return arrow.
7. Title, subtitle, header, footer present.
8. `§` in `21 CFR § 58`.
9. No em dash, no double dash, no triple dash.
10. No color outside palette.
