# Methodology and decisions

## Why audit and revise are separate
Early runs scored the revised rubric and asked agents to both audit and revise. Agents found the planted defects nearly every time; score differences came from revisions that settled ambiguities on the owner's behalf (for example making one criterion a hard constraint, or adding a prompt-adherence rule). A quality score cannot tell a warranted clarification from an unapproved decision, so the benchmark now scores the audit alone and reports revision behaviour as a separate measure.

## Permission model
Default is audit and suggest. Edits need explicit permission; settling open choices needs an explicit grant of judgment. This follows the view that a rubric's main weakness is ill-definition, which is the owner's call to resolve.

## Judge design
Audit-only judge, six axes (0-2), no total, arm hidden, revised text stripped, two runs per packet. A cross-family judge (Gemini Flash) was much more lenient than the primary judge; Sol was stable on retest (86% exact). Human adjudication of a sample of contested edits was started and is not complete.

## Things that went wrong and were fixed
- A "known gaps" reference written by the authors moved control scores by 2-3 points: results that depend on references should be treated as sensitivity analyses.
- Original-versus-revised comparisons used a different judge prompt than the revision scores; deltas are indicative.
- Parallel Docker trials exhausted the default network address pool; keep concurrency modest, or pre-bake the agent CLI into the image to cut setup time.

## What is not established
Efficacy on real studies, human agreement improvements, cross-host behaviour of the skill, or performance on image-heavy and audio studies.
