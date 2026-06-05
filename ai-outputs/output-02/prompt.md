## Prompt
#### Claude Code Opus 4.8 (1M Context) Max

Your goal is to provide 30 different LaTeX zip templates to be used for future legislative publications building off of the INSPIRATIONS open source works. You don’t need to know all context from each open source work: simply label titles and headings based on the new template theme, and provide minimal text for each section. All new templates must be based on open source developments. 

Rules:
1. Only single column templates are allowed
2. Only provide a short paragraph of text in each section of the new template
3. No images, charts, diagrams, or tables are needed, but include 1 image placeholder based on the figure code from cancer-automated/tree/main/papers/VVUQ-02/final-paper. Include 1 table template from Table 1 of kevinkawchak/cancer-automated/tree/main/papers/VVUQ-05/final-bill
4. Include all of the author and company information (where appropriate)
5. Include a properly placed DOI 10.5281/zenodo.xxxxxxxx (https://doi.org/10.5281/zenodo.xxxxxxxx) for each template
6. Where relevant, include a blank single line section for Keywords
7. Include the back_matter.tex information from cancer-automated/tree/main/papers/VVUQ-03/final-paper, where relevant, to the template type
8. Include the green orcid logo file in the LaTeX source files and respective cover pages, where relevant to the template, (found in physical-ai-oncology-trials/tree/main/patient-journey/paper), in place of green cover page “iD” text
9. Each of the 30 template sets must have a main.tex, .sty, .bib, and README.md, plus a “sections” folder with “section-x.tex” (x=a, b, c..) file with minimal text. Note in the README, that the template needs to have 1 section file per document section

“Templates by Type”
-12 templates for each of the 12 deliverables in cancer-automated/tree/main/papers/VVUQ-05/final-bill/deliverables
-5 templates that are Coding Based and look mainstream (example: monospaced fonts like courier new, anonymous, etc.)
-5 templates on Oncology Clinical Trials
-5 templates suitable for VVUQ 
-3 templates suitable for Physical AI
“Templates by Type”

“INSPIRATIONS”
1. kevinkawchak/cancer-automated/tree/main/papers/VVUQ-05/final-bill
2. cancer-automated/tree/main/papers/VVUQ-03/final-paper
3. cancer-automated/tree/main/papers/VVUQ-02/final-paper
4. cancer-automated/tree/main/papers/VVUQ-01/final-paper
5. Clinical-AI-Demos/tree/main/demo-projects/07-humanoid/paper/final-paper
6. robotic-surgeries/tree/main/2030-pdac-1min/paper/final-paper
7. robotic-surgeries/tree/main/2030-gbm-1min/paper/full-paper/final-paper
8. physical-ai-oncology-trials/tree/main/patients/paper/full-paper/final-paper
9. physical-ai-oncology-trials/tree/main/national-platform/new_paper/final_paper
10. physical-ai-oncology-trials/tree/main/new-trial/site/all-documents
11. physical-ai-oncology-trials/tree/main/regulatory/Adaption-21-CFR-Part-312/source
12. physical-ai-oncology-trials/tree/main/patient-journey/paper
“INSPIRATIONS”

Output all files as separate “LaTeX-Source-Files-xx” (xx = 01-30) zip files to kevinkawchak/Clinical-AI-Demos/tree/main/ai-outputs/output-02. The descriptive README for this directory needs to include the directory structure, toc, etc. Also include a single pdf that has only the first compiled pages for each of 30 templates (include the “LaTeX-Source-Files-xx” at the bottom of each page, not overlapping any of the cover page contents)

Include a brief note for the Current version as the last entry under “Changed” using your username and today’s date in Clinical-AI-Demos/blob/main/CHANGELOG.md that has under 200 characters without spaces (using the same format as the previous changelog Changed update). Only commit to Clinical-AI-Demos, and no other repository. You have permission to commit directly to main. 
