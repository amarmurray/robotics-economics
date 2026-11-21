'use strict';
/* Conditional triple-dependence/qualified-production source-X versus grounded-G example.
   No real robot, buyer, or model-training data. Exact integers throughout.
   Run: node lineage_triple_policy.js > lineage_triple_policy_results.json */
function main() {
  let assertions=0, laws=0, candidatePolicies=0;
  function check(x,msg){assertions++;if(!x)throw new Error(msg);}
  function bitCount(x){let n=0;for(let i=0;i<3;i++)n+=(x>>i)&1;return n;}
  function signalWeight(mask,k){let m=bitCount(mask);
    if(m===0)return 112-k;
    if(m===1)return 32+k;
    if(m===2)return 16-k;
    return k;
  }
  function scorePolicy(p,k){
    let twiceNumerator=0;
    // Uniform theta. s=error if theta=0; s=(7 xor error) if theta=1.
    for(let e=0;e<8;e++){
      let w=signalWeight(e,k);
      if(((p>>e)&1)===0)twiceNumerator+=w;
      if(((p>>(7^e))&1)===1)twiceNumerator+=w;
    }
    return twiceNumerator; // probability correct = numerator/512.
  }
  let majority=0;for(let s=0;s<8;s++)if(bitCount(s)>=2)majority|=(1<<s);
  let cases=[];
  for(let k=0;k<=16;k++){
    let weights=Array.from({length:8},(_,i)=>signalWeight(i,k));
    check(weights.every(w=>w>=0),'negative mass');
    check(weights.reduce((a,b)=>a+b,0)===256,'law normalization');
    for(let i=0;i<3;i++){
      check(weights.reduce((z,w,mask)=>z+(((mask>>i)&1)?w:0),0)===64,'marginal wrong');
      for(let j=i+1;j<3;j++)check(weights.reduce((z,w,mask)=>z+(((mask>>i)&1)&&((mask>>j)&1)?w:0),0)===16,'pairwise wrong');
    }
    let majScore=scorePolicy(majority,k);
    check(majScore===416+4*k,'majority accuracy numerator');
    let best=0;
    for(let policy=0;policy<256;policy++){
      let score=scorePolicy(policy,k);if(score>best)best=score;
      check(score<=majScore,'majority not Bayes-optimal');
      candidatePolicies++;
    }
    check(best===majScore,'optimality');
    let xNet128=1264+10*k;
    let gNet128=1344, eNet128=1280, retained128=1216;
    check((xNet128-gNet128)===10*(k-8),'X-G difference');
    cases.push({k,triple_all_wrong_fraction:k+'/256',optimal_accuracy_fraction:(208+2*k)+'/256',x_net_fraction:xNet128+'/128',x_minus_g_fraction:(xNet128-gNet128)+'/128',preferred:xNet128>gNet128?'X':xNet128<gNet128?'G':'tie'});
    laws++;
  }
  const summary={
    status:'synthetic conditional exact model; no causal learner or paid production observations',
    fixed_assumptions:{signal_wrong_marginal:'1/4',signal_pair_wrong:'1/16',posterior_prior:'1/2 per customer regime',qualified_correct_capture:'12',wrong_but_fallback_capture:'2',source_X_cost:'1/4',grounding_G_accuracy:'7/8',grounding_G_cost:'1/4',certified_generalist_E_net:'10',old_one_signal_net:'19/2'},
    sharp_t_range:['0','1/16'],
    posterior_correct_range:['13/16','15/16'],
    source_X_net_range:['79/8','89/8'],
    grounding_G_net:'21/2',
    x_minus_g_range:['-5/8','5/8'],
    crossing_t:'1/32',
    independent_errors_t:'1/64',
    independent_errors_x_net:'163/16',
    endpoint_prior_equal_value_of_perfect_triple_audit:'5/16',
    audit_requirements:'same-target paired triple outcomes and true regime; independently supported physically signed complete production policy and original buyer payment needed for applied J',
    exhaustive_laws:laws,
    deterministic_3_signal_policies_per_law:256,
    policy_evaluations:candidatePolicies,
    integer_assertions:assertions,
    selected_cases:cases.filter(c=>[0,4,8,16].includes(c.k))
  };
  check((cases[0].x_minus_g_fraction)==='-80/128','lower choice gap');
  check((cases[16].x_minus_g_fraction)==='80/128','upper choice gap');
  check(cases[8].preferred==='tie','choice switch');
  check(cases[4].preferred==='G','independent conditional error world');
  summary.integer_assertions=assertions;
  return summary;
}
if(typeof module!=='undefined' && require.main===module) console.log(JSON.stringify(main(),null,2));
