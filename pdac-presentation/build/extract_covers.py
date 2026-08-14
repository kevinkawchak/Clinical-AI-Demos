"""Extract the PDAC paper cover images from the source Word document.

The source ``cover-images/ChemicalQDevice-PDAC-Covers-13Aug26.docx`` embeds
nineteen JPEG cover pages, one per paper, laid out in the document body in
chronological order (earliest paper first).  A ``.docx`` is a ZIP archive, so
the covers are read straight out of ``word/media`` and re-ordered by the
``r:embed`` relationship identifiers in the order they appear in
``word/document.xml``.  The relationship map in ``word/_rels/document.xml.rels``
is not stored in document order, which is why the document body has to be
parsed rather than the media folder simply being listed.

The twentieth paper in the deck, "From Independent Scientist to Novel
Performer" (10.5281/zenodo.21887807, August 11, 2026), has no cover page in the
source document.  Its cover is reconstructed by ``render_cover_20.py`` from the
paper's own deposited front matter so that all twenty slides carry a cover.

Run from the repository root::

    python pdac-presentation/build/extract_covers.py
"""

from __future__ import annotations

import re
import shutil
import sys
import zipfile
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
PRESENTATION_DIR = REPO_ROOT / "pdac-presentation"
SOURCE_DOCX = PRESENTATION_DIR / "cover-images" / "ChemicalQDevice-PDAC-Covers-13Aug26.docx"
OUTPUT_DIR = PRESENTATION_DIR / "cover-images" / "extracted"

EMBED_PATTERN = re.compile(rb'r:embed="(rId\d+)"')
RELATION_PATTERN = re.compile(rb'Id="(rId\d+)"[^>]*Target="([^"]+)"')

# Chronological slugs, earliest paper first.  Index i of this list is the paper
# that owns the i-th image in the document body.
COVER_SLUGS = (
    "01-pdac-digital-twin-proposals",
    "02-chatgpt-100k-patient-phase-iii",
    "03-qsp-metastatic-pdac-simulation",
    "04-fda-compliance-cost-efficiency",
    "05-ich-harmonised-guideline",
    "06-21-cfr-part-50",
    "07-21-cfr-part-312",
    "08-national-platform",
    "09-2030-60-second-whipple",
    "10-unitree-h2-surgical-humanoid",
    "11-vvuq-oncology-trial-bill",
    "12-hr-9510-bill-v5",
    "13-earning-the-clinicians-trust",
    "14-phase-1-ind-ide-protocol",
    "15-phase-2-rct-protocol",
    "16-ind-application-daraxonrasib",
    "17-funding-application-v2",
    "18-patient-robot-advocacy",
    "19-ten-funding-applications",
)


def document_image_order(docx_path: Path) -> list[str]:
    """Return the archive member names of the covers in document-body order."""
    with zipfile.ZipFile(docx_path) as archive:
        document = archive.read("word/document.xml")
        relations = archive.read("word/_rels/document.xml.rels")

    targets = {rel_id.decode("utf-8"): target.decode("utf-8") for rel_id, target in RELATION_PATTERN.findall(relations)}
    ordered = []
    for match in EMBED_PATTERN.findall(document):
        target = targets[match.decode("utf-8")]
        ordered.append(f"word/{target}")
    return ordered


def extract(docx_path: Path, output_dir: Path) -> list[Path]:
    """Write each cover to ``output_dir`` under its chronological slug."""
    members = document_image_order(docx_path)
    if len(members) != len(COVER_SLUGS):
        raise SystemExit(f"expected {len(COVER_SLUGS)} covers in {docx_path.name}, found {len(members)}")

    output_dir.mkdir(parents=True, exist_ok=True)
    written = []
    with zipfile.ZipFile(docx_path) as archive:
        for slug, member in zip(COVER_SLUGS, members):
            suffix = Path(member).suffix.lower()
            destination = output_dir / f"cover-{slug}{suffix}"
            with archive.open(member) as source, destination.open("wb") as target:
                shutil.copyfileobj(source, target)
            written.append(destination)
    return written


def main() -> int:
    if not SOURCE_DOCX.exists():
        raise SystemExit(f"source document not found: {SOURCE_DOCX}")
    written = extract(SOURCE_DOCX, OUTPUT_DIR)
    for path in written:
        print(f"wrote {path.relative_to(REPO_ROOT)} ({path.stat().st_size:,} bytes)")
    print(f"{len(written)} covers extracted to {OUTPUT_DIR.relative_to(REPO_ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
