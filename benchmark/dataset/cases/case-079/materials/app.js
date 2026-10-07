const ids=['A','B','C'];
const ratings=Object.fromEntries(ids.map(id=>[id,50]));
const cards=document.getElementById('cards');
for(const id of ids){
 const section=document.createElement('section');
 section.innerHTML=`<h2>Candidate ${id}</h2><audio controls src="assets/${id}.wav"></audio><label>Fidelity rating <select aria-label="Candidate ${id} fidelity"><option value="">Choose a rating</option><option value="0">0 — entirely different</option><option value="25">25 — major differences</option><option value="50">50 — moderate differences</option><option value="75">75 — small differences</option><option value="100">100 — no audible difference</option><option value="cannot_judge">Cannot judge</option></select></label>`;
 const select=section.querySelector('select');select.value=ratings[id]===null?'':String(ratings[id]);
 select.onchange=()=>ratings[id]=select.value===''?null:select.value==='cannot_judge'?'cannot_judge':Number(select.value);
 cards.append(section);
}
document.getElementById('save').onclick=()=>{
 if(Object.values(ratings).some(v=>v===null)){document.getElementById('message').textContent='Choose a rating or Cannot judge for every candidate.';return;}
 const record={item_id:'chirp-01',ratings};localStorage.setItem('sound-reconstruction',JSON.stringify(record));
 document.getElementById('output').textContent=JSON.stringify(record,null,2);document.getElementById('message').textContent='Saved on this device.';
};
