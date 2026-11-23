'use strict';
const assert=require('node:assert/strict');
let checks=0;
const eq=(a,b)=>{assert.equal(a,b);checks++;};
function pair(n,d){return `${n}/${d}`;}
// The same 60 equally weighted disturbances generate three *conditional* G changes.
let qualified=0, ordered=0, jobs=0, success=0;
for(let u=0;u<4;u++) for(let v=0;v<3;v++) for(let w=0;w<5;w++){
  const q=+(u!==0), d=+(v!==0), j=+(w===0), queue=Math.max(0,j);
  const paid=q*d*+(queue===0);
  qualified+=q;ordered+=d;jobs+=j;success+=paid;
  eq(queue,j);eq(paid,+(q===1&&d===1&&queue===0));
}
eq(qualified,45);eq(ordered,40);eq(jobs,12);eq(success,24);
const deltaNumerator=60-success;
eq(deltaNumerator,36);eq(success*5,60*2);
// Identical within-arm Q,D,J distribution, two different cross-arm potential-history couplings.
let sameMismatch=0,oppositeMismatch=0,pPaid=0,samePaid=0,oppositePaid=0;
for(let z=0;z<2;z++){
 const P={q:z,d:z,j:1-z},G0={q:z,d:z,j:1-z},G1={q:1-z,d:1-z,j:z};
 const f=x=>x.q*x.d*+(x.j===0);
 const a=f(P),b=f(G0),c=f(G1);
 sameMismatch+=+(a!==b);oppositeMismatch+=+(a!==c);
 pPaid+=a;samePaid+=b;oppositePaid+=c;
 eq(P.j+P.q,1);eq(G1.j+G1.q,1);
}
eq(sameMismatch,0);eq(oppositeMismatch,2);eq(pPaid,samePaid);eq(pPaid,oppositePaid);eq(pPaid,1);
// A second post-decision transition with mismatch cap 1/10; first-stage mismatch 3/5.
// The terminal accepted-service opportunity survives only if all requisite gates remain intact.
let terminal=0;
for(let u=0;u<4;u++)for(let v=0;v<3;v++)for(let w=0;w<5;w++)for(let k=0;k<10;k++){
 const q=+(u!==0),d=+(v!==0),j=+(w===0),j2=+(k===0);
 const workerQueue=Math.max(0,j+j2);
 const y=q*d*+(workerQueue===0);
 terminal+=y;
 eq(y,+(q===1&&d===1&&j===0&&j2===0));
}
eq(terminal,216);eq(600-terminal,384);
// The physical queue recursion is 1-Lipschitz in backlog plus job arrivals when worker service is shared.
for(let a=0;a<5;a++)for(let b=0;b<5;b++)for(let ja=0;ja<4;ja++)for(let jb=0;jb<4;jb++)for(let service=0;service<4;service++){
 const fa=Math.max(0,a+ja-service),fb=Math.max(0,b+jb-service);
 assert.ok(Math.abs(fa-fb)<=Math.abs(a-b)+Math.abs(ja-jb)); checks++;
}
const results={experiment:'conditional stage kernel and cross-world distinction',scope:'synthetic exact integer enumeration only',gate_counts:{one_date_paths:60,one_date_success:success,one_date_failures:deltaNumerator,two_date_paths:600,two_date_success:terminal,two_date_failures:600-terminal},stage_mismatch_caps:{qualification:'1/4',original_buyer_order:'1/3',recovery_job:'1/5'},composed_one_date_TV_envelope:'3/5',two_date_TV_envelope:'16/25',identical_marginals_crossworld:{same_coupling_discordance:'0',opposite_coupling_discordance:'1',both_within_program_paid_probability:'1/2'},queue_lipschitz_grid_cases:5*5*4*4*4,assertions:checks};
console.log(JSON.stringify(results,null,2));
