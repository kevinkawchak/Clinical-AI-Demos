# LaTeX Source File Templates 01-30 (output-02)

[![License](https://img.shields.io/badge/License-CC%20BY%204.0-yellow.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Templates](https://img.shields.io/badge/Templates-30%20zips-blue.svg)](.)
[![Single column](https://img.shields.io/badge/Layout-Single%20column-green.svg)](.)
[![Preview](https://img.shields.io/badge/Preview-30--page%20cover%20PDF-orange.svg)](LaTeX-Source-Files-Cover-Pages.pdf)

*Independent research drafts. Not enacted law and not legal advice; not endorsed
by the FDA, HHS, or any Member of Congress.*

This directory holds **30 single-column LaTeX zip templates** for future
legislative publications, each building on the open-source **INSPIRATIONS**
listed below. Every template carries minimal placeholder text so a title and a
short paragraph per section can be swapped in quickly. The titles and headings
are themed; the prose is intentionally short.

## Templates by type

- **01-12 - Legislative deliverables (12).** One per deliverable in `cancer-automated/papers/VVUQ-05/final-bill/deliverables`; built on the bill caption apparatus and Table 1 of VVUQ-05 and the back matter of VVUQ-03.
- **13-17 - Coding, monospaced (5).** Mainstream code-doc look in Courier, Inconsolata, Anonymous Pro, Source Code Pro, and DejaVu Sans Mono.
- **18-22 - Oncology clinical trials (5).** Protocol, patient journey, adverse event response, site operations, and national platform.
- **23-27 - VVUQ (5).** Method and pipeline, ten-gate threshold spec, evidence-to-law assessment, uncertainty quantification, and the standard.
- **28-30 - Physical AI (3).** Surgical humanoid system, sensor-stream safety, and embodied control and camaraderie.

## Directory structure

```
ai-outputs/output-02/
  README.md                          (this file: structure, TOC, conventions)
  LaTeX-Source-Files-Cover-Pages.pdf (one cover-page preview per template, 30 pages)
  LaTeX-Source-Files-01.zip          (legislative: one-page summary)
  LaTeX-Source-Files-02.zip          (legislative: section-by-section analysis)
  ...                                 ...
  LaTeX-Source-Files-12.zip          (legislative: testimony and influence brief)
  LaTeX-Source-Files-13.zip          (coding: robot-patient code reference)
  ...                                 ...
  LaTeX-Source-Files-17.zip          (coding: test and error-check harness manual)
  LaTeX-Source-Files-18.zip          (oncology: trial protocol)
  ...                                 ...
  LaTeX-Source-Files-22.zip          (oncology: national platform)
  LaTeX-Source-Files-23.zip          (VVUQ: method and pipeline)
  ...                                 ...
  LaTeX-Source-Files-27.zip          (VVUQ: verification before generation)
  LaTeX-Source-Files-28.zip          (physical AI: surgical humanoid system)
  LaTeX-Source-Files-29.zip          (physical AI: sensor-stream safety)
  LaTeX-Source-Files-30.zip          (physical AI: embodied control)
```

## Inside each `LaTeX-Source-Files-XX.zip`

```
LaTeX-Source-Files-XX/
  main.tex            top-level document (single column)
  <name>style.sty     style file (fonts, colors, macros)
  references.bib      bibliography (ieeetr)
  README.md           per-template readme (file map + compile steps)
  orcid_icon.png      green ORCID logo (rule 8)
  sections/
    section-a.tex     document section 1 (overview / purpose)
    section-b.tex     document section 2 (holds the one image placeholder)
    section-c.tex     document section 3 (holds the one table template)
    section-d.tex     document section 4
    section-e.tex     document section 5
    section-f.tex     back matter (acknowledgments, rights, citation, data)
```

**One section file per document section.** Each template uses one
`section-x.tex` file per document section (rule 9); add a section by adding
`sections/section-g.tex` and an `\input` line in `main.tex`. Each per-template
`README.md` restates this and maps every letter to its section.

## Table of contents

| # | Zip | Template title | Category | Body style |
|:--|:--|:--|:--|:--|
| 01 | `LaTeX-Source-Files-01.zip` | One-Page Summary of H. R. 9510 | Legislative deliverable | Times, U.S. Code look |
| 02 | `LaTeX-Source-Files-02.zip` | Section-by-Section Analysis of H. R. 9510 | Legislative deliverable | Times, U.S. Code look |
| 03 | `LaTeX-Source-Files-03.zip` | Plain-English Policy Memorandum for H. R. 9510 | Legislative deliverable | Times, U.S. Code look |
| 04 | `LaTeX-Source-Files-04.zip` | Legislative Findings for H. R. 9510 | Legislative deliverable | Times, U.S. Code look |
| 05 | `LaTeX-Source-Files-05.zip` | Ramseyer Comparative Print for H. R. 9510 | Legislative deliverable | Times, U.S. Code look |
| 06 | `LaTeX-Source-Files-06.zip` | Constitutional Authority Statement for H. R. 9510 | Legislative deliverable | Times, U.S. Code look |
| 07 | `LaTeX-Source-Files-07.zip` | PAYGO and Cost Estimate Note for H. R. 9510 | Legislative deliverable | Times, U.S. Code look |
| 08 | `LaTeX-Source-Files-08.zip` | Sponsor and Cosponsor Packet for H. R. 9510 | Legislative deliverable | Times, U.S. Code look |
| 09 | `LaTeX-Source-Files-09.zip` | Stakeholder Engagement Plan for H. R. 9510 | Legislative deliverable | Times, U.S. Code look |
| 10 | `LaTeX-Source-Files-10.zip` | Legislative Counsel Routing Memo for H. R. 9510 | Legislative deliverable | Times, U.S. Code look |
| 11 | `LaTeX-Source-Files-11.zip` | Currency and Cross-Reference Matrix for H. R. 9510 | Legislative deliverable | Times, U.S. Code look |
| 12 | `LaTeX-Source-Files-12.zip` | Testimony and Research-Influence Brief for H. R. 9510 | Legislative deliverable | Times, U.S. Code look |
| 13 | `LaTeX-Source-Files-13.zip` | Robot-Patient Interaction Code Reference | Coding (monospaced) | Courier (mono) |
| 14 | `LaTeX-Source-Files-14.zip` | VVUQ Pipeline Engineering Notebook | Coding (monospaced) | Inconsolata (mono) |
| 15 | `LaTeX-Source-Files-15.zip` | Autonomous Code-Generation Run Log | Coding (monospaced) | Anonymous Pro (mono) |
| 16 | `LaTeX-Source-Files-16.zip` | Humanoid Control Stack API Reference | Coding (monospaced) | Source Code Pro (mono) |
| 17 | `LaTeX-Source-Files-17.zip` | Test and Error-Check Harness Manual | Coding (monospaced) | DejaVu Sans Mono (mono) |
| 18 | `LaTeX-Source-Files-18.zip` | Physical AI Oncology Trial Protocol | Oncology clinical trials | Palatino, deep navy accent |
| 19 | `LaTeX-Source-Files-19.zip` | Patient Journey in a Physical AI Oncology Trial | Oncology clinical trials | XCharter, teal accent |
| 20 | `LaTeX-Source-Files-20.zip` | Adverse Event Response Plan | Oncology clinical trials | Linux Libertine, burgundy accent |
| 21 | `LaTeX-Source-Files-21.zip` | Clinical Trial Site Operations Manual | Oncology clinical trials | Times (mathptmx), forest green accent |
| 22 | `LaTeX-Source-Files-22.zip` | National Physical AI Oncology Trial Platform | Oncology clinical trials | Kp-Fonts, slate accent |
| 23 | `LaTeX-Source-Files-23.zip` | VVUQ Method and Pipeline | VVUQ | Palatino, deep navy accent |
| 24 | `LaTeX-Source-Files-24.zip` | Ten-Gate Threshold Specification | VVUQ | Times (mathptmx), slate accent |
| 25 | `LaTeX-Source-Files-25.zip` | Evidence-to-Law Credibility Assessment | VVUQ | XCharter, teal accent |
| 26 | `LaTeX-Source-Files-26.zip` | Uncertainty Quantification Report | VVUQ | Linux Libertine, burgundy accent |
| 27 | `LaTeX-Source-Files-27.zip` | Verification Before Generation Standard | VVUQ | Utopia (Fourier), forest green accent |
| 28 | `LaTeX-Source-Files-28.zip` | Mobile Surgical Humanoid System Description | Physical AI | Helvetica (sans), slate accent |
| 29 | `LaTeX-Source-Files-29.zip` | Sensor-Stream Safety Bands | Physical AI | Palatino, teal accent |
| 30 | `LaTeX-Source-Files-30.zip` | Embodied Control and Camaraderie Behavior | Physical AI | Times (mathptmx), deep navy accent |

## What every template includes (per the task rules)

1. **Single column only** (rule 1) - every `main.tex` is one-column `article`.
2. **A short paragraph per section** (rule 2).
3. **No images, charts, diagrams, or tables**, except the required two (rule 3):
   - one **image placeholder** in `section-b.tex`, based on the figure code of
     `cancer-automated/papers/VVUQ-02/final-paper`;
   - one **table** in `section-c.tex`, modeled on **Table 1** of
     `cancer-automated/papers/VVUQ-05/final-bill`.
4. **All author and company information** (rule 4): Kevin Kawchak, CEO ChemicalQDevice,
   ORCID `0009-0007-5457-8667`, kevink@chemicalqdevice.com.
5. A properly placed **DOI** [`10.5281/zenodo.xxxxxxxx`](https://doi.org/10.5281/zenodo.xxxxxxxx) on the cover and in the
   citation block (rule 5).
6. A **blank single-line Keywords** section on the first page (rule 6).
7. The **back matter** from `cancer-automated/papers/VVUQ-03/final-paper`
   (acknowledgments, ethical disclosures, rights, cite-this, data availability),
   in `section-f.tex` (rule 7).
8. The **green ORCID logo** (`orcid_icon.png`, from
   `physical-ai-oncology-trials/patient-journey/paper`) on the cover, in place of
   the green `iD` text (rule 8).
9. A **`main.tex`, `.sty`, `.bib`, `README.md`, and `sections/section-x.tex`**
   set, one section file per document section (rule 9).

## The cover-page preview PDF

`LaTeX-Source-Files-Cover-Pages.pdf` has **one page per template (30 pages)**
showing each template's first page, with the `LaTeX-Source-Files-XX` tag at the
bottom of every page, clear of the cover content. (LaTeX is not installed in the
generation sandbox, so these are faithful first-page previews; each zip compiles
to the same first page on Overleaf with pdfLaTeX.)

## Compile any template (Overleaf, pdfLaTeX)

Upload the zip to Overleaf (or run locally with a full TeX Live), then:

```
pdflatex main
bibtex   main
pdflatex main
pdflatex main
```

## INSPIRATIONS (open-source works these templates build on)

1. `kevinkawchak/cancer-automated/.../papers/VVUQ-05/final-bill`
2. `cancer-automated/.../papers/VVUQ-03/final-paper`
3. `cancer-automated/.../papers/VVUQ-02/final-paper`
4. `cancer-automated/.../papers/VVUQ-01/final-paper`
5. `Clinical-AI-Demos/.../demo-projects/07-humanoid/paper/final-paper`
6. `robotic-surgeries/.../2030-pdac-1min/paper/final-paper`
7. `robotic-surgeries/.../2030-gbm-1min/paper/full-paper/final-paper`
8. `physical-ai-oncology-trials/.../patients/paper/full-paper/final-paper`
9. `physical-ai-oncology-trials/.../national-platform/new_paper/final_paper`
10. `physical-ai-oncology-trials/.../new-trial/site/all-documents`
11. `physical-ai-oncology-trials/.../regulatory/Adaption-21-CFR-Part-312/source`
12. `physical-ai-oncology-trials/.../patient-journey/paper`

## License

Released under the Creative Commons Attribution 4.0 International License
(CC BY 4.0). Reproduced public-domain U.S. Government text is used under
17 U.S.C. § 105. Author: Kevin Kawchak, CEO ChemicalQDevice
([ORCID 0009-0007-5457-8667](https://orcid.org/0009-0007-5457-8667)).
