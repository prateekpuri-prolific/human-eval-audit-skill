# Synthetic source-support rating

This is a synthetic test fixture, not a historical study.

## Decision and materials

Decide whether a short answer accurately represents the **single source excerpt shown directly above it**. Each task contains the full excerpt and one answer of at most three sentences. Judge source support only; writing style and whether the answer is useful are outside this question.

## Question

Are all factual claims in the answer supported by the displayed excerpt?

- **Yes:** Every factual claim is directly stated by the excerpt or follows without adding a new fact. A specific, accurate claim about what the excerpt omits may be Yes.
- **No:** At least one factual claim contradicts the excerpt or adds a fact the excerpt does not support. Select No even if the other claims are supported.
- **No factual claim:** The displayed answer contains no checkable factual claim about the excerpt, such as a pure refusal.
- **Cannot assess:** The excerpt or answer is missing, truncated, or fails to load. Do not use this for a merely difficult or ambiguous claim; use No when the source does not support it.

Examples: If the excerpt says “The trial enrolled 40 adults,” “The trial enrolled 40 adults” is Yes; “The trial enrolled 400 adults” is No; “I cannot answer from this excerpt” is No factual claim. If the excerpt says “The trial enrolled 40 adults” but gives no age range, “The trial enrolled 40 adults aged 18–30” is No because the added age range is unsupported.

The study records the raw option label and rubric version for every response. Raters can reopen the excerpt before answering. No answer is preselected.
