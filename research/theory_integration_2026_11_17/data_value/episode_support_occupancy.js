"use strict";
// Fixed-archive occupancy and source/grounding/embodiment counterexample; normalized hypothetical units only.
const occupancyAudit = function occupancyAudit() {
  class F {
    constructor(n,d=1n) {n=BigInt(n);d=BigInt(d);if(d===0n)throw Error("zero");if(d<0n){n=-n;d=-d}let a=n<0n?-n:n,b=d;while(b){let c=a%b;a=b;b=c}this.n=n/a;this.d=d/a;}
    add(y){return new F(this.n*y.d+y.n*this.d,this.d*y.d)}
    neg(){return new F(-this.n,this.d)}
    sub(y){return this.add(y.neg())}
    mul(y){return new F(this.n*y.n,this.d*y.d)}
    pow(k){return new F(this.n**BigInt(k),this.d**BigInt(k))}
    eq(y){return this.n===y.n&&this.d===y.d}
    le(y){return this.n*y.d<=y.n*this.d}
    toString(){return this.d===1n?this.n.toString():this.n+"/"+this.d}
  }
  const f=(a,b=1)=>new F(a,b),zero=f(0),one=f(1);
  let checks=0;
  function ck(x,y,label){if(!x.eq(y))throw Error(label+": "+x+" != "+y);checks++}
  function expect(c,label){if(!c)throw Error(label);checks++}
  function sum(a){return a.reduce((x,y)=>x.add(y),zero)}
  function expectedDistinct(w,k){return sum(w.map(p=>one.sub(one.sub(p).pow(k))))}
  function both(w,k){let a=w[0],b=sum(w.slice(1));return one.sub(a.pow(k)).sub(b.pow(k))}
  function distinctTwoB(w){let a=w[0],b=sum(w.slice(1)),h=sum(w.slice(1).map(z=>z.pow(2)));return f(3).mul(a).mul(b.pow(2).sub(h))}
  function enumerate(w,variant){let n=w.length,c=zero;for(let i=0;i<n;i++)for(let j=0;j<n;j++)for(let k=0;k<n;k++){
    let ids=[i,j,k],ns=ids.filter(x=>x>0),qualified=variant==="both" ? ids.includes(0)&&ns.length>0 : ns.length===2&&ns[0]!==ns[1]&&ids.includes(0);
    if(qualified)c=c.add(w[i].mul(w[j]).mul(w[k]));
  }return c}
  const old=[f(9,10),f(1,10)],ground=[f(1,2),f(1,2)],source=[f(9,18),...Array.from({length:9},()=>f(1,18))];
  const policies={old,ground,source};let probabilities={},distinctEpisodes={},hhi={};
  for(const [name,w] of Object.entries(policies)){
    ck(sum(w),one,name+" normalized weights");
    ck(both(w,3),enumerate(w,"both"),name+" qualified both enumeration");
    ck(distinctTwoB(w),enumerate(w,"diverse"),name+" distinct B enumeration");
    probabilities[name]={both:both(w,3).toString(),two_distinct_B:distinctTwoB(w).toString()};
    distinctEpisodes[name]=expectedDistinct(w,3).toString();
    hhi[name]=sum(w.map(z=>z.pow(2))).toString();
  }
  ck(both(old,3),f(27,100),"baseline both");
  ck(both(ground,3),f(3,4),"grounding both");
  ck(both(source,3),f(3,4),"new source both");
  ck(distinctTwoB(old),zero,"baseline no distinct B");
  ck(distinctTwoB(ground),zero,"ground no new B");
  ck(distinctTwoB(source),f(1,3),"new source distinct B");
  ck(expectedDistinct(old,3),f(127,100),"baseline distinct episodes");
  ck(expectedDistinct(ground,3),f(7,4),"ground distinct episodes");
  ck(sum(source.map(z=>z.pow(2))),f(5,18),"source HHI");
  const grossQualified=f(12),retained=f(2),increment=grossQualified.sub(retained),E=f(19,5);
  const costs={old:zero,ground:f(2,5),source:f(7,5)};
  const outcome={};for(let rule of ["both","diverse"]){
    let v={};for(const [name,w] of Object.entries(policies)){
      let prob=rule==="both"?both(w,3):distinctTwoB(w);
      v[name]=retained.add(increment.mul(prob)).sub(costs[name]);
    }
    v.embodiment=E;
    outcome[rule]=Object.fromEntries(Object.entries(v).map(([k,x])=>[k,x.toString()]));
    expect((rule==="both"? v.ground.le(v.ground) && v.source.le(v.ground) && v.embodiment.le(v.ground) && v.old.le(v.ground) : v.old.le(v.source)&&v.ground.le(v.source)&&v.embodiment.le(v.source)),rule+" winner");
  }
  ck(f(2).add(increment.mul(both(old,3))),f(47,10),"baseline both value");
  ck(f(2).add(increment.mul(both(ground,3))).sub(f(2,5)),f(91,10),"grounded value");
  ck(f(2).add(increment.mul(both(source,3))).sub(f(7,5)),f(81,10),"source value");
  ck(f(2).add(increment.mul(distinctTwoB(source))).sub(f(7,5)),f(59,15),"source diversity value");
  expect(f(59,15).n*E.d>E.n*f(59,15).d,"source diversity wins embodiment");
  let gridCases=0;
  for(let k=2;k<=6;k++)for(let i=0;i<=20;i++){
    let x=f(i,20),w=[x,one.sub(x)],balanced=expectedDistinct([f(1,2),f(1,2)],k);
    expect(expectedDistinct(w,k).le(balanced),"two-type balancing grid");
    gridCases++;
  }
  return {status:"exact conditional synthetic reference audit, no real archive or robot results",sampler:"iid with-replacement accepted episode draws, fixed 3 updates",source_episodes:"A length 9, initial B length 1, source acquires 8 new independent B episodes; grounding reweights existing A/B only",probabilities,expected_unique_episodes:distinctEpisodes,episode_hhi:hhi,original_customer_contribution:{fallback:"2",certified_success:"12",fixed_E:"19/5",cost_ground:"2/5",cost_new_source:"7/5",fully_optimized_policy_values:outcome},exact_checks:checks,grid_cases:gridCases,truth_status:"finite enumeration supports formulas; calculus proofs and causal assumptions are in companion theory text"};
};
if (typeof module !== "undefined") module.exports = occupancyAudit;
if (typeof require !== "undefined" && require.main === module) process.stdout.write(JSON.stringify(occupancyAudit(),null,2)+"\n");
