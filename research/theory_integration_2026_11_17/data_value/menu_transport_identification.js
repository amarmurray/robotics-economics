function runMenuTransportAudit(){
  const d=120; let checks=0;
  function assert(ok,msg){checks++;if(!ok)throw Error(msg);}
  const G2=(k)=>7*d+3*k; // G net in numerator units 1/(2*d)
  const E2=9*d;
  assert(G2(0)===7*d,"low-world natural response");
  assert(G2(d)===10*d,"high-world natural response");
  assert(G2(80)===E2,"natural menu switch threshold 2/3");
  let pairs=0;
  for(let contract=0;contract<=d;contract++) for(let eps=0;eps<=d;eps++){
    pairs++;
    const lo=Math.max(0,contract-eps),hi=Math.min(d,contract+eps);
    assert(lo<=contract&&contract<=hi,"identified interval includes C");
    assert(G2(lo)<=G2(hi),"economic bounds ordered");
    assert(Math.abs(lo-contract)<=eps&&Math.abs(hi-contract)<=eps,"endpoints satisfy sensitivity restriction");
    assert(G2(lo)===7*d+3*lo&&G2(hi)===7*d+3*hi,"economic endpoints constructible by Bernoulli laws");
  }
  const signal=[];
  for(let accuracy=60;accuracy<=d;accuracy++){
    // equal H/L prior, symmetric binary signal with q(H|+) = accuracy/d
    const expectedInfoNumerator=Math.max(E2,G2(accuracy))+Math.max(E2,G2(d-accuracy))-2*E2;
    const formula=Math.max(0,3*accuracy-2*d);
    assert(expectedInfoNumerator===formula,"signal Bayes EVSI exact");
    signal.push([accuracy,expectedInfoNumerator]);
  }
  for(let low=0;low<=d;low++){
    // maximin over p in [low/d,u/d], u>=low/d and prior uncertain.
    const robustNoInfo=Math.max(E2,G2(low));
    const robustWithPerfectSignal=E2+low;
    assert(robustWithPerfectSignal>=robustNoInfo,"information optionality under lower-prior bound");
    const explicit=low<=80?low:2*d-2*low;
    assert(robustWithPerfectSignal-robustNoInfo===explicit,"robust prior expression");
  }
  assert(G2(90)===1110&&E2===1080,"contract=1 epsilon=1/4 robust preference for G");
  assert(G2(60)===1020&&G2(60)<E2,"contract=0 epsilon=1/2 robust rejection of G");
  return {
    kind:"conditional synthetic original-market menu-transport audit",
    date_utc:"2026-11-20",
    assertions:checks,
    sharp_contract_sensitivity_grid_pairs:pairs,
    denominator_for_theta:120,
    normalization:"all contributions are hypothetical; G2(k) = 840+3k in units of 1/240; E2=1080",
    natural_high_group_response_worlds:{low:"0",high:"1",natural_G_net_low:"7/2",natural_G_net_high:"5",E_net:"9/2",switch_probability:"2/3"},
    contract_transport_example:{contract_high_response:"1",sensitivity:"1/4",natural_response_identified:"[3/4,1]",G_net_identified:"[37/8,5]",embodiment_net:"9/2",conditional_choice:"G only if joint G physically and legally admitted"},
    opposite_contract_example:{contract_high_response:"0",sensitivity:"1/2",natural_response_identified:"[0,1/2]",G_net_identified:"[7/2,17/4]",embodiment_net:"9/2",conditional_choice:"E"},
    signal_under_equal_prior:{accuracy:"3/4",gross_EVSI:"1/16",nonzero_only_if_accuracy_exceeds:"2/3",perfect_signal_gross_EVSI:"1/4"},
    robust_prior:{lower_p_zero:"0",perfect_signal_maximin_increment_at_zero:"0",lower_p_half:"1/2",perfect_signal_maximin_increment_at_half:"1/4"},
    field_trials:false,validated_menu_transport:false,signed_joint_G:false,observed_customer_panel:false,scientific_novelty_established:false
  };
}
if (typeof module !== 'undefined' && require.main === module) {
  process.stdout.write(JSON.stringify(runMenuTransportAudit(), null, 2) + '\n');
}
module.exports = {runMenuTransportAudit};
