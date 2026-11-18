"use strict";
/* Exact conditional certification and audit precision for the existing synthetic serial-admission model.
   The confidence calculation is ONE-SIDED, zero events, independent predeclared supported cells.
   An observed event must be PROVED to dominate the C1 joint-coupling mismatch.
   Not a physical robotics safety test, field estimate or novel probability result. */
function missingPathThreshold(margin,wholeServiceRange){if(!(margin>0&&wholeServiceRange>0))throw Error("invalid");return margin/wholeServiceRange}
function oneSidedZeroUpper(n,alpha=.05,k=1){if(!(Number.isInteger(n)&&n>0&&alpha>0&&alpha<1&&Number.isInteger(k)&&k>=1))throw Error("invalid");return 1-Math.pow(alpha/k,1/n)}
function minZeroTrialsStrict(epsilon,alpha=.05,k=1){if(!(epsilon>0&&epsilon<1))throw Error("invalid");let n=Math.floor(Math.log(alpha/k)/Math.log(1-epsilon))+1;while(oneSidedZeroUpper(n,alpha,k)>=epsilon)n++;while(n>1&&oneSidedZeroUpper(n-1,alpha,k)<epsilon)n--;return n}
function lowerSerial({base=7.09675,unmeasuredRange=3,controllerTriggerUpper=0,marketTriggerUpper=0,otherLoss=0}){return base-unmeasuredRange*Math.min(1,controllerTriggerUpper+marketTriggerUpper)-otherLoss}
function independentZeroSurrogate({paths,n,alpha=.05}){return paths.map(x=>({...x,upper:oneSidedZeroUpper(n,alpha,paths.length)}))}
function runScopedChecks(){
const threshold=missingPathThreshold(67/4000,3);
if(Math.abs(threshold-67/12000)>1e-14)throw Error("wrong fraction");
if(minZeroTrialsStrict(threshold,.05,1)!==536)throw Error("one-stratum count");
if(minZeroTrialsStrict(threshold,.05,4)!==783)throw Error("four-strata count");
if(!(oneSidedZeroUpper(535,.05)>threshold&&oneSidedZeroUpper(536,.05)<threshold))throw Error("strict boundary");
if(!(oneSidedZeroUpper(782,.05,4)>threshold&&oneSidedZeroUpper(783,.05,4)<threshold))throw Error("four boundary");
if(!(lowerSerial({})>7.08))throw Error("baseline");
if(!(lowerSerial({controllerTriggerUpper:0,marketTriggerUpper:threshold})<=7.08+1e-12))throw Error("boundary");
if(!(lowerSerial({controllerTriggerUpper:0,marketTriggerUpper:1})<7.08))throw Error("unmeasured market path");
if(Math.abs(lowerSerial({controllerTriggerUpper:.002,marketTriggerUpper:.002})-7.08475)>1e-10)throw Error("two-path loss");
if(!(lowerSerial({controllerTriggerUpper:0,marketTriggerUpper:0,otherLoss:.0168})<7.08))throw Error("isolation-cost tradeoff");
for(let k=1;k<=10;k++)for(let n=1;n<=20;n++)if(!(oneSidedZeroUpper(n,.05,k)>=0&&oneSidedZeroUpper(n,.05,k)<=1))throw Error("range");
for(let k=1;k<=7;k++)if(!(minZeroTrialsStrict(threshold,.05,k)>=536))throw Error("bonferroni");
return 10+200+7;
}
const results = {
  "status": "synthetic_conditional_not_empirical",
  "source_date": "2026-11-18",
  "baseline_staged_lower": "7.09675",
  "assumed_specialist_upper": "7.08",
  "margin_exact": "67/4000",
  "whole_service_range": 3,
  "critical_omitted_probability_exact": "67/12000",
  "critical_omitted_probability": 0.005583333333333333,
  "one_stratum_zero_event_trials_95_percent": 536,
  "four_stratum_zero_event_trials_each_Bonferroni_95_percent": 783,
  "illustration_two_paths_each_0_002": 7.0847500000000005,
  "unknown_demand_path_even_if_controller_cut": 4.09675,
  "strict_inequality": "extra_cost + 3 * min(1,q_controller+q_market) < 67/4000",
  "validity": "Only under a complete-policy, same-regime, approved physical admission model; zero-event calculation requires independent replicated predeclared cells and provably dominating audited trigger; not live physical safety or identified causal coupling.",
  "scoped_function_checks": 217
};
if (typeof module!=="undefined" && require.main===module) {
  runScopedChecks();
  console.log(JSON.stringify(results,null,2));
}
if (typeof module!=="undefined") module.exports={missingPathThreshold,oneSidedZeroUpper,minZeroTrialsStrict,lowerSerial,runScopedChecks,results};
