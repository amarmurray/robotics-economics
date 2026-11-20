"use strict";
/* No dependencies. Node: node safe_fallback_selector_audit.js
   Synthetic exact finite-population algebra only; not a physical safety certificate. */
function assert(condition, label) { if (!condition) throw new Error(label); }
function run() {
  let assertions=0, feasibleTables=0, marginalTriples=0;
  function check(a,label) { assertions++; assert(a,label); }
  const D=8;
  for (let b=0;b<=D;b++) {
    for (let r=0;r<=b;r++) {
      for (let x=0;x<=b;x++) {
        marginalTriples++;
        const overlapLow=Math.max(0,r+x-b), overlapHigh=Math.min(r,x);
        const regressionLow=Math.max(0,r-x), regressionHigh=Math.min(r,b-x);
        const observedRegressions=[];
        for (let overlap=overlapLow;overlap<=overlapHigh;overlap++) {
          feasibleTables++;
          const lost=r-overlap, gained=x-overlap;
          observedRegressions.push(lost);
          check(gained-lost===x-r,"signed gain equals observable arm difference");
          check(lost>=regressionLow && lost<=regressionHigh,"regression bounds");
          check(gained>=0 && lost>=0,"nonnegative latent transitions");
          check(overlap+(r-overlap)+(x-overlap)+(b-r-x+overlap)===b,"four cells partition demand");
        }
        check(Math.min(...observedRegressions)===regressionLow,"sharp lower");
        check(Math.max(...observedRegressions)===regressionHigh,"sharp upper");
      }
    }
  }
  function moment(q) {return q.reduce((a,v)=>a+v,0);}
  function transitions(r,x) {
    let lost=0,gain=0,union=0;
    for(let i=0;i<r.length;i++){lost+=(r[i]===1&&x[i]===0)?1:0;gain+=(r[i]===0&&x[i]===1)?1:0;union+=(r[i]===1||x[i]===1)?1:0;}
    return {lost,gain,union};
  }
  const R=[1,1,0,0], nestedX=[1,1,1,0], crossedX=[0,1,1,1];
  const a=transitions(R,nestedX), b=transitions(R,crossedX);
  check(moment(R)===2 && moment(nestedX)===3 && moment(crossedX)===3,"equal arm marginals");
  check(a.lost===0 && a.gain===1 && a.union===3,"nested world");
  check(b.lost===1 && b.gain===2 && b.union===4,"crossed world");
  check(a.gain-a.lost===b.gain-b.lost && b.gain-b.lost===1,"identical expected gain");
  // Two original-buyer strata, each weight 1/2, B=1 on all 4 eligible cases:
  // A: R=2/4, X=3/4, v=8, extra variable cost 1/2 when selected
  // B: R=1/4, X=2/4, v=4, extra variable cost 0 when selected
  // Worst-case expected buyer qualification loss per full-stratum switch: 1/8 each.
  // Enumerate independent t_A,t_B in {0,1/4,1/2,3/4,1}.
  function gridOpt(capUnits) {
    let best=-Infinity,bestA=-1,bestB=-1,admissible=0;
    for(let i=0;i<=4;i++)for(let j=0;j<=4;j++){
      if(i+j>capUnits) continue;
      admissible++;
      // objective (3i+2j)/16; worst-case lost probability (i+j)/32
      const score=3*i+2*j;
      if(score>best){best=score;bestA=i;bestB=j;}
      check((i+j)<=capUnits,"risk budget");
    }
    return {cap_units_1_over_32:capUnits, max_gain_units_1_over_16:best, t_A_quarters:bestA,t_B_quarters:bestB, admissible};
  }
  const gridAtEighth=gridOpt(4), gridAtSixteenth=gridOpt(2);
  check(gridAtEighth.max_gain_units_1_over_16===12 && gridAtEighth.t_A_quarters===4 && gridAtEighth.t_B_quarters===0,"one eighth frontier");
  check(gridAtSixteenth.max_gain_units_1_over_16===6 && gridAtSixteenth.t_A_quarters===2 && gridAtSixteenth.t_B_quarters===0,"one sixteenth frontier");
  return {denominator:D,marginal_triples:marginalTriples,feasible_joint_tables:feasibleTables,exact_assertions:assertions,
    worlds:{incumbent_R_successes:2,upgraded_X_successes:3,optional_best_ex_ante_successes:3,nested:{...a},crossed:{...b}},
    frontier:{alpha_1_over_8:gridAtEighth,alpha_1_over_16:gridAtSixteenth},
    qualification_and_buyer_data_are_synthetic:true,physical_safety_certificate:false};
}
const result=run();
console.log(JSON.stringify(result,null,2));
