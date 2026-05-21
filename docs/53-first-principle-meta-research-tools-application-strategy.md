# First-Principle Meta Research Tools Application Strategy

## Purpose

This document records the first-principle strategy for applying to Meta Research Tools Manager for Meta Content Library / API access.

The application should not be framed as an app build, a scraper replacement, a policing system, or a production detector. It should be framed as a public-interest research request for governed access to official research infrastructure.

## Scarce Resource

The scarce resource is not model power or data volume.

The scarce resource is trust:

- trust from Meta and CASD that the research team will not misuse controlled access
- trust from CIB/165 stakeholders that the research preserves evidence boundaries
- trust from reviewers that the system supports human judgement rather than replacing it
- trust from future readers that the repo preserves uncertainty and avoids overclaiming

Therefore, the application must lead with governance, ethics, minimization, and reviewer support before discussing detection performance.

## First-Principle Chain

1. Public social-media scam-like content is ambiguous evidence, not proof of legal fraud.
2. Full-platform collection is not necessary to answer the first research question.
3. Unofficial scraping creates legal, platform, privacy, reproducibility, and stakeholder-trust risk.
4. The regular Threads API is primarily a developer/app route, not a complete research archive.
5. Meta Content Library / API is the official controlled research route where access and surface coverage are approved.
6. Therefore, the right request is not "give us data to catch scammers."
7. The right request is "allow bounded official access so we can study public investment-scam narratives and metadata-based reviewer-support mechanisms."
8. The output should be candidate generation, risk-priority reasoning, and aggregate research findings.
9. The final judgement remains human, and legal/platform enforcement remains outside this repo.

## Recommended Research Question

Use this as the application north star:

> How can metadata-based reviewer-assist systems reduce human review burden while preserving uncertainty awareness and minimizing over-enforcement risks in large-scale public social-media scam monitoring?

A shorter application-facing version:

> Study public investment-scam narratives and metadata-based reviewer-support mechanisms under large-scale social media environments.

## Application Positioning

Lead with:

- public-interest online-harm research
- academic and institutional accountability
- public Threads content only
- data minimization
- metadata-first observation
- human review as the final judgement step
- no autonomous accusation
- no legal fraud determination
- no private messages or private accounts
- controlled raw storage outside git
- aggregate and redacted outputs by default
- clear retention, deletion, and access rules

Do not lead with:

- "catch scam accounts"
- "build a scam classifier"
- "monitor all Threads"
- "automate enforcement"
- "scrape public pages if API access is incomplete"
- "publish account-level examples"

## Minimal Viable Research Architecture

```mermaid
flowchart LR
    A[Approved public Threads source] --> B[Metadata extraction]
    B --> C[Risk feature scoring]
    C --> D[Candidate queue]
    D --> E[Human review]
    E --> F[Aggregate analysis]
```

This architecture keeps the research question operational:

- candidate generation is not accusation
- scoring is prioritization, not verdict
- reviewer routing is the value proposition
- aggregate analysis is the publishable output

## What To Prepare Before Submission

Prepare these before clicking `Get started` in Research Tools Manager:

| Item | Needed content |
|---|---|
| Research purpose | Public-interest study of scam-like public investment narratives and reviewer-support mechanisms. |
| Research question | The metadata-based reviewer-assist question above, or a narrower approved variant. |
| Institutional context | Academic affiliation, lead researcher role, collaborator roles, and accountable organization. |
| Data minimization | Field list, why each field is necessary, and why excluded fields are not needed. |
| Governance boundary | Public data only, no private messages, no autonomous accusation, aggregate reporting. |
| Ethics / IRB position | Whether the work is human-subjects research, needs review, or is exempt/observational. |
| Storage / access / retention | Controlled raw storage, access roles, deletion schedule, and repo-safe outputs. |
| Misuse prevention | No scraping fallback, no account naming, no enforcement claims, no raw evidence in git. |
| Output plan | Aggregate metrics, reviewer-burden analysis, redacted examples only if approved. |

Use `templates/meta_research_tools_application_prep.md` to draft the application materials outside git if sensitive.

## Personal Information Page Strategy

The personal-information page should establish accountable research identity,
not describe the project.

Visible fields and fill guidance are recorded in
[../notes/2026-05-21-meta-research-tools-manager-personal-information-page.md](../notes/2026-05-21-meta-research-tools-manager-personal-information-page.md).
Use exact legal and institutional information in the actual application, while
keeping legal name, organizational email, ORCID, CV file names, uploaded CVs,
application IDs, and access screenshots out of git.

Recommended stance:

- use the applicant's exact legal name from official records;
- use institutional country, state/province, and city consistent with the next
  organization section;
- use an institutional email, not a personal mailbox;
- choose the closest academic discipline category rather than a marketing term;
- upload a concise academic CV if ready, because it strengthens trust and
  eligibility;
- keep CIB-sensitive details, raw evidence, screenshots, handles, URLs, and
  access identifiers out of the CV and repo.

## Organization Page Strategy

The organization page should establish institutional accountability. It should
make it easy for Meta and CASD to verify that the applicant is affiliated with
a legitimate academic organization.

Visible fields and repo-safe filled status are recorded in
[../notes/2026-05-21-meta-research-tools-manager-organization-page.md](../notes/2026-05-21-meta-research-tools-manager-organization-page.md).

Recommended stance:

- use the exact official English institution name;
- use the official institution website;
- use a department/institute/lab name that matches institutional records;
- choose the closest role dropdown, such as PhD student when accurate;
- use an organization-hosted profile, directory, lab, advisor, or research-group
  page for affiliation verification;
- do not use LinkedIn, GitHub Pages, or a personal website;
- do not use this page to discuss CIB operations, raw evidence, scam labels, or
  enforcement claims.

## Research Details Page Strategy

The research-details page is the core trust-review page. It should show why the
research needs controlled official access and why the team can use that access
without turning the project into scraping, policing, public accusation, or
production enforcement.

Visible fields and repo-safe filled status are recorded in
[../notes/2026-05-21-meta-research-tools-manager-research-details-page.md](../notes/2026-05-21-meta-research-tools-manager-research-details-page.md).
The official product-documentation requirements snapshot that supports the
checked product-documentation confirmation is recorded in
[54-meta-official-product-documentation-requirements.md](54-meta-official-product-documentation-requirements.md).

Observed current draft state:

- research title is filled at `60/60` and appears to end mid-word;
- research-program description is filled at `1772/4000`;
- relevant-data explanation is filled at `1552/4000`;
- EU systemic-risk question is answered `Yes`;
- both Meta Content Library web-based tool and Meta Content Library API are selected;
- Meta Secure Research Environment is selected as the secure computing platform;
- both required confirmations are checked;
- `Next` appears enabled.

Recommended stance:

- shorten the title before submission so it does not look truncated;
- keep the description focused on public, aggregate, metadata-first research
  and human reviewer support;
- request only public or platform-approved research data;
- describe API access as necessary for reproducible, scalable analysis inside
  the approved secure environment, not as a general data export path;
- treat Meta Secure Research Environment as a WorkSpaces Secure Browser
  cleanroom with copy, network, download, export, model, and package-management
  restrictions;
- keep `Yes` on the EU systemic-risk question only if the application is ready
  to defend systemic-risk relevance;
- preserve the no private messages, no non-public user data, no autonomous
  enforcement, no legal attribution, and aggregate-output boundaries;
- do not mention raw case evidence, CIB operational details, specific accounts,
  handles, URLs, or screenshots in this page.

## Collaborators Page Strategy

The collaborators page is optional in the visible application UI, but it still
belongs to the access-governance boundary. It should answer whether anyone
besides the lead researcher needs direct approved access.

Visible fields and repo-safe filled status are recorded in
[../notes/2026-05-21-meta-research-tools-manager-collaborators-page.md](../notes/2026-05-21-meta-research-tools-manager-collaborators-page.md).

Observed current draft state:

- `Personal information`, `Organization`, and `Research details` are complete;
- `Collaborators` is active and optional;
- one collaborator email field is visible and blank;
- no additional collaborator rows are visible;
- `Add another` is visible and unused;
- `Next` appears enabled.

Recommended stance:

- proceed with zero collaborators only if the lead researcher can complete the
  application and near-term research workflow without collaborator access;
- add collaborators only when their approved access is necessary for the
  research program;
- use organizational email addresses;
- decide collaborator roles outside git before adding invitations;
- do not store collaborator emails, invitation links, collaborator application
  status, or collaborator personal details in git;
- record only aggregate collaborator state in repo-visible files.

## Claim Boundary

Allowed:

- "The project studies public investment-scam narratives under official research access."
- "The system generates suspicious candidates for human review."
- "The evaluation measures reviewer burden, uncertainty handling, and false-positive pressure."
- "The output is aggregate research evidence and repo-safe decision support."

Not allowed:

- "The system identifies criminals."
- "The dataset captures all Threads scam content."
- "The model determines fraud."
- "API gaps can be bypassed by scraping."
- "Producer lists are scammer lists."

## Relationship To Breeze Guard 26

Breeze Guard 26 may become a later classifier comparison or guardrail candidate, but it should not be used to justify the Research Tools Manager application.

The access request should stand on the research question and governance plan, not on the availability of any single model.

If Breeze Guard 26 is later tested, it should be evaluated as an auxiliary safety-classifier signal for human-review routing on approved redacted text, not as final adjudication.

## Relationship To Versioning

This document is part of the `v1.3.0` repo operating update. It formalizes the shift from generic "API access" language to first-principle Research Tools Manager application strategy.
