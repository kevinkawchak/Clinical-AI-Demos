"""Central on-prem Claude Code compute bus.

Passive observer of the 4 sites. Receives de-identified hourly summary posts,
validates PHI absence, writes to a shared DuckDB store. NEVER writes to a
robot.
"""

from __future__ import annotations

import json
import pathlib
from typing import Optional


REQUIRED_FIELDS = {
    "site_id",
    "hour_iso",
    "ae_count_by_grade",
    "response_time_p50_seconds",
    "response_time_p95_seconds",
    "escalation_count",
    "fda_rtct_1hr_compliance_rate",
    "swarm_uptime_percent",
    "peer_handoff_p95_seconds",
    "camaraderie_invariants_pass_rate",
    "fleet_battery_p10_percent",
}

PHI_BLOCKLIST = {"patient_id", "patient_name", "dob", "address", "ssn", "mrn"}


class CrossSiteBus:
    def __init__(self, output_path: Optional[pathlib.Path] = None) -> None:
        self.output_path = (
            output_path
            or pathlib.Path(__file__).resolve().parent.parent
            / "data"
            / "cross_site_summary.jsonl"
        )
        self.output_path.parent.mkdir(parents=True, exist_ok=True)
        self.received: list[dict] = []

    def receive_summary(self, summary: dict) -> tuple[bool, str]:
        missing = REQUIRED_FIELDS - set(summary.keys())
        if missing:
            return False, f"missing fields: {sorted(missing)}"
        phi_present = PHI_BLOCKLIST & set(summary.keys())
        if phi_present:
            return False, f"phi_egress forbidden: {sorted(phi_present)} present"
        self.received.append(summary)
        with self.output_path.open("a") as f:
            f.write(json.dumps(summary) + "\n")
        return True, "ok"

    def query(self, site_id: Optional[str] = None) -> list[dict]:
        if site_id is None:
            return list(self.received)
        return [s for s in self.received if s.get("site_id") == site_id]
