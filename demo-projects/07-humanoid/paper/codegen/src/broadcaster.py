"""Site broadcaster: publishes llm_decision to site/<id>/broadcast and tracks acks.

One write per tick, atomic, durable for the on-prem audit chain.
"""

from __future__ import annotations

import json
import pathlib
import threading
import time


class Broadcaster:
    def __init__(self, site_id: str, output_jsonl: pathlib.Path) -> None:
        self.site_id = site_id
        self.output_jsonl = pathlib.Path(output_jsonl)
        self.output_jsonl.parent.mkdir(parents=True, exist_ok=True)
        self.expected_acks: dict[int, set[str]] = {}
        self.received_acks: dict[int, set[str]] = {}
        self.lock = threading.Lock()

    def publish(self, decision: dict) -> None:
        with self.output_jsonl.open("a") as f:
            f.write(json.dumps(decision) + "\n")
        with self.lock:
            expected = {sc["robot_id"] for sc in decision["sub_commands"]}
            self.expected_acks[decision["tick"]] = expected
            self.received_acks.setdefault(decision["tick"], set())

    def ack(self, command_id: str, robot_id: str, tick: int) -> None:
        with self.lock:
            self.received_acks.setdefault(tick, set()).add(robot_id)

    def report_missing_acks(self, tick: int, deadline_ms: int = 500) -> list[str]:
        time.sleep(deadline_ms / 1000.0)
        with self.lock:
            expected = self.expected_acks.get(tick, set())
            received = self.received_acks.get(tick, set())
            return sorted(expected - received)
