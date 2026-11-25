"use strict";
function renewalStudy(){
 const S=[];for(const d of [-1,1])for(const e of [-1,1])for(const r of [-1,1])for(const n of [-1,1])S.push({d,e,r,n,L:r*d*e,N:n*e,O:d*e});
 const sum=a=>a.reduce((x,y)=>x+y,0), dot=(p,f)=>sum(p.map((w,i)=>w*f(S[i]))),eps=1e-9;
 const prior=(d,e,r,n)=>S.map(s=>(1+d*s.d)*(1+e*s.e)*(1+r*s.r)*(1+n*s.n)/16);
 function reports(p,f,q,u=()=>1){return [-1,0,1].map(y=>{let w=p.map((v,i)=>v*(y===0?1-u(S[i]):u(S[i])*(y===f(S[i])?q:1-q)));let m=sum(w);return {y,m,p:w.map(v=>m?v/m:0)}}).filter(x=>x.m>1e-12)}
 const acc=(p,k)=>(1+Math.abs(dot(p,s=>s[k])))/2,after=(p,k,f,q)=>sum(reports(p,f,q).map(o=>o.m*acc(o.p,k)));
 let checks=0;function eq(a,b){if(Math.abs(a-b)>1e-8)throw Error(`${a} != ${b}`);checks++}function ok(x){if(!x)throw Error("inequality");checks++}
 for(const d of [0,.2,.6,1])for(const r of [.1,.8,1])for(const n of [.2,.9,1])for(const q of [.5,.7,1]){
 const p=prior(d,0,r,n),l=2*q-1;
 eq(after(p,"L",s=>s.O,q),(1+r*l)/2);eq(after(p,"N",s=>s.O,q),(1+n*d*l)/2);
 eq(after(p,"L",s=>s.e,q),(1+r*d*l)/2);eq(after(p,"N",s=>s.e,q),(1+n*l)/2);
 }
 const base=()=>({v:0,L:0,N:0,A:0,B:0,C:0,old:0,new:0,portable:0,diag:0});
 const keys=Object.keys(base()),add=(a,b)=>Object.fromEntries(keys.map(k=>[k,a[k]+b[k]])),scale=(a,w)=>Object.fromEntries(keys.map(k=>[k,a[k]*w]));
 const best=xs=>xs.reduce((a,b)=>b.v>a.v+1e-10?b:a),mix=xs=>xs.reduce((a,o)=>add(a,scale(o.r,o.m)),base());
 function solve(p,mode="all"){
 let cache=new Map();
 function terminal(post,held){
 const key=JSON.stringify([held,post.map(x=>Math.round(x*1e10))]);if(cache.has(key))return cache.get(key);
 const jobs=[{L:p.vL},{N:p.vN},p.shared?{L:p.vS,N:p.vS}:{}];
 function end(b,nL,nN){
 let prob=dot(b,s=>1-(1-p.u0)*Math.pow(1-(s.d===1?p.uL:p.uL/2),nL)*Math.pow(1-(s.d===1?p.uN/2:p.uN),nN));
 return {...base(),v:p.beta*p.w*prob,C:prob};
 }
 function tests(b,H,P,mask,nL,nN){
 const rows=[end(b,nL,nN)];
 if(H>0&&P>0)for(let j=0;j<jobs.length;j++)if(!(mask&(1<<j)))for(const k of Object.keys(jobs[j]))for(const z of [-1,1]){
 const nextmask=mask|(1<<j);
 rows.push(mix(reports(b,s=>s[k],1).map(o=>{
 let skip=tests(o.p,H-1,P,nextmask,nL,nN);let r=skip;
 if(o.y===z){const accepted=tests(o.p,H-1,P-1,nextmask,nL+Number(k==="L"),nN+Number(k==="N"));accepted.v+=jobs[j][k];accepted[k]+=1;r=best([skip,accepted]);}
 return {m:o.m,r};
 })));
 }return best(rows);
 }
 const opts=[tests(post,p.H,p.P,0,0,0)];
 if(p.H>=2){
 const candidates=[{f:s=>s.L,q:p.extQ,c:p.ext},{f:s=>s.N,q:p.extQ,c:p.ext}];
 if(held==="old"||held==="both"||p.equiv)candidates.push({f:s=>s.O,q:p.q,c:p.bridge});
 if(held==="new"||held==="both"||p.equiv)candidates.push({f:s=>s.e,q:p.q,c:p.bridge});
 for(const a of candidates){let r=mix(reports(post,a.f,a.q).map(o=>({m:o.m,r:tests(o.p,p.H-1,p.P,0,0,0)})));r.v-=a.c;r.diag++;opts.push(r)}
 if(held==="portable"){let r=mix(reports(post,s=>s.d,p.portQ).map(o=>({m:o.m,r:mix(reports(o.p,s=>s.e,p.portQ).map(t=>({m:t.m,r:tests(t.p,p.H-1,p.P,0,0,0)})))})));r.v-=p.bridge;r.diag++;opts.push(r)}
 }
 const out=best(opts);cache.set(key,out);return out;
 }
 function source(b,site){const cap=s=>site==="A"?(s.d===1?p.uA:p.uA/2):(s.d===1?p.uB/2:p.uB);return reports(b,s=>site==="A"?s.r:s.n,site==="A"?p.qA:p.qB,cap)}
 const b=prior(p.d,p.e,p.r,p.n),rows=[];
 for(const site of ["A","B"]){
 let o=mix(source(b,site).map(x=>{
 const opts=[["none",0,0],["old",0,p.cOld],["portable",1,p.cPort]];
 if(site==="B")opts.push(["new",1,p.cNew],["both",1,p.cNew+p.cOld]);
 const allowed=opts.filter(([h])=>mode==="all"||mode==="legacy"&&!["new","both"].includes(h)||mode==="none"&&h==="none");
 const rr=allowed.filter(([,s])=>s<=p.H1-1).map(([held,slots,cost])=>{
 let histories=[{p:x.p,m:1}];const extra=p.H1-1-slots;
 for(let i=0;i<extra;i++)histories=histories.flatMap(h=>source(h.p,"A").map(t=>({p:t.p,m:h.m*t.m})));
 let cont=mix(histories.map(t=>({m:t.m,r:terminal(t.p,held)})));
 cont.v=p.beta*cont.v+extra*p.mA-cost;cont.A+=extra;
 if(held==="old"||held==="both")cont.old++;
 if(held==="new"||held==="both")cont.new++;
 if(held==="portable")cont.portable++;
 return cont;
 });return {m:x.m,r:best(rr)};
 }));
 o.v+=site==="A"?p.mA:p.mB;o[site]++;rows.push({...o,site});
 }return {...best(rows),bySite:rows};
 }
 const p={d:.2,e:0,r:.8,n:0,H1:2,H:3,P:2,shared:true,vL:4,vN:10,vS:6,mA:1,mB:1.2,uA:.4,uB:1,qA:.8,qB:1,q:1,extQ:1,ext:5,bridge:.1,cOld:.1,cNew:.1,cPort:3,portQ:.9,beta:.95,u0:.1,uL:.8,uN:.2,w:0,equiv:false};
 const cases=[];for(const vN of [3,10,20])for(const shared of [false,true])for(const H of [2,3])for(const P of [1,2])for(const w of [0,6]){
 const z={...p,vN,shared,H,P,w};let a=solve(z),b=solve(z,"legacy");ok(a.v>=b.v-eps);ok(a.L+a.N<=P+eps);ok(b.L+b.N<=P+eps);cases.push({params:{vN,shared,H,P,w},a,b});
 }
 const strong=cases.filter(x=>x.a.new>.01&&x.a.v>x.b.v+eps);
 const signed=strong.find(x=>x.a.N>x.b.N+eps&&x.a.L<x.b.L-eps);
 const fewer=strong.find(x=>x.a.N+x.a.L<x.b.N+x.b.L-eps);
 const more=strong.find(x=>x.a.N+x.a.L>x.b.N+x.b.L+eps);
 const overlap=strong.find(x=>x.params.shared&&x.a.N>x.b.N+eps&&x.a.L<x.b.L-eps);
 const flip=strong.find(x=>x.a.site!==x.b.site);
 const equal=solve({...p,equiv:true,cPort:99});const equal0=solve({...p,equiv:true,cPort:99},"none");eq(equal.v,equal0.v);
 // Check a shared report can change the joint outcome law without changing marginals.
 const joint=prior(.2,0,.8,.9);const cov=dot(joint,s=>s.L*s.N);eq(cov,.2*.8*.9);
 return {checks,cases:cases.length,params:p,renewalCases:strong.length,signed:signed??null,fewer:fewer??null,more:more??null,overlap:overlap??null,siteFlip:flip??null,first:strong[0]??null,equivalentOutside:{equal,equal0},scope:"Finite-history enumeration to floating tolerance; no empirical calibration"};
}
console.log(JSON.stringify(renewalStudy(),null,2));
