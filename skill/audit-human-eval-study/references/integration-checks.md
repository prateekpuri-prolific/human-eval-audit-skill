# Optional configuration and test-flow checks

Read only when settings, code, assignment records, or a testable completion flow are available. This guide does not implement a recorder, platform connector or test backend. Use existing host tools and supplied exports; no platform account or broad database access is required.

## Check what the evidence permits

| Check | Minimum evidence | Verification and stopping boundary |
| --- | --- | --- |
| Settings consistency | Advert/settings plus relevant instrument | Compare duration, reward currency/units, eligibility/devices, task URL and completion configuration. State missing policy inputs; do not invent pay thresholds. |
| Media/access | Preview and supplied representative assets | Verify observed loading, references and compatible presentation. A fetched URL alone does not prove playable media. Bound conclusions to inspected items/devices. |
| Consent and exit flow | Supplied notice/consent requirements and accessible states | Check required information/order and available exit route against supplied requirements. Do not claim legal compliance or accept new terms to finish a check. |
| Completion routing | Configured completion destination/code and preview route | Compare expected and observed routing. Navigate a submission/redirect only if authorized for a sandbox/test identity; otherwise inspect configuration and mark execution unverified. |
| Display-to-storage mapping | Same-version rendered options plus codebook/test record | Match question ID, raw code, scale direction, tie/N/A states, and displayed candidate to stable identity. Code inspection establishes intent; recorded tests establish observed writes. |
| Randomization | Assignment logic/config plus versioned assignment records | Inspect candidate side/first position and independent-item order separately. Multiple screenshots alone do not prove randomness. Preserve ordinal category order and meaningful task sequences. |
| Save before redirect | Authorized test submission plus readable persisted receipt/log | Verify durable response acknowledgment precedes redirect using transaction/event evidence. A success page alone is insufficient. If timing/order is absent, report it unverified. |
| Reload/retry/duplicate writes | Safe test environment, explicit test-write scope, readable records | Exercise one bounded retry/recovery path and compare logical response IDs/counts. Distinguish intentional answer revisions from duplicate inserts. Stop on unexpected production routing or unclear state; do not retry an ambiguous write blindly. |

Use stable test IDs and study/template versions to join evidence. Broad production access and real participant identities are unnecessary for these checks. A narrow exported receipt may suffice. Do not call storage verified from a frontend event alone.

## Results and reusable checks

A deterministic failure requires an explicit invariant and observed mismatch, e.g. the displayed `0 = equal` stores the documented code for `A better`. A rule with unknown intent is a question for the owner, not an automatic failure. Absence of an attention check, fixed ordinal category order, or an unusual answer distribution does not by itself fail prelaunch review.

Record check, evidence version/state, expected versus observed, and status: pass/fail/not_verified/not_applicable. Keep recommendations and predicted behavioral consequences separate. A real failure need not recur in two of three model runs to be reported; repeated suggestions are not independent validation.

For repeated launches, reuse template-level results only while relevant UI, rubric, branching and storage versions remain unchanged. Check launch-specific settings and item/media availability separately. If version identity or prior coverage is unknown, do not inherit a pass. This is a reuse option, not an instruction to create monitoring or a recurring job.
