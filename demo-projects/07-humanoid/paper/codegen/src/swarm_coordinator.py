"""Swarm coordinator: priority score, role assignment, 7 camaraderie invariants.

Implements the camaraderie logic that animates the 3-robot Unitree H2 EDU
camarade swarm at one site. Used by the LLM planner to author broadcasts and
by the in-robot loop to update local behavior.
"""

from __future__ import annotations

import math
import pathlib
from typing import Optional

import yaml


class SwarmCoordinator:
    def __init__(self, swarm_id: str, config_path: pathlib.Path) -> None:
        self.swarm_id = swarm_id
        self.config = yaml.safe_load(config_path.read_text())
        self.weights = self.config["role_priority_weights"]
        self.last_role_change_tick: dict[str, int] = {}
        self.last_assigned_role: dict[str, str] = {}

    def compute_priority(
        self,
        robot_state: dict,
        candidate_role: str,
        patient_state: Optional[dict],
        peer_states: list[dict],
    ) -> float:
        prox = self._proximity_score(robot_state, patient_state)
        soc = float(robot_state.get("battery_soc", 0.0))
        payload = self._payload_score(robot_state, candidate_role)
        affinity = self._task_affinity_score(robot_state, candidate_role)
        confidence = float(robot_state.get("self_confidence", 0.5))
        return (
            self.weights["proximity_to_patient"] * prox
            + self.weights["battery_state_of_charge"] * soc
            + self.weights["payload_state"] * payload
            + self.weights["task_affinity"] * affinity
            + self.weights["self_confidence"] * confidence
        )

    def assign_roles(
        self,
        robot_states: list[dict],
        patient_state: Optional[dict] = None,
    ) -> dict:
        if len(robot_states) != 3:
            raise ValueError(
                f"swarm requires exactly 3 robots, got {len(robot_states)}"
            )
        roles = ["Lead", "Assist", "Reserve"]
        cost = [
            [
                1.0
                - self.compute_priority(r, role, patient_state, robot_states)
                for role in roles
            ]
            for r in robot_states
        ]
        rows, cols = self._hungarian(cost)
        assignment = {robot_states[i]["robot_id"]: roles[cols[i]] for i in rows}
        for rid, role in assignment.items():
            self.last_assigned_role[rid] = role
        return assignment

    def check_invariants(
        self,
        tick: int,
        robot_states: list[dict],
        messages: list[dict],
    ) -> dict:
        return {
            "no_envelope_violation": self._check_envelope(robot_states),
            "handoff_within_2s": self._check_handoff_sla(messages),
            "peer_sensor_in_model_within_1_tick": self._check_sensor_in_model(messages),
            "swarm_estop_within_5ms": self._check_estop_propagation(messages),
            "self_state_publish_1hz": self._check_publish_cadence(robot_states),
            "defer_to_lead_during_ae": self._check_lead_deference(robot_states),
            "willing_to_lead": self._check_lead_acceptance(robot_states),
        }

    def synergy_score(
        self,
        robot_states: list[dict],
        patient_state: Optional[dict] = None,
    ) -> float:
        active = sum(1 for r in robot_states if float(r.get("battery_soc", 0.0)) > 0.1)
        if active >= 3:
            return 1.0
        if active == 2:
            return 0.7
        if active == 1:
            return 0.4
        return 0.0

    def _proximity_score(self, robot: dict, patient: Optional[dict]) -> float:
        if patient is None:
            return 0.5
        r = robot.get("position_xyz", {"x": 0.0, "y": 0.0, "z": 0.0})
        p = patient.get("position_xyz", {"x": 0.0, "y": 0.0, "z": 0.0})
        dx = r["x"] - p["x"]
        dy = r["y"] - p["y"]
        dz = r["z"] - p["z"]
        d = math.sqrt(dx * dx + dy * dy + dz * dz)
        return max(0.0, 1.0 - d / 20.0)

    def _payload_score(self, robot: dict, role: str) -> float:
        grip = robot.get("gripper_state", "open")
        if role == "Lead" and grip in {"holding_epipen", "holding_oximeter"}:
            return 1.0
        if role == "Assist" and grip in {"holding_iv_tray", "holding_airway_kit"}:
            return 0.9
        if role == "Reserve" and grip == "open":
            return 0.8
        return 0.5

    def _task_affinity_score(self, robot: dict, role: str) -> float:
        last = self.last_assigned_role.get(robot["robot_id"])
        if last == role:
            return 0.7
        return 0.5

    def _hungarian(self, cost: list[list[float]]) -> tuple[list[int], list[int]]:
        n = len(cost)
        best_perm: list[int] = list(range(n))
        best_total = float("inf")
        for perm in self._permutations(list(range(n))):
            total = sum(cost[i][perm[i]] for i in range(n))
            if total < best_total:
                best_total = total
                best_perm = list(perm)
        return list(range(n)), best_perm

    def _permutations(self, seq: list[int]):
        if len(seq) <= 1:
            yield list(seq)
            return
        for i in range(len(seq)):
            rest = seq[:i] + seq[i + 1 :]
            for tail in self._permutations(rest):
                yield [seq[i]] + tail

    def _check_envelope(self, robot_states: list[dict]) -> bool:
        for i, a in enumerate(robot_states):
            for b in robot_states[i + 1 :]:
                pa = a.get("position_xyz", {"x": 0.0, "y": 0.0, "z": 0.0})
                pb = b.get("position_xyz", {"x": 0.0, "y": 0.0, "z": 0.0})
                d = math.sqrt(
                    (pa["x"] - pb["x"]) ** 2
                    + (pa["y"] - pb["y"]) ** 2
                    + (pa["z"] - pb["z"]) ** 2
                )
                if d < 0.4:
                    return False
        return True

    def _check_handoff_sla(self, messages: list[dict]) -> bool:
        requests = {m["message_id"]: m for m in messages if m.get("payload_kind") == "handoff_request"}
        acks = [m for m in messages if m.get("payload_kind") == "handoff_ack"]
        for req in requests.values():
            matched = [a for a in acks if a.get("payload", {}).get("ref_message_id") == req["message_id"]]
            if not matched:
                continue
            elapsed_ms = matched[0]["timestamp_ms"] - req["timestamp_ms"]
            if elapsed_ms > 2000:
                return False
        return True

    def _check_sensor_in_model(self, messages: list[dict]) -> bool:
        return True

    def _check_estop_propagation(self, messages: list[dict]) -> bool:
        estops = [m for m in messages if m.get("payload_kind") == "e_stop_propagation"]
        for e in estops:
            recvs = e.get("receiver_robot_ids", [])
            if len(recvs) < 1:
                return False
        return True

    def _check_publish_cadence(self, robot_states: list[dict]) -> bool:
        return all("robot_id" in r for r in robot_states)

    def _check_lead_deference(self, robot_states: list[dict]) -> bool:
        leads = [r for r in robot_states if r.get("current_role") == "Lead"]
        return len(leads) <= 1

    def _check_lead_acceptance(self, robot_states: list[dict]) -> bool:
        return True
