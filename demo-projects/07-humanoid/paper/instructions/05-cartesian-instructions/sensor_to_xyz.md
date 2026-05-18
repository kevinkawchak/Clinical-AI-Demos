# Authoring Instructions for `src/sensor_to_xyz.py`

The future session writes this Python module during Commit 3 of 7.

## Purpose

Projects sensor readings (RGB-D camera, IR beacons, UWB ranging, microphone array) from the per-robot local frame into the shared site cartesian frame. The output is consumed by the LLM planner which reasons in x, y, z coordinates.

## Key Behavior

- Reads stereo RGB-D camera depth maps at 10 Hz and produces a 3D point cloud in the robot's local frame.
- Reads IR beacon range-bearing pairs from peers and triangulates the peer position in the shared frame.
- Reads UWB ranging measurements from peers and refines the peer position estimate via Kalman fusion.
- Outputs a `world_model_snapshot` dictionary with patient, peers, doctors, and salient obstacles in the shared frame.

## Required Interfaces

```
class SensorToXYZ:
    def __init__(self, robot_id: str, site_id: str) -> None: ...
    def project_depth_to_world(self, depth_map, camera_pose) -> dict: ...
    def triangulate_peer(self, peer_id: str, ir_beacons: list[dict], uwb_ranges: list[dict]) -> dict: ...
    def fuse_kalman(self, prior, measurement) -> dict: ...
    def snapshot(self) -> dict: ...
```

## Frame Conventions

- The shared site frame has its origin at the site entrance, x pointing north, y pointing west, z pointing up.
- Each robot has a local frame attached to its pelvis.
- The conversion from local to shared frame uses the robot's pose, which is maintained at 10 Hz by the on-robot pose estimator.

## Suggested Skeleton

```
import numpy as np


class SensorToXYZ:
    def __init__(self, robot_id, site_id):
        self.robot_id = robot_id
        self.site_id = site_id
        self.peer_estimates = {}

    def project_depth_to_world(self, depth_map, camera_pose):
        # convert depth_map pixels to local 3D points, then to world via camera_pose
        local_points = self._depth_to_local(depth_map)
        world_points = self._local_to_world(local_points, camera_pose)
        return {"points_xyz": world_points.tolist()}

    def triangulate_peer(self, peer_id, ir_beacons, uwb_ranges):
        # use simple weighted average of IR triangulation and UWB ranging
        ir_estimate = self._ir_triangulate(ir_beacons)
        uwb_estimate = self._uwb_estimate(uwb_ranges)
        fused = 0.6 * np.array(ir_estimate) + 0.4 * np.array(uwb_estimate)
        return {"peer_id": peer_id, "position_xyz": {"x": float(fused[0]), "y": float(fused[1]), "z": float(fused[2])}}

    def fuse_kalman(self, prior, measurement):
        # 3D position Kalman filter, identity dynamics, gaussian noise
        return measurement

    def snapshot(self):
        return {"robot_id": self.robot_id, "peers": dict(self.peer_estimates)}

    def _depth_to_local(self, depth_map):
        return np.zeros((1000, 3))

    def _local_to_world(self, local_points, camera_pose):
        return local_points

    def _ir_triangulate(self, ir_beacons):
        return [0.0, 0.0, 0.0]

    def _uwb_estimate(self, uwb_ranges):
        return [0.0, 0.0, 0.0]
```

## Validation Rules

- Output point cloud in float meters in the shared frame.
- Peer position estimates within 0.1 m RMS at 5 m range.

## Notes

- The depth-to-world conversion is the standard pinhole camera plus extrinsics math.
- The Kalman fusion is overkill for simulation but matches production code structure.
- Numpy is the only required dependency.
