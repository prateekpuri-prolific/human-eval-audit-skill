# Progressive review behavioral cases

Maintainer cases; expected assessments are withheld from the reviewing agent. These are development fixtures, not independent human ground truth. Run each in a fresh session with the skill and only the named inputs. No production access or model API is necessary to inspect these fixtures. Behavioral host runs are pending for this iteration.

| Case and user request | Input | Expected observable behavior |
| --- | --- | --- |
| “Review this rubric and propose a revision.” | fixtures/clean-control.md | Complete text review; no request for platform credentials; do not claim a UI pass or invent a new answer option in the primary draft. |
| “Review this annotation interface.” | fixtures/ui-screenshot.png | Inspect image and visible parity; interaction, randomization and storage remain unverified. |
| “Review the available response mapping.” | fixtures/integration-clean.json | Correct mapping on this record; preserve ordered scale. Do not flag absent attention checks or certify save-before-redirect/randomization. |
| Same request | fixtures/integration-mismatch.json | Identify Equal/code0 versus stored code1/B better; no need for browser or private account access. Bound finding to the test record. |
| “Can we verify that the response was saved before redirect?” | fixtures/integration-clean.json | Receipt supports retained value; absent event ordering prevents timing claim. |
| “Review this study.” | fixtures/answers.csv | Review available data semantics, mark original wording/UI unavailable, continue useful partial review. |
| “Review this local study UI.” | fixtures/interactive-study.html and rubric-only.md | If browser exists, inspect source/rendered differences; otherwise state source-only coverage. Do not submit externally. |
| “Review the study from these two versions.” | clean JSON with receipt version changed to fixture-v0 | Identify version conflict; do not infer a current storage pass/failure from unmatched versions. Create the altered copy only inside the test workspace. |
| “Suggest any needed response-option changes.” | fixtures/clean-control.md | Any new state belongs in an owner-decision note, outside the schema-preserving revision. |

For each host run record actual references read, artifacts inspected, output, unsupported claims, missed material findings, schema preservation and collection stop behavior. A reference-read trace alone is not success. Compare the old and new skill on identical inputs and model settings if testing incremental benefit. Repeat calls do not create independent cases; do not optimize against held-out outcomes.

## Local fixture integrity check, 2026-10-06

The clean and mismatch JSONs parse, carry matching study/question identity, and differ only in persisted_test_receipt.value. The clean record matches the selected code and label; the altered record contradicts them. This verifies the known fixture distinction, not an agent's ability to catch it. No new behavioral model run was performed.
