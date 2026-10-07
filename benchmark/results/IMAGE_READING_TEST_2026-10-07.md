# Image-reading test: bare vs skill v2 vs skill v2.1

Cases: 015 (PNG screenshot, fresh), 081 and 082 (SVG image-region, fresh), 083 (the earlier colour-swap case, already seen). Arms: bare, v2, v2.1. Models: Haiku, Sonnet, Opus. 3 repeats per cell, prompt P1, 108 trials, 0 errors after a Docker network-pool recovery (earlier attempts preserved in img-v1/setup-failures). Judge: audit-only Sol, 2 runs, test-retest 80-92% exact per axis.

## Pooled over models (36 trials per arm)
| Metric | bare | v2 | v2.1 |
|---|---|---|---|
| Evidence accuracy (0-2) | 1.12 | 1.35 | 1.29 |
| Wrong major or critical claims per run | 1.08 | 0.68 | 0.79 |
| Critical wrong claims (count over 72 judged runs) | 3 | 3 | 8 |
| Coverage of reference items | 0.75 | 0.82 | 0.85 |
| Ambiguity quality | 1.36 | 1.69 | 1.64 |
| Overclaims per run | 1.56 | 0.92 | 1.03 |
| Rewrote the rubric anyway | 44% | 8% | 0% |

Per model, wrong major+critical per run: Haiku 2.12 / 1.38 / 1.42; Sonnet 0.71 / 0.62 / 0.75; Opus 0.42 / 0.04 / 0.21 (bare / v2 / v2.1). Haiku coverage 0.28 / 0.47 / 0.54.

## Reading
- v2 reduces misreadings against bare (major+critical 1.08 to 0.68), most clearly on Opus (0.42 to 0.04) and Haiku (2.12 to 1.38).
- v2.1's read-before-cite sentence did not help: critical wrong claims rose to 8 (Sonnet 6) and evidence accuracy was not better than v2. Sonnet on case-083, the known colour-swap case, had 0 critical claims for bare and v2 and 2 judged runs (1 trial) for v2.1; the swap did not reproduce in bare or v2 this time. Treat the colour swap as an occasional stochastic error, not a fixed behaviour.
- Haiku remains weak on image sources even with the skill.
- Limits: 3 repeats, 4 cases (one already seen), judge-flagged errors not independently verified.

## Recommendation
Drop v2.1 (consistent with the fresh-case result). Keep v2. Image reading needs a different intervention (for example a deterministic extraction step), not more prompt text.
