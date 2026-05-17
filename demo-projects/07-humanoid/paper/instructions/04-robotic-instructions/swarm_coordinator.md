# Authoring Instructions for `src/swarm_coordinator.py`

The future session writes this Python module during Commit 3 of 7. It is the heart of the camaraderie logic.

## Purpose

Implements the priority score for role rotation, the peer-aware policy adapter, and the camaraderie invariants checker. Used by the LLM planner to author the next broadcast and by the in-robot loop to update local behavior.

## Key Behavior

- Accepts the 3 robots in a swarm plus the patient state plus the doctor state.
- Computes the priority score for each (robot, role) pair.
- Returns the assignment that maximizes the total swarm priority via Hungarian bipartite match.
- Enforces a 3 second minimum role dwell and a 5 second cool-down between consecutive rotations of the same robot.
- Checks the 7 camaraderie invariants every tick and emits a `camaraderie_invariants_pass_rate` metric.

## Required Interfaces

```
class SwarmCoordinator:
    def __init__(self, swarm_id: str, config_path: pathlib.Path) -> None: ...
    def compute_priority(self, robot_state: dict, candidate_role: str, patient_state: dict, peer_states: list[dict]) -> float: ...
    def assign_roles(self, robot_states: list[dict], patient_state: dict) -> dict: ...
    def check_invariants(self, tick: int, robot_states: list[dict], messages: list[dict]) -> dict: ...
    def synergy_score(self, robot_states: list[dict], patient_state: dict) -> float: ...
```

## Camarade Invariants Implemented Here

The 7 invariants from `00-project-overview/swarm-overview.md` are encoded in `check_invariants`:

1. No envelope violation: for each peer pair, current pose plus 2 second motion projection does not overlap unless a handoff is in progress.
2. Hand-off within 2 seconds: every `handoff_request` message must have a matching `handoff_ack` within 2 seconds.
3. Peer-reported sensor reading in world model within 1 tick: every `sensor_share` message must be present in the world model by the next tick.
4. Swarm-wide E-stop within 5 ms: every `e_stop_propagation` message must reach all 2 peers within 5 ms.
5. Self-state publish at 1 Hz: every robot must publish a `robot_camarade_state` record at most 1100 ms apart.
6. Defer to Lead during AE: during an active AE, Assist and Reserve must not enter the patient's 1.0 m radius without a Lead-issued handoff.
7. Willing to lead when asked: a robot designated as Lead must not decline the role; if it declines, the invariant fails.

Each invariant returns a boolean for the current tick. The pass rate is the sum of true divided by 7.

## Suggested Skeleton

```
import pathlib
import math


class SwarmCoordinator:
    def __init__(self, swarm_id: str, config_path: pathlib.Path) -> None:
        import yaml
        self.swarm_id = swarm_id
        self.config = yaml.safe_load(config_path.read_text())
        self.weights = self.config["role_priority_weights"]
        self.last_role_change_tick = {}

    def compute_priority(self, robot_state, candidate_role, patient_state, peer_states):
        prox = self._proximity_score(robot_state, patient_state)
        soc = robot_state["battery_soc"]
        payload = self._payload_score(robot_state, candidate_role)
        affinity = self._task_affinity_score(robot_state, candidate_role)
        confidence = robot_state.get("self_confidence", 0.5)
        return (
            self.weights["proximity_to_patient"] * prox
            + self.weights["battery_state_of_charge"] * soc
            + self.weights["payload_state"] * payload
            + self.weights["task_affinity"] * affinity
            + self.weights["self_confidence"] * confidence
        )

    def assign_roles(self, robot_states, patient_state):
        roles = ["Lead", "Assist", "Reserve"]
        cost = [[1.0 - self.compute_priority(r, role, patient_state, robot_states) for role in roles] for r in robot_states]
        from scipy.optimize import linear_sum_assignment
        rows, cols = linear_sum_assignment(cost)
        return {robot_states[i]["robot_id"]: roles[cols[i]] for i in rows}

    def check_invariants(self, tick, robot_states, messages):
        return {
            "no_envelope_violation": self._check_envelope(robot_states),
            "handoff_within_2s": self._check_handoff_sla(messages),
            "peer_sensor_in_model_within_1_tick": self._check_sensor_in_model(messages),
            "swarm_estop_within_5ms": self._check_estop_propagation(messages),
            "self_state_publish_1hz": self._check_publish_cadence(robot_states),
            "defer_to_lead_during_ae": self._check_lead_deference(robot_states),
            "willing_to_lead": self._check_lead_acceptance(robot_states),
        }

    def synergy_score(self, robot_states, patient_state):
        # estimate of swarm benefit over single robot
        active = sum(1 for r in robot_states if r["battery_soc"] > 0.1)
        if active == 3:
            return 1.0
        if active == 2:
            return 0.7
        return 0.4

    def _proximity_score(self, robot, patient):
        if patient is None:
            return 0.5
        dx = robot["position_xyz"]["x"] - patient["position_xyz"]["x"]
        dy = robot["position_xyz"]["y"] - patient["position_xyz"]["y"]
        dz = robot["position_xyz"]["z"] - patient["position_xyz"]["z"]
        d = math.sqrt(dx * dx + dy * dy + dz * dz)
        return max(0.0, 1.0 - d / 20.0)

    def _payload_score(self, robot, role):
        if role == "Lead" and robot.get("gripper_state", "open") == "holding_epipen":
            return 1.0
        return 0.5

    def _task_affinity_score(self, robot, role):
        return 0.5  # populated by history in commit 4

    def _check_envelope(self, robot_states):
        return True

    def _check_handoff_sla(self, messages):
        return True

    def _check_sensor_in_model(self, messages):
        return True

    def _check_estop_propagation(self, messages):
        return True

    def _check_publish_cadence(self, robot_states):
        return True

    def _check_lead_deference(self, robot_states):
        return True

    def _check_lead_acceptance(self, robot_states):
        return True
```

## Validation Rules

- Role priority weights sum to 1.0.
- Assignment is a valid bipartite match (each robot to one unique role).
- Pass rate is between 0.0 and 1.0.

## Notes

- `scipy.optimize.linear_sum_assignment` is the standard Hungarian algorithm implementation. It is `O(n^3)` but n=3 is trivial.
- The `_check_*` helper methods are stubs in commit 3 and are filled in commit 4.
- The invariant checker is exercised in `tests/test_swarm_invariants.py` in commit 6.
