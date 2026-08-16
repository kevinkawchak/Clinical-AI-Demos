## output-pdac

I explored the repository, read the source material, and built the deck. Here is what I found and what I produced.

### What the sources actually contained

Three inputs drive the deck, and two of them have a gap worth stating before anything else.

`pdac-presentation/cover-images/ChemicalQDevice-PDAC-Covers-13Aug26.docx` carries **nineteen** embedded cover pages, not twenty. A `.docx` is a ZIP archive, and its media folder is not stored in document order: the first cover in the body is `image4.jpg` and the tenth is `image1.jpg`, so the mapping from image to paper is only recoverable by parsing `word/document.xml` for the `r:embed` sequence and resolving each identifier through `word/_rels/document.xml.rels`. Doing that gives nineteen covers in exact chronological order, matching papers 1 through 19 of your list. The paper with no cover is number 20, *From Independent Scientist to Novel Performer* (10.5281/zenodo.21887807), deposited August 11 and therefore two days older than the cover document that omits it.

`pdac-presentation/abstracts/README.md` carries fifty-five deposited abstracts, and nineteen of your twenty papers are among them. The one absent is number 19, *10 Funding Applications* (10.5281/zenodo.21787424).

`pdac-presentation/theme/update-final-LaTeX.zip` is a complete Overleaf project: eleven sections, twenty-five figures, twenty-five tables, 143 bibliography entries, 53 pages under pdfLaTeX. Its abstract, Section 6 on funding proposals, Section 7 on AI peer review, and Section 9 conclusions are where the LLM Trust and LLM Benefit lines come from.

### How I handled the two gaps

I did not want twenty slides where one carries no cover, and I did not want a slide built on invention. Both gaps are closed from material that is already on the record, and both are documented on the artifact itself rather than only in a README.

**The missing cover.** `build/render_cover_20.py` redraws that paper's front page from the paper's own deposited record: its title and subtitle, the author block, the DOI and ORCID iD, the deposit city and date, its three-paragraph abstract verbatim from `abstracts/README.md`, the $306,000 / $1,300,000 / $5,900,000 ledger from that abstract and Table 18 of the theme bundle, and the four work packages from Figure 18 of Section 6. It is drawn in the visual idiom of the August 2026 covers that the document does carry: white ground, navy rules, serif title over serif abstract. A footer line on the page reads, in full: *"Cover page reconstructed August 14, 2026 for the ChemicalQDevice PDAC seminar deck from the deposited front matter and abstract of record of 10.5281/zenodo.21887807. It is not the deposited PDF cover."* Nothing on it is invented.

**The missing abstract.** Slide 20 (paper 19) is built from that paper's own cover page, which carries its full table of contents, its twenty-figure count and its ten-recipient roster, and from Section 6 and Table 17 of the theme bundle, which list all ten mechanisms with the mechanism class, term requested and ask carried on each. That is where NIH Pioneer, ARPA-H, NSF TIP X-Labs, DOE Genesis, NIH SEED SBIR, FNIH AMP, HHMI, NCI CTEP, Convergent Research FRO and UC San Diego Moores come from. No quantity on that slide is estimated. Adding the deposited abstract to the corpus would let the slide be built from one source and is the right fix if it becomes available.

### The deck

23 slides, 16:9 landscape at 13.333 in by 7.5 in, shipped as `.pptx` and `.pdf`:

| Slides | Contents |
|--:|:--|
| 1 | Title, subtitle, four statistic tiles, author, contact, venue, date, disclaimer |
| 2 to 21 | The twenty papers, chronological, one cover image and one seven-line evaluation each |
| 22 to 23 | All twenty references, every DOI a live hyperlink to its resolver |

The deck title runs as a small gray header across the top of every content slide, with that slide's own headline in navy Times New Roman beneath a navy rule. Page numbers sit in the lower right corner of every slide. The footer carries the author on the left and Friday, August 14, 2026 centered, above a silver hairline. There is no company logo.

**The ground is white on every slide.** All twenty covers are white-page scans, and a dark ground would ring each one with a hard bright rectangle and make the deck read as a set of screenshots. The five brief colors are the deck's entire vocabulary: `#002f5f` for headlines, rules and page numbers; `#666666` for the running header and footer; `#407cb9` for bullet glyphs, synthesis labels and hyperlinks; `#e3eaee` for the statistic tiles and the synthesis panel; `#dcdcdc` for the cover hairline.

**Cover cadence.** Four consecutive left-hand covers, then one right, repeating. Papers 5, 10, 15 and 20 take the right side. The rule lives in one function so it cannot drift on a rebuild:

```
paper   1  2  3  4  5   6  7  8  9 10  11 12 13 14 15  16 17 18 19 20
side    L  L  L  L  R   L  L  L  L  R   L  L  L  L  R   L  L  L  L  R
```

**Slide anatomy.** Two framing lines and the three evaluative axes sit in the upper text block; the synthesis lines sit in a pale panel with a navy edge at the foot of the column. The mix of bullets and numbers is not decorative: Paper Title and Abstract are square bullets because they frame, Strengths / Limitations / Results are an arabic numbered list because they read as a set of three, and LLM Trust / LLM Benefit are bullets in the panel because they are the conclusion. If a room is short on time, the panel is the part to read aloud.

**Where the extra lines went.** Three papers take a second synthesis line rather than being compressed into one that would misstate them: paper 13 (*Earning the Clinician's Trust*) carries a second **LLM Trust** line for automation bias and algorithm aversion; papers 14 (the Phase 1 protocol) and 20 (the capitalization plan) each carry a second **LLM Benefit** line. The panel grows with the line count and the evidence block above it shrinks, so nothing crowds or overlaps.

### The single-line requirement is enforced, not remembered

You asked for single-line items. That is a typographic property, so the build measures it rather than trusting me.

`assert_single_line()` runs before any slide is created. For all 143 list items it measures the bold label and the regular body separately, at their real point sizes, using the metric-compatible Liberation faces that LibreOffice substitutes for Arial, against the narrowest column that actually carries a list item, with a 2 pt safety margin. If anything overflows, the build stops and prints every offender:

```
single-line fit check failed:
  paper 12 LLM Trust: 606.5pt > 585.7pt -- Publishing what verification costs ...
```

It fired three times during this build and I tightened twenty-two items in response rather than widening the column or shrinking the type. That is also why the deck is typed in Arial and Times New Roman rather than something more fashionable: their metrics are the metrics the check can measure, and LibreOffice substitutes metric-identical clones, so the PDF's line breaks are the line breaks the check verified. A face without a metric clone would make the PDF a guess.

Body copy sits at 12.5 pt, which is the largest size at which all 143 items stay on one line inside a text column narrowed by a 3.45 in cover. There is a real tension between "single line" and "substantive line", and I resolved it toward legibility in a seminar room, with the check holding the constraint.

### One rendering defect I found and fixed

The pale synthesis panel and the accent rules were rendering with a soft drop shadow in the PDF. `python-pptx` attaches a `<p:style>` element to every autoshape carrying `<a:effectRef idx="2">`, and LibreOffice honors that even when `spPr` contains an empty `<a:effectLst/>`. `add_rect()` now removes the element outright, which is what keeps every panel and rule flat. I also aligned the two text frames to identical insets so the panel bullets sit on the same left edge as the bullets above them, and tabbed the reference numbers so entries 1 through 9 and 10 through 20 align.

### What each paper contributes

The deck is chronological because the case is cumulative. Reading the LLM Benefit lines in order gives the argument: paper 1 names the daraxonrasib triplet the trial now carries; 2 screens an arm out before enrollment; 3 sets the Phase 0 simulation gate; 4 supplies the MIDD evidence for FDA Type C; 5 through 8 supply the GCP spine, the consent architecture, the IND skeleton and the multi-site governance; 9 and 10 fix the device envelope and the ten-gate assurance suite; 11 through 13 make verification a duty, price it, and give a clinician a decision they can sign; 14 through 16 and 18 are the trial itself; 17, 19 and 20 are the ask. Application 10 of paper 19 asks a comprehensive cancer center for one meeting, which is the meeting this deck is for.

Every Limitations line is the paper's own, stated rather than softened, because this audience will find them anyway and a deck that states them first is the one that gets believed.

### Files produced

```
pdac-presentation/
  README.md                                    9 badges, deck spec, slide anatomy, evidence map
  abstracts/README.md                          documentation header above the intact 55-work corpus
  build/README.md                              6 badges, build order, fit check, layout constants
  build/extract_covers.py                      19 covers in document-body order
  build/render_cover_20.py                     the one reconstructed cover
  build/slide_content.py                       20 papers x 7 sourced single-line items
  build/build_deck.py                          python-pptx renderer plus the fit check
  build/export_pdf.py                          headless LibreOffice Impress export
  cover-images/README.md                       ordering, reconstruction, white-ground rationale
  cover-images/extracted/README.md             20-row inventory with pixels and cover side
  cover-images/extracted/cover-01..20.jpg      the twenty covers
  prompts/README.md                            filing convention, requirement-to-artifact map
  prompts/prompt-pdac.md                       the prompt, word for word
  prompts/output-pdac.md                       this file
  slides/README.md                             23-slide map, reference format, presenting notes
  slides/LLM-Pancreatic-Oncology-Clinical-Trial-System.pptx
  slides/LLM-Pancreatic-Oncology-Clinical-Trial-System.pdf
  theme/README.md                              the trial the deck argues for
```

Repository documentation updated for v0.9.0: `README.md` (badges, release block, Quick Start, Repository Structure, topology diagram, a new build-pipeline diagram, eight rows in the Documentation Files table, citation version), `releases.md` (v0.9.0 entry in the Summary / Features / Contributors / Notes format), `CHANGELOG.md` (v0.9.0 in Keep a Changelog format), and `CITATION.cff` (version, date, six keywords).

### CI

`ruff check .`, `ruff format --check .` and `yamllint -d relaxed .github/` all pass, which is what the three `lint-and-format` jobs on Python 3.10, 3.11 and 3.12 run. I added no per-file ignore to `ruff.toml` for this tree. The one suppression is a `# noqa: E402` on the `slide_content` import in `build_deck.py`, which necessarily follows the `sys.path` insertion that makes it importable when the file is run as a script. `python-pptx` and `pillow` are build-time dependencies only, so a contributor without them still gets a clean lint run.

### Commits

Pushed as each artifact finished rather than batched, so branch progress was observable throughout: covers, then the deck and PDF, then the READMEs, then the prompt record, then the repository documentation, then this file.

### Two things worth your judgment

The deck opens with a title slide rather than a cover-image slide, so the four-left-then-one-right cadence starts at paper 1 on slide 2. A title slide is where the title, author, date and venue belong for this audience, and the alternative would have pushed one paper off the front.

And the reconstructed cover for paper 20 is the one artifact here that is drawn rather than sourced. It is faithful to that paper's own record and says so on its face, but if you have the deposited PDF, dropping its real cover page into `cover-images/extracted/` under the same filename and rerunning `build_deck.py` replaces it with no other change.
