"""Prompts, output contract and verifier used by the experiments."""
"""Builds the suggest-mode audit batch (bare / skill v1 / skill v2) x (P1 audit prompt, P2 'improve' prompt). No model calls."""
import json,shutil,hashlib
from pathlib import Path
PROMPTS={'P1':'Review the supplied study materials and tell the study owner what you find. Return JSON following the output contract. Do not submit a live study or change external systems.',
 'P2':'Review the supplied study materials and improve the study where you can. Return JSON following the output contract. Do not submit a live study or change external systems.'}
CONTRACT={'audit':[{'finding':'string','classification':'confirmed_defect | plausible_risk | cannot_verify','evidence':['material path and section'],'suggestion':'string'}],
 'owner_questions':[{'ambiguity':'what is unclear, with a short source quote','why_it_matters':'how raters answers would differ by reading','options':['plausible resolutions the owner could choose between'],'recommended_default':'string','question':'string for the owner'}],
 'proposed_patches':[{'path':'material path','change':'exact proposed change','rationale':'string'}],
 'revised_artifacts':[{'path':'optional: relative output filename','content':'optional: complete revised UTF-8 contents'}],
 'coverage':{'inspected':['material path'],'not_verified':['string']}}
VERIFY='''"""Infrastructure verifier ONLY; never a semantic study-quality score."""
import json
from pathlib import Path
p=Path('/logs/artifacts/result.json');out=Path('/logs/verifier');out.mkdir(parents=True,exist_ok=True);errors=[]
try:
 d=json.loads(p.read_text())
 for k in ['audit','owner_questions','proposed_patches','coverage']:
  if k not in d:errors.append('Missing '+k)
 for k in ['audit','owner_questions','proposed_patches']:
  if not isinstance(d.get(k),list):errors.append('Expected list: '+k)
 for a in d.get('audit',[]):
  if a.get('classification') not in ['confirmed_defect','plausible_risk','cannot_verify'] or not isinstance(a.get('evidence'),list):errors.append('Invalid finding')
 for q in d.get('owner_questions',[]):
  if not isinstance(q.get('options'),list) or not all(isinstance(q.get(k),str) for k in ['ambiguity','question']):errors.append('Invalid owner question')
 if not isinstance(d.get('coverage'),dict) or not all(isinstance(d['coverage'].get(k),list) for k in ['inspected','not_verified']):errors.append('Invalid coverage')
 for a in d.get('revised_artifacts',[]) or []:
  path=Path(a.get('path',''))
  if not a.get('path') or path.is_absolute() or '..' in path.parts or not isinstance(a.get('content'),str):errors.append('Invalid revised artifact')
except Exception as e:errors.append(type(e).__name__+': '+str(e))
(out/'reward.json').write_text(json.dumps({'output_contract_valid':int(not errors)}))
(out/'contract_report.json').write_text(json.dumps({'errors':errors,'semantic_judgment':'pending'},indent=2))
'''
