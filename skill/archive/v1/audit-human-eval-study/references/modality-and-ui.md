# Rendered annotation UI and modality checks

Read this reference whenever a screenshot, recording, URL, open tab, prototype or UI source is supplied. Apply only checks supported by the artifact inspected. Sources were checked 2026-09-29. A layout preference is a recommendation to pilot, not proof of an IRR or accuracy effect.

## Evidence level

| Evidence | May support | Does not establish alone |
| --- | --- | --- |
| Screenshot | Visible question/context, labels, option order, apparent parity, clipping and visual hierarchy at that viewport. | Click/keyboard behavior, hidden branches, playback, save semantics, responsive layouts or accessibility conformance. |
| Screen recording | Behavior and states actually shown, including observed transitions. | Unrecorded branches, stable behavior across devices or codebook mapping. |
| Live URL or local preview | Rendered states and safe interactions the agent actually exercised. | Historical rater experience, unvisited branches, final export semantics or effects on human quality. |
| Source HTML/code | Intended wording, controls and branch logic. | The rendered state/version raters saw. |

When both a rubric and UI are available, compare exact wording, answer labels, scale direction, required fields, branch conditions and media/reference roles. Record source version and viewport. For a URL, use the host browser if accessible; if an interactive surface is unavailable, assess visible content and state the limit. Use a safe preview or test mode for branch tests. Avoid submitting live labels or changing a live study.

## Cross-modal UI checks

- **At the decision point:** Can raters see the named criterion, prompt/reference, candidate(s), and needed definitions/examples without losing their place? Are long items truncated or hidden by overlays? Relevant guidance and highlights helped in one 15-interface text study, while more validation was not uniformly better. [Dong et al. 2023](https://journals.sagepub.com/doi/abs/10.1177/01655515231204802).
- **Response semantics:** Are labels and controls visibly tied to the question, with distinct meanings for tie/neither/N/A/uncertain/technical failure where applicable? Does the UI reveal required fields and recoverable errors? [W3C WCAG 2.2](https://www.w3.org/TR/wcag/).
- **SxS parity and ordering:** Are A/B panes comparably sized, cropped, loaded and controllable? Is source/model identity concealed if blinding is intended? Check assignment configuration and exports for randomized/counterbalanced side or first/second position and the actual displayed mapping to stable IDs. For independent items, check item-order controls where context effects are plausible. A screenshot alone cannot verify randomization. The ordering of annotation items affected labels in one NLP study; this motivates testing, not an assumed effect size here. [Beck et al. 2024](https://aclanthology.org/2024.uncertainlp-1.8/).
- **Complex labels and rationales:** If options form a hierarchy or there are many categories, inspect grouping and staged gates rather than assuming a long flat list is harmless. If raters must mark spans/regions/times, check the selection gesture, zoom/seek and ability to revise. Interface affordances changed rationale selection in a text study; hierarchical presentation improved performance in one multi-label task. [Sullivan Jr. et al. 2022](https://aclanthology.org/2022.naacl-main.38/), [Stureborg et al. 2023](https://par.nsf.gov/servlets/purl/10468993).
- **Interaction and accessibility:** On an interactive preview, try keyboard navigation and visible focus, labels/instructions, validation errors, return/edit and relevant narrow viewport. Do not infer a keyboard failure from a screenshot. [W3C WCAG 2.2](https://www.w3.org/TR/wcag/).

## Modality-specific presentation

- **Text:** Preserve paragraphs, tables, code, citations and conversational context. Check long-answer scrolling and whether one side receives an easier reading layout.
- **Image:** Show the exact prompt and any source/reference image. Check equal display/crop/zoom, full-resolution inspection, and source versus edited-output roles. A small screenshot can suggest clipping but cannot prove full-resolution access.
- **Audio:** Inspect playback, replay, volume, duration, channel/headphone guidance where relevant, reference audio/transcript availability, load failures and symmetric controls. A transcript is insufficient to judge sound or the listening UI. [ITU-T P.808](https://www.itu.int/rec/T-REC-P.808).
- **Video:** Inspect full-clip access, aspect ratio, resolution, replay/seek, timecode and audio state. For matched SxS clips, consider shared play/pause/seek and an A/B audio switch, with adequate pane size and a fallback when timelines do not align. Simultaneous aligned comparison is a documented method; its IRR benefit for generated-video tasks is unproved. [ITU-T P.910 Annex C](https://www.itu.int/rec/dologin_pub.asp?id=T-REC-P.910-202111-S%21%21PDF-E&lang=e&type=items).

## Calibrate the strength of a finding

Report a visible or exercised failure as an observation with its exact viewport/step. For a plausible design improvement without direct outcome evidence, call it a **pilot recommendation**. A screenshot or heuristic checklist cannot certify study validity. In one dialogue-rating comparison, several different UIs yielded high-quality ratings with no significant quality difference between them. [den Hengst 2020](https://research.vu.nl/en/publications/collecting-high-quality-dialogue-user-satisfaction-ratings-with-t/). Task instruction guidelines have mixed empirical support across settings. [Wu and Quinn 2017](https://ojs.aaai.org/index.php/HCOMP/article/view/13317).
