/* Conditional synthetic companion for ENDOGENOUS_DEMAND_PERSISTENT_TRANSFER.md.
Exact source generated from the same function executed in the connected JS runtime, 18 Nov 2026.
To replay with Node: node endogenous_demand_persistent_transfer.js
Do not interpret normalized payoff units as measured robot economics. */
function runAnalysis(){
  "use strict";
  const tol=1e-10, checks=[];
  const assert=(condition,label)=>{if(!condition)throw new Error(label);checks.push(label);};
  const close=(a,b)=>Math.abs(a-b)<tol;
  const cap=2;
  const scenarios={
    R:{H:{current:2,order:"B",terminal:12,qualified:true,reached:true,operator:2,report:"green"},
       L:{current:2,order:"S",terminal:1,qualified:false,reached:false,operator:1,report:"no-safe-B-support"}},
    G:{H:{current:-1,order:"B",terminal:8,qualified:true,reached:true,operator:2,report:"grounded"},
       L:{current:-1,order:"B",terminal:11,qualified:true,reached:true,operator:2,report:"grounded"}},
    E:{H:{current:-1.5,order:"B",terminal:9,qualified:true,reached:true,operator:1,report:"redesigned"},
       L:{current:-1.5,order:"B",terminal:9,qualified:true,reached:true,operator:1,report:"redesigned"}},
    S:{H:{current:3,order:"S",terminal:3,qualified:true,reached:true,operator:1,report:"specialist"},
       L:{current:3,order:"S",terminal:3,qualified:true,reached:true,operator:1,report:"specialist"}}
  };
  const val=(a,t,w=scenarios)=>w[a][t].current+w[a][t].terminal;
  for(const a of Object.keys(scenarios))for(const t of ["H","L"]){
    const x=scenarios[a][t];
    assert(x.operator<=cap,`pathwise-safe ${a}/${t}`);
    assert(x.order==="S"||x.qualified,`customer-accepted B only if qualified ${a}/${t}`);
    assert(x.order==="S"||x.reached,`B only if target supported ${a}/${t}`);
    assert(Number.isFinite(x.current)&&Number.isFinite(x.terminal),`finite-real-flows ${a}/${t}`);
  }
  const pay=Object.fromEntries(Object.keys(scenarios).map(a=>[a,{H:val(a,"H"),L:val(a,"L")}]));
  assert(close(pay.R.H,14)&&close(pay.R.L,3),"R full path");
  assert(close(pay.G.H,7)&&close(pay.G.L,10),"G full path");
  assert(close(pay.E.H,7.5)&&close(pay.E.L,7.5),"E full path");
  assert(close(pay.S.H,6)&&close(pay.S.L,6),"S full path");
  const l=2/5,u=3/5;
  const expectation=(a,p,w=scenarios)=>p*val(a,"H",w)+(1-p)*val(a,"L",w);
  const floor=a=>Math.min(expectation(a,l),expectation(a,u));
  const floors=Object.fromEntries(Object.keys(scenarios).map(a=>[a,floor(a)]));
  assert(close(floors.R,7.4)&&close(floors.G,8.2)&&close(floors.E,7.5)&&close(floors.S,6),"maximin pure lower endpoints");
  assert(floors.G>floors.E&&floors.E>floors.R&&floors.R>floors.S,"pure maximin rankings");
  const differences={
    RminusGatLower:expectation("R",l)-expectation("G",l),
    RminusGatUpper:expectation("R",u)-expectation("G",u),
    GminusEatLower:expectation("G",l)-expectation("E",l),
    GminusEatUpper:expectation("G",u)-expectation("E",u)
  };
  assert(close(differences.RminusGatLower,-1.4)&&close(differences.RminusGatUpper,1.4),"paired no dominance");
  assert(close(differences.GminusEatUpper,.7)&&close(differences.GminusEatLower,1.3),"G uniformly E in interval");
  const mixR=3/14,mixG=1-mixR;
  const mixH=mixR*val("R","H")+mixG*val("G","H");
  const mixL=mixR*val("R","L")+mixG*val("G","L");
  assert(close(mixH,8.5)&&close(mixL,8.5),"mix equalizer in both persistent regimes");
  for(const p of [l,.5,u]) assert(close(p*mixH+(1-p)*mixL,8.5),`mix flat at ${p}`);
  for(const a of Object.keys(scenarios)) assert(expectation(a,.5)<=8.5+tol,`dual upper at p=.5 ${a}`);
  const altered=JSON.parse(JSON.stringify(scenarios));
  altered.G.L.terminal=5;
  for(const t of ["H","L"]) assert(close(val("R",t,altered),val("R",t,scenarios)),`on-policy R observational invariance ${t}`);
  const lowG=Math.min(expectation("G",l,altered),expectation("G",u,altered));
  assert(close(lowG,5.2),"unobserved G response alternative changes maximin");
  assert(lowG<floors.E&&floors.G>floors.E,"opposite G/E ranking under identical R law");
  // Y is fair and independent of the same persistent latent theta; the market demands A-only or L-only skill.
  const coherent=p=>(p+(1-p))/2;
  const rectangular=(pOnA,pOnL)=>.5*pOnA+.5*(1-pOnL);
  for(const p of [.25,.5,.75]) assert(close(coherent(p),.5),`one-prior conditional law ${p}`);
  const rectVal=rectangular(.25,.75);
  assert(close(rectVal,.25),"splicing post-order priors reduces artificial value");
  assert(rectVal<coherent(.25),"nonrectangular gap positive");
  // Partial-regime payoff intervals yield conservative lower ranking bounds, not necessarily sharp.
  function pairLower(a,b,width){
    const dH=(val(a,"H")-width)-(val(b,"H")+width);
    const dL=(val(a,"L")-width)-(val(b,"L")+width);
    return Math.min(l*dH+(1-l)*dL,u*dH+(1-u)*dL);
  }
  assert(close(pairLower("G","E",0),.7),"coupled endpoint bound recovers exact comparison");
  assert(close(pairLower("G","E",.1),.5),"conservative interval outer bound penalizes both routes only once");
  return {model:"synthetic_two_period_persistent_regime_customer_production",assumptions:{latent:"one persistent H/L regime",p_interval:[l,u],operator_budget_per_supported_terminal_path:cap,normalization:"captured real contribution units; no source-derived dollars",qualified_old_policy_retained:true},paths:scenarios,values_by_regime:pay,pure_robust_floor:floors,paired_differences:differences,randomized_first_action:{R_fraction:mixR,G_fraction:mixG,H_value:mixH,L_value:mixL,robust_floor:8.5,requires:"ex ante fractional allocation/randomization feasible"},identification_countermodel:{on_policy_R_indistinguishable:true,G_L_alternate_terminal:5,G_alternate_robust_floor:lowG,G_vs_E_reversed:true},nonrectangularity:{coherent_full_law_worst:.5,spliced_rectangular_value:rectVal,splicing_invalid_for_common_regime_prior:true},interval_bound:{G_minus_E_width_0:pairLower("G","E",0),G_minus_E_width_point_1:pairLower("G","E",.1)},checks_passed:checks.length,check_labels:checks};
}
console.log(JSON.stringify(runAnalysis(),null,2));
