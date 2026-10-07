# Original instrument assessment

Read only the original listed materials. No candidate revision, defect key, source variant name or agent arm is available. Assess what these artifacts actually establish, not hypothetical missing deployment components.

Score seven dimensions from 0 to 2, or null when not assessable: construct_preservation (coherence with stated intended decision), operational_clarity, response_anchors, evidence_fit, examples_boundaries, workload_usability, decision_logic. 0 means evidenced substantial weakness, 1 partial/ambiguous, 2 clear and adequate for the stated task. Missing evidence alone is not a zero. Preserve ordinal option order and legitimate subjective differences. Do not invent gold keys or human fatigue/IRR effects. A fixture export may support mapping assessment but not rubric-quality scoring.

Return JSON: scores (each dimension -> {score:0|1|2|null,evidence:string,reasoning:string}), evidence_completeness, limitations (array), confidence. Do not give an unconditional total across unassessable dimensions. Keep this judgment independent of revision generation and later repair adjudication.
