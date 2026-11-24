"use strict";
function run(){
 let assertions=0,laws=0,cells=0,sharpChecks=0;const ck=(b,m)=>{assertions++;if(!b)throw Error(m)};
 const reports=[j=>0,j=>j>>2,j=>j>>1,j=>+(j>=6)];
 function ev(n,report,external=null){
  let sum=0,safe=0,joint=0;
  for(const r of new Set(n.map((_,j)=>report(j)))){
   const inds=n.map((_,j)=>j).filter(j=>report(j)===r),mass=inds.reduce((a,j)=>a+n[j],0);if(!mass)continue;
   const S=inds.filter(j=>external?external[j]:n[j]>0);
   ck(inds.every(j=>!n[j]||S.includes(j)),"support");
   const load=(a,j)=>((a&1)?j>>2:0)+((a&2)?(j>>1)&1:0);
   const feas=[0,1,2,3].filter(a=>S.every(j=>load(a,j)<=1));
   const h=inds.reduce((a,j)=>a+(j&1)*n[j],0),v=a=>a===3?8*mass+2*h:a===0?0:4*mass;
   const opt=Math.max(...feas.map(v));sum+=opt;cells++;
   if(feas.includes(3)){safe+=mass;joint+=h}
   const bad=S.find(j=>j>=6),lambda=bad===undefined?0:4*mass+2*h;
   const penalty=a=>bad===undefined?0:lambda*Math.max(0,load(a,bad)-1);
   ck(Math.max(...[0,1,2,3].map(a=>v(a)-penalty(a)))===opt,"positive-part penalty exact");
   const signed=a=>bad===undefined?0:lambda*(load(a,bad)-1);
   ck(Math.max(...[0,1,2,3].map(a=>v(a)-signed(a)))>=opt,"signed dual upper not necessarily exact");
  }
  ck(sum===4*n.reduce((a,b)=>a+b,0)+4*safe+2*joint,"report closure");return {sum,safe,joint};
 }
 const groups=new Map(),N=8;
 function visit(n,left){
  if(n.length===7){
   n=[...n,left];laws++;
   const p=n[6]+n[7],h=n.reduce((a,b,j)=>a+(j&1)*b,0),q=h-n[7];
   const [none,one,full,flag]=reports.map(f=>ev(n,f));
   ck(full.sum===4*N+4*(N-p)+2*q,"full formula");
   ck(flag.sum===full.sum,"flag sufficient");
   ck(none.sum<=one.sum&&one.sum<=full.sum,"refinement");
   ck(none.sum===(p?4*N:full.sum),"hidden");
   ck(q>=Math.max(0,h-p)&&q<=Math.min(h,N-p),"interval");
   const key=[p,h].join(","),z=groups.get(key)||[Infinity,-Infinity];groups.set(key,[Math.min(z[0],q),Math.max(z[1],q)]);return;
  }
  for(let x=0;x<=left;x++)visit([...n,x],left-x);
 }
 visit([],N);
 for(const [k,[lo,hi]] of groups){const [p,h]=k.split(",").map(Number);ck(lo===Math.max(0,h-p)&&hi===Math.min(h,N-p),"sharp extrema");sharpChecks++}
 const cases={anti:[0,0,4,4,4,4,0,0],alignedBlocked:[8,0,0,0,0,0,0,8],alignedUseful:[0,8,0,0,0,0,8,0],sameLoadLow:[0,3,3,2,5,0,0,3],sameLoadHigh:[0,3,0,5,5,0,3,0]};
 const vals={};for(const [k,n] of Object.entries(cases)){
  const full=ev(n,reports[2]),none=ev(n,reports[0]),den=n.reduce((a,b)=>a+b,0);
  ck(den===16&&n.slice(4).reduce((a,b)=>a+b,0)===8&&n[2]+n[3]+n[6]+n[7]===8&&n.reduce((a,b,j)=>a+(j&1)*b,0)===8,"same marginals");
  vals[k]={p11:(n[6]+n[7])/den,q:full.joint/den,grounding:Math.max(0,full.sum/den-5),hiddenGrounding:Math.max(0,none.sum/den-5)};
 }
 ck(vals.anti.grounding===4&&vals.alignedBlocked.grounding===1&&vals.alignedUseful.grounding===2,"worlds");
 ck(vals.sameLoadLow.grounding===2.875&&vals.sameLoadHigh.grounding===3.25,"rank reversal");
 ck(vals.anti.hiddenGrounding===4&&vals.sameLoadHigh.hiddenGrounding===0,"support matters");
 ck(ev(cases.anti,reports[0],Array(8).fill(true)).sum===64,"union safety");
 return {synthetic:true,assertions,laws,reportCells:cells,sharpGroups:sharpChecks,cases:vals,sourceX:.5,independentE:3};
}
console.log(JSON.stringify(run(),null,2));
