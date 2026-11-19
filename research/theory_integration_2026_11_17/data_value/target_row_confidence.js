"use strict";
// Self-contained V8/Node.js conditional model; no physical experiments or external dependencies.
function calculate(){
 const pay={F:[0,0],S:[.75,.75],G:[3,-1],T:[4,-6]};
 const names=Object.keys(pay), rules=names.flatMap(a=>names.map(b=>[a,b])); let checks=0;
 const ok=(test,why)=>{checks++;if(!test)throw Error("check "+checks+" "+why)};
 const eq=(a,b)=>Math.abs(a-b)<1e-10;
 const V=(r,h,l)=>{let [a,b]=r;return .5*(h*pay[a][0]+(1-h)*pay[b][0]+l*pay[a][1]+(1-l)*pay[b][1])};
 const top=(h,l)=>rules.map(r=>({rule:r,value:V(r,h,l)})).sort((a,b)=>b.value-a.value)[0];
 const band=(k,n)=>{if(!n)return {low:0,high:1,radius:null};let radius=Math.sqrt(Math.log(80)/(2*n)),p=k/n;return {low:Math.max(0,p-radius),high:Math.min(1,p+radius),radius}};
 const floor=(r,h,l)=>{let [a,b]=r,dh=pay[a][0]-pay[b][0],dl=pay[a][1]-pay[b][1];return .5*(pay[b][0]+(dh>=0?h.low:h.high)*dh+pay[b][1]+(dl>=0?l.low:l.high)*dl)};
 ok(eq(top(.6,.4).value,43/40),"known rows 43/40");ok(eq(top(.6,.6).value,1),"no information");
 const cases=[];
 for(const n of [100,400,1600,2000]){
   const high=band(.6*n,n),low=band(.4*n,n),corner=[high.low,low.high];
   const gs=floor(["G","S"],high,low),g=floor(["G","G"],high,low);
   ok(eq(gs,.75+1.125*high.low-.875*low.high),"GS exact floor");
   ok(eq(g,1),"constant G");
   let selected,guarantee,certificate;
   const intersection=Math.max(high.low,low.low)<=Math.min(high.high,low.high);
   if(intersection){
      const q=Math.max(high.low,low.low);
      ok(eq(top(q,q).value,1),"uninformative permissible world"); selected=["G","G"];guarantee=1;certificate="uninformative admissible kernel";
   }else{
      const t=top(...corner);
      if(eq(t.value,1)&&eq(V(["G","G"],...corner),1)){selected=["G","G"];guarantee=1;certificate="G optimal at admissible corner";}
      else if(t.rule.join("")==="GS"&&eq(t.value,gs)){selected=["G","S"];guarantee=gs;certificate="G/S saddle at adverse corner";}
      else throw Error("Cannot prove randomized maximin at this corner");
   }
   for(const r of rules){
      ok(floor(r,high,low)<=V(r,...corner)+1e-10,"row floor <= fixed corner");
      ok(floor(r,high,low)<=guarantee+1e-10,"no rule can exceed certified upper");
   }
   ok(eq(floor(selected,high,low),guarantee),"attained robust certificate");
   cases.push({n_per_independent_pre_action_stratum:n,high_report_H_band:high,high_report_L_band:low,GS_lower:gs,robust_rule:selected,robust_value:guarantee,certificate});
 }
 ok(cases[0].robust_rule.join("")==="GG"&&cases[1].robust_rule.join("")==="GG","small samples");
 ok(cases[2].robust_rule.join("")==="GS"&&cases[3].robust_rule.join("")==="GS","large samples");
 ok(cases[2].robust_value>1&&cases[3].robust_value>cases[2].robust_value,"guarantee gain");
 const sample_threshold=Math.log(80)/(2*(.6/16)**2);
 ok(sample_threshold>1500&&sample_threshold<1600,"information threshold");
 const rshare=1/(1+Math.pow(.9,2/3));
 const bound=x=>1/Math.sqrt(x)+.9/Math.sqrt(1-x);
 ok(rshare>.51&&rshare<.53,"rare-high-opportunity audit");
 ok(bound(rshare)<bound(.1),"economic rather than prevalence proportion");
 for(let j=1;j<100;j++)ok(bound(rshare)<=bound(j/100)+1e-10,"KKT minimizes bound on grid");
 ok(eq(top(.6,.4).value,1.075)&&eq(top(.6,.6).value,1),"selected-label opposite economic optimum");
 return {scope:"synthetic fixed qualified whole-network customer service, no real target sample or safety approval",date:"2026-11-19",payoffs:pay,assumptions:"precommitted independent Bernoulli reports n per each original target opportunity state; family delta=.05 m=2",confidence_certificates:cases,known_target_value:43/40,known_target_rule:["G","S"],saddle_method:"known-kernel optimum at adversarial corner equals candidate's rectangular lower value",audit_bound_example:{pre_action_shares:[.1,.9],whole_service_spans:[10,1],economic_weights:[1,.9],rare_state_label_fraction:rshare,prevalence_fraction:.1,width_at_economic_allocation:bound(rshare),width_at_prevalence_allocation:bound(.1)},critical_n_per_row_for_positive_GS_lower:sample_threshold,selective_high_report_only_counterworld:{same_selected_report:"h",missing_original_opportunity_denominator:true,unselected_low_state_kernel_options:[.4,.6],optimized_original_population_values:[43/40,1]},deterministic_rules_at_fixed_certifying_kernel:rules.length,scoped_assertions:checks,not_identified:["physical qualification","real complete customer-order contribution","true target row confidence","site-level independence","source physical learning transfer","numerical BEA-BLS IO crosswalk","scientific novelty"]};
}
if(typeof require!=="undefined"&&typeof module!=="undefined"&&require.main===module)console.log(JSON.stringify(calculate(),null,2));
if(typeof module!=="undefined")module.exports={calculate};
