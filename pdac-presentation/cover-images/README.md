# pdac-presentation/cover-images - source cover art (v0.9.0)

[![Release](https://img.shields.io/badge/Release-v0.9.0-brightgreen.svg)](../../releases.md)
[![Source](https://img.shields.io/badge/Source-1%20.docx-002f5f.svg)](ChemicalQDevice-PDAC-Covers-13Aug26.docx)
[![Embedded](https://img.shields.io/badge/Embedded%20covers-19-407cb9.svg)](#what-the-source-document-carries)
[![Extracted](https://img.shields.io/badge/Extracted%20covers-20-407cb9.svg)](extracted/)
[![Ground](https://img.shields.io/badge/Page%20ground-white-e3eaee.svg)](#why-the-deck-is-light)

**The source Word document of PDAC paper cover pages, and the extraction that
turns it into the twenty numbered covers the seminar deck places on its slides.**

---

## Contents

| Path | What it is |
|:--|:--|
| [`ChemicalQDevice-PDAC-Covers-13Aug26.docx`](ChemicalQDevice-PDAC-Covers-13Aug26.docx) | The source document, assembled August 13, 2026. 3.4 MB, 19 embedded JPEG cover pages, no captions |
| [`extracted/`](extracted/) | The twenty covers the deck uses, numbered 01 to 20 in chronological order |

## What the source document carries

Nineteen JPEG cover pages, one per paper, laid out down the document body in
chronological order, earliest first. The document has no caption text: the images
are the entire content, so the order of the body is the only thing that maps an
image to a paper.

That ordering is not recoverable from the ZIP archive's file listing. A `.docx`
stores its media as `word/media/image1.jpg`, `image2.jpg` and so on, in the order
Word happened to intern them, and its relationship map at
`word/_rels/document.xml.rels` is not written in document order either. In this
document the first cover in the body is `image4.jpg` and the tenth is `image1.jpg`.

[`../build/extract_covers.py`](../build/extract_covers.py) therefore parses
`word/document.xml` for the sequence of `r:embed` relationship identifiers,
resolves each one through the relationship map, and writes the covers out under
the chronological slug of the paper that owns them.

```
word/document.xml         r:embed order  ->  rId7  rId8  rId9  rId10 ...
word/_rels/...rels        resolves to    ->  image4 image14 image12 image3 ...
extracted/                written as     ->  cover-01 cover-02 cover-03 cover-04 ...
```

## The twentieth cover

The source document does not carry a cover page for the twentieth paper in the
deck, *From Independent Scientist to Novel Performer: A Small-Business Operating,
Milestone, and Capitalization Plan for a Phase 1 LLM-Advised Robotic Whipple*
([10.5281/zenodo.21887807](https://doi.org/10.5281/zenodo.21887807), deposited
August 11, 2026). The document was assembled on August 13 and the paper is two
days older, so the omission is a gap in the source, not an error in the deck.

[`../build/render_cover_20.py`](../build/render_cover_20.py) reconstructs that
page from the paper's own deposited front matter and its abstract of record, in
the visual idiom of the August 2026 covers that the document does carry. Nothing
on the reconstructed page is invented: every string is quoted from the abstract in
[`../abstracts/README.md`](../abstracts/README.md) or taken from the funding
tables of [`../theme/update-final-LaTeX.zip`](../theme/). A footer line on the
page itself states that it is a reconstruction and not the deposited PDF cover.

## Why the deck is light

Every one of the twenty covers is a white page. A dark slide ground would ring
each cover with a hard bright rectangle and make the deck look like a set of
screenshots. The deck therefore runs a white ground throughout, sets navy
`#002f5f` type on it, and separates each cover from the page with a single
`#dcdcdc` hairline rather than a heavy frame or a drop shadow.

## Reproducing the extraction

```bash
pip install pillow
python pdac-presentation/build/extract_covers.py     # 19 covers, in document order
python pdac-presentation/build/render_cover_20.py    # the reconstructed 20th
```

Both scripts are idempotent and overwrite their outputs. `extract_covers.py`
fails loudly if the document stops carrying exactly nineteen images, so a
replacement source document cannot silently shift the paper-to-cover mapping.

## Licensing and use

The covers are the front pages of the author's own deposited works, reproduced
here to identify each paper on its slide. Each work is cited in full, with its
DOI, on the last two slides of the deck and in
[`../README.md`](../README.md#the-twenty-papers).
