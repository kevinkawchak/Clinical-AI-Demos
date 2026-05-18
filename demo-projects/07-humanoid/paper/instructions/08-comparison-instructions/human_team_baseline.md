# Authoring Instructions for `data/human_team_baseline.csv`

The future session writes this CSV during Commit 5 of 7.

## Purpose

A reference table of human paramedic team AE response times from 6 published trial site studies. Used as a baseline for the comparison framework.

## Layout

```
study_id,study_year,site_type,team_size,ae_type,median_response_seconds,p95_response_seconds,sample_size,doi_or_pmid
```

30 rows covering 5 AE types across 6 studies:

- 5 rows per AE type
- AE types: anaphylaxis, cytokine_release_syndrome, hypotension, syncope, cardiac_arrest
- Study years 2021 to 2025
- Team sizes: 1 (solo nurse), 2 (nurse plus on-call), 3 (full rapid response team)
- Sample sizes 50 to 800 patient-events per study

## Example Rows

```
study_id,study_year,site_type,team_size,ae_type,median_response_seconds,p95_response_seconds,sample_size,doi_or_pmid
STUDY-001,2024,academic_medical_center,3,anaphylaxis,420,720,250,10.1234/synthetic
STUDY-002,2023,community_hospital,2,cytokine_release_syndrome,540,900,180,10.5678/synthetic
STUDY-003,2025,academic_medical_center,3,hypotension,360,600,420,10.9012/synthetic
STUDY-004,2022,trial_site,3,syncope,300,540,500,10.3456/synthetic
STUDY-005,2021,community_hospital,1,cardiac_arrest,180,360,800,10.7890/synthetic
STUDY-006,2025,trial_site,3,anaphylaxis,420,660,200,10.1357/synthetic
```

## Validation Rules

- 30 rows.
- All response times in seconds.
- DOI fields use synthetic prefixes (e.g., `10.1234/synthetic`); not real DOIs. Production version would use real PMIDs.

## Notes

- The 3-human-paramedic team baseline at 420 seconds median is the strict comparison target for the camarade swarm.
- The camarade swarm target is under 90 seconds median, a 4.7x improvement.
