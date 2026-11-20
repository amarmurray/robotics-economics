"use strict";
const compute = function compute(){
  "use strict";
  let assertions=0;
  const eq=(a,b,why)=>{assertions++;if(a!==b)throw Error(why+": "+a+" != "+b);};
  const ge=(a,b,why)=>{assertions++;if(a<b)throw Error(why+": "+a+" < "+b);};
  // Payoffs are normalized captured-contribution HALF-units, not benchmark rates.
  // Equal-prior demand states are A and B; accuracy n/d >= one-half,
  // report arrives before permitted whole-policy choice.
  const R=[4,4], EA=[8,0], EB=[0,8], robust=[7,7];
  function gross(approvedPolicies,n,d){
    if(!approvedPolicies.length||2*n<d||n>d)throw Error("invalid menu or signal");
    const left=Math.max(...approvedPolicies.map(p=>n*p[0]+(d-n)*p[1]));
    const right=Math.max(...approvedPolicies.map(p=>(d-n)*p[0]+n*p[1]));
    // each payoff tick is 1/2 contribution unit; reports equally likely
    return (left+right)/(4*d);
  }
  const rows=[];
  for(let n=4;n<=8;n++){
    const a=n/8;
    const row={
      accuracy:a, retained:gross([R],n,8),
      single_source:gross([R,EA],n,8),
      paired_source:gross([R,EA,EB],n,8),
      independent_generalist:gross([R,robust],n,8),
      generalist_plus_paired:gross([R,robust,EA,EB],n,8)
    };
    eq(row.retained,2,"retained invariant");
    eq(row.single_source,1+2*a,"single source formula");
    eq(row.paired_source,4*a,"paired source formula");
    eq(row.independent_generalist,3.5,"robust independent");
    eq(row.generalist_plus_paired,Math.max(3.5,4*a),"robust alternative frontier");
    eq(row.paired_source-row.single_source,2*a-1,"paired source differential");
    rows.push(row);
  }
  // More choices cannot reduce optimized gross contribution. More informative
  // symmetric binary signals cannot reduce gross value for a fixed menu.
  let menu_checks=0;
  for(let x=0;x<=8;x++)for(let y=0;y<=8;y++){
    const added=[x,y],menu=[R,added];
    for(let n=4;n<=8;n++){
      ge(gross(menu,n,8),gross([R],n,8),"optional policy menu");
      if(n>4)ge(gross(menu,n,8),gross(menu,n-1,8),"Blackwell order");
      menu_checks++;
    }
  }
  const perfect=8,uninformative=4,d=8;
  const voi=menu=>gross(menu,perfect,d)-gross(menu,uninformative,d);
  const menu_complementarity=voi([R,EA,EB])-voi([R]);
  const menu_substitution=voi([EA,EB,robust])-voi([EA,EB]);
  eq(menu_complementarity,2,"specialist menu raises information value");
  eq(menu_substitution,-1.5,"generalist menu lowers information value");
  eq(gross([R,EA,EB],6,8),3,"perfectly paired 75% signal");
  eq(gross([R,robust,EA,EB],6,8),3.5,"generalist crowds out 75% signal");
  eq(gross([R,robust,EA,EB],7,8),3.5,"generalist boundary at 7/8");
  // If embodiment selection is irrevocable before the report, only one
  // specialist is available after the report (plus a *certified* R fallback).
  for(let n=4;n<=8;n++){
    const alpha=n/8;
    const locked=Math.max(gross([R,EA],n,8),gross([R,EB],n,8));
    eq(locked,1+2*alpha,"locked body with real post-report R fallback");
  }
  const prior_locked_no_fallback=Math.max(2,(EA[0]+EA[1])/4,(EB[0]+EB[1])/4);
  eq(prior_locked_no_fallback,2,"irrevocable body no post-report policy choice");
  const cost_package=0.6, cost_generalist=0.8;
  const net_rows=rows.map(row=>({
    accuracy:row.accuracy,
    retained:2,
    paired_grounded_specialist:row.paired_source-cost_package,
    independent_generalist:row.independent_generalist-cost_generalist,
    preferred:
      row.paired_source-cost_package>row.independent_generalist-cost_generalist?"paired-grounded-specialist":
      row.paired_source-cost_package<row.independent_generalist-cost_generalist?"generalist":"tie"
  }));
  eq(net_rows[2].preferred,"generalist","7/8 synthetic net choice"); 
  eq(net_rows[4].preferred,"paired-grounded-specialist","perfect-signal synthetic net choice");
  return {
    scope:"Finite two-regime, common original-market paid and qualified production; all policies hypothetically physically approved; no actual robotics data",
    units:"normalized captured-contribution units, not benchmark percentages or actual dollars",
    initial_approved_policy:"R=[2,2]",
    signal:"symmetric predecision target report with accuracy in [1/2,1], equal prior, unchanged original customer terms",
    policies:{retained:[2,2],specialist_A:[4,0],specialist_B:[0,4],generalist:[3.5,3.5]},
    formula_frontiers:{
      retained:"2",
      one_source_specialist_with_certified_retained_fallback:"1+2*alpha",
      paired_source_flexible_specialists:"4*alpha",
      independent_generalist:"7/2",
      generalist_and_paired_flexible_specialists:"max(7/2,4*alpha)",
      paired_vs_one_source:"2*alpha-1",
      generalist_screens_paired_target_grounding:"alpha<=7/8",
      packaged_vs_generalist_net_comparison:"4*alpha-C_package > 7/2-C_generalist"
    },
    rows,menu_interactions:{information_complement_from_specialists:menu_complementarity,information_substitution_from_generalist:menu_substitution},
    timing:{locked_specialist_with_certified_retained_option:"1+2*alpha",irreversible_pre_signal_choice_without_retained_dispatch:"2"},
    illustrative_once_only_costs:{paired_grounding_specialist:cost_package,generalist:cost_generalist},
    net_rows,
    checks:{assertions,optional_menu_and_signal_cases:menu_checks,independent_source_field_effect:false,physical_policy_approval:false,customer_payment_panel:false,november_22_gate_passed:false}
  };
};
const result = compute();
if (typeof console !== "undefined") console.log(JSON.stringify(result,null,2));
result;
