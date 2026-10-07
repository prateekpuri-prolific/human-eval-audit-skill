# Step 1b: judge test-retest, second-family judge, v2 axes

24 packets (Sonnet and Opus x 5 cases x bare/skill, plus Haiku and Gemini Pro on control case-018), three conditions, 72 calls, 0 errors. Script: `rejudge.py`; analysis: `analyze_rejudge.py`. Outputs in data/private/.../rejudge/. Original judgments untouched. Judges: openai/gpt-6-sol (original and v2 prompt), gemini/gemini-3.8-flash (v2 prompt). Per-dimension comparisons use dimensions non-null in both judgments.

## 1. Sol test-retest (same prompt, same packets)
- Per-dimension exact agreement 86%, within one point 100%, mean absolute difference in total 0.54 points, same major/critical-regression count in 22/24 packets.
- Skill-minus-bare gap, original vs retest (sum over 5 cases for 1-point dimensions): Sonnet -12 vs -14, Opus -7 vs -7, Gemini Pro -5 vs -3, Haiku -1 vs +1.
- Reading: judge noise is about 0.5 points per packet. The Sonnet and Opus skill deficits are well outside it. Haiku and Pro gaps are within noise-ish range (Pro -5/-3; Haiku about zero).

## 2. Cross-family (Sol v2 vs Flash v2)
- Exact per-dimension agreement 55%, mean total difference 2.9 points. Flash is much more lenient: 1 new_decision edit across 12 bare runs versus 15 under Sol; revision fidelity 2.00 in every bare run; 0 overclaims on bare audits.
- The sign of the skill-minus-bare gap is preserved for all four models under Flash (Haiku -3, Opus -1, Sonnet -8, Pro -1), with smaller magnitude. Flash is not discriminating enough to arbitrate; which judge is right on contested edits needs human adjudication.

## 3. v2 axes (Sol; Flash in brackets)
| Axis | bare (12 runs) | skill (12 runs) |
|---|---|---|
| Edits grounded in owner material / audit evidence / new decision | 37 / 16 / 15 [29 / 13 / 1] | 39 / 13 / 9 [23 / 10 / 2] |
| Edits that change meaning | 14 [0] | 8 [2] |
| Audit usefulness alone (0-2) | 1.67 [2.00] | 1.67 [1.82] |
| Audit calibration overclaims | 5 of 12 [0] | 6 of 12 [2] |
| Unsupported claims | 19 [0] | 14 [4] |
| Revision fidelity (0-2) | 1.75 [2.00] | 1.42 [1.83] |
| Net vs original: better / same / worse | 10 / 0 / 2 [12 / 0 / 0] | 6 / 2 / 4 [11 / 0 / 1] |

- Audit quality alone is equal across arms (1.67 vs 1.67 under Sol). The skill neither helps nor hurts the audit half.
- The deficit is in revision: fidelity 1.75 to 1.42 and net-worse 2 to 4 of 12 under Sol, same direction under Flash.
- Against the earlier hypothesis: the skill made fewer new_decision and meaning-changing edits than bare under Sol (9 vs 15; 8 vs 14). Its failures are fewer but costlier edits, not more unauthorised edits by count. Severity weighting, not edit counts, explains the loss. Bare-arm edits are also riskier in count, so edit-count rules alone would not fix the skill.

## 4. Was the control already perfect?
- Under Sol v2, original_adequacy on case-018: minor_improvements_warranted 5, sound 3 (of 8). Under Flash: minor_improvements_warranted 8 of 8. No judge calls it materially defective; no judge consistently calls it flawless. Sol is inconsistent with itself (3 sound vs 5 minor), which is noise to resolve with a fixed list of known grounded gaps (read-prompt, replay, audio, response question, Left/Right) as an explicit reference in the judge packet.

## Limits
Two judges, 24 packets, one generation per cell, author-created issue key. Judge agreement is not human validation. Flash leniency may be partly a model-capability effect, not necessarily the more accurate view.

## 5. Adjudication sheet and known-gaps reference (follow-up)
- `ADJUDICATION_SHEET.md`: 26 edits Sol v2 labeled new_decision or changes_meaning, blinded (arm and model hidden; key in data/private/.../adjudication-key-private.json). 13 have a comparable Flash edit that Flash did not flag; 11 have no comparable Flash edit. Awaiting human verdicts (A grounded / B new decision / C changes meaning).
- Known-gaps reference for case-018 (`rejudge/known-gaps-018.md`, author-written from a diff of participant.md against study.md; not independent adjudication) added to the 8 control packets, Sol rejudge (`v3-sol-ref`, 8 calls).
  - original_adequacy converges: 8 of 8 minor_improvements_warranted (v2 Sol gave sound for 3 of 8).
  - Control totals, v2 to v3: bare 46 to 39 (Haiku 7/7, Opus 14 to 12, Sonnet 12 to 10, Pro 13 to 10); skill 33 to 32 (7/7, 10 to 8, 8 to 9, 8/8). The bare-minus-skill control gap roughly halves, 13 to 7 points over 4 models.
  - Changes of 2-3 points exceed the 0.5 test-retest noise, so the reference itself moved scores. It lowered bare scores where bare edits missed or only partly closed the listed gaps. Treat the v3 numbers as sensitivity analysis on the criteria, not as a replacement; the list is mine, so the adjudication of the gaps should be confirmed by you before it enters the judge.
