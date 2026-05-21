# Meta Research Tools Manager Personal Information Page Snapshot

- Date recorded: 2026-05-21
- Source: user-provided screenshot
- Visible page: Meta Research Tools Manager application draft
- Visible URL pattern: `www.facebook.com/research-tools-manager/applications/[redacted-application-id]`
- Repo-safe privacy note: the logged-in account name, application ID, legal name, email address, ORCID, CV file name, and any uploaded file details are intentionally not recorded in git.

## Visible Page State

- Left navigation title: `Research Tools Manager`
- Left navigation selected item: `Your application`
- Application status badge: `Draft`
- Main page heading: `Application`
- Section navigation:
  - `Personal information` is active.
  - `Organization` is listed after personal information.
  - `Research details` is listed after organization.
  - `Collaborators` is listed after research details.
  - `Terms and Conditions` is listed last.
- Main panel title: `Personal information`
- Main panel helper text: `Tell us about who you are and what you do.`
- `Next` button is visible but disabled before required fields are complete.

## Filled Page State From Later Screenshot

The later screenshot shows the personal-information page partially filled.
Because these fields contain personal information, the repo-safe status below
redacts identity-bearing values.

| Field | Repo-safe observed status | Notes |
|---|---|---|
| Legal first name | Filled; value redacted in git | Actual value stored only in ignored private local note if needed. |
| Legal last name | Filled; value redacted in git | Actual value stored only in ignored private local note if needed. |
| Preferred name | Filled; value redacted in git | Optional field was filled in the UI. |
| Your country | Filled: `Taiwan` | Non-sensitive country-level value retained. |
| Your state or province | Filled: `Hsinchu` | Consider consistency with city and organization address before submission. |
| Your city | Blank / not filled | This is the visible likely blocker for the disabled `Next` button. |
| Organizational email | Filled; NYCU organizational email redacted in git | Do not commit the actual email address. |
| Your discipline or area of expertise | Filled: `Computer science` | This matches the computer-science research identity. |
| ORCID ID | Filled; value redacted in git | Do not commit the actual ORCID unless explicitly approved. |
| Resume or CV | One PDF uploaded; file name redacted in git | Do not commit the file name or CV contents. |

Repo-safe interpretation:

- The page is almost complete.
- The visible required field still missing is `Your city`.
- Before pressing `Next`, fill `Your city` and confirm that country,
  state/province, city, organizational email, ORCID, and CV are all intended for
  the formal application.
- Suggested city value candidates are `Hsinchu` or `Hsinchu City`, depending on
  how the applicant wants the address to align with the organization page.

Private actual values, if a local audit trail is needed, belong only in ignored
private storage such as `data/private/`. Do not commit that private note.

## Visible Fields

| Field | Required? | UI note |
|---|---|---|
| Legal first name | Required | Free-text field. |
| Legal last name | Required | Free-text field. |
| Preferred name | Optional | Free-text field. |
| Your country | Required | Dropdown. |
| Your state or province | Required | Free-text field. |
| Your city | Required | Free-text field. |
| Organizational email | Required | UI says this should be the email associated with the research institution or organization. |
| Your discipline or area of expertise | Required | Dropdown with placeholder `Select`. |
| ORCID ID | Optional | UI describes this as the unique persistent digital identifier provided by ORCID. |
| Resume or CV | Optional | PDF upload area with drag-and-drop or choose-file control. |

## First-Principle Filling Strategy

The scarce resource in this application is trust. The personal-information page
should establish that the applicant is a real, accountable academic researcher
using an institutional identity.

Fill the page with exact identity and affiliation information. Do not use
marketing language, project claims, CIB-sensitive details, raw evidence, or
application strategy text in this section.

## Field Filling Design

| Field | Recommended filling rule | Draft value design |
|---|---|---|
| Legal first name | Use the exact legal given name used by the applicant's institution, passport, or official research records. Do not infer from the logged-in display name unless it matches legal records. | Use the applicant's legal given name. If the legal English given name is `Sheng`, use `Sheng`; otherwise use the official legal form. |
| Legal last name | Use the exact legal family name used by the applicant's institution, passport, or official research records. | Use the applicant's legal family name. If the legal English family name is `Lin`, use `Lin`; otherwise use the official legal form. |
| Preferred name | Optional. Use only if the applicant normally publishes or corresponds under a different name. Keep it simple; do not add titles. | Leave blank if the legal name is already the preferred professional name. Otherwise use the professional display name used in publications or institutional pages. |
| Your country | Use the country tied to the applicant's institutional research identity and current application context. | For this NYCU / Taiwan public-interest research framing, use `Taiwan` if the dropdown supports it and it is accurate for the applicant. |
| Your state or province | Use the applicant's institution or research-base region. Keep it consistent with the organization address that will be entered in the next section. | For NYCU, use `Hsinchu City` if free text is accepted. If the form expects province-level text, use the closest official region used by the organization. |
| Your city | Use the applicant's institution or research-base city. | For NYCU, use `Hsinchu City` if accurate. |
| Organizational email | Use an institutional email associated with the university or research organization. Do not use Gmail or a personal email if an institutional email is available. | Use the applicant's NYCU organizational email. Do not record the actual address in git. |
| Your discipline or area of expertise | Choose the closest official dropdown category to the researcher's academic identity, not the project buzzword. | First choice: `Computer and Information Sciences` or closest equivalent. If unavailable, choose the closest option such as `Computer Science`, `Information Science`, `Data Science`, `Artificial Intelligence`, or `Cybersecurity`, depending on the dropdown. |
| ORCID ID | Recommended if available, because it strengthens research identity. Use the exact ORCID identifier format requested by the form. | Enter the applicant's ORCID if already available. If unavailable, leave blank or create/verify an ORCID before submission if time allows. Do not record the ORCID in git unless explicitly approved. |
| Resume or CV | Optional in UI, but recommended for this access request because it supports trust, eligibility, and research identity. Upload a concise academic CV PDF. | Upload a PDF CV prepared outside git. It should emphasize NYCU affiliation, PhD status, AI governance, cybercrime/online harm, Trust & Safety, data governance, publications, and relevant research projects. Omit national ID, home address, personal phone, birthdate, raw case details, credentials, and sensitive stakeholder material. |

## Recommended CV Content For This Application

The CV should support the access request, not sell a product.

Include:

- Current academic affiliation and PhD status.
- Research areas: AI governance, cybercrime, online harms, Trust & Safety, social-media scam research, reviewer-support systems, and data governance.
- Relevant publications, papers, reports, or project artifacts.
- Methods expertise: metadata analysis, human-review workflows, evaluation design, privacy-aware data handling, and reproducible research.
- Public-interest or government-facing research context at a non-sensitive level.

Avoid:

- National ID, home address, personal phone, or private personal identifiers.
- Raw Threads examples, screenshots, handles, URLs, or evidence details.
- Claims that the applicant can identify criminals, determine fraud, or enforce platform actions.
- Confidential CIB operational details.

## Fill Order

1. Confirm legal name spelling from institutional or passport records.
2. Confirm the organizational email is active and accessible.
3. Confirm country, state/province, and city match the organization section that will be submitted next.
4. Choose the discipline category from the dropdown; prefer the closest academic field over a marketing term.
5. Add ORCID only if accurate.
6. Upload a current academic CV PDF if ready.
7. Proceed to `Organization` only after the page contains no personal placeholders.

## Repo Boundary

This note records the form structure and filling strategy only. It does not
record the completed application values. Filled personal-information drafts,
CVs, ORCID values, and organizational email addresses should stay outside git
unless explicitly redacted and approved.
