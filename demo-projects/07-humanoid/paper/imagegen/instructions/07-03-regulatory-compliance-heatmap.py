"""Image 07-03: AE Response Regulatory and Risk Compliance Heatmap.

Letter landscape, 11.0 x 8.5 inches, 300 dpi. Main heatmap 10 phases x 14 frameworks,
sub-heatmap 4 sites x 14 frameworks. Outlined HR 9505 and CTCAE columns. Section
sign used in CFR references.
"""

from __future__ import annotations

import pathlib

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap

PALETTE = {
    "deep_navy": "#1F3A68",
    "teal": "#2E8B8B",
    "burgundy": "#8B2E3F",
    "gold": "#C18A2C",
    "forest_green": "#2F6B3E",
    "slate": "#4A5568",
    "mauve": "#8B6B8B",
    "light_gray": "#E2E8F0",
    "off_white": "#F7FAFC",
}

PHASES = [
    "AE Detection (Sensor / Self-Report)",
    "Per-Site Claude Opus Triage",
    "H2 Bedside Dispatch (90 s SLA)",
    "CTCAE Grading (HR 9505 1 h)",
    "On-Call Physician Activation",
    "Cross-Site Transit (Drone / Charter)",
    "Cross-Site H2 Re-Dispatch",
    "Sponsor Acknowledgment (HR 9505 1 h)",
    "MedDRA Coding and Submission",
    "Audit Reconciliation across 4 Sites",
]

FRAMEWORKS = [
    "21 CFR § 312",
    "21 CFR § 314.80",
    "21 CFR § 50",
    "ICH E2A",
    "ICH E2D",
    "ICH E6(R3)",
    "IEC 80601-2-77",
    "MedDRA",
    "CTCAE v5.0",
    "HR 9504",
    "HR 9505",
    "HIPAA 45 CFR § 164.514(b)",
    "FDA RTCT 2026",
    "FAA Part 135",
]

SITES = ["SF-01", "SD-01", "BO-01", "AT-01"]


def main(out_path: pathlib.Path) -> None:
    rng = np.random.default_rng(7)
    n_phase = len(PHASES)
    n_fw = len(FRAMEWORKS)

    main_grid = rng.uniform(0.62, 0.99, size=(n_phase, n_fw))
    main_grid[3, 10] = 0.998  # CTCAE x HR 9505
    main_grid[7, 10] = 0.998
    main_grid[3, 8] = 0.995
    main_grid[5, 13] = 0.987  # transit x FAA
    main_grid[9, 11] = 0.997  # audit x HIPAA
    main_grid[1, 7] = 0.93  # triage x MedDRA
    main_grid[0, 6] = 0.88  # detection x IEC

    site_grid = rng.uniform(0.85, 0.999, size=(4, n_fw))
    site_grid[:, 10] = [0.998, 0.997, 0.998, 0.996]
    site_grid[:, 8] = [0.995, 0.993, 0.997, 0.994]
    site_grid[:, 13] = [0.989, 0.971, 0.982, 0.985]

    fig = plt.figure(figsize=(11.0, 8.5), facecolor="white")

    fig.text(
        0.045,
        0.965,
        "3x H2 + Per-Site Claude Opus 4.7 1M AE Response Compliance Matrix",
        fontsize=15,
        ha="left",
        color="black",
        fontweight="bold",
    )
    fig.text(
        0.045,
        0.940,
        "10 AE Response Phases x 14 Frameworks, PAT-NET-001 4-Site Network, 168-Hour Cycle",
        fontsize=10,
        ha="left",
        color=PALETTE["slate"],
    )
    fig.text(0.955, 0.915, "Demo 07 / Image 03 of 10 / Landscape", fontsize=8.5, ha="right", color=PALETTE["slate"])

    main_ax = fig.add_axes([0.27, 0.40, 0.58, 0.48])
    sub_ax = fig.add_axes([0.27, 0.20, 0.58, 0.105])
    cbar_ax = fig.add_axes([0.87, 0.40, 0.018, 0.48])

    cmap = LinearSegmentedColormap.from_list(
        "compliance",
        [PALETTE["burgundy"], PALETTE["gold"], PALETTE["forest_green"], PALETTE["deep_navy"]],
    )

    im_main = main_ax.imshow(main_grid, cmap=cmap, vmin=0.6, vmax=1.0, aspect="auto")
    main_ax.set_xticks([])
    main_ax.set_xticklabels([])
    main_ax.tick_params(axis="x", length=0, pad=2)
    main_ax.set_yticks(np.arange(n_phase))
    main_ax.set_yticklabels(PHASES, fontsize=8.0, color="black")
    main_ax.tick_params(axis="y", length=0, pad=2)

    for i in range(n_phase):
        for j in range(n_fw):
            val = main_grid[i, j]
            txt_color = "white" if val < 0.78 or val > 0.95 else "black"
            main_ax.text(j, i, f"{val * 100:.0f}", ha="center", va="center", fontsize=6.0, color=txt_color)

    for col in [8, 10]:
        main_ax.add_patch(
            plt.Rectangle(
                (col - 0.5, -0.5),
                1.0,
                n_phase,
                fill=False,
                ec="black",
                lw=2.2,
            )
        )

    main_ax.set_xticks(np.arange(-0.5, n_fw, 1), minor=True)
    main_ax.set_yticks(np.arange(-0.5, n_phase, 1), minor=True)
    main_ax.grid(which="minor", color="white", lw=0.6)
    main_ax.tick_params(which="minor", length=0)

    sub_ax.imshow(site_grid, cmap=cmap, vmin=0.6, vmax=1.0, aspect="auto")
    sub_ax.set_xticks(np.arange(n_fw))
    sub_ax.set_xticklabels(FRAMEWORKS, rotation=40, ha="right", fontsize=7.5, color="black")
    sub_ax.set_yticks(np.arange(4))
    sub_ax.set_yticklabels(SITES, fontsize=8.0, color="black", fontweight="bold")
    sub_ax.tick_params(axis="both", length=0, pad=2)
    for i in range(4):
        for j in range(n_fw):
            val = site_grid[i, j]
            txt_color = "white" if val < 0.78 or val > 0.95 else "black"
            sub_ax.text(j, i, f"{val * 100:.1f}", ha="center", va="center", fontsize=5.8, color=txt_color)
    for col in [8, 10]:
        sub_ax.add_patch(
            plt.Rectangle(
                (col - 0.5, -0.5),
                1.0,
                4,
                fill=False,
                ec="black",
                lw=2.0,
            )
        )
    sub_ax.set_xticks(np.arange(-0.5, n_fw, 1), minor=True)
    sub_ax.set_yticks(np.arange(-0.5, 4, 1), minor=True)
    sub_ax.grid(which="minor", color="white", lw=0.6)
    sub_ax.tick_params(which="minor", length=0)

    fig.text(
        0.27,
        0.325,
        "Per-Site Posture (4 sites x 14 frameworks)",
        fontsize=9.0,
        color=PALETTE["slate"],
        fontweight="bold",
    )

    cbar = fig.colorbar(im_main, cax=cbar_ax)
    cbar.set_label("Compliance Posture (percent of cases meeting framework)", fontsize=8.5, color=PALETTE["slate"])
    cbar.ax.tick_params(labelsize=7.5)
    cbar.set_ticks([0.6, 0.7, 0.8, 0.9, 1.0])
    cbar.set_ticklabels(["60", "70", "80", "90", "100"])

    callout = (
        "Callout: H2 per-site dispatch consistently meets the 90 s SLA. Cross-site transit relies on FAA Part 135.\n"
        "HR 9505 and CTCAE v5.0 are outlined as the 2 critical compliance columns."
    )
    fig.text(
        0.5,
        0.087,
        callout,
        fontsize=7.5,
        color="black",
        ha="center",
        va="center",
        bbox=dict(boxstyle="round,pad=0.45", fc=PALETTE["off_white"], ec=PALETTE["slate"], lw=0.8),
    )

    fig.text(
        0.045,
        0.045,
        "Clinical-AI-Demos v0.8.0 / Demo 07 Adverse Event Response",
        fontsize=7.8,
        ha="left",
        color=PALETTE["slate"],
    )
    fig.text(
        0.955, 0.045, "DOI: 10.5281/zenodo.18445179 / MIT License", fontsize=7.8, ha="right", color=PALETTE["slate"]
    )

    fig.savefig(out_path, dpi=300, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    out = pathlib.Path(__file__).with_suffix(".png")
    main(out)
    print(f"Saved {out}")
