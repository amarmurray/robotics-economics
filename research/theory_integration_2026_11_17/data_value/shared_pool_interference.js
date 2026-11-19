const result=(function sharedPoolInterferenceDiagnostic(){
"use strict";
let assertions=0;
function ok(condition,message){assertions++;if(!condition)throw Error(message);}
function reduced(a,b=1){let x=Math.abs(a),y=Math.abs(b);while(y){const t=x%y;x=y;y=t;}const g=x||1;return {numerator:a/g,denominator:b/g};}
// All money is computed in integer half-units. Baseline b=3 per fixed prepolicy site,
// new qualified incremental service v=4, costly source conversion k=5/2 per site,
// and optional physically qualified second slot E costs K=1 per shared pool.
// Pooled source information changes incremental complete-service contribution by ell
// only when both sites acquire X. No unapproved physical outcome is estimated.
const P={b2:6,v2:8,k2:5,K2:2};
function F2(q,e,ell2=0,parameters=P){
 if(![0,1,2].includes(q)||![0,1].includes(e)||ell2<0)throw Error("invalid portfolio");
 return 2*parameters.b2+parameters.v2*Math.min(q,1+e)+(q===2?ell2:0)-parameters.k2*q-parameters.K2*e;
}
function individual2(own,other,ell2=0,parameters=P){
 const q=own+other;
 return parameters.b2+(own?parameters.v2/q-parameters.k2+(q===2?ell2/2:0):0);
}
function D2(p,ell2=0,parameters=P){
 return (1-p)*(parameters.v2-parameters.k2)
     +p*(parameters.v2/2+ell2/2-parameters.k2);
}
function T2(ell2=0,parameters=P){
 return (F2(2,0,ell2,parameters)-F2(0,0,ell2,parameters))/2;
}
function cross2(e,ell2=0,parameters=P){
 return F2(2,e,ell2,parameters)-2*F2(1,e,ell2,parameters)+F2(0,e,ell2,parameters);
}
function expectedIndependent2(p,ell2=0,parameters=P){
 return (1-p)**2*F2(0,0,ell2,parameters)
       +2*p*(1-p)*F2(1,0,ell2,parameters)+p*p*F2(2,0,ell2,parameters);
}
const portfolios={none:F2(0,0),one_X:F2(1,0),two_X:F2(2,0),
 embodiment_only:F2(0,1),one_X_plus_E:F2(1,1),two_X_plus_E:F2(2,1)};
ok(JSON.stringify(portfolios)===JSON.stringify({none:12,one_X:15,two_X:10,embodiment_only:10,one_X_plus_E:13,two_X_plus_E:16}),"exact incumbent/one/two/body portfolio payoffs");
ok(individual2(1,0)===9&&individual2(0,1)===6&&individual2(1,1)===5&&individual2(0,0)===6,"exact site payoffs in half-units");
ok(D2(1/2)===1&&T2()===-1,"locally positive randomized direct effect, globally negative full-X contrast");
ok(D2(1/2)-T2()===2,"local minus global gap one whole unit");
ok(cross2(0)===-8&&cross2(1)===0&&cross2(1)-cross2(0)===P.v2,"capacity-only factorial identifies congestion component");
ok(F2(2,0,12)===22&&D2(1/2,12)===4&&T2(12)===5,"pooled-source complementarity reverses interference bias direction");
ok(expectedIndependent2(3/8)===13.125,"exact independent-saturation optimum in half-units");
ok(expectedIndependent2(1/2)===13,"independent half-saturation exact mean");
let cases=0;
for(let v2=2;v2<=16;v2+=2)for(let ell2=0;ell2<=16;ell2+=2)
for(let k2=0;k2<=12;k2++)for(let K2=0;K2<=6;K2+=2)
for(let n=0;n<=8;n++){
 const a={b2:6,v2,k2,K2},p=n/8;
 const d=D2(p,ell2,a),t=T2(ell2,a);
 const exact=(1-p)*(v2-ell2)/2;
 ok(d-t===exact,"local/full policy gap identity");
 ok(Math.abs(d-t)<=(1-p)*Math.abs(v2-ell2)/2,"sharp interference sensitivity envelope");
 ok(cross2(0,ell2,a)===ell2-v2&&cross2(1,ell2,a)===ell2,"source set interaction with and without body");
 ok(cross2(1,ell2,a)-cross2(0,ell2,a)===v2,"factorial operator congestion increment");
 ok(F2(0,0,ell2,a)===2*a.b2,"incumbent remains physically producible");
 ok(F2(2,0,ell2,a)+2*k2>=2*a.b2,"gross old production retained despite costly X");
 cases++;
}
const all=[
 ["none",portfolios.none],["one_X",portfolios.one_X],["two_X",portfolios.two_X],
 ["embodiment_only",portfolios.embodiment_only],["one_X_plus_E",portfolios.one_X_plus_E],
 ["two_X_plus_E",portfolios.two_X_plus_E]
];
all.sort((a,b)=>b[1]-a[1]);
ok(all[0][0]==="two_X_plus_E"&&all[0][1]===16,"best of six physically assumed portfolios");
return {
 schema:"cross-network shared-operator source-versus-embodiment synthetic diagnostic v1",
 provenance:"Self-contained mathematical synthetic example, not a field trial or source-calibrated payoff table.",
 unit:"Each integer tick denotes one half normalized complete-service contribution unit.",
 parameters:{per_site_baseline:reduced(3),source_increment:reduced(4),source_training_cost:reduced(5,2),second_qualified_slot_cost:reduced(1)},
 portfolio_total: Object.fromEntries(Object.entries(portfolios).map(([k,v])=>[k,reduced(v,2)])),
 best_qualified_investment:all[0][0],
 fixed_body_absent:{
  market_full_X_minus_G_per_site:reduced(T2(),2),
  Bernoulli_half_saturation_own_X_effect:reduced(D2(1/2),2),
  mixed_policy_mean_at_half_saturation:reduced(expectedIndependent2(1/2),2),
  independent_saturation_optimum_p:reduced(3,8),
  independent_saturation_optimum_total:reduced(expectedIndependent2(3/8)*8,16),
  shared_operator_set_interaction:reduced(cross2(0),2),
  capacity_added_set_interaction:reduced(cross2(1),2),
  exact_sensitivity_gap_at_p_half:reduced(D2(1/2)-T2(),2)
 },
 pooling_ell_6:{
  all_X_total:reduced(F2(2,0,12),2),
  local_direct_p_half:reduced(D2(1/2,12),2),
  full_X_minus_G_per_site:reduced(T2(12),2),
  source_set_interaction_with_one_slot:reduced(cross2(0,12),2),
  source_set_interaction_with_two_slots:reduced(cross2(1,12),2)
 },
 grid:{parameter_saturation_cases:cases,exact_assertions:assertions},
 restrictions:"Exactly two fixed prepolicy sites; safe unchanged baseline qualified recipes; one shared incremental-recovery slot, optional second independent qualified slot; fixed v,k,K,ell and demand; separable operator capacity effect; no model update leakage beyond the specified ell term.",
 unestablished:"No approved robotic intervention, observed original-order demand, measured learning synergy, verified operator exposure graph, customer contribution calibration, independent novelty review or whole-repository CI."
};
})();
if(typeof process!=="undefined"&&process.stdout)process.stdout.write(JSON.stringify(result,null,2)+"\n");
