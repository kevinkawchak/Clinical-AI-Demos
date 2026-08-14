"""Slide content for the LLM Pancreatic Oncology Clinical Trial System deck.

Twenty deposited papers, in chronological order (earliest first), each carrying
the seven-line evaluation the seminar audience is asked to follow:

    Paper Title  what was deposited, and when
    Abstract     the one sentence the paper's own abstract of record supports
    Strengths    what the work does that a trialist would call sound
    Limitations  what it does not do, stated by the paper itself
    Results      the number the paper actually reports
    LLM Trust    how the paper made an LLM-based pancreatic cancer trial more
                 trustworthy than it was before the paper existed
    LLM Benefit  what the paper contributes to the upcoming LLM-enabled trial
                 described in theme/update-final-LaTeX.zip

Every quantity on these slides is taken from ``abstracts/README.md`` or from
the section files of ``theme/update-final-LaTeX.zip``.  Nothing is estimated.
Two papers need a second LLM Trust or LLM Benefit line, and take one, rather
than being compressed into a line that would misstate them.

Item styles
-----------
``"bullet"``  a square bullet, used for the framing and synthesis lines
``"number"``  an automatically numbered line, used for the three evaluative
              axes (Strengths, Limitations, Results), which read as a set

Slide sides
-----------
The cover image sits on the left for four consecutive papers, then on the
right for the fifth, and the cadence repeats: papers 5, 10, 15 and 20 are the
right-hand covers.  ``side_for`` is the single source of truth for that rule.
"""

from __future__ import annotations

DECK_TITLE = "LLM Pancreatic Oncology Clinical Trial System: Large Documents, Funding, and AI Peer Review"
DECK_TITLE_LINES = (
    "LLM Pancreatic Oncology Clinical Trial System:",
    "Large Documents, Funding, and AI Peer Review",
)
DECK_SUBTITLE = "Twenty deposited papers, and the Phase 1 trial they were written to support"
AUTHOR = "Kevin Kawchak, Chief Executive Officer, ChemicalQDevice"
AUTHOR_SHORT = "Kevin Kawchak, CEO ChemicalQDevice"
PRESENTED_DATE = "Friday, August 14, 2026"
VENUE = "Oncology Trials Seminar  |  University Comprehensive Cancer Center"
CONTACT = "San Diego, CA  |  kevink@chemicalqdevice.com  |  ORCID 0009-0007-5457-8667"
DISCLAIMER = (
    "Independent research. Not medical or regulatory advice, and not endorsed by the FDA, "
    "NIH, HHS, an IRB, ICH, or any sponsor. No trial described here is active or approved."
)

TITLE_STATS = (
    ("20", "deposited papers", "June 2025 to August 2026"),
    ("4 days", "to assemble a 12-module IND", "594,657 characters"),
    ("n = 18", "Phase 1, 3+3 escalation", "behind a 1000-simulation gate"),
    ("$1.6M", "small-business ask", "against a $3.5M direct program"),
)

RIGHT_COVER_EVERY = 5


def side_for(paper_number: int) -> str:
    """Return ``"left"`` or ``"right"`` for the cover image of ``paper_number``.

    Four consecutive left-hand covers are followed by one right-hand cover, so
    every fifth paper takes the right side.
    """
    return "right" if paper_number % RIGHT_COVER_EVERY == 0 else "left"


PAPERS = (
    {
        "number": 1,
        "doi": "10.5281/zenodo.15735068",
        "date": "June 24, 2025",
        "cover": "cover-01-pdac-digital-twin-proposals.jpg",
        "reference_title": ("End-to-End Pancreatic Ductal Adenocarcinoma Digital Twin Clinical Trial Proposals"),
        "headline": "End-to-End PDAC Digital Twin Clinical Trial Proposals",
        "items": (
            ("bullet", "Paper Title", "End-to-End PDAC Digital Twin Clinical Trial Proposals, deposited June 24, 2025"),
            (
                "bullet",
                "Abstract",
                "Seven AI model combinations built 40 PDAC meta-analyses that five AI judges then ranked",
            ),
            (
                "number",
                "Strengths",
                "A 408,001-word source corpus, automated verification, and five judges scoring one rubric",
            ),
            (
                "number",
                "Limitations",
                "Models self-reported 84.0% accuracy against 95% verified; grounding remains preliminary",
            ),
            (
                "number",
                "Results",
                "Top proposal scored 9.60/10 on deliverable completion, 9.20 on citation, 8.94 on trial impact",
            ),
            (
                "bullet",
                "LLM Trust",
                "Cross-model verification, not one model's word, is what made the meta-analysis defensible",
            ),
            (
                "bullet",
                "LLM Benefit",
                "Named the daraxonrasib triplet the trial carries, traced to meta-analyses MA-23 and MA-15",
            ),
        ),
    },
    {
        "number": 2,
        "doi": "10.5281/zenodo.16415815",
        "date": "July 24, 2025",
        "cover": "cover-02-chatgpt-100k-patient-phase-iii.jpg",
        "reference_title": (
            "ChatGPT 100,000 Patient 24-Month In Silico Phase III 5-Arm Pancreatic Cancer Clinical Trial Triplicate"
        ),
        "headline": "ChatGPT 100,000 Patient In Silico Phase III Triplicate",
        "items": (
            (
                "bullet",
                "Paper Title",
                "ChatGPT 100,000 Patient 24-Month In Silico Phase III 5-Arm PDAC Triplicate, July 24, 2025",
            ),
            (
                "bullet",
                "Abstract",
                "One user reproduced a 100,000-patient, five-arm, 24-month Phase III three times in 30 days",
            ),
            (
                "number",
                "Strengths",
                "Triplicate reproducibility, six-model cross-verification, external validation on Flatiron OS",
            ),
            (
                "number",
                "Limitations",
                "ECOG validation diverged, a KRAS-mutant labeling issue persisted, patients were synthetic",
            ),
            (
                "number",
                "Results",
                "$36,304 total against a $20.0M Phase II and a $100.0M Phase III; 4.5 months against 5.0 years",
            ),
            (
                "bullet",
                "LLM Trust",
                "Three identical runs with the divergence published is reproducibility a trialist can check",
            ),
            (
                "bullet",
                "LLM Benefit",
                "Screened Arm A out before any enrollment, avoiding an estimated $19.96M failed trial",
            ),
        ),
    },
    {
        "number": 3,
        "doi": "10.5281/zenodo.17001137",
        "date": "August 29, 2025",
        "cover": "cover-03-qsp-metastatic-pdac-simulation.jpg",
        "reference_title": (
            "QSP Metastatic Pancreatic Cancer AI Clinical Trial Simulation From Protocol to "
            "Prediction: Code, VVUQ, and Playbook"
        ),
        "headline": "QSP Metastatic PDAC Simulation: Code, VVUQ, and Playbook",
        "items": (
            (
                "bullet",
                "Paper Title",
                "QSP Metastatic PDAC AI Trial Simulation: Code, VVUQ, and Playbook, August 29, 2025",
            ),
            (
                "bullet",
                "Abstract",
                "A text protocol became Python, then a 10-arm trial of 10,000 patients at 250 ODEs each",
            ),
            (
                "number",
                "Strengths",
                "Numerically stable at dt = 0.05, VVUQ throughout, and a plain-text protocol regenerated",
            ),
            (
                "number",
                "Limitations",
                "mPFS and Grade 3+ adverse events grounded poorly to external controls; 2.5M states",
            ),
            ("number", "Results", "Arm C reached ORR 70.8% and mOS 11.9 months at HR 0.50; ORR error bounded at 11%"),
            (
                "bullet",
                "LLM Trust",
                "VVUQ, not model authority, is what made the simulation admissible to a trial reviewer",
            ),
            (
                "bullet",
                "LLM Benefit",
                "Set the verification discipline the Phase 1 protocol's Phase 0 simulation gate now requires",
            ),
        ),
    },
    {
        "number": 4,
        "doi": "10.5281/zenodo.17239510",
        "date": "September 30, 2025",
        "cover": "cover-04-fda-compliance-cost-efficiency.jpg",
        "reference_title": (
            "Accelerating FDA Compliance and Cost Efficiency of in silico Clinical Trials via "
            "AI Digital Twin Pancreatic Cancer Simulation"
        ),
        "headline": "Accelerating FDA Compliance of in silico Trials via Digital Twin",
        "items": (
            (
                "bullet",
                "Paper Title",
                "Accelerating FDA Compliance and Cost Efficiency of in silico Trials, September 30, 2025",
            ),
            ("bullet", "Abstract", "A 10-arm, 36-month PDAC platform twin assessed under ICH M15 and ASME V&V 40"),
            (
                "number",
                "Strengths",
                "Technical criteria pre-specified across a VV40 suite, with model risk stated before results",
            ),
            (
                "number",
                "Limitations",
                "Model risk graded Medium, not High; multi-endpoint external calibration is open",
            ),
            ("number", "Results", "Arm A tracked external ORR and mOS closely; Arm G underpredicted mPFS and OS"),
            (
                "bullet",
                "LLM Trust",
                "Grading against a published credibility framework lets a regulator audit a claim, not a word",
            ),
            (
                "bullet",
                "LLM Benefit",
                "Supplies MIDD evidence for FDA Type C and pre-submission meetings before the IND",
            ),
        ),
    },
    {
        "number": 5,
        "doi": "10.5281/zenodo.18973368",
        "date": "March 12, 2026",
        "cover": "cover-05-ich-harmonised-guideline.jpg",
        "reference_title": (
            "Adaption: ICH Harmonised Guideline, End-to-End Physical AI Oncology Clinical Trial Unification"
        ),
        "headline": "Adaption: ICH Harmonised Guideline for Good Physical AI Practice",
        "items": (
            (
                "bullet",
                "Paper Title",
                "Adaption: ICH Harmonised Guideline, Physical AI Oncology Trial Unification, March 12, 2026",
            ),
            (
                "bullet",
                "Abstract",
                "ICH E6(R3) rebuilt in LaTeX and modified into a Good Physical AI Clinical Practice draft",
            ),
            (
                "number",
                "Strengths",
                "Works inside the guideline sites already run on rather than proposing a parallel standard",
            ),
            ("number", "Limitations", "An independent adaptation, not endorsed or sponsored by ICH, and not adopted"),
            (
                "number",
                "Results",
                "A clause-level text naming the sponsor, investigator, and monitor duties a Physical AI arm adds",
            ),
            ("bullet", "LLM Trust", "Mapping the new modality onto E6(R3) means an IRB reads a familiar document"),
            (
                "bullet",
                "LLM Benefit",
                "Gives the LLM-directed Whipple its GCP spine, cited at Section 1.4 of both trial protocols",
            ),
        ),
    },
    {
        "number": 6,
        "doi": "10.5281/zenodo.19040707",
        "date": "March 16, 2026",
        "cover": "cover-06-21-cfr-part-50.jpg",
        "reference_title": ("Adaption: 21 CFR Part 50, End-to-End Physical AI Oncology Clinical Trial Unification"),
        "headline": "Adaption: 21 CFR Part 50, Protection of Human Subjects",
        "items": (
            (
                "bullet",
                "Paper Title",
                "Adaption: 21 CFR Part 50, Physical AI Oncology Trial Unification, March 16, 2026",
            ),
            (
                "bullet",
                "Abstract",
                "Public-domain eCFR text rebuilt in Markdown, then LaTeX, around human-subject protection",
            ),
            (
                "number",
                "Strengths",
                "Human-subject protection is settled first, before any autonomy claim is made for the system",
            ),
            (
                "number",
                "Limitations",
                "An independent modified regulatory draft, not endorsed by the FDA or by the eCFR",
            ),
            (
                "number",
                "Results",
                "Consent elements restated so a participant can check each one against the trial's own record",
            ),
            (
                "bullet",
                "LLM Trust",
                "Consent written as a participant capability, not a sponsor obligation, is checkable at bedside",
            ),
            ("bullet", "LLM Benefit", "Underwrites the seven commitments the Phase 1 advocacy paper makes enforceable"),
        ),
    },
    {
        "number": 7,
        "doi": "10.5281/zenodo.19057628",
        "date": "March 17, 2026",
        "cover": "cover-07-21-cfr-part-312.jpg",
        "reference_title": ("Adaption: 21 CFR Part 312, End-to-End Physical AI Oncology Clinical Trial Unification"),
        "headline": "Adaption: 21 CFR Part 312, Investigational New Drug Application",
        "items": (
            (
                "bullet",
                "Paper Title",
                "Adaption: 21 CFR Part 312, Physical AI Oncology Trial Unification, March 17, 2026",
            ),
            (
                "bullet",
                "Abstract",
                "Part 312 rebuilt in Markdown and LaTeX around investigational-drug rules for Physical AI",
            ),
            (
                "number",
                "Strengths",
                "Content items map one to one onto the codified section a reviewer opens; nothing invented",
            ),
            (
                "number",
                "Limitations",
                "An independent modified regulatory draft, not endorsed by the FDA, and not an active IND",
            ),
            (
                "number",
                "Results",
                "A Subpart J overlay carrying the robot and the model alongside the drug in a single dossier",
            ),
            (
                "bullet",
                "LLM Trust",
                "The IND answers to 21 CFR 312.23 line by line, which is where a regulatory reviewer starts",
            ),
            (
                "bullet",
                "LLM Benefit",
                "Became the skeleton the twelve-module daraxonrasib IND was built against in four days",
            ),
        ),
    },
    {
        "number": 8,
        "doi": "10.5281/zenodo.19244918",
        "date": "March 28, 2026",
        "cover": "cover-08-national-platform.jpg",
        "reference_title": "National Platform for Physical AI Oncology Trials",
        "headline": "National Platform for Physical AI Oncology Trials",
        "items": (
            ("bullet", "Paper Title", "National Platform for Physical AI Oncology Trials, deposited March 28, 2026"),
            (
                "bullet",
                "Abstract",
                "Public-domain federal material and licensed ICH guidance unified into one governance draft",
            ),
            (
                "number",
                "Strengths",
                "One resource covering governance and implementation, not three a site has to reconcile",
            ),
            (
                "number",
                "Limitations",
                "A draft, unaffiliated with CFR, ICH, FDA, a sponsor, a CRO, a site, an IRB, or a regulator",
            ),
            (
                "number",
                "Results",
                "A platform text a comprehensive cancer center can adopt without writing its own crosswalk",
            ),
            (
                "bullet",
                "LLM Trust",
                "One reconciled source closes the gaps between guidance documents where deviations start",
            ),
            (
                "bullet",
                "LLM Benefit",
                "Sets the multi-site governance the Phase 2 eight-center study runs under a single IRB",
            ),
        ),
    },
    {
        "number": 9,
        "doi": "10.5281/zenodo.20196639",
        "date": "May 15, 2026",
        "cover": "cover-09-2030-60-second-whipple.jpg",
        "reference_title": (
            "2030: 60 Second Pancreatic Ductal Adenocarcinoma Robotic Whipple Procedure & Daraxonrasib Simulation"
        ),
        "headline": "2030: 60 Second PDAC Robotic Whipple and Daraxonrasib Simulation",
        "items": (
            ("bullet", "Paper Title", "2030: 60 Second PDAC Robotic Whipple and Daraxonrasib Simulation, May 15, 2026"),
            (
                "bullet",
                "Abstract",
                "On-premises LLMs command an eight-arm coelomic robot from real-time x, y, z sensor data",
            ),
            (
                "number",
                "Strengths",
                "A five-phase build, a seeded deterministic sweep, and a four-entrant simulation tournament",
            ),
            (
                "number",
                "Limitations",
                "A synthetic patient gap, a hypothetical hardware gap, and TRIPOD+AI and CREMLS floors",
            ),
            (
                "number",
                "Results",
                "Mean composite 93.298, SD 1.225, 95% CI half width 0.462; PancreSpeed 1.0 led at 93.735",
            ),
            (
                "bullet",
                "LLM Trust",
                "Seed 20260513 and a 1,001-record sensor log make the run reproducible, not reported",
            ),
            (
                "bullet",
                "LLM Benefit",
                "Fixes the device envelope the IDE arm specifies: 0.05 mm RMS, 3 ms E-stop, 18 N cap",
            ),
        ),
    },
    {
        "number": 10,
        "doi": "10.5281/zenodo.20421754",
        "date": "May 28, 2026",
        "cover": "cover-10-unitree-h2-surgical-humanoid.jpg",
        "reference_title": "Mobile Pancreatic Cancer Unitree H2 Surgical Humanoid with Priority VVUQ",
        "headline": "Mobile Pancreatic Cancer Unitree H2 Humanoid with Priority VVUQ",
        "items": (
            (
                "bullet",
                "Paper Title",
                "Mobile Pancreatic Cancer Unitree H2 Surgical Humanoid with Priority VVUQ, May 28, 2026",
            ),
            (
                "bullet",
                "Abstract",
                "An autonomous agent carried a spec to a codebase and a full 60-second Whipple record",
            ),
            (
                "number",
                "Strengths",
                "Code assurance, not code generation, is treated as the decision-bearing work and held higher",
            ),
            (
                "number",
                "Limitations",
                "Simulation against simulation only; the humanoid trails the eight-arm cart on throughput",
            ),
            (
                "number",
                "Results",
                "172 of 172 automated tests passed, 64 in a ten-gate suite; 32 of 32 sweeps cleared every gate",
            ),
            (
                "bullet",
                "LLM Trust",
                "Ten ACCEPT, three BLOCK and one ESCALATE is the gate refusing the model, as intended",
            ),
            (
                "bullet",
                "LLM Benefit",
                "Binds every gate to a published consensus standard, making the argument defensible",
            ),
        ),
    },
    {
        "number": 11,
        "doi": "10.5281/zenodo.20454870",
        "date": "May 30, 2026",
        "cover": "cover-11-vvuq-oncology-trial-bill.jpg",
        "reference_title": "VVUQ Physical AI Oncology Trial Bill",
        "headline": "VVUQ Physical AI Oncology Trial Bill",
        "items": (
            (
                "bullet",
                "Paper Title",
                "VVUQ Physical AI Oncology Trial Bill, 119th Congress draft, deposited May 30, 2026",
            ),
            (
                "bullet",
                "Abstract",
                "A draft bill requiring automated VVUQ before robot-patient interaction code is generated or run",
            ),
            (
                "number",
                "Strengths",
                "The duty attaches before code generation, not after execution, where harm is preventable",
            ),
            (
                "number",
                "Limitations",
                "An independent legislative draft: not enacted law, not legal advice, not endorsed",
            ),
            (
                "number",
                "Results",
                "A statutory rule that a verification gate, not a policy commitment, clears code to reach a patient",
            ),
            (
                "bullet",
                "LLM Trust",
                "Verification before generation turns a voluntary practice into a duty a sponsor is held to",
            ),
            (
                "bullet",
                "LLM Benefit",
                "Names in statute the gate the Phase 1 trial already implements as a Phase 0 entry criterion",
            ),
        ),
    },
    {
        "number": 12,
        "doi": "10.5281/zenodo.20619762",
        "date": "June 10, 2026",
        "cover": "cover-12-hr-9510-bill-v5.jpg",
        "reference_title": "H. R. 9510 (Bill v5.0) 2026",
        "headline": "H. R. 9510 (Bill v5.0) 2026, the Financial Data Amendment",
        "items": (
            (
                "bullet",
                "Paper Title",
                "H. R. 9510 (Bill v5.0) 2026, the Financial Data Amendment, deposited June 10, 2026",
            ),
            (
                "bullet",
                "Abstract",
                "An FD&C Act amendment adding a financial-data record, transparency, fees and appropriations",
            ),
            (
                "number",
                "Strengths",
                "Five versions in nineteen days, each adding what its predecessor lacked, on the record",
            ),
            (
                "number",
                "Limitations",
                "Dollar figures are illustrative unless tied to a cited statute or notice; the bill is not enacted",
            ),
            (
                "number",
                "Results",
                "A cost ledger attaches to every verification run, so assurance is priced on the same record",
            ),
            ("bullet", "LLM Trust", "Publishing what verification costs stops assurance being an unpriced promise"),
            (
                "bullet",
                "LLM Benefit",
                "Gives a cancer center a fee and appropriations basis for hosting a Physical AI oncology trial",
            ),
        ),
    },
    {
        "number": 13,
        "doi": "10.5281/zenodo.20710602",
        "date": "June 16, 2026",
        "cover": "cover-13-earning-the-clinicians-trust.jpg",
        "reference_title": ("Earning the Clinician's Trust: New Framework for Verified Physical AI Oncology Trials"),
        "headline": "Earning the Clinician's Trust: A Framework for Verified Trials",
        "items": (
            (
                "bullet",
                "Paper Title",
                "Earning the Clinician's Trust: New Framework for Verified Physical AI Trials, June 16, 2026",
            ),
            (
                "bullet",
                "Abstract",
                "Written for the clinician who must decide at the bedside when reliance on Physical AI is earned",
            ),
            (
                "number",
                "Strengths",
                "Eight questions a clinician already asks, each closing on a gate, a record, a role or a control",
            ),
            (
                "number",
                "Limitations",
                "Calibrated trust, not maximal trust; it governs reliance without replacing clinical judgment",
            ),
            (
                "number",
                "Results",
                "An adoption decision a clinician can sign, on a lineage of 172 of 172 tests in a ten-gate suite",
            ),
            ("bullet", "LLM Trust", "Every clinical concern closes on a mechanism rather than on reassurance"),
            (
                "bullet",
                "LLM Trust",
                "Automation bias and algorithm aversion are named as the two failure modes, and mitigated",
            ),
            (
                "bullet",
                "LLM Benefit",
                "Answers the three questions a PI asks: my own family member, tumor board, auditor",
            ),
        ),
    },
    {
        "number": 14,
        "doi": "10.5281/zenodo.20780121",
        "date": "June 21, 2026",
        "cover": "cover-14-phase-1-ind-ide-protocol.jpg",
        "reference_title": (
            "On-Premises LLM-Directed Robotic Pancreaticoduodenectomy with Perioperative "
            "Daraxonrasib (RMC-6236) in KRAS-Mutated Pancreatic Ductal Adenocarcinoma"
        ),
        "headline": "On-Premises LLM-Directed Robotic Whipple, Phase 1 IND/IDE Protocol",
        "items": (
            (
                "bullet",
                "Paper Title",
                "On-Premises LLM-Directed Robotic Whipple with Perioperative Daraxonrasib, June 21, 2026",
            ),
            (
                "bullet",
                "Abstract",
                "A first-in-human combined IND/IDE protocol in KRAS-mutated PDAC: drug arm and device arm",
            ),
            (
                "number",
                "Strengths",
                "Drug, device and Physical AI compliance are settled in one Section 1, not across three filings",
            ),
            (
                "number",
                "Limitations",
                "A draft protocol: not an active or approved IND/IDE, and not medical or regulatory advice",
            ),
            (
                "number",
                "Results",
                "n = 18 on a 3+3 escalation behind a Phase 0 gate of 1000+ simulations across two frameworks",
            ),
            (
                "bullet",
                "LLM Trust",
                "The model cannot reach a participant until the simulation gate clears, written into entry criteria",
            ),
            (
                "bullet",
                "LLM Benefit",
                "This is the trial this seminar is about; the other nineteen papers are its supporting evidence",
            ),
            (
                "bullet",
                "LLM Benefit",
                "369,299 characters and 42 figures across both protocols, deposited two days apart",
            ),
        ),
    },
    {
        "number": 15,
        "doi": "10.5281/zenodo.20807027",
        "date": "June 23, 2026",
        "cover": "cover-15-phase-2-rct-protocol.jpg",
        "reference_title": (
            "A Phase 2, Daraxonrasib + LLM Guided Robotic PDAC Whipple Procedure, Clinical Trial Protocol"
        ),
        "headline": "Phase 2 Daraxonrasib + LLM Guided Robotic PDAC Whipple Protocol",
        "items": (
            (
                "bullet",
                "Paper Title",
                "A Phase 2, Daraxonrasib + LLM Guided Robotic PDAC Whipple Protocol, June 23, 2026",
            ),
            (
                "bullet",
                "Abstract",
                "A multicenter randomized Phase 2 on the Phase 1 predicate, under single-IRB governance",
            ),
            (
                "number",
                "Strengths",
                "Co-investment governance and single-IRB oversight are specified before any site is activated",
            ),
            (
                "number",
                "Limitations",
                "A draft contingent on a Phase 1 predicate that has not yet enrolled a first participant",
            ),
            (
                "number",
                "Results",
                "n = 220 across eight high-volume centers, targeting a hazard ratio of 0.60 on the endpoint",
            ),
            (
                "bullet",
                "LLM Trust",
                "Randomization against standard of care converts a simulation result into a comparative claim",
            ),
            (
                "bullet",
                "LLM Benefit",
                "Shows a cancer center the multi-site path, deposited two days after the Phase 1 protocol",
            ),
        ),
    },
    {
        "number": 16,
        "doi": "10.5281/zenodo.21097442",
        "date": "July 1, 2026",
        "cover": "cover-16-ind-application-daraxonrasib.jpg",
        "reference_title": (
            "Investigational New Drug Application - Daraxonrasib, Phase 1, LLM-Directed "
            "Robotic Whipple in KRAS-Mutated PDAC"
        ),
        "headline": "Investigational New Drug Application, Daraxonrasib Phase 1",
        "items": (
            (
                "bullet",
                "Paper Title",
                "Investigational New Drug Application, Daraxonrasib, Phase 1 Robotic Whipple, July 1, 2026",
            ),
            (
                "bullet",
                "Abstract",
                "A draft initial IND under 21 CFR 312.23 for perioperative daraxonrasib with a robotic Whipple",
            ),
            (
                "number",
                "Strengths",
                "FDA forms, clinical rationale and the RAS(ON) multi-selective mechanism in a single dossier",
            ),
            (
                "number",
                "Limitations",
                "A draft: not an active or agency-endorsed IND, and the live submission system applies",
            ),
            (
                "number",
                "Results",
                "12 modules, 594,657 characters, 22 figures, 84 tables and 52 cross-references, in four days",
            ),
            ("bullet", "LLM Trust", "Every module carries a commit and a source, so a reviewer audits provenance"),
            (
                "bullet",
                "LLM Benefit",
                "This is the filing the trial turns on, and it exists today as a deposited, readable object",
            ),
        ),
    },
    {
        "number": 17,
        "doi": "10.5281/zenodo.21317266",
        "date": "July 12, 2026",
        "cover": "cover-17-funding-application-v2.jpg",
        "reference_title": "Clinical Trial Funding Application v2.0, RFA-RM-27-001, Kawchak K.",
        "headline": "Clinical Trial Funding Application v2.0, RFA-RM-27-001",
        "items": (
            (
                "bullet",
                "Paper Title",
                "Clinical Trial Funding Application v2.0, RFA-RM-27-001, deposited July 12, 2026",
            ),
            ("bullet", "Abstract", "An NIH-adaptable application for a five-year daraxonrasib Phase 1 robotic Whipple"),
            (
                "number",
                "Strengths",
                "Twelve section files carrying cover, strategy, trial synopsis, human subjects and regulatory",
            ),
            (
                "number",
                "Limitations",
                "A drafting resource, not a substitute for SF424, ASSIST or Grants.gov; verify the solicitation",
            ),
            (
                "number",
                "Results",
                "The most complete single funding document in the set, written against a named opportunity",
            ),
            (
                "bullet",
                "LLM Trust",
                "The AI peer review roster is disclosed inside the application, so a funder sees who reviewed it",
            ),
            (
                "bullet",
                "LLM Benefit",
                "Puts a named project and a named applicant in front of a specific NIH mechanism",
            ),
        ),
    },
    {
        "number": 18,
        "doi": "10.5281/zenodo.21720120",
        "date": "July 31, 2026",
        "cover": "cover-18-patient-robot-advocacy.jpg",
        "reference_title": (
            "Patient Robot Advocacy: A Phase 1, First-in-Human, PDAC Clinical Trial Protocol "
            "of a LLM-Directed Robotic Whipple with Daraxonrasib (RMC-6236)"
        ),
        "headline": "Patient Robot Advocacy: Read Before the Consent Conversation",
        "items": (
            (
                "bullet",
                "Paper Title",
                "Patient Robot Advocacy: A Phase 1 First-in-Human PDAC Trial Protocol, July 31, 2026",
            ),
            (
                "bullet",
                "Abstract",
                "The seven things the Phase 1 protocol commits to the participant, each tied to a clause",
            ),
            (
                "number",
                "Strengths",
                "Every commitment names something a participant can check, not something to take on faith",
            ),
            (
                "number",
                "Limitations",
                "Not the consent form and not a substitute for one; two of the cost items remain unsettled",
            ),
            ("number", "Results", "21 documented concerns answered across 30 figures; 27 days of contact, 18 visits"),
            (
                "bullet",
                "LLM Trust",
                "A human surgeon approves every motion, the model has no path to the arms, stop is 3 ms",
            ),
            (
                "bullet",
                "LLM Benefit",
                "Gives the cancer center a document to hand a patient before the consent conversation",
            ),
        ),
    },
    {
        "number": 19,
        "doi": "10.5281/zenodo.21787424",
        "date": "August 4, 2026",
        "cover": "cover-19-ten-funding-applications.jpg",
        "reference_title": (
            "10 Funding Applications: A Phase 1, First-in Human, PDAC Clinical Trial Protocol "
            "of a LLM-Directed Robotic Whipple with Daraxonrasib (RMC-6236)"
        ),
        "headline": "10 Funding Applications for the Phase 1 Robotic Whipple",
        "items": (
            (
                "bullet",
                "Paper Title",
                "10 Funding Applications for the Phase 1 LLM-Directed Robotic Whipple, August 4, 2026",
            ),
            (
                "bullet",
                "Abstract",
                "Ten applications filed as an independent scientist, each answering a specific federal clause",
            ),
            (
                "number",
                "Strengths",
                "Set A leads on the surgical perspective and Set B on medical oncology, redundancy stated",
            ),
            (
                "number",
                "Limitations",
                "Nine of the ten mechanisms fund a person or an institution, not a firm; 05 was the shortest",
            ),
            ("number", "Results", "NIH Pioneer, ARPA-H, NSF TIP, DOE Genesis, NIH SEED, FNIH, HHMI, CTEP, FRO, Moores"),
            (
                "bullet",
                "LLM Trust",
                "Ten filings in one production window, each under a DOI, is throughput made checkable",
            ),
            (
                "bullet",
                "LLM Benefit",
                "Application 10 asks a comprehensive cancer center for one meeting, which is this seminar",
            ),
        ),
    },
    {
        "number": 20,
        "doi": "10.5281/zenodo.21887807",
        "date": "August 11, 2026",
        "cover": "cover-20-independent-scientist-to-novel-performer.jpg",
        "reference_title": (
            "From Independent Scientist to Novel Performer: A Small-Business Operating, "
            "Milestone, and Capitalization Plan for a Phase 1 LLM-Advised Robotic Whipple"
        ),
        "headline": "From Independent Scientist to Novel Performer: The Capitalization Plan",
        "items": (
            (
                "bullet",
                "Paper Title",
                "From Independent Scientist to Novel Performer: A Capitalization Plan, August 11, 2026",
            ),
            (
                "bullet",
                "Abstract",
                "The author converts to small-business operator and rewrites application 05 properly",
            ),
            (
                "number",
                "Strengths",
                "Twelve costed milestones, each with an evidence artifact, a stop condition and a payer",
            ),
            (
                "number",
                "Limitations",
                "$2,104,000 of the five-year direct program sits outside the award and is funded another way",
            ),
            (
                "number",
                "Results",
                "$306,000 Phase I plus $1,300,000 Phase II, against a $3,500,000 five-year direct program",
            ),
            (
                "bullet",
                "LLM Trust",
                "A stop condition written before the work begins is what makes a milestone auditable",
            ),
            (
                "bullet",
                "LLM Benefit",
                "A 15.0% company load against $2,137,000 for identical direct work at a 57% university rate",
            ),
            (
                "bullet",
                "LLM Benefit",
                "$5,900,000 of private capital above the firewall at 3.67 to one, released only on a milestone",
            ),
        ),
    },
)

CLOSING_NOTE = (
    "All twenty works are deposited under a DOI and readable today. "
    "Digital object identifiers resolve through https://doi.org."
)
