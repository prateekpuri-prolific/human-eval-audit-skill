import json,statistics,collections
from pathlib import Path
from config import WORK,DATASET
H=Path(__file__).resolve().parent;J=WORK/'img-v1/judge'
mp=json.loads((J/'map-private.json').read_text());AX=['key_issue_handling','classification_calibration','evidence_accuracy','ambiguity_coverage','ambiguity_quality','scope_and_abstention']
refs={c:{i['id']:i for i in json.loads((J/'reference'/f'{c}.json').read_text())['reference']['items']} for c in {m['case'] for m in mp.values()}}
rows=[]
for k,m in mp.items():
 js=[]
 for r in('1','2'):
  p=J/'packets'/k/f'judgment-{r}.json'
  if p.exists():js.append(json.loads(p.read_text())['judgment'])
 rows.append({**m,'js':js,'tok':k})
sc=lambda j,a:j['axis_scores'].get(a,{}).get('score')
def mean(v):v=[x for x in v if x is not None];return round(statistics.mean(v),2) if v else None
print('Judge test-retest')
for a in AX:
 pr=[(sc(r['js'][0],a),sc(r['js'][1],a)) for r in rows if len(r['js'])==2 and sc(r['js'][0],a) is not None and sc(r['js'][1],a) is not None]
 print(f"  {a:26} exact {sum(p==q for p,q in pr)/len(pr):.0%} mad {statistics.mean(abs(p-q) for p,q in pr):.2f} n={len(pr)}")
def cond(rs):
 js=[j for r in rs for j in r['js']];n=max(1,len(js))
 am=[x for j in js for x in j.get('ambiguities',[])]
 cov=[]
 for r in rs:
  core=[i for i,x in refs[r['case']].items() if x['type'] in('defect','ambiguity')]
  for j in r['js']:cov.append(len(set(j.get('reference_coverage',{}).get('covered',[]))&set(core))/len(core))
 ws=collections.Counter(w.get('severity') for j in js for w in j.get('wrong_or_unsupported_claims',[]))
 return {'n':len(rs),'valid':sum(r['valid'] for r in rs),'cov':mean(cov),**{a[:9]:mean([sc(j,a) for j in js]) for a in AX},
  'amb/run':round(len(am)/n,1),'decree':round(sum(bool(x.get('resolved_by_decree')) for x in am)/max(1,len(am)),2),'opts>=2':round(sum((x.get('options_offered') or 0)>=2 for x in am)/max(1,len(am)),2),'explain':round(sum(bool(x.get('explains_reading_differences')) for x in am)/max(1,len(am)),2),'default':round(sum(bool(x.get('recommended_default')) for x in am)/max(1,len(am)),2),'question':round(sum(bool(x.get('question_to_owner')) for x in am)/max(1,len(am)),2),
  'overclaims/run':round(sum(j.get('overclaims') or 0 for j in js)/n,2),'wrong major+crit/run':round((ws['major']+ws['critical'])/n,2),'critical':ws['critical'],
  'revised_rate':round(sum(r.get('n_revised',0)>0 for r in rs)/len(rs),2),'questions/run':round(statistics.mean(r.get('n_questions',0) for r in rs),1),'patches/run':round(statistics.mean(r.get('n_patches',0) for r in rs),1)}
out={}
for pk in['P1']:
 print(f'\n=== Prompt {pk} ===')
 for m in['haiku','sonnet','opus']:
  for arm in['bare','v2','v21']:
   rs=[r for r in rows if r['prompt']==pk and r['model']==m and r['arm']==arm and r['js']]
   if rs:c=cond(rs);out[f'{pk}-{m}-{arm}']=c;print(f"{m:7}{arm:5}",c)
json.dump(out,open(J/'summary.json','w'),indent=1)
print('\nPooled across models, per prompt and arm')
for pk in['P1']:
 for arm in['bare','v2','v21']:
  rs=[r for r in rows if r['prompt']==pk and r['arm']==arm and r['js']]
  if rs:print(pk,arm,cond(rs))
