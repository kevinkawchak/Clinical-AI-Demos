# pdac-presentation/cover-images/extracted - the twenty deck covers (v0.9.0)

[![Release](https://img.shields.io/badge/Release-v0.9.0-brightgreen.svg)](../../../releases.md)
[![Covers](https://img.shields.io/badge/Covers-20-002f5f.svg)](#inventory)
[![Order](https://img.shields.io/badge/Order-chronological-407cb9.svg)](#inventory)
[![Format](https://img.shields.io/badge/Format-JPEG%2C%20portrait-666666.svg)](#inventory)
[![Ground](https://img.shields.io/badge/Ground-white%20page-e3eaee.svg)](../README.md#why-the-deck-is-light)
[![Generated](https://img.shields.io/badge/Generated-do%20not%20edit%20by%20hand-dcdcdc.svg)](#regenerating)

**Twenty paper cover pages, numbered 01 to 20 in the chronological order the deck
presents them. Nineteen are extracted from the source Word document; the
twentieth is reconstructed from its paper's deposited front matter.**

---

## How to read a filename

```
cover-07-21-cfr-part-312.jpg
      |  |
      |  +-- short slug of the paper
      +----- slide order, 01 = earliest paper, 20 = most recent
```

The number is the deck's paper number. Paper *n* appears on deck slide *n + 1*,
because slide 1 is the title slide.

## Inventory

| File | Paper | Deposited | Pixels | Size | Cover side |
|:--|--:|:--|:--|--:|:--|
| `cover-01-pdac-digital-twin-proposals.jpg` | 1 | Jun 24, 2025 | 1206 x 1614 | 390 KB | left |
| `cover-02-chatgpt-100k-patient-phase-iii.jpg` | 2 | Jul 24, 2025 | 1204 x 1630 | 405 KB | left |
| `cover-03-qsp-metastatic-pdac-simulation.jpg` | 3 | Aug 29, 2025 | 1208 x 1642 | 414 KB | left |
| `cover-04-fda-compliance-cost-efficiency.jpg` | 4 | Sep 30, 2025 | 1214 x 1636 | 386 KB | left |
| `cover-05-ich-harmonised-guideline.jpg` | 5 | Mar 12, 2026 | 935 x 1293 | 78 KB | **right** |
| `cover-06-21-cfr-part-50.jpg` | 6 | Mar 16, 2026 | 939 x 1276 | 74 KB | left |
| `cover-07-21-cfr-part-312.jpg` | 7 | Mar 17, 2026 | 932 x 1268 | 76 KB | left |
| `cover-08-national-platform.jpg` | 8 | Mar 28, 2026 | 974 x 1457 | 80 KB | left |
| `cover-09-2030-60-second-whipple.jpg` | 9 | May 15, 2026 | 1031 x 1402 | 260 KB | left |
| `cover-10-unitree-h2-surgical-humanoid.jpg` | 10 | May 28, 2026 | 1030 x 1361 | 202 KB | **right** |
| `cover-11-vvuq-oncology-trial-bill.jpg` | 11 | May 30, 2026 | 1031 x 1315 | 123 KB | left |
| `cover-12-hr-9510-bill-v5.jpg` | 12 | Jun 10, 2026 | 1087 x 1499 | 232 KB | left |
| `cover-13-earning-the-clinicians-trust.jpg` | 13 | Jun 16, 2026 | 906 x 1233 | 192 KB | left |
| `cover-14-phase-1-ind-ide-protocol.jpg` | 14 | Jun 21, 2026 | 924 x 1322 | 170 KB | left |
| `cover-15-phase-2-rct-protocol.jpg` | 15 | Jun 23, 2026 | 905 x 1330 | 172 KB | **right** |
| `cover-16-ind-application-daraxonrasib.jpg` | 16 | Jul 1, 2026 | 916 x 1291 | 192 KB | left |
| `cover-17-funding-application-v2.jpg` | 17 | Jul 12, 2026 | 932 x 1152 | 149 KB | left |
| `cover-18-patient-robot-advocacy.jpg` | 18 | Jul 31, 2026 | 902 x 1295 | 187 KB | left |
| `cover-19-ten-funding-applications.jpg` | 19 | Aug 4, 2026 | 941 x 1312 | 158 KB | left |
| `cover-20-independent-scientist-to-novel-performer.jpg` | 20 | Aug 11, 2026 | 1240 x 1730 | 517 KB | **right, reconstructed** |

Every page is portrait, white-ground, and between 0.70 and 0.81 wide relative to
its height. `build_deck.py` fits each one inside a fixed 3.45 in by 5.36 in box
with its aspect ratio preserved and centers it, so the varying source dimensions
never distort a cover or push a text column.

## Cover 20 is a reconstruction

`cover-20-independent-scientist-to-novel-performer.jpg` is the only file here
that is drawn rather than extracted. The source Word document was assembled on
August 13, 2026 and carries no cover page for the paper deposited on August 11.

The reconstruction is built by
[`../../build/render_cover_20.py`](../../build/render_cover_20.py) from the
paper's own record:

| Element on the page | Source |
|:--|:--|
| Title and subtitle | The paper's title as deposited |
| Author, email, ORCID iD, DOI, city, date | The paper's front matter |
| Abstract, three paragraphs | Verbatim from [`../../abstracts/README.md`](../../abstracts/README.md) |
| $306,000 / $1,300,000 / $5,900,000 ledger | The abstract and Table 18 of [`../../theme/`](../../theme/) |
| Four work packages table | Figure 18 of `theme/update-final-LaTeX.zip`, section 6 |
| Footer notice | Written by the build to mark the page a reconstruction |

The footer line on the page reads, in full: *"Cover page reconstructed August 14,
2026 for the ChemicalQDevice PDAC seminar deck from the deposited front matter
and abstract of record of 10.5281/zenodo.21887807. It is not the deposited PDF
cover."* Nothing on the page is invented.

## Regenerating

These files are build output. Edit the generators, never the JPEGs.

```bash
python pdac-presentation/build/extract_covers.py     # rewrites covers 01 to 19
python pdac-presentation/build/render_cover_20.py    # rewrites cover 20
python pdac-presentation/build/build_deck.py         # rebuilds the deck around them
```

`extract_covers.py` raises `SystemExit` if the source document stops carrying
exactly nineteen embedded images, so a replacement document cannot silently
shift the paper-to-cover mapping.
