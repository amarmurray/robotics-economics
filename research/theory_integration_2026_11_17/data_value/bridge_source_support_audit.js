"use strict";
/*
Source-origin versus fixed-archive inclusion: metadata-only exact audit.
No episodes, models, customer data, training, or robot access.
Run: node bridge_source_support_audit.js > bridge_source_support_results.json

Public publisher statements inspected 2026-11-20:
https://rail-berkeley.github.io/bridgedata/
https://github.com/rail-berkeley/bridge_data_v2
Counts are publisher metadata, not causal contrasts.
*/
function gcd(a,b) {
  a = a < 0n ? -a : a;
  b = b < 0n ? -b : b;
  while(b!==0n){const r=a%b;a=b;b=r;}
  return a===0n?1n:a;
}
function frac(n,d=1n) {
  n=BigInt(n);d=BigInt(d);
  if(d===0n)throw Error("zero denominator");
  if(d<0n){n=-n;d=-d;}
  const g=gcd(n,d);
  return {n:n/g,d:d/g};
}
function add(a,b){return frac(a.n*b.d+b.n*a.d,a.d*b.d);}
function mul(a,b){return frac(a.n*b.n,a.d*b.d);}
function neg(a){return frac(-a.n,a.d);}
function sub(a,b){return add(a,neg(b));}
function equal(a,b){return a.n===b.n && a.d===b.d;}
function str(a){return a.d===1n?String(a.n):String(a.n)+"/"+String(a.d);}
function assert(p,m){if(!p)throw Error(m);}
function supportBound(coveredWeight,coveredContrast) {
  // Bounded potential outcome in [0,1] => contrast in [-1,1].
  const missing=sub(frac(1),coveredWeight);
  return {lower:sub(mul(coveredWeight,coveredContrast),missing),
          upper:add(mul(coveredWeight,coveredContrast),missing)};
}
const pub={teleoperated:50365,scripted_pick_place:9731,total:60096,environments:24,skill_categories:13};
assert(pub.teleoperated+pub.scripted_pick_place===pub.total,"publisher composition");
const sourceShare=frac(pub.scripted_pick_place,pub.total);
const teleopShare=frac(pub.teleoperated,pub.total);
assert(equal(add(sourceShare,teleopShare),frac(1)),"source shares");
const rho=frac(1,13),d=frac(1);
const bounds=supportBound(rho,d);
const lowerWitness=add(mul(rho,d),mul(sub(frac(1),rho),frac(-1)));
const upperWitness=add(mul(rho,d),mul(sub(frac(1),rho),frac(1)));
assert(equal(bounds.lower,frac(-11,13)),"sharp lower");
assert(equal(bounds.upper,frac(1)),"sharp upper");
assert(equal(bounds.lower,lowerWitness)&&equal(bounds.upper,upperWitness),"attainability");
assert(equal(supportBound(frac(0),frac(0)).lower,frac(-1)),"no support lower");
assert(equal(supportBound(frac(0),frac(0)).upper,frac(1)),"no support upper");
assert(equal(supportBound(frac(1),frac(-1)).lower,frac(-1)),"full support");
assert(equal(supportBound(frac(1),frac(-1)).upper,frac(-1)),"point ID");
for(let k=0;k<=13;k++){
 const x=frac(k,13);
 const b=supportBound(x,frac(1));
 assert(equal(b.upper,frac(1)),"upper endpoint across support grid");
 assert(equal(b.lower,frac(2*k-13,13)),"lower endpoint across support grid");
}
const record={
  type:"metadata_only_exact_conditional_audit",
  checked_utc_date:"2026-11-20",
  publisher_metadata:pub,
  source_episode_shares:{scripted:str(sourceShare),teleoperated:str(teleopShare)},
  conditional_example_NOT_measured:{
    claim:"If at most 1 of 13 equally weighted skill-context generation comparisons has joint source-generation support, and that supported context has unit contrast, the whole-context mean source-generation contrast remains sign-unidentified.",
    eligible_generation_support_mass_at_most:str(rho),
    supported_effect_assumed:str(d),
    potential_outcomes_bounded:"[0,1]",
    exact_sharp_interval_if_covered_mass_equals_one_thirteenth:[str(bounds.lower),str(bounds.upper)],
    lower_witness_outside_contrast:"-1",
    upper_witness_outside_contrast:"+1",
    not_an_effect_of_scripted_training_on_other_tasks:true
  },
  code_checks:{publisher_count_sum:true,shares_sum_to_one:true,endpoint_witnesses:true,
    no_support_and_full_support:true,covered_mass_grid_cases:14},
  limitations:[
    "No episode hashes, sample or metadata manifest, split, model run, evaluation, customer receipts, or signed deployment",
    "The uniform 13-context distribution, coverage at one context and unit supported effect are explicitly hypothetical",
    "The source's pick-and-place-only script does NOT prevent cross-task transfer from that archived scripted source",
    "Training-inclusion contrasts require randomized learner/update components and held-out target evaluation, not task-level source generation overlap",
    "No numerical economic returns, episode-level license verification or independent novelty claim"
  ]
};
console.log(JSON.stringify(record,null,2));
