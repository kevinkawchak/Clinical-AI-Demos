# Authoring Instructions for `data/sample_sensor.csv` and `data/sample_xyz.csv`

The future session writes these CSV files during Commit 3 of 7.

## Purpose

Provide a 60-second representative sample of sensor readings and cartesian commands for one robot. Used by `src/sensor_to_xyz.py` to demonstrate the conversion and by `src/cartesian_planner.py` to demonstrate the trajectory generation.

## `data/sample_sensor.csv` Layout

```
timestamp_iso,robot_id,sensor_type,reading
2026-05-17T12:00:00Z,SF-01-H2-A,joint_encoder,{ ... 39 angle values in radians ... }
2026-05-17T12:00:00Z,SF-01-H2-A,depth_camera,{ ... depth map summary ... }
2026-05-17T12:00:00Z,SF-01-H2-A,uwb_range,{ ... peer ID and range in meters ... }
2026-05-17T12:00:00Z,SF-01-H2-A,ir_beacon,{ ... peer ID and bearing/range ... }
2026-05-17T12:00:00Z,SF-01-H2-A,force_torque_left_wrist,{ ... 6-axis FT ... }
```

600 rows for 60 seconds at 10 Hz, covering all sensor types.

## `data/sample_xyz.csv` Layout

```
timestamp_iso,robot_id,role,x,y,z,roll,pitch,yaw,gripper_state
2026-05-17T12:00:00Z,SF-01-H2-A,Lead,1.0,2.0,1.5,0.0,0.0,0.0,open
2026-05-17T12:00:01Z,SF-01-H2-A,Lead,1.1,2.0,1.5,0.0,0.0,0.0,open
```

60 rows for 60 seconds at 1 Hz, showing the Lead robot approaching a patient bed and beginning an intervention.

## Validation Rules

- CSV with header row.
- ISO timestamps.
- Synthetic robot IDs only (SF-01-H2-A in this sample).

## Notes

- These files are small (about 100 KB each). They exist to demonstrate the data shapes.
- The full 168-hour data lives in Parquet under `data/week_*.parquet` and is generated in commit 4.
