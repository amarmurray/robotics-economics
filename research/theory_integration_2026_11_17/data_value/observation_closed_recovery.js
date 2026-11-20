// Conditional finite original-service example, not a signed safety controller.
function observe(s,type){if(s==="done")return "done";if(s==="alpha"||s==="beta")return type==="fine"?s:"retry";return s}

function recoveryWinner(B,t,type,universal=false,seen=new Map()){
 const key=JSON.stringify([B.slice().sort(),t,type,universal]);if(seen.has(key))return seen.get(key);
 const goal=B.length>0&&B.every(s=>s==="done");if(goal){seen.set(key,true);return true}if(t===0||B.some(s=>s==="fault")){seen.set(key,false);return false}
 const acts=universal?["ra","rb","u"]:["ra","rb"];
 for(const a of acts){const byObs=new Map();let good=true;
 for(const s of B){
  const ss=s==="done"?"done":a==="u"?"done":(a==="ra"&&s==="alpha")||(a==="rb"&&s==="beta")?"done":"fault";
  if(ss==="fault"){good=false;break}
  const o=observe(ss,type);if(!byObs.has(o))byObs.set(o,new Set());byObs.get(o).add(ss);
 }
 if(good&&[...byObs.values()].every(x=>recoveryWinner([...x],t-1,type,universal,seen))){seen.set(key,true);return true}
 }
 seen.set(key,false);return false;
}

function firstStepAdmissible(S,type,universal=false){
 const groups=new Map();for(const s of S){if(s==="fault")return false;const obs=observe(s,type);if(!groups.has(obs))groups.set(obs,new Set());groups.get(obs).add(s)}
 return [...groups.values()].every(B=>recoveryWinner([...B],1,type,universal))
}

function run(){
 const assert=(condition,message)=>{if(!condition)throw Error(message);checks++};let checks=0;
 assert(recoveryWinner(["alpha"],1,"coarse"),"alpha known");
 assert(recoveryWinner(["beta"],1,"coarse"),"beta known");
 assert(!recoveryWinner(["alpha","beta"],1,"coarse"),"hidden state action conflict");
 assert(recoveryWinner(["alpha","beta"],1,"coarse",true),"embodiment universal retry");
 assert(!firstStepAdmissible(["done","alpha","beta"],"coarse"),"coarse first step rejected");
 assert(firstStepAdmissible(["done","alpha","beta"],"fine"),"certified fine first step admitted");
 assert(firstStepAdmissible(["done","alpha","beta"],"coarse",true),"universal retry admits");
 assert(!firstStepAdmissible(["done","alpha","beta","fault"],"fine"),"physical fault rejects");
 let counts={coarse:0,fine:0,embodiment:0},n=0;
 const options=["done","alpha","beta"];
 for(let mask=1;mask<8;mask++){
  const S=options.filter((_,i)=>(mask&(1<<i))!==0);n++;
  for(const mode of Object.keys(counts)){if(firstStepAdmissible(S,mode==="fine"?"fine":"coarse",mode==="embodiment"))counts[mode]++;checks++}
  if(firstStepAdmissible(S,"coarse"))assert(firstStepAdmissible(S,"fine"),"refinement cannot shrink accepted set");
 }
 assert(counts.coarse===5&&counts.fine===7&&counts.embodiment===7,"acceptance subset counts");
 const v={R:4,X:4,G:4,E:4,XG:6,XE:5},interaction=v.XG-v.X-v.G+v.R;
 assert(interaction===2,"complementarity data observation & source route");
 assert(v.XG>v.XE&&v.XE>v.R,"conditional original-customer net comparisons");
 let n95=Math.ceil(Math.log(.05)/Math.log(.99));
 assert(n95===299,"binomial zero-failure n 95% for one-percent risk upper");
 return {model:"finite original-order information-consistent X-to-R recovery",root_outcomes:options,observation:{coarse:"alpha/beta indistinguishable",fine:"certified distinguishes alpha vs beta",noisy_99_percent:"same worst-case support as coarse, not robust admission"},universal_retry:"independently qualified embodiment spare",possible_x_first_step_subsets:n,admitted_subsets:counts,fully_supported_x_admitted:{coarse:false,fine:true,embodiment:true},physical_fault_always_rejected:true,synthetic_net_original_market_contribution:v,source_grounding_complementarity:interaction,zero_fault_trials_needed_for_iid_one_sided_95percent_upper_risk_at_most_one_percent:n95,assertions:checks};
}
console.log(JSON.stringify(run(),null,2));
