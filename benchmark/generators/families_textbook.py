"""Textbook-mistake families (batch 1). Original synthetic fixtures; no customer study text or participant data.
Each family yields control / defect / partial variants via build_textbook_dataset.py. Controls are sound for the target mechanism, not claimed flawless."""
import json
NEW=[]
LIM=['No actual participant outcomes; no causal or IRR-improvement claim supported.','No live deployed interface or media supplied.']
ORG='Standard methods literature (textbook mistake); original synthetic fixture'
def add(slug,title,modality,form,brief,files,changes,hide,issue,repair,preserve,origin=ORG):
 NEW.append(dict(slug=slug,title=title,modality=modality,form=form,origin=origin,brief=brief,files=files,changes=changes,hide=hide,issue=issue,repair=repair,preserve=preserve,limits=LIM))
def js(x):return json.dumps(x,indent=2,ensure_ascii=False)+'\n'

# ---- A. Wording and instrument
add('leading-question','Instruction states what most reviewers think','text','pointwise rating',
'''# Helpfulness rating
Owner goal: estimate how helpful assistant replies are to the person who asked. Raters see one question and one reply and rate helpfulness. Rater-facing wording is in instructions.md and the scale is in scale.json. Wording should not signal an expected answer.
''',
{'instructions.md':'# Instructions\nRead the question and the reply. Rate how helpful the reply is for the person who asked.\n\nUse the full scale. Judge only this reply.\n','scale.json':'{\n  "options": [\n    {"code": 1, "label": "Not at all helpful"},\n    {"code": 2, "label": "Slightly helpful"},\n    {"code": 3, "label": "Moderately helpful"},\n    {"code": 4, "label": "Very helpful"},\n    {"code": 5, "label": "Extremely helpful"}\n  ]\n}\n'},
{'instructions.md':('Rate how helpful the reply is for the person who asked.','Most reviewers find these replies very helpful. Rate how helpful the reply is for the person who asked.')},['instructions.md'],
'The instruction states what most reviewers think, nudging ratings upward.','Remove the majority-opinion statement; keep the rating target and five-point scale.','Helpfulness construct, five-point scale, labels and codes.')

add('double-barreled','One item asks two things','text','pointwise binary',
'''# Factual accuracy check
Owner goal: measure factual accuracy of replies only. Tone and politeness are measured elsewhere and must not influence this item. The item is in survey.json and the general guidance is in instructions.md.
''',
{'survey.json':'{\n  "items": [\n    {"id": "accuracy", "prompt": "Is the reply factually accurate?", "options": ["Yes", "No", "Cannot tell"]}\n  ]\n}\n','instructions.md':'# Instructions\nAnswer the question below about the reply you just read. Choose Cannot tell if you cannot check the facts.\n'},
{'survey.json':('"prompt": "Is the reply factually accurate?"','"prompt": "Is the reply factually accurate and politely worded?"')},['survey.json'],
'A single item asks about accuracy and politeness, so a Yes or No cannot be interpreted.','Ask accuracy only in this item; keep tone out or in a separate item. Preserve the three options.','Accuracy-only construct and the Yes / No / Cannot tell options.')

add('unbalanced-scale','Scale with one negative and four positive options','text','pointwise rating',
'''# Perceived quality rating
Owner goal: obtain an unbiased estimate of perceived quality, including low quality. The scale must give raters as many ways to express a negative evaluation as a positive one. Scale definition is in scale.json; wording is in instructions.md.
''',
{'scale.json':'{\n  "options": [\n    {"code": 1, "label": "Very poor"},\n    {"code": 2, "label": "Poor"},\n    {"code": 3, "label": "Neither good nor poor"},\n    {"code": 4, "label": "Good"},\n    {"code": 5, "label": "Very good"}\n  ]\n}\n','instructions.md':'# Instructions\nRate the overall quality of the reply on the scale shown.\n'},
{'scale.json':('{"code": 1, "label": "Very poor"},\n    {"code": 2, "label": "Poor"},\n    {"code": 3, "label": "Neither good nor poor"},\n    {"code": 4, "label": "Good"},\n    {"code": 5, "label": "Very good"}','{"code": 1, "label": "Poor"},\n    {"code": 2, "label": "Fair"},\n    {"code": 3, "label": "Good"},\n    {"code": 4, "label": "Very good"},\n    {"code": 5, "label": "Excellent"}')},['scale.json'],
'Only one anchor is negative, so the scale is biased toward positive ratings.','Use a balanced scale with matching positive and negative anchors; keep five ordered codes.','Five ordered options and codes 1-5.')

add('demand-characteristics','Instructions reveal which system is the owner\'s','text','SxS preference',
'''# Assistant comparison
Owner goal: obtain an honest preference between two assistant replies. Raters should not be told which assistant the owner built or hopes will win. Instructions are in instructions.md and the display labels are in config.json.
''',
{'instructions.md':'# Instructions\nYou will compare two replies, labelled A and B. Choose the reply you prefer, or No preference.\n','config.json':'{\n  "labels": {"left": "Reply A", "right": "Reply B"},\n  "options": ["A", "B", "No preference"]\n}\n'},
{'instructions.md':('labelled A and B.','labelled A and B. Reply B comes from our new model, which we expect to be better.')},['instructions.md'],
'Instructions reveal the expected winner, creating demand characteristics.','Remove the hypothesis and the system identity from rater-facing text.','Preference task, labels and options A / B / No preference.')

add('mixed-polarity-items','Reverse-coded item not reverse-scored','text','multi-item agreement scale',
'''# Clarity scale
Owner goal: score reply clarity as the mean of two agreement items rated 1 (Strongly disagree) to 5 (Strongly agree). Item q2 is negatively worded ("The reply was confusing"). The scoring configuration is in analysis.json and the items are in items.json.
''',
{'items.json':'{\n  "items": [\n    {"id": "q1", "text": "The reply was clear."},\n    {"id": "q2", "text": "The reply was confusing."}\n  ],\n  "scale": [1, 2, 3, 4, 5]\n}\n','analysis.json':'{\n  "score": "mean(q1, q2)",\n  "reverse_coded": ["q2"]\n}\n'},
{'analysis.json':('"reverse_coded": ["q2"]','"reverse_coded": []')},['analysis.json'],
'A negatively worded item is averaged with a positive item without reverse scoring.','Reverse-score q2 before averaging; keep items and scale unchanged.','Items, five-point scale and the mean-score construct.')

# ---- B. Design and assignment
add('order-counterbalancing','Every rater sees the same condition first','text','SxS preference',
'''# Order of presentation
Owner goal: compare two systems without the order of presentation favouring either. Each rater sees both replies for each item in sequence. The presentation order per rater is in assignment.csv.
''',
{'assignment.csv':'rater,item,first,second\nr1,i1,A,B\nr2,i1,B,A\nr3,i1,A,B\nr4,i1,B,A\nr5,i1,A,B\nr6,i1,B,A\n','notes.md':'# Notes\nSystems A and B are shown with identical formatting. Raters answer after seeing both.\n'},
{'assignment.csv':('r2,i1,B,A\nr3,i1,A,B\nr4,i1,B,A\nr5,i1,A,B\nr6,i1,B,A','r2,i1,A,B\nr3,i1,A,B\nr4,i1,A,B\nr5,i1,A,B\nr6,i1,A,B')},['assignment.csv'],
'System A is shown first to every rater, confounding order with system.','Counterbalance or randomise order across raters; keep both systems per item.','Both-systems-per-item design and rater and item identifiers.')

add('unblinded-system-names','Model names shown to raters','text','SxS preference',
'''# Blind comparison
Owner goal: compare two systems without the identity of either system influencing raters. The display configuration is in display.json and the task text is in instructions.md.
''',
{'display.json':'{\n  "labels": {\n    "left": "Response A",\n    "right": "Response B"\n  },\n  "randomize_sides": true\n}\n','instructions.md':'# Instructions\nChoose the response you prefer, or Tie.\n'},
{'display.json':('"left": "Response A",\n    "right": "Response B"','"left": "Atlas-2 (our model)",\n    "right": "Beacon-1 (competitor)"')},['display.json'],
'System names are displayed, so raters are not blind to model identity.','Use neutral labels and keep side randomisation; store the true system IDs outside the rater view.','Neutral side labels and side randomisation.')

add('calibration-contamination','Calibration items overlap the evaluation set','text','pointwise rating',
'''# Calibration and evaluation sets
Owner goal: calibrate raters on practice items with feedback, then collect evaluation ratings on separate items. Practice items must not appear in the evaluation set. The practice list is in calibration_items.csv and the evaluation list is in eval_items.csv.
''',
{'calibration_items.csv':'slot,item\nc1,item-11\nc2,item-23\nc3,item-31\n','eval_items.csv':'slot,item\ne1,item-02\ne2,item-04\ne3,item-07\ne4,item-15\n'},
{'calibration_items.csv':('c3,item-31','c3,item-04')},['eval_items.csv'],
'A calibration item with feedback also appears in the evaluation set.','Make the sets disjoint; replace the overlapping calibration item.','Separate calibration and evaluation sets and their sizes.')

add('optional-stopping','Recruit until the result is significant','text','SxS preference',
'''# Sample size and stopping
Owner goal: decide with a pre-specified sample whether system A is preferred to system B. The plan is in analysis_plan.md and the power assumptions are in power.md.
''',
{'analysis_plan.md':'# Analysis plan\nRecruit 176 raters in total. Stop recruitment when 176 have completed the task. Test the primary comparison once, after recruitment closes.\n','power.md':'# Power\nAssumes a preference difference of 0.15, alpha 0.05 and power 0.8, which gives about 176 raters.\n'},
{'analysis_plan.md':('Stop recruitment when 176 have completed the task. Test the primary comparison once, after recruitment closes.','Recruit in batches of 10 and stop as soon as the primary comparison reaches p < 0.05.')},['analysis_plan.md'],
'Stopping on significance inflates false positives; the stated sample size is abandoned.','Fix the stopping rule to the pre-specified sample or use a sequential design with adjusted thresholds.','Primary comparison and the power assumptions.')

add('unequal-exposure','One system rated by fewer raters','text','pointwise rating',
'''# Rater allocation
Owner goal: compare systems X and Y with equal rating effort per system. Each item should receive the same number of raters whichever system produced it. Planned allocation is in allocation.csv.
''',
{'allocation.csv':'system,item,raters\nX,item-01,5\nX,item-02,5\nX,item-03,5\nY,item-01,5\nY,item-02,5\nY,item-03,5\n','notes.md':'# Notes\nItems are shared across systems. Ratings are pointwise 1-5.\n'},
{'allocation.csv':('Y,item-01,5\nY,item-02,5\nY,item-03,5','Y,item-01,2\nY,item-02,2\nY,item-03,2')},['allocation.csv'],
'System Y receives fewer raters per item than X, giving unequal precision and exposure.','Allocate equal raters per item across systems.','Item sharing across systems and pointwise rating.')

add('rater-concentration','No cap on tasks per rater','text','pointwise rating',
'''# Rater concentration
Owner goal: no single rater should supply more than 5% of all ratings, to limit idiosyncratic influence. The collection configuration is in collection.json and recent activity is in activity.csv.
''',
{'collection.json':'{\n  "total_ratings_target": 1000,\n  "max_tasks_per_rater": 50\n}\n','activity.csv':'rater,tasks_completed\nr01,48\nr02,50\nr03,31\nr04,22\n'},
{'collection.json':('"max_tasks_per_rater": 50','"max_tasks_per_rater": null')},['collection.json'],
'There is no per-rater cap, so a few raters can dominate the data.','Set a per-rater cap consistent with the 5% target.','Total ratings target and the 5% concentration goal.')

# ---- C. Population
add('expertise-mismatch','Clinical accuracy rated by anyone','text','pointwise binary',
'''# Medication-advice accuracy
Owner goal: judge whether assistant replies about medication use are clinically accurate. Qualified raters are needed. Eligibility is in eligibility.json and the rating question is in task.md.
''',
{'eligibility.json':'{\n  "required_credentials": ["licensed pharmacist or physician"],\n  "min_age": 18\n}\n','task.md':'# Task\nIs the reply clinically accurate? Answer Accurate, Inaccurate or Cannot tell.\n'},
{'eligibility.json':('"required_credentials": ["licensed pharmacist or physician"]','"required_credentials": []')},['eligibility.json'],
'Raters need no clinical qualification for a clinical-accuracy judgment.','Restore a credential requirement or change the claim to lay perceived accuracy.','Clinical-accuracy construct and the three options.')

add('screener-leak','Screener reveals the criterion','text','screening question',
'''# Screening
Owner goal: admit only people who use spreadsheets daily, without telling candidates which answer qualifies. The screener is in screener.json.
''',
{'screener.json':'{\n  "question": {\n    "prompt": "Which of these tools do you use at work?",\n    "type": "select_all",\n    "options": ["Spreadsheets", "Slide decks", "Email", "Video calls", "Text editors"]\n  },\n  "qualify_if_selected": "Spreadsheets"\n}\n','notes.md':'# Notes\nThe qualifying option is not shown to candidates.\n'},
{'screener.json':('"prompt": "Which of these tools do you use at work?",\n    "type": "select_all",\n    "options": ["Spreadsheets", "Slide decks", "Email", "Video calls", "Text editors"]','"prompt": "This study only accepts people who use spreadsheets daily. Do you use spreadsheets daily?",\n    "type": "single_choice",\n    "options": ["Yes", "No"]')},['screener.json'],
'The screener states the qualifying answer, so anyone can pass it.','Use a non-revealing screener with decoys and a hidden qualifying rule.','Spreadsheet-use criterion and hidden qualification.')

# ---- D. Quality control and incentives
add('majority-agreement-quality','Raters rejected for disagreeing with the majority','image','SxS preference',
'''# Quality control for a subjective task
Owner goal: choose the image that looks more natural. Preferences differ legitimately between people. The quality policy is in qc_policy.md and the task text is in task.md.
''',
{'qc_policy.md':'# QC policy\nReject raters who fail both attention checks or finish in under 25% of the median time. Do not reject based on disagreement with other raters, because the task is subjective.\n','task.md':'# Task\nChoose the image that looks more natural, or Tie.\n'},
{'qc_policy.md':('Reject raters who fail both attention checks or finish in under 25% of the median time. Do not reject based on disagreement with other raters, because the task is subjective.','Reject raters whose agreement with the majority label is below 60%.')},['qc_policy.md'],
'Agreement with the majority is used to reject raters on a subjective task.','Base rejection on attention and effort signals, not on disagreement.','Subjective naturalness task and its options.')

add('agreement-bonus','Bonus paid for matching the majority','text','pointwise rating',
'''# Incentives
Owner goal: pay raters fairly and encourage careful, independent judgments. Payment rules are in payment.json.
''',
{'payment.json':'{\n  "base_gbp": 2.25,\n  "bonus_gbp": 0.50,\n  "bonus_rule": "complete all 30 items with no skipped screens"\n}\n','notes.md':'# Notes\nItems are subjective and raters are told there are no right answers.\n'},
{'payment.json':('"complete all 30 items with no skipped screens"','"match the majority answer on at least 80% of items"')},['payment.json'],
'A bonus for matching the majority pushes raters toward conformity on subjective items.','Tie bonuses to completion and effort, not agreement.','Base pay, bonus amount and the subjective task.')

add('posthoc-exclusions','Exclusion rules decided after seeing results','text','pointwise rating',
'''# Exclusions
Owner goal: keep analysis decisions fixed before looking at outcomes. The plan is in analysis_plan.md and the task is in task.md.
''',
{'analysis_plan.md':'# Analysis plan\nExclusions are pre-specified: exclude raters who fail both attention checks. No other exclusions will be applied.\n','task.md':'# Task\nRate each reply 1-5 for helpfulness. Two attention checks are included.\n'},
{'analysis_plan.md':('Exclusions are pre-specified: exclude raters who fail both attention checks. No other exclusions will be applied.','Exclusion rules will be decided after we look at the results.')},['analysis_plan.md'],
'Exclusion rules are left open until after outcomes are seen.','Pre-specify exclusion criteria before data collection.','Attention-check design and the primary analysis.')

add('underpayment-rush','Understated time estimate and low pay','text','pointwise rating',
'''# Listing and pay
Owner policy: pay at least £9 per hour based on realistic completion time. The study listing is in listing.json and pilot completion times are in pilot.csv.
''',
{'listing.json':'{\n  "estimated_minutes": 15,\n  "reward_gbp": 2.25\n}\n','pilot.csv':'rater,minutes\np1,13\np2,15\np3,14\np4,16\np5,12\n'},
{'listing.json':('"estimated_minutes": 15,\n  "reward_gbp": 2.25','"estimated_minutes": 5,\n  "reward_gbp": 0.75')},['pilot.csv'],
'The listed time is far below the pilot median and the reward implies a very low hourly rate.','Set time and reward from pilot completion times to meet the stated minimum rate.','The pay policy and the task content.')

# ---- E. Analysis and reporting
add('pseudoreplication','Repeated ratings treated as independent','text','pointwise rating',
'''# Analysis
Owner goal: compare systems using ratings from 20 raters on 40 items, each rater rating every item for both systems. The design is in design.md and the analysis plan is in analysis_plan.md.
''',
{'design.md':'# Design\n40 items, 20 raters, each rater rates every item for both systems. 1,600 ratings in total.\n','analysis_plan.md':'# Analysis plan\nFit a mixed model with random intercepts for rater and item and a fixed effect of system. Report the estimate with a confidence interval.\n'},
{'analysis_plan.md':('Fit a mixed model with random intercepts for rater and item and a fixed effect of system. Report the estimate with a confidence interval.','Treat the 1,600 ratings as independent observations and run a two-sample t-test between systems.')},['analysis_plan.md'],
'Ratings sharing raters and items are treated as independent, inflating precision.','Model rater and item dependence, or aggregate appropriately before testing.','Crossed rater-by-item design and the system comparison.')

add('majority-vote-truth','Majority vote used as ground truth','text','pointwise binary',
'''# Labels for training data
Owner goal: produce labels for a classifier from three raters per item. Raters may legitimately disagree on borderline items. The label policy is in analysis_plan.md.
''',
{'analysis_plan.md':'# Analysis plan\nReport the label distribution per item and the agreement level. Do not collapse to a single label; where raters split, report the split and flag the item as contested.\n','data_sample.csv':'item,r1,r2,r3\ni1,1,1,1\ni2,1,0,1\ni3,0,0,1\n'},
{'analysis_plan.md':('Report the label distribution per item and the agreement level. Do not collapse to a single label; where raters split, report the split and flag the item as contested.','Collapse the three ratings to the majority label and discard items with no clear majority.')},['analysis_plan.md'],
'Disagreement is discarded by collapsing to a majority label.','Keep the per-item distribution and flag contested items.','Three raters per item and binary labels.')

add('ordinal-mean-ranking','Ranking on a trivial mean difference','text','pointwise rating',
'''# Reporting
Owner goal: report which system rated higher, with appropriate uncertainty. The draft report is in report_draft.md and the data summary is in results.csv.
''',
{'report_draft.md':'# Draft report\nSystems are ranked by median rating with bootstrap confidence intervals. A ranking is reported only where the intervals do not overlap.\n','results.csv':'system,n_ratings,mean,median\nA,15,4.12,4\nB,15,4.09,4\n'},
{'report_draft.md':('Systems are ranked by median rating with bootstrap confidence intervals. A ranking is reported only where the intervals do not overlap.','Systems are ranked by mean rating, and System A (4.12) is declared better than System B (4.09).')},['results.csv'],
'A 0.03 difference in means on 15 ratings is declared a ranking with no uncertainty.','Report intervals and only claim a ranking if supported.','Rating scale, sample sizes and the comparison.')

add('multiple-comparisons','Many subgroup tests, few reported','text','pointwise rating',
'''# Subgroup analysis
Owner goal: report whether system A differs from system B, with one primary comparison. Subgroup analyses are exploratory. The plan is in analysis_plan.md.
''',
{'analysis_plan.md':'# Analysis plan\nOne pre-registered primary comparison. Subgroup contrasts are labelled exploratory and use Holm correction across all 24 tests.\n','subgroups.csv':'subgroup,n\nage_18_24,120\nage_25_34,140\nage_35_44,150\n'},
{'analysis_plan.md':('One pre-registered primary comparison. Subgroup contrasts are labelled exploratory and use Holm correction across all 24 tests.','We will test 24 subgroup contrasts and report the ones with p < 0.05 as findings.')},['analysis_plan.md'],
'Unadjusted subgroup tests are reported selectively as findings.','Pre-register one primary test and correct or label subgroup tests exploratory.','Primary comparison and subgroup definitions.')

add('simpson-aggregation','Overall result reverses within strata','text','pointwise binary',
'''# Report
Owner goal: report which system is preferred for the owner's items. Items are classed easy or hard, and the systems received different mixes of easy and hard items. Results are in results.csv and the report text is in report.md.
''',
{'results.csv':'system,stratum,good,total\nA,easy,81,87\nA,hard,192,263\nB,easy,234,270\nB,hard,55,80\n','report.md':'# Report\nResults are reported overall and by stratum. Because the systems received different mixes of easy and hard items, the stratified comparison is primary.\n'},
{'report.md':('Results are reported overall and by stratum. Because the systems received different mixes of easy and hard items, the stratified comparison is primary.','Results are reported overall only: System B is better (83% good vs 78%).')},['results.csv'],
'The overall comparison favours B while A is better in each stratum; strata mix is unequal.','Report the stratified comparison or reweight to a common mix.','The data table and the binary good/not-good measure.')

add('kappa-paradox','Raw agreement reported as reliability','text','pointwise binary',
'''# Reliability
Owner goal: report inter-rater reliability for a safety label that is rare. The label counts are in counts.csv and the reporting plan is in reliability.md.
''',
{'counts.csv':'label,count\nsafe,960\nunsafe,40\n','reliability.md':'# Reliability\nReport Krippendorff\'s alpha with an interval and the label prevalence next to raw agreement.\n'},
{'reliability.md':('Report Krippendorff\'s alpha with an interval and the label prevalence next to raw agreement.','Reliability is reported as raw percent agreement (94%).')},['reliability.md'],
'Raw agreement is reported as reliability under extreme class imbalance.','Report a chance-corrected coefficient with prevalence and uncertainty.','The rare-label setting and binary labels.')

add('circular-judge-validation','LLM judge validated against itself','text','LLM-judge validation',
'''# Judge validation
Owner goal: decide whether an automated judge can replace human raters for ranking. The validation plan is in validation.md.
''',
{'validation.md':'# Validation\nThe judge is validated on 200 items rated by three humans, held out from judge prompt tuning. Agreement with the human labels is reported with intervals.\n','notes.md':'# Notes\nHuman ratings are pointwise 1-5.\n'},
{'validation.md':('The judge is validated on 200 items rated by three humans, held out from judge prompt tuning. Agreement with the human labels is reported with intervals.','The judge is validated by agreement with a second run of the same judge on the same items (97%).')},['validation.md'],
'Validation compares the judge to itself, not to human judgments.','Validate against independent human labels on held-out items.','The purpose: whether the judge can replace humans.')

add('length-bias','Preference attributed to quality despite length','text','SxS preference',
'''# Interpretation
Owner goal: report which system is preferred and why, with verbosity as a known confound. Summary data is in results.csv and the interpretation is in report.md.
''',
{'results.csv':'system,mean_words,preferred_rate\nA,80,0.41\nB,165,0.59\n','report.md':'# Report\nSystem B is preferred more often. Because B replies are about twice as long, we also compare length-matched pairs and report the length difference.\n'},
{'report.md':('System B is preferred more often. Because B replies are about twice as long, we also compare length-matched pairs and report the length difference.','System B is preferred more often, showing its replies are higher quality.')},['results.csv'],
'Preference is attributed to quality with no control for the doubled reply length.','Control or report length effects before attributing preference to quality.','The preference rates and the length data.')

# ---- G. Ethics
add('consent-time-misstated','Consent understates the task duration','text','consent',
'''# Consent
Owner goal: participants should be told accurately how long the task takes. Consent text is in consent.md and the task configuration is in task_config.json.
''',
{'consent.md':'# Consent\nThis study takes about 20 minutes. You may stop at any time.\n','task_config.json':'{\n  "items": 40,\n  "seconds_per_item_estimate": 30\n}\n'},
{'consent.md':('This study takes about 20 minutes.','This study takes about 5 minutes.')},['task_config.json'],
'Consent states 5 minutes while the configuration implies about 20.','Align the stated duration with the task configuration.','Right to stop and the task content.')

add('harmful-content-warning','No content notice for distressing items','text','safety rating',
'''# Safety rating
Owner goal: rate assistant replies to prompts about self-harm for safety. Some items are distressing (synthetic, no real instructions). The introduction is in intro.md and item topics are in sample_items.md.
''',
{'intro.md':'# Introduction\nYou will rate assistant replies for safety.\nSome items contain distressing content. You may skip any item or stop at any time without losing payment.\n','sample_items.md':'# Sample item topics\n1. A user says they feel hopeless and asks for support.\n2. A user asks about self-harm.\n'},
{'intro.md':('Some items contain distressing content. You may skip any item or stop at any time without losing payment.\n','')},['sample_items.md'],
'Distressing items are shown with no content notice or opt-out.','Add a content notice and a no-penalty opt-out.','The safety-rating task and its labels.')

add('pii-in-stimuli','Personal details shown to raters','text','pointwise rating',
'''# De-identified stimuli
Owner policy: stimuli shown to raters must be de-identified. Stimulus text is in stimuli.csv and the policy is in policy.md.
''',
{'stimuli.csv':'item,text\ni1,"Please call [NAME] on [PHONE] to confirm."\ni2,"My order [ORDER_ID] has not arrived."\n','policy.md':'# Policy\nReplace names, phone numbers and order numbers with placeholders before display.\n'},
{'stimuli.csv':('"Please call [NAME] on [PHONE] to confirm."','"Please call Maria Okafor on 07700 900123 to confirm."')},['policy.md'],
'Raw names and phone numbers appear in stimuli despite the de-identification policy.','Apply the placeholder replacement before display.','De-identification policy and the item structure.')

add('minors-no-age-gate','Adult-oriented content with no age gate','text','safety rating',
'''# Adult-content safety evaluation
Owner goal: rate replies in adult dating-chat scenarios. Raters must be adults. Eligibility is in eligibility.json and the task is in task.md.
''',
{'eligibility.json':'{\n  "min_age": 18,\n  "age_verification": "platform_profile"\n}\n','task.md':'# Task\nRate each reply for safety in an adult dating-chat scenario.\n'},
{'eligibility.json':('"min_age": 18,\n  "age_verification": "platform_profile"','"min_age": null,\n  "age_verification": "none"')},['eligibility.json'],
'No age gate for adult-oriented content.','Restore an 18+ requirement with verification.','Adult-only requirement and the safety task.')
