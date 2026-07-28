#### Output-04: Phase 1 PDAC + LLM Trial Protocol Six-Platform Diagram Atlas
- [README.md](https://github.com/kevinkawchak/Clinical-AI-Demos/tree/main/ai-outputs/output-04)

[![Output](https://img.shields.io/badge/Output-04-1F3A68.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/tree/main/ai-outputs/output-04)
[![Diagrams](https://img.shields.io/badge/Mermaid%20Type%20Perspectives-20-2E8B8B.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/tree/main/ai-outputs/output-01)
[![Diagrams](https://img.shields.io/badge/Excalidraw%20Type%20Perspectives-20-8B2E3F.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/tree/main/ai-outputs/output-01)
[![Diagrams](https://img.shields.io/badge/PlantUML%20Type%20Perspectives-20-C18A2C.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/tree/main/ai-outputs/output-01)
[![Diagrams](https://img.shields.io/badge/D2%20Type%20Perspectives-20-2F6B3E.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/tree/main/ai-outputs/output-01)
[![Diagrams](https://img.shields.io/badge/Diagrams%20(Python)%20Type%20Perspectives-20-2E8B8B.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/tree/main/ai-outputs/output-01)
[![Diagrams](https://img.shields.io/badge/Graphviz%20Type%20Perspectives-20-8B2E3F.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/tree/main/ai-outputs/output-01)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


# A Six-Platform Diagram Atlas (v1.0.0)

[![License](https://img.shields.io/badge/License-CC%20BY%204.0-yellow.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Figures](https://img.shields.io/badge/Figures-120%20(6%20%C3%97%2020)-00417A.svg)](main.tex)
[![Platforms](https://img.shields.io/badge/Platforms-6-00417A.svg)](main.tex)
[![Rendering](https://img.shields.io/badge/Rendering-100%25%20TikZ%20vector-6C757D.svg)](dxstyle.sty)
[![Raster images](https://img.shields.io/badge/Raster%20images-0-6C757D.svg)](dxstyle.sty)
[![Compiles](https://img.shields.io/badge/Overleaf-pdfLaTeX-6C757D.svg)](main.tex)
[![ORCID](https://img.shields.io/badge/ORCID-0009--0007--5457--8667-A6CE39.svg)](https://orcid.org/0009-0007-5457-8667)
[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.20780121-blue.svg)](https://doi.org/10.5281/zenodo.20780121)

A companion diagram atlas for the Phase 1, first-in-human, combined IND/IDE
clinical trial protocol of **on-premises LLM-directed robotic
pancreaticoduodenectomy (Whipple) with perioperative daraxonrasib (RMC-6236) in
KRAS-mutated pancreatic ductal adenocarcinoma**.

The parent publication
([`trial-protocol/final-protocol/publication`](https://github.com/kevinkawchak/physical-ai-oncology-trials/tree/main/trial-protocol/final-protocol/publication))
carries 20 TikZ figures. This atlas adds **120 more**: six sections of twenty,
each section adopting the idiom of one open-source diagram platform and applying
that idiom to the facets of the protocol that platform expresses best. **No
figure repeats a figure of the parent publication.** Every figure is a new
perspective on data, structure, or argument already present in the protocol.

---

## The six sections

| § | Platform | Figures are called | Strength the twenty figures exploit |
|:--|:--|:--|:--|
| 1 | [Mermaid](https://mermaid.js.org) (MIT) | **mermaid-type** | Decisions in time: `flowchart`, `sequenceDiagram`, `classDiagram`, `stateDiagram-v2`, `erDiagram`, `gantt`, `journey`, `pie`, `quadrantChart`, `mindmap`, `timeline`, `gitGraph`, `sankey-beta`, `requirementDiagram`, `C4Context`, `block-beta`, `xychart-beta`, `packet-beta`, `kanban`, `architecture-beta` |
| 2 | [Excalidraw](https://excalidraw.com) (MIT) | **excalidraw-type** | Deliberately unfinished thinking: whiteboards, floor plans, sticky-note clustering, storyboards, 2×2 matrices, gauges, wireframes, napkin arithmetic |
| 3 | [PlantUML](https://plantuml.com) (GPL/LGPL/Apache) | **PlantUML-type** | Formal notation: the full UML set plus `timing`, `salt`, `wbs`, `gantt`, ArchiMate layering, and C4 containers |
| 4 | [D2](https://d2lang.com) (MPL-2.0) | **D2-type** | Nesting and tabulation: containers within containers, true `grid` layouts, `sql-table` and `class` shapes, and `layers`/`steps` storytelling |
| 5 | [Diagrams (Python)](https://diagrams.mingrammer.com) (MIT) | **Diagrams (Python)-type** | Infrastructure reality: clustered deployment, data pipelines, network segmentation, failover, lifecycle, and publication architecture |
| 6 | [Graphviz](https://graphviz.org) (EPL) | **Graphviz-type** | Pure graph structure: `dot` DAGs and record nodes, `circo` rings, `twopi` radials, `neato`/`fdp` embeddings, fault and event trees, bipartite maps |

**Figure numbering restarts at Figure 1 in each section and ends at Figure 20**,
so a citation must name both, for example *Section 4, Figure 11 (D2-type)*.

### Naming rule

The figures are **drawn natively in LaTeX with TikZ**, not rendered by the
platforms themselves. They must therefore not be called Mermaid diagrams,
PlantUML diagrams, and so on. Every caption states the type explicitly
(`mermaid-type`, `excalidraw-type`, `PlantUML-type`, `D2-type`,
`Diagrams (Python)-type`, `Graphviz-type`), and the monospace tag in the top
left of every frame names the native construct being reproduced — for example
`flowchart TD`, `@startuml / sequence`, `d2: grid-rows / grid-columns`,
`diagrams: Diagram + Cluster`, or `digraph { rankdir=LR }` — so any figure can
be carried back to its platform of origin.

---

## Files

```
physical-ai-diagram-atlas/
  main.tex        cover, "how to read", clickable TOC, 6 sections x 20 figures
  dxstyle.sty     palette, figure frame, caption rule, and the six TikZ vocabularies
  references.bib  parent protocol bibliography + the six diagram platforms + PGF/TikZ
  README.md       this file
```

Nothing else is required. There are no images, no generated assets, no external
data files, and no shell-escape.

---

## Compile (Overleaf, pdfLaTeX)

Upload the four files to a new Overleaf project, set the compiler to
**pdfLaTeX**, and set `main.tex` as the main document.

```
pdflatex main
bibtex   main
pdflatex main
pdflatex main
```

The document is TikZ-heavy (120 pictures); a full four-pass build takes a few
minutes on Overleaf. Nothing in the build requires `--shell-escape`, a custom
TeX Live version, or any package outside a standard full TeX Live / Overleaf
installation.

**Packages used:** `mathptmx`, `helvet`, `courier`, `geometry`, `xcolor`,
`amsmath`, `amssymb`, `microtype`, `array`, `longtable`, `tabularx`,
`xltabular`, `ragged2e`, `needspace`, `enumitem`, `booktabs`, `caption`,
`adjustbox`, `ifthen`, `tikz` (+ 20 libraries), `fancyhdr`, `titlesec`,
`hyperref`, `url`.

---

## Design rules honoured throughout

**Palette.** Inherited verbatim from the parent `protostyle.sty`: Corporate Blue
`#00417A`, Professional Gray `#6C757D`, Classic White, near-black `#222222`, and
the light grays `#E9ECEF` / `#D9D9D9`. It is extended **only** by tints and
shades of those same two hues (`pb1`–`pb8`, `pg1`–`pg6`), so the atlas and the
protocol remain colour-consistent. ORCID green `#A6CE39` is reserved, as in the
parent style, for the ORCID mark and pass/verified states.

**Frame.** One centred, black-ruled, white-background frame for all 120 figures.
The frame fits itself to the text measure and to the page (`adjustbox` with
`max width` and `max totalheight`), so no figure can overflow horizontally or
vertically regardless of its internal coordinates.

**Captions.** Each caption is broken with explicit `\\` so that **every line
carries a rendered character count close to the line below it**. The break
points are chosen by a minimum-raggedness dynamic program that minimises the
squared deviation of each line's length from the mean line length.

**Vector only.** All 120 figures are TikZ. There are no raster images anywhere,
including the icons in Section 5, which are hand-drawn vector pictograms defined
in `dxstyle.sty` (`\glyphserver`, `\glyphdb`, `\glyphrobot`, `\glyphshield`, and
sixteen more).

**Machine readable and open source.** The figure source is plain text under an
open licence, re-editable without a proprietary tool, and every figure declares
the open-source construct it reproduces.

---

## Quantitative content

The figures are built from the protocol's own constants, so they can be checked
against it directly: the 3+3 escalation over DL1 160 mg / DL2 220 mg / DL3 300 mg
with a 28-day DLT window and *n* up to 18; the Phase 0 gate (≥ 1000 simulated
procedures, ≥ 2 independent frameworks, USL ≥ 7.0, trajectory gap < 2 mm,
tip-force gap < 0.5 N); the platform (8 arms, 56 DOF, 640 channels at 80 per arm,
0.05 mm RMS at 1,200 mm/s, 100 kHz force and 10 kHz command rates); the safety
envelope (≤ 3 N per arm, ≤ 18 N cumulative, 10 kHz heartbeat on a 64-byte frame
with a 100 µs watchdog, 50 µs arm park, ≤ 3 ms cross-arm E-stop, ≤ 500 ms
hardware E-stop); the five-vessel zone gate (3.0 mm soft warning, 1.0 mm no-fly
at SMV/PV, 1.5 mm at HA/CA/SMA, 5.0 mm hard stop, and the 83/6/6/5 verdict
sample); the three anastomosis bands (PJ 0.30–0.60 N, HJ 0.20–0.50 N,
GJ 0.40–0.80 N); the restart advisory sweep (29/32 T+7d, 3/32 T+14d, 0/32 T+21d,
trough 0.45 vs 0.50 ng/mL); and the Dutch 2025 comparators (conversion 10.1 %,
Clavien-Dindo III+ 41.3 %, ISGPS B/C 24.4 %, 30-day mortality 3.9 %).

Two figures compute values the parent protocol asserts but does not tabulate:
Section 1 Figure 17 gives the exact 3+3 operating characteristic
*P*(escalate) = (1−*p*)³ + 3*p*(1−*p*)⁵ across true DLT rates, and Section 2
Figure 20 and Section 4 Figure 18 give exact Clopper-Pearson intervals at the
planned sample sizes.

---

## Provenance and scope

Independent research draft. **Not** an active IND or IDE, not an approved
protocol, and not medical or regulatory advice; not endorsed by the FDA, NIH,
HHS, an IRB, ICH, or any sponsor. Clinical figures derive from the author's
simulation sources and are illustrative unless tied to a cited reference. The
synthetic reference exemplar `PAT-PDAC-0001` is used for design illustration and
does not represent an enrolled individual.

The six diagram platforms are cited in `references.bib` and are **not invoked at
compile time** — this atlas depends on none of them to build.

---

## License

Released under CC BY 4.0. Author: Kevin Kawchak, CEO ChemicalQDevice
([ORCID 0009-0007-5457-8667](https://orcid.org/0009-0007-5457-8667)).
