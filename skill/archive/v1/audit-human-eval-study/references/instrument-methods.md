# Instrument methods for human rating

Use this reference when interpreting a rubric, question, options or exported answer fields. Sources were checked through 2026-10-01. These are transferable design checks, not a certification score.

## Criterion contract

For each decision-bearing question, identify: **unit → construct/criterion → required reference/evidence → response form → applicability/uncertainty states → target decision**. If one is unstated, record the limit and inspect what is still available. Keep subjective preference, checkable correctness and technical failure distinct. A “better” vote needs the goal or audience it means better *for*. [HEDS](https://aclanthology.org/2022.humeval-1.6/), [van der Lee et al.](https://aclanthology.org/W19-8643/), [Artstein and Poesio](https://aclanthology.org/J08-4004/).

## Response form

| Form | Use when | Check in the instrument |
| --- | --- | --- |
| SxS/pairwise | The decision is relative preference between outputs for the same context. | Common prompt/reference; blinded identity; randomized or counterbalanced A/B side/first position; recorded shown-to-stable-ID mapping; meaningful tie/neither/cannot assess states. A winner can still be unacceptable. |
| Pointwise binary | A property has an operational pass/fail threshold. | Explicit threshold, evidence and N/A/uncertain path if needed. Do not force partial severity into yes/no. |
| Pointwise ordinal | Degree or severity matters against a stable reference. | Distinguishable adjacent anchors and examples; direction and endpoints clear. Keep ordinal interpretation unless equal spacing is justified. |
| Multi-label, localized or structured | Multiple defects, spans/regions/times or a demonstration are the intended output. | Co-occurrence and `none` rules; localization tolerance; suitable UI controls; assessment protocol for free-form work. |

The mode and criterion must match the study decision. A binary default from an LLM-judge workflow does not generalize to human preference ratings. There is no universal best scale or safe dimension count. Pilot the actual form on boundary and conflicting-dimension cases when those choices matter. [Amidei et al.](https://aclanthology.org/W19-8648/), [Belz and Kow](https://aclanthology.org/W10-4201/), [ConSiDERS](https://aclanthology.org/2024.acl-long.63/).

## Ordering and randomization

- For SxS, randomize or counterbalance which candidate appears left/right or first/second at the **assignment** level. Retain stable candidate IDs and the actual displayed mapping in each response record. A static screenshot shows one assignment, so it cannot verify the assignment policy.
- For independent items, randomize or counterbalance item order or comparable blocks when prior examples could prime later judgments. If multiple criteria are presented in sequence, consider counterbalancing criterion order in a pilot when priming is plausible; keep the response fields and export mapping unambiguous. Inspect order effects rather than assuming a particular effect size. [Beck et al. 2024](https://aclanthology.org/2024.uncertainlp-1.8/).
- Keep order fixed where it carries meaning: conversation history, event chronology, staged eligibility branches, training/calibration steps and the progression of ordinal scale categories. Declare any constrained randomization and log what each rater actually saw. For matched video comparisons, presentation order is a design variable even when simultaneous playback is used. [ITU-T P.910 Annex C](https://www.itu.int/rec/dologin_pub.asp?id=T-REC-P.910-202111-S%21%21PDF-E&lang=e&type=items).

## A usable rubric

- State the exact task, object/span and relevant context. Put the reference the rater needs within reach.
- Define each criterion with observable evidence and decision consequence. Keep distinct constructs separate unless intentionally collecting an overall preference.
- Make answer choices nonoverlapping. Distinguish tie, neither acceptable, N/A, cannot assess, skip and broken media only where their meanings differ; define which answers trigger follow-up branches.
- Gate whether the property is present before asking for its defect or severity when absence would otherwise fit two options. Define `none` exclusivity for multi-select answers.
- Anchor every ordinal category **to the named criterion**, especially adjacent boundaries. A generic overall-quality description does not define the levels of a specialized criterion. Give a clear good, bad and borderline example with a brief reason; include conflicting-dimension examples where an attractive output fails a hard constraint. Check whether worked A/B examples create a fixed side cue.
- If evidence, a source URL or a rationale is required, specify the required proof for a positive, negative and no-claim case. Ensure the evidence request is feasible and proportional to the target decision; pilot time burden.
- Check that the source instruction, rendered question, branch and exported code express the same answer. Preserve raw labels and rubric version.
- When analyzing recorded answers, distinguish an **offered** option from a branch the rater selected. A strict-choice event may omit a no-preference follow-up that appears for other raters. Observed question-set differences alone do not establish different source rubric versions; check the template and branch codebook.
- Test comprehension and burden with the target population. Agreement by itself does not establish validity, and legitimate preference diversity is not a rater error. [HEDS](https://aclanthology.org/2022.humeval-1.6/), [Howcroft et al.](https://aclanthology.org/2020.inlg-1.23/), [Davani et al.](https://aclanthology.org/2022.tacl-1.6/).

## Memory and workload preflight

Before a human pilot, walk through one ordinary, one borderline, and one missing-evidence item as a rater would. Inventory the criteria, scale boundaries, exceptions, and precedence rules needed **at the answer control**; check whether each is visible or easily retrieved there. Count distinct judgments and required actions per typical item, including media runtime/replays, reference switching, and required rationales. Separate this per-item demand from the length of the full handbook and study-owner notes. If only rubric text is supplied, mark instruction placement and actual workload `cannot_verify`; do not guess that raters must memorize an unseen onboarding page. A static length or model-generated completion-time estimate is a triage clue, not a measure of fatigue. Recommend a smaller local anchor or less repeated work only when it preserves the target construct. There is no validated universal word, duration, or dimension cutoff. [Nielsen's recognition-rather-than-recall heuristic](https://www.nngroup.com/articles/ten-usability-heuristics/), [Wu and Quinn 2017](https://ojs.aaai.org/index.php/HCOMP/article/view/13317/), [Organisciak et al. 2012](https://asistdl.onlinelibrary.wiley.com/doi/10.1002/meet.14504901166), [Hata et al. 2017](https://cs.stanford.edu/people/ranjaykrishna/glimpse/).

**Example of a supported finding:** The rubric defines 1–5 prompt adherence, but the rendered question offers `No / Minor / Major` with no mapping. Report the exact source and UI states, the construct or export ambiguity, a proposed aligned set of options and a verification on the rendered test item. If only the rubric is available, do not invent a UI mismatch.

## Precision and proposed changes

Missing attention checks are not automatically a design defect, and repeated identical answers are not sufficient grounds to label a rater careless. Review existing training/check material against its stated rules when supplied; a subjective preference is not a uniquely correct gold answer. Keep unvalidated check keys and screening/exclusion policies as owner decisions. A model passing a comprehension quiz does not demonstrate human understanding.

In a revision, preserve the original response schema and construct. If evidence suggests adding `cannot assess`, changing precedence, or splitting a criterion, describe the proposed design change separately; keep the primary draft compatible with observed choices until the owner selects it. Do not improve apparent completeness by inventing a reference, threshold, gold key or option.
