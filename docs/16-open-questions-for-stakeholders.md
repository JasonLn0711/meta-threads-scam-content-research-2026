# Open Questions For Stakeholders

## Criminal Investigation Stakeholders

- What counts as report-worthy Threads content from an investigative perspective?
- Are we studying illegal scam, suspicious fraud-like content, or high-risk lures?
- What evidence standard is useful before opening a case?
- Which scam types are currently most operationally painful?
- Are redirection handles, links, or comments more important than original post text?
- Can de-identified examples be shared for research?
- What must never be stored in the research repo?

## Anti-Fraud Office Stakeholders

- What review queue outcome would be useful: high-risk triage, subtype classification, evidence summary, or referral recommendation?
- What false positive rate is tolerable for a research prototype?
- Which categories should be prioritized: investment, loans, jobs, medical claims, impersonation, or other lures?
- Is Threads currently higher priority than other Meta surfaces?
- What reporting volume should the phase-1 sample reflect?
- What format should the final recommendation memo use?

## Legal And Policy Stakeholders

- What collection methods are permitted?
- What platform terms or policy constraints apply?
- Can public Threads examples be stored in redacted form?
- Can screenshots be retained, and under what restrictions?
- Can stakeholder-provided reports be used for annotation?
- What language should be used to avoid legal overclaiming?
- What is the retention and deletion requirement for raw evidence?

## Domain Reviewers

- Which signals are strong enough to mark `scam` under the research guideline?
- Which finance or marketing examples are commonly misread as scam-like?
- How should annotators handle celebrity references?
- How should annotators handle political or medical claims?
- What makes a case `uncertain` rather than `scam`?
- Which evidence fields are most useful during review?

## Engineering And Research Stakeholders

- Is CSV sufficient for first annotation, or is JSONL needed immediately?
- What OCR tool is acceptable for the first local experiment?
- Are LLM-assisted explanations permitted on redacted samples?
- What minimum metrics should decide phase-2 continuation?
- Who owns dataset versioning and schema changes?
