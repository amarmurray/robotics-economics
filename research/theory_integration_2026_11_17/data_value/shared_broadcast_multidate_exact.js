"use strict";
function pairedMultidateAudit(){
  "use strict";
  const states=Array.from({length:32},(_,i)=>({l:(i>>4)&1,w:(i>>3)&1,s1:(i>>2)&1,s2:(i>>1)&1,f:i&1}));
  const check=(ok,msg)=>{if(!ok)throw Error(msg);};
  let tableCases=0,assertions=0;
  function model(weights){
    const n=weights.reduce((a,b)=>a+b,0),m=[0,0],p=[0,0];
    for(let i=0;i<32;i++){const a=states[i],v=weights[i];if(a.l){m[a.w]+=v;p[a.w]+=v*a.f*(a.s1||a.s2);}}
    const formula=16*n+m.reduce((v,x,w)=>v+Math.max(0,8*p[w]-5*x),0);
    let direct=-Infinity;
    for(let mask=0;mask<4;mask++){let total=0;for(let i=0;i<32;i++){const a=states[i],pilot=a.l&&((mask>>a.w)&1);total+=weights[i]*(16+(pilot?(-5+8*a.f*(a.s1||a.s2)):0));}direct=Math.max(direct,total);}
    return {n,m,p,formula,direct,noReport:16*n+Math.max(0,8*(p[0]+p[1])-5*(m[0]+m[1]))};
  }
  const w=new Array(32).fill(0);
  function enumerate(k,left){if(k===31){w[k]=left;const v=model(w);check(v.formula===v.direct,"dynamic policy error");assertions++;check(v.formula>=v.noReport,"free report monotonicity error");assertions++;tableCases++;return;}for(let x=0;x<=left;x++){w[k]=x;enumerate(k+1,left-x);}}
  enumerate(0,3);
  function world(kind){const weights=new Array(32).fill(0);weights[1]=64;const pairs=kind==="diversified"?[[1,1,2],[1,0,1],[0,1,1]]:[[1,1,3],[0,0,1]];for(const [s1,s2,count] of pairs)for(const [f,fw] of [[0,1],[1,3]])weights[16+4*s1+2*s2+f]+=4*count*fw;return model(weights);}
  const diverse=world("diversified"),synchronized=world("synchronized");
  check(diverse.n===128 && synchronized.n===128,"mass");assertions++;
  check(diverse.formula===2112 && synchronized.formula===2048,"headline");assertions++;
  check(diverse.formula*16>65*4*diverse.n && synchronized.formula*16<65*4*synchronized.n,"E reversal");assertions++;
  check(diverse.m[0]===64 && synchronized.m[0]===64 && diverse.p[0]===48 && synchronized.p[0]===36,"joint counts");assertions++;
  check(diverse.noReport===diverse.formula && synchronized.noReport===synchronized.formula,"constant report");assertions++;
  return {synthetic_only:true,full_joint_32_state_tables:tableCases,exact_integer_assertions:assertions,source_checkpoint_probability:"1/2",site_marginal_eligibility_given_checkpoint:"3/4",operator_free_probability_given_checkpoint:"3/4",shared_one_slot:true,legal_report_atoms:2,diversified:{joint_site_overlap_conditional:"1/2",paid_event_unconditional:"3/8",whole_program:"33/8"},synchronized:{joint_site_overlap_conditional:"3/4",paid_event_unconditional:"9/32",whole_program:"4"},independent_embodiment_net:"65/16",scientific_gate:"OPEN",original_buyer_paid_measurements:false};
}
const result=pairedMultidateAudit();
if(typeof module!=="undefined"&&module.exports)module.exports={pairedMultidateAudit};
if(typeof require!=="undefined"&&require.main===module)console.log(JSON.stringify(result,null,2));
