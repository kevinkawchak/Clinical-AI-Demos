"""Sensor to shared cartesian frame projection.

Reads RGB-D camera, IR beacon, UWB ranging, and microphone array per robot
local frame. Produces a world_model_snapshot with patient, peers, doctors,
and salient obstacles in the shared site cartesian frame (origin at the site
entrance, x north, y west, z up).
"""

from __future__ import annotations

import math
from typing import Optional


class SensorToXYZ:
    def __init__(self, robot_id: str, site_id: str) -> None:
        self.robot_id = robot_id
        self.site_id = site_id
        self.peer_estimates: dict[str, dict] = {}

    def project_depth_to_world(
        self,
        depth_map: list[list[float]],
        camera_pose: dict,
    ) -> dict:
        local_points = self._depth_to_local(depth_map)
        world_points = self._local_to_world(local_points, camera_pose)
        return {"points_xyz": world_points}

    def triangulate_peer(
        self,
        peer_id: str,
        ir_beacons: list[dict],
        uwb_ranges: list[dict],
    ) -> dict:
        ir_xy = self._ir_triangulate(ir_beacons)
        uwb_xy = self._uwb_estimate(uwb_ranges)
        fused = [
            0.6 * ir_xy[0] + 0.4 * uwb_xy[0],
            0.6 * ir_xy[1] + 0.4 * uwb_xy[1],
            0.6 * ir_xy[2] + 0.4 * uwb_xy[2],
        ]
        out = {
            "peer_id": peer_id,
            "position_xyz": {"x": fused[0], "y": fused[1], "z": fused[2]},
        }
        self.peer_estimates[peer_id] = out
        return out

    def fuse_kalman(self, prior: Optional[dict], measurement: dict) -> dict:
        if prior is None:
            return dict(measurement)
        out: dict = {}
        for k, v in measurement.items():
            if isinstance(v, dict):
                pv = prior.get(k, {})
                out[k] = {kk: 0.5 * vv + 0.5 * pv.get(kk, vv) for kk, vv in v.items()}
            else:
                out[k] = v
        return out

    def snapshot(self) -> dict:
        return {
            "robot_id": self.robot_id,
            "site": self.site_id,
            "peers": {pid: dict(est) for pid, est in self.peer_estimates.items()},
        }

    def _depth_to_local(self, depth_map: list[list[float]]) -> list[list[float]]:
        return [[0.0, 0.0, float(d)] for row in depth_map for d in row[:1]]

    def _local_to_world(
        self,
        local_points: list[list[float]],
        camera_pose: dict,
    ) -> list[list[float]]:
        cx = float(camera_pose.get("x", 0.0))
        cy = float(camera_pose.get("y", 0.0))
        cz = float(camera_pose.get("z", 0.0))
        return [[p[0] + cx, p[1] + cy, p[2] + cz] for p in local_points]

    def _ir_triangulate(self, ir_beacons: list[dict]) -> list[float]:
        if not ir_beacons:
            return [0.0, 0.0, 0.0]
        xs = sum(b.get("x", 0.0) for b in ir_beacons) / len(ir_beacons)
        ys = sum(b.get("y", 0.0) for b in ir_beacons) / len(ir_beacons)
        zs = sum(b.get("z", 0.0) for b in ir_beacons) / len(ir_beacons)
        return [xs, ys, zs]

    def _uwb_estimate(self, uwb_ranges: list[dict]) -> list[float]:
        if not uwb_ranges:
            return [0.0, 0.0, 0.0]
        xs = sum(b.get("x", 0.0) for b in uwb_ranges) / len(uwb_ranges)
        ys = sum(b.get("y", 0.0) for b in uwb_ranges) / len(uwb_ranges)
        zs = sum(b.get("z", 0.0) for b in uwb_ranges) / len(uwb_ranges)
        return [xs, ys, zs]
