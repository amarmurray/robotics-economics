"use strict";
// Complete policy treatment-dependent interference: exact rational synthetic audit.
// Run: node network_policy_closure.js > network_policy_closure_results.json
const core = function core(){
  const gcd=(a,b)=>{a=a<0n?-a:a;b=b<0n?-b:b;while(b){const c=a%b;a=b;b=c;}return a||1n;};
  const F=(a,b=1n)=>{a=BigInt(a);b=BigInt(b);if(b===0n)throw Error("zero denominator");if(b<0n){a=-a;b=-b;}const g=gcd(a,b);return [a/g,b/g];};
  const add=(x,y)=>F(x[0]*y[1]+y[0]*x[1],x[1]*y[1]);
  const neg=x=>F(-x[0],x[1]);
  const sub=(x,y)=>add(x,neg(y));
  const mul=(x,y)=>F(x[0]*y[0],x[1]*y[1]);
  const div=(x,y)=>F(x[0]*y[1],x[1]*y[0]);
  const sum=xs=>xs.reduce((a,b)=>add(a,b),F(0));
  const eq=(x,y)=>x[0]===y[0]&&x[1]===y[1];
  const txt=x=>x[1]===1n?x[0].toString():`${x[0]}/${x[1]}`;
  const assert=(v,label)=>{if(!v)throw Error(label);checks++;};
  let checks=0;
  const old=[10,10,10,10].map(x=>F(x));
  const shared=[8,15,8,8].map(x=>F(x));
  const isolated=[F(23,2),F(23,2),F(23,2),F(23,2)];
  const eligOld=[5,5,5,5].map(x=>F(x));
  const eligNew=[7,7,7,7].map(x=>F(x));
  const mean=x=>div(sum(x),F(x.length));
  const oldMean=mean(old),sharedMean=mean(shared),isolatedMean=mean(isolated);
  const gainShared=sub(sharedMean,oldMean),gainIso=sub(isolatedMean,oldMean),gainEligible=sub(mean(eligNew),mean(eligOld));
  assert(eq(gainShared,F(-1,4)),"complete shared effect");
  assert(eq(gainIso,F(3,2)),"isolated complete effect");
  assert(eq(gainEligible,F(2)),"eligible-only contrast");
  assert(eq(sub(sharedMean,isolatedMean),F(-7,4)),"total shared-vs-isolated effect");
  // Four independent *whole-network* clusters, each assigned a complete approved policy at p=1/2.
  // Expected Horvitz-Thompson means are design-identifiable even with persistent internal learning.
  let hOld=F(0),hShared=F(0),assignmentVectors=0;
  for(let mask=0;mask<16;mask++){
    let treated=F(0),control=F(0);
    for(let i=0;i<4;i++){
      if(mask&(1<<i))treated=add(treated,mul(shared[i],F(2)));
      else control=add(control,mul(old[i],F(2)));
    }
    hShared=add(hShared,div(div(treated,F(4)),F(16)));
    hOld=add(hOld,div(div(control,F(4)),F(16)));
    assignmentVectors++;
  }
  assert(eq(hOld,oldMean),"HT control expectation");
  assert(eq(hShared,sharedMean),"HT shared expectation");
  assert(eq(sub(hShared,hOld),gainShared),"HT contrast");
  assert(assignmentVectors===16,"assignment enumeration");
  // Two-unit sharp bound: eligible direct gain +2; unsupported fallback baseline 5,
  // unsupported outcome [0,10], additional isolated cost 1/2.
  const lower=sub(add(F(2),sub(F(0),F(5))),F(1,2));
  const upper=sub(add(F(2),sub(F(10),F(5))),F(1,2));
  assert(eq(lower,F(-7,2))&&eq(upper,F(13,2)),"sharp unsupported bounds");
  assert(eq(sub(F(2),F(1,2)),F(3,2)),"verified isolation causal target");
  // Potential-interference union graph, not a status-quo realized graph.
  const nodes=["A","B","C","D"];
  const baseEdges=[[0,1]],targetOnlyEdges=[[1,2]];
  const components=(edges)=>{
    const p=nodes.map((_,i)=>i);
    const root=i=>{while(p[i]!==i)i=p[i];return i;};
    for(const [a,b] of edges){const x=root(a),y=root(b);if(x!==y)p[y]=x;}
    const groups=new Map();for(let i=0;i<nodes.length;i++){const r=root(i);if(!groups.has(r))groups.set(r,[]);groups.get(r).push(nodes[i]);}
    return [...groups.values()].sort((a,b)=>a[0].localeCompare(b[0]));
  };
  const baselineComponents=components(baseEdges),unionComponents=components([...baseEdges,...targetOnlyEdges]);
  assert(JSON.stringify(baselineComponents)===JSON.stringify([["A","B"],["C"],["D"]]),"baseline graph components");
  assert(JSON.stringify(unionComponents)===JSON.stringify([["A","B","C"],["D"]]),"policy union graph components");
  // Monotonicity only for optional access that preserves all feasible old policies.
  const max=(xs)=>xs.reduce((a,b)=>a[0]*b[1]>=b[0]*a[1]?a:b);
  assert(eq(max([F(10),F(8)]),F(10)),"optional menu preserves baseline");
  assert(eq(max([F(10),F(11)]),F(11)),"optional menu can improve");
  return {version:"2026-11-18",scope:"conditional exact arithmetic; complete policy reward; no customer/robot field measurement",
    inputs:{networks:4,old_whole_service:old.map(txt),grounding_shared_whole_service:shared.map(txt),grounding_isolated_after_cost:isolated.map(txt),eligible_old:eligOld.map(txt),eligible_grounding:eligNew.map(txt),assignment_probability:"1/2",isolation_incremental_cost:"1/2",unsupported_original_outcome:"5",unsupported_grounding_interval:["0","10"]},
    results:{old_mean:txt(oldMean),shared_mean:txt(sharedMean),isolated_mean:txt(isolatedMean),shared_minus_old:txt(gainShared),isolated_minus_old:txt(gainIso),eligible_only_gain:txt(gainEligible),shared_minus_isolated:txt(sub(sharedMean,isolatedMean)),unsupported_effect_after_cost_lower:txt(lower),unsupported_effect_after_cost_upper:txt(upper),HT_expected_shared:txt(hShared),HT_expected_old:txt(hOld),HT_expected_difference:txt(sub(hShared,hOld)),status_quo_components:baselineComponents,policy_union_components:unionComponents},
    assignment_vectors_enumerated:assignmentVectors,scoped_assertions:checks,
    limitations:["All payoffs are normalized synthetic complete service contribution, not task scores or dollar calibration.","Four independent complete interference networks are assumed, not four robots in one connected customer market.","No physical safety of any policy, isolation efficacy or transfer effect is inferred by enumerating assignments."]};
};
if (typeof module !== "undefined" && module.exports) module.exports={core};
if (typeof require !== "undefined" && typeof module !== "undefined" && require.main === module) process.stdout.write(JSON.stringify(core(),null,2)+"\n");
