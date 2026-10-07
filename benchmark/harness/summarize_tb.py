import json,statistics,collections
from pathlib import Path
from config import WORK,DATASET
H=Path(__file__).resolve().parent;J=WORK/'tb-v1/judge'
DS=DATASET
mp=json.loads((J/'map-private.json').read_text());AX=['key_issue_handling','classification_calibration','evidence_accuracy','ambiguity_coverage','ambiguity_quality','scope_and_abstention']
cinfo={c:json.loads((DS/'cases'/c/'case.json').read_text()) for c in {m['case'] for m in mp.values()}}
refs={c:{i['id']:i for i in json.loads((J/'reference'/f'{c}.json').read_text())['reference']['items']} for c in cinfo}
rows=[]
for k,m in mp.items():
 js=[json.loads((J/'packets'/k/f'judgment-{r}.json').read_text())['judgment'] for r in('1','2') if (J/'packets'/k/f'judgment-{r}.json').exists()]
 if js:rows.append({**m,'js':js,'variant':cinfo[m['case']]['variant'],'family':cinfo[m['case']]['family_id']})
sc=lambda j,a:j['axis_scores'].get(a,{}).get('score')
mean=lambda v:round(statistics.mean([x for x in v if x is not None]),2) if [x for x in v if x is not None] else None
def cond(rs):
 js=[j for r in rs for j in r['js']];am=[x for j in js for x in j.get('ambiguities',[])];cov=[]
 for r in rs:
  core=[i for i,x in refs[r['case']].items() if x['type'] in('defect','ambiguity')]
  for j in r['js']:cov.append(len(set(j.get('reference_coverage',{}).get('covered',[]))&set(core))/max(1,len(core)))
 return {'n':len(rs),'cov':mean(cov),**{a[:9]:mean([sc(j,a) for j in js]) for a in AX},'decree':round(sum(bool(x.get('resolved_by_decree')) for x in am)/max(1,len(am)),2),'overclaims/run':round(sum(j.get('overclaims') or 0 for j in js)/max(1,len(js)),2),'wrong major+crit/run':round(sum(w.get('severity') in('major','critical') for j in js for w in j.get('wrong_or_unsupported_claims',[]))/max(1,len(js)),2),'revised_rate':round(sum(r.get('n_revised',0)>0 for r in rs)/max(1,len(rs)),2)}
print('Judge test-retest')
for a in AX:
 pr=[(sc(r['js'][0],a),sc(r['js'][1],a)) for r in rows if len(r['js'])==2 and None not in(sc(r['js'][0],a),sc(r['js'][1],a))]
 print(f"  {a:26} exact {sum(p==q for p,q in pr)/len(pr):.0%} n={len(pr)}")
print('\nBy arm and case variant (sonnet, P1)')
for v in['defect','control','partial']:
 for arm in['bare','v2']:
  rs=[r for r in rows if r['variant']==v and r['arm']==arm]
  if rs:print(v,arm,cond(rs))
print('\nPlanted-defect families: key_issue_handling (mean of 2 runs; <2 means missed or mischaracterised)')
miss=[]
for f in sorted({r['family'] for r in rows if r['variant']=='defect'}):
 b=[r for r in rows if r['family']==f and r['variant']=='defect' and r['arm']=='bare'];s=[r for r in rows if r['family']==f and r['variant']=='defect' and r['arm']=='v2']
 kb=mean([sc(j,'key_issue_handling') for r in b for j in r['js']]);ks=mean([sc(j,'key_issue_handling') for r in s for j in r['js']])
 print(f'  {f:28} bare {kb}  v2 {ks}')
 if (kb is not None and kb<2) or (ks is not None and ks<2):miss.append(f)
print('\nFamilies where either arm scored below 2 on the planted defect:',miss)
json.dump({'by_variant_arm':{f'{v}-{a}':cond([r for r in rows if r['variant']==v and r['arm']==a]) for v in['defect','control','partial'] for a in['bare','v2'] if [r for r in rows if r['variant']==v and r['arm']==a]},'missed_families':miss},open(J/'summary.json','w'),indent=1)
