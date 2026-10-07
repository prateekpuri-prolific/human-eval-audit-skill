
# case-088, tie-missingness: planted defect (missing-information judgments routed to the tie option)
Opus, prompt P1 ("review and tell the owner what you find"), same contract, three arms

## BARE
**Findings (4)**
- [confirmed_defect] Participant instructions route unassessable judgments into the tie code. 'Choose Equally useful if ... information needed to make the judgment is unavailable' sends cases that could not be assessed to T, which analysis.json counts in the preference denominator as genuine equal preference. That inflates ties, dilutes the A/B shares, and undercounts the unassessable tasks the study says it will report.
  - suggestion: Reserve 'Equally useful' for genuine equal preference after both answers were assessed. Route missing or unavailable information to 'Cannot assess' (U).
- [confirmed_defect] 'Cannot assess' is limited to page-load failure ('only if the page does not load'). Other real reasons a rater cannot judge, such as one answer being blank, truncated or unreadable, or the rater lacking the information needed, have no valid code. Raters are pushed into T or a forced A/B choice.
  - suggestion: Widen the U criterion to any case where the rater cannot meaningfully assess both answers, and give examples.
- [plausible_risk] The perspective is unclear. Raters judge what is 'more useful to you', but the study is about answering customer support questions. Some raters may judge for themselves and others for the customer who asked, which adds variance between raters. The instructions also say there is no single correct preference, so this may be intentional.
  - suggestion: Ask the owner to confirm the intended perspective (see owner_questions).
- [cannot_verify] The materials do not show whether answer position (A/B) is randomized or counterbalanced between the two generators, or how many raters judge each task. The only example item is a single illustration.
  - suggestion: Confirm that position counterbalancing and the generator-to-position mapping are recorded outside these files.

**Owner questions (2)**
- Ambiguity: Whose usefulness is being judged: 'more useful to you'.
  - Why it matters: If raters judge for themselves, preferences reflect personal habits (for example, whether they like phone reminders). If they judge for the customer, they weigh how well each answer fits the question. The two readings can give different A/B/T distributions.
  - Options: Keep 'more useful to you' (rater as a stand-in for the customer) | Change to 'more useful to the customer who asked this question'
  - Recommended default: Keep 'to you' and add 'imagine you asked this question', which keeps the subjective framing the study states.
  - Question: Should raters judge usefulness for themselves or for the customer who asked the question?
- Ambiguity: How to code a task where only one answer can be assessed (for example, one answer is blank or truncated). The current text only mentions 'the page does not load'.
  - Why it matters: Some raters would pick the readable answer (A/B), some would pick T, and some U. That changes both the preference distribution and the unassessable count.
  - Options: Code as U (both answers must be assessable) | Allow a preference for the readable answer
  - Recommended default: Code as U, which matches the report's 'where both answers could be assessed'.
  - Question: If one answer is missing or unreadable, should raters choose Cannot assess?

**Proposed patches:** 1; **rewrote the rubric anyway:** yes (1 file); **not verified:** Whether A/B position is randomized or counterbalanced across generators; Rater count per task, rater pool and the full task set (only one example item supplied); How the live platform renders the form or records U reasons

## SKILL v1
**Findings (5)**
- [confirmed_defect] The rater instructions send 'cannot judge' cases to the tie option. participant.md says to choose Equally useful (T) 'if information needed to make the judgment is unavailable'. analysis.json counts T in the preference denominator, and study.md defines the primary report as the preference distribution 'among judgments where both answers could be assessed, including genuine equal preference'. As written, cases that could not be assessed will be stored as T and counted as genuine ties. That inflates the tie rate, dilutes A/B shares, and leaves the separate count of unassessable tasks too low. The stored data cannot undo this, because both kinds of case end up with the same code.
  - suggestion: Limit Equally useful to cases where both answers were assessed and neither is meaningfully more useful. Route every case where either answer cannot be assessed to Cannot assess (U). Keep all codes and labels as they are. Before launch, check by rating a test item with missing information and confirming it is stored as U and left out of the preference denominator.
- [confirmed_defect] Cannot assess (U) is limited to a technical failure ('only if the page does not load'). The study's 'could not be assessed' category is wider than that. Cases where the page loads but a rater still cannot judge (for example an empty or cut-off answer, or a judgment that needs information the rater lacks) have no correct option. Together with the first finding, this pushes those cases into T or into a forced A/B choice.
  - suggestion: Redefine U as 'one or both answers cannot be assessed', with page-load failure as one example. Ask the owner whether a rater's own lack of knowledge should count as U (see owner_questions).
- [plausible_risk] It is unclear whose usefulness raters should judge. The instructions say 'more useful to you', but the task is framed as a customer's support question. Some raters will answer from their own habits (for example, whether they personally use reminders). Others will judge usefulness for the customer who asked. These readings can give different preferences on the same item.
  - suggestion: Owner to choose the perspective. The study accepts that preferences vary ('there need not be one objectively correct preference'), so a personal perspective is reasonable if that is what is intended. Either way, state the perspective explicitly.
- [cannot_verify] Nothing supplied shows how answers are blinded or how sides are assigned. The materials do not show whether the generator identity is hidden, whether which generator appears as A or B is randomized or counterbalanced per assignment, or whether each response records which generator was shown as A and which as B. Without that mapping, stored A/B codes cannot be turned into generator preferences, and a fixed side would mix position bias into the result.
  - suggestion: Provide the assignment configuration and one test response record. These should show that generator side is randomized and that each response stores the stable generator ID shown as A and as B.
- [cannot_verify] The sample question and answers are part of the instruction text. It is unclear whether this pair is a worked example, a practice item or a real rated item. If it is an example with a suggested answer, it could create a side cue. No suggested answer is given, so no defect is confirmed.
  - suggestion: Label the block as 'Example (not scored)' or move it to the task screen, depending on what it is meant to be.

**Owner questions (2)**
- Ambiguity: What counts as 'could not be assessed' beyond a technical failure? Currently: 'Choose Cannot assess only if the page does not load' vs study.md 'tasks that could not be assessed'.
  - Why it matters: If a rater who lacks the knowledge to judge chooses U, those tasks are left out of the preference denominator. If they are expected to choose anyway, they record A, B or T. This changes both the preference distribution and the unassessable count.
  - Options: U = technical or content failure only (page or answer missing, empty or cut off); raters always judge otherwise | U = technical or content failure OR information needed to judge is unavailable (the case the current text sends to T) | Also split U into sub-reasons in a follow-up field (new field; outside the current schema)
  - Recommended default: Option 2: U covers any case where either answer cannot be assessed, including missing information. This matches study.md's 'both answers could be assessed' and needs no schema change.
  - Question: Should 'Cannot assess' cover cases where the page loads but the rater lacks the information needed to judge, or only technical or content failures?
- Ambiguity: Whose usefulness is judged? Currently 'more useful to you' vs 'Read the customer question'.
  - Why it matters: Raters judging from their own habits can choose differently from raters judging for the asking customer. That changes what the preference distribution measures.
  - Options: Rater's own perspective: 'if you had asked this question' | The customer who asked, as stated in the question | A general support-quality standard
  - Recommended default: 'More useful to you if you had asked this question'. It keeps the current wording's personal-preference intent and makes the perspective explicit.
  - Question: Should raters judge usefulness for themselves as the asker, or for the customer described in the question?

**Proposed patches:** 3; **rewrote the rubric anyway:** yes (1 file); **not verified:** Rendered UI or preview: no screenshot or URL supplied. The form labels match form.json in the text only.; A/B side randomization, blinding and storage of which generator was shown on each side: no assignment config or test records; Display-to-storage mapping: no test response record. Intended consis

## SKILL v2
**Findings (5)**
- [confirmed_defect] The rater instructions send unassessable cases to the tie option. participant.md says to 'Choose Equally useful if neither is meaningfully more useful, or if information needed to make the judgment is unavailable.' 'Equally useful' is code T, and analysis.json counts T in the preference denominator. study.md says the primary report covers only 'judgments where both answers could be assessed, including genuine equal preference', with unassessable tasks reported separately. As written, missing-information cases would be counted as real ties, which inflates the tie share and dilutes the A and B shares of the main metric.
  - suggestion: Limit 'Equally useful' to cases where both answers were assessed and neither is meaningfully more useful. Send missing or unavailable information to 'Cannot assess' (U). Codes stay the same.
- [confirmed_defect] The 'Cannot assess' rule is too narrow for its job in the analysis. participant.md says 'Choose Cannot assess only if the page does not load.' If the page does not load, the rater cannot see or answer the form, so U can hardly ever be recorded. Partial failures have no valid option: one answer missing, blank, truncated or unreadable. Raters would have to pick T, or A/B for whichever answer did render. The separate unassessable count that study.md asks for would then be close to zero and wrong.
  - suggestion: Widen U to cover a question or either answer that is missing, did not load or cannot be read, plus cases where information needed for the judgment is unavailable. Whether U should also cover the rater's own lack of knowledge or context is an owner decision (see owner_questions).
- [plausible_risk] The usefulness criterion is not fully defined. 'More useful to you' points to the rater's own situation, not the customer who asked. Two considerations are listed ('addresses the question and gives practical steps') with no order of priority, and 'meaningfully more useful' has no threshold. The materials do allow legitimate disagreement ('there need not be one objectively correct preference'), but unclear wording can add noise that is not real preference variation.
  - suggestion: Settling these points changes what the study measures, so they are listed as owner questions. They were not changed in the revised draft.
- [cannot_verify] Nothing supplied shows blinding, A/B side randomization or counterbalancing per assignment, or a record linking displayed A/B to stable generator IDs. form.json stores only A/B/T/U, which are display-side codes. Without a per-response mapping, A/B preferences cannot be attributed to the generators, and position bias cannot be checked.
  - suggestion: Supply the assignment configuration and a sample response record showing the displayed side to generator ID mapping per response, then confirm side is randomized or counterbalanced.
- [cannot_verify] The rendered interface, question order, test response records and storage of codes could not be checked. Only source text and a codebook were supplied. The headphones item in participant.md may be a worked example or a live item. If it is an example, it gives no reason and no expected answer, so its purpose is unclear.
  - suggestion: Provide a preview screenshot or test record if display-to-storage mapping should be verified. Confirm whether the headphones item is a practice example (see owner_questions).

**Owner questions (5)**
- Ambiguity: Whose usefulness counts: 'Choose A or B if one would be more useful to you.'
  - Why it matters: If raters judge for themselves, someone who already uses phone reminders may prefer B for personal reasons. If they judge for the customer who asked, they weigh how well each answer fits the stated need. The two readings produce different preference distributions, and only the second one estimates usefulness for support users.
  - Options: Rater's own perspective: keep 'more useful to you if you had asked this question'. | Customer's perspective: 'Choose the answer that would be more useful to the customer who asked this question.' | Typical user: 'Choose the answer that would be more useful to a typical person asking this question.'
  - Recommended default: Option 1, 'more useful to you if you had asked this question'. It keeps the current wording and fits 'there need not be one objectively correct preference', while making clear that raters should picture themselves as the person asking.
  - Question: Should raters judge usefulness for themselves or for the customer who asked? Note that this choice changes what the study measures.
- Ambiguity: Precedence between criteria: 'Consider whether the answer addresses the question and gives practical steps.'
  - Why it matters: One answer may address the question directly but give few concrete steps, while the other gives detailed steps that only partly fit. Raters who put relevance first will choose differently from raters who put actionability first.
  - Options: Relevance first: 'First consider whether the answer addresses the question; among answers that do, prefer the one with more practical, usable steps.' | Holistic: 'Weigh both together in an overall judgment of usefulness.' | Keep both as non-exhaustive considerations with no stated order.
  - Recommended default: Relevance first. An answer that gives steps without addressing the question is rarely more useful, and a stated order reduces noise from unclear wording.
  - Question: When relevance and practical steps conflict, which should take priority, or should raters weigh them together?
- Ambiguity: What 'Cannot assess' covers beyond technical failure. The source mentions 'information needed to make the judgment is unavailable'.
  - Why it matters: If a rater lacks the background or personal context to judge (for example, a device they have never used), they could choose U, which leaves the item out of the denominator, or pick a preference anyway. A broader U reduces the denominator and may remove harder items selectively.
  - Options: Technical or content unavailability only: the question or an answer is missing, did not load or cannot be read. | Also include cases where information needed for the judgment is unavailable to the rater, such as missing context or unfamiliar subject matter. | Technical only, with raters told to judge on their best understanding otherwise.
  - Recommended default: Option 2, because it matches the source's own 'information needed ... unavailable' clause, now routed to U instead of T. Monitor the U rate in a pilot.
  - Question: Besides technical or display failures, should 'Cannot assess' cover the rater's own lack of information or context?
- Ambiguity: The tie threshold: 'neither is meaningfully more useful.'
  - Why it matters: Some raters will choose T whenever the difference is small, while others will pick a winner on any slight edge. That changes the tie share, which is part of the primary report.
  - Options: Keep 'meaningfully' undefined, so raters use their own judgment. | 'Choose A or B even if the difference is small; choose Equally useful only if you genuinely have no preference.' | 'Choose Equally useful if any difference is too small to matter in practice.'
  - Recommended default: Option 2. It reduces default ties while keeping a genuine-tie option, as study.md requires.
  - Question: Should slight preferences be recorded as A/B, or as 'Equally useful'?
- Ambiguity: What the headphones item is for: 'Question: How can I make sure I remember to charge my headphones? A: ... B: ...'
  - Why it matters: If it is a worked example, it gives no expected answer and no reason, so raters may infer a preferred side. If it is a live item, it sits inside the instructions.
  - Options: Live item: separate it from the instructions in the interface. | Worked example: label it 'Example' and add a brief note that either choice can be reasonable, with the reason. | Remove it from the instruction text.
  - Recommended default: Treat it as a live item shown below the instructions. That leaves the current layout unchanged until the owner confirms.
  - Question: Is the headphones comparison a practice example or a real rated item?

**Proposed patches:** 1; **rewrote the rubric anyway:** yes (1 file); **not verified:** Rendered interface and where instructions appear relative to the answer controls (no preview supplied); A/B side randomization or counterbalancing, blinding, and per-response mapping from displayed side to generator ID (no assignment config or records); Display-to-storage mapping of A/B/T/U codes (n

# case-018, motion-construct: control (no planted defect)
Opus, prompt P1 ("review and tell the owner what you find"), same contract, three arms

## BARE
**Findings (5)**
- [plausible_risk] Participants are told to read the prompt, but the participant instructions never say what the prompt is for. They don't say whether motion that is smooth but doesn't perform the prompted action (for example, the wrong action or a missing interaction) should count against a clip. study.md says the goal is 'more convincing motion for short action clips', which suggests the prompted action matters. participant.md judges motion quality only in the abstract.
  - suggestion: Have the owner decide whether the prompted action is part of motion quality, and then say so explicitly in participant.md (see owner_questions).
- [plausible_risk] The study design says audio is not part of the task, but the participant instructions don't tell raters to ignore audio. If clips have sound, it could affect motion preference.
  - suggestion: Add 'Ignore audio' to participant.md, or confirm that the clips are muted or silent.
- [plausible_risk] The participant instructions don't mention the replay controls or the reset-both button that the design relies on ('replay as needed'). Raters may judge from a single, out-of-sync viewing.
  - suggestion: Add a sentence saying raters may replay either clip, and can use reset-both to restart both clips in sync.
- [plausible_risk] 'Cannot judge' is limited to missing or unplayable clips. The instructions don't cover a clip that plays but is frozen, a static image, or truncated. Some raters may call that a playback failure, while others may treat it as a severe motion error. This would mix generator failures into the 'Cannot judge' bucket.
  - suggestion: State that a clip which plays but shows frozen or almost no motion should be judged as a motion failure, not marked Cannot judge (if the owner agrees).
- [cannot_verify] I couldn't verify the live UI, media, randomization or logging. This includes whether left/right is randomized per participant-item and kept on replay, whether both the displayed side and the stable output ID are recorded, and whether the controls work.
  - suggestion: Before launch, run a pilot that checks the logged side-to-output-ID mapping, that randomization stays the same on replay, and that the reset-both button works.

**Owner questions (1)**
- Ambiguity: The role of the prompt in judging motion: participants 'read the prompt', but the criteria are 'coherent trajectories, stable identities and physically plausible interactions'.
  - Why it matters: Suppose one clip has smooth motion but the wrong or a missing action, and the other has the correct action with small artifacts. Raters who only judge motion quality would pick the first. Raters who think the action has to match the prompt would pick the second.
  - Options: Motion quality only; the prompt is context and adherence is ignored | Motion should depict the prompted action; failing to perform it counts as a motion error | Collect prompt adherence as a separate secondary question
  - Recommended default: Count failure to perform the prompted action as a motion error, but don't penalize non-motion details (objects, style). This fits 'convincing motion for short action clips'.
  - Question: Should raters penalize a clip whose motion is plausible but doesn't perform the action described in the prompt?

**Proposed patches:** 1; **rewrote the rubric anyway:** yes (1 file); **not verified:** Video media and whether clips contain audio; Live UI: playback controls, reset-both, replay behavior; Left/right randomization and keeping it on replay; Logging of displayed side and stable output ID; Prompt text shown to participants

## SKILL v1
**Findings (5)**
- [plausible_risk] The rater instructions never say how the prompt relates to the motion judgment. The study brief says raters 'read the prompt' and the goal is 'more convincing motion for short action clips'. The participant text says only 'Compare motion in the two clips'. It does not say whether a clip with smooth, plausible motion that performs the wrong action (or no action) counts as convincing. Some raters may judge motion quality alone and others motion of the prompted action, so votes on prompt-mismatch items could split for reasons unrelated to motion.
  - suggestion: Have the owner decide what role the prompt plays (see owner question 1). Then add one sentence to the instructions and one worked example where a clip has good motion but the wrong action.
- [plausible_risk] The study brief says 'Audio is not part of this task', but the rater instructions say nothing about sound. If any clip has an audio track, sound quality or sync could affect motion preferences.
  - suggestion: Add 'Ignore sound; audio is not part of this task' to the instructions. Better still, strip or mute audio in the player for both clips. Check on the rendered preview that audio is muted for both sides.
- [plausible_risk] The materials do not say which stable output ID to record, or how, when the answer is 'No meaningful difference' or 'Cannot judge'. They also do not say how to record which clip failed when only one fails. The brief says 'Record the selected displayed side and stable output ID', which only makes sense for a Left or Right answer. Without a mapping for both sides, tie and failure records cannot be traced back to generators, and playback failures cannot be counted per generator.
  - suggestion: Store the left-to-ID and right-to-ID mapping on every response, not just the selected ID. For Cannot judge, record which side(s) failed (owner decision on whether to add this field). Verify with one test record per answer option.
- [cannot_verify] The answer options are well designed for this decision. The response form is pairwise preference, which matches 'select the generator'. The construct is limited to motion and excludes appeal. There are separate tie and technical-failure states and a rule for when both clips are flawed. Side is randomized per participant-item and kept on replay. However, none of this can be checked as built: no UI, assignment code, media or response records were supplied.
  - suggestion: Before launch, check in a preview: (a) side assignment varies across test assignments and stays the same on replay; (b) both panes have the same size, crop and resolution; (c) each displayed option stores its documented code and correct side-to-ID mapping. Pilot recommendation: there is only a reset-both button, so consider a shared play/pause control so raters can compare aligned motion. Any benefit for IRR is unproven.
- [plausible_risk] 'Cannot judge' is defined only as playback failure. The instructions do not cover a clip that plays but has almost no motion, or is so short or degraded that motion cannot be assessed. Raters could choose Cannot judge, No meaningful difference, or the other clip.
  - suggestion: State that a clip that plays but has static or near-static motion should be judged as a motion failure, not marked Cannot judge (owner to confirm).

**Owner questions (3)**
- Ambiguity: Study brief: 'Participants read the prompt'. Instructions: 'Compare motion in the two clips.' The role of the prompt is never stated.
  - Why it matters: Take a clip whose motion is fluid and plausible but which shows the wrong action, against one that shows the prompted action with some artifacts. Raters who judge motion only would prefer the first. Raters who judge 'convincing motion for this action' would prefer the second.
  - Options: Motion is judged against the prompted action: a clip that does not perform the prompted action has a motion error | The prompt is context only: judge motion quality whatever the action fidelity, and collect prompt adherence separately if needed | Add a separate prompt-adherence question next to the motion preference
  - Recommended default: Judge motion against the prompted action. The goal names 'action clips' and raters are told to read the prompt. Keep overall prompt adherence beyond the action out of scope.
  - Question: Should a clip that moves convincingly but does not perform the prompted action count as having worse motion, or should raters judge motion quality without regard to the prompt?
- Ambiguity: 'use Cannot judge for missing or unplayable clips' does not cover clips that play but have little or no motion.
  - Why it matters: Some raters would mark a static clip 'Cannot judge'. Others would count it as a motion failure and pick the other clip. That changes the win rates for generators that produce static output.
  - Options: A static or near-static clip that plays is a motion failure; choose the other clip unless both are static | A static clip counts as Cannot judge
  - Recommended default: Treat it as a motion failure; reserve Cannot judge for technical playback problems.
  - Question: When a clip plays but shows almost no motion, should raters count it as worse motion or mark Cannot judge?
- Ambiguity: 'Record the selected displayed side and stable output ID' gives no rule for tie and Cannot judge answers, or for which clip failed.
  - Why it matters: Without the full left/right-to-ID mapping on every record, ties and failures cannot be linked to generators, and you cannot analyze failure rates per generator.
  - Options: Store both displayed-side-to-ID mappings on every response | Also add a 'which clip failed' field for Cannot judge
  - Recommended default: Store both mappings on every response. Treat the failed-side field as an optional addition.
  - Question: Can the export store both left and right output IDs on every response, and do you want raters to say which clip failed when they choose Cannot judge?

**Proposed patches:** 4; **rewrote the rubric anyway:** yes (1 file); **not verified:** Rendered UI, pane parity, player controls and reset-both behavior (no preview or screenshots supplied); Left/right randomization and persistence on replay (no assignment code or records); Mapping from displayed option to stored data and stable output IDs (no codebook or test records); Media: clip le

## SKILL v2
**Findings (7)**
- [confirmed_defect] Participant instructions never mention the text prompt, although the study design says participants read the prompt before watching. Raters get no guidance on whether the prompt matters to a motion judgment, for example a smooth clip that shows the wrong action.
  - suggestion: Tell raters a prompt is shown and say how to use it. How much prompt adherence should count is an owner decision (see owner_questions).
- [confirmed_defect] Participant instructions do not say that replay is allowed. The study design permits replay, and it gives each clip its own controls plus a reset-both button.
  - suggestion: Add: 'You may replay either clip as often as needed; use Reset both to restart them together.'
- [plausible_risk] Rater text does not exclude audio, although the study says audio is not part of the task. If clips have sound, raters may let it influence their preference.
  - suggestion: Add 'Ignore any audio.' Or confirm that clips are served muted or have no audio track.
- [plausible_risk] The no-preference option is defined by a threshold ('meaningfully better') with no anchor, and there is no option for 'can watch it but cannot decide'. Raters with similar perceptions may split between a forced side, No meaningful difference, and Cannot judge.
  - suggestion: Owner to define the tie threshold and to say whether 'hard to decide' goes to tie (see owner_questions). Keep Cannot judge for playback failure only, as the study states.
- [plausible_risk] The participant text broadens Cannot judge from 'playback failure' to 'missing or unplayable clips'. The two mostly match, but 'missing' could cover a missing prompt or a clip that is truncated yet playable. The analysis could treat these differently.
  - suggestion: Align the wording. For example: 'Cannot judge: a clip is missing, will not play, or stops before the end.' Confirm this matches the owner's intent.
- [cannot_verify] Interface and data behaviour cannot be verified: per-participant-item left/right randomization, side retained on replay, independent controls and reset-both, full-clip enforcement, and recording of displayed side plus stable output ID. No screenshots, preview, configuration or test response records were supplied.
  - suggestion: Supply a preview or screenshots and 2–3 test response records showing displayed side, stable output ID and the selected option, so the mapping can be checked.
- [cannot_verify] Clip content, durations, aspect ratios, audio state and whether paired clips are time-aligned cannot be verified. No media was supplied.
  - suggestion: Provide sample paired clips, or a manifest with duration, resolution and audio track per output.

**Owner questions (5)**
- Ambiguity: How 'convincing motion' relates to the listed criteria, and which criterion wins when they conflict. Source: 'Prefer coherent trajectories, stable identities and physically plausible interactions.'
  - Why it matters: Take one clip with stable identities but floaty physics and another with realistic physics but a brief identity swap. Some raters will favour identity and others physics, so the preference becomes rater-dependent instead of measuring the owner's construct.
  - Options: Equal weight, holistic: 'Weigh all three together; no single criterion automatically wins.' | Explicit precedence: 'Identity breaks (morphing, swapping) outweigh trajectory issues, which outweigh minor physics implausibility.' | Severity-based only: 'Judge by how much each error disrupts the believability of the action, whatever its type.'
  - Recommended default: Severity-based only. It fits the existing 'less disruptive' language and the 'convincing' goal without imposing an unvalidated ranking.
  - Question: When the motion criteria conflict, should raters weigh them holistically, follow a fixed precedence, or judge by disruptiveness? (This changes what the study measures.)
- Ambiguity: 'choose the clip with fewer or less disruptive motion errors' does not say what to do when count and severity disagree.
  - Why it matters: Take one clip with many tiny jitters and another with a single major limb-merge. A rater counting errors picks the second clip; a rater weighing severity picks the first.
  - Options: Severity first: 'If one clip has fewer but more severe errors, prefer the clip whose errors are less disruptive overall.' | Count first: 'Prefer the clip with fewer distinct motion errors; use severity only to break ties.'
  - Recommended default: Severity first. Disruptiveness tracks 'convincing' motion better than a raw count.
  - Question: When error count and severity conflict, which should decide the preference?
- Ambiguity: Whether prompt adherence of the action counts. The study is about 'convincing motion for short action clips', but the rater text never mentions the prompt.
  - Why it matters: Take a clip with fluid motion of the wrong action and a clip with slightly jerky motion of the requested action. Raters will split depending on whether they treat the prompt as in scope.
  - Options: Exclude: 'Judge motion quality only; do not penalize a clip for not matching the prompt.' | Include as context: 'Use the prompt to know which action is intended; motion that does not perform the requested action counts as a motion error.' | Gate: 'If a clip does not attempt the prompted action at all, prefer the other clip.'
  - Recommended default: Include as context. The goal names action clips and the design has raters read the prompt, but owner confirmation is needed because this widens the construct.
  - Question: Should failing to perform the prompted action affect the motion preference, and if so, how?
- Ambiguity: Threshold for a tie: 'Use No meaningful difference if neither is meaningfully better'. It is also unclear whether 'both bad equally' or 'I can't decide' belongs here.
  - Why it matters: Cautious raters will choose ties often and decisive raters will rarely do so. This changes win rates and tie rates between raters for the same pairs.
  - Options: Strict tie: 'Choose a side whenever you notice any motion difference; use No meaningful difference only if you cannot see one after replaying.' | Practical tie: 'Use No meaningful difference when any difference is too small to matter to a typical viewer, including when both are equally flawed.'
  - Recommended default: Practical tie, with 'equally flawed' and 'cannot decide after replay' both routed to No meaningful difference. This keeps Cannot judge for playback failure only.
  - Question: How large must a difference be to choose a side, and should 'equally flawed' and 'cannot decide' be recorded as No meaningful difference?
- Ambiguity: Scope of 'motion errors' against adjacent visual artifacts and camera motion. Source: 'Ignore color grading and still-frame beauty.'
  - Why it matters: Flicker, texture boiling, background warping and camera shake are temporal but not subject motion. Some raters will count them and others will ignore them.
  - Options: Subject motion only: 'Judge the movement of people, animals and objects; ignore camera motion and texture flicker.' | All temporal artifacts: 'Any change over time that looks unnatural counts, including flicker, warping backgrounds and erratic camera motion.'
  - Recommended default: All temporal artifacts except deliberate camera movement. It is closer to 'convincing motion', but this needs owner confirmation.
  - Question: Should camera motion, flicker and background warping count as motion errors?

**Proposed patches:** 2; **rewrote the rubric anyway:** no; **not verified:** Rendered interface, playback controls, reset-both, full-watch enforcement; Left/right randomization per participant-item and retention on replay; Response records (displayed side + stable output ID mapping); Media content, durations, alignment, audio presence; Human comprehension and workload (needs
