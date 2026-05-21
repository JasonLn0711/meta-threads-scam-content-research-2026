# Meta Research Tools Manager Application Flow Snapshot

- Date recorded: 2026-05-21
- Source: user-provided screenshot
- URL visible in browser: `www.facebook.com/research-tools-manager`
- Page title / app: Meta Research Tools Manager
- Repo-safe privacy note: the left sidebar shows a logged-in account identity, but the name is intentionally omitted from this note.

## Visible Page State

- Left navigation title: `Research Tools Manager`
- Selected navigation item: `New applications and invites`
- Main panel heading: `Apply to access research tools`
- Primary action button under Step 1: `Get started`
- Bottom-left navigation control: `Collapse`

## Application Draft Personal Information Page

A later user-provided screenshot showed the application draft after `Get
started`, at the `Personal information` section. The visible page contains
fields for legal first name, legal last name, preferred name, country,
state/province, city, organizational email, discipline or area of expertise,
ORCID ID, and resume/CV upload.

The repo-safe field transcription and filling strategy are recorded in
[2026-05-21-meta-research-tools-manager-personal-information-page.md](2026-05-21-meta-research-tools-manager-personal-information-page.md).
The visible application ID and logged-in account identity are intentionally not
recorded in git.

## Application Draft Organization Page

A later user-provided screenshot showed the application draft at the
`Organization` section after personal information was completed. The visible
page contains fields for organization name, organization country, organization
type, organization website, department name, role at organization, and an
organization-hosted profile or page URL used to verify affiliation.

The repo-safe field transcription and filling status are recorded in
[2026-05-21-meta-research-tools-manager-organization-page.md](2026-05-21-meta-research-tools-manager-organization-page.md).
The visible application ID, logged-in account identity, and affiliation details
that directly identify the applicant are intentionally not recorded in full in
git.

## Application Draft Research Details Page

A later user-provided screenshot showed the application draft at the
`Research details` section after personal information and organization were
completed. The visible page contains fields for research program title,
research program description, relevant data, EU systemic-risk contribution,
research-tool selection, secure computing platform selection, and required
confirmations.

The full repo-safe field transcription and filling status are recorded in
[2026-05-21-meta-research-tools-manager-research-details-page.md](2026-05-21-meta-research-tools-manager-research-details-page.md).
The visible application ID, logged-in account identity, screenshots, and any
private access or controlled-content artifacts are intentionally not recorded in
git.

## Application Draft Collaborators Page

A later user-provided screenshot showed the application draft at the
`Collaborators` section after personal information, organization, and research
details were completed. The visible page is marked optional and contains a
blank collaborator email field, an `Add another` control, and `Back`, `Save`,
and `Next` controls.

The full repo-safe field transcription and filling status are recorded in
[2026-05-21-meta-research-tools-manager-collaborators-page.md](2026-05-21-meta-research-tools-manager-collaborators-page.md).
The visible application ID, logged-in account identity, screenshots,
collaborator email addresses, invitation links, and any private access or
controlled-content artifacts are intentionally not recorded in git.

## Application Flow Shown In The UI

### Step 1: Submit Application

Visible instruction:

- Before beginning the application, review the application guide and product documentation for Meta Content Library.
- The Secure Data Access Center (CASD) independently reviews applications for access to Meta Content Library.
- The lead researcher of the team should submit an application about the research program, organization, and collaborators.
- Filling out the application can take more than 30 minutes.
- Progress can be saved and the application can be completed across multiple sessions.

Operational implication for this repo:

- The CIB/165 Threads case should treat the Research Tools Manager application as a formal access-control step, not a casual API signup.
- The lead researcher, organization, collaborator list, research program description, and intended use should be aligned before pressing `Get started`.
- Do not put completed application text, collaborator personal data, or access credentials in git.

### Step 2: Application Review

Visible instruction:

- CASD reviews the application to determine whether the research program is eligible for Meta Content Library access.
- This process can take 2 to 3 weeks.
- Application status can be tracked in Research Tools Manager.

Operational implication for this repo:

- Treat the application-review period as a schedule dependency.
- Record only repo-safe status such as `submitted`, `under_casd_review`, `approved`, `rejected`, or `needs_revision`.
- Keep detailed application correspondence, reviewer comments, and any sensitive eligibility material outside git unless explicitly approved and redacted.

### Step 3: Application In Process

Visible instruction:

- Meta's processing typically takes 2 to 3 weeks after the application review.

Operational implication for this repo:

- Access is not available immediately after CASD review.
- Pilot planning should include an additional Meta processing window after eligibility review.
- Do not start API-based collection until access details are actually received and the controlled launch record confirms the approved route, environment, fields, storage, retention, and redaction limits.

### Step 4: Gain Access

Visible instruction:

- The applicant receives an email with access details.

Operational implication for this repo:

- The access email is sensitive operational material.
- Do not commit emails, invitation links, tokens, credentials, access screenshots, or cleanroom details.
- Repo-visible notes may record only non-sensitive access status and high-level route availability.

## Research Planning Consequences

- Expected access lead time is at least two staged windows: CASD review of 2 to 3 weeks, then Meta processing of 2 to 3 weeks.
- The application can require more than 30 minutes and may span multiple sessions.
- The lead researcher should prepare the research program description, organization information, and collaborator information before starting.
- The official application path reinforces the repo rule that Meta Content Library / API access is governed and approval-based.
- Threads pilot collection should not assume API availability until the Research Tools Manager status and access email confirm it.

## What This Page Represents

The visible page means the researcher is inside Meta's official Research Tools Manager application entrypoint.

This is not a normal developer API page and should not be treated as an app-building workflow. It is a research-grade data-access application system.

The practical framing is:

| Wrong mental model | Correct mental model |
|---|---|
| Build an app with Meta APIs | Demonstrate eligibility for controlled research access |
| Collect as much data as possible | Request the minimum official data needed for a public-interest research question |
| Detect or accuse scam accounts | Study scam-like public narratives and route suspicious candidates to human review |
| Treat access as a technical setup task | Treat access as governance, ethics, privacy, and institutional trust review |

The applicant is not merely asking Meta for API credentials. The applicant is asking Meta and CASD to trust the research program, the institution, the collaborators, and the data-handling plan.

## What Meta And CASD Are Likely Evaluating

The application should be prepared as if reviewers are evaluating these questions:

| Review question | What reviewers are likely checking |
|---|---|
| Who are you? | Whether the researcher is credible and accountable. |
| Who do you represent? | Whether there is institutional backing and a responsible organization. |
| What are you studying? | Whether the research has a scientific or public-interest purpose. |
| How will data be handled? | Whether the project has safe storage, access control, minimization, retention, and redaction. |
| How will misuse be prevented? | Whether the project has governance controls rather than uncontrolled scraping or exposure. |
| Do you understand ethics? | Whether IRB, privacy, safety, and human-subjects questions have been considered. |
| Will this become a scraping business? | Whether the project respects official access limits and does not become bulk harvesting. |

## CASD Interpretation

The screenshot names the Secure Data Access Center (CASD) as the independent reviewer for Meta Content Library access.

For this repo, CASD should be treated as a third-party research data-governance review body, not as a normal Meta developer-support queue.

Operational implication:

- Write the application for a governance reviewer, not for a developer API reviewer.
- Expect questions about data minimization, ethics, privacy, public-interest value, and misuse prevention.
- Do not frame the project as platform policing or account takedown.

## Project Advantages To Emphasize

This project has a stronger application posture when it emphasizes:

- NYCU PhD / academic research context.
- AI governance focus.
- Cybercrime and online-harm research framing.
- Metadata-first methodology.
- Reviewer scarcity as the operational problem.
- Human-review routing instead of autonomous enforcement.
- Public-interest investment-scam research.
- Uncertainty-aware analysis.
- No private messages.
- No de-anonymization as a research goal.
- No public accusation of individual accounts.
- Aggregate reporting by default.

These points matter because they distinguish the project from a requester who only wants broad data access.

## Recommended Application Framing

Avoid:

> I want to catch scam accounts.

Prefer:

> Study public investment-scam narratives and metadata-based reviewer-support mechanisms under large-scale social media environments.

For the research question, avoid:

> Build a scam classifier.

Prefer:

> How can metadata-based reviewer-assist systems reduce human review burden while preserving uncertainty awareness and minimizing over-enforcement risks in large-scale public social-media scam monitoring?

For system purpose, avoid:

> Automatically identify bad actors.

Prefer:

> Generate and prioritize suspicious public-content candidates for authorized human review, with transparent reasons, missing-evidence flags, and aggregate research reporting.

## Public-Interest Rationale

Investment-scam research can be framed as public-interest research because it connects to:

- online harms
- fraud and scam exposure
- financial consumer protection
- cybercrime intelligence
- social engineering narratives
- platform transparency
- reviewer-burden reduction
- safer AI-assisted moderation infrastructure

The application should avoid promising full-platform detection or enforcement. It should describe a bounded study of public scam-like narratives and review-support methods.

## Data Governance Points To Lead With

The strongest governance boundary is:

- public data only
- no private messages
- no private accounts
- metadata-first analysis
- data minimization
- no autonomous accusation
- no account naming in repo outputs
- no legal or fraud determination
- human review required
- aggregate reporting by default
- controlled raw storage outside git
- retention and deletion rules recorded before collection
- query, field, and export limits recorded per run

These should be included before discussing model performance.

## Why Research Access Is Necessary

The application should explain why normal approaches are insufficient:

- unofficial scraping creates platform, legal, privacy, and reproducibility risk
- the regular Threads API is primarily an app/developer API and is not designed for broad research-scale public-discourse analysis
- investment-scam narratives require trend, keyword, and producer-level context to understand diffusion and reviewer burden
- official access creates a safer and more auditable path for public-interest research
- secure environment access and field limits help reduce misuse risk

The point is not "we need more data." The point is "official research access is the safer, more governable, more reproducible way to answer this public-interest question."

## Human Subjects And Ethics Questions

Prepare for questions about:

- whether the research involves human subjects
- whether IRB review is required
- whether personal data or account identifiers are collected
- whether outputs could expose or accuse individuals
- whether the project will publish examples
- whether the project can work with aggregate results or redacted examples

The safest direction is metadata-level observational research with controlled raw access, redacted working artifacts, aggregate outputs, and no de-anonymization goal.

## Minimal Viable Research Architecture

Use this architecture when explaining the project:

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

The mature Trust & Safety framing is:

> AI does not decide who is bad. AI helps allocate scarce review capacity across a large public information stream.

## Pre-Application Work To Finish Before Clicking Get Started

Do not rush the application. Prepare these first:

1. Research question.
2. Public-interest purpose.
3. Governance boundary.
4. Minimal viable research architecture.
5. Data minimization statement.
6. Field list and why each field is necessary.
7. Raw storage, access, retention, and deletion plan.
8. IRB or ethics-review position.
9. Collaborator and organization list.
10. Description of expected outputs, with aggregate and redacted outputs as the default.

## Repo-Safe Status Fields To Track

Use these fields in outside-git controlled records or repo-safe aggregate notes:

- Research Tools Manager application status.
- Application submitted date.
- CASD review status.
- Meta processing status.
- Access email received: yes / no.
- Approved tool route: Meta Content Library UI, Content Library API, both, or neither.
- Threads availability through the approved environment.
- Download/export availability and approval status.
- Approved field list and minimization rationale.

Do not track raw application text, collaborator personal data, account identity, emails, access links, credentials, or screenshots in git.
