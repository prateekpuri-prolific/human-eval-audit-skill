# Audit-only benchmark v3 (first scoring pass)

Scope decision (user, 2026-10-06): audit benchmark first; revision benchmark deferred because revising involves owner-level decisions. Reporting: separate axes, no total. Judge sees only the audit, owner decisions and coverage (revised artifacts stripped, arm and model hidden). Ambiguity handling has its own axes. Decision recorded for the later revision benchmark: a judgment call placed in rater text gets a full penalty even if also flagged as an owner question. The old wording "provide a revised instrument where the evidence permits" is ambiguous about permission; future task prompts must say explicitly whether edits are permitted.

Method: Sol (openai/gpt-6-sol), 45 packets (Haiku, Sonnet, Opus, Gemini Pro bare and skill; Flash skill only) x 2 judge runs = 90 calls, 0 errors. Frozen per-case reference of defects, ambiguities and missing evidence generated once from the original materials and key (5 Sol calls, no candidates shown). The case-018 reference was augmented with 5 author-derived items (documented participant.md gaps and open owner-level ambiguities); this is not independent adjudication. Script: audit_judge.py, summarize_audit.py. Private outputs: data/private/.../audit-v3/.

Reading guide: 1 case per cell, 2 judge runs per packet. Axis differences of under about 0.3 per case are not meaningful.

## Judge reliability (run 1 vs run 2)
Exact agreement per axis: key_issue_handling 100%, ambiguity_coverage 96%, ambiguity_quality 91%, calibration 87%, evidence_accuracy 87%, scope 84%; mean absolute difference 0.00 to 0.16. Stable.

## Results (means of 2 runs; 0-2 per axis)
Judge test-retest (run1 vs run2), per axis exact agreement / mean abs diff
  key_issue_handling         100% / 0.00 (n=45)
  classification_calibration 87% / 0.13 (n=45)
  evidence_accuracy          87% / 0.13 (n=45)
  ambiguity_coverage         96% / 0.04 (n=45)
  ambiguity_quality          91% / 0.09 (n=45)
  scope_and_abstention       84% / 0.16 (n=45)

Mean axis score per condition (avg of 2 judge runs; 0-2; no totals)
model arm n | key_issue_h | classificat | evidence_ac | ambiguity_c | ambiguity_q | scope_and_a | amb/run decree% opts>=2% explain% question% | overclaims wrong(sev,per cond)
claude-haiku  bare  5 | 2 | 1.3 | 1.3 | 1 | 0.3 | 1.5 | 2.7 59% 41% 44% 37% | 1.8 {'major': 9.0, 'minor': 4.5}
claude-haiku  skill 5 | 2 | 1.6 | 1.2 | 1 | 0.8 | 1.2 | 2.5 8% 68% 52% 84% | 1.1 {'major': 3.5, 'minor': 7.5}
claude-sonnet bare  5 | 2 | 1.2 | 1.4 | 1.2 | 1 | 1.8 | 2.7 4% 15% 44% 78% | 0.7 {'major': 2.5, 'minor': 6.0}
claude-sonnet skill 5 | 2 | 1.5 | 1.3 | 1.2 | 0.8 | 1.7 | 3.9 5% 28% 41% 79% | 1.0 {'minor': 5.5, 'critical': 1.5, 'major': 1.5}
claude-opus   bare  5 | 2 | 1.4 | 1.5 | 1.2 | 1 | 1.8 | 3.6 22% 50% 61% 72% | 1.1 {'minor': 6.0, 'major': 3.0}
claude-opus   skill 5 | 2 | 1.5 | 1.5 | 1.2 | 0.9 | 1.7 | 4.3 14% 49% 67% 79% | 0.7 {'major': 2.5, 'minor': 1.5}
gemini-pro    bare  5 | 2 | 1.8 | 1.6 | 1 | 0.5 | 1.1 | 0.8 0% 75% 12% 75% | 0.4 {'minor': 1.5, 'major': 0.5}
gemini-pro    skill 5 | 2 | 1.6 | 1.8 | 1 | 0.7 | 1.7 | 1.1 0% 64% 45% 64% | 0.2 {'major': 1.0}
gemini-flash  skill 5 | 2 | 1.5 | 1.4 | 1.2 | 1 | 1.4 | 5.0 2% 72% 38% 98% | 0.8 {'minor': 4.5, 'major': 3.5}

Paired bare->skill per axis, summed over 5 cases x 2 runs / 2 (positive = skill higher)
  claude-haiku   key_issue +0.0 | classific +1.5 | evidence_ -0.5 | ambiguity +0.0 | ambiguity +2.5 | scope_and -1.5
  claude-sonnet  key_issue +0.0 | classific +1.5 | evidence_ -0.5 | ambiguity +0.0 | ambiguity -1.0 | scope_and -0.5
  claude-opus    key_issue +0.0 | classific +0.5 | evidence_ +0.0 | ambiguity +0.0 | ambiguity -0.5 | scope_and -0.5
  gemini-pro     key_issue +0.0 | classific -1.0 | evidence_ +1.0 | ambiguity +0.0 | ambiguity +1.0 | scope_and +3.0

Control case-018 only: ambiguity axes and decree rate
  claude-haiku  bare   coverage 1 quality 0.5 calib 1 key 2 | ambiguities 6.0 decree 33%
  claude-haiku  skill  coverage 1 quality 1 calib 1 key 2 | ambiguities 6.0 decree 8%
  claude-sonnet bare   coverage 1 quality 1 calib 1 key 2 | ambiguities 3.5 decree 0%
  claude-sonnet skill  coverage 1 quality 1 calib 1.5 key 2 | ambiguities 4.5 decree 0%
  claude-opus   bare   coverage 1 quality 1 calib 1 key 2 | ambiguities 4.0 decree 25%
  claude-opus   skill  coverage 1 quality 1 calib 1.5 key 2 | ambiguities 6.0 decree 17%
  gemini-pro    bare   coverage 1 quality 0.5 calib 2 key 2 | ambiguities 1.0 decree 0%
  gemini-pro    skill  coverage 1 quality 0 calib 1 key 2 | ambiguities 2.0 decree 0%
  gemini-flash  skill  coverage 1 quality 1 calib 1 key 2 | ambiguities 4.0 decree 0%
