---
name: audit-human-eval-study
description: Audit human-rating study rubrics, questions, and annotation interfaces, and surface ambiguities for the owner to resolve. Edits to rater-facing text happen only with the owner's explicit permission. Use for study-design review or prelaunch checks of supplied previews, settings, and test records.
---

# Audit a human evaluation study

Review the instrument against the study's stated decision. Accept native documents, screenshots, URLs, code, media or datasets; no mandatory schema or complete bundle. Finish a useful review within the available evidence. Use one agent with the host's existing tools; no required services or specialist ensemble.

## 0. Authority: audit and suggest by default

Decide first what the user has authorised. A request to review, audit, check, improve or "tell me what you think" authorises findings, questions and proposed options, **not** changes to the study's meaning. Treat edits to rater-facing text as authorised only when the user says so explicitly (for example "revise it", "apply your fixes", "use your judgment on open choices"). Without that, never present a rewritten rubric as the result and never settle an open choice yourself.

Many problems in a rubric are not errors but under-specification: the study owner has not said what a term or rule means, and each reading would change what raters choose. Resolving such a point is a decision about the study's purpose, so it belongs to the owner.

## 1. Discover

Inspect supplied artifacts and their directly relevant links. Identify the target decision/population if stated, rating unit, modality, response form, study version and safe interaction scope. Keep a small working evidence map: artifact/source pointer, availability (`supplied`, `accessible_uninspected`, `inspected`, `unavailable`), version, and what it can establish. Missing access limits coverage; it is not a study defect. Do not require the user to fill out an intake form or obtain optional access before doing useful work.

## 2. Collect

Read [evidence collection](references/evidence-collection.md) when inputs span multiple artifacts, need extraction, or include a preview/recording. For a self-contained rubric, read it directly. Collect only the evidence needed for applicable checks; preserve wording, scale direction, branches, candidate identity and provenance. Keep the working packet in context unless a saved record is useful or requested.

If screenshots, recordings, a URL or runnable UI are supplied, inspect them and provide the supported UI feedback. Exercise only safe, authorized preview interactions. Stop short of live submissions, new terms, or production changes; a preview label alone does not authorize writes. Missing tools or access should be reported, not replaced with imagined observations. A targeted return to collection is appropriate when a consequential finding depends on an accessible missing fact.

## 3. Review — load only applicable guidance

| Available evidence / requested review | Read |
| --- | --- |
| Instructions, questions, scales, examples; rubric revision | [Instrument methods](references/instrument-methods.md) |
| Screenshot, recording, preview, or media presentation | [Modality and UI](references/modality-and-ui.md); use the relevant modality sections |
| Settings, assignment code/configuration, completion flow, test response records | [Integration checks](references/integration-checks.md) |

Capabilities combine independently: test records can support mapping checks without a browser; screenshots cannot establish interactions. Distinguish source wording, rendered behavior, configured intent and stored data. Apply deterministic comparisons where evidence supports them; identify the exact record/state behind a failure. Do not call a heuristic suggestion a failed check.

Review ordinary, boundary and missing-evidence cases where available. Keep fixed ordinal order and meaningful sequences distinct from candidate-side/item randomization. Neither missing attention checks nor straightlining alone proves a defect. Repeated model agreement is not validation; verify consequential findings against sources. Agent task-taking can exercise UI paths but cannot certify human comprehension, fatigue, preference distributions or IRR gains. Do not add synthetic-persona forecasts to the default audit.

## 4. Report: findings, owner questions, determined fixes

Lead with reviewed scope and the most consequential supported findings, then the rest compactly. Leading with a few is about order, not a cap: report every supported defect and every material ambiguity you find, each as a short entry, and do not drop one because a stronger finding already exists. Separate three kinds of item:

**Determined fixes.** The owner's own materials settle the answer: an example that contradicts its own scale, rater text that omits something the study description requires (for example an exclusion or a replay rule), a schedule that confounds position with system. State the observation, the evidence quote, the consequence and the exact correction. These may be proposed as ready-to-apply patches. Applying them is still an edit, so apply only with permission.

**Open ambiguities (owner questions).** Wherever a term, criterion, option boundary or precedence is undefined, do not choose a reading. Look systematically at: undefined evaluative terms ("better", "plausible", "natural", "convincing"); precedence among several criteria; scope against adjacent constructs (for example prompt adherence versus the stated construct); tie versus hard-to-decide versus cannot-assess; partial or one-sided failures; what an example is meant to teach. For each ambiguity give:
1. what is unclear, with a short source quote;
2. how raters' answers would differ under each reading, concretely;
3. two or three plausible options, each with draft wording the owner could adopt;
4. a recommended default and the reason;
5. one clear question for the owner, and whether resolving it changes what the study measures.
Never put an unanswered owner question, a bracketed note or a chosen reading into rater-facing text. If a question tool is available and the user is present, ask the questions before drafting any revision; otherwise list them in the output and stop short of settling them.

Before finalising, do a coverage sweep: go through every rater-facing statement and response option once more and confirm each undefined term, precedence question, scope boundary and edge case is either reported or deliberately judged not to matter.

**Limits.** Report what cannot be verified (absent media, interface, implementation, responses) as `cannot_verify` and do not describe content you have not seen.

Calibrate labels: use `confirmed_defect` only when a quoted source establishes it; use `plausible_risk` for effects that depend on how raters or the interface behave; use `cannot_verify` or `needs_human_judgment` otherwise. Before citing a source, re-read the quoted passage and check you have not misread direction, colour, side or scale. For images, SVG, markup, configuration or code, state a fact about them only after reading the exact value (a fill or colour, a coordinate, a left/right assignment, a sign, a default) and quote that value; check which file is the original and which is the edited or candidate version. If you cannot read a value, say `cannot_verify` instead of describing it. A study with no planted defect is still rarely flawless: report real gaps, but do not manufacture defects or declare the study ready.

Separate confirmed defects, plausible risks/recommendations, `cannot_verify`, and `needs_human_judgment`. If reporting check statuses, use `pass`, `fail`, `not_verified`, or `not_applicable` with evidence and scope. A sampled pass is not whole-study certification. Keep raw paths, internal IDs, long quotes and traces out of the main prose. Include no private participant content or identifiers. Ask only for the smallest missing artifact that materially affects the requested decision.

## 5. When revision is explicitly authorised

Deliver the rater-facing rubric separately from audit rationale. Preserve the intended construct, response schema, scale polarity and scoring rules. Apply determined fixes and any owner-answered decisions. Keep every unanswered question outside the draft, under **owner decision required**. Supply only a labeled partial draft when evidence cannot establish the original instrument. List each judgment call you made so the owner can review it.
