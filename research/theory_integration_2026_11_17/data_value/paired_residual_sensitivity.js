/* Exact paired whole-service uncertainty comparison; normalized synthetic units.
   Run: node -p "JSON.stringify(require('./paired_residual_sensitivity.js'),null,2)"
   No external dependencies. Standard box and linear optimization identities. */
(function () {
  "use strict";
  function gcd(a,b){a=a<0n?-a:a;b=b<0n?-b:b;while(b){const t=a%b;a=b;b=t;}return a||1n;}
  function F(n,d=1n){n=BigInt(n);d=BigInt(d);if(d<0n){n=-n;d=-d;}if(d===0n)throw Error("zero denominator");const g=gcd(n,d);return [n/g,d/g];}
  const add=(a,b)=>F(a[0]*b[1]+b[0]*a[1],a[1]*b[1]);
  const neg=a=>F(-a[0],a[1]);
  const sub=(a,b)=>add(a,neg(b));
  const mul=(a,b)=>F(a[0]*b[0],a[1]*b[1]);
  const cmp=(a,b)=>a[0]*b[1]<b[0]*a[1]?-1:(a[0]*b[1]>b[0]*a[1]?1:0);
  const min=(a,b)=>cmp(a,b)<0?a:b;
  const fmt=a=>a[1]===1n?String(a[0]):String(a[0])+"/"+String(a[1]);
  const z=F(0),one=F(1);
  let checks=0;
  function assert(condition,msg){checks++;if(!condition)throw Error("failed: "+msg);}
  function bounds(pa,pb,l,h,eta){
    if(cmp(z,pa)>0||cmp(pa,one)>0||cmp(z,pb)>0||cmp(pb,one)>0||cmp(l,h)>0||cmp(z,eta)>0||cmp(eta,sub(h,l))>0)throw Error("invalid domain");
    const d=sub(pa,pb),o=mul(min(pa,pb),eta);
    if(cmp(d,z)>=0)return {low:sub(mul(d,l),o),high:add(mul(d,h),o)};
    return {low:sub(mul(d,h),o),high:add(mul(d,l),o)};
  }
  function naive(pa,pb,l,h){return {low:sub(mul(pa,l),mul(pb,h)),high:sub(mul(pa,h),mul(pb,l))};}
  const pa=F(1,2),pb=F(1,4),D=F(-1,20),l=F(0),h=F(4);
  function withD(b){return {low:fmt(add(D,b.low)),high:fmt(add(D,b.high))};}
  const baseline={common:withD(bounds(pa,pb,l,h,z)),
    paired_eta_half:withD(bounds(pa,pb,l,h,F(1,2))),
    unrestricted:withD(bounds(pa,pb,l,h,F(4))),
    naive:withD(naive(pa,pb,l,h)),
    diagnostic_u_3_to_4_eta_1:withD(bounds(pa,pb,F(3),F(4),F(1))),
    diagnostic_u_3_to_4_eta_0:withD(bounds(pa,pb,F(3),F(4),z))};
  assert(baseline.common.low==="-1/20" && baseline.common.high==="19/20","common");
  assert(baseline.paired_eta_half.low==="-7/40" && baseline.paired_eta_half.high==="43/40","half");
  assert(baseline.unrestricted.low==="-21/20" && baseline.unrestricted.high==="39/20","unrestricted");
  assert(JSON.stringify(baseline.unrestricted)===JSON.stringify(baseline.naive),"naive endpoint");
  assert(baseline.diagnostic_u_3_to_4_eta_1.low==="9/20" && baseline.diagnostic_u_3_to_4_eta_1.high==="6/5","conditional diagnostic");
  assert(baseline.diagnostic_u_3_to_4_eta_0.low==="7/10" && baseline.diagnostic_u_3_to_4_eta_0.high==="19/20","diagnostic invariant");
  let grids=0;
  // Exact adversarial 5x5 corner/inner grid: eta and l/h share the grid, so extremes are attained.
  for(const paN of [0,1,2,3,4])for(const pbN of [0,1,2,3,4])
  for(const width of [1,2,4])for(const etaN of [0,1,2,3,4]){
    const a=F(paN,4),b=F(pbN,4),lo=F(0),hi=F(width),eta=F(width*etaN,4);
    const claim=bounds(a,b,lo,hi,eta);
    let low=null,high=null;
    for(let i=0;i<=4;i++)for(let j=0;j<=4;j++){
      const ua=F(width*i,4),ub=F(width*j,4);
      const gap=cmp(ua,ub)>=0?sub(ua,ub):sub(ub,ua);
      if(cmp(gap,eta)>0)continue;
      const val=sub(mul(a,ua),mul(b,ub));
      if(low===null||cmp(val,low)<0)low=val;
      if(high===null||cmp(val,high)>0)high=val;
    }
    assert(cmp(claim.low,low)===0&&cmp(claim.high,high)===0,"grid exact "+[paN,pbN,width,etaN].join(","));
    grids++;
    if(etaN===4){
      const independent=naive(a,b,lo,hi);
      assert(cmp(claim.low,independent.low)===0&&cmp(claim.high,independent.high)===0,"unrestricted ends");
    }
  }
  // Same observed K,p and support, reversed unsupported returns => opposite economically preferred arm.
  const worldA=add(D,sub(mul(pa,F(0)),mul(pb,F(4))));
  const worldB=add(D,sub(mul(pa,F(4)),mul(pb,F(0))));
  assert(fmt(worldA)==="-21/20" && fmt(worldB)==="39/20","nonidentification counterexample");
  const result={model:"Paired unsupported residuals with auditable policy-discrepancy cap",
    assumptions:"Same whole-network opportunity census, policy-specific identified K/p, common state label, each remaining conditional expected value in [l,h], and joint |u_a-u_b| <= eta; rectangular labels only for multi-label sharpness.",
    formula:"lower/upper = common-residual signed bounds minus/plus min(p_a,p_b)*eta, for 0<=eta<=h-l",
    baseline,undetectable_worlds:{copy_worse:fmt(worldA),copy_better:fmt(worldB)},
    exact_grid_cases:grids,checks};
  if(typeof module!=="undefined"&&module.exports)module.exports=result;
  return result;
})()
