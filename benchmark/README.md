# Benchmark

```
dataset/        165 synthetic cases (cases/ = agent-visible materials; evaluator-only/ = keys, never shown to agents)
generators/     49 family definitions and a builder (control / defect / partial per family); 6 coverage-pass families ship as cases only
harness/        experiment runner, judge, summaries, Docker files, Harbor task template
results/        written reports for each test
taxonomy/       55 textbook mistakes in human-rating studies, mapped to coverage
skill-variants/ skill v2.1 (not adopted), kept for the comparisons in results/
```

Case variants per family: `control` (no planted defect; matched), `defect` (one planted mistake, usually a one-file mutation), `partial` (the decisive file withheld; the right answer is to say it cannot be verified). Keys carry `expected_detection`, an assessment, and prohibited changes.

Judging principles (see `results/` for the reasoning behind each):
1. Score the audit separately from any revision; no summed total.
2. The judge sees the audit and owner questions, not the revised rubric, and not which arm produced it.
3. A frozen reference of defects, ambiguities and evidence limits is generated once per case, before any candidate is scored.
4. An ambiguity is only handled well if the audit explains how readings differ, offers options, recommends a default, and asks the owner; settling it by decree is penalised.
5. Every judge pass is repeated and test-retest agreement is reported.
