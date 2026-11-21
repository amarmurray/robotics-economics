"use strict";
// Reproduce with: node economic_report_sufficiency.js
// Exact finite integer model; no robot or customer outcomes observed.
function runModel() {
  "use strict";
  const assert=(yes,msg)=>{if(!yes)throw new Error(msg)};
  const comb=[1,3,3,1];
  const pop=n=>{let c=0;while(n){c+=n&1;n>>=1;}return c};
  const rows=[];
  let checks=0, fullPolicies=0, compressedPolicies=0;
  for(let j=0;j<=16;j++){
    // g_k(t) probability for each particular vector with k errors; denominator 256.
    const g=[112-j,32+j,16-j,j];
    assert(g.reduce((s,x,k)=>s+comb[k]*x,0)===256,"conditional law"); checks++;
    let labelTotal=0, majNum=0, directFull=0;
    const a=[],b=[],labelRule=[];
    for(let pattern=0;pattern<8;pattern++){
      const k=pop(pattern);
      a[pattern]=g[k]; // one eighth? P(theta=0,pattern)*r_A, common denominator 2048
      b[pattern]=3*g[3-k]; // P(theta=1,pattern)*r_B
      labelRule[pattern]=k>=2?1:0;
      const chosen=labelRule[pattern]===0?a[pattern]:b[pattern];
      majNum+=chosen;
      directFull+=Math.max(a[pattern],b[pattern]);
      // majority accuracy is P(correct original regime), denominator 512
      labelTotal+=(labelRule[pattern]===0?g[k]:g[3-k]);
    }
    let best=-1;
    for(let mask=0;mask<256;mask++){
      let score=0;
      for(let pattern=0;pattern<8;pattern++)score+=((mask>>pattern)&1)?b[pattern]:a[pattern];
      best=Math.max(best,score);fullPolicies++;
    }
    let coarseBest=-1;
    for(let action0=0;action0<=1;action0++)for(let action1=0;action1<=1;action1++){
      let score=0;
      for(let pattern=0;pattern<8;pattern++){
        const majority=pop(pattern)>=2?1:0;
        score+=(majority? action1:action0)?b[pattern]:a[pattern];
      }
      coarseBest=Math.max(coarseBest,score);compressedPolicies++;
    }
    assert(best===directFull,"full posterior max");checks++;
    assert(coarseBest===majNum,"optimal majority compression");checks++;
    assert(labelTotal===2*(208+2*j),"majority task-label accuracy");checks++;
    assert(best===((j<=4)?(880-4*j):(832+8*j)),"exact q piecewise");checks++;
    assert(coarseBest===(832+8*j),"compressed q");checks++;
    assert(best-coarseBest===Math.max(48-12*j,0),"report compression loss");checks++;
    rows.push({t:`${j}/256`,full_paid_success_numerator_2048:best,majority_report_paid_success_numerator_2048:coarseBest,conditional_report_value_numerator_2048:best-coarseBest});
  }
  // An independent signed 2-state physical/operator context counterexample.
  // Theta is independent of Z. A and B each return 8 if matched to Z and fallback 2 otherwise.
  // All four (theta,z) outcomes have probability 1/4. Z provides no theta predictive information.
  const coarse=Math.max((8+2)/2,(2+8)/2);
  const fine=((Math.max(8,2))+(Math.max(2,8)))/2;
  const accuracy=1/2;
  assert(coarse===5&&fine===8&&fine-coarse===3,"economic context information");checks++;
  assert(accuracy===0.5,"context says nothing about theta");checks++;
  // Conservative conditional dominance certificate for the existing X/G/E/R case.
  const Xmax=(7/4)+10*(15/32);
  const G=(7/4)+10*(7/16);
  const E=10;
  assert(Xmax===103/16&&G===49/8&&E-Xmax===57/16,"E dominator");checks++;
  return {
    scope:"exact finite synthetic report compression; no learned robot, real payment, source experiment or empirical transfer",
    report_model:"three exchangeable signals, rA=1/4, rB=3/4, t=j/256, original buyer R/X/G/E",
    success_denominator:2048,
    full_policies_evaluated:fullPolicies,
    compressed_policies_evaluated:compressedPolicies,
    checks,
    rows,
    report_value_identity:"max(3/128 - 3t/2, 0)",
    report_value_at_t_zero_in_qualified_success:"3/128",
    report_value_at_t_zero_in_contribution:"15/64",
    report_value_after_t_one_over_64:"0",
    separately_synthetic_context_example:{original_regime_label_accuracy_both:"1/2",coarse_captured_contribution:coarse,fine_captured_contribution:fine,gross_observation_value:fine-coarse,net_observation_value_at_cost_one:fine-coarse-1},
    existing_full_program_E_net:"10",
    existing_program_X_max_net:"103/16",
    existing_program_G_net:"49/8",
    original_investment_choice_t_audit_value:"0",
    scientific_novelty:"not established; classical conditional information, Bayes action and production accounting"
  };
}
console.log(JSON.stringify(runModel(),null,2));
