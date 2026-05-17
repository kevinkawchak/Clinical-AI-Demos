# Authoring Instructions for `config/site_frame_bounds.yaml`

The future session writes this YAML during Commit 6 of 7.

## Purpose

Per-site cartesian frame bounds and no-fly zones. Consumed by `src/xyz_safety.py`.

## Content

```
sites:
  SF-01:
    x_min_m: -50.0
    x_max_m: 50.0
    y_min_m: -50.0
    y_max_m: 50.0
    z_min_m: 0.0
    z_max_m: 3.0
    no_fly_zones:
      - name: oxygen_tank_rack
        center_xyz: {x: -5.0, y: 0.0, z: 0.5}
        radius_m: 1.5
      - name: imaging_equipment
        center_xyz: {x: 10.0, y: 5.0, z: 1.0}
        radius_m: 2.0
  SD-01:
    x_min_m: -50.0
    x_max_m: 50.0
    y_min_m: -50.0
    y_max_m: 50.0
    z_min_m: 0.0
    z_max_m: 3.0
    no_fly_zones:
      - name: oxygen_tank_rack
        center_xyz: {x: -3.0, y: 0.0, z: 0.5}
        radius_m: 1.5
  BO-01:
    x_min_m: -50.0
    x_max_m: 50.0
    y_min_m: -50.0
    y_max_m: 50.0
    z_min_m: 0.0
    z_max_m: 3.0
    no_fly_zones:
      - name: pharmacy_clean_room_partition
        center_xyz: {x: 0.0, y: 10.0, z: 1.5}
        radius_m: 0.5
  AT-01:
    x_min_m: -50.0
    x_max_m: 50.0
    y_min_m: -50.0
    y_max_m: 50.0
    z_min_m: 0.0
    z_max_m: 3.0
    no_fly_zones: []
```

## Validation Rules

- 4 sites.
- All bounds within +/-50 m.
- z_min is 0.0 (floor) and z_max is 3.0 (ceiling).

## Notes

- No-fly zone radii are conservative; 1.5 m around an oxygen tank rack guarantees no robot collision.
- These bounds are read by `xyz_safety.validate_command` to reject out-of-bounds commands.
