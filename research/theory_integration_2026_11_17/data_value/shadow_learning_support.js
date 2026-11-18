// Conditional robotics-economics shadow-learning and support audit.
// Exact fractions via BigInt. Reproduce with: node shadow_learning_support.js
const shadowResearchChecks = function shadowResearchChecks(){
  const gcd=(a,b)=>{while(b!==0n){const t=a%b;a=b;b=t}return a<0n?-a:a};
  const F=(n,d=1)=>{n=BigInt(n);d=BigInt(d);if(d===0n)throw Error("zero denominator");if(d<0n){n=-n;d=-d}const g=gcd(n,d);return [n/g,d/g]};
  const add=(x,y)=>F(x[0]*y[1]+y[0]*x[1],x[1]*y[1]);
  const sub=(x,y)=>F(x[0]*y[1]-y[0]*x[1],x[1]*y[1]);
  const mul=(x,y)=>F(x[0]*y[0],x[1]*y[1]);
  const eq=(x,y)=>x[0]===y[0]&&x[1]===y[1];
  const cmp=(x,y)=>{const n=x[0]*y[1]-y[0]*x[1];return n<0n?-1:n>0n?1:0};
  const show=x=>x[1]===1n?String(x[0]):`${x[0]}/${x[1]}`;
  let checks=0;
  const assert=(v,m)=>{checks++;if(!v)throw Error("assertion "+checks+": "+m)};
  const zero=F(0),one=F(1);
  const lowWeight=F(3,5),highWeight=F(2,5),lowService=F(1,2),highMax=F(2);
  const cost=F(1,4),specialistNet=F(2,5);
  const gross=h=>add(mul(lowWeight,lowService),mul(highWeight,h));
  const net=h=>sub(gross(h),cost);
  assert(eq(net(zero),F(1,20)),"lower bound");
  assert(eq(net(highMax),F(17,20)),"upper bound");
  const breakeven=F(7,8);
  assert(eq(net(breakeven),specialistNet),"specialist threshold");
  assert(cmp(net(zero),specialistNet)<0 && cmp(net(highMax),specialistNet)>0,"ranking not identified");
  for(let k=0;k<=16;k++){
    const h=F(k,8),v=net(h);
    assert(cmp(v,net(zero))>=0 && cmp(v,net(highMax))<=0,"finite-grid sharp interval");
    assert(cmp(v,specialistNet)===cmp(h,breakeven),"pointwise ranking threshold");
  }
  // Two observationally identical F logs (zero A probes); A targeted service differs across worlds.
  const worlds=[{id:"A-unsupported-fails",observedF:"B0: accepted",targetGain:zero},
    {id:"A-unsupported-works",observedF:"B0: accepted",targetGain:highMax}];
  assert(worlds[0].observedF===worlds[1].observedF,"source log observational equivalence");
  assert(!eq(worlds[0].targetGain,worlds[1].targetGain),"target not identified by F");
  // Separate physical isolation and resource isolation: identical B controller, but shared operator resource lowers accepted B.
  const Bbaseline=F(2),BwithQueue=F(19,10);
  assert(cmp(BwithQueue,Bbaseline)<0,"controller pinning is insufficient for B");
  // Joint qualification with p1=1/2 and p2=3/4: Fréchet joint probability bounds [1/4,1/2].
  const p1=F(1,2),p2=F(3,4),jointLo=F(1,4),jointHi=F(1,2);
  const indep=mul(p1,p2);
  assert(eq(indep,F(3,8)),"independent joint");
  const feasibleJoint=q=>cmp(q,jointLo)>=0 && cmp(q,jointHi)<=0;
  for(let j=0;j<=8;j++){
    const q=F(j,16);
    // Explicit four-cell joint probability table nonnegative and total 1.
    const n11=q,n10=sub(p1,q),n01=sub(p2,q),n00=add(sub(one,add(p1,p2)),q);
    const valid=[n11,n10,n01,n00].every(v=>cmp(v,zero)>=0);
    assert(valid===feasibleJoint(q),"joint Frechet consistency");
    assert(eq(add(add(n11,n10),add(n01,n00)),one),"joint table sums to one");
  }
  const eligiblePeriods=2; // T=4, qualification latency=2, remaining periods t=2,3
  const expectedGain=q=>sub(mul(F(eligiblePeriods),q),cost);
  assert(eq(expectedGain(indep),F(1,2)),"two remaining periods, independence");
  assert(eq(expectedGain(jointLo),F(1,4)),"two periods, adverse correlation");
  assert(eq(expectedGain(jointHi),F(3,4)),"two periods, favorable correlation");
  assert(eq(sub(mul(F(0),indep),cost),F(-1,4)),"expired market, forced expenditure loses");
  // Free optional acquisition cannot reduce an unchanged feasible policy menu.
  const b=(values)=>values.reduce((m,v)=>cmp(v,m)>0?v:m,zero);
  const baseMenu=[zero,specialistNet],expandedMenu=[...baseMenu,F(-1,4),F(1,2)];
  assert(cmp(b(expandedMenu),b(baseMenu))>=0,"option set inclusion");
  assert(eq(b([zero,F(-1,4)]),zero),"fallback prevents loss before sunk investment");
  // Exact support decomposition: 3/5 covered, 2/5 uncovered with [0,2].
  assert(eq(gross(zero),F(3,10))&&eq(gross(highMax),F(11,10)),"support bound");
  return {status:"passed",checks,illustrations:{
    target_support_share:"3/5",unsupported_share:"2/5",
    known_supported_mean:"1/2",unsupported_mean_range:["0","2"],investment_cost:"1/4",
    shadow_net_identified_interval:[show(net(zero)),show(net(highMax))],
    competent_specialist_net:show(specialistNet),
    shadow_beats_specialist_iff_unsupported_mean_exceeds:show(breakeven),
    qualification_marginals:[show(p1),show(p2)],
    joint_qualification_frechet_range:[show(jointLo),show(jointHi)],
    independent_joint_qualification:show(indep),
    remaining_service_periods:eligiblePeriods,
    two_period_qualification_net_range:[show(expectedGain(jointLo)),show(expectedGain(jointHi))],
    independence_net:show(expectedGain(indep)),
    expired_demand_forced_training_net:"-1/4"
  },caveat:"Constructed normalized economic inputs; no target population, safety, technical transfer or customer evidence."};
};
const result = shadowResearchChecks();
if (typeof console !== "undefined") console.log(JSON.stringify(result,null,2));
