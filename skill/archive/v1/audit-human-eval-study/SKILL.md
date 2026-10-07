---
name: audit-human-eval-study
description: Audit or revise human-rating study rubrics, questions, and annotation interfaces. Use for study-design review, evidence-backed revisions, or prelaunch checks of supplied previews, settings, and test records.
---

# Audit a human evaluation study

Review the instrument against the study's stated decision. Accept native documents, screenshots, URLs, code, media or datasets; no mandatory schema or complete bundle. Finish a useful review within the available evidence. Use one agent with the host's existing tools; no required services or specialist ensemble.

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

## 4. Report or revise

Lead with reviewed scope and the few most consequential supported findings (usually up to three). For each, name the question or state in owner-facing terms and give observation, evidence, consequence, concrete correction and verification. Keep other verified findings in a compact appendix when needed; do not suppress a real failure because it appeared in only one pass. Keep raw paths, internal IDs, long quotes and traces out of the main prose; use compact evidence notes. Include no private participant content or identifiers.

Separate confirmed defects, plausible risks/recommendations, `cannot_verify`, and `needs_human_judgment`. If reporting check statuses, use `pass`, `fail`, `not_verified`, or `not_applicable` with evidence and scope. A sampled pass is not whole-study certification. Report unavailable branches, settings or storage explicitly. Ask only for the smallest missing artifact that materially affects the requested decision.

When revision is requested, deliver the rater-facing rubric itself separately from audit rationale. Preserve the intended construct, response schema, scale polarity and scoring rules. Put proposed new options, keys, precedence rules or screening policies under **owner decision required**, outside the schema-preserving draft; do not silently insert them. Supply only a labeled partial draft when evidence cannot establish the original instrument. Use exhaustive or machine-readable output only when requested.
