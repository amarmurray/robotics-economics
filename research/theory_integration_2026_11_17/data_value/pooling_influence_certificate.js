'use strict';
/** Conditional synthetic pooling influence audit; Node >=18. Not field estimates. */
function run(){
 let checks=0,grid=0;const check=(p,msg)=>{checks++;if(!p)throw Error(msg)};
 const H=8,pop=x=>x.toString(2).split("1").length-1,sgBase=[],eBase=[],sg=[],e=[];
 const sign=m=>(3-pop(m))%2===0?1:-1;
 for(let m=0;m<H;m++){sgBase[m]=550+120*pop(m);eBase[m]=150+120*pop(m);sg[m]=sgBase[m]+10*sign(m);e[m]=eBase[m]-10*sign(m);}
 const sub=(a,b)=>a.map((v,i)=>v-b[i]);
 const mobius=v=>Array.from({length:8},(_,i)=>sign(i)*v[i]).reduce((x,y)=>x+y,0);
 const truncated=v=>v[3]+v[5]+v[6]-v[1]-v[2]-v[4]+v[0];
 const nested=v=>v.every((x,A)=>v.every((y,B)=>((A&B)!==A)||x<=y));
 const diff=sub(sg,e);
 check(sg.every(x=>x>=0&&x<=1000)&&e.every(x=>x>=0&&x<=1000),"valid settled payoff range");
 check(nested(sg)&&nested(e),"optional-source value monotone under both programs");
 for(let m=0;m<8;m++){check(Math.abs(sg[m]-sgBase[m])===10,"SG kernel TV 0.01");check(Math.abs(e[m]-eBase[m])===10,"E kernel TV 0.01")}
 check(truncated(diff)===260,"observed source-pair extrapolation 0.26");
 check(diff[7]===420,"full source contrast 0.42");
 check(mobius(sg)-mobius(e)===160,"high-order contrast 0.16");
 check(diff[7]-truncated(diff)===160,"contrast identity");
 check(8*(10+10)===160,"generic source-tail TV bound");
 check(truncated(diff)-160===100,"positive lower investment certificate 0.10");
 const sActivation=sgBase.slice(),eActivation=eBase.slice();
 sActivation[7]+=10;eActivation[7]-=10;
 const dActivation=sub(sActivation,eActivation);
 check(truncated(dActivation)===400&&dActivation[7]===420,"activation-local experiment");
 check(mobius(sActivation)-mobius(eActivation)===20,"activation tail 0.02");
 check(nested(sActivation)&&nested(eActivation),"activation version optionality");
 const local=Array.from({length:8},(_,m)=>300+100*pop(m)),triple=local.slice();triple[7]+=100;
 check(local.slice(0,7).every((x,i)=>x===triple[i]),"all lower-coalition tests identical");
 check(mobius(triple)-mobius(local)===100,"missing triple can change full production by 0.10");
 check(nested(triple),"triple-only effect respects optional gross use");
 check(10000-(99*98)===298,"two-horizon product mismatch 0.0298");
 for(const bs of [0,5,10,15,20])for(const be of [0,5,10,15,20]){
  for(let mask=0;mask<256;mask++){
   const s=sgBase.map((x,i)=>x+bs*((mask>>i&1)?1:-1));
   const t=eBase.map((x,i)=>x-be*sign(i)),d=sub(s,t);
   check(Math.abs(d[7]-truncated(d))<=8*(bs+be),"uniform source-coalition tail for all sign patterns");
   grid++;
  }
 }
 check(grid===6400,"exact finite perturbation grid");
 return {
  classification:"conditional synthetic paid-customer theory; no robot field evidence",
  normalized_unit:"one thousandth of a binary accepted-and-settled complete-customer contribution",
  source_types:["field_and_recovery","licensed_teleoperation","simulation_and_synthetic"],public_pretrained_separate:true,
  bounded_kernel_lemma:{total_reward_range:1,one_step_program_tv_bound:"1/100",per_program_coalition_value_bound:"1/100",two_step_tv_example:"149/5000"},
  uniform_bound:{D2:"13/50",tail:"4/25",full_D:"21/50",identified_outer_D:["1/10","21/50"],sg_monotone:true,e_monotone:true},
  activated_only_all_sources:{D2:"2/5",tail:"1/50",full_D:"21/50",identified_outer_D:["19/50","21/50"]},
  invalid_empty_context_calibration:{all_lower_same:true,unobserved_three_way_paid_effect:"1/10",free_optional_value_preserved:true},
  exact_checks:checks,scoped_synthetic_perturbation_configurations:grid
 }
}
if (typeof module !== 'undefined' && require.main === module) process.stdout.write(JSON.stringify(run(),null,2)+'\n');
if (typeof module !== 'undefined') module.exports={run};
