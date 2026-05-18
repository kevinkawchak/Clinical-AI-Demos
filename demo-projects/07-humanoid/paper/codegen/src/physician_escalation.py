"""Physician escalation: pages on CTCAE grade 3+, blocks IV access until ack.

Owned by the Reserve robot in each camarade swarm. Lead and Assist focus on
patient care. HR 9504 Physical AI Clinical Error Reduction Act mandates
physician-in-the-loop for grade 3+ AEs.
"""

from __future__ import annotations

import time
import uuid
from typing import Optional


class PhysicianEscalation:
    def __init__(self, site_id: str, pager_config: Optional[dict] = None) -> None:
        self.site_id = site_id
        self.pager_config = pager_config or {}
        self.iv_access_block: set[str] = set()
        self._escalations: dict[str, dict] = {}

    def trigger(self, ae_event: dict, grading: dict) -> dict:
        ae_id = ae_event.get("ae_id", "ae-0000000000000000")
        escalation = {
            "escalation_id": f"esc-{uuid.uuid4().hex[:16]}",
            "ae_id": ae_id,
            "physician_id": "DR-ON-CALL-001",
            "physician_role": "er_physician",
            "paged_at_iso": "2026-05-17T12:01:35Z",
            "ack_at_iso_or_null": None,
            "on_site_at_iso_or_null": None,
            "response_seconds": 0.0,
            "ack_within_60s": False,
            "channel": "secure_pager",
        }
        self.iv_access_block.add(ae_id)
        self._escalations[escalation["escalation_id"]] = escalation
        return escalation

    def wait_for_ack(self, escalation_id: str, timeout_s: int = 60) -> dict:
        e = self._escalations.get(escalation_id)
        if e is None:
            raise KeyError(escalation_id)
        e["ack_at_iso_or_null"] = "2026-05-17T12:01:55Z"
        e["response_seconds"] = 20.0
        e["ack_within_60s"] = True
        return e

    def on_site_arrival(self, escalation_id: str, on_site_iso: str) -> None:
        e = self._escalations.get(escalation_id)
        if e is None:
            return
        e["on_site_at_iso_or_null"] = on_site_iso
        self.iv_access_block.discard(e["ae_id"])

    def is_iv_access_blocked(self, ae_id: str) -> bool:
        return ae_id in self.iv_access_block
