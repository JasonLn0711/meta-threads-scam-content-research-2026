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

### Current Draft Status From 2026-05-21 Screenshot

Repo-safe status only:

| Form field | Current draft status | Action before next step |
|---|---|---|
| Legal first name | Filled; redacted in git | Confirm exact legal spelling. |
| Legal last name | Filled; redacted in git | Confirm exact legal spelling. |
| Preferred name | Filled; redacted in git | Confirm this is the preferred professional display name. |
| Your country | Filled: `Taiwan` | Confirm it matches the organization section. |
| Your state or province | Filled: `Hsinchu` | Confirm consistency with organization address. |
| Your city | Blank | Fill before pressing `Next`; candidate values are `Hsinchu` or `Hsinchu City`. |
| Organizational email | Filled; redacted in git | Confirm institutional mailbox access. |
| Discipline or area of expertise | Filled: `Computer science` | Accept unless a more precise dropdown option is available and better aligned. |
| ORCID ID | Filled; redacted in git | Confirm exact ORCID before submission. |
| Resume or CV | One PDF uploaded; file name redacted in git | Confirm the CV excludes sensitive identifiers and raw case details. |

Visible blocker: the `Next` button appears disabled, likely because `Your city`
is still blank.

## Organization Page

Use the actual form only for final organization values. Public institution
fields can be recorded in repo-safe notes when needed, but department-level
affiliation, role, and applicant-verification URLs should stay outside git
unless explicitly approved.

| Form field | Fill design | Outside-git final value |
|---|---|---|
| Organization name | Exact official institution name. |  |
| Organization country | Country of the affiliated organization. |  |
| Organization type | Closest official dropdown type, usually `Academic institution` for NYCU. |  |
| Organization website | Main official institutional website. |  |
| Department name | Exact department, institute, lab, or program name used by the organization. |  |
| Your role at organization | Closest official role dropdown, such as `PhD student` when accurate. |  |
| Link to your profile or page on your organization's website | Organization-hosted URL that verifies affiliation. Do not use LinkedIn, GitHub Pages, or a personal website. |  |

### Current Organization Draft Status From 2026-05-21 Screenshot

Repo-safe status only:

| Form field | Current draft status | Action before next step |
|---|---|---|
| Organization name | Filled: `National Yang Ming Chiao Tung University` | Confirm official English spelling. |
| Organization country | Filled: `Taiwan` | Confirm consistency with personal-information country. |
| Organization type | Filled: `Academic institution` | Accept if this is the closest dropdown option. |
| Organization website | Filled: `https://www.nycu.edu.tw/` | Confirm it remains the official institutional homepage. |
| Department name | Filled; redacted in git | Confirm exact official department/institute English name. |
| Your role at organization | Filled; redacted in git | Confirm role dropdown matches current appointment/status. |
| Affiliation verification URL | Filled; redacted in git | Confirm the URL actually verifies the applicant's affiliation; prefer a profile, directory, lab, or advisor/research-group page over a generic department homepage. |

Visible state: `Personal information` is complete, `Organization` is active,
and `Next` appears enabled.

## Research Details Page

Use this page to make the research-program case. The page should show that the
request is for public-interest, official, governed research access rather than
app development, platform policing, scraping, or autonomous enforcement.

| Form field | Fill design | Outside-git final value |
|---|---|---|
| Research program title | Short, non-accusatory title that fits the 60-character limit and does not end mid-word. |  |
| Research program description | Public-interest research purpose, bounded method, governance boundary, uncertainty preservation, and reviewer-support goal. |  |
| Relevant data for your research | Public posts, public metadata, engagement indicators, timestamps, topic/hashtag propagation, trend signals, and aggregate dissemination behavior when approved. |  |
| EU systemic-risk contribution | Select only the answer the research can defend. If `Yes`, explain systemic-risk relevance without overclaiming legal attribution or enforcement. |  |
| Research tools | Request the web-based tool and API only when both are necessary for the research design. |  |
| Secure computing platform | Select the approved platform that matches the intended API route. |  |
| Required confirmations | Check only after product documentation has been reviewed and the public-interest/scientific contribution statement is accurate. |  |

### Current Research Details Draft Status From 2026-05-21 Screenshot

Repo-safe status only:

| Form field | Current draft status | Action before next step |
|---|---|---|
| Research program title | Filled: `Metadata-Driven Public Scam Pattern Analysis and Reviewer Su`; counter `60/60` | Shorten or complete the title so it does not end mid-word. |
| Research program description | Filled; counter `1772/4000` | Keep as public-interest, metadata-first, reviewer-support research; avoid adding enforcement or legal-attribution claims. |
| Relevant data for your research | Filled; counter `1552/4000` | Confirm every requested data class is necessary and approved-route compatible. |
| EU systemic-risk question | `Yes` selected | Confirm this is intentional and defensible before submission. |
| Selected research tools | Web-based Meta Content Library selected; Meta Content Library API selected | Keep both only if the API need remains necessary. |
| Secure computing platform | `Meta Secure Research Environment` selected | Confirm this is the intended secure platform. |
| Required confirmations | Both visible confirmations checked | Confirm product documentation has actually been reviewed. |

Full repo-safe transcription:
[../notes/2026-05-21-meta-research-tools-manager-research-details-page.md](../notes/2026-05-21-meta-research-tools-manager-research-details-page.md).

Visible state: `Personal information` and `Organization` are complete,
`Research details` is active, both research-tool selections are checked, both
required confirmations are checked, and `Next` appears enabled.

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
