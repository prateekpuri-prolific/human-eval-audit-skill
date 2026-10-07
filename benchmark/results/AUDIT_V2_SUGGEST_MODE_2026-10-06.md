# Suggest-mode audit comparison: bare vs skill v1 vs skill v2 

Design: 5 cases x 3 arms (bare, frozen v1 skill, v2 skill with authority gate) x 2 prompts. P1 = "review and tell the owner what you find". P2 = "review and improve the study where you can". Same output contract for every arm (audit, owner_questions, proposed_patches, coverage, optional revised_artifacts); the contract carries format, so differences reflect method. Claude Code 2.1.285, Haiku 4.5 and Sonnet 5.5. Judge: audit-only Sol, 2 runs per packet, six axes, no totals; frozen per-case references (unvalidated by a human, case-018 partly author-derived). Opus P1 failed in setup on the first attempt (network errors installing the CLI, 15 of 15, infra only; saved under audit-v2/setup-failures) and was rerun at lower concurrency with 0 errors. All 75 trials are valid and judged (2 runs each); the interim table below covers Haiku and Sonnet, the update section adds Opus.
Judge test-retest: 82-95% exact per axis, mean abs diff 0.05-0.18.

## Pooled Haiku + Sonnet (n=10 trials per cell; axes 0-2)
| Metric | P1 bare | P1 v1 | P1 v2 | P2 bare | P2 v1 | P2 v2 |
|---|---|---|---|---|---|---|
| Coverage of reference defects and ambiguities | 0.52 | 0.69 | 0.74 | 0.56 | 0.82 | 0.75 |
| Classification calibration | 1.20 | 1.05 | 1.55 | 1.10 | 1.45 | 1.35 |
| Evidence accuracy | 1.10 | 1.05 | 1.40 | 1.05 | 1.35 | 1.10 |
| Ambiguity quality | 1.10 | 1.20 | 1.25 | 1.05 | 1.00 | 1.25 |
| Ambiguities settled by decree | 8% | 12% | 2% | 17% | 16% | 7% |
| Explains how readings differ | 77% | 91% | 98% | 69% | 81% | 91% |
| Owner question present | 79% | 82% | 93% | 64% | 70% | 85% |
| Overclaims per run | 1.3 | 1.45 | 0.55 | 1.45 | 0.65 | 0.90 |
| Wrong major+critical claims per run | 1.0 | 1.2 | 0.75 | 0.95 | 0.65 | 0.65 |
| Produced revised rubric files anyway | 70% | 40% | 10% | 100% | 50% | 20% |

## Reading
- Both skills raise defect-and-ambiguity coverage over bare (P1 0.52 to 0.69/0.74; P2 0.56 to 0.82/0.75). The v1 skill already helps audit coverage under the new contract.
- v2 adds what it was written for: fewer decrees (2% vs 8-12% on P1), more reading-difference explanations (98%), better calibration and fewer overclaims on P1, and far less unrequested revision (P2: 100% bare, 50% v1, 20% v2 produced rewritten rubrics even though the contract only asked for proposals).
- v2 is not uniformly better: on P2 v1 had higher coverage (0.82 vs 0.75; driven by Haiku, v1 0.81 vs v2 0.55) and better evidence accuracy. Do not claim v2 dominates.
- The 4 critical wrong claims on Sonnet v2 P1 are one trial (case-083, counted in 2 judge runs): it swapped the red and blue triangle colours and misdescribed the purple rectangle. The earlier Sonnet-with-skill run made the same mistake on this case. Evidence-accuracy failures on image/SVG reading are not fixed by either skill.
- Limits: 5 cases, 1 trial per cell, two models, one judge family, unvalidated references. Differences of about 0.3 axis points between arms at n=10 are suggestive only.

## Update: Opus complete (75 of 75 trials judged; judge test-retest 79-96% exact per axis)
Opus, prompt P1 (bare / v1 / v2): coverage 0.75 / 0.88 / 1.00; calibration 1.6 / 1.5 / 1.8; evidence accuracy 1.4 / 1.6 / 1.7; ambiguity quality 1.3 / 1.5 / 1.9; settled by decree 12% / 10% / 0%; explains reading differences 94% / 95% / 100%; overclaims per run 0.9 / 0.6 / 0.3; produced a rewritten rubric anyway 80% / 100% / 20%; owner questions per run 2.6 / 3.2 / 4.4.

Pooled across all three models, P1 (15 trials per arm; bare / v1 / v2): coverage 0.60 / 0.76 / 0.82; calibration 1.33 / 1.20 / 1.63; evidence accuracy 1.20 / 1.23 / 1.50; ambiguity quality 1.17 / 1.30 / 1.47; decree 9% / 11% / 2%; explains readings 82% / 92% / 98%; overclaims 1.17 / 1.17 / 0.47; rewrote the rubric 73% / 60% / 13%.
Pooled P2 is Haiku and Sonnet only (Opus was not run on P2): see the interim table.

Reading after Opus: on the strongest model v2 is better than v1 on every audit axis, and v1 made Opus more likely to rewrite the rubric (100%) than bare (80%). The permission-gate effect (v2 20% vs 80-100%) holds across all three models. The one place v2 did not beat v1 remains P2 coverage on Haiku. Still one trial per cell on five cases, an unvalidated reference, and one judge family; the Sonnet case-083 image misreading persists under v2.
