# Step 1a: re-slicing existing native-agent judgments (no model calls)

Source: native-comparison.json (GPT-6 Sol judgments, 5 cases, 1 run per cell). Script: `rescore_axes.py`; row-level output in data/private/.../rescore-axes.json. Gemini Flash bare excluded (incomplete). Flash skill has no paired baseline.
Case types from the issue keys: planted defect (002, 028, 088), matched control with no defect (018), insufficient evidence (083). Cells are tiny (control n=4 runs, one per model); treat as hypothesis-generating.

## Score by case type, Haiku/Sonnet/Opus/Gemini Pro pooled
| Case type | Arm | Score | Planted detected | False alarms / run | Regressions / run |
|---|---|---|---|---|---|
| Planted defect (n=12) | bare | 89% | 12/12 | 0.17 | 0.00 |
| Planted defect (n=12) | skill | 80% | 12/12 | 0.17 | 0.08 |
| Control, no defect (n=4) | bare | 84% | n/a | 1.25 | 1.00 |
| Control, no defect (n=4) | skill | 61% | n/a | 1.75 | 1.50 |
| Insufficient evidence (n=4) | bare | 68% | n/a | 3.00 | 1.50 |
| Insufficient evidence (n=4) | skill | 62% | n/a | 1.75 | 1.00 |

Control case 018, bare to skill: Haiku 8 to 7, Sonnet 12 to 9, Opus 14 to 10, Gemini Pro 13 to 8 (4 of 4 down).

## What this changes in the earlier diagnosis
- Detection of planted defects is 12/12 in both arms. The gap sits in revision quality and, mostly, in restraint cases (no defect, missing evidence).
- Skill drops are concentrated in construct_preservation, decision_logic and operational_clarity, i.e. revision dimensions (Sonnet construct 10 to 7).
- NOT supported: "checklist leads to more findings, then more edits." Mean findings per run: Haiku 4.4 vs 3.8, Sonnet 5.0 vs 4.6, Opus 5.4 vs 6.0, Pro 2.4 vs 2.4. Revised artifacts are MORE similar to the originals with the skill (difflib similarity: Haiku 0.46 to 0.73, Sonnet 0.73 to 0.79, Opus 0.79 to 0.82, Pro 0.96 to 0.91). Failures are wrong or unwarranted edits, not larger edits.
- Skill costs: see seconds and cost_usd in rescore-axes.json.
- The per-model "detect %" printed by the script mixes planted and non-planted issue rows and is not meaningful; use the planted-only table above.
- owner_decisions_separated verdicts are inconsistently typed by the judge (True/'yes'/'partial'); not usable without normalising. Heuristic owner-text leak count: only Haiku (2/2) and Gemini Pro skill (2) had hits.

## Not yet done
- Judge test-retest and a second-family judge (requires paid calls; awaiting authorization).
- Splitting the judge prompt into audit vs revision axes (requires rejudge).

## Control case-018: was the baseline "already perfect"? No (free analysis of existing outputs)
- The issue key itself says no-planted-defect is not a claim the study is flawless, and that evidence-supported unrelated improvements are allowed.
- Real gaps in the original participant.md versus study.md: it never says to read the prompt first, never states replay/reset-both is allowed, never says audio is out of scope (study.md does), never poses the response question, and never defines Left/Right.
- The two highest control scores made exactly those grounded edits: Opus bare 14/14 (added prompt-reading, replay, audio exclusion, an explicit question, option definitions) and Gemini Pro bare 13/14 (read-prompt, replay, ignore audio). So the judge does reward change; it penalises ungrounded change.
- Control regressions in skill arms are new owner-level decisions inserted into rater text, not syncing with the owner's own materials: Haiku made physical plausibility a ranked "Hard Constraint"; Sonnet added "for the action described in the prompt"; Pro placed "[Owner decision required: Prompt adherence precedence]" in participant text; Opus added "including when the choice is hard" to the tie option.
- Skill audits also over-label: 4 of 5 skill runs flagged items as confirmed_defect/material that the judge deemed overstated, i.e. a calibration problem.
- Implication: "restraint" is the wrong axis. The right per-edit axis is grounded (traceable to owner material or cited evidence) versus new_decision. The current 7-dimension total mixes the two, and the control's "0 changes is best" reading should not be used.
- The v2 judge prompt in rejudge.py adds edit_audit (grounded_in, effect), audit_quality, revision_quality and original_adequacy. Staged but not run (see below).
