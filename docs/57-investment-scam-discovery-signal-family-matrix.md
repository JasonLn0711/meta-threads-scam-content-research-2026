# Investment Scam Discovery Signal-Family Matrix

## Purpose

Define the signal-family matrix for scalable, stable, and reviewable discovery of Threads investment-scam candidates.

This matrix supports candidate discovery. It does not determine legal fraud, guilt, enforcement action, takedown eligibility, or production detection.

This matrix does not authorize new evidence collection, item `0082`, browser/crawler expansion, confirmed-pointer intake, model training, public release, or raw evidence in git.

## Unit Of Discovery

The method should discover candidates across four units:

| Unit | Description | Review Note |
|---|---|---|
| post candidate | Top-level post has visible investment-scam risk signals | Useful for explicit lures |
| thread candidate | Post plus replies/comments create the risk pattern | Required for comment-layer funnels and supporting-account behavior |
| account-context candidate | Profile or repeated posting pattern strengthens risk | Use only bounded repo-safe context; no graph expansion without separate decision |
| funnel candidate | Visible path points from Threads to DM, group, external contact, or external destination | Candidate discovery only; do not infer unseen private-message content |

## Signal Matrix

| Signal family | Example surface | Discovery value | FP risk | Needs reply? | Needs OCR? | Hard-negative contrast | Review note |
|---|---|---:|---:|---:|---:|---|---|
| investment domain seed | stocks, investing, wealth management, crypto, options, funds | medium | high | no | no | ordinary investment discussion | Use for candidate finding only, never as label by itself |
| private-channel migration | DM, add friend, LINE, Telegram, WhatsApp, Messenger, group movement | high | medium | sometimes | no | normal contact info without investment funnel | Stronger when paired with individualized help, profit proof, or group conversion |
| reply/comment funnel cue | comment-layer contact cue, safe-contact claim, reply coordination | high | medium | yes | no | ordinary Q&A or warning comments | Critical because top-level post may look benign |
| profit-proof | earnings sheet, return screenshot, success proof, gain claims | high | medium | no | often | normal portfolio/performance discussion | Stronger when tied to teacher/advisor, group, or contact migration |
| teacher/advisor framing | teacher, assistant, analyst, mentor, expert, helper | high | medium | sometimes | no | financial education without funnel | Risk rises when authority is tied to private group, individualized holdings help, or profit claims |
| group invitation | stock group, daily watchlist, holdings clinic, join community | high | medium | sometimes | no | ordinary community discussion | Especially important when group is framed as exclusive or action-oriented |
| testimonial/witness cue | other accounts praise results or claim joining helped | medium-high | medium | yes | sometimes | real user feedback without conversion path | Watch for supporting-account coordination or staged reassurance |
| reassurance/no-fee/safety language | not charging, just sharing, anti-scam, safe channel | medium | high | sometimes | no | genuine anti-scam warning | This is camouflage only when combined with funnel or conversion cues |
| external-link/contact signal | visible link/contact type/domain category | high | medium-high | sometimes | no | legitimate public website or official profile | Tracked repo should use presence/category/redacted reference, not raw URL/contact |
| OCR-derived financial claim | image-only returns, stock names, group QR, testimonial, contact text | high | medium | no | yes | educational chart or ordinary screenshot | OCR can surface hidden proof/contact claims, but needs human verification |
| profile-context pattern | repeated investment persona, repeated calls to group/DM, multi-style funnel | medium-high | high | no | no | ordinary finance creator profile | Keep bounded; no follower graph, private graph, or broad profile expansion without decision |
| anti-scam warning hard negative | warning others about scam methods | protective | n/a | sometimes | sometimes | n/a | Do not label scam unless the item creates a new conversion path |
| ordinary investment hard negative | market commentary, personal investing opinion, education | protective | n/a | no | sometimes | n/a | Finance vocabulary alone is insufficient |
| insufficient-evidence fragment | isolated vague investment phrase with no context | protective | n/a | maybe | maybe | n/a | Preserve as `uncertain` or `insufficient_evidence` rather than forcing a label |

## Combination Rules

Single weak signals should usually create candidates, not final labels.

Escalate review priority when multiple signal families converge:

| Combination | Review Priority |
|---|---|
| investment domain seed + private-channel migration | high |
| profit-proof + teacher/advisor framing | high |
| reply/comment funnel cue + external-link/contact signal | high |
| group invitation + individualized holdings help | high |
| no-fee/safety reassurance + group/contact movement | medium-high |
| OCR-derived contact/profit proof + private-channel migration | high |
| profile-context repetition + post/reply funnel cue | medium-high |
| investment vocabulary only | low / hard-negative check |
| anti-scam warning only | hard-negative check |

## Review Questions

For each candidate, reviewers should ask:

1. Which unit is actually suspicious: post, thread, account-context, or funnel?
2. Which signal families are visible?
3. Is a reply/comment needed to understand the risk?
4. Is OCR/image text needed to understand the risk?
5. Is contact or private-channel migration visible?
6. Is there a profit-proof, teacher/advisor, testimonial, or group-conversion pattern?
7. What is the strongest hard-negative explanation?
8. Is evidence sufficient for `scam`, or should it remain `uncertain` / `insufficient_evidence`?
9. Would this candidate be safe and useful for human review at scale?

## Metrics Link

The signal matrix should feed the labor-efficient north-star metrics in [61-labor-efficient-investment-scam-candidate-discovery-north-star.md](61-labor-efficient-investment-scam-candidate-discovery-north-star.md). A future capped method test should measure:

- candidate yield;
- high-risk yield;
- scam-label yield;
- duplicate rate;
- average review time per candidate;
- median review time;
- p95 review time;
- candidates reviewed per hour;
- percentage of fields auto-filled;
- percentage of fields manually corrected;
- summary usefulness rating;
- percentage of candidates requiring full original-thread reading;
- second-review rate;
- disagreement rate;
- hard-negative false-positive pressure;
- false-negative pressure;
- insufficient-evidence rate;
- review-worthy yield per source arm;
- high-risk yield per reviewer hour;
- thread-context dependency;
- OCR dependency;
- private-channel migration rate;
- profile-context dependency.

## Boundary

This matrix is a design artifact. It does not authorize execution.

Any future method test must be opened by a separate capped decision record before candidate discovery begins.
