const historyToShow=ITEM.history;
for(const turn of historyToShow){const p=document.createElement('p');p.textContent=turn.role+': '+turn.text;document.getElementById('history').append(p);}
for(const [label,text] of Object.entries(ITEM.candidates)){const s=document.createElement('section');const h=document.createElement('h2');h.textContent=label;const p=document.createElement('p');p.textContent=text;s.append(h,p);document.getElementById('answers').append(s);}
document.getElementById('save').onclick=()=>{const choice=document.getElementById('choice').value;if(!choice)return;const record={item_id:ITEM.item_id,choice};localStorage.setItem('conversation-review',JSON.stringify(record));document.getElementById('output').textContent=JSON.stringify(record,null,2);};
