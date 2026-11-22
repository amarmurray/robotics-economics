"use strict";
// A synthetic economic decision, NOT a trained model or original buyer record.
function runModel(){
 let n=0;
 const ok=(condition,label)=>{n++;if(!condition)throw Error(label)};
 const q=(theta,a)=>a==="R"?0.5:a==="E"?0.875:Number(theta===a);
 function W(alpha,menu,usable=true){
  let ans=0;
  for(const signal of (usable?["A","B"]:["missing"])){
   let best=-Infinity;
   for(const action of menu){
    let payoff=0;
    for(const theta of ["A","B"]){payoff+=0.5*(usable?(signal===theta?alpha:1-alpha):1)*q(theta,action);}
    best=Math.max(best,payoff);
   }
   ans+=best;
  }
  return ans;
 }
 const accuracies=[0.5,0.625,0.75,0.875,1],menus=[["R"],["R","A"],["R","A","B"],["R","A","B","E"]];
 for(const menu of menus)for(const low of accuracies){
  ok(W(low,menu,true)>=W(low,menu,false),"optional lawful signal");
  for(const high of accuracies)if(high>=low)ok(W(high,menu,true)>=W(low,menu,true),"more informative fixed menu");
 }
 for(let i=0;i<=16;i++){
  let r=i/64;
  ok((r+W(.75,["R","A","B"])>=-.125+W(1,["R","A","B"]))===(r>=.125),"receipt threshold");
 }
 const outcomes={
  productive_with_paid_receipt:.25+W(.75,["R","A","B"]),
  deliberate_with_acquisition_cost:-.125+W(1,["R","A","B"]),
  generalist_embodiment_with_cost:-.0625+W(.5,["R","E"],false),
  retained_baseline:W(.5,["R"],false),
  productive_if_no_current_receipt:W(.75,["R","A","B"]),
  deliberate_but_missing_B_qualification:-.125+W(1,["R","A"]),
  perfect_but_unusable_signal:W(1,["R","A","B"],false),
  report_accuracy_by_grounding_interaction:W(.75,["R","A","B"])-W(.5,["R","A","B"])-W(.75,["R"])+W(.5,["R"])
 };
 for(const [key,val] of Object.entries({productive_with_paid_receipt:1,deliberate_with_acquisition_cost:.875,generalist_embodiment_with_cost:.8125,retained_baseline:.5,productive_if_no_current_receipt:.75,deliberate_but_missing_B_qualification:.625,perfect_but_unusable_signal:.5,report_accuracy_by_grounding_interaction:.25})){ok(outcomes[key]===val,key)}
 return {description:"Entirely stipulated dyadic two-date accepted-and-finally-settled original-buyer production; NOT empirical robotics data",prior:{A:.5,B:.5},future_actions:["R","A","B"],reward_units:"normalized paid contribution",results:outcomes,thresholds:{P_vs_D_current_paid_receipt:.125,P_vs_E_current_paid_receipt:.0625},validation:{dyadic_assertions:n,scenarios_have_optional_retained_R:true,conditional_menus_and_rights_must_be_lawfully_supported:true}};
}
console.log(JSON.stringify(runModel(),null,2));
