// Reproduce with node shared_metrology_market.js; synthetic values, not field estimates.
function study(){
  let checks=0,cases=0,crowdCases=0;
  const eps=1e-9,eq=(a,b)=>{checks++;if(Math.abs(a-b)>eps)throw Error(`${a} != ${b}`)},ok=x=>{checks++;if(!x)throw Error("assertion")};
  function outcomes(p,q,j,D,c,d,e,f,x,y){
    let a=0,b=0,w=0,na=0,nb=0;
    for(const [sa,sb,pr] of [[1,1,j],[1,0,p-j],[0,1,q-j],[0,0,1-p-q+j]]){
      const aa=sa*x,bb=sb*y,wa=aa*(1-bb/2),wb=bb*(1-aa/2);
      na+=pr*wa;nb+=pr*wb;
      a+=pr*(D*aa*(1-bb)+e*wa);
      b+=pr*(D*bb*(1-aa)+f*wb);
      w+=pr*D*(aa||bb);
    }
    return {a:a-c*x,b:b-d*y,real:w-c*x-d*y,n:[na,nb]};
  }
  function analytic(p,q,j,D,c,d,e,f,x,y){
    const k=j*x*y,A=p*x-k/2,B=q*y-k/2;
    return {a:D*(p*x-k)+e*A-c*x,b:D*(q*y-k)+f*B-d*y,real:D*(p*x+q*y-k)-c*x-d*y,n:[A,B]};
  }
  function pure(p,q,j,D,c,d,e=0,f=0){
    let out=[];
    for(const x of [0,1])for(const y of [0,1]){
      let z=analytic(p,q,j,D,c,d,e,f,x,y);
      if(z.a>=analytic(p,q,j,D,c,d,e,f,1-x,y).a-eps&&z.b>=analytic(p,q,j,D,c,d,e,f,x,1-y).b-eps)out.push({test:[x,y],...z});
    }
    return out;
  }
  function mixed(p,q,j,D,c,d,e=0,f=0){
    if(j===0)return null;
    const x=(q*(D+f)-d)/(j*(D+f/2)),y=(p*(D+e)-c)/(j*(D+e/2));
    if(x<=0||x>=1||y<=0||y>=1)return null;
    let v={a:0,b:0,real:0,n:[0,0]};
    for(const i of [0,1])for(const k of [0,1]){
      let pr=(i?x:1-x)*(k?y:1-y),z=outcomes(p,q,j,D,c,d,e,f,i,k);
      v.a+=pr*z.a;v.b+=pr*z.b;v.real+=pr*z.real;v.n[0]+=pr*z.n[0];v.n[1]+=pr*z.n[1];
    }
    eq(v.a,0);eq(v.b,0);
    return {test:[x,y],...v};
  }
  const grid=[.2,.4,.6,.8],costs=[.5,1.5,2.5,4,5.5];
  for(const p of grid)for(const q of grid){
    const lo=Math.max(0,p+q-1),hi=Math.min(p,q);
    for(const j of [lo,(lo+hi)/2,hi])for(const c of costs)for(const d of costs)for(const e of [0,1])for(const f of [0,2]){
      cases++;
      for(const x of [0,1])for(const y of [0,1]){
        let z=outcomes(p,q,j,10,c,d,e,f,x,y),a=analytic(p,q,j,10,c,d,e,f,x,y);
        for(const k of ["a","b","real"])eq(z[k],a[k]);
        eq(z.n[0],a.n[0]);eq(z.n[1],a.n[1]);
      }
      ok(pure(p,q,j,10,c,d,e,f).length>=1);mixed(p,q,j,10,c,d,e,f);
    }
  }
  for(const p of grid)for(const q of grid)for(const r of grid.filter(x=>x>p)){
    const lo=Math.max(0,p+q-1),hi=Math.min(p,q);
    for(const j of [lo,(lo+hi)/2,hi]){
      const aLo=Math.max(0,r-p-(1-q-p+j)),aHi=Math.min(r-p,q-j);
      if(aLo>aHi+eps)continue;
      for(const dj of [aLo,(aLo+aHi)/2,aHi])for(const c of costs)for(const d of costs){
        const k=j+dj;
        if(!(10*(p-j)>c+eps&&10*(q-j)>d+eps&&10*(r-k)>c+eps&&10*(q-k)<d-eps))continue;
        crowdCases++;
        const before=pure(p,q,j,10,c,d),after=pure(r,q,k,10,c,d);
        ok(before.length===1&&before[0].test.join()==="1,1");
        ok(after.length===1&&after[0].test.join()==="1,0");
        const W=after[0].a-before[0].a,R=after[0].real-before[0].real;
        eq(W,10*(r-p+j));eq(R,W-10*q+d);ok(R>0);ok(W>R);
        eq(after[0].n[0]+after[0].n[1]-before[0].n[0]-before[0].n[1],r-p-q+j);
      }
    }
  }
  const base=pure(.5,.6,.3,10,1.5,2.4)[0],a=pure(.7,.6,.42,10,1.5,2.4)[0];
  const W=a.a-base.a,R=a.real-base.real;
  eq(W,5);eq(R,1.4);eq(base.n[1],.45);
  const pc=.3,rc=.8,Dc=8,alpha=.5,cc=.5;
  ok(alpha*Dc*pc>cc);ok(alpha*Dc*rc>cc);
  const WC=alpha*Dc*(rc-pc),RC=Dc*(rc-pc);
  const p0=.2,u=.5,betaD=10;
  const successor=(b)=>(1-p0)*u*b;
  const succLoss=betaD*(successor(a.n[1])-successor(base.n[1]));
  eq(succLoss,-1.8);
  let plans=[];
  for(const A of [0,1])for(const C of [0,1]){
    let n=A+C,cost=n===0?0:n===1?.8:3.3;
    let ab=A?a:base,cprob=C?rc:pc;
    plans.push({plan:[A,C],capacity:n,realCapacityCost:cost,providerProfit:A*W+C*WC-cost,
      realGain:A*(R+succLoss)+C*RC-cost,
      installations:[ab.n[0],ab.n[1],cprob,p0+successor(ab.n[1])],
      totalCurrent:ab.n[0]+ab.n[1]+cprob,
      fees:[A*W,C*WC]});
  }
  const privateBest=plans.reduce((a,b)=>b.providerProfit>a.providerProfit?b:a);
  const realBest=plans.reduce((a,b)=>b.realGain>a.realGain?b:a);
  ok(privateBest.plan.join()==="1,0");ok(realBest.plan.join()==="0,1");
  eq(privateBest.realGain,-1.2);eq(realBest.realGain,3.2);
  eq(privateBest.totalCurrent-plans[0].totalCurrent,-.1);
  const shared={pure:pure(.7,.8,.58,10,1.5,2.4),mixed:mixed(.7,.8,.58,10,1.5,2.4)};
  ok(shared.pure.length===2&&shared.mixed!==null);
  const cutoff=(2.4-10*(.6-.42))/(.6-.42/2);
  eq(cutoff,20/13);
  ok(pure(.7,.6,.42,10,1.5,2.4,0,cutoff-.01)[0].test.join()==="1,0");
  ok(pure(.7,.6,.42,10,1.5,2.4,0,cutoff+.01)[0].test.join()==="1,1");
  return {checks,cases,crowdCases,scope:"Finite synthetic qualification entry, joint outcome enumeration, and capacity menu; no empirical calibration or full CI",baseline:base,upgradeA:a,W,R,WC,RC,succLoss,plans,privateBest,realBest,shared,BprivateContinuationCutoff:cutoff};
}
console.log(JSON.stringify(study(),null,2));
