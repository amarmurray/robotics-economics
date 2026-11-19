(function(){
"use strict";let assertions=0,cases=0;const eps=1e-10;
function ok(x,m){assertions++;if(!x)throw Error(m);}
function val(p1,p2,r,g1,g2){
 if(g1<g2||r<Math.max(0,p1+p2-1)-eps||r>Math.min(p1,p2)+eps)throw Error("invalid law");
 const U=Math.max(g1*p1,g2*p2),F1=g1*p1+g2*(p2-r),F2=g1*p1+g2*p2;
 return {U,F1,F2,I:F1-U,C:F2-F1,remaining:F2-U};
}
for(let n=2;n<=18;n++)for(let a=0;a<=n;a++)for(let b=0;b<=n;b++)
 for(let t=Math.max(0,a+b-n);t<=Math.min(a,b);t++){
 const p1=a/n,p2=b/n,r=t/n;
 for(const [g1,g2] of [[1,1],[3,1],[8,8],[8,5]]){
  const z=val(p1,p2,r,g1,g2);
  ok(Math.abs(z.I+z.C-z.remaining)<eps,"identity");
  ok(z.I>-eps&&z.C>-eps,"option monotonicity");
  ok(Math.abs(z.C-g2*r)<eps,"intersection");
  ok(Math.abs(z.remaining-Math.min(g1*p1,g2*p2))<eps,"second opportunity");
  ok(r>=-eps&&p1-r>=-eps&&p2-r>=-eps&&1-p1-p2+r>=-eps,"atoms");
 }
 cases++;
}
const worlds={exclusive:{atoms:[[0,0,0],[0,1,.5],[1,0,.5],[1,1,0]],r:0},
 synchronized:{atoms:[[0,0,.5],[0,1,0],[1,0,0],[1,1,.5]],r:.5}};
for(const w of Object.values(worlds)){
 const p1=w.atoms.reduce((s,a)=>s+a[0]*a[2],0),p2=w.atoms.reduce((s,a)=>s+a[1]*a[2],0);
 const r=w.atoms.reduce((s,a)=>s+a[0]*a[1]*a[2],0);
 const z=val(p1,p2,r,8,8);
 ok(p1===.5&&p2===.5&&r===w.r,"identical one-order evidence");
 w.values={...z,retained:z.U,auditNet:z.F1-1,bodyNet:z.F2-2,selectedSuccess:(p1+p2)/2};
}
ok(worlds.exclusive.values.auditNet===7&&worlds.exclusive.values.bodyNet===6,"exclusive");
ok(worlds.synchronized.values.auditNet===3&&worlds.synchronized.values.bodyNet===6,"synchronized");
ok(worlds.exclusive.values.selectedSuccess===worlds.synchronized.values.selectedSuccess,"selection equivalence");
const out={schema:"synthetic order qualification information and capacity v1",cases,assertions,worlds,
sharpBounds:{r:[0,.5],auditMinusBody:[-3,1]},limits:"fixed-law approved report/body assumption; not real robot economics; finite tests not mathematical proof"};
if(typeof process!=="undefined"&&typeof require!=="undefined"&&require.main===module)console.log(JSON.stringify(out,null,2));
return out;
})()
