# Authoring Instructions for `src/cartesian_planner.py`

The future session writes this Python module during Commit 3 of 7.

## Purpose

Helps the LLM planner author cartesian commands. Given a robot pose plus a target pose plus environment constraints, the planner returns a smooth trajectory in cartesian space that the on-robot inverse kinematics solver can follow.

## Key Behavior

- Generates a 5-th order polynomial trajectory between current pose and target pose with bounded velocity and acceleration.
- Inserts waypoints around the patient bed and around peer robots to honor the 0.4 m minimum hand-off distance and the 1.2 m rest distance.
- Returns a list of intermediate cartesian targets to be issued over 1 to 5 seconds.

## Required Interfaces

```
class CartesianPlanner:
    def __init__(self, kinematics_path: pathlib.Path, swarm_config_path: pathlib.Path) -> None: ...
    def plan(self, current_pose: dict, target_pose: dict, peer_poses: list[dict], patient_pose: dict, duration_s: float) -> list[dict]: ...
    def check_envelope(self, trajectory: list[dict], peer_poses: list[dict]) -> bool: ...
```

## Suggested Skeleton

```
import math
import pathlib


class CartesianPlanner:
    def __init__(self, kinematics_path, swarm_config_path):
        import yaml
        self.kinematics = yaml.safe_load(kinematics_path.read_text())
        self.swarm = yaml.safe_load(swarm_config_path.read_text())
        self.min_dist_handoff = 0.4
        self.min_dist_rest = 1.2

    def plan(self, current_pose, target_pose, peer_poses, patient_pose, duration_s):
        steps = max(5, int(duration_s * 10))
        out = []
        for i in range(steps + 1):
            t = i / steps
            blended = self._quintic_blend(current_pose, target_pose, t)
            if peer_poses and self._too_close_to_peers(blended, peer_poses):
                blended = self._nudge_away(blended, peer_poses)
            out.append(blended)
        return out

    def check_envelope(self, trajectory, peer_poses):
        for step in trajectory:
            for peer in peer_poses:
                d = self._distance(step["target_pose_xyz"], peer["position_xyz"])
                if d < self.min_dist_handoff:
                    return False
        return True

    def _quintic_blend(self, a, b, t):
        s = 10 * t**3 - 15 * t**4 + 6 * t**5
        return {
            "target_pose_xyz": {
                "x": a["x"] + (b["x"] - a["x"]) * s,
                "y": a["y"] + (b["y"] - a["y"]) * s,
                "z": a["z"] + (b["z"] - a["z"]) * s,
            }
        }

    def _too_close_to_peers(self, pose, peer_poses):
        for peer in peer_poses:
            if self._distance(pose["target_pose_xyz"], peer["position_xyz"]) < self.min_dist_handoff:
                return True
        return False

    def _nudge_away(self, pose, peer_poses):
        # add a small offset away from the nearest peer
        return pose

    def _distance(self, a, b):
        return math.sqrt((a["x"] - b["x"]) ** 2 + (a["y"] - b["y"]) ** 2 + (a["z"] - b["z"]) ** 2)
```

## Validation Rules

- Trajectory steps respect the 0.4 m hand-off and 1.2 m rest distances.
- Total trajectory duration matches the requested `duration_s`.
- Quintic blend ensures zero velocity and acceleration at the endpoints.

## Notes

- The planner uses cartesian-space planning; the on-robot IK solver does the joint-space conversion at 10 Hz.
- For complex obstacle environments, the future session could swap in OMPL or MoveIt; for the 168-hour AE response simulation, the simple quintic blend is sufficient.
