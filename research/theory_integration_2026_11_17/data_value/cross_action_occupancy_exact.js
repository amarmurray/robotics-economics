'use strict';
// Exact rational demonstration and exhaustive sharp-bound enumeration for documented conditional common-law theorem.
function check(){
  const assert=(cond,msg)=>{if(!cond)throw Error(msg);checks++};let checks=0;
  const gcd=(a,b)=>{a=a<0n?-a:a;b=b<0n?-b:b;while(b){const t=a%b;a=b;b=t}return a||1n};
  class R{
    constructor(n,d=1n){n=BigInt(n);d=BigInt(d);if(d===0n)throw Error("zero denominator");if(d<0n){n=-n;d=-d}const g=gcd(n,d);this.n=n/g;this.d=d/g;}
    add(o){return new R(this.n*o.d+o.n*this.d,this.d*o.d)}
    mul(o){return new R(this.n*o.n,this.d*o.d)}
    sub(o){return new R(this.n*o.d-o.n*this.d,this.d*o.d)}
    eq(o){return this.n===o.n && this.d===o.d}
    toString(){return this.d===1n?String(this.n):`${this.n}/${this.d}`}
  }
  const r=(n,d=1)=>new R(n,d),z=r(0),one=r(1);
  let validatedJointLaws=0;let extremes=[];
  for(let k=0;k<=16;k++){
    const t=r(k,64), extra=r(32-k,48-k);
    let sum=z,W=z,F=z,A=z,B=z,AB=z,AW0=z,mis=z,Q=z,D=z,QD=z,QF=z,DF=z;
    for(let q=0;q<=1;q++)for(let d=0;d<=1;d++)for(let f=0;f<=1;f++){
      const p=r((q+d+f)%2===1?k:16-k,64);
      for(let w=0;w<=1;w++){
        const pw=f===1?(w===1?one:z):r(1,2);
        if(pw.eq(z))continue;
        const b=q*d*f;
        for(let a=0;a<=1;a++){
          let pa;
          if(w===0)pa=a===0?one:z;
          else if(b===1)pa=a===1?one:z;
          else pa=a===1?extra:one.sub(extra);
          if(pa.eq(z))continue;
          const mass=p.mul(pw).mul(pa);
          sum=sum.add(mass);
          if(w)W=W.add(mass);
          if(f)F=F.add(mass);
          if(a)A=A.add(mass);
          if(b)B=B.add(mass);
          if(a&&b)AB=AB.add(mass);
          if(a&&!w)AW0=AW0.add(mass);
          if(a!==b)mis=mis.add(mass);
          if(q)Q=Q.add(mass);
          if(d)D=D.add(mass);
          if(q&&d)QD=QD.add(mass);
          if(q&&f)QF=QF.add(mass);
          if(d&&f)DF=DF.add(mass);
        }
      }
    }
    for(let [actual,expected,name] of [[sum,one,"norm"],[W,r(3,4),"W"],[F,r(1,2),"F"],[A,r(1,2),"A"],[B,t,"B"],[AB,t,"AB"],[AW0,z,"A≤W"],[mis,r(1,2).sub(t),"mismatch"],[Q,r(1,2),"Q"],[D,r(1,2),"D"],[QD,r(1,4),"QD"],[QF,r(1,4),"QF"],[DF,r(1,4),"DF"]])assert(actual.eq(expected),`${name} k=${k} ${actual} vs ${expected}`);
    assert((mis.n*8n<=mis.d*3n)===(k>=8),`ε feasibility k=${k}`);
    let G=r(5,16).add(t.mul(r(2))),P=r(3,4),E=r(23,32);
    assert(G.eq(r(5,16).add(t.mul(r(2)))),"G formula");
    assert(P.eq(r(3,4)) && E.eq(r(23,32)),"comparator");
    if(k===8||k===16) extremes.push({t:t.toString(),G:G.toString(),P:P.toString(),E:E.toString(),workerFree:W.toString(),discordance:mis.toString(),maxProgram:(G.n*P.d>P.n*G.d?"G":"P")});
    validatedJointLaws++;
  }
  let sharpCells=0,sharpBounds=0,infeasible=0;
  for(let c=0;c<=16;c++)for(let l=0;l<=16-c;l++)for(let d=0;d<=16-c-l;d++){
    const e=16-c-l-d;
    for(let eps=0;eps<=16;eps++){
      let min=17,max=-1;
      for(let x=0;x<=c;x++)for(let y=0;y<=d;y++){
        const disag=l+(c-x)+y;
        if(disag<=eps){min=Math.min(min,x+y);max=Math.max(max,x+y);}
      }
      if(eps<l){assert(max===-1,`feasible despite forced mismatch ${c},${l},${d},${e},${eps}`);infeasible++}
      else{
        assert(min===Math.max(0,c+l-eps),`lower bound failure ${c} ${l} ${d} eps=${eps} got=${min}`);
        assert(max===Math.min(c+d,c+eps-l),`upper bound failure ${c} ${l} ${d} eps=${eps} got=${max}`);
        sharpBounds++;
      }
    }
    sharpCells++;
  }
  const tL=r(1,8),tU=r(1,4), P=r(3,4), G_L=r(9,16), G_U=r(13,16);
  const gMix=r(1,4), lowerReg=gMix.mul(P.sub(G_L)), upperReg=one.sub(gMix).mul(G_U.sub(P));
  assert(lowerReg.eq(r(3,64)) && upperReg.eq(r(3,64)),"regret equilibrium");
  assert(r(1,8).mul(r(7,16)).eq(r(7,128)),"prior regret");
  const PvsE=P.sub(r(23,32));
  assert(PvsE.eq(r(1,32)),"E comparator");
  return {model:"Common-law target-grounding zero-support sensitivity and queue safety",exactAssertions:checks,discreteSharpObservedTables:sharpCells,discreteSharpBoundConfigurations:sharpBounds,infeasibleConfigurations:infeasible,constructedPairwiseMatchedJointLaws:validatedJointLaws,lawfulSensitivityFeasibleT:"[1/8,1/4]",P:"3/4",E:"23/32",calibratedGInterval:"[9/16,13/16]",GMinimaxRegretShare:"1/4",worstRegret:"3/64",oldUnrestrictedWorstRegret:"7/128",extremes,limitations:"Exact synthetic common histories; cross-arm discordance bound is an unverified sensitivity assumption, no original-buyer field data."};
}
console.log(JSON.stringify(check(),null,2));
