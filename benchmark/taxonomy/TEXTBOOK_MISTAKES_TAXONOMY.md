# Textbook mistakes in human-evaluation studies: taxonomy and coverage map

Purpose: list the classic design, measurement, recruitment, quality-control, analysis and ethics mistakes in human-rating and annotation studies, map them against the existing benchmark (37 families, 95 cases), and prioritise what to add. Author-compiled from general survey-methodology, psychometrics, HCI-evaluation and crowdsourcing-methods knowledge; not individually sourced in this pass. Before any item is cited in a report, a primary source should be added with URL and retrieval date. Sources worth checking (named from memory, not retrieved): Schuman and Presser on question wording; Krosnick on satisficing; Podsakoff et al. on common-method bias; Cohen and Krippendorff on agreement coefficients; Kittur et al. on crowdsourced user studies; Oppenheimer et al. on instructional manipulation checks; Peer et al. on crowdsourcing platform data quality.

## Coverage map
Covered by existing families: construct mismatch (motion-construct), scale changes what is measured (audio-scale), merged or exclusive options (merged-options, exclusive-none), one saved field for several questions (confidence-granularity), promised but missing follow-up, position confounds and stable labels (side-assignment, image-layout), allocation and ranges (prompt-allocation, range-boundary, rank-validation, selection-cap), workload feasibility (inspection-load), subjective gold checks (subjective-gold), answer cues (answer-leakage), response-mapping and export integrity (resume-mapping, playback-evidence, export-freshness, source-roles, narration-binding, optional-upload), tie handling in analysis (tie-missingness), delivery specification (temporal-evidence).
Not covered, and the main gap: recruitment and population, incentives and quality control as design choices, statistical analysis and reporting, blinding and demand characteristics, instrument-wording biases, and ethics and consent.

## A. Wording and instrument (priority families marked *)
1. Leading or loaded question *
2. Double-barreled item *
3. Unbalanced or non-exclusive scale anchors *
4. Undefined construct or vague key term (partly covered)
5. Demand characteristics: instructions reveal the hypothesis or the preferred system *
6. Mixed-polarity items without notice (reverse coding) *
7. Priming by showing other raters' scores, model confidence or a prior label
8. Examples that bias (only extremes, or example key leaks the answer)
9. Forced choice with no escape option
10. Ambiguous reference frame ("compared to what?")
11. Instructions too long or buried; too many dimensions per page
12. Translation or localisation drift

## B. Design and assignment
13. No counterbalancing of condition or dimension order; carryover effects *
14. Unblinded system or model identity *
15. Calibration or training items overlap the evaluation items *
16. Unrepresentative or cherry-picked item sample
17. Unequal exposure: one system gets more raters or easier items *
18. Within versus between design mismatched to the claim
19. Sample size not justified; stopping on significance *
20. No pilot or dry run
21. Item-condition confounds: length, difficulty, domain
22. Rater concentration: a few raters supply most ratings *

## C. Population and recruitment
23. Rater expertise does not match the task (domain tasks given to a general crowd, no screener) *
24. Screener reveals the criterion or the correct answer, so it can be gamed *
25. Population not representative for a subjective or cultural judgment
26. Language or locale mismatch
27. Duplicate accounts or repeat participation
28. Over-restrictive screening that biases the sample

## D. Quality control and incentives
29. Majority agreement used as the quality criterion for a subjective task (penalises legitimate disagreement) *
30. Bonus for agreement with the majority (induces conformity) *
31. Attention check that is ambiguous, subjective or unfair; post-hoc exclusions *
32. Pay or time estimate that rewards rushing (piece rate, understated duration) *
33. No rater training or calibration; drift
34. Speeder thresholds that exclude honest fast raters
35. No feedback or appeal path

## E. Analysis and reporting
36. Pseudoreplication: ratings by the same rater or on the same item treated as independent *
37. Majority vote as ground truth; disagreement discarded *
38. Ordinal scale averaged and ranked without justification; ranking on non-significant gaps *
39. Multiple comparisons without correction; subgroup fishing *
40. Simpson-type aggregation across unequal strata *
41. Percent agreement reported as reliability under heavy class imbalance (kappa paradox) *
42. Judge-model agreement treated as validation; circular LLM-judge validation *
43. Length or verbosity bias uncontrolled *
44. Ceiling and floor effects ignored
45. Missing data dropped without a mechanism (survivorship)
46. Causal or population claims beyond the design
47. Uncertainty not reported (no intervals)

## F. Operations and integration (largely covered)
48. Stale exports, wrong item association after resume, silent field overwrites, unverified playback

## G. Ethics and compliance
49. Consent time or compensation misstated relative to the real task *
50. Harmful content with no warning or opt-out *
51. Personal data in stimuli *
52. Minors or age-sensitive content with no age gate *
53. Deception without debrief; no right to withdraw
54. Data retention not stated

## H. Presentation and accessibility
55. Colour-only cues, audio without captions, small touch targets, keyboard traps (covered partly by the UI reference in the skill)

## Plan
First batch (starred, 29 families x 3 variants = 87 cases, text and configuration only, synthetic): see `augmentation_families_textbook.py`. Each family follows the existing control, defect and partial triple; controls are sound but not claimed flawless. Next batch: unstarred items above, then image and audio variants.
