"""Run Harbor trial jobs for an experiment. Usage: run_trials.py img|rev|tb [job-name ...]. Keys come from the environment."""
import os,sys,subprocess,concurrent.futures
from pathlib import Path
import shutil
from config import WORK
H=Path(__file__).resolve().parent;B=WORK
F={'img':B/'img-v1','rev':B/'rev-v1','tb':B/'tb-v1'}[sys.argv[1]]
e=os.environ.copy()
if not e.get('ANTHROPIC_API_KEY'):raise SystemExit('Set ANTHROPIC_API_KEY in the environment.')
e['HARBOR_TELEMETRY']='0'
names=sorted(p.stem for p in F.glob(sys.argv[1]+'-*.json')) if len(sys.argv)<3 else sys.argv[2:]
def run(n):
 if (F/'jobs'/n).exists():return n,'exists'
 with open(F/(n+'.log'),'w') as f:r=subprocess.run([(shutil.which('harbor') or 'harbor'),'run','-c',str(F/(n+'.json'))],env=e,stdout=f,stderr=subprocess.STDOUT)
 return n,r.returncode
with concurrent.futures.ThreadPoolExecutor(2) as ex:
 for n,rc in ex.map(run,names):print(n,'exit',rc,flush=True)
