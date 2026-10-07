"""Original development fixtures. No customer study text or participant data."""
import json

def js(x): return json.dumps(x,indent=2,ensure_ascii=False)+'\n'
FAMILIES=[]
def add(slug,title,modality,form,origin,brief,files,changes,hide,issue,repair,preserve,limits=None):
 FAMILIES.append(dict(slug=slug,title=title,modality=modality,form=form,origin=origin,brief=brief,files=files,changes=changes,hide=hide,issue=issue,repair=repair,preserve=preserve,limits=limits or ['No actual participant outcomes; no causal or IRR-improvement claim supported.','No live deployed interface or media pixels/waveforms supplied.']))

add('motion-construct','Motion versus overall preference','video','SxS preference','Internal observation (reference removed for publication)',
'''# Motion evaluation
Owner goal: select the generator with more convincing motion for short action clips. The primary response is motion preference, not overall visual appeal.
Participants read the prompt, watch both complete clips, replay as needed, then answer. Left/right assignment is randomized once per participant-item and retained on replay. Both clips have independent controls and a reset-both button. There is no claim that simultaneous playback improves agreement.
Options: Left / Right / No meaningful difference / Cannot judge (playback failure). Record the selected displayed side and stable output ID. Audio is not part of this task.
''',
{'participant.md':'# Instructions\nCompare motion in the two clips.\n\nWatch both clips fully. Prefer coherent trajectories, stable identities and physically plausible interactions. Ignore color grading and still-frame beauty. When both are flawed, choose the clip with fewer or less disruptive motion errors. Use No meaningful difference if neither is meaningfully better; use Cannot judge for missing or unplayable clips.\n'},
{'participant.md':('Compare motion in the two clips.','Choose the clip you prefer overall, including composition and appearance.')},['participant.md'],
'Introduction asks overall preference while detailed guidance and owner goal ask motion only.','Align introduction to motion; preserve tie and cannot-judge options.','Motion construct, side-to-output mapping and existing response codes.')

add('resume-mapping','Responses after session resume','video','SxS preference','Internal observation (reference removed for publication)',
'''# Short action clip preference
Choose Left, Right, Tie or Cannot judge after watching both outputs. Assigned item order may differ between participants, but resume must restore the same items, side mapping and answers for one session. The response field chosen_output_id records the selected output, not its screen position.
The supplied trace is a synthetic integration test, not a live participant record. Review the rubric and trace together. Do not claim to deploy a backend repair.
''',
{'session.csv':'event,session,item_id,left_id,right_id,selected_side,stored_item_id,stored_output_id\nsubmit,s01,item-7,out-7a,out-7b,left,item-7,out-7a\nresume,s01,item-7,out-7a,out-7b,left,item-7,out-7a\nsubmit,s02,item-2,out-2b,out-2a,right,item-2,out-2a\n'},
{'session.csv':('resume,s01,item-7,out-7a,out-7b,left,item-7,out-7a','resume,s01,item-7,out-7a,out-7b,left,item-2,out-2b')},['session.csv'],
'Resumed response is associated with a different item/output than displayed.','Propose stable identity-based persistence and a regression test for resume. Do not remove between-participant randomization.','Per-session consistency and legitimate between-rater randomization.')

add('narration-binding','Which video is being narrated?','video','pointwise + binary dimensions','Internal observation (reference removed for publication)',
'''# Accessibility narration evaluation
Rate the narration for the candidate clip only. A reference clip shows the target action and is not the narration source. Rate candidate-narration accuracy 1 (unrelated), 2 (major mismatches), 3 (mixed), 4 (minor omissions), 5 (accurate). Also mark whether any narrated object is absent: Yes / No / Cannot judge.
The dataset has reference_video_url and candidate_video_url. The owner explicitly requires candidate-video narration. A missing binding must be resolved before generating narration; do not infer it from column order.
''',
{'config.json':js({'fields':['reference_video_url','candidate_video_url'],'narration':{'source_field':'candidate_video_url'},'rating_target':'candidate_narration','schema_version':1})},
{'config.json':('"source_field": "candidate_video_url"','"source_field": "reference_video_url"')},['config.json'],
'Narration configuration binds the reference instead of the intended candidate.','Set source_field to candidate_video_url; preserve reference role and response scale.','Reference/candidate distinction and pointwise narration target.')

add('side-assignment','Position randomization and stable labels','video','SxS preference + binary subdimension','Internal observation (reference removed for publication)',
'''# Overall clip preference
Goal: compare systems across a balanced clip bank without making system identity synonymous with screen position. Participants choose Left / Right / Tie, then mark whether either clip has a continuity error (Left, Right, Both, Neither, Cannot judge). System names are hidden. Side assignment should be balanced across the study and stable within an item. Never shuffle ordinal response labels.
The assignment file is the complete planned schedule for this small synthetic test, not a sample of realized random assignments. No playback or human outcomes are supplied.
''',
{'assignment.csv':'item,left_system,right_system\na,system-x,system-y\nb,system-y,system-x\nc,system-x,system-y\nd,system-y,system-x\n'},
{'assignment.csv':('system-y,system-x','system-x,system-y')},['assignment.csv'],
'Complete planned assignment confounds system with position on every item.','Balance or randomize side assignments with stable output IDs; keep ordinal scales ordered.','Blinding, stable within-item assignment and post-preference diagnostic question.')

add('playback-evidence','Playback claims from a static preview','video','SxS preference','Progressive visibility and UI evidence checks',
'''# Video comparison
Rate action continuity after watching both clips. Responses: Left / Right / Tie / Cannot judge. Both clips must be playable before a judgment can be saved. A static HTML mock is provided alongside a synthetic interaction receipt when available. It does not contain real video assets.
A screenshot or mock alone cannot establish synchronization, successful playback or saved-response behavior. Review supplied evidence and request the smallest missing check.
''',
{'preview.html':'<!doctype html><html><body><h1>Compare continuity</h1><section><h2>Left</h2><button>Play left</button><p>Clip A placeholder</p></section><section><h2>Right</h2><button>Play right</button><p>Clip B placeholder</p></section><button>Cannot judge</button></body></html>',
'receipt.json':js({'synthetic_test':True,'left_playback':'ended','right_playback':'ended','save_enabled':True,'saved_choice':'Left'})},
{'receipt.json':('"right_playback": "ended"','"right_playback": "decode_error"')},['receipt.json'],
'Test receipt allows a preference save despite candidate playback failure.','Gate ordinary choice on playable candidates and keep cannot-judge route; do not claim mock proves actual playback.','No mandated simultaneous playback; maintain legitimate abstention.')

add('selection-cap','Diagnostic tags with a selection cap','audio','SxS preference + binary tags','Internal observation (reference removed for publication)',
'''# Speech generation comparison
Listen to both utterances at a comfortable level. Choose A / B / Tie / Cannot judge for naturalness. Then select up to two audible issues that most affected your choice. The tags are diagnostics, not an additional ranking, and do not determine a correct preference.
Tags: clipping, repetitions, unnatural pauses, distorted phonemes, none. None must be exclusive. Do not change the primary preference response.
''',
{'questions.json':js({'preference':{'type':'single','options':['A','B','Tie','Cannot judge']},'diagnostics':{'type':'multiple','helper':'Select up to two','answer_limit':2,'options':['clipping','repetitions','unnatural pauses','distorted phonemes','none'],'exclusive_options':['none']}})},
{'questions.json':('"answer_limit": 2','"answer_limit": -1')},['questions.json'],
'Configured unlimited selection disagrees with an explicit cap of two.','Set cap to two, retaining exclusive none and primary preference; verify runtime enforcement separately.','Preference, diagnostic labels and exclusive none.')

add('export-freshness','Export scope and completeness','audio','pointwise ratings','Internal observation (reference removed for publication) / Internal observation (reference removed for publication) duplicate incident',
'''# Speech intelligibility audit
Participants rate each utterance from 1 (no words intelligible) to 5 (all words intelligible). Export uses one row per approved submission. A frozen eligible-ID manifest and an export receipt refer to the same UTC cutoff, study and no-filter scope. IDs here are fabricated. Review completeness, not participant competence.
A deliberately filtered export is not inherently defective; compare scope and denominator before flagging.
''',
{'eligible.csv':'submission_id\ns1\ns2\ns3\ns4\n','export.csv':'submission_id,rating\ns1,3\ns2,4\ns3,2\ns4,5\n','receipt.json':js({'scope':'all approved submissions','cutoff_utc':'2026-09-15T12:00:00Z','exported_at':'2026-09-15T12:01:00Z','expected_rows':4,'row_unit':'submission','filters':[]})},
{'export.csv':('s3,2\ns4,5\n','')},['eligible.csv','receipt.json'],
'Export omits two eligible submissions under identical cutoff/scope.','Reconcile job version, filters and eligible IDs and re-export; never fabricate missing ratings.','Row unit, cutoff and legitimate filters.')

add('optional-upload','Optional pronunciation recording','audio','collection + optional upload','Internal observation (reference removed for publication)',
'''# Pronunciation feedback
Write how easy a phrase is to pronounce, using Easy / Moderate / Difficult / Cannot judge. You may optionally upload a short recording; declining must not block completion or affect compensation. Only upload your own recording and avoid names or other personal details. Accepted formats WAV or MP3, at most one file, maximum 15 MB.
The provided validator result is from a synthetic test; it does not demonstrate deployed behavior.
''',
{'config.json':js({'upload':{'min_files':0,'max_files':1,'accepted':['wav','mp3'],'max_mb':15}}),'validation.json':js({'submitted_files':0,'result':'accepted','other_required_fields_valid':True})},
{'validation.json':('"result": "accepted"','"result": "rejected: at least one file required"')},['validation.json'],
'Validator rejects zero uploads although guidance and configuration make recording optional.','Allow zero-file submission; test required-field behavior separately.','Recording remains optional; do not resolve by making it mandatory.')

add('subjective-gold','Taste preferences and gold checks','audio','SxS music preference','Training QA benchmark and synthetic-rater findings',
'''# Music preference
Choose which of two instrumental excerpts you would replay for enjoyment: A / B / No preference / Cannot judge. Both styles are valid; the goal is a distribution of taste, not technical correctness. Separately, a clearly instructed-response practice item asks the participant to choose “Ready.”
Do not use majority agreement or synthetic-persona agreement as an automatic rejection criterion. A validated objective check would need distinct evidence and a prespecified policy.
''',
{'quality-policy.json':js({'ordinary_preference':{'gold_key':None,'wrong_answer_action':'none'},'practice':{'question':'Select Ready to continue','key':'Ready','failure_action':'explain_and_retry'},'payment':'not affected by taste'})},
{'quality-policy.json':('"gold_key": null,\n    "wrong_answer_action": "none"','"gold_key": "A",\n    "wrong_answer_action": "reject_submission"')},['quality-policy.json'],
'Unvalidated taste preference is assigned a unique gold key and punitive action.','Remove correctness enforcement on preference; preserve ordinary responses and explicit practice retry.','Legitimate taste heterogeneity; no invented media gold.')

add('audio-scale','A scale that changes what it measures','audio','pointwise ordinal','Internal observation (reference removed for publication)',
'''# Audible distortion
Rate only distortion in one generated spoken passage. Do not rate accent, liking or whether you agree with its content. Headphones are recommended; choose Cannot judge if playback is unusable. The intended scale increases from no distortion to severe distortion, so larger values are worse. Output code meanings must remain stable.
''',
{'scale.json':js({'question':'How much audible distortion is present?','options':[{'code':1,'label':'None'},{'code':2,'label':'Slight'},{'code':3,'label':'Moderate'},{'code':4,'label':'Severe'}],'abstention':'Cannot judge'})},
{'scale.json':('"label": "Severe"','"label": "My favorite voice"')},['scale.json'],
'Highest distortion anchor switches to liking, violating the intended construct.','Restore a severe-distortion anchor without reversing code polarity.','Higher means worse; accent and taste are excluded.')

add('rank-validation','Distinct ranks across images','image','multiway ranking','Internal observation (reference removed for publication)',
'''# Poster legibility ranking
Rank four poster thumbnails from 1 (easiest to read) to 4 (hardest to read), using each rank once. Review all four before assigning ranks. The task is relative legibility, not overall design liking. If an image cannot load, use Cannot judge the set.
Fixtures provide form rules and an explicit validation receipt, not poster pixels or a deployed UI. The synthetic receipt submits duplicate ranks. Independent pointwise ratings would change the task.
''',
{'form.json':js({'fields':['poster-a','poster-b','poster-c','poster-d'],'type':'integer','min':1,'max':4,'unique_across_fields':True}), 'validation.json':js({'submitted':[1,1,3,4],'accepted':False,'message':'Each rank must be used once'})},
{'validation.json':('"accepted": false','"accepted": true')},['validation.json','form.json'],
'Explicit validation receipt accepts duplicate ranks despite uniqueness rule.','Require a permutation of 1–4 and clear correction feedback; retain cannot-judge option.','Relative ranking and lower-is-better polarity.')

add('range-boundary','Count ranges with shared boundaries','image','pointwise binary + count bins','Internal observation (reference removed for publication)',
'''# Object-count fidelity
Given a request for an image with several visible lanterns, first answer whether any lantern is visible (Yes / No / Cannot judge), then choose the number visible. Count a partly occluded lantern once if its distinct body is visible. Do not infer hidden objects.
Use the count bins exactly as configured. The intended bins partition nonnegative integer counts; Cannot judge is separate from zero. Example: two distinct lantern bodies means count 2.
''',
{'options.json':js({'count_options':['0','1–2','3–5','6 or more','Cannot judge']})},
{'options.json':('3–5','2–5')},['options.json'],
'Count 2 falls in two response bins.','Use nonoverlapping 1–2 and 3–5 bins or obtain owner-approved equivalent; preserve zero and abstention.','Integer counting policy; do not merge cannot-judge and zero.')

add('image-layout','Asymmetric candidate presentation','image','SxS preference','Prior UI screenshot and DES-102 preview visibility',
'''# Product image comparison
Which image better matches the written product request? Responses: Left / Right / Tie / Cannot judge. Evaluate the image content, not differences introduced by the interface. Both images should receive equivalent display treatment. The supplied HTML is a self-contained static mock with colored placeholders; it is evidence about layout only, not image quality, saving or assignment randomization.
''',
{'preview.html':'<!doctype html><html><head><style>.pair{display:flex;gap:20px}.candidate{width:240px;height:180px;background:#ccd8e9;border:1px solid #667} .right{width:240px;height:180px}</style></head><body><h1>Which matches the request?</h1><p>Request: a ceramic cup on a plain table.</p><div class="pair"><div class="candidate">Left image placeholder</div><div class="candidate right">Right image placeholder</div></div><p>Left · Right · Tie · Cannot judge</p></body></html>'},
{'preview.html':('.right{width:240px;height:180px}', '.right{width:80px;height:60px}')},['preview.html'],
'Preview gives one candidate materially less screen area.','Use equivalent size/fit treatment and verify real aspect-ratio handling; do not claim a known preference effect magnitude.','Equal opportunity to inspect; no conclusions about actual image quality.')

add('inspection-load','Required inspection workload','image','pointwise + multiple dimensions','Fatigue discussion: structural burden versus human prediction',
'''# Illustrated-scene inspection
Owner goal: collect object-presence and spatial-relation judgments on 12 scenes. Each scene has five binary checks, one overall 1–5 adherence rating, and a brief rationale only when an error is marked. Every scene must be inspected for at least 20 seconds. Instructions remain available beside each scene; checks are grouped by scene and can be revisited before submission.
This is a structural feasibility review. Do not infer a universal memory limit, actual fatigue or expected IRR from word count or an LLM run. Timing below excludes onboarding and any rationale entry, so it is a lower bound.
''',
{'schedule.json':js({'scenes':12,'minimum_view_seconds_per_scene':20,'session_time_limit_seconds':600,'instructions_persistent':True,'required_rationale':'only_if_error'})},
{'schedule.json':('"session_time_limit_seconds": 600','"session_time_limit_seconds": 180')},['schedule.json'],
'Mandatory viewing alone requires 240 seconds, exceeding the 180-second session limit.','Increase limit beyond minimum viewing plus measured response/onboarding time or seek approval to reduce workload. No precise fatigue prediction.','Required coverage and construct; changing item count needs owner decision.')

add('source-roles','Reference versus candidate fields','image','pointwise + binary dimensions','DES-263 and progressive collection requirements',
'''# Image edit evaluation
Compare the candidate edit against the reference photograph and edit request. Rate edit compliance 1–5 and mark unintended changes Yes / No / Cannot judge. The reference is not an output to score. A collection summary may omit question configurations; retrieve both guidance and question definitions before deciding what the instrument asks.
''',
{'questions.json':js({'display':{'reference_field':'original_image','candidate_field':'edited_image'},'rating':{'target_field':'edited_image','scale':[1,2,3,4,5]},'unintended_changes':{'target_field':'edited_image','options':['Yes','No','Cannot judge']}})},
{'questions.json':('"target_field": "edited_image"','"target_field": "original_image"')},['questions.json'],
'Configured rating target is original rather than edited image.','Bind rating targets to edited_image while retaining original_image as reference.','Reference and candidate roles, ordered 1–5 scale.')

add('answer-leakage','Unaided knowledge after an answer cue','text','knowledge + confidence','Internal observation (reference removed for publication)',
'''# Terminology familiarity
Goal: measure unaided knowledge of a fictional technical abbreviation, then show its definition and ask whether that explanation helps. Do not search externally. Use Don't know rather than guessing if unfamiliar. The abbreviation is invented for this fixture.
Answer labels and codes must remain stable; the intended change is ordering, not making the knowledge test easier.
''',
{'pages.json':js({'pages':[{'id':'knowledge','prompt':'What does RLT stand for?','options':['Rapid Load Transfer','Recursive Label Test','Remote Link Timing',"Don't know"]},{'id':'definition','text':'In this glossary RLT means Rapid Load Transfer.'},{'id':'helpfulness','prompt':'Was the explanation helpful?','options':['Yes','No','Unsure']}]})},
{'pages.json':('"pages": [','"pages": [\n    {"id":"primer","text":"RLT means Rapid Load Transfer."},')},['pages.json'],
'Answer appears before an explicitly unaided knowledge measure.','Place the knowledge item before any definition; retain post-definition helpfulness stage.','Unaided knowledge estimand and intentional later disclosure.')

add('merged-options','Alternative labels merged into one','text','comparison + rationale','Internal observation (reference removed for publication)',
'''# Summarization preference
Read the source passage and two summaries. Choose which better preserves the source's main point without unsupported additions. Response codes are A, B, T (equally good), U (cannot judge). Briefly explain a choice of A or B. Do not use writing style to override factual correctness. Source and summaries are supplied below.
Source: The museum closes on Mondays. Admission is free for children under twelve.
Summary A: Children younger than twelve enter free; the museum is closed Mondays.
Summary B: The museum is open daily and free for all children.
These demonstration texts are not an attention check or rejection key.
''',
{'options.json':js({'options':[{'code':'A','label':'Summary A'},{'code':'B','label':'Summary B'},{'code':'T','label':'Equally good'},{'code':'U','label':'Cannot judge'}]})},
{'options.json':('"label": "Summary B"\n    },\n    {\n      "code": "T",\n      "label": "Equally good"','"label": "Summary B / Equally good"')},['options.json'],
'Tie label is merged into B and its distinct code disappears.','Restore separate B and T options without changing response-code meaning.','A/B/T/U schema and non-punitive demonstration.')

add('promised-followup','Instructions promise a missing follow-up','text','pointwise rating + interpretation','Internal observation (reference removed for publication)',
'''# Contextual sentence judgment
Read each situation, then rate how appropriate the target sentence is from 1 (completely inappropriate) to 7 (completely appropriate). Assume the situation is as stated; do not add facts. After each rating, answer one interpretation question. An optional comment box lets you explain an ambiguity. The owner intends to analyze rating and interpretation jointly.
This packet contains the complete one-item form configuration; there are no external follow-up pages.
''',
{'form.json':js({'fields':[{'id':'appropriateness','type':'single','options':[1,2,3,4,5,6,7]},{'id':'interpretation','type':'single','prompt':'Does the sentence require every visitor to leave?','options':['Yes','No','Unclear']},{'id':'comment','type':'text','optional':True}],'situation':'Some visitors remain inside after the bell.','target':'Not everyone left.'})},
{'form.json':('    {\n      "id": "interpretation",\n      "type": "single",\n      "prompt": "Does the sentence require every visitor to leave?",\n      "options": [\n        "Yes",\n        "No",\n        "Unclear"\n      ]\n    },\n','')},['form.json'],
'Complete form lacks promised interpretation field needed for joint analysis.','Restore interpretation question using intended options; do not delete goal to conceal omission.','Rating-plus-interpretation estimand and optional comment.')

add('exclusive-none','None alongside substantive answers','text','multi-select survey','Internal observation (reference removed for publication)',
'''# Editing workflow survey
Which editing activities did you perform in the past week? Select all that apply: fact-checking, shortening, tone adjustment, none. None means no listed activity and cannot be combined with any substantive option. This is self-report; there is no correct respondent profile.
The supplied test is synthetic and checks contradictory selections only.
''',
{'config.json':js({'options':['fact-checking','shortening','tone adjustment','none'],'exclusive_options':['none']}),'receipt.json':js({'selected':['none','fact-checking'],'accepted':False})},
{'receipt.json':('"accepted": false','"accepted": true')},['receipt.json'],
'Explicit receipt accepts none together with a substantive activity.','Reject or automatically deselect contradictory choices with clear feedback; validate other multi-select combinations.','Self-report validity; do not invent a correct personal answer.')

add('confidence-granularity','Per-dimension question, one response','text','comparison + Likert subdimensions','Internal observation (reference removed for publication)',
'''# Answer evaluation
Compare two responses to a support request. First choose A / B / Tie / Cannot judge for overall usefulness. Then provide separate 1–5 ratings for factual accuracy and actionability for each response. Accuracy: 1 many substantive errors, 3 mixed, 5 no detected factual errors. Actionability: 1 no usable steps, 3 partially usable, 5 clear feasible steps. Cannot assess is distinct from 1.
Separate ratings are required because the owner will analyze these two constructs independently. Do not infer a universal maximum dimension count or that independent widgets eliminate halo effects.
''',
{'form.json':js({'overall':['A','B','Tie','Cannot judge'],'subratings':[{'response':'A','dimension':'accuracy','field':'a_accuracy'},{'response':'A','dimension':'actionability','field':'a_actionability'},{'response':'B','dimension':'accuracy','field':'b_accuracy'},{'response':'B','dimension':'actionability','field':'b_actionability'}],'scale':[1,2,3,4,5,'Cannot assess']})},
{'form.json':('"field": "a_actionability"','"field": "a_accuracy"')},['form.json'],
'Two different dimensions for response A share one storage field.','Give each response-dimension pair a unique field and test roundtrip; preserve both constructs and scale.','Separate accuracy/actionability; no single holistic replacement.')
