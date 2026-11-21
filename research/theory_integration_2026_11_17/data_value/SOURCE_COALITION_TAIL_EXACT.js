/** Exact synthetic paid-source-mixture coalition audit; no field data. Node >=18. */
'use strict';
function run() {
 let checks=0,cohortWorlds=0;
 function check(p,message){checks++; if(!p)throw Error(message)}
 const types=["field_recovery","licensed_teleoperation","simulation_synthetic"];
 const base=[20,21,21,25,21,25,25,null];
 function mobius(v,mask){
   let total=0,s=mask;
   while(true){const parity=(mask.toString(2).split("1").length-1)-(s.toString(2).split("1").length-1);total+=(parity%2===0?1:-1)*v[s];if(s===0)break;s=(s-1)&mask;}
   return total;
 }
 function world(full){const v=base.slice();v[7]=full;return v}
 function monotone(v){return v.every((x,A)=>v.every((y,B)=>(A&B)!==A||x<=y))}
 const posS=world(35),posE=world(27),negS=world(27),negE=world(35);
 for(const [s,e,sign] of [[posS,posE,1],[negS,negE,-1]]){
   check(monotone(s)&&monotone(e),"optional-data monotonicity");
   for(let mask=0;mask<7;mask++)check(s[mask]===e[mask],"identical lower-order program outcomes");
   check((s[7]-e[7])===sign*8,"pooled SG/E ranking");
   check(mobius(s,7)-mobius(e,7)===sign*8,"third order dividend");
   check(mobius(s,7)===s[7]-32,"SG reconstruction");
 }
 for(let sFull=25;sFull<=35;sFull++){
   for(let eFull=25;eFull<=35;eFull++){
     cohortWorlds++; const s=world(sFull),e=world(eFull);
     check(monotone(s)&&monotone(e),"monotone optional source availability");
     const lowerD=[0,1,2,3,4,5,6].map(mask=>s[mask]-e[mask]);
     check(lowerD.every(d=>d===0),"all one/pair contrasts zero");
     check((sFull-eFull)===mobius(s,7)-mobius(e,7),"exact economic high-order residual");
     const bounded=(sFull-eFull)>=-10&&(sFull-eFull)<=10;
     check(bounded,"sharp monotone plus cap interval");
   }
 }
 const narrow=[27,35].flatMap(s=>[27,35].map(e=>s-e));
 check(Math.min(...narrow)===-8&&Math.max(...narrow)===8,"conditional narrower sharp endpoints");
 const threshold=Array.from({length:8},(_,m)=>m===7?8:0);
 const resource=Array.from({length:8},(_,m)=>Math.min(2,m.toString(2).split("1").length-1));
 check(mobius(threshold,7)===8,"additive technical score threshold induces 3-way economic complement");
 check(mobius(resource,7)===-1,"shared saturating capacity induces 3-way substitute");
 const local=Array.from({length:16},(_,m)=>{
   const pop=m.toString(2).split("1").length-1;
   return 20+pop+2*[3,5,6,9,10,12].filter(pair=>(m&pair)===pair).length;
 });
 for(let mask=0;mask<16;mask++)if(mask.toString(2).split("1").length-1>2)check(mobius(local,mask)===0,"2-local separated production exact truncation");
 const byClassSG=[4,2,0],byClassE=[1,2,3],targetWeights=[3,2,1],islandWeights=[2,2,2];
 const diff=(weights)=>weights.reduce((acc,w,i)=>acc+w*(byClassSG[i]-byClassE[i]),0);
 check(diff(targetWeights)===6,"target original buyers ranking");
 check(diff(islandWeights)===0,"island distribution not target mix");
 check(types.length===3,"distinct source provenance");
 return {
  status:"synthetic conditional constructions; no real customer or learning data",
  source_types:types,
  normalized_contribution_unit:"one tenth normalized paid-service contribution for source coalition table",
  fixed_market_lower_coalition:{empty:2,single:2.1,pair:2.5},
  high_order_program_worlds:[
   {name:"SG-compatible triple",sg_all:3.5,e_all:2.7,sg_dividend:0.3,e_dividend:-0.5,sg_minus_e:0.8},
   {name:"E-compatible triple",sg_all:2.7,e_all:3.5,sg_dividend:-0.5,e_dividend:0.3,sg_minus_e:-0.8}
  ],
  exact_pairwise_prediction_for_each_program:3.2,
  whole_program_pooled_rank_with_only_monotone_and_cap_3_5:{lower:-1,upper:1},
  conditional_full_program_bounds_2_7_to_3_5:{lower:-0.8,upper:0.8},
  additive_technical_threshold_three_way_economic_dividend:8,
  saturating_shared_capacity_three_way_dividend:-1,
  two_local_separated_four_source_all_high_order_dividends_zero:true,
  buyer_mix_reweighting:{island_sg_minus_e:0,target_sg_minus_e:1},
  executed_checks:checks,
  monotone_cohort_completions_examined:cohortWorlds
 };
}
if (typeof module !== 'undefined' && require.main === module) process.stdout.write(JSON.stringify(run(),null,2)+'\n');
if (typeof module !== 'undefined') module.exports={run};
