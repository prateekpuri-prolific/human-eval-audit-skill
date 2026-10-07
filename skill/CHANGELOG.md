# Skill changelog

## v2 (current)
- Section 0, authority: audit and suggest by default. Edits to rater-facing text only when the user explicitly authorises them.
- Open ambiguities are reported as owner questions with: source quote, how rater answers differ by reading, 2-3 options with draft wording, a recommended default, and one question. Never settled by decree and never placed in rater text.
- Determined fixes (the owner's own materials settle the answer) are separated from ambiguities.
- Label calibration rule: `confirmed_defect` only when a quoted source establishes it.
- Revision moved to its own section, used only when explicitly authorised.

## v1 (archived at `archive/v1/`)
The original skill: audit or revise in one pass, evidence-map driven, with no authority gate or owner-question template.

## v2.1 (not adopted; `../benchmark/skill-variants/v2.1/`)
Added a read-before-cite rule for images and structured sources, "report every ambiguity", and a coverage sweep. On fresh cases it raised overclaims; on image cases it did not reduce misreadings. See `benchmark/results/`.
