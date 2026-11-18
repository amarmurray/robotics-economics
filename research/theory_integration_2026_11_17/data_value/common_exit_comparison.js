"use strict";
// Conditional same-world policy comparison. Exact fractions; no robotics calibration.
function abs(a){return a<0n?-a:a;}
function gcd(a,b){a=abs(a);b=abs(b);while(b){const t=a%b;a=b;b=t;}return a||1n;}
function q(n,d=1){n=BigInt(n);d=BigInt(d);if(!d)throw Error("zero denominator");if(d<0n){n=-n;d=-d;}const g=gcd(n,d);return [n/g,d/g];}
function add(a,b){return q(a[0]*b[1]+b[0]*a[1],a[1]*b[1]);}
function neg(a){return [-a[0],a[1]];}
function sub(a,b){return add(a,neg(b));}
function mul(a,b){return q(a[0]*b[0],a[1]*b[1]);}
function cmp(a,b){const n=sub(a,b)[0];return n<0n?-1:n>0n?1:0;}
function str(a){return a[1]===1n?String(a[0]):String(a[0])+"/"+String(a[1]);}
function min(a,b){return cmp(a,b)<0?a:b;}
function max(a,b){return cmp(a,b)>0?a:b;}
function scalarPolicies(ka,kb,rows){
  let exactLo=sub(ka,kb),exactHi=sub(ka,kb),sepLo=sub(ka,kb),sepHi=sub(ka,kb);
  let overlap=q(0),pASum=q(0),pBSum=q(0);
  for(const {pa,pb,l,u} of rows){
    if(cmp(pa,q(0))<0||cmp(pb,q(0))<0||cmp(l,u)>0)throw Error("bad stratum");
    const d=sub(pa,pb);
    exactLo=add(exactLo,mul(d,cmp(d,q(0))>=0?l:u));
    exactHi=add(exactHi,mul(d,cmp(d,q(0))>=0?u:l));
    sepLo=add(sepLo,sub(mul(pa,l),mul(pb,u)));
    sepHi=add(sepHi,sub(mul(pa,u),mul(pb,l)));
    overlap=add(overlap,mul(min(pa,pb),sub(u,l)));
    pASum=add(pASum,pa);pBSum=add(pBSum,pb);
  }
  if(cmp(pASum,q(1))>0||cmp(pBSum,q(1))>0)throw Error("exit probability >1");
  return {lo:exactLo,hi:exactHi,separateLo:sepLo,separateHi:sepHi,overlapGain:overlap};
}
function run(){
  let checks=0;
  function assertEq(a,b,label){checks++;if(cmp(a,b)!==0)throw Error(label+": "+str(a)+" !== "+str(b));}
  const ka=q(27,20),kb=q(7,5),pa=q(1,2),pb=q(1,4);
  const all=scalarPolicies(ka,kb,[{pa,pb,l:q(0),u:q(4)}]);
  assertEq(all.lo,q(-1,20),"common worst");
  assertEq(all.hi,q(19,20),"common best");
  assertEq(all.separateLo,q(-21,20),"separate worst");
  assertEq(all.separateHi,q(39,20),"separate best");
  assertEq(all.overlapGain,q(1),"overlap cancellation");
  assertEq(sub(all.lo,all.separateLo),all.overlapGain,"lower improvement identity");
  assertEq(sub(all.separateHi,all.hi),all.overlapGain,"upper improvement identity");
  for(let j=0;j<=16;j++){
    const u=q(j,4);
    const gain=sub(add(ka,mul(pa,u)),add(kb,mul(pb,u)));
    assertEq(gain,add(q(-1,20),mul(q(1,4),u)),"shared u arithmetic");
    if(cmp(gain,all.lo)<0||cmp(gain,all.hi)>0)throw Error("outside sharp interval");
    checks++;
  }
  const calibrated=scalarPolicies(ka,kb,[{pa,pb,l:q(3),u:q(4)}]);
  assertEq(calibrated.lo,q(7,10),"grounded contrast lower");
  assertEq(calibrated.hi,q(19,20),"grounded contrast upper");
  assertEq(add(ka,mul(pa,q(3))),q(57,20),"copy conditional lower");
  assertEq(add(kb,mul(pb,q(3))),q(43,20),"no-copy conditional lower");
  const identical=scalarPolicies(q(1,5),q(0),[{pa:q(1,4),pb:q(1,4),l:q(0),u:q(4)}]);
  assertEq(identical.lo,q(1,5),"identical occupancy cancellation lower");
  assertEq(identical.hi,q(1,5),"identical occupancy cancellation upper");
  const two=scalarPolicies(q(1,10),q(0),[
    {pa:q(1,4),pb:q(1,8),l:q(0),u:q(2)},
    {pa:q(1,4),pb:q(3,8),l:q(1),u:q(5)}
  ]);
  assertEq(two.lo,q(-21,40),"two strata lower");
  assertEq(two.hi,q(9,40),"two strata upper");
  for(let i=0;i<=8;i++)for(let j=0;j<=16;j++){
    const u1=q(i,4),u2=add(q(1),q(j,4));
    const a=add(q(1,10),add(mul(q(1,4),u1),mul(q(1,4),u2)));
    const b=add(mul(q(1,8),u1),mul(q(3,8),u2));
    const d=sub(a,b);
    if(cmp(d,two.lo)<0||cmp(d,two.hi)>0)throw Error("two-strata enumeration outside bounds");
    checks++;
  }
  // Falsification: a shared label alone does NOT establish common post-exit production.
  const falseInvariance=sub(mul(q(1,4),q(0)),mul(q(1,4),q(4)));
  assertEq(falseInvariance,q(-1),"different post-exit response");
  return {
    assumptions:"Each policy has independently identified stopped occupancy; same-world conditional residual value u_j is invariant across policies, including B orders/customer/operator response; separate physical approval.",
    single_stratum:{
      copy_known: str(ka),no_copy_known:str(kb),copy_exit:str(pa),no_copy_exit:str(pb),
      shared_contrast_interval:[str(all.lo),str(all.hi)],
      independently_subtracted_interval:[str(all.separateLo),str(all.separateHi)],
      each_endpoint_overlap_improvement:str(all.overlapGain),
      crossover_unsupported_contribution:"1/5",
      conditional_u_3_to_4:[str(calibrated.lo),str(calibrated.hi)]
    },
    identical_exit_occupancy_contrast:[str(identical.lo),str(identical.hi)],
    two_exit_strata:[str(two.lo),str(two.hi)],
    invalid_invariance_witness:str(falseInvariance),
    scoped_assertions:checks,
    empirical_claims:false,physical_approval:false,novelty_claim:false
  };
}
if(typeof module!=="undefined")module.exports={run};
if(typeof require!=="undefined"&&require.main===module)console.log(JSON.stringify(run(),null,2));
