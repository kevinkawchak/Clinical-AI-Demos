"""Export the seminar deck to PDF with LibreOffice Impress.

PowerPoint is not available in the build environment, so the landscape PDF
handout is rendered by ``soffice --headless --convert-to pdf``.  The deck is
typed in Arial and Times New Roman precisely so this step is faithful:
LibreOffice substitutes Liberation Sans and Liberation Serif, which are
metric-compatible clones, so line breaks in the PDF match the line breaks the
build's fit check measured.

A private user profile is used so the export cannot be disturbed by, or
disturb, any other LibreOffice state in the container.

Run from the repository root::

    python pdac-presentation/build/export_pdf.py
"""

from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
SLIDES_DIR = REPO_ROOT / "pdac-presentation" / "slides"
DECK_NAME = "LLM-Pancreatic-Oncology-Clinical-Trial-System"
SOURCE_PPTX = SLIDES_DIR / f"{DECK_NAME}.pptx"
OUTPUT_PDF = SLIDES_DIR / f"{DECK_NAME}.pdf"

CONVERT_TIMEOUT_SECONDS = 600


def find_soffice() -> str:
    for candidate in ("soffice", "libreoffice"):
        path = shutil.which(candidate)
        if path:
            return path
    raise SystemExit(
        "LibreOffice was not found on PATH. Install libreoffice-impress, or export "
        "the PDF from PowerPoint with File > Export > Create PDF/XPS."
    )


def export() -> Path:
    if not SOURCE_PPTX.exists():
        raise SystemExit(f"deck not found: {SOURCE_PPTX}. Run build_deck.py first.")

    with tempfile.TemporaryDirectory(prefix="pdac-soffice-") as profile:
        command = [
            find_soffice(),
            "--headless",
            "--norestore",
            f"-env:UserInstallation=file://{profile}",
            "--convert-to",
            "pdf",
            str(SOURCE_PPTX),
            "--outdir",
            str(SLIDES_DIR),
        ]
        result = subprocess.run(command, capture_output=True, text=True, timeout=CONVERT_TIMEOUT_SECONDS)
    if result.returncode != 0 or not OUTPUT_PDF.exists():
        raise SystemExit(
            "PDF export failed\n"
            f"  exit code: {result.returncode}\n"
            f"  stdout: {result.stdout.strip()}\n"
            f"  stderr: {result.stderr.strip()}"
        )
    return OUTPUT_PDF


def main() -> int:
    path = export()
    print(f"wrote {path.relative_to(REPO_ROOT)} ({path.stat().st_size:,} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
