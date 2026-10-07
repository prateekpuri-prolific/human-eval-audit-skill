# Skill comparison: interim failure diagnosis

Remaining generation and judging paused at user request on 2026-10-06. This analysis uses completed saved judgments only; no new model calls or skill edits.

## Descriptive results

Common applicable instrument dimensions total 64 points. Five convenience-selected public/synthetic cases, one generation and one blinded Sol judgment per condition; these are not validated human quality scores.

| Model | One-shot | Native bare agent | Native skill agent |
|---|---:|---:|---:|
| Sol |56|60|58|
| Haiku |44|49|43|
| Sonnet |54|56|44|
| Opus |55|55|49|
| Gemini Flash |49|unfinished|49|
| Gemini Pro |incomplete|53|48|

Skill versus native bare is the matched comparison. One-shot versus native also changes tools, runtime and potentially reasoning settings. All 25 completed native skill traces explicitly read SKILL.md; matched completed bare traces show zero reads.

## Concrete failures flagged

- Sonnet skill, case083: requested image edit reversed from red-to-blue to blue-to-red. The audit also describes an added purple rectangle as deleted. Judge flags the proposed instruction reversal critical. This is source fidelity failure, not useful methodological advice.
- Haiku skill, case018: converts physical plausibility into a hard constraint and ranked priority where the source specifies holistic motion preference. Sonnet adds prompt adherence before its scope is resolved. These can change the intended judgment.
- Gemini Pro skill, case018: inserts an unanswered owner question about prompt adherence directly into participant instructions; requests examples there without providing them.
- Opus skill: broadens tie wording to include a hard choice (case018), and narrows No unintended change so the unchanged-image boundary becomes unclear (case083).
- Haiku skill, case083: removes the visible description input while requiring descriptions, and adds storage requirements despite missing implementation. Actual runtime breakage cannot be established without app.js.

Across four complete native model pairs, dimension-point changes (skill minus bare) sum to: operational clarity -6, decision logic -6, construct preservation -5, response anchors -5, workload usability -3, evidence fit -3, examples/boundaries -1. These are descriptive sums of ordinal model judgments; a single source error can affect several dimensions.

## What the skill itself says

The frozen SKILL.md explicitly requires preservation of construct, schema, scale polarity and scoring, and places new precedence/options under owner decision required outside the draft. Instrument methods repeats that requirement and prohibits inventing thresholds, keys or options. Several observed failures violate existing instructions; adding more prose may not solve them. Its broad review checklist and guidance to provide boundary examples may encourage excessive completion, but this is a hypothesis, not isolated causation.

## Measurement limitations

The score measures the proposed instrument, conflating safe abstention with unfinished work. Missing media or implementation can lower scores even when the agent correctly limits its claims. Judge packets omit execution traces, so real browser smoke tests in earlier Sol arms were not available to substantiate test claims. Similar tie-boundary findings and speech-example repairs have been classified inconsistently across outputs. False-alarm counts include speculative or partly valid concerns; they are not calibrated false-positive rates. High total scores can conceal major code regressions. Haiku skill has fewer regression entries (5 versus 8 bare) despite its lower sum.

## Interpretation and next changes to consider

There is no demonstrated skill uplift in this pilot. Some losses are genuine revision regressions; some arise from endpoint and judge limitations. The pattern suggests over-editing and failure to preserve source semantics rather than inability to detect the planted issue. Do not infer a stable model ranking or causal human-data effect.

Before more runs: constrain edits to supported issues; keep owner questions outside participant artifacts; add a final source/schema/construct diff check; score detection, safe abstention, repair fidelity and severity separately from instrument completeness; adjudicate inconsistent keys and matched findings. Freeze changes before repeating evaluation on held-out cases. No such changes were implemented in this pause.

Evidence: private pilot-five-20261006/native-comparison.json, per-job semantic judgments/candidate outputs, frozen-skill/SKILL.md and references/instrument-methods.md. Existing prompt reports in this directory contain one-shot results.
