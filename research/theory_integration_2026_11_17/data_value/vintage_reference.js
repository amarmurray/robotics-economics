"use strict";
function vintageStudy(){
 const S=[];for(const x of [-1,1])for(const a of [-1,1])for(const e of [-1,1])S.push({x,a,e,t:x*e,b:a*e});
 const sum=a=>a.reduce((s,x)=>s+x,0), dot=(p,f)=>sum(p.map((v,i)=>v*f(S[i]))), EPS=1e-9;
 const initial=c=>S.map(({x,a,e})=>e===a?(1+c*x*a)/4:0);
 function drift(p,d){return p.map((v,i)=>(1-d)*v+d*p[i^1]);}
 function signal(p,f,q){return [-1,1].map(y=>{const w=p.map((v,i)=>v*(f(S[i])===y?q:1-q)),m=sum(w);return {y,m,p:m?w.map(v=>v/m):p}}).filter(o=>o.m>1e-13)}
 const acc=p=>(1+Math.abs(dot(p,s=>s.t)))/2;
 const after=(p,f,q)=>sum(signal(p,f,q).map(o=>o.m*acc(o.p)));
 let checks=0;function check(a,b,t=1e-8){if(Math.abs(a-b)>t)throw Error(`${a} != ${b}`);checks++}
 for(const c of [-1,-.7,0,.3,1])for(const d of [0,.1,.25,.5])for(const q of [.5,.65,.9,1]){
  const p=drift(initial(c),d),rho=1-2*d;
  check(acc(p),(1+Math.abs(c*rho))/2);
  check(after(p,s=>s.b,q),(1+Math.abs(c)*Math.max(rho,2*q-1))/2);
  check(after(p,s=>s.x,1),acc(p));check(after(p,s=>s.e,1),acc(p));
 }
 for(let k=0;k<100;k++){
  const p=S.map((s,i)=>1+((i+1)*(k+7)*13%37));const n=sum(p);for(let i=0;i<p.length;i++)p[i]/=n;
  const mt=dot(p,s=>s.t),mx=dot(p,s=>s.x),me=dot(p,s=>s.e);
  check(after(p,s=>s.e,1),(1+Math.max(Math.abs(mt),Math.abs(mx)))/2);
  check(after(p,s=>s.x,1),(1+Math.max(Math.abs(mt),Math.abs(me)))/2);
 }
 function solve(par,available=true,forceFirst=null){
  const cache=new Map();
  const base=()=>({v:0,B:0,A:0,newB:0,kept:0,bridge:0,external:0,source:0,test:0,redesign:0});
  const keys=Object.keys(base());
  const plus=(x,y)=>Object.fromEntries(keys.map(k=>[k,x[k]+y[k]]));
  const scale=(x,w)=>Object.fromEntries(keys.map(k=>[k,x[k]*w]));
  // Discount only monetary contribution; counts are undiscounted.
  const discount=x=>({...x,v:x.v*par.beta});
  const best=rows=>rows.reduce((a,b)=>b.v>a.v+1e-10?b:a);
  const mix=rows=>rows.reduce((a,{m,r})=>plus(a,scale(r,m)),base());
  function dp(t,p,held){
   if(t===par.H.length)return base();
   const key=JSON.stringify([t,held,p.map(v=>Math.round(v*1e12))]);
   if(t>0&&cache.has(key))return cache.get(key);
   const alternatives=[];
   for(const keep of held?[false,true]:[false]){
    if(t===0&&forceFirst!==null&&keep!==forceFirst)continue;
    for(const r of [0,1]){
     const pp=drift(p,par.d[r]),H=par.H[t],P=par.P[t];
     // Complete dated production; ordinary data from actual serviced cohort.
     function finish(b,used,post){
      if(b>P)throw Error("production overrun");
      const a=P-b;
      const cur={...base(),v:a*par.a+b*par.b[r],A:a,B:b,newB:b*r,test:used};
      // Source-specific observations, conditionally independent across actual serviced units.
      let histories=[{m:1,p:post}];
      for(const [count,u,q] of [[a,par.uA,par.qA],[b,par.uB,par.qB]]){
       for(let i=0;i<count;i++){
        const next=[];
        for(const h of histories){
         if(u<1)next.push({m:h.m*(1-u),p:h.p});
         if(u>0)for(const o of signal(h.p,s=>s.x,q))next.push({m:h.m*u*o.m,p:o.p});
        }histories=next;
       }
      }
      return plus(cur,discount(mix(histories.map(o=>({m:o.m,r:dp(t+1,o.p,keep)})))));
     }
     function operate(post,remaining){
      const options=[finish(0,0,post)];
      if(remaining>=1&&P>=1)for(const z of [-1,1]){
       options.push(mix(signal(post,s=>s.t,1).map(o=>({m:o.m,r:o.y===z?best([finish(0,1,o.p),finish(1,1,o.p)]):finish(0,1,o.p)}))));
      }
      return best(options);
     }
     const routes=[{name:"none",cost:0,slots:0}];
     if(H>=1){
      routes.push({name:"source",cost:par.sourceCost,slots:1,f:s=>s.x,q:par.sourceQ},{name:"absolute",cost:par.absCost,slots:1,f:s=>s.e,q:par.absQ},{name:"external",cost:par.extCost,slots:1,f:s=>s.t,q:par.extQ});
      if(keep)routes.push({name:"bridge",cost:par.bridgeCost,slots:1,f:s=>s.b,q:par.bridgeQ});
     }
     const rr=routes.map(route=>{
      const cont=route.f?mix(signal(pp,route.f,route.q).map(o=>({m:o.m,r:operate(o.p,H-route.slots)}))):operate(pp,H);
      const v={...cont,v:cont.v-route.cost-par.setup[r]-(keep?par.carry[t]:0),kept:cont.kept+Number(keep),redesign:cont.redesign+r};
      if(["bridge","external","source"].includes(route.name))v[route.name]+=1;
      return {...v,first:{keep,redesign:r,route:route.name}};
     });
     alternatives.push(best(rr));
    }
   }
   const out=best(alternatives);if(t>0)cache.set(key,out);return out;
  }
  return dp(0,initial(par.c),available);
 }
 const par={c:.9,H:[1,2],P:[1,1],beta:.95,d:[.05,.5],a:3,b:[4,9],setup:[0,.7],carry:[.3,.3],sourceCost:.4,absCost:.4,extCost:3,bridgeCost:.1,sourceQ:.9,absQ:1,extQ:1,bridgeQ:1,uA:.4,qA:.8,uB:.2,qB:.7};
 const witness={optional:solve(par),retire:solve(par,true,false),forcedKeep:solve(par,true,true),noRef:solve(par,false)};
 check(witness.retire.v,witness.noRef.v);
 if(witness.optional.v+EPS<witness.noRef.v)throw Error("option monotonicity");checks++;
 // At date 0 a bridge and test cannot jointly fit; retaining for later may pay.
 const cases=[];
 for(const H of [[1,2],[2,2],[1,1]])for(const carry of [.05,.3,1])for(const drift of [.15,.5])for(const ext of [.1,3]){
  const p={...par,H,carry:[carry,carry],d:[.05,drift],extCost:ext};
  const a=solve(p),b=solve(p,false);
  if(a.v+EPS<b.v)throw Error("optional retention");
  checks++;check(a.v,Math.max(solve(p,true,true).v,solve(p,true,false).v));
  cases.push({H,carry,drift,ext,with:a,without:b});
 }
 const delayed=cases.filter(x=>x.H[0]===1&&x.with.first.keep&&x.with.first.route==="none"&&x.with.v>x.without.v+EPS);
 const reversal=cases.filter(x=>x.with.first.redesign!==x.without.first.redesign);
 const cheap=cases.filter(x=>x.ext===.1&&x.with.first.keep===false);
 return {checks,scope:"Synthetic finite two-transition model; arithmetic checks, no field calibration or independent novelty",par,witness,delayedExample:delayed[0]??null,designReversal:reversal[0]??null,cheapExample:cheap[0]??null,caseCount:cases.length};
}
console.log(JSON.stringify(vintageStudy(),null,2));
