"""Image 07-08: AE Detection to Sponsor Acknowledgment Funnel.

Letter portrait, 8.5 x 11.0 inches, 300 dpi. Vertical 7-stage trapezoidal
funnel covering the AE event lifecycle from detection through to audit
reconciliation. Filter rules left, pass-rate right.
"""

from __future__ import annotations

import pathlib

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt

PALETTE = {
    "deep_navy": "#1F3A68",
    "teal": "#2E8B8B",
    "burgundy": "#8B2E3F",
    "burgundy_dk": "#5A1E2A",
    "gold": "#C18A2C",
    "forest_green": "#2F6B3E",
    "slate": "#4A5568",
    "mauve": "#8B6B8B",
    "light_gray": "#E2E8F0",
    "off_white": "#F7FAFC",
}

STAGES = [
    ("AE Events Detected", 84, PALETTE["burgundy"], "Sensor + Self-Report Inbound", "100%"),
    ("Per-Site Claude Opus Triage Pass", 82, PALETTE["teal"], "1 Hz LLM triage rule pass", "97.6%"),
    ("H2 Bedside Arrival under 90 s", 79, PALETTE["deep_navy"], "Cartesian dispatch under SLA", "94.0%"),
    ("CTCAE Grading under 1 h (HR 9505)", 78, PALETTE["gold"], "CTCAE v5.0 + swarm consensus", "92.8%"),
    ("On-Call Physician Acknowledged", 60, PALETTE["burgundy"], "Grade 3+ pager activation", "71.4%"),
    ("Sponsor Acknowledged under 1 h", 60, PALETTE["burgundy_dk"], "HR 9505 sponsor pager + log", "71.4%"),
    ("AE Closed + Audit Reconciled", 82, PALETTE["forest_green"], "Hash chain + 4-site reconcile", "97.6%"),
]


def main(out_path: pathlib.Path) -> None:
    fig = plt.figure(figsize=(8.5, 11.0), facecolor="white")
    fig.text(
        0.06,
        0.975,
        "3x H2 + Per-Site Claude Opus AE Lifecycle Funnel",
        fontsize=13.0,
        ha="left",
        color="black",
        fontweight="bold",
    )
    fig.text(
        0.06,
        0.957,
        "Detection to Sponsor Acknowledgment",
        fontsize=11.0,
        ha="left",
        color=PALETTE["slate"],
        fontweight="bold",
    )
    fig.text(
        0.06,
        0.940,
        "168-Hour Cycle, 4-Site Network, Reference v0.8.0",
        fontsize=8.8,
        ha="left",
        color=PALETTE["slate"],
    )
    fig.text(0.94, 0.948, "Demo 07 / Image 08 of 10 / Portrait", fontsize=8.5, ha="right", color=PALETTE["slate"])

    ax = fig.add_axes([0.04, 0.10, 0.92, 0.82])
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 11)
    ax.set_axis_off()

    n = len(STAGES)
    max_count = max(s[1] for s in STAGES)
    base_w = 5.4
    top_y = 9.5
    bot_y = 1.0
    stage_h = (top_y - bot_y) / n

    fig.text(
        0.21,
        0.91,
        "Filter Rule",
        fontsize=9.5,
        color=PALETTE["slate"],
        fontweight="bold",
        ha="right",
    )
    fig.text(
        0.80,
        0.91,
        "Pass Rate",
        fontsize=9.5,
        color=PALETTE["slate"],
        fontweight="bold",
        ha="left",
    )

    x_center = 5.0
    prev_top_w = base_w
    prev_y = top_y

    for i, (name, count, color, rule, rate) in enumerate(STAGES):
        next_count = STAGES[i + 1][1] if i + 1 < n else count
        w_top = base_w * count / max_count
        w_bot = base_w * next_count / max_count
        if i == n - 1:
            w_bot = w_top * 0.92
        y_top_seg = top_y - i * stage_h
        y_bot_seg = y_top_seg - stage_h * 0.86
        x_left_top = x_center - w_top / 2
        x_right_top = x_center + w_top / 2
        x_left_bot = x_center - w_bot / 2
        x_right_bot = x_center + w_bot / 2

        poly = plt.Polygon(
            [
                (x_left_top, y_top_seg),
                (x_right_top, y_top_seg),
                (x_right_bot, y_bot_seg),
                (x_left_bot, y_bot_seg),
            ],
            fc=color,
            ec="white",
            lw=2.0,
            alpha=0.90,
        )
        ax.add_patch(poly)
        ax.text(
            x_center,
            (y_top_seg + y_bot_seg) / 2 + 0.05,
            name,
            ha="center",
            va="center",
            fontsize=9.5,
            color="white",
            fontweight="bold",
        )
        ax.text(
            x_center,
            (y_top_seg + y_bot_seg) / 2 - 0.18,
            f"{count} events",
            ha="center",
            va="center",
            fontsize=8.5,
            color="white",
        )

        ax.plot(
            [1.95, x_left_top - 0.08],
            [(y_top_seg + y_bot_seg) / 2, (y_top_seg + y_bot_seg) / 2],
            color=PALETTE["light_gray"],
            lw=0.7,
        )
        ax.text(
            1.85,
            (y_top_seg + y_bot_seg) / 2,
            rule,
            ha="right",
            va="center",
            fontsize=7.5,
            color=PALETTE["slate"],
        )

        ax.plot(
            [x_right_top + 0.08, 8.10],
            [(y_top_seg + y_bot_seg) / 2, (y_top_seg + y_bot_seg) / 2],
            color=PALETTE["light_gray"],
            lw=0.7,
        )
        ax.text(
            8.20,
            (y_top_seg + y_bot_seg) / 2,
            rate,
            ha="left",
            va="center",
            fontsize=10.0,
            color=color,
            fontweight="bold",
        )

    bottom_note = (
        "Note: Approximately 60 to 90 AE events per week network-wide.\n"
        "About 95% close within HR 9505 1-hour cumulative SLA at v0.8.0 reference.\n"
        "Re-entry from Sponsor Ack to AE Closed reflects the audit reconcile loop."
    )
    fig.text(
        0.5,
        0.062,
        bottom_note,
        fontsize=7.6,
        color="black",
        ha="center",
        va="center",
        bbox=dict(boxstyle="round,pad=0.40", fc=PALETTE["off_white"], ec=PALETTE["slate"], lw=0.8),
    )

    fig.text(
        0.06,
        0.012,
        "Clinical-AI-Demos v0.8.0 / Demo 07 Adverse Event Response",
        fontsize=7.3,
        ha="left",
        color=PALETTE["slate"],
    )
    fig.text(
        0.94, 0.012, "DOI: 10.5281/zenodo.18445179 / MIT License", fontsize=7.3, ha="right", color=PALETTE["slate"]
    )

    fig.savefig(out_path, dpi=300, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    out = pathlib.Path(__file__).with_suffix(".png")
    main(out)
    print(f"Saved {out}")
