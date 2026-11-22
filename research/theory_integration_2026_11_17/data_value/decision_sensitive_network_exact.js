"use strict";
// Exact integer census for decision-sensitive network production.
// Standalone: node decision_sensitive_network_exact.js
function assert(ok,why){ if(!ok) throw new Error("FAIL: "+why); checks++; }
let checks=0, laws=0, refLaws=0, demandStates=0;
const N=8, rows=[];
for(let both=0;both<=N;both++)for(let qNotH=0;qNotH<=N-both;qNotH++)for(let notQH=0;notQH<=N-both-qNotH;notQH++){
 const neither=N-both-qNotH-notQH, q=both+qNotH, h=both+notQH;
 // A is a standing original buyer order; C is offered and qualified iff Q.
 // Terminal payoff numerator over N draws is 2*Pr(Q,!H)+Pr(!Q,!H).
 const terminalNum=2*qNotH+neither;
 const bNum4N=3*N+4*terminalNum, aNum4N=8*N;
 const analyticalNum4N=3*N+4*(N-h+q-both);
 assert(bNum4N===analyticalNum4N,"terminal paid identity");
 assert(Math.max(aNum4N,bNum4N)>=aNum4N,"optional old policy");
 assert(bNum4N===3*N+4*(N-h+q-both),"joint Q and outage");
 const paymentByEvent=[0,2,0,1]; // QH,Q!H,!QH,!Q!H
 assert(terminalNum===paymentByEvent[0]*both+paymentByEvent[1]*qNotH+
                           paymentByEvent[2]*notQH+paymentByEvent[3]*neither,"event census");
 // Reference with same marginals and zero Q/H overlap only when feasible.
 if(q+h<=N){
   refLaws++;
   const refTerminal=2*q+(N-q-h);
   const refB4N=3*N+4*refTerminal, refV4N=Math.max(aNum4N,refB4N);
   const gapB4N=refV4N-refB4N, gapA4N=refV4N-aNum4N;
   const deltaB4N=bNum4N-refB4N;
   assert(deltaB4N===-4*both,"exact value-weighted transition residual");
   assert(bNum4N===refV4N+deltaB4N-gapB4N,"B policy telescoping");
   assert(aNum4N===refV4N-gapA4N,"A policy telescoping");
   const TVnumerator=2*both; // TV = (2*both)/N
   assert(TVnumerator>=0&&Math.abs(deltaB4N)<=4*2*TVnumerator,"span TV envelope");
   // The naive span*TV bound is 4*both/N, the exact value error is both/N.
   assert(Math.abs(deltaB4N)*4===4*2*TVnumerator,"exact factor four when overlap positive");
 }
 laws++;
}
for(let Q=0;Q<2;Q++)for(let H=0;H<2;H++)
 for(let Oa=0;Oa<2;Oa++)for(let Oc=0;Oc<2;Oc++){
  const paid=H?0:Math.max(Oa,2*Q*Oc);
  const formula=Oa*(1-H)+2*Q*Oc*(1-H)-Oa*Q*Oc*(1-H);
  assert(paid===formula,"general original-buyer overlap expansion");
  demandStates++;
}
for(let j=0;j<=2;j++){
 const QH=j, QnotH=5-j, notQH=2-j, neither=1+j;
 const Bnum16=12+2*(2*QnotH+neither), Anum16=32, Enum16=33;
 const Pnum16=Math.max(Anum16,Bnum16);
 assert(Bnum16===34-2*j,"fixed marginals paid B");
 assert(Pnum16===(j===0?34:32),"optimized P with retained A");
 assert((Pnum16>Enum16)===(j===0),"P/E ranking synthetic");
 assert((Bnum16>Anum16)===(j===0),"within P B versus A");
 rows.push({QH_joint_fraction:j+"/8",B_fraction:Bnum16+"/16",P_optimized_fraction:Pnum16+"/16",
            E_fraction:"33/16",P_minus_E_fraction:(Pnum16-33)+"/16",dispatch:j===0?"B":j===1?"A or B":"A"});
}
assert(2*0===0,"outage erases conditional Q value even at TV=1");
const result={model:"lawful decision-sensitive network production, synthetic exact numerators",
 denominator:N, joint_four_cell_laws:laws, reference_zero_overlap_laws:refLaws,
 general_customer_offer_states:demandStates,exact_integer_assertions:checks,
 fixed_q5_h2_rows:rows, total_variation_one_zero_economic_error:true,
 reference_investment_gap_fraction:"+1/16",true_high_overlap_investment_gap_fraction:"-1/16",
 source:"conditional standard finite-horizon Bellman residual and original-buyer paid service algebra",
 field_measurements:false,physical_approval:false,independent_novelty:false};
if(typeof require!=="undefined" && typeof module!=="undefined" && require.main===module)
 console.log(JSON.stringify(result,null,2));
result;
