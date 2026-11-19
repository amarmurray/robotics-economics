function runCheck() {
  const eps=1e-10;let checks=0;
  function ok(cond,label){if(!cond)throw Error("failed: "+label); checks++;}
  const S=0.75;
  const base=[[3,-1],[0,-6]], substitute=[[3,1],[0,-6]], complement=[[3,-1],[4,-6]];
  const best=(actions,p)=>Math.max(0,S,...actions.map(([h,l])=>p*h+(1-p)*l));
  const W=(actions,q)=>(best(actions,q)+best(actions,1-q))/2;
  const close=(a,b)=>Math.abs(a-b)<eps;
  ok(close(W(base,.5),1),"base no report");
  ok(close(W(base,1),15/8),"base perfect report");
  ok(close(W(substitute,.5),2)&&close(W(substitute,1),2),"substitution controller");
  ok(close(W(complement,.5),1)&&close(W(complement,1),19/8),"complement controller");
  ok(close((W(substitute,1)-W(substitute,.5))-(W(base,1)-W(base,.5)),-7/8),"negative interaction");
  ok(close((W(complement,1)-W(complement,.5))-(W(base,1)-W(base,.5)),1/2),"positive interaction");
  const costC=3/10,costI=9/10;
  const choices={retained:W(base,.5),report_only:W(base,1)-costI,admission_only:W(complement,.5)-costC,joint:W(complement,1)-costC-costI};
  ok(close(choices.report_only,39/40)&&close(choices.admission_only,7/10)&&close(choices.joint,47/40),"costed options");
  ok(choices.joint>Math.max(choices.retained,choices.report_only,choices.admission_only),"joint beats options");
  ok(close(W(complement,193/200)-costC-costI,1),"joint cost break even q");
  let minInteraction=Infinity,maxInteraction=-Infinity, priorB=-Infinity, priorC=-Infinity;
  for(let k=120;k<=240;k++){
    const q=k/240;
    const b=W(base,q),c=W(complement,q),u=W(substitute,q);
    const exactB=q<=9/16 ? 1 : 2*q-1/8;
    const exactC=q<=9/16 ? 1 : (q<=5/6 ? 2*q-1/8 : 5*q-21/8);
    ok(close(b,exactB),"base piecewise "+k);
    ok(close(c,exactC),"complement piecewise "+k);
    ok(close(u,2),"substitution piecewise "+k);
    ok(b>=1-eps && c>=1-eps && u>=2-eps,"information monotone "+k);
    ok(b>=priorB-eps && c>=priorC-eps,"Blackwell monotone "+k);
    priorB=b;priorC=c;
    const interaction=(c-W(complement,.5))-(b-W(base,.5));
    minInteraction=Math.min(minInteraction,interaction);maxInteraction=Math.max(maxInteraction,interaction);
  }
  ok(close(minInteraction,0)&&close(maxInteraction,.5),"complement interaction range");
  return {status:"passed",assertions:checks,grid_points:121,normalized:"whole-network captured accepted-service contribution",arms_perfect_information:{baseline_hidden:"1",baseline_disclosed:"15/8",substitute_hidden:"2",substitute_disclosed:"2",complement_hidden:"1",complement_disclosed:"19/8"},interaction:{substitution:"-7/8",complement:"1/2"},paid_options:{retain:"1",signal_only:"39/40",training_only:"7/10",combined:"47/40"},accuracy_threshold:{no_signal_value_begins:"9/16",new_target_action_activated:"5/6",paid_combination_break_even:"193/200"},interpretation:"synthetic economic responses; no robot/customer observation or independent novelty"};
}
if(typeof console!=="undefined") console.log(JSON.stringify(runCheck(),null,2));
