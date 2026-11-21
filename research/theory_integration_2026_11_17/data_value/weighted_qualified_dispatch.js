/* Exact finite decision-table check for a conditional robotics economics model.
 * No external data, training, hardware or customer receipts; node >=16.
 * Run: node weighted_qualified_dispatch.js > weighted_qualified_dispatch_results.json
 */
function exactWeightedDispatch(){
  function popcount(n){let k=0;while(n){k+=n&1;n>>=1;}return k;}
  function check(condition,message){if(!condition)throw Error(message);}
  const rows=[];let policyChecks=0,pairwiseChecks=0;
  for(let j=0;j<=16;j++){
    const g=[112-j,32+j,16-j,j]; // each exact three-bit error cell, denominator 256
    const masses=[1,3,3,1];
    check(g.every(x=>x>=0),"negative atom");
    check(g.reduce((a,x,i)=>a+x*masses[i],0)===256,"total mass");
    check(g[1]+2*g[2]+g[3]===64,"single-error marginal");
    check(g[2]+g[3]===16,"pairwise-error moment");pairwiseChecks+=3;
    const optimum=Array.from({length:8},(_,b)=>Math.max(g[popcount(b)],3*g[3-popcount(b)])).reduce((a,b)=>a+b,0);
    let enumerated=-1,bestCount=0;
    for(let rule=0;rule<256;rule++){
      let value=0;
      for(let b=0;b<8;b++)value+=((rule>>b)&1)?3*g[3-popcount(b)]:g[popcount(b)];
      check(value<=optimum,"decision rule exceeds Bayes envelope");
      if(value>enumerated){enumerated=value;bestCount=1;}else if(value===enumerated)bestCount++;
      policyChecks++;
    }
    check(enumerated===optimum,"enumeration does not attain envelope");
    const majority=832+8*j;
    check(optimum>=majority,"optimal dispatch below majority");
    check(optimum===(j<=4?880-4*j:832+8*j),"piecewise algebra discrepancy");
    rows.push({t_fraction:`${j}/256`,technical_accuracy_numerator_256:208+2*j,majority_qualified_numerator_2048:majority,optimized_qualified_numerator_2048:optimum,optimal_rules_count:bestCount,relative_to_grounding_qualified_numerator_2048:optimum-896});
  }
  check(rows[0].optimized_qualified_numerator_2048===880,"left endpoint");
  check(rows[4].optimized_qualified_numerator_2048===864,"interior minimum");
  check(rows[8].optimized_qualified_numerator_2048===896,"grounding crossover");
  check(rows[16].optimized_qualified_numerator_2048===960,"right endpoint");
  check(rows[0].optimized_qualified_numerator_2048>rows[4].optimized_qualified_numerator_2048,"nonmonotonicity");
  check(rows[0].optimized_qualified_numerator_2048+rows[16].optimized_qualified_numerator_2048-2*rows[8].optimized_qualified_numerator_2048===48,"audit decomposition");
  check(7/4+10*(960/2048)<10,"unchanged E dominance");
  return {scope:"conditional synthetic source-error law and signed original-buyer contribution, NOT measured robots",q_denominator:2048,t_denominator:256,r_A:"1/4",r_B:"3/4",grounding_qualified:"7/16",retained_net:"7/4",embodiment_net:"10",policyChecks,pairwiseChecks,rows,sharp_qualified_interval:["27/64","15/32"],sharp_X_minus_G_qualified_interval:["-1/64","1/32"],sharp_X_minus_G_net_interval:["-5/32","5/16"],within_X_precommitment_perfect_t_audit_information_value:"15/128",complete_X_G_E_portfolio_audit_value:"0"};
}
console.log(JSON.stringify(exactWeightedDispatch(),null,2));
