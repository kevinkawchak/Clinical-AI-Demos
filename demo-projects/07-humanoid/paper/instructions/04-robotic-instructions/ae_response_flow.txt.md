# Authoring Instructions for `diagrams/ae_response_flow.txt`

The future session writes this ASCII diagram during Commit 3 of 7.

## Purpose

A 3-lane swimlane showing Lead, Assist, and Reserve activity during a typical 90-second AE response. Caps at 80 columns by 60 lines.

## Required Content

```
                       AE Response Swimlane (Single AE, 90 seconds)
                       ===============================================

  Time  Lead (H2-A)                Assist (H2-B)             Reserve (H2-C)
  ---   -------------------        ----------------          -----------------
  t+0    AE detected, role assign  AE detected, prep tools  AE detected, scan perimeter
  t+5    move to bedside           move to bedside backup   stand 1.5 m off side
  t+15   epinephrine ready         hand-off epinephrine     page on-call physician
  t+18   epinephrine injected      pulse oximeter prepared  log to audit chain
  t+22   verify spo2 reading       hand-off pulse oximeter  monitor doctor proximity
  t+30   secondary intervention    ecg leads attached       fda rtct submission
  t+45   continuous monitoring     vital sign relay         physician on site check
  t+60   transfer to physician     tool inventory restock   sponsor acknowledgment log
  t+75   step back, observe        step back, observe       step back, observe
  t+90   ready for next AE         ready for next AE        ready for next AE

  Notes:
    - All 3 robots arrive within 90 seconds.
    - Hand-offs complete within 2 seconds via 60 GHz UWB.
    - Reserve does FDA RTCT submission in parallel with Lead intervention.
```

## Validation Rules

- 80 columns by 60 lines max.
- 3 lanes always.
- Time markers in seconds.

## Notes

- This is illustrative; actual timing varies by AE type.
- The diagram is referenced from `reports/report.md`.
