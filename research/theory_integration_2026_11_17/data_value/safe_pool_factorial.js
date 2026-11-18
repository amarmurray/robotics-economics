"use strict";
/* Research-only, synthetic, 18 Nov 2026. No field claims. Node: node safe_pool_factorial.js */
function check(ok, message){ if(!ok) throw Error(message); }
function almost(a,b,tol=1e-11){ return Math.abs(a-b) <=tol; }
const observed={0:7,1:7.5,2:7.4};
function totalForCount(k,z){ return k===3 ? z : observed[k]; }
function bernoulliThree(x,z){
  return observed[0]*(1-x)**3+3*observed[1]*x*(1-x)**2+
         3*observed[2]*x*x*(1-x)+z*x**3;
}
function polynomialThree(x,z){return 7+1.5*x-1.8*x*x+(z-6.7)*x**3;}
function higherOrder(z){return z-3*observed[2]+3*observed[1]-observed[0];}
function fixedSaturation(k,z){return totalForCount(k,z);}
function targetValue(outcomeA,outcomeB,wA=0.7){
  return wA*outcomeA+(1-wA)*outcomeB;
}
function runModel(){
  const asserted={count:0};
  function A(ok,msg){check(ok,msg);asserted.count++;}
  A(almost(3*observed[2]-3*observed[1]+observed[0],6.7),"pair extrapolation");
  A(almost(higherOrder(6),-0.7),"negative third-order interaction");
  A(almost(higherOrder(9),2.3),"positive third-order interaction");
  for(const z of [6,6.7,7.5,9]){
    for(let i=0;i<=100;i++){
      const x=i/100;
      A(almost(bernoulliThree(x,z),polynomialThree(x,z)),"Bernoulli expansion "+z+"/"+i);
    }
    A(almost(bernoulliThree(0,z),7),"zero-R endpoint");
    A(almost(bernoulliThree(1,z),z),"three-R endpoint");
  }
  const xStar=(Math.sqrt(71)-6)/7, low=bernoulliThree(xStar,6);
  A(xStar>0 && xStar<1,"interior lower-world optimum");
  A(almost(1.5-3.6*xStar-2.1*xStar*xStar,0),"first-order condition");
  for(let i=0;i<=1000;i++){
    A(low+1e-10 >= bernoulliThree(i/1000,6),"global low-world Bernoulli maximum");
  }
  A(almost(low,7.27451687304294,1e-10),"low-world maximum independent check");
  A(almost(fixedSaturation(1,6),7.5),"safe one-R fixed saturation");
  A(fixedSaturation(1,6)>low,"fixed saturation outperforms Bernoulli under lower world");
  const unknownB={lower:5,upper:9},baseline=targetValue(7,7);
  const allMix=[targetValue(7.5,unknownB.lower),targetValue(7.5,unknownB.upper)];
  const selective=targetValue(7.5,7);
  A(almost(baseline,7),"baseline");
  A(almost(allMix[0],6.75)&&almost(allMix[1],7.95),"sharp transport interval");
  A(almost(selective,7.35),"selective safe policy");
  A(allMix[0]<baseline&&allMix[1]>selective,"unknown B changes ranking");
  A(selective>baseline,"selectively known A value");
  const threshold=0.7*(7.5-7);
  A(almost(threshold,0.35),"net differentiating implementation cost limit");
  const possibleTriple={lower:6,upper:9};
  A(possibleTriple.lower<7.5&&possibleTriple.upper>7.5,"three-way ambiguity reverses ranking");
  A(almost(7.5-6.7,0.8),"needed high-order contribution to outrank one-R");
  const result={
    synthetic:true,observed_per_pool:observed,triple_certified:false,
    high_order_coefficient_interval:[higherOrder(6),higherOrder(9)],
    pair_only_extrapolated_three_R:6.7,
    three_R_possible_contribution_interval:[6,9],
    triple_superiority_threshold:7.5,
    optimum_bernoulli_low_world:{routine_probability:xStar,contribution:low},
    safety_if_three_R_unapproved:"Independent Bernoulli assignment with x>0 has P(RRR)=x^3>0; exclude.",
    safe_fixed_one_R:7.5,
    target_with_A_weight_0_7:{
      baseline,all_mix_partial_identification:allMix,
      selective_mixed_A_pure_G_B:selective,
      maximum_additional_segmentation_cost_for_strict_advantage:threshold
    },
    checks:asserted.count,
    limits:"Arithmetic and finite countermodels only; no physical qualification, independent review, or field data."
  };
  return result;
}
if(typeof module!=="undefined" && require.main===module)
  console.log(JSON.stringify(runModel(),null,2));
