const canvas=document.getElementById('edit'),ctx=canvas.getContext('2d'),image=new Image();
const boxes=[];let start=null;image.src='assets/edit.svg';image.onload=()=>ctx.drawImage(image,0,0);
function point(e){const r=canvas.getBoundingClientRect();return {x:(e.clientX-r.left)*canvas.width/r.width,y:(e.clientY-r.top)*canvas.height/r.height};}
function normalizeBox(a,b){return {x:Math.min(a.x,b.x)/canvas.width,y:Math.min(a.y,b.y)/canvas.height,width:Math.abs(a.x-b.x)/canvas.width,height:Math.abs(a.y-b.y)/canvas.height};}
canvas.onpointerdown=e=>{start=point(e);canvas.setPointerCapture(e.pointerId);};
canvas.onpointerup=e=>{if(!start)return;const end=point(e);boxes.push(normalizeBox(start,end));ctx.strokeStyle='black';ctx.strokeRect(start.x,start.y,end.x-start.x,end.y-start.y);start=null;};
document.getElementById('clear').onclick=()=>{boxes.length=0;ctx.drawImage(image,0,0);};
document.getElementById('save').onclick=()=>{
 const decision=document.getElementById('decision').value,description=document.getElementById('description').value.trim();
 if(!decision||(decision==='Yes'&&(!boxes.length||!description))||(decision!=='Yes'&&boxes.length)){document.getElementById('message').textContent='Choose an answer; Yes needs a region and description. Clear regions for other answers.';return;}
 const record={item_id:'edit-01',decision,regions:boxes,description};localStorage.setItem('edit-review',JSON.stringify(record));document.getElementById('output').textContent=JSON.stringify(record,null,2);
};
