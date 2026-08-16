"""Reconstruct the cover page for paper 20 of the PDAC seminar deck.

``cover-images/ChemicalQDevice-PDAC-Covers-13Aug26.docx`` was assembled on
August 13, 2026 and carries nineteen cover pages.  The twentieth paper in the
seminar deck,

    From Independent Scientist to Novel Performer: A Small-Business Operating,
    Milestone, and Capitalization Plan for a Phase 1 LLM-Advised Robotic Whipple
    10.5281/zenodo.21887807, August 11, 2026

has no cover page in that document.  Rather than leave slide 20 without the
cover image every other slide carries, this module redraws the paper's own
deposited front matter -- title, author block, DOI, ORCID iD, deposit city and
date, and the abstract exactly as filed in ``abstracts/README.md`` -- in the
visual idiom of the August 2026 covers that do appear in the source document:
white ground, navy rules, a serif title over a serif abstract.

Nothing on the reconstructed page is invented.  Every string is either quoted
from the paper's abstract of record or taken from the funding tables of
``theme/update-final-LaTeX.zip``.  A footer line on the page itself states that
it is a reconstruction, so the page cannot be mistaken for the deposited PDF.

Run from the repository root::

    python pdac-presentation/build/render_cover_20.py
"""

from __future__ import annotations

import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

REPO_ROOT = Path(__file__).resolve().parents[2]
OUTPUT_PATH = (
    REPO_ROOT
    / "pdac-presentation"
    / "cover-images"
    / "extracted"
    / "cover-20-independent-scientist-to-novel-performer.jpg"
)

# The source covers are portrait pages a little wider than 0.71 of their height.
PAGE_WIDTH = 1240
PAGE_HEIGHT = 1730
MARGIN = 92

WHITE = (255, 255, 255)
NAVY = (33, 65, 104)
BLUE = (64, 124, 185)
GRAY = (102, 102, 102)
INK = (26, 26, 26)
PALE = (227, 234, 238)
RULE = (220, 220, 220)

FONT_DIR = Path("/usr/share/fonts/truetype/liberation")
SERIF = FONT_DIR / "LiberationSerif-Regular.ttf"
SERIF_BOLD = FONT_DIR / "LiberationSerif-Bold.ttf"
SERIF_ITALIC = FONT_DIR / "LiberationSerif-Italic.ttf"
SANS = FONT_DIR / "LiberationSans-Regular.ttf"
SANS_BOLD = FONT_DIR / "LiberationSans-Bold.ttf"

TITLE_LINES = ("From Independent Scientist to Novel Performer",)
SUBTITLE_LINES = (
    "A Small-Business Operating, Milestone, and Capitalization Plan",
    "for a Phase 1 LLM-Advised Robotic Whipple",
)
BADGES = ("12 milestones", "SBIR Phase I + II", "33 months", "$1,606,000 award")
AUTHOR_LINE = "CEO Kevin Kawchak, ChemicalQDevice  |  kevink@chemicalqdevice.com"
IDENTIFIER_LINE = "10.5281/zenodo.21887807  |  ORCID 0009-0007-5457-8667"
PLACE_LINE = "San Diego, CA  |  August 11, 2026"

ABSTRACT_PARAGRAPHS = (
    "In August 2026 the author filed ten funding applications for a Phase 1 trial of an "
    "LLM-advised robotic pancreaticoduodenectomy with perioperative daraxonrasib, written "
    "throughout as an independent scientist. Nine of the ten address mechanisms that fund a "
    "person or an institution. One, application 05, addresses the only mechanism in the set "
    "built for a company, and it was the shortest of the ten. This paper converts the author "
    "from independent scientist to small-business operator and rewrites that application as "
    "the document it should have been.",
    "The clause the conversion turns on is neither the report's individual-scientist language "
    "nor its novel-performers chapter. It is the Small Business Innovation Research clause of "
    "Science: A New Golden Age, which appears in three separate chapters and is the only clause "
    "in the report written for a firm. Three numbers govern what follows: $306,000 for a "
    "nine-month Phase I, $1,300,000 for a twenty-four-month Phase II, and the $3,500,000 "
    "five-year direct program the two are measured against. Two more are derived: $1,396,000 of "
    "direct work sits inside the $1,606,000 award, and $2,104,000 sits outside it.",
    "What is offered is a costed twelve-milestone schedule. Every row carries an evidence "
    "artifact that exists as a file, a cost that sums into its phase, a stop condition stated "
    "before the work begins, and the funder mechanism that pays.",
)

LEDGER_CELLS = (
    ("SBIR Phase I", "$306,000", "9 months, 5 milestones"),
    ("SBIR Phase II", "$1,300,000", "24 months, 7 milestones"),
    ("Private above firewall", "$5,900,000", "3.67 to one on cash alone"),
)

PACKAGE_TABLE_TITLE = "The four work packages, inside the award and against the five-year direct program"
PACKAGE_HEADERS = ("Work package", "SBIR Phase I", "SBIR Phase II", "Five-year direct")
PACKAGE_ROWS = (
    ("Simulation and verification", "in Phase I scope", "carried forward", "carried forward"),
    ("Regulatory and protocol", "in Phase I scope", "carried forward", "carried forward"),
    ("Site and device readiness", "not in scope", "in Phase II scope", "carried forward"),
    ("Clinical conduct", "not in scope", "partial", "full"),
    ("Overhead and fee load", "15.0 percent", "15.0 percent", "direct only"),
)

DISCLAIMER = (
    "Independent research paper and practical adoption guide. It is not medical or regulatory "
    "advice and is not endorsed by the FDA, NIH, HHS, an IRB, ICH, or any sponsor."
)
RECONSTRUCTION_NOTE = (
    "Cover page reconstructed August 14, 2026 for the ChemicalQDevice PDAC seminar deck from the "
    "deposited front matter and abstract of record of 10.5281/zenodo.21887807. It is not the "
    "deposited PDF cover."
)


def load(path: Path, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(path), size)


def wrap(text: str, font: ImageFont.FreeTypeFont, width: float) -> list[str]:
    """Greedy word wrap against a measured pixel width."""
    words = text.split()
    lines: list[str] = []
    current = ""
    for word in words:
        candidate = f"{current} {word}".strip()
        if font.getlength(candidate) <= width or not current:
            current = candidate
        else:
            lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def centered(draw: ImageDraw.ImageDraw, y: int, text: str, font, fill) -> int:
    width = font.getlength(text)
    draw.text(((PAGE_WIDTH - width) / 2, y), text, font=font, fill=fill)
    return y + int(font.size * 1.32)


def draw_badges(draw: ImageDraw.ImageDraw, y: int, font) -> int:
    pad_x, pad_y, gap = 16, 8, 14
    widths = [font.getlength(label) + 2 * pad_x for label in BADGES]
    total = sum(widths) + gap * (len(BADGES) - 1)
    x = (PAGE_WIDTH - total) / 2
    height = int(font.size * 1.7)
    for label, width in zip(BADGES, widths):
        draw.rounded_rectangle([x, y, x + width, y + height], radius=5, fill=PALE, outline=BLUE, width=1)
        draw.text((x + pad_x, y + pad_y - 1), label, font=font, fill=NAVY)
        x += width + gap
    return y + height + 26


def draw_ledger(draw: ImageDraw.ImageDraw, y: int, label_font, value_font, note_font) -> int:
    gap = 18
    width = (PAGE_WIDTH - 2 * MARGIN - gap * (len(LEDGER_CELLS) - 1)) / len(LEDGER_CELLS)
    height = 118
    x = MARGIN
    for label, value, note in LEDGER_CELLS:
        draw.rectangle([x, y, x + width, y + height], fill=PALE)
        draw.rectangle([x, y, x + 4, y + height], fill=NAVY)
        draw.text((x + 20, y + 16), label, font=label_font, fill=GRAY)
        draw.text((x + 20, y + 42), value, font=value_font, fill=NAVY)
        for offset, line in enumerate(wrap(note, note_font, width - 40)):
            draw.text((x + 20, y + 80 + offset * 20), line, font=note_font, fill=GRAY)
        x += width + gap
    return y + height + 30


def draw_package_table(draw: ImageDraw.ImageDraw, y: int, title_font, head_font, cell_font) -> int:
    draw.text((MARGIN, y), PACKAGE_TABLE_TITLE, font=title_font, fill=NAVY)
    y += 34

    table_width = PAGE_WIDTH - 2 * MARGIN
    first = table_width * 0.34
    other = (table_width - first) / 3
    columns = [MARGIN, MARGIN + first, MARGIN + first + other, MARGIN + first + 2 * other]
    row_height = 34

    draw.rectangle([MARGIN, y, PAGE_WIDTH - MARGIN, y + row_height], fill=NAVY)
    for x, header in zip(columns, PACKAGE_HEADERS):
        draw.text((x + 12, y + 8), header, font=head_font, fill=WHITE)
    y += row_height

    for index, row in enumerate(PACKAGE_ROWS):
        if index % 2 == 0:
            draw.rectangle([MARGIN, y, PAGE_WIDTH - MARGIN, y + row_height], fill=PALE)
        for x, cell in zip(columns, row):
            draw.text((x + 12, y + 9), cell, font=cell_font, fill=INK)
        draw.line([MARGIN, y + row_height, PAGE_WIDTH - MARGIN, y + row_height], fill=RULE, width=1)
        y += row_height
    return y + 30


def render() -> Path:
    page = Image.new("RGB", (PAGE_WIDTH, PAGE_HEIGHT), WHITE)
    draw = ImageDraw.Draw(page)

    title_font = load(SERIF_BOLD, 46)
    subtitle_font = load(SERIF_BOLD, 29)
    eyebrow_font = load(SANS_BOLD, 19)
    badge_font = load(SANS, 19)
    meta_font = load(SERIF, 23)
    doi_font = load(SERIF, 22)
    heading_font = load(SANS_BOLD, 24)
    body_font = load(SERIF, 23)
    small_font = load(SERIF_ITALIC, 19)
    tiny_font = load(SANS, 16)
    ledger_label = load(SANS_BOLD, 16)
    ledger_value = load(SANS_BOLD, 27)
    ledger_note = load(SANS, 15)

    draw.rectangle([MARGIN, 46, PAGE_WIDTH - MARGIN, 52], fill=NAVY)

    y = 78
    y = centered(draw, y, "CHEMICALQDEVICE INDEPENDENT RESEARCH", eyebrow_font, BLUE)
    y += 12
    for line in TITLE_LINES:
        y = centered(draw, y, line, title_font, NAVY)
    y += 8
    for line in SUBTITLE_LINES:
        y = centered(draw, y, line, subtitle_font, INK)

    y += 26
    y = draw_badges(draw, y, badge_font)

    y = centered(draw, y, AUTHOR_LINE, meta_font, INK)
    y = centered(draw, y, IDENTIFIER_LINE, doi_font, BLUE)
    y = centered(draw, y, PLACE_LINE, meta_font, INK)

    y += 16
    draw.rectangle([MARGIN, y, PAGE_WIDTH - MARGIN, y + 3], fill=NAVY)
    y += 34

    draw.text((MARGIN, y), "Abstract", font=heading_font, fill=NAVY)
    y += 40
    text_width = PAGE_WIDTH - 2 * MARGIN
    for paragraph in ABSTRACT_PARAGRAPHS:
        for line in wrap(paragraph, body_font, text_width):
            draw.text((MARGIN, y), line, font=body_font, fill=INK)
            y += 31
        y += 14

    y += 10
    y = draw_ledger(draw, y, ledger_label, ledger_value, ledger_note)
    y = draw_package_table(draw, y, heading_font, ledger_label, ledger_note)

    draw.line([MARGIN, y, PAGE_WIDTH - MARGIN, y], fill=RULE, width=1)
    y += 18
    for line in wrap(DISCLAIMER, small_font, text_width):
        draw.text((MARGIN, y), line, font=small_font, fill=GRAY)
        y += 26

    footer_y = PAGE_HEIGHT - MARGIN - 46
    draw.line([MARGIN, footer_y - 16, PAGE_WIDTH - MARGIN, footer_y - 16], fill=RULE, width=1)
    for line in wrap(RECONSTRUCTION_NOTE, tiny_font, text_width):
        draw.text((MARGIN, footer_y), line, font=tiny_font, fill=GRAY)
        footer_y += 22

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    page.save(OUTPUT_PATH, "JPEG", quality=94, subsampling=0)
    return OUTPUT_PATH


def main() -> int:
    path = render()
    print(f"wrote {path.relative_to(REPO_ROOT)} ({path.stat().st_size:,} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
