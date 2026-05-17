# Authoring Instructions for `src/kinematics.yaml`

The future session writes this YAML during Commit 3 of 7.

## Purpose

Shared kinematics chain for the Unitree H2 humanoid. Used by all 12 robots and by the inverse kinematics solver in `cartesian_planner.py`.

## Fields

```
platform: Unitree H2
dof: 39
base_frame: site_world
height_m: 1.8
mass_kg: 70

chains:
  spine:
    - {name: pelvis,        parent: base,          axis: [0, 0, 1], offset_m: [0.0, 0.0, 0.0],  range_rad: [-0.5, 0.5]}
    - {name: lower_torso,   parent: pelvis,        axis: [0, 0, 1], offset_m: [0.0, 0.0, 0.15], range_rad: [-0.3, 0.3]}
    - {name: upper_torso,   parent: lower_torso,   axis: [0, 0, 1], offset_m: [0.0, 0.0, 0.20], range_rad: [-0.3, 0.3]}
    - {name: neck_yaw,      parent: upper_torso,   axis: [0, 0, 1], offset_m: [0.0, 0.0, 0.20], range_rad: [-1.5, 1.5]}
    - {name: head,          parent: neck_yaw,      axis: [0, 1, 0], offset_m: [0.0, 0.0, 0.08], range_rad: [-1.0, 1.0]}
  left_arm:
    - {name: shoulder_y,    parent: upper_torso,   axis: [0, 1, 0], offset_m: [0.0, 0.18, 0.40], range_rad: [-3.14, 3.14]}
    - {name: shoulder_p,    parent: shoulder_y,    axis: [1, 0, 0], offset_m: [0.0, 0.0, 0.0],   range_rad: [-2.0, 2.0]}
    - {name: shoulder_r,    parent: shoulder_p,    axis: [0, 0, 1], offset_m: [0.0, 0.0, 0.0],   range_rad: [-2.0, 2.0]}
    - {name: elbow,         parent: shoulder_r,    axis: [0, 1, 0], offset_m: [0.0, 0.0, -0.25], range_rad: [-2.5, 0.0]}
    - {name: wrist_r,       parent: elbow,         axis: [0, 0, 1], offset_m: [0.0, 0.0, -0.20], range_rad: [-3.14, 3.14]}
    - {name: wrist_p,       parent: wrist_r,       axis: [1, 0, 0], offset_m: [0.0, 0.0, 0.0],   range_rad: [-1.5, 1.5]}
    - {name: wrist_y,       parent: wrist_p,       axis: [0, 1, 0], offset_m: [0.0, 0.0, 0.0],   range_rad: [-1.5, 1.5]}
    - {name: hand_grip,     parent: wrist_y,       axis: [0, 0, 1], offset_m: [0.0, 0.0, -0.10], range_rad: [-1.0, 1.0]}
  right_arm: # mirror of left arm with negated y offsets
    - {name: shoulder_y,    parent: upper_torso,   axis: [0, 1, 0], offset_m: [0.0, -0.18, 0.40], range_rad: [-3.14, 3.14]}
    # ... same pattern as left arm with y negated where applicable
  left_leg:
    - {name: hip_y,         parent: pelvis,        axis: [0, 1, 0], offset_m: [0.0, 0.10, -0.10], range_rad: [-1.5, 1.5]}
    - {name: hip_p,         parent: hip_y,         axis: [1, 0, 0], offset_m: [0.0, 0.0, 0.0],   range_rad: [-1.0, 1.5]}
    - {name: hip_r,         parent: hip_p,         axis: [0, 0, 1], offset_m: [0.0, 0.0, 0.0],   range_rad: [-0.5, 0.5]}
    - {name: knee,          parent: hip_r,         axis: [0, 1, 0], offset_m: [0.0, 0.0, -0.40], range_rad: [0.0, 2.5]}
    - {name: ankle_p,       parent: knee,          axis: [1, 0, 0], offset_m: [0.0, 0.0, -0.40], range_rad: [-0.8, 0.5]}
    - {name: ankle_y,       parent: ankle_p,       axis: [0, 1, 0], offset_m: [0.0, 0.0, 0.0],   range_rad: [-0.5, 0.5]}
  right_leg: # mirror of left_leg with negated y offsets
    # ... same pattern as left leg with y negated where applicable

ik_solver:
  algorithm: damped_least_squares
  damping: 0.01
  max_iterations: 100
  position_tolerance_m: 0.005
  orientation_tolerance_rad: 0.01
  joint_step_max_rad: 0.05
```

## Validation Rules

- 39 joints total across all chains.
- All joint ranges are physically realizable.
- `ik_solver.algorithm` is `damped_least_squares` (DLS) for numerical stability.

## Notes

- The DLS solver is the standard pick for 7-DOF redundant arms. It handles singularities gracefully.
- The right arm and right leg sections are abbreviated for space; the future session expands them by mirroring left arm and left leg with negated `y` offsets.
