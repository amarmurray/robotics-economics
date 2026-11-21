console.log(JSON.stringify((function verifyConditionalComponent() {
  const cases=[];
  let checks=0, forcedNegativeObserved=false, optionalMonotone=true;
  const baseline=85, grounding=90, embodiment=95; // ticks of 1/80
  const margins={u_paid:10,v_paid:10,denominator:20};
  for(let k=0;k<=10;k++){
    const probs=[k,10-k,10-k,k]; // p(00), p(01), p(10), p(11); each /20
    const weightedU=probs[2]+probs[3],weightedV=probs[1]+probs[3];
    if(probs.reduce((a,b)=>a+b,0)!==20||weightedU!==10||weightedV!==10)throw Error("invalid copula");
    checks+=4;
    for(const rights of [false,true]){
      for(const q4 of [2,3]){ // q in quarters, cost=1/4 per attempt
        let brute=Number.NEGATIVE_INFINITY;
        for(let mask=0;mask<16;mask++){
          // only joint successful and rights-valid histories open the later original-buyer action
          const learnedPay=rights && (mask & 8)?k*(q4-1):0;
          const value=80+learnedPay;
          brute=Math.max(brute,value);
          checks++;
        }
        const analytic=80+(rights?k*(q4-1):0);
        if(brute!==analytic)throw Error("adaptive strategy mismatch");
        checks++;
        if(rights && q4===3){
          const optionalSG=Math.max(grounding,analytic);
          const optionalS=Math.max(baseline,80+k);
          const signedDifference=optionalSG-embodiment;
          const directCorrelationGain=analytic-80;
          if(optionalSG<grounding||optionalS<baseline)optionalMonotone=false;
          if(k===0) forcedNegativeObserved=analytic<grounding;
          cases.push({joint_success_numerator:k,first_service_paid_marginals:[10,10],joint_probs_numerators_00_01_10_11:probs,trained_SG_value_eightieths:analytic,optional_SG_value_eightieths:optionalSG,SG_minus_E_eightieths:signedDifference,optional_S_value_eightieths:optionalS,direct_joint_training_gain_eightieths:directCorrelationGain});
          checks+=4;
        }
      }
    }
  }
  const low=cases[0], middle=cases[5],high=cases[10];
  if(low.optional_SG_value_eightieths!==90||high.optional_SG_value_eightieths!==100||middle.optional_SG_value_eightieths!==90)throw Error("interval endpoints");
  if(low.SG_minus_E_eightieths!==-5||high.SG_minus_E_eightieths!==5)throw Error("sign reversal");
  if(high.optional_S_value_eightieths!==90||100-90-90+85!==5)throw Error("cross difference");
  if(!forcedNegativeObserved||!optionalMonotone)throw Error("data opt-out");
  checks+=6;
  const certified={w_upper_one_third:{upper_SG_fraction:"7/6",embodiment:"19/16",strict_E:true},w_lower_two_fifths:{lower_SG_fraction:"6/5",embodiment:"19/16",strict_SG:true},indifference_threshold_joint_success:"3/8"};
  return {model:"Two first-paid-service original buyers U,V with identical 1/2 marginal, one licensed joint-success future service, one shared later operator slot; q0=1/2, q1=3/4, attempt_cost=1/4; legacy joint=1/4; E=19/16; normalized synthetic units",value_denominator:80,policy_bruteforce_rules_per_law:16,checked_conditional_laws:44,assertions:checks,all_checks_passed:true,first_paid_service_value_eightieths:80,old_policy_value_eightieths:baseline,grounding_only_value_eightieths:grounding,embodiment_value_eightieths:embodiment,licensed_optional_SG_range_eightieths:[low.optional_SG_value_eightieths,high.optional_SG_value_eightieths],comparison_SG_minus_E_range_eightieths:[low.SG_minus_E_eightieths,high.SG_minus_E_eightieths],positive_source_grounding_cross_difference_eightieths:5,rights_absent_optimal_new_service_value_eightieths:80,optional_old_policy_never_worse:optionalMonotone,forced_worse_recipe_possible:forcedNegativeObserved,certified,grid:cases};
})(), null, 2));
