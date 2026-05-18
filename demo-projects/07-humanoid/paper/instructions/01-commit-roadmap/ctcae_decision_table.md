# Authoring Instructions for `data/ctcae_decision_table.csv`

The future session writes this CSV during Commit 6 of 7 (or commit 4 if memory budget permits).

## Purpose

Maps AE type plus vital sign thresholds to CTCAE v5.0 grade and term. Used by `src/ctcae_grader.py`.

## Layout

```
ae_type,vital_threshold,grade,term
anaphylaxis,spo2<85,4,Anaphylaxis Grade 4 life threatening
anaphylaxis,spo2<92,3,Anaphylaxis Grade 3 severe
anaphylaxis,wheezing+rash,2,Anaphylaxis Grade 2 moderate
anaphylaxis,rash_only,1,Anaphylaxis Grade 1 mild
hypotension,sbp<60,4,Hypotension Grade 4 life threatening
hypotension,sbp<70,3,Hypotension Grade 3 severe
hypotension,sbp<90,2,Hypotension Grade 2 moderate
hypoxia,spo2<85,4,Hypoxia Grade 4 life threatening
hypoxia,spo2<88,3,Hypoxia Grade 3 severe
hypoxia,spo2<92,2,Hypoxia Grade 2 moderate
syncope,loss_of_consciousness_seconds>180,4,Syncope Grade 4 life threatening
syncope,loss_of_consciousness_seconds>60,3,Syncope Grade 3 severe
syncope,loss_of_consciousness_seconds>10,2,Syncope Grade 2 moderate
cytokine_release_syndrome,fever+hypotension+hypoxia,4,CRS Grade 4 life threatening
cytokine_release_syndrome,fever+hypotension,3,CRS Grade 3 severe
cytokine_release_syndrome,fever_only,2,CRS Grade 2 moderate
cardiac_arrest,asystole,5,Cardiac Arrest Grade 5 death
bleeding,massive_hemorrhage,4,Bleeding Grade 4 life threatening
thrombosis,acute_with_organ_dysfunction,4,Thrombosis Grade 4 life threatening
infection_sepsis,septic_shock,4,Sepsis Grade 4 life threatening
seizure,prolonged_or_status,4,Seizure Grade 4 life threatening
pulmonary_embolism,massive_pe,4,PE Grade 4 life threatening
hypertension_crisis,sbp>200,4,Hypertension Crisis Grade 4 life threatening
```

## Validation Rules

- All grades in [1, 5].
- Vital thresholds use simple comparison strings.
- One row per (ae_type, threshold) pair.

## Notes

- The table is intentionally simple. Production would use a learned classifier.
- Cite the author's prior FAERS work in the file header comment.
