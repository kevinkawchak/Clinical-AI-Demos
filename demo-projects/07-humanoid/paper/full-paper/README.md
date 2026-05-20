# Full Paper: Triple Humanoid 24/7 Adverse Event Oncology Trial Response Team

[![Repo](https://img.shields.io/badge/Repo-Clinical--AI--Demos-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)
[![Companion](https://img.shields.io/badge/Companion-physical--ai--oncology--trials-purple.svg)](https://github.com/kevinkawchak/physical-ai-oncology-trials)
[![Release](https://img.shields.io/badge/Release-v0.7.0-brightgreen.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)
[![DOI Placeholder](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.20303281-blue)](https://doi.org/10.5281/zenodo.20303281)
[![Prior DOI](https://img.shields.io/badge/Prior%20DOI-10.5281%2Fzenodo.18029100-blue)](https://doi.org/10.5281/zenodo.18029100)
[![Instructions DOI](https://img.shields.io/badge/Instructions%20DOI-10.5281%2Fzenodo.18445179-blue)](https://doi.org/10.5281/zenodo.18445179)
[![Draft DOI](https://img.shields.io/badge/Draft%20DOI-10.5281%2Fzenodo.18445179-blue)](https://github.com/kevinkawchak/Clinical-AI-Demos/tree/main/demo-projects/07-humanoid/paper/draft-paper)
[![License](https://img.shields.io/badge/License-CC%20BY%204.0-green.svg)](https://creativecommons.org/licenses/by/4.0/)
[![LaTeX](https://img.shields.io/badge/LaTeX-Overleaf%20Ready-orange.svg)](https://www.overleaf.com)
[![Paper Status](https://img.shields.io/badge/Status-Full%20Paper-brightgreen.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)
[![References](https://img.shields.io/badge/References-28%20entries-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)

This directory holds the full LaTeX paper **Triple Humanoid 24/7 Adverse Event Oncology Trial Response Team: 4-Site Rotation**, expanded from the v0.6.0 bracketed draft scaffold at `paper/draft-paper/` into the finished v0.7.0 manuscript.

## Thesis

On-premises repository based LLMs provide commands to humanoid robots based on real-time sensor data and controlled via x, y, z coordinates to administer synergistic treatment regarding patient adverse events. This workflow minimizes single robot error potential.

## Title Page Metadata

| Field | Value |
|-------|-------|
| Title | Triple Humanoid 24/7 Adverse Event Oncology Trial Response Team: 4-Site Rotation |
| Author | Kevin Kawchak, CEO ChemicalQDevice |
| ORCID | 0009-0007-5457-8667 |
| DOI placeholder | 10.5281/zenodo.20303281 |
| Date | May 20, 2026 |
| License | CC BY 4.0 |
| Version | v0.7.0 |

## File Inventory

```
full-paper/
  main.tex                                  Top level manuscript file.
  humanoid_paper_template.sty               Style file with palette,
  section heading rules, the
  8 column section table macro,
  a 2 column narrative table
  macro, and a 3 column metrics
  table macro.
  references.bib                            28 references with clickable
  DOIs plus URLs.
  README.md                                 This file.
  sections/
    abstract.tex                            ~300 word abstract with no
  citations.
    introduction.tex                        5 subsection introduction.
    methods.tex                             9 subsection methods.
    results.tex                             7 subsection results.
    discussion.tex                          6 subsection discussion.
    limitations_future.tex                  5 subsection limitations
  and future work.
    conclusions.tex                         4 subsection conclusions.
    back_matter.tex                         Acknowledgments, Ethical
  Disclosures, Rights and
  Permissions, Cite This
  Article, Data Availability.
  LaTeX-Source.zip                          Convenience bundle for
  Overleaf upload. Same files
  as above.
```

## Headline Metrics Table

| Metric | Value | Anchor file in repository |
|--------|-------|---------------------------|
| Sites | 4 (SF-01, SD-01, BO-01, AT-01) | `paper/instructions/README.md` |
| Robots per site | 3 Unitree H2 EDU | `paper/codegen/config/h2_humanoid.yaml` |
| Robots total | 12 | `paper/codegen/src/h2_dispatcher.py` |
| LLM cadence | 1 Hz broadcast | `paper/codegen/src/llm_planner.py` |
| Motion cadence | 10 Hz per robot | `paper/codegen/src/robot_loop.cpp` |
| Monitoring window | 168 hours | `paper/codegen/src/week_runner.py` |
| AE volume | about 84 in the week | `paper/codegen/data/iterations/index.jsonl` |
| SAE volume | about 24 (CTCAE grade 3+) | `paper/codegen/data/iterations/index.jsonl` |
| Iterations | 32 deterministic sweeps | `paper/codegen/data/iterations/index.jsonl` |
| E-stop latency | 5 ms swarm wide | `paper/codegen/src/robot_loop.cpp` |
| Camaraderie reduction | factor of 3 | `paper/codegen/src/swarm_coordinator.py` |

## RESEARCH Inputs Drawn On By The Full Paper

The full paper section files cite specific files in these read-only RESEARCH trees. The trees are not modified by this paper.

- `demo-projects/07-humanoid/paper/instructions/` 11 subdirectories.
- `demo-projects/07-humanoid/paper/codegen/` 27 source files, schemas, configs, ASCII diagrams, reports, and figures.
- `demo-projects/07-humanoid/paper/execution/` per-step logs, ASCII diagrams, figures, output tables, reports, and per-site decision streams.
- `demo-projects/07-humanoid/paper/inputs/` Deep-Research-A (Medical Full Automation A) and Deep-Research-B (Medical Rapid Prototyping B) source bundles.
- Prior FDA AERS LLM paper at `kawchak_2025_18029100` (DOI `10.5281/zenodo.18029100`).

## High Level ASCII Diagram

```
              Full Paper Pipeline (v0.7.0)
              ============================

   instructions/          codegen/          execution/         inputs/
   (project plan,         (27 src files,    (4 site runtime    (prior paper,
    11 subdirectories,     diagrams,         JSONL, DuckDB,     Deep-Research A
    swarm pattern,         reports,          ASCII diagrams,    and B chunks)
    camaraderie,           dashboard.html,   reports, figures,
    inventory,             iterations index, logs, outputs)
    LLM planner plan)      tests)
        |                    |                  |                |
        +-----+--------------+---------+--------+-------+--------+
              |                        |                |
              v                        v                v
        +----------------------------------------------------------+
        | main.tex (full paper)                                     |
        |   + humanoid_paper_template.sty                           |
        |   + references.bib (28 entries)                           |
        |   + sections/abstract,intro,methods,results,discussion,   |
        |              limitations_future,conclusions,back_matter   |
        |                                                           |
        | Each section now carries finished prose, sectiontable     |
        | matrices, narrativetable rows, ASCII figures, and         |
        | citations resolved against references.bib.                |
        +----------------------------------------------------------+
                                  |
                                  v
                  +----------------------------------+
                  | Full Paper PDF                   |
                  | Compiled in Overleaf from the    |
                  | LaTeX-Source.zip in this folder. |
                  +----------------------------------+
```

## Continental Network ASCII Diagram

```
                  PAT-NET-001 4-Site Continental Adverse Event Network
                  =====================================================

  +-----------------+    +-----------------+    +-----------------+    +-----------------+
  | San Francisco   |    | San Diego       |    | Boston          |    | Atlanta         |
  | Site SF-01      |    | Site SD-01      |    | Site BO-01      |    | Site AT-01      |
  |                 |    |                 |    |                 |    |                 |
  | Claude Opus 4.7 |    | Claude Opus 4.7 |    | Claude Opus 4.7 |    | Claude Opus 4.7 |
  | 1M on-prem      |    | 1M on-prem      |    | 1M on-prem      |    | 1M on-prem      |
  | broadcaster     |    | broadcaster     |    | broadcaster     |    | broadcaster     |
  |   |   |   |     |    |   |   |   |     |    |   |   |   |     |    |   |   |   |     |
  |   v   v   v     |    |   v   v   v     |    |   v   v   v     |    |   v   v   v     |
  | H2-A H2-B H2-C  |    | H2-D H2-E H2-F  |    | H2-G H2-H H2-I  |    | H2-J H2-K H2-L  |
  | swarm camarades |    | swarm camarades |    | swarm camarades |    | swarm camarades |
  +--------+--------+    +--------+--------+    +--------+--------+    +--------+--------+
           |                      |                      |                      |
           +----------------------+----------+-----------+----------------------+
                                             |
                                             v
                          +-------------------------------------+
                          | Cross Site De-Identified Summary Bus|
                          | (hourly summaries only, no PHI,     |
                          | no robot transit between sites)     |
                          +-------------------------------------+
```

## Compile in Overleaf

1. Download `LaTeX-Source.zip` from this directory.
2. In Overleaf, click New Project then Upload Project, and pick the zip.
3. Set the compiler to pdfLaTeX and the main document to `main.tex`.
4. Run pdfLaTeX, BibTeX, pdfLaTeX, pdfLaTeX to resolve citations.

The compile yields a finished PDF with the title block, the disclaimer, the abstract, the keyword line, the introduction with the continental network and 4-site execution ASCII figures, the table of contents, the methods, results, discussion, limitations and future work, conclusions, and back matter sections, plus a clickable bibliography with all 28 entries.

## Notes on Style and Formatting

- Single dashes only. No em dashes. No double dashes. No triple dashes.
- Black body text everywhere. The accent and link color is the deep slate blue defined in `humanoid_paper_template.sty`. Orcid icons are green.
- The shared `\sectiontable{caption}{rows}` macro renders the 8 cell planning matrix that closes each section. Each row carries Item, Ref, Step, Input, Action, Output, Check, and Status. Every column uses `>{\raggedright\arraybackslash}p{...cm}` so cell content is left aligned and word spacing stays tight.
- A 2 column `\narrativetable{caption}{header1}{header2}` macro and a 3 column `\metricstable{caption}` macro carry reader-friendly content like roles, headline numbers, file inventories, and regulatory anchors.
- Body text uses `\RaggedRight` from ragged2e plus `\emergencystretch=3em` plus `\tolerance=2500`. This combination keeps word spacing inside a line tight and even so the text does not stretch into rivers of white space, and at the same time prevents text from running off the right margin.
- Widow and orphan penalties are at 10000. The `\raggedbottom` directive lets pages end short rather than stretch. The combination prevents single 1 or 2 word lines from being stranded on their own page.
- Replace any stray `SS` artifact with the section sign `\S`.
- Replace `10.5281/zenodo.20303281` everywhere with the real Zenodo DOI once the paper is deposited.

## Reference Format Notes

Every reference in `references.bib` carries:

- `doi` field with the bare DOI string when one exists.
- `url` field with the full `https://doi.org/` resolver URL when a DOI exists, otherwise the canonical landing page URL.
- `howpublished` field wrapping the URL in `\url{...}` so the ieeetr style prints a clickable hyperlink in the rendered bibliography.

Repository entries (`kawchak_2026_clinical_ai_demos_repo`, `kawchak_2026_physical_ai_oncology_trials_repo`) also carry the GitHub URL and the Zenodo URL inside the `note` field so the bibliography page prints both as clickable hyperlinks.

## License

CC BY 4.0. See `LICENSE` at the repository root and the Rights and Permissions block inside `sections/back_matter.tex`.

## Citation

```bibtex
@misc{kawchak_2026_humanoid_4site_full_paper,
  author       = {Kawchak, Kevin},
  title        = {Triple Humanoid 24/7 Adverse Event Oncology Trial Response Team: 4-Site Rotation},
  month        = may,
  year         = {2026},
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.20303281},
  url          = {https://doi.org/10.5281/zenodo.20303281}
}
```
