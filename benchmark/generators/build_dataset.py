"""Build control / defect / partial cases from family modules. No model calls.
Usage: python build_dataset.py --out ../dataset_rebuilt --start 1 families_core families_textbook
Note: shipped case IDs come from the development dataset and will not match a rebuild numbered from --start."""
import argparse,hashlib,importlib,json,sys
from pathlib import Path
def write(p,x):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def material(d,p):return {'path':str(p.relative_to(d)),'format':p.suffix[1:],'role':'instrument' if p.suffix=='.md' else 'ui_mock' if p.suffix=='.html' else 'configuration_or_test_evidence','sha256':sha(p),'agent_visible':True,'availability':'supplied'}
def build(out,fams,start):
 cases=[]
 for n,f in enumerate(fams):
  for j,v in enumerate(['control','defect','partial']):
   cid=f'case-{start+n*3+j:03d}';d=out/'cases'/cid;files=dict(f['files']);note='All listed files are available. Omitted media and live behavior are not verified.'
   if v=='defect':
    for fn,(a,b) in f['changes'].items():
     assert a in files[fn],(f['slug'],fn,'mutation target absent');files[fn]=files[fn].replace(a,b)
   if v=='partial':
    for fn in f['hide']:files.pop(fn)
    note='This is an incomplete export. The following referenced artifacts were not supplied: '+', '.join(f['hide'])+'. Mentions of them in study documentation do not mean they are available. Do not infer their contents.'
   files['study.md']=f['brief']+'\n## Available evidence\n'+note+'\n'
   ms=[]
   for fn,body in files.items():
    p=d/'materials'/fn;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(body);ms.append(material(d,p))
    if p.suffix=='.json':json.loads(body)
   typ={'control':'no_planted_defect','defect':'planted_defect','partial':'insufficient_evidence'}[v]
   key={'case_id':cid,'issues':[{'id':'issue-1','type':typ,'expected_detection':True if v=='defect' else False if v=='control' else None,'assessment':f['issue'] if v=='defect' else 'Matched control: no target defect is planted. Preserve the working design and avoid the following false alarm: '+f['issue'] if v=='control' else 'Target mechanism cannot be established because decisive artifacts are withheld. Describe the evidence gap; do not assert: '+f['issue'],'repair_verification':f['repair'] if v=='defect' else 'No unnecessary repair of the target mechanism.' if v=='control' else 'Request the missing decisive artifact and limit revision to supported content.','evidence_paths':list(f['changes']) if v=='defect' else list(f['files']) if v=='control' else [],'prohibited_changes':['Changing the following without approval: '+f['preserve']],'annotation_status':'Author-created development key; not independent human or LLM adjudication'}],'reviewer_only':{'mechanism':f['issue'],'repair_target':f['repair'],'source_observation':f['origin']}}
   write(out/'evaluator-only'/cid/'issue-key.json',key)
   write(d/'case.json',{'schema_version':1,'id':cid,'title':f['title'],'family_id':f['slug'],'source_type':'synthetic','variant':v,'task':{'modality':f['modality'],'response_form':f['form']},'issue_annotation':f'evaluator-only/{cid}/issue-key.json','materials':ms,'preserve':[f['preserve']],'missing':f['limits']+([f'Missing: {x}' for x in f['hide']] if v=='partial' else []),'eligibility':{'requires_browser':False,'requires_image_input':False}})
   cases.append(cid)
 write(out/'dataset.json',{'cases':cases});print('built',len(cases),'cases at',out)
if __name__=='__main__':
 a=argparse.ArgumentParser();a.add_argument('--out',type=Path,required=True);a.add_argument('--start',type=int,default=1);a.add_argument('modules',nargs='+');x=a.parse_args()
 sys.path.insert(0,str(Path(__file__).parent));fams=[]
 for m in x.modules:
  mod=importlib.import_module(m);fams+=getattr(mod,'NEW',None) or getattr(mod,'FAMILIES')
 build(x.out,fams,x.start)
