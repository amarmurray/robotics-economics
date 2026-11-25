"use strict";
function study(){
  const S=Array.from({length:16},(_,i)=>i), chi=(x,u)=>{let t=x&u,n=0;while(t){n^=t&1;t>>=1}return n?-1:1};
  const sum=a=>a.reduce((x,y)=>x+y,0),m=(p,u)=>sum(p.map((w,i)=>w*chi(i,u)));
  let checks=0;const eq=(a,b)=>{if(Math.abs(a-b)>1e-9)throw Error(`${a} != ${b}`);checks++},ok=(v)=>{if(!v)throw Error("check failed");checks++};
  const observe=(p,u,q)=>[-1,1].map(y=>{let z=p.map((w,i)=>w*(1+y*(2*q-1)*chi(i,u))/2),mass=sum(z);return{y,mass,p:z.map(w=>mass?w/mass:0)}}).filter(z=>z.mass>1e-12);
  const prior=(d)=>S.map(i=>(1+d*chi(i,3))/16);
  for(let k=1;k<=100;k++){
    const w=S.map(i=>1+((i+7)*(k+3)*17+i*i*3)%31),p=w.map(x=>x/sum(w));
    for(const v of [1,3,4,7,9,15])for(const q of [.5,.73,1])for(const o of observe(p,v,q)){
      for(let u=0;u<16;u++)eq(m(o.p,u),(m(p,u)+o.y*(2*q-1)*m(p,u^v))/(1+o.y*(2*q-1)*m(p,v)));
    }
  }
  for(const z of [-.7,0,.2,.9,1])for(const a of [-.5,0,.7,1])for(const b of [0,.3,.8,1])for(const c of [0,.5,1]){
    const means=[z,a,b,c],p=S.map(i=>means.reduce((v,mu,j)=>v*(1+mu*chi(i,1<<j))/2,1));
    eq(m(p,6),a*b);eq(m(p,15),z*a*b*c);
  }
  const target=[7,4],value=[4,10];
  function solve(p,H,P,mask=3){
    let best={v:0,n:[0,0],first:"stop"};
    if(H<=0||P<=0||!mask)return best;
    for(let j=0;j<2;j++)if(mask&(1<<j))for(const guess of [-1,1]){
      let r={v:0,n:[0,0],first:`${j}:${guess}`};
      for(const o of observe(p,target[j],1)){
        let a=solve(o.p,H-1,P,mask^(1<<j));
        if(o.y===guess){let b=solve(o.p,H-1,P-1,mask^(1<<j));b={...b,v:b.v+value[j],n:b.n.slice()};b.n[j]++;if(b.v>a.v+1e-12)a=b}
        r.v+=o.mass*a.v;r.n=r.n.map((x,i)=>x+o.mass*a.n[i]);
      }
      if(r.v>best.v+1e-12)best=r;
    }
    return best;
  }
  function outside(p,H,P,q,fee){
    let v=-fee,n=[0,0];for(const o of observe(p,4,q)){const r=solve(o.p,H,P);v+=o.mass*r.v;n=n.map((x,i)=>x+o.mass*r.n[i])}return {v,n};
  }
  const results=[];
  for(const d of [-1,-.8,0,.4,.8,1])for(const H of [1,2,3])for(const P of [1,2])for(const q of [.5,.8,1]){
    const p=prior(d);eq(m(p,7),0);eq(m(p,4),0);eq(m(p,3),d);
    for(const u of [1,2,4])eq(m(p,u),0);
    const a=solve(p,H,P),b=outside(p,H,P,q,0);
    ok(b.v>=a.v-1e-9);ok(sum(a.n)<=P+1e-9);ok(sum(b.n)<=P+1e-9);
    if(H>=2&&P===2)eq(a.v,2+5*(1+Math.abs(d)));
    if(H===1)eq(a.v,5);
    if(H>=2&&P===2&&q===1)eq(b.v,10+2*(1+Math.abs(d)));
    results.push({d,H,P,q,ordinary:a,external:outside(p,H,P,q,3.5)});
  }
  const comp=(p,q,D,b,p2,D2,alpha,F,publicAccess)=>{
    let base=[0,0],net=[0,0],real0=0,real=0,robot0=0,robot=0;
    for(const a of [0,1])for(const c of [0,1])for(const e of [0,1])for(const r of [0,1]){
      let w=(a?p:1-p)*(c?p:1-p)*(e?p2:1-p2)*(r?q:1-q);
      let aa=a||r,cc=c||(publicAccess&&r),ee=e||(publicAccess&&r);
      base[0]+=w*(D*a*(1-c)+b*a);base[1]+=w*(D*c*(1-a)+b*c+alpha*D2*e);
      net[0]+=w*(D*aa*(1-cc)+b*aa);net[1]+=w*(D*cc*(1-aa)+b*cc+alpha*D2*ee);
      real0+=w*(D*(a||c)+D2*e);real+=w*(D*(aa||cc)+D2*ee);
      robot0+=w*((a||c)+e);robot+=w*((aa||cc)+ee);
    }
    return {gain:net.map((v,i)=>v-base[i]),realGain:real-real0-F,robotGain:robot-robot0};
  };
  for(const p of [.1,.4,.7,.9])for(const q of [0,.2,.7,1])for(const p2 of [.2,.6])for(const b of [0,.2,1]){
    const D=10,D2=6,alpha=.1,F=.4,r=comp(p,q,D,b,p2,D2,alpha,F,true);
    eq(r.gain[0],q*(1-p)*(b-D*p));eq(r.gain[1],q*(1-p)*(b-D*p)+q*(1-p2)*alpha*D2);
    eq(r.realGain,q*(D*(1-p)**2+D2*(1-p2))-F);eq(r.robotGain,q*((1-p)**2+1-p2));
    const ex=comp(p,q,D,b,p2,D2,alpha,F,false);
    eq(ex.gain[0],q*(1-p)*(D*(1-p)+b));eq(ex.realGain,q*D*(1-p)**2-F);
  }
  const publicCase=comp(.5,.8,10,.2,.4,6,.1,1,true),exclusiveCase=comp(.5,.8,10,.2,.4,6,.1,1,false);
  ok(publicCase.gain.every(x=>x<0));ok(publicCase.realGain>exclusiveCase.realGain);ok(exclusiveCase.gain[0]>1);
  return {checks,cases:results.length,scope:"Synthetic finite posterior, safe test and procurement enumeration; not industrial calibration or full CI",witness:results.filter(x=>[0,.8].includes(x.d)&&x.H===2&&x.P===2&&x.q===1),publicCase,exclusiveCase};
}
console.log(JSON.stringify(study(),null,2));
