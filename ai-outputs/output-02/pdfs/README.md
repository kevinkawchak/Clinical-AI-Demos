# Compiled PDFs - output-02 templates (pdf-01 to pdf-30)

[![PDFs](https://img.shields.io/badge/PDFs-30-blue.svg)](.)
[![Engine](https://img.shields.io/badge/Engine-pdfLaTeX%20(TeX%20Live%202023)-green.svg)](.)
[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.xxxxxxxx-blue.svg)](https://doi.org/10.5281/zenodo.xxxxxxxx)

Compiled PDFs of the 30 single-column LaTeX templates in [`..`](..) (`LaTeX-Source-Files-01.zip` ... `LaTeX-Source-Files-30.zip`). Each PDF was produced from its zip with the four-pass recipe `pdflatex -> bibtex -> pdflatex -> pdflatex` on TeX Live 2023. `pdf-NN.pdf` is the compile of `LaTeX-Source-Files-NN.zip`.

## Index

| PDF | Source template | Title | Category |
|:--|:--|:--|:--|
| `pdf-01.pdf` | `LaTeX-Source-Files-01.zip` | One-Page Summary of H. R. 9510 | Legislative deliverable |
| `pdf-02.pdf` | `LaTeX-Source-Files-02.zip` | Section-by-Section Analysis of H. R. 9510 | Legislative deliverable |
| `pdf-03.pdf` | `LaTeX-Source-Files-03.zip` | Plain-English Policy Memorandum for H. R. 9510 | Legislative deliverable |
| `pdf-04.pdf` | `LaTeX-Source-Files-04.zip` | Legislative Findings for H. R. 9510 | Legislative deliverable |
| `pdf-05.pdf` | `LaTeX-Source-Files-05.zip` | Ramseyer Comparative Print for H. R. 9510 | Legislative deliverable |
| `pdf-06.pdf` | `LaTeX-Source-Files-06.zip` | Constitutional Authority Statement for H. R. 9510 | Legislative deliverable |
| `pdf-07.pdf` | `LaTeX-Source-Files-07.zip` | PAYGO and Cost Estimate Note for H. R. 9510 | Legislative deliverable |
| `pdf-08.pdf` | `LaTeX-Source-Files-08.zip` | Sponsor and Cosponsor Packet for H. R. 9510 | Legislative deliverable |
| `pdf-09.pdf` | `LaTeX-Source-Files-09.zip` | Stakeholder Engagement Plan for H. R. 9510 | Legislative deliverable |
| `pdf-10.pdf` | `LaTeX-Source-Files-10.zip` | Legislative Counsel Routing Memo for H. R. 9510 | Legislative deliverable |
| `pdf-11.pdf` | `LaTeX-Source-Files-11.zip` | Currency and Cross-Reference Matrix for H. R. 9510 | Legislative deliverable |
| `pdf-12.pdf` | `LaTeX-Source-Files-12.zip` | Testimony and Research-Influence Brief for H. R. 9510 | Legislative deliverable |
| `pdf-13.pdf` | `LaTeX-Source-Files-13.zip` | Robot-Patient Interaction Code Reference | Coding (monospaced) |
| `pdf-14.pdf` | `LaTeX-Source-Files-14.zip` | VVUQ Pipeline Engineering Notebook | Coding (monospaced) |
| `pdf-15.pdf` | `LaTeX-Source-Files-15.zip` | Autonomous Code-Generation Run Log | Coding (monospaced) |
| `pdf-16.pdf` | `LaTeX-Source-Files-16.zip` | Humanoid Control Stack API Reference | Coding (monospaced) |
| `pdf-17.pdf` | `LaTeX-Source-Files-17.zip` | Test and Error-Check Harness Manual | Coding (monospaced) |
| `pdf-18.pdf` | `LaTeX-Source-Files-18.zip` | Physical AI Oncology Trial Protocol | Oncology clinical trial |
| `pdf-19.pdf` | `LaTeX-Source-Files-19.zip` | Patient Journey in a Physical AI Oncology Trial | Oncology clinical trial |
| `pdf-20.pdf` | `LaTeX-Source-Files-20.zip` | Adverse Event Response Plan | Oncology clinical trial |
| `pdf-21.pdf` | `LaTeX-Source-Files-21.zip` | Clinical Trial Site Operations Manual | Oncology clinical trial |
| `pdf-22.pdf` | `LaTeX-Source-Files-22.zip` | National Physical AI Oncology Trial Platform | Oncology clinical trial |
| `pdf-23.pdf` | `LaTeX-Source-Files-23.zip` | VVUQ Method and Pipeline | VVUQ |
| `pdf-24.pdf` | `LaTeX-Source-Files-24.zip` | Ten-Gate Threshold Specification | VVUQ |
| `pdf-25.pdf` | `LaTeX-Source-Files-25.zip` | Evidence-to-Law Credibility Assessment | VVUQ |
| `pdf-26.pdf` | `LaTeX-Source-Files-26.zip` | Uncertainty Quantification Report | VVUQ |
| `pdf-27.pdf` | `LaTeX-Source-Files-27.zip` | Verification Before Generation Standard | VVUQ |
| `pdf-28.pdf` | `LaTeX-Source-Files-28.zip` | Mobile Surgical Humanoid System Description | Physical AI |
| `pdf-29.pdf` | `LaTeX-Source-Files-29.zip` | Sensor-Stream Safety Bands | Physical AI |
| `pdf-30.pdf` | `LaTeX-Source-Files-30.zip` | Embodied Control and Camaraderie Behavior | Physical AI |

## Reproduce

```
unzip LaTeX-Source-Files-NN.zip && cd LaTeX-Source-Files-NN
pdflatex main && bibtex main && pdflatex main && pdflatex main
# main.pdf is published here as pdf-NN.pdf
```

## License

CC BY 4.0. Author: Kevin Kawchak, CEO ChemicalQDevice
([ORCID 0009-0007-5457-8667](https://orcid.org/0009-0007-5457-8667)). DOI placeholder [`10.5281/zenodo.xxxxxxxx`](https://doi.org/10.5281/zenodo.xxxxxxxx).
