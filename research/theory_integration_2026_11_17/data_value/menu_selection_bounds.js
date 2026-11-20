"use strict";
// Exact finite-grid audit; Node: node menu_selection_bounds.js
function audit(){
  const D=24,Q=D*D;
  let groups=0,completions=0,assertions=0,G=0,E=0,unknown=0;
  function ok(cond,msg){assertions++;if(!cond)throw Error(msg)}
  for(let a=0;a<=D;a++)for(let b=0;b<=D;b++)for(let c=0;c<=D;c++){
    groups++;
    const L=Math.max(0,a*b-D*c),U=Math.min(Q,a*b+(D-a)*D+D*c);
    ok(L<=U,"ordered bounds");
    let min=Q,max=0;
    for(let d=0;d<=D;d++){
      completions++;
      const C=a*b+(D-a)*d,lo=Math.max(0,C-D*c),hi=Math.min(Q,C+D*c);
      ok(L<=lo && hi<=U,"completion contained");
      min=Math.min(min,lo);max=Math.max(max,hi);
    }
    ok(min===L&&max===U,"sharp endpoint");
    if(3*L>2*Q)G++;else if(3*U<2*Q)E++;else unknown++;
  }
  const base={a:18,b:24,c:3},lb=base.a*base.b-D*base.c, ub=Math.min(Q,base.a*base.b+(D-base.a)*D+D*base.c);
  const nonrespLb=lb+(D-base.a)*12;
  ok(lb===360&&ub===576,"base interval");
  ok(nonrespLb===432,"nonresponse audit interval");
  ok(3*lb<2*Q && 3*nonrespLb>2*Q,"audit changes robust comparison");
  ok(3*lb>0,"positive");
  const alpha=.05,n=400,h=Math.sqrt(Math.log(4/alpha)/(2*n));
  const auditedL=.75*Math.max(0,1-h)+.25*Math.max(0,.5-h)-.125;
  ok(auditedL>2/3,"joint Bonferroni audit screening");
  const blindL=.75*Math.max(0,1-h)-.125;
  ok(blindL<2/3,"respondent-only cannot rank");
  return {denominator:D,grid_parameters:groups,admissible_completions:completions,assertions,rankings:{G,E,unranked_or_boundary:unknown},examples:{respondents_all_yes_coverage_three_quarters_menu_epsilon_one_eighth:{theta_N_lower:"5/8",theta_N_upper:"1",G_net_lower:"71/16",E_net:"9/2"},nonrespondent_conditional_acceptance_lower_half:{theta_N_lower:"3/4",G_net_lower:"37/8"},hypothetical_two_stratum_sample:{n_each:n,alpha_joint:alpha,bonferroni_hoeffding_h:h,theta_N_lower:auditedL,G_net_lower:3.5+1.5*auditedL,respondent_only_theta_N_lower:blindL}},evidence:"synthetic math, not customer estimates"};
}
console.log(JSON.stringify(audit(), null, 2));
