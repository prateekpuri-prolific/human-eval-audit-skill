# Original study baseline vs revised instruments (delta)

Method: the existing BASELINE_JUDGE.md prompt (original materials only; no candidate, no key, arm hidden) scored the five original studies on the seven dimensions, 2 Sol runs (baseline-v3/). Delta = revised-instrument score from the earlier key-aware Sol judgment minus the original baseline score, over the same dimensions per case, run-averaged baseline.
Comparability limit: the baseline and revised scores come from different prompts (the revised judgment saw the candidate and the evaluator key), so deltas are indicative, not a clean paired measurement. Case-002 is excluded (the baseline judge marked evidence_fit not assessable, and workload in one run). The case-028 maximum is 8 (fewer assessable dimensions).

Original baseline (of max): case-018 control 12.5/14; case-028 defect 3.5/8; case-083 insufficient evidence 9/14; case-088 defect 7.5/14.

## Revised minus original, per case (positive = revision improved on the original)
| model arm | 018 control | 028 defect | 083 partial | 088 defect |
|---|---|---|---|---|
| haiku bare | -4.5 | +2.5 | 0.0 | +6.5 |
| haiku skill | -5.5 | +3.5 | +1.0 | +1.5 |
| sonnet bare | -0.5 | +4.5 | +1.0 | +6.5 |
| sonnet skill | -3.5 | +2.5 | -3.0 | +5.5 |
| opus bare | +1.5 | +3.5 | +1.0 | +5.5 |
| opus skill | -2.5 | +2.5 | 0.0 | +6.5 |
| gemini-pro bare | +0.5 | +3.5 | 0.0 | +6.5 |
| gemini-pro skill | -4.5 | +2.5 | +1.0 | +6.5 |
| gemini-flash skill | -0.5 | +1.5 | 0.0 | +5.5 |

## Reading
- On planted-defect cases (028, 088) every arm improves on the original, often by a large margin. Revision works where there is something to fix.
- On the no-defect control (018) the judge scores the original at 12.5/14, and most revisions score lower than the original (all skill arms, plus Haiku and Sonnet bare). Only Opus bare and Pro bare finish at or above the original. So on this control the judge says the original was better left mostly alone, which differs from the audit-benchmark view that it had minor warranted gaps (see the adjudication and reference work). Both judge views reflect the same limit: a quality score cannot tell a warranted clarification from an unapproved decision.
- On the insufficient-evidence case (083) revisions are about neutral, except Sonnet with skill (-3.0), the image-misreading run.
- Skill arms are not ahead of bare here, consistent with earlier results. This is revision-quality, which the v2/v2.1 skill de-emphasises by default.
