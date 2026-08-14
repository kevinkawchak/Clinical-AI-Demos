# pdac-presentation/slides - the deliverables (v0.9.0)

[![Release](https://img.shields.io/badge/Release-v0.9.0-brightgreen.svg)](../../releases.md)
[![Slides](https://img.shields.io/badge/Slides-23-002f5f.svg)](#slide-map)
[![Aspect](https://img.shields.io/badge/Aspect-16%3A9%20landscape-407cb9.svg)](#deck-specification)
[![PPTX](https://img.shields.io/badge/PPTX-4.1%20MB-666666.svg)](LLM-Pancreatic-Oncology-Clinical-Trial-System.pptx)
[![PDF](https://img.shields.io/badge/PDF-5.0%20MB-666666.svg)](LLM-Pancreatic-Oncology-Clinical-Trial-System.pdf)
[![Links](https://img.shields.io/badge/DOI%20hyperlinks-20-407cb9.svg)](#references)
[![Generated](https://img.shields.io/badge/Generated-do%20not%20edit%20by%20hand-dcdcdc.svg)](#regenerating)

**The seminar deck, in both formats. Twenty deposited papers, in chronological
order, and the Phase 1 LLM-directed robotic Whipple trial they were written to
support.**

---

## Files

| File | Format | What it is for |
|:--|:--|:--|
| [`LLM-Pancreatic-Oncology-Clinical-Trial-System.pptx`](LLM-Pancreatic-Oncology-Clinical-Trial-System.pptx) | Office Open XML presentation | Presenting. Opens in PowerPoint, Keynote, LibreOffice Impress and Google Slides |
| [`LLM-Pancreatic-Oncology-Clinical-Trial-System.pdf`](LLM-Pancreatic-Oncology-Clinical-Trial-System.pdf) | PDF | The handout, and the archival record. All twenty DOI hyperlinks are live |

Both are build output. See [Regenerating](#regenerating).

## Deck specification

| Field | Value |
|:--|:--|
| Title | LLM Pancreatic Oncology Clinical Trial System: Large Documents, Funding, and AI Peer Review |
| Author | Kevin Kawchak, Chief Executive Officer, ChemicalQDevice |
| Date | Friday, August 14, 2026 |
| Venue | Oncology trials seminar, university comprehensive cancer center |
| Orientation | 16:9 landscape, 13.333 in by 7.5 in (960 pt by 540 pt) |
| Slide count | 23 |
| Title position | Top of every page: the deck title as a running header, and the slide's own headline beneath the navy rule |
| Page numbers | Lower right corner, navy, bold, on every slide including the title slide |
| Footer | Author left, date centered, page number right, above a `#dcdcdc` hairline |
| Body typeface | Arial 12.5 pt |
| Display typeface | Times New Roman, navy `#002f5f` |
| Company logo | None, by instruction |

## Slide map

| Slide | Contents | Cover side |
|--:|:--|:--|
| 1 | Title, subtitle, four statistic tiles, author, contact, venue, date, disclaimer | none |
| 2 | Paper 01, End-to-End PDAC Digital Twin Clinical Trial Proposals | left |
| 3 | Paper 02, ChatGPT 100,000 Patient In Silico Phase III Triplicate | left |
| 4 | Paper 03, QSP Metastatic PDAC Simulation | left |
| 5 | Paper 04, Accelerating FDA Compliance of in silico Trials | left |
| 6 | Paper 05, Adaption: ICH Harmonised Guideline | **right** |
| 7 | Paper 06, Adaption: 21 CFR Part 50 | left |
| 8 | Paper 07, Adaption: 21 CFR Part 312 | left |
| 9 | Paper 08, National Platform for Physical AI Oncology Trials | left |
| 10 | Paper 09, 2030: 60 Second PDAC Robotic Whipple | left |
| 11 | Paper 10, Mobile Unitree H2 Surgical Humanoid | **right** |
| 12 | Paper 11, VVUQ Physical AI Oncology Trial Bill | left |
| 13 | Paper 12, H. R. 9510 (Bill v5.0) 2026 | left |
| 14 | Paper 13, Earning the Clinician's Trust | left |
| 15 | Paper 14, On-Premises LLM-Directed Robotic Whipple, Phase 1 | left |
| 16 | Paper 15, Phase 2 Daraxonrasib + LLM Guided Robotic Whipple | **right** |
| 17 | Paper 16, Investigational New Drug Application, Daraxonrasib | left |
| 18 | Paper 17, Clinical Trial Funding Application v2.0 | left |
| 19 | Paper 18, Patient Robot Advocacy | left |
| 20 | Paper 19, 10 Funding Applications | left |
| 21 | Paper 20, From Independent Scientist to Novel Performer | **right** |
| 22 | References 1 to 10 of 20 | none |
| 23 | References 11 to 20 of 20 | none |

## References

The last two slides carry all twenty works in author-date form, with the title in
italics and the digital object identifier rendered as a live hyperlink to its
resolver:

```
 7.  Kawchak, K. (2026). Adaption: 21 CFR Part 312, End-to-End Physical AI
     Oncology Clinical Trial Unification. Zenodo.
     https://doi.org/10.5281/zenodo.19057628
```

All twenty hyperlinks survive the PDF export and are clickable in the handout.
The entry number is followed by a tab rather than padded spaces, so numbers 1
through 9 and 10 through 20 align on the same left edge.

## Presenting notes

* **The four statistic tiles on slide 1** are the deck's whole argument in four
  numbers: twenty deposited papers, a twelve-module IND in four days, a Phase 1
  at n = 18 behind a 1000-simulation gate, and a $1.6M small-business ask against
  a $3.5M direct program.
* **The pale panel at the foot of every paper slide** is the synthesis. If the
  room is short on time, the two or three lines inside it are the ones to read
  aloud; the five lines above them are the supporting record.
* **Slides 6, 11, 16 and 21 flip the cover to the right.** The rhythm is
  deliberate: it breaks the scan pattern every fifth slide, at the four points
  where the narrative changes register (regulation, assurance, randomization,
  capitalization).
* **Every limitation on every slide is the paper's own.** They are stated rather
  than softened because this audience will find them anyway, and a deck that
  states them first is the one that gets believed.

## Regenerating

```bash
pip install python-pptx pillow
python pdac-presentation/build/build_deck.py    # writes the .pptx
python pdac-presentation/build/export_pdf.py    # writes the .pdf
```

`build_deck.py` measures every bullet and numbered item before it writes anything
and fails the build if any of them would wrap onto a second line. Edit the copy
in [`../build/slide_content.py`](../build/slide_content.py), never the `.pptx`
directly: a hand edit is lost on the next build and is not covered by the fit
check.

`export_pdf.py` calls headless LibreOffice Impress under a private user profile.
Where Impress is unavailable, export from PowerPoint with
**File > Export > Create PDF/XPS**; the deck is typed in Arial and Times New
Roman so both routes break lines identically.

## Disclaimer

Independent research. Not medical or regulatory advice, and not endorsed by the
FDA, NIH, HHS, an IRB, ICH, or any sponsor. No trial described in this deck is
active or approved.
