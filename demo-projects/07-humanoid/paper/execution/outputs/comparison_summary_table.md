# Comparison Across 4 Configurations (from comparison.json)

| Configuration | p50 s | p95 s | cam_pass | fda_1h | survey | safety_estop | cost_per_ae_usd | weighted_score |
|---|---|---|---|---|---|---|---|---|
| v0_4_0 | 72.2 | 94.4 | 0.9695 | 0.9974 | 0.92 | 0.9999 | 250 | 0.9530 |
| competitor_atlas | 95.0 | 130.0 | 0.8500 | 0.9700 | 0.86 | 0.9980 | 400 | 0.8470 |
| competitor_optimus | 100.0 | 140.0 | 0.8200 | 0.9600 | 0.84 | 0.9970 | 350 | 0.8210 |
| competitor_human_team | 375.0 | 720.0 | 0.7000 | 0.8500 | 0.88 | 0.9500 | 1800 | 0.6820 |

Weight vector (sum 1.00):
- response_time: 0.25
- patient_safety: 0.20
- fda_rtct_compliance: 0.15
- camaraderie: 0.10
- cost: 0.10
- safety: 0.10
- patient_experience: 0.10
