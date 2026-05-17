# Education and Learning Sciences Article Template

Perspective: **Education and Learning Sciences Perspective**

Designed for learning studies, classroom interventions, assessment research, and theory-driven manuscripts.

## Contents

- `main.tex` — top-level manuscript file; includes every section file.
- `education_learning_sciences_template.sty` — template-specific style file.
- `references.bib` — starter bibliography file.
- `sections/abstract.tex`
- `sections/introduction.tex`
- `sections/methods.tex`
- `sections/results.tex`
- `sections/discussion.tex`
- `sections/limitations_future.tex`
- `sections/conclusions.tex`
- `sections/back_matter.tex`

## Section structure

The template follows a general academic paper structure: Abstract, Introduction, Methods, Results, Discussion, Limitations and Future Work, Conclusions, References, and Back Matter. Back Matter includes Acknowledgments, Ethical Disclosures, Rights and Permissions, Cite This Article, and a general Data Availability section.

## Required first-page keyword line

The first page includes a blank single-line `Keywords:` field. Replace the rule with manuscript-specific keywords before submission.

## Tables

Each section contains a compact three-row table using the same eight-column width pattern copied into the style macro from the requested exemplar Table 2 layout:

```tex
p{2cm} p{0.9cm} p{0.9cm} p{1.9cm} p{1.9cm} p{1.9cm} p{2cm} p{1.6cm}
```

## Compile

```bash
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```

The template is intentionally single-column and does not use line numbers, draft watermarks, editorial annotations, or pre-print editing formatting.

## License note

This is an original reusable template prepared for CC BY 4.0-compatible use. Confirm the license requirements of the target journal before submission.
