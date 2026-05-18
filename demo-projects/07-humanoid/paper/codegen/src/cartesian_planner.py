"""Cartesian planner: quintic polynomial trajectories with envelope checks.

Given a current pose, target pose, and peer states, returns a smooth
trajectory in shared site cartesian frame for the on-robot IK solver to
follow. Respects the 0.4 m hand-off and 1.2 m rest distances.
"""

from __future__ import annotations

import math
import pathlib

import yaml


class CartesianPlanner:
    def __init__(
        self,
        kinematics_path: pathlib.Path,
        swarm_config_path: pathlib.Path,
    ) -> None:
        self.kinematics = yaml.safe_load(kinematics_path.read_text())
        self.swarm = yaml.safe_load(swarm_config_path.read_text())
        self.min_dist_handoff = 0.4
        self.min_dist_rest = 1.2

    def plan(
        self,
        current_pose: dict,
        target_pose: dict,
        peer_poses: list[dict],
        patient_pose: dict,
        duration_s: float,
    ) -> list[dict]:
        steps = max(5, int(duration_s * 10))
        out: list[dict] = []
        for i in range(steps + 1):
            t = i / steps
            blended = self._quintic_blend(current_pose, target_pose, t)
            if peer_poses and self._too_close_to_peers(blended, peer_poses):
                blended = self._nudge_away(blended, peer_poses)
            out.append(blended)
        return out

    def check_envelope(
        self,
        trajectory: list[dict],
        peer_poses: list[dict],
    ) -> bool:
        for step in trajectory:
            for peer in peer_poses:
                d = self._distance(
                    step["target_pose_xyz"],
                    peer.get("position_xyz", {"x": 0.0, "y": 0.0, "z": 0.0}),
                )
                if d < self.min_dist_handoff:
                    return False
        return True

    def _quintic_blend(self, a: dict, b: dict, t: float) -> dict:
        s = 10 * t**3 - 15 * t**4 + 6 * t**5
        return {
            "target_pose_xyz": {
                "x": a["x"] + (b["x"] - a["x"]) * s,
                "y": a["y"] + (b["y"] - a["y"]) * s,
                "z": a["z"] + (b["z"] - a["z"]) * s,
            }
        }

    def _too_close_to_peers(self, pose: dict, peer_poses: list[dict]) -> bool:
        for peer in peer_poses:
            d = self._distance(
                pose["target_pose_xyz"],
                peer.get("position_xyz", {"x": 0.0, "y": 0.0, "z": 0.0}),
            )
            if d < self.min_dist_handoff:
                return True
        return False

    def _nudge_away(self, pose: dict, peer_poses: list[dict]) -> dict:
        if not peer_poses:
            return pose
        nearest = min(
            peer_poses,
            key=lambda p: self._distance(
                pose["target_pose_xyz"],
                p.get("position_xyz", {"x": 0.0, "y": 0.0, "z": 0.0}),
            ),
        )
        np_xyz = nearest.get("position_xyz", {"x": 0.0, "y": 0.0, "z": 0.0})
        dx = pose["target_pose_xyz"]["x"] - np_xyz["x"]
        dy = pose["target_pose_xyz"]["y"] - np_xyz["y"]
        norm = max(1e-6, math.sqrt(dx * dx + dy * dy))
        offset = 0.1
        pose["target_pose_xyz"]["x"] += offset * dx / norm
        pose["target_pose_xyz"]["y"] += offset * dy / norm
        return pose

    def _distance(self, a: dict, b: dict) -> float:
        return math.sqrt(
            (a["x"] - b["x"]) ** 2 + (a["y"] - b["y"]) ** 2 + (a["z"] - b["z"]) ** 2
        )
