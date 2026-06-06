# Compiled PDFs - output-03 templates (pdf-01 to pdf-30)

[![PDFs](https://img.shields.io/badge/PDFs-30-blue.svg)](.)
[![Engine](https://img.shields.io/badge/Engine-pdfLaTeX%20(TeX%20Live%202023)-green.svg)](.)
[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.xxxxxxxx-blue.svg)](https://doi.org/10.5281/zenodo.xxxxxxxx)

Compiled PDFs of the 30 genre-diverse single-column LaTeX templates in [`..`](..) (`LaTeX-Source-Files-01.zip` ... `LaTeX-Source-Files-30.zip`). Each PDF was produced with `pdflatex -> bibtex -> pdflatex -> pdflatex` on TeX Live 2023. `pdf-01.pdf` is the compile of this set's `LaTeX-Source-Files-01.zip`, through `pdf-30.pdf` for `LaTeX-Source-Files-30.zip`.

## Index

| PDF | Source template | Title | Genre / perspective |
|:--|:--|:--|:--|
| `pdf-01.pdf` | `LaTeX-Source-Files-01.zip` | One-Page Summary of H. R. 9510 | Executive one-pager (labeled blocks) |
| `pdf-02.pdf` | `LaTeX-Source-Files-02.zip` | Section-by-Section Analysis of H. R. 9510 | Per-section annotation/gloss |
| `pdf-03.pdf` | `LaTeX-Source-Files-03.zip` | Verify Robot Code Before It Touches a Patient | Policy memorandum (TO/FROM/RE; Q&A) |
| `pdf-04.pdf` | `LaTeX-Source-Files-04.zip` | Legislative Findings of Fact for H. R. 9510 | Findings of fact (numbered) + authorities |
| `pdf-05.pdf` | `LaTeX-Source-Files-05.zip` | Ramseyer Comparative Print for H. R. 9510 | Ramseyer redline (strike/insert) |
| `pdf-06.pdf` | `LaTeX-Source-Files-06.zip` | Constitutional Authority Statement for H. R. 9510 | Formal authority statement (boxed operative sentence) |
| `pdf-07.pdf` | `LaTeX-Source-Files-07.zip` | PAYGO and Cost Estimate Note for H. R. 9510 | Fiscal note (budget table + earmark declaration) |
| `pdf-08.pdf` | `LaTeX-Source-Files-08.zip` | Sponsor and Original Cosponsor Packet for H. R. 9510 | Recruitment packet (checklist + signature lines) |
| `pdf-09.pdf` | `LaTeX-Source-Files-09.zip` | Stakeholder Engagement Plan for H. R. 9510 | Engagement plan (register + phases) |
| `pdf-10.pdf` | `LaTeX-Source-Files-10.zip` | Legislative Counsel Routing Memo for H. R. 9510 | Routing memo (amendatory table + numbered questions) |
| `pdf-11.pdf` | `LaTeX-Source-Files-11.zip` | Currency and Cross-Reference Matrix for H. R. 9510 | Audit matrix (verification table + checklist + sign-off) |
| `pdf-12.pdf` | `LaTeX-Source-Files-12.zip` | Testimony and Research-Influence Brief for H. R. 9510 | Hearing testimony (opening statement + Q&A + influences) |
| `pdf-13.pdf` | `LaTeX-Source-Files-13.zip` | Robot-Patient Interaction Code: API Reference | API reference (signature blocks) |
| `pdf-14.pdf` | `LaTeX-Source-Files-14.zip` | VVUQ Pipeline Engineering Notebook | Engineering notebook (dated entries) |
| `pdf-15.pdf` | `LaTeX-Source-Files-15.zip` | Autonomous Code-Generation Run Log | Console transcript (run log) |
| `pdf-16.pdf` | `LaTeX-Source-Files-16.zip` | Humanoid Control Stack: Repository README | Repository README (badges + code fences + tree) |
| `pdf-17.pdf` | `LaTeX-Source-Files-17.zip` | Test and Error-Check Harness: Test Plan | Test plan (numbered test cases + traceability) |
| `pdf-18.pdf` | `LaTeX-Source-Files-18.zip` | Physical AI Oncology Trial Protocol | Clinical trial protocol (synopsis header) |
| `pdf-19.pdf` | `LaTeX-Source-Files-19.zip` | Patient Journey in a Physical AI Oncology Trial | Patient-journey map (persona + stages) |
| `pdf-20.pdf` | `LaTeX-Source-Files-20.zip` | Adverse Event Response Standard Operating Procedure | SOP (roles + numbered steps) |
| `pdf-21.pdf` | `LaTeX-Source-Files-21.zip` | Clinical Trial Site Operations Manual | Operations manual (revision block + checklists) |
| `pdf-22.pdf` | `LaTeX-Source-Files-22.zip` | National Physical AI Oncology Trial Platform | Program white paper (mission + roadmap) |
| `pdf-23.pdf` | `LaTeX-Source-Files-23.zip` | VVUQ Method and Pipeline: A Research Paper | Classic IMRAD research paper |
| `pdf-24.pdf` | `LaTeX-Source-Files-24.zip` | Ten-Gate Threshold Specification | Requirements specification (REQ ids) |
| `pdf-25.pdf` | `LaTeX-Source-Files-25.zip` | Evidence-to-Law Credibility Assessment | ASME V&V 40-style credibility assessment |
| `pdf-26.pdf` | `LaTeX-Source-Files-26.zip` | Uncertainty Quantification Report | Technical report (executive summary) |
| `pdf-27.pdf` | `LaTeX-Source-Files-27.zip` | Verification Before Generation Standard | Standards-body document (numbered clauses) |
| `pdf-28.pdf` | `LaTeX-Source-Files-28.zip` | Mobile Surgical Humanoid: System Datasheet | Technical datasheet (specifications) |
| `pdf-29.pdf` | `LaTeX-Source-Files-29.zip` | Sensor-Stream Safety Bands: An Assurance Case | Safety case (claim-argument-evidence) |
| `pdf-30.pdf` | `LaTeX-Source-Files-30.zip` | Embodied Control and Camaraderie Behavior: A Design Note | Design note / RFC (states + coordination) |

## Reproduce

```
unzip LaTeX-Source-Files-NN.zip && cd LaTeX-Source-Files-NN
pdflatex main && bibtex main && pdflatex main && pdflatex main
# main.pdf is published here as pdf-NN.pdf
```

## License

CC BY 4.0. Author: Kevin Kawchak, CEO ChemicalQDevice
([ORCID 0009-0007-5457-8667](https://orcid.org/0009-0007-5457-8667)). DOI placeholder [`10.5281/zenodo.xxxxxxxx`](https://doi.org/10.5281/zenodo.xxxxxxxx).
