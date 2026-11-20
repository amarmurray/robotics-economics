// Exact synthetic original-network sequential-regime support diagnostic.
// Node.js: node sequential_source_policy_audit.js
// Conditional standard identification, NOT a robotics field experiment.
const audit = function audit() {
  "use strict";
  const checks=[];
  function eq(label,actual,expected){if(actual!==expected)throw new Error(`${label}: ${actual} != ${expected}`);checks.push(label)}
  const rows=[];
  for(const h of ["A","B"])for(const s of ["X","G"]){
    const q=s==="G"||h==="A";
    for(const a of (q?["deploy","keep"]:["keep"])){
      const p8=q?1:2; // P(H)=1/2, P(S)=1/2, P(A|Q)=1/2 when Q=1, else 1
      const gross=a==="deploy"?(s==="X"?5:4):2;
      rows.push({h,s,q,a,p8,w4:4*gross-1});
    }
  }
  eq("logging row probability totals eight eighths",rows.reduce((n,r)=>n+r.p8,0),8);
  function regime(s,options={}) {
    const matches=rows.filter(r=>r.s===s&&r.a===(r.q?"deploy":"keep"));
    const total8=matches.reduce((acc,r)=>acc+r.p8*(r.q?4:2)*r.w4,0);
    eq(`IPW ${s} is an integer numerator over 8`,total8%8,0);
    return total8/8; // result measured in quarter-unit ticks, already includes .25 source cost
  }
  const jX4=regime("X"), jG4=regime("G");
  eq("X policy quarter-unit ticks",jX4,13);
  eq("G policy quarter-unit ticks",jG4,15);
  eq("X source qualifies in exactly one of two customer regimes",rows.filter(r=>r.s==="X"&&r.q).reduce((n,r)=>n+r.p8,0),2);
  eq("G source qualifies in both regimes",rows.filter(r=>r.s==="G"&&r.q).reduce((n,r)=>n+r.p8,0),4);
  eq("qualified X nominal gross service beats qualified G",5>4,true);
  eq("full-policy G net beats X",jG4>jX4,true);
  // Removal of positive X/deploy support leaves its original-buyer production unobserved.
  const lowX4=(3+2)*2-1, highX4=(7+2)*2-1; // 4*[(source-X payoff+retained 2)/2 - 1/4]
  eq("low unsupported X policy ticks",lowX4,9);
  eq("high unsupported X policy ticks",highX4,17);
  eq("unsupported X endpoints reverse ranking against G",lowX4<jG4&&highX4>jG4,true);
  const report={
    study:"synthetic, pre-source randomized X/G; independently hypothetical physical whole-policy permission",
    original_parent_regimes:["A","B"],
    source_training_cost:"1/4 normalized production unit under both X and G",
    retained_policy_gross:"2 units, safe fallback before an unqualified new-policy attempt",
    source_X_qualification:"A only",
    source_G_qualification:"A and B",
    conditional_qualified_gross_X:5,
    conditional_qualified_gross_G:4,
    complete_policy_net_X:`${jX4}/4`,
    complete_policy_net_G:`${jG4}/4`,
    sequential_IPW_policy_contrast_G_minus_X:`${jG4-jX4}/4`,
    unsupported_X_deploy_gross_worlds:[3,7],
    unsupported_X_policy_net_identified_examples:[`${lowX4}/4`,`${highX4}/4`],
    complete_logging_rows:rows,
    assertions:checks
  };
  return report;
};
const result = audit();
console.log(JSON.stringify(result, null, 2));
