# Draft Paper: Triple Humanoid 24/7 Adverse Event Oncology Trial Response Team

[![Repo](https://img.shields.io/badge/Repo-Clinical--AI--Demos-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)
[![Companion](https://img.shields.io/badge/Companion-physical--ai--oncology--trials-purple.svg)](https://github.com/kevinkawchak/physical-ai-oncology-trials)
[![DOI Placeholder](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.xxxxxxxx-blue)](https://doi.org/10.5281/zenodo.xxxxxxxx)
[![Prior DOI](https://img.shields.io/badge/Prior%20DOI-10.5281%2Fzenodo.18029100-blue)](https://doi.org/10.5281/zenodo.18029100)
[![Instructions DOI](https://img.shields.io/badge/Instructions%20DOI-10.5281%2Fzenodo.18445179-blue)](https://doi.org/10.5281/zenodo.18445179)
[![License](https://img.shields.io/badge/License-CC%20BY%204.0-green.svg)](https://creativecommons.org/licenses/by/4.0/)
[![LaTeX](https://img.shields.io/badge/LaTeX-Overleaf%20Ready-orange.svg)](https://www.overleaf.com)
[![Paper Status](https://img.shields.io/badge/Status-Draft%20Scaffold-yellow.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)

This directory holds the LaTeX draft scaffold for the paper
**Triple Humanoid 24/7 Adverse Event Oncology Trial Response Team: 4-Site Rotation**.

The scaffold is not yet a finished paper. Every section file contains
bracketed processing instructions. A future Claude Code Opus 4.7 1M Max
session will read those bracketed instructions, then read the exact
repository directories and files named inside the brackets, then expand
the scaffold into a 70 plus page final paper. The future session must
not modify any file under `paper/codegen/`, `paper/execution/`,
`paper/instructions/`, or `paper/inputs/`; those four trees are
read only RESEARCH inputs.

## Thesis

On-premises repository based LLMs provide commands to humanoid robots
based on real-time sensor data and controlled via x, y, z coordinates
to administer synergistic treatment to patient adverse events. This
workflow minimizes single robot error potential.

## Title Page Metadata

- Title: Triple Humanoid 24/7 Adverse Event Oncology Trial Response Team: 4-Site Rotation
- Author: Kevin Kawchak, CEO ChemicalQDevice, Orcid 0009-0007-5457-8667
- DOI placeholder: 10.5281/zenodo.xxxxxxxx
- Date: May 20, 2026
- License: CC BY 4.0

## Contents

```
draft-paper/
  main.tex                                  Top level manuscript file.
  humanoid_paper_template.sty               Style file, color palette,                section heading rules, and
  the shared 8 column section
  planning table macro.
  references.bib                            Bibliography with clickable
  DOIs and URLs.
  README.md                                 This file.
  sections/
    abstract.tex                            Abstract scaffold and
  bracketed instructions.
    introduction.tex                        Introduction scaffold and
  bracketed instructions.
    methods.tex                             Methods scaffold and
  bracketed instructions.
    results.tex                             Results scaffold and
  bracketed instructions.
    discussion.tex                          Discussion scaffold and
  bracketed instructions.
    limitations_future.tex                  Limitations and Future Work
  scaffold and bracketed
  instructions.
    conclusions.tex                         Conclusions scaffold and
  bracketed instructions.
    back_matter.tex                         Acknowledgments, Ethical
  Disclosures, Rights and
  Permissions, Cite This
  Article, Data Availability.
  LaTeX-Source.zip                          Convenience bundle for
  uploading to Overleaf. Same
  files as above. Created in
  the last error pass commit.
```

## RESEARCH Inputs Pointed To By The Scaffold

The bracketed instructions inside each section file reference these
directory trees and files. Future Claude Code Opus 4.7 1M Max processing
must read them in place and must not modify them.

- `demo-projects/07-humanoid/paper/instructions/` whole tree, with
  emphasis on `README.md` (high level thesis and inventory), and the
  10 numbered subdirectories `00-project-overview/` through
  `09-runtime-instructions/`. Note that `10-repository-update-instructions/`
  is referenced in the README repo-structure block but is not yet
  present on disk.
- `demo-projects/07-humanoid/paper/codegen/` whole tree, including
  `README.md`, `architecture.md`, `Cargo.toml`, `pyproject.toml`,
  `docker-compose.yml`, the 27 files in `src/`, the 9 files in
  `schemas/`, the 6 files in `config/`, the 6 files in `data/`
  (including `data/iterations/index.jsonl`), the 3 ASCII diagrams in
  `diagrams/`, the 4 files in `reports/` (including `dashboard.html`),
  and the test files in `tests/`.
- `demo-projects/07-humanoid/paper/execution/` whole tree, including
  `README.md`, the 4 ASCII diagrams in `diagrams/`, the 6 figures in
  `figures/`, the 23 numbered log files in `logs/`, the 4 markdown
  outputs in `outputs/`, the 5 reports in `reports/`, and the data
  files in `data/` (notably `iterations_aggregate.duckdb`, the two
  `iterations_index_*.jsonl` files, and the 4 site files in
  `data/site_runtime_runs/`).
- `demo-projects/07-humanoid/paper/inputs/` whole tree. This is the
  prior author paper's context. Includes `main.tex`, `new_paper.sty`,
  `references.bib`, the `sections/` LaTeX files, the `Deep-Research-A/`
  Medical Full Automation A sources, and the `Deep-Research-B/`
  Medical Rapid Prototyping B sources.
- Relevant files previously identified in `paper/instructions/` from
  `kevinkawchak/physical-ai-oncology-trials`, including the trial
  hours 00 through 55 under `new-trial/national-24-7-trial/`. Note
  that hours 56 through 83 are explicitly excluded by the instructions
  README.
- Author's December 2025 paper on LLM code generation against the
  FDA Adverse Event Reporting System, used to establish that LLMs are
  effective for FDA adverse events data: `kawchak_2025_18029100` at
  `https://doi.org/10.5281/zenodo.18029100`.

## High Level ASCII Diagram

```
              Draft Paper Scaffold Filling Pipeline
              =====================================

   instructions/         codegen/            execution/         inputs/
   (project plan,        (27 src files,      (4 site runtime    (prior paper,
    config plan,          ASCII diagrams,     JSONL, DuckDB,     Deep-Research A
    schemas plan,         reports,            ASCII diagrams,    and B chunks)
    swarm plan,           dashboard.html,     reports, figures,
    iteration plan,       iterations index,   logs, outputs)
    LLM planner plan)     test_xyz_safety)
        |                     |                   |                 |
        +-------+-------------+----------+--------+--------+--------+
                |                        |                 |
                v                        v                 v
        +----------------------------------------------------------+
        | main.tex                                                  |
        |   + humanoid_paper_template.sty                           |
        |   + references.bib                                        |
        |   + sections/abstract,intro,methods,results,discussion,   |
        |              limitations_future,conclusions,back_matter   |
        |                                                           |
        | each .tex file holds bracketed instructions that name the |
        | exact RESEARCH paths a future Claude Code session reads   |
        | when expanding the scaffold into the 70 plus page paper.  |
        +----------------------------------------------------------+
                                  |
                                  v
                  +----------------------------------+
                  | 70 plus page final paper PDF     |
                  | compiled in Overleaf from the    |
                  | LaTeX-Source.zip in this folder. |
                  +----------------------------------+
```

## Compile in Overleaf

1. Download `LaTeX-Source.zip` from this directory.
2. In Overleaf, click New Project then Upload Project, and pick the zip.
3. Set the compiler to pdfLaTeX and the main document to `main.tex`.
4. Run pdfLaTeX, BibTeX, pdfLaTeX, pdfLaTeX to resolve citations.

## Notes on Style And Formatting

- Single dashes only. No em dashes. No double dashes. No triple dashes.
- Black body text. The accent and link color is the deep slate blue
  defined in `humanoid_paper_template.sty`. Orcid icons are green.
- Every section planning table uses the macro `\sectiontable{caption}{rows}`
  defined in `humanoid_paper_template.sty`. Each row has 8 cells matching
  Item, Ref, Step, Input, Action, Output, Check, Status.
- Every fixed-width table column uses `>{\raggedright\arraybackslash}p{...cm}`
  so word spacing inside cells stays tight.
- Body text uses `\RaggedRight` from the ragged2e package. Combined with
  `\emergencystretch=3em` this prevents text from running off the right
  edge while avoiding visible rivers of white space between words.
- Widow and orphan suppression knobs are set in the `.sty` file. Future
  sessions should still scan the rendered PDF and shrink or grow a
  paragraph by a line as needed to avoid a single line stranded on a
  page by itself.
- Replace any stray `SS` artifact with the section sign `\S`.
- Replace `10.5281/zenodo.xxxxxxxx` everywhere with the real Zenodo DOI
  once the paper is deposited.

## License

CC BY 4.0. See `LICENSE` at the repository root and the Rights and
Permissions block inside `sections/back_matter.tex`.

## Citation

```bibtex
@misc{kawchak_2026_humanoid_4site_paper,
  author       = {Kawchak, Kevin},
  title        = {Triple Humanoid 24/7 Adverse Event Oncology Trial Response Team: 4-Site Rotation},
  month        = may,
  year         = {2026},
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.xxxxxxxx},
  url          = {https://doi.org/10.5281/zenodo.xxxxxxxx}
}
```
