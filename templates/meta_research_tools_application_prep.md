# Meta Research Tools Application Prep

Use this template before starting a Meta Research Tools Manager application. Filled versions may contain sensitive institutional, collaborator, access, or ethics details. Keep filled versions outside git unless fully redacted and explicitly approved.

## Application Identity

- Prep record ID:
- Date:
- Lead researcher:
- Organization / institution:
- Collaborators:
- Related project:
- Intended Meta tool route: Meta Content Library UI / Content Library API / both / unknown pending approval

## Personal Information Page

Use the actual form only for final personal values. Do not store legal name,
organizational email, ORCID, CV file name, or uploaded CV contents in this repo
unless explicitly redacted and approved.

| Form field | Fill design | Outside-git final value |
|---|---|---|
| Legal first name | Exact legal given name from institutional, passport, or official research records. |  |
| Legal last name | Exact legal family name from institutional, passport, or official research records. |  |
| Preferred name | Optional; leave blank if legal name is already the professional name. Do not add titles. |  |
| Your country | Country tied to the applicant's institutional research identity and application context. For NYCU/Taiwan framing, use `Taiwan` if accurate and available. |  |
| Your state or province | Region consistent with the organization address. For NYCU, use `Hsinchu City` if free text is accepted and accurate. |  |
| Your city | City consistent with the organization address. For NYCU, use `Hsinchu City` if accurate. |  |
| Organizational email | Institutional email associated with the research institution or organization; avoid personal Gmail when an institutional email exists. |  |
| Discipline or area of expertise | Choose the closest academic dropdown category, preferably `Computer and Information Sciences`, `Computer Science`, `Information Science`, `Data Science`, `Artificial Intelligence`, or `Cybersecurity`, depending on available options. |  |
| ORCID ID | Optional but recommended if the applicant has an accurate ORCID. |  |
| Resume or CV | Optional in the UI, but recommended. Upload a concise academic CV PDF prepared outside git. |  |

CV should emphasize academic affiliation, PhD status, AI governance, cybercrime
or online-harm research, Trust & Safety, data governance, publications, and
privacy-aware methods. Do not include national ID, home address, raw Threads
examples, screenshots, handles, URLs, credentials, or confidential stakeholder
details.

## Research Purpose

Recommended framing:

> Study public investment-scam narratives and metadata-based reviewer-support mechanisms under large-scale social media environments.

Working research question:

> How can metadata-based reviewer-assist systems reduce human review burden while preserving uncertainty awareness and minimizing over-enforcement risks in large-scale public social-media scam monitoring?

Project-specific research question:

-

Public-interest rationale:

-

What the project is not doing:

- Not building an autonomous enforcement system.
- Not making legal, financial, or criminal determinations.
- Not naming or accusing individual accounts in repo outputs.
- Not collecting private messages or private account content.
- Not replacing official access limits with scraping.

## Data Governance Boundary

Mark each item as planned, not planned, or pending review.

| Boundary | Status | Notes |
|---|---|---|
| Public data only |  |  |
| No private messages |  |  |
| No private accounts |  |  |
| Metadata-first analysis |  |  |
| Data minimization |  |  |
| Human review required |  |  |
| No autonomous accusation |  |  |
| Aggregate reporting by default |  |  |
| Controlled raw storage outside git |  |  |
| Retention and deletion rule |  |  |
| Redaction before repo-visible artifacts |  |  |

## Why Official Research Access Is Necessary

Explain why the regular Threads API or unofficial scraping is insufficient:

-

Explain how official access reduces risk:

-

Explain why the requested fields are the minimum needed:

-

## Minimal Viable Research Architecture

```text
Public Threads posts
        |
        v
Metadata extraction
        |
        v
Risk feature scoring
        |
        v
Candidate queue
        |
        v
Human review
        |
        v
Aggregate analysis
```

Human-review role:

-

Uncertainty handling:

-

Reviewer-scarcity measurement:

-

## Ethics And Human Subjects

- IRB status:
- Human-subjects position:
- Personal data expected:
- PII minimization plan:
- Publication or example-sharing restriction:
- De-anonymization risk mitigation:
- Harm or over-enforcement risk mitigation:

## Requested Tool Capabilities

| Capability | Needed? | Rationale | Governance control |
|---|---|---|---|
| Keyword search |  |  |  |
| Trend analysis |  |  |  |
| Producer lists |  |  |  |
| API access |  |  |  |
| Download/export |  |  |  |
| Engagement or view metrics |  |  |  |

## Pre-Submission Checklist

- [ ] Research question is specific and public-interest oriented.
- [ ] Governance boundary is written.
- [ ] Field minimization is justified.
- [ ] Storage, access, retention, and deletion plan exists.
- [ ] IRB or ethics-review position is documented.
- [ ] Collaborator list is complete.
- [ ] No application wording implies autonomous accusation or enforcement.
- [ ] No application wording implies full-platform coverage.
- [ ] No application wording implies scraping as a fallback.
