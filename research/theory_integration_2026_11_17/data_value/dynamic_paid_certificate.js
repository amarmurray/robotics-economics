"use strict";
/*
  Dynamic complete-policy paid-value certificate: synthetic exact-integer example.
  Units are twentieths for probabilities and costs and four-hundredths for expected value.
  No observed robotics data, customer revenue or field permission is represented.
  Run with: node dynamic_paid_certificate.js
*/
function run() {
  const H = 20;
  function solve(p,q,r,c,d,rights) {
    const future = rights ? Math.max(0,q-c) : 0;
    const recovery = Math.max(0,r-d);
    return p*(H+future)+(H-p)*recovery; // divide by 400
  }
  function policy(p,q,r,c,d,rights,train,rescue) {
    if(train && !rights) throw Error("unlicensed training policy");
    const success = H + (train ? q-c : 0);
    const failure = rescue ? r-d : 0;
    return p*success+(H-p)*failure;
  }
  function dual(p,q,r,c,d,rights,lambda) {
    const future = rights ? Math.max(0,q-c-lambda) : 0;
    const recovery = Math.max(0,r-d-lambda);
    // Future action consumes <=one unit of an ex-post robot/operator slot.
    // lambda*b (b=1) is included once, not as an economic cost.
    return H*lambda+p*(H+future)+(H-p)*recovery;
  }
  let assertions=0, cases=0, rightsCases=0, dualCases=0;
  function check(cond,detail) {
    assertions++;
    if(!cond) throw Error("exact assertion failed: "+detail);
  }
  for(let p=0;p<=H;p++)for(let q=0;q<=H;q++)for(let r=0;r<=H;r++){
    for(const c of [0,3,20])for(const d of [0,1,20]){
      const withRights=solve(p,q,r,c,d,true);
      const withoutRights=solve(p,q,r,c,d,false);
      check(withRights>=withoutRights,"free optional licensed data");
      for(const rights of [false,true]){
        cases++;
        const v=solve(p,q,r,c,d,rights);
        let optimizer=-Infinity;
        for(const train of (rights?[false,true]:[false]))
          for(const rescue of [false,true]){
            const value=policy(p,q,r,c,d,rights,train,rescue);
            check(value<=v,"supermartingale/value dominance");
            optimizer=Math.max(optimizer,value);
          }
        check(v===optimizer,"dynamic policy enumeration");
        for(const lambda of [0,1,5,20]){
          dualCases++;
          check(dual(p,q,r,c,d,rights,lambda)>=v,"resource price weak duality");
          if(lambda===0)check(dual(p,q,r,c,d,rights,lambda)===v,"zero-price sharp witness");
        }
        if(rights) rightsCases++;
      }
    }
  }
  const p=8,q=16,r=10,c=3,d=1;
  const root=solve(p,q,r,c,d,true);
  const strongerBuyer=solve(p,18,r,c,d,true);
  const noRights=solve(p,q,r,c,d,false);
  const naiveSum=H*p + H*(q-c) + H*(r-d);
  const embodiment=380;
  check(root===372,"signed dynamic ceiling 93/100");
  check(strongerBuyer===388,"uncertified future demand 97/100");
  check(noRights===268,"rights-restricted 67/100");
  check(naiveSum===600,"branch-double-count bound 150/100");
  check(solve(p,17,r,c,d,true)===embodiment,"future buyer threshold 17/20");
  check(root<embodiment && strongerBuyer>embodiment,"ranking counterworld");
  // Nonrectangular uncertainty: world A (p=.5,q=0), world B (p=0,q=1).
  // Rectangular stagewise recombination p=.5,q=1 is infeasible in either world.
  const actualWorldA=solve(10,0,0,0,0,true);
  const actualWorldB=solve(0,20,0,0,0,true);
  const rectangularUpper=solve(10,20,0,0,0,true);
  check(actualWorldA===200 && actualWorldB===0 && rectangularUpper===400,
    "rectangular hull can be conservative");
  // Endogenous initial paid-service occupancy x target grounding interaction:
  // p depends only on source x; later conditional q only on grounding g.
  const interaction=solve(12,16,10,3,1,true)-solve(12,10,10,3,1,true)
                    -solve(8,16,10,3,1,true)+solve(8,10,10,3,1,true);
  check(interaction===(12-8)*(16-10),"occupancy-times-grounding increasing differences");
  // Even with free optional access, x and g can instead be substitutes in q.
  // q00=0, q10=q01=q11=16 twentieths.
  const substitutive=solve(8,16,10,0,1,true)-solve(8,16,10,0,1,true)
                    -solve(8,16,10,0,1,true)+solve(8,0,10,0,1,true);
  check(substitutive===-128,"negative cross-effect with individual nonnegative options");
  return {
    model:"synthetic full-horizon original-buyer paid-service dynamic envelope",
    units:"integers /400 for expected service-equivalent contribution",
    allTestsPassed:true,
    assertions,cases,rightsCases,dualCases,
    inputs:{p_first_paid:"2/5",q_future_paid_conditional:"4/5",r_recovery_paid_conditional:"1/2",learning_and_grounding_cost:"3/20",recovery_cost:"1/20",licensed_use:true},
    policy_ceiling:{numerator:root,denominator:400},
    naive_sum_of_exclusive_branch_ceilings:{numerator:naiveSum,denominator:400},
    embodiment_comparator:{numerator:embodiment,denominator:400},
    high_future_demand_counterworld:{numerator:strongerBuyer,denominator:400},
    without_data_rights:{numerator:noRights,denominator:400},
    future_paid_threshold_for_tie:"17/20",
    source_occupancy_times_grounding_cross_difference:{numerator:interaction,denominator:400},
    optional_substitutive_technical_input_cross_difference:{numerator:substitutive,denominator:400},
    rectangular_hull_example:{max_actual_world:Math.max(actualWorldA,actualWorldB)/400,stagewise_recombined_upper:rectangularUpper/400},
    interpretation:"Conditional mathematics only. p, q, r are complete paid-service probabilities, not controller benchmark scores."
  };
}
if (typeof module !== "undefined" && typeof require !== "undefined" && require.main === module) {
  console.log(JSON.stringify(run(),null,2));
}
