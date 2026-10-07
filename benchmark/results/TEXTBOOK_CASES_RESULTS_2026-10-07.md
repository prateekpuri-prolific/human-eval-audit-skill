# Textbook-mistake cases: bare vs skill v2 (Sonnet 5.5, suggest mode)

Cases: 87 synthetic cases from 29 textbook-mistake families (control, defect, partial each); 174 trials, one per cell, prompt P1 ("review and tell the owner what you find"), Claude Code 2.1.285. Judge: audit-only, 2 runs per packet (test-retest 80-97% exact per axis). References generated once from the original materials and key, unvalidated by a human. Axes 0-2.

| Case type | Arm | Coverage | Key-issue handling | Calibration | Evidence accuracy | Ambiguity quality | Overclaims/run | Wrong major+crit/run | Rewrote the rubric anyway |
|---|---|---|---|---|---|---|---|---|---|
| Defect (29) | bare | 0.99 | 2.00 | 1.62 | 1.48 | 1.41 | 0.60 | 0.38 | 97% |
| Defect (29) | v2 | 0.97 | 1.97 | 1.66 | 1.59 | 1.59 | 0.41 | 0.41 | 0% |
| Control (29-30) | bare | 0.57 | 1.81 | 1.10 | 1.28 | 1.31 | 1.33 | 1.05 | 62% |
| Control (29-30) | v2 | 0.65 | 1.87 | 1.33 | 1.33 | 1.57 | 0.83 | 0.58 | 0% |
| Partial (29-30) | bare | 0.31 | 1.95 | 1.64 | 1.47 | 1.62 | 0.48 | 0.28 | 10% |
| Partial (29-30) | v2 | 0.30 | 1.98 | 1.78 | 1.62 | 1.80 | 0.28 | 0.27 | 0% |

Decrees (ambiguity settled for the owner): defect 7% vs 0%, control 6% vs 1%, partial 8% vs 0%.

## Reading
- Detection is at ceiling. In 26 of 28 families with a scored planted defect, both arms scored 2.0 on key-issue handling. These textbook defects are easy for Sonnet; the cases are not discriminating on detection.
- Where the skill differs is restraint and calibration. On controls, v2 had fewer overclaims (0.83 vs 1.33), fewer wrong major or critical claims (0.58 vs 1.05) and better ambiguity quality (1.57 vs 1.31). The largest behavioural gap is unrequested rewriting: bare rewrote the rubric in 97% of defect runs and 62% of control runs; v2 did so in none.
- Partial cases show the same pattern with smaller gaps; coverage is low for both arms (about 0.3), partly because the reference lists for partial cases contain items that require the withheld file.
- Three families scored below 2 for v2 on the planted defect (unbalanced-scale 1.5, pii-in-stimuli 1.5, harmful-content-warning not scored by the judge). Worth reading those transcripts before generalising.
- Limits: one model, one trial per cell, a single judge family, author-written keys and references, synthetic cases.

## Implication for the benchmark
Add harder, subtler variants of these defects (the defect hidden in a combination of files, or a defect plus a plausible-looking justification) so detection can discriminate, and keep reporting restraint and calibration separately.
