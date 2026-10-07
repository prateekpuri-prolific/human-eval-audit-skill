# Collect evidence for a scoped study review

Read when reviewing mixed artifacts, extracting source material, or walking through a study. This is a collection guide, not a required integration contract.

## Route by visibility

| Evidence | Collect | Boundary |
| --- | --- | --- |
| Document, Markdown, PDF | Original instructions, questions/options, examples, version and page/section pointers | Mark OCR/extraction and uncertain layout; preserve original for comparison |
| Screenshot or recording | Visible wording, media/reference roles, viewport, controls and shown transitions | Unseen branches, randomization and saving remain unverified |
| Runnable preview | Relevant ordinary path, boundary/error state and available branch variants; record actions and outcomes | Use test identity only if supplied/authorized; no production slots or live ratings |
| Media/reference set | Bounded representative items, roles, loading and display quality | A transcript is not audio; sampled frames are not full motion/audio |
| Configuration/code | Relevant settings, version, branch and assignment rules | Intended behavior is not verified runtime behavior |
| Responses/test receipts | Question/version IDs, raw option values, displayed-to-stable candidate mapping, outcome of authorized test writes | Do not infer offered choices or absent training solely from answered records |

Record each fact as observed, transformed, inferred or unknown. Keep availability separate from reliability: an inspected export may still belong to a different version. If sources conflict, name the conflict and resolve the version before prescribing a change; do not silently privilege a stale rubric or code snapshot.

## Bounded walkthrough

Start from the supplied study, not an account-wide scan. Choose an ordinary item, a meaningful boundary case and a missing-evidence/error route if available. Follow branches relevant to the requested checks; record unvisited ones. Do not manufacture media failures or submit retries outside a safe, authorized test environment. Stop once applicable claims have evidence or a concrete coverage limit. “All available evidence” is not a request to download all media or click every possible path.

A reusable capture can be ordinary Markdown plus screenshots, or an existing recorder's export. Useful fields are study/version, item/page/step, action, displayed question/options, media/reference roles, viewport, observed result, source pointer, and capture time. Include explicit unvisited branches and transformed content. No required JSON schema, browser vendor, or recording service.

Capture candidate-only media separately from completed response screens when preparing any later model evaluation. Check that screenshots actually contain the intended media; an offscreen blank capture is a collection failure, not a study failure. Do not treat model-enriched summaries as originals. Paraphrasing private wording neither proves transmission permission nor preserves exact wording defects: retain its transformation status and use an approved source-handling route.

## Timing and completion

Observed playback duration and interaction steps can establish a lower bound or workload inventory. Agent latency and generated reading estimates are not human completion time. Full human burden, abandonment and fatigue require human/pilot evidence. Preserve test identifiers and minimize any participant data in saved captures.

Before reviewing, the packet should contain enough evidence for each selected check or explicitly mark that check unavailable. Review the supported subset now; return for one targeted fact only if it could change a consequential conclusion.
