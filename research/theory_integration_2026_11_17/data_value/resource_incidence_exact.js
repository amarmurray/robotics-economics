"use strict";
function run(){
  let assertions=0,cases=0,laws=0;
  const ck=(x,m)=>{assertions++;if(!x)throw Error(m)};
  // units = quarters, three columns: retained old A, updated A, B.
  // A variants mutually exclusive; B must have lawful authorization.
  const C=[0,1,2,4,5,6];
  const evals=(m,w,A)=>{let v=0,u=[0,0,0];for(let j=0;j<3;j++)if(m>>j&1){v+=w[j];for(let k=0;k<3;k++)u[k]+=A[j][k]}return {v,u}};
  const dot=(a,b)=>a.reduce((s,v,k)=>s+v*b[k],0);
  const best=(D,w,A,b)=>Math.max(...D.map(m=>evals(m,w,A)).filter(z=>z.u.every((v,k)=>v<=b[k])).map(z=>z.v));
  const lag=(D,w,A,p)=>Math.max(...D.map(m=>{let z=evals(m,w,A);return z.v-dot(z.u,p)}));
  const old=[0,1,4,5];
  for(let L=0;L<2;L++)for(let Q=0;Q<2;Q++)for(let cap=1;cap<=2;cap++)for(let auth=0;auth<=1;auth++)for(let a=0;a<=20;a+=2)for(let v=0;v<=20;v+=2){
    const A=[[1,1,1],[+(L!==0),+(L!==1),1],[+(Q===0),+(Q===1),1]],w=[a,a,v],b=[1,1,cap];
    const D0=old.filter(m=>auth||!(m&4)),D1=C.filter(m=>auth||!(m&4));
    const V0=best(D0,w,A,b),V1=best(D1,w,A,b);
    ck(V0===Math.max(a,auth*v),"retained optimum");
    ck(V1===Math.max(V0,cap===2&&auth&&L===Q?a+v:0),"new optimum");
    const p=[Q===0?v:0,Q===1?v:0,0];
    const U0=dot(b,p)+lag(D0,w,A,p),U1=dot(b,p)+lag(D1,w,A,p);
    ck(U0>=V0&&U1>=V1&&V1>=V0,"dual and optionality");
    if(auth&&cap===2&&a>=v){ck(U0===V0&&U1===V1,"matched price exact")}
    for(let k=0;k<3;k++){const pp=[k,k+1,2*k];const m0=lag(D0,w,A,pp),m1=lag(D1,w,A,pp);ck(V1-V0<=dot(b,pp)+m0-V0+m1-m0,"domain-changing transport");}
    cases++;
  }
  // Common-menu incidence perturbations and capacity changes.
  const D=[0,1,4,5]; 
  for(let q=0;q<2;q++)for(let l=0;l<2;l++)for(let cap0=1;cap0<=2;cap0++)for(let cap1=1;cap1<=2;cap1++)for(let a=1;a<=5;a++)for(let v=1;v<=5;v++)for(let delta=-1;delta<=1;delta++){
    const A0=[[1,1,1],[0,0,0],[+(q===0),+(q===1),1]],A1=[[+(l!==0),+(l!==1),1],[0,0,0],A0[2]];
    const w0=[a,0,v],w1=[a+delta,0,v],b0=[1,1,cap0],b1=[1,1,cap1],V0=best(D,w0,A0,b0),V1=best(D,w1,A1,b1);
    const p=[q===0?v:0,q===1?v:0,1];
    const m0=lag(D,w0,A0,p),m1=lag(D,w1,A1,p),gap=dot(b0,p)+m0-V0;
    let tmax=-Infinity, exact=-Infinity;
    for(const m of D){const z0=evals(m,w0,A0),z1=evals(m,w1,A1),r0=z0.v-dot(z0.u,p),r1=z1.v-dot(z1.u,p),t=r1-r0;tmax=Math.max(tmax,t);exact=Math.max(exact,t-(m0-r0))}
    const db=dot(b1.map((v,k)=>v-b0[k]),p);
    ck(m1-m0===exact,"priced transport identity");
    ck(V1-V0<=gap+db+exact&&exact<=tmax,"nested bounds");
    cases++;
  }
  // All four-cell laws with denominator 24 and fixed half marginals.
  const N=24;
  for(let n00=0;n00<=N;n00++)for(let n01=0;n01<=N-n00;n01++)for(let n10=0;n10<=N-n00-n01;n10++){
    let n11=N-n00-n01-n10;const align=n00+n11;
    const net=Math.max(0,12*align-N);
    ck(net===Math.max(0,[n00,n01,n10,n11].reduce((s,n,i)=>s+n*(i===0||i===3?12:0),0)-N),"joint value");
    if(n00+n01===N/2&&n00+n10===N/2)ck((net>6*N)===(12*align>7*N),"E threshold");
    laws++;
  }
  const g=a=>Math.max(0,3*a-1/4);
  ck(g(0)===0&&g(.5)===1.25&&g(1)===2.75,"counterworlds");
  ck(g(.5)<1.5&&g(1)>1.5&&g(7/12)===1.5,"strict decision");
  return {synthetic:true,assertions,cases,laws,grounding:[g(0),g(.5),g(1)],strengthening:.5,independentEmbodiment:1.5,alignmentThreshold:"7/12",freeRoutineAlignedValue:3};
}
console.log(JSON.stringify(run(),null,2));
