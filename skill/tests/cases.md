# Synthetic cases for a future host run

These are maintainer checks, outside the installed skill. They are not automated benchmark results. Run the same installed skill in Codex, Claude Code and Antigravity, both by explicit name and by an ordinary audit request. Use only the synthetic files in `fixtures/`.

| Case | Input prompt | What to inspect in the agent result |
| --- | --- | --- |
| Rubric only | “Audit [rubric-only.md](fixtures/rubric-only.md).” | Detect the vague comparative criterion and unanchored scale; review wording while marking UI behavior `cannot_verify`. |
| Screenshot only | “Review the annotation UI shown in [ui-screenshot.png](fixtures/ui-screenshot.png).” | Use the image; flag visible asymmetric A/B space. Note that no tie/neither option is visible, but assess whether one is required only after the intended decision is known. Leave click, keyboard and export behavior unverified. |
| Ordering evidence | “Can you verify A/B randomization from [ui-screenshot.png](fixtures/ui-screenshot.png)?” | Report the observed side placement only. Mark assignment randomization `cannot_verify` from one screenshot and request the assignment configuration or a display-order export with stable candidate IDs. |
| Local page | “Inspect the UI in [interactive-study.html](fixtures/interactive-study.html).” | Render/open page if host permits. Check the exact controls and visible states, distinguish exercised interaction from source inspection, and avoid final submission. |
| Data only | “Audit the study represented by [answers.csv](fixtures/answers.csv).” | Inspect fields/code mapping possibilities; do not invent rubric text, UI or IRR. Do not infer that a neutral branch was unavailable merely because a recorded answer chose A or B. Ask for the smallest source artifact needed for a fuller conclusion. |
| Mixed | “Compare [rubric-only.md](fixtures/rubric-only.md) with [interactive-study.html](fixtures/interactive-study.html).” | Identify source/rendered wording or option mismatch only if both artifacts support it; cite both. |
| URL only | “Audit the rating UI at a user-provided accessible URL.” | Use a browser if available, report visited states and viewport; if inaccessible, say so and do not fabricate UI findings. |
| Valid control | “Audit [clean-control.md](fixtures/clean-control.md).” | Recognize the stated decision, evidence, answer boundaries and examples; avoid generic findings made only to fill a checklist. UI behavior remains `cannot_verify`. |
| Adjacent request | “Compute agreement from these already collected labels.” | Do not misroute a statistical-analysis task into an instrument/UI audit unless the user also asks for instrument review. |

Acceptance concerns: trigger precision, artifact/tool use, observation versus inference, modality-specific checks, `cannot_verify` behavior, concise prioritized findings, no live submission, and no claim that a UI change improves IRR without a comparison study.

Additional visibility, version, mapping and restraint cases: [progressive review cases](progressive-review-cases.md).
