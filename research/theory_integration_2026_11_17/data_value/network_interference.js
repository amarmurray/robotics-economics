"use strict";
/**
 * Network interference and shared recovery — exact finite synthetic diagnostic.
 * Units: normalized total accepted-service contribution; NOT dollars, benchmark percentage,
 * field measurements or a safety certificate.
 * No external dependencies. Run: node network_interference.js
 */
function runNetworkInterferenceTests() {
  let assertions = 0;
  const eps = 1e-11;
  function ok(condition, label) { assertions++; if (!condition) throw new Error("Assertion: "+label); }
  function near(actual, expected, label) { ok(Math.abs(actual-expected) < eps, label+" "+actual+" vs "+expected); }

  const baseline = 7, weightA = 0.7, gainA = 0.5;
  function selective(s, cost=0, w=weightA, gain=gainA) {
    return baseline + w*gain - (1-w)*s - cost;
  }
  const selectLower = selective(1.5), selectUpper = selective(-0.4);
  near(selectLower,6.90,"spillover lower");
  near(selectUpper,7.47,"spillover upper");
  near(selective(0),7.35,"independent pool original benchmark");
  near(selective(7/6),baseline,"zero cost sign threshold");
  near(selective((0.35-0.05)/0.3,0.05),baseline,"cost sign threshold");
  near(selective(1.5)-baseline,-.1,"adverse rollout");
  near(selective(-.4)-baseline,.47,"beneficial spillover");
  for(let i=0;i<=100;i++) {
    const s=-.4+1.9*i/100;
    const cost=.05*(i%5);
    near(selective(s,cost)-baseline, weightA*gainA-(1-weightA)*s-cost,"general spillover identity "+i);
    near(selective(s,cost) - selective(s,0), -cost,"incremental costs "+i);
  }
  for(let i=0;i<50;i++) {
    const s=-.4+1.9*i/49;
    const worse=Math.min(selective(-.4),selective(1.5));
    ok(selective(s)>=worse-eps,"interval bound "+i);
  }

  // Two alternative structural attributions, observationally equal in total output.
  const attributionA={qualChange:-0.6,orderChange:0};
  const attributionB={qualChange:0.2,orderChange:-0.8};
  near(attributionA.qualChange+attributionA.orderChange,-0.6,"qual-only total");
  near(attributionB.qualChange+attributionB.orderChange,-0.6,"demand-heavy total");
  ok(attributionA.qualChange!==attributionB.qualChange,"source attribution unidentified");

  const independent=[
    {u1:0,u2:0,p:.81},{u1:1,u2:0,p:.09},
    {u1:0,u2:1,p:.09},{u1:1,u2:1,p:.01}
  ];
  const disjoint=[
    {u1:0,u2:0,p:.8},{u1:1,u2:0,p:.1},
    {u1:0,u2:1,p:.1}
  ];
  function jointRecovery(table, cap=1){
    const valid=table.every(x=>x.p>=0 && x.p<=1);
    const total=table.reduce((s,x)=>s+x.p,0);
    const marg1=table.reduce((s,x)=>s+x.p*x.u1,0);
    const marg2=table.reduce((s,x)=>s+x.p*x.u2,0);
    const mean=table.reduce((s,x)=>s+x.p*(x.u1+x.u2),0);
    const peak=Math.max(...table.filter(x=>x.p>0).map(x=>x.u1+x.u2));
    return {valid, total, marg1,marg2,mean,peak,admissible:valid&&Math.abs(total-1)<eps&&peak<=cap};
  }
  const overlap=jointRecovery(independent), noOverlap=jointRecovery(disjoint);
  near(overlap.total,1,"joint probability total I");
  near(noOverlap.total,1,"joint probability total II");
  near(overlap.marg1,.1,"marg1 I");
  near(noOverlap.marg1,.1,"marg1 II");
  near(overlap.marg2,.1,"marg2 I");
  near(noOverlap.marg2,.1,"marg2 II");
  near(overlap.mean,.2,"expected load I");
  near(noOverlap.mean,.2,"expected load II");
  ok(overlap.peak===2 && overlap.admissible===false,"supported simultaneous recovery violates cap");
  ok(noOverlap.peak===1 && noOverlap.admissible===true,"disjoint support satisfies stated peak cap");

  // Exact finite population HT expectation, whole network rather than isolated pool.
  // Each independent network is a unit; only approved vectors are randomized.
  const networks=[
    {p:.2, y00:14, y10:14.7},
    {p:.8, y00:14, y10:13.5},
    {p:.45,y00:15, y10:16},
    {p:.6, y00:13.5,y10:14.1}
  ];
  let htExpected=0;
  for(const n of networks) {
    // Probability-weighted expectation of I(A=10)Y(10)/p(A=10).
    htExpected += (n.p*(n.y10/n.p)+(1-n.p)*0)/networks.length;
  }
  const actualMean=networks.reduce((s,n)=>s+n.y10,0)/networks.length;
  near(htExpected,actualMean,"whole network HT expectation");
  const baselineMean=networks.reduce((s,n)=>s+n.y00,0)/networks.length;
  near(actualMean-baselineMean,networks.reduce((s,n)=>s+n.y10-n.y00,0)/networks.length,"whole network paired mean");
  for (const n of networks) { ok(n.p>0 && n.p<1,"known positive approved network assignment"); }

  // Sequential stochastic target policy with the full history observed.
  function behaviorJoint(a0,a1){
    const p0=.5, p1given0=a0===0?.25:.75;
    return p0*(a1===1?p1given0:1-p1given0);
  }
  function targetJoint(a0,a1){return a1===1-a0?.5:0;}
  function acceptedContribution(a0,a1){return 7+.5*a0-.6*a1+.9*a0*a1;}
  let reweighted=0, direct=0, behaviorMass=0,targetMass=0;
  for(const a0 of [0,1]) for(const a1 of [0,1]){
    const p=behaviorJoint(a0,a1),pi=targetJoint(a0,a1);
    ok(p>0,"sequential behavior positivity");
    behaviorMass+=p;targetMass+=pi;
    reweighted+=p*(pi/p)*acceptedContribution(a0,a1);
    direct+=pi*acceptedContribution(a0,a1);
  }
  near(behaviorMass,1,"behavior mass");
  near(targetMass,1,"target mass");
  near(reweighted,direct,"history weighting");
  near(direct,6.95,"adaptive exact accepted contribution");
  ok(behaviorJoint(1,1)>0,"target support included");

  // A hard unsupported recovery branch cannot acquire value from an IPW comparison.
  function supported(behavior, target) { return target.every((p,i)=>p===0||behavior[i]>0); }
  ok(supported([.5,.5,0],[0,0,1])===false,"positivity failure flag");
  ok(supported([.5,.5,0],[1,0,0])===true,"supported policy flag");

  // Robust network choice, preserving old no-training and free-optional-data fallback.
  const robustUncertain=Math.min(selective(-.4),selective(1.5));
  const robustBounded=Math.min(selective(-.4),selective(.8));
  near(robustUncertain,6.9,"uncertain spillover lower bound");
  near(robustBounded,7.11,"tight measured bound");
  ok(Math.max(baseline,robustUncertain)===baseline,"retain old policy under broad uncertainty");
  near(Math.max(baseline,robustBounded),7.11,"selective route under supported tighter bound");
  for(let i=0;i<25;i++){
    const forced=baseline-(i+1)/100;
    ok(Math.max(baseline,forced)>=baseline,"optional old policy dominates forced worse retrain");
  }
  return {
    scope:"conditional synthetic network-level production, not calibration or safety signoff",
    assertions,
    selective:{baseline,independent:selective(0),sensitivity_set:[-.4,1.5],net_interval:[selectLower,selectUpper],zero_cost_spillover_cutoff:7/6,
      robust_old_when_uncertain:Math.max(baseline,robustUncertain),robust_mix_when_tighter:Math.max(baseline,robustBounded)},
    recovery:{identical_marginals:[overlap.marg1,overlap.marg2],identical_expected_total:overlap.mean,
      overlapping_supported_peak:overlap.peak, overlapping_peak_feasible:overlap.admissible,
      mutually_exclusive_peak:noOverlap.peak, mutually_exclusive_peak_feasible:noOverlap.admissible},
    identification:{ht_target_mean:actualMean,ht_design_expectation:htExpected,adaptive_target_value:direct,
      adaptive_ipw_value:reweighted,unidentified_mechanism:true},
    status:{field_data:false,verified_robot_safety:false,independent_review:false,full_repo_ci:false}
  };
}
const result=runNetworkInterferenceTests();
if(typeof console!=="undefined"&&typeof process!=="undefined"&&process.stdout) console.log(JSON.stringify(result,null,2));
result;
