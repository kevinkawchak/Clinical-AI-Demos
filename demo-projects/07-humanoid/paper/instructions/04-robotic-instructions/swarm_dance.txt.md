# Authoring Instructions for `diagrams/swarm_dance.txt`

The future session writes this ASCII diagram during Commit 3 of 7. It is new in v0.3.0 and visualizes the camarade synchronization pattern over a 10-second window.

## Purpose

Shows position trails of 3 H2 robots around the patient bed during a 10-second window at AE response peak. Caps at 80 columns by 60 lines.

## Required Content

```
                       Camarade Swarm Dance (10 second window)
                       =========================================

  Top down view of the patient bed and 3 H2 robots over 10 seconds at 1 Hz frames.
  P is patient bed. L is Lead H2-A. A is Assist H2-B. R is Reserve H2-C.
  Subscripts 0 through 9 are seconds since AE peak. Each robot draws its trail.

           (north wall)
      .......................................
      .                                     .
      .                R0                   .
      .                                     .
      .          R3 R6 R9                   .
      .                                     .
      .             A0                      .
      .         A2  A4  A6   A8             .
      .                                     .
      .              L0                     .
      .              ||                     .
      .              PP   <-- patient bed   .
      .              ||                     .
      .              L2                     .
      .              L4                     .
      .              L6                     .
      .              L8                     .
      .                                     .
      .......................................
           (south wall)

  Observations:
    - Lead stays close to patient bed, 0.4 m offset on the south side.
    - Assist orbits 0.8 m to the west of the patient, ready to hand off.
    - Reserve circles a 1.5 m perimeter, watching the room.
    - No robot enters another robot's 2 second motion envelope.
    - At t+6, Lead asks Assist for the secondary epinephrine; Assist arrives at L position within 2 seconds.
```

## Validation Rules

- 80 columns by 60 lines max.
- Shows all 3 robots' trails.
- Indicates the patient bed location.

## Notes

- This diagram is referenced from `reports/report.md`.
- The 1 Hz frames match the LLM broadcast cadence; the diagram is a direct visualization of one second by one second decisions.
