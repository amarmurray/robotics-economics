// Synthetic decision/identification checks. Run: node deployment_topology.js
function run(){
 let checks=0; const check=(b,m)=>{if(!b)throw Error(m);checks++}, close=(a,b)=>Math.abs(a-b)<1e-8, pos=x=>Math.max(0,x);
 function post(p,q1,q0){let z=p*q1+(1-p)*q0;return [[z,z?p*q1/z:0],[1-z,z<1?p*(1-q1)/(1-z):0]]}
 function menu(p,bridge,orders,K){let best=0; for(let mask=0;mask<2**orders.length;mask++){let v=0,k=0;for(let i=0;i<orders.length;i++)if(mask>>i&1){let {w,a,d}=orders[i];v+=w*(1+(bridge?Math.max(a*p,d):d))/2;k++}if(k<=K)best=Math.max(best,v)}return best}
 function solve(p,q1,q0,orders,K,b,c){let base=menu(p,false,orders,K),B=p=>menu(p,true,orders,K)-base, outcomes=post(p,q1,q0), before=B(p)-b, A=-c+outcomes.reduce((s,[z,t])=>s+z*pos(B(t)-b),0), BA=-b-c+outcomes.reduce((s,[z,t])=>s+z*B(t),0);return {base,before,A,BA,best:Math.max(0,before,A,BA),outcomes,postBridge:outcomes.map(([z,t])=>[z,B(t),B(t)>b])}}
 const orders=Array.from({length:4},()=>({w:10,a:1,d:.5}));
 let example=solve(.4,1,.5,orders,4,.8,.3), tight=solve(.4,1,.5,orders,2,.8,.3), noisy=solve(.4,.9,.5,orders,4,.8,.3), capture=solve(.4,1,.5,orders.map(o=>({...o,w:o.w*.75})),4,.8,.3);
 check(close(example.A,.14)&&close(example.BA,-.1)&&close(example.before,-.8),"strict staged bundle");
 check(tight.best===0&&noisy.best===0&&capture.best===0,"constraints/noise/capture");
 check(close(example.outcomes.reduce((s,[z,t])=>s+z*t,0),.4),"martingale");
 let cases=0;
 for(const p of [.1,.4,.6,.9])for(const q1 of [.6,.8,1])for(const q0 of [.2,.5,.6])for(const K of [0,1,2,3])for(const b of [0,.1,.8,2])for(const c of [0,.3,1]){
  const os=[{w:6,a:.9,d:.3},{w:11,a:.7,d:.6},{w:4,a:1,d:.1}];
  let sol=solve(p,q1,q0,os,K,b,c), ps=post(p,q1,q0),V0=menu(p,false,os,K);
  let exhaustive=-Infinity;
  // Ex ante bridge or no bridge; optional audit; independent contingent decisions in each signal state.
  for(const first of ["stop","bridge","audit","bridgeAudit"]){
   if(first==="stop"){exhaustive=Math.max(exhaustive,0);continue}
   if(first==="bridge"){exhaustive=Math.max(exhaustive,menu(p,true,os,K)-b-V0);continue}
   for(let mask=0;mask<4;mask++){
    let v=-c-(first==="bridgeAudit"?b:0);
    for(let j=0;j<2;j++){const [z,t]=ps[j],buy=first==="bridgeAudit"||!!(mask>>j&1);v+=z*(menu(t,buy,os,K)-V0-(first==="audit"&&buy?b:0))}
    exhaustive=Math.max(exhaustive,v)
   }
  }
  check(close(sol.best,exhaustive),"adaptive enumeration");
  check(sol.A+1e-8>=sol.BA,"postpone cost when identical dates");
  check(close(ps.reduce((s,[z,t])=>s+z*t,0),p),"posterior martingale");
  cases++;
 }
 // Direct enumeration of 3 latent vertex labels and per-edge persistent deviation and reading noise.
 const signs=[-1,1],pr=(x,r)=>(1+x*r)/2;
 function obs(m,n){const out=Array(8).fill(0);let repeat=0,held=0,den=0;
  for(let v=0;v<8;v++){let Z=[0,1,2].map(i=>v>>i&1?1:-1);
   for(let u=0;u<8;u++){let U=[0,1,2].map(i=>u>>i&1?1:-1),pu=U.reduce((s,x)=>s*pr(x,m),1)/8;
    let M=[Z[0]*Z[1]*U[0],Z[1]*Z[2]*U[1],Z[0]*Z[2]*U[2]];
    for(let e=0;e<8;e++){let E=[0,1,2].map(i=>e>>i&1?1:-1),pe=E.reduce((s,x)=>s*pr(x,n),pu),R=M.map((x,i)=>x*E[i]),idx=R.reduce((s,x,i)=>s+(x===1?1<<i:0),0);out[idx]+=pe;
      if(R[0]===1&&R[1]===1){held+=pe*M[2];den+=pe}
      for(const fresh of signs)repeat+=pe*pr(fresh,n)*R[0]*M[0]*fresh;
    }
   }
  }return {out,repeat,held:held/den}
 }
 let noiseCases=0;for(const m of [.2,.5,.8,1])for(const n of [.2,.5,.8,1]){let x=obs(m,n),t=m*n;check(close(x.out.reduce((a,b)=>a+b,0),1),"normalization");check(close(x.repeat,n*n),"repeat moment");check(close(x.held,m*t*t),"held-out true edge");let cycle=x.out.reduce((s,p,i)=>s+p*([0,1,2].reduce((r,j)=>r*(i>>j&1?1:-1),1)),0);check(close(cycle,t**3),"cycle moment");noiseCases++}
 const n1=obs(.5,.8),n2=obs(.8,.5);check(n1.out.every((p,i)=>close(p,n2.out[i])),"single-reading equivalence");check(!close(n1.held,n2.held)&&!close(n1.repeat,n2.repeat),"economic ambiguity");
 const half=solve(.4,1,.5,orders.slice(0,2),2,.4,0);
 check(close(half.A,.22)&&2*half.A>.3&&half.A<.3,"shared report financing");
 return {checks,cases,noiseCases,example,tight,noisy,capture,repeatWitness:{m1:.5,n1:.8,m2:.8,n2:.5,edgeLaw:n1.out,repeat:[n1.repeat,n2.repeat],heldout:[n1.held,n2.held]},coalition:{oneGross:half.A,twoGross:2*half.A,cost:.3},field_calibration:false,full_repository_ci:false}
}
console.log(JSON.stringify(run(),null,2));
