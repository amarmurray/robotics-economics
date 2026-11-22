"use strict";
// Reproducible exact integer enumeration of a lawful pre-investment signal.
// Entire connected-cluster normalized accepted-and-cleared contributions.
// v entries are in tenths; no benchmark-to-dollar mapping or robot data.
const P=[[20,40],[15,50]]; // R retained; productive source pilot
const E=[[19,39],[22,45]]; // R after E capex; independent E capacity
let assertions=0, configurations=0;
function check(flag, label){assertions++;if(!flag)throw Error(label);}
function maxRow(rows,w,y){
  return Math.max(...rows.map(r=>w[0][y]*r[0]+w[1][y]*r[1]));
}
function values(n,d,k,m){
  if(!(d>0&&m>0&&n>=0&&n<=d&&k>=0&&k<=m))throw Error("bad probabilities");
  // theta=n/d, signal accuracy q=k/m; weights share denominator d*m.
  // w[z][y]=P(Z=z,Y=y)*d*m for exogenous Z before program assignment.
  const w=[[(d-n)*k,(d-n)*(m-k)],[n*(m-k),n*k]];
  const best=(rows,y)=>maxRow(rows,w,y);
  const p=best(P,0)+best(P,1),e=best(E,0)+best(E,1);
  const pre=best(P.concat(E),0)+best(P.concat(E),1);
  const post=Math.max(p,e);
  const no=Math.max(...P.concat(E).map(r=>((d-n)*r[0]+n*r[1])*m));
  return {pre,post,no,p_locked:p,e_locked:e,denominator:10*d*m};
}
const bayes=values(1,2,3,4);
check(bayes.pre===276&&bayes.post===268&&bayes.no===268,"pre/post signal numerator");
check(bayes.p_locked===265&&bayes.e_locked===268,"program-locked continuation");
check(bayes.denominator===80,"normalized denominator");
const low=values(1,4,3,4);
check(low.pre===444&&low.post===444&&low.no===444&&low.denominator===160,"theta=1/4 robust endpoint");
check(values(1,2,7,12).pre===values(1,2,7,12).no,"preinvestment accuracy boundary");
check(values(1,2,4,5).post===values(1,2,4,5).no,"late signal program switch boundary");
check(values(1,2,1,1).pre===72&&values(1,2,1,1).post===70,"perfectly observed pre/post signal");
for(let d=1;d<=16;d++)for(let n=0;n<=d;n++)
 for(let m=2;m<=12;m++)for(let k=Math.ceil(m/2);k<=m;k++){
   const v=values(n,d,k,m);
   check(v.pre>=v.post,"premature lock-in cannot improve informational value");
   check(v.post>=v.no,"optional signal cannot harm a fixed lawful program");
   check(v.pre>=v.no,"free optional report cannot reduce optimized value");
   if(k*2===m)check(v.pre===v.no&&v.post===v.no,"uninformative binary signal");
   configurations++;
 }
for(let m=2;m<=48;m++)for(let k=Math.ceil(m/2);k<=m;k++){
 const v=values(1,2,k,m);
 // Common denominator 20*m. These formulas follow from the row intersection
 // structure, not from a parameter sweep or presumed economics of robotics.
 check(v.pre===Math.max(67*m,60*m+12*k),"sharp early-report envelope");
 check(v.post===Math.max(67*m,55*m+15*k),"sharp late-report envelope");
}
const result={
  model:"one common preassignment network regime, lawful binary predecision signal",
  payment_rows_tenths:{P,E}, signal_accuracy:"3/4", prior_factor_prevalence:"1/2",
  before_investment:"69/20",after_investment_best_program:"67/20",
  without_signal_best_program:"67/20", P_locked_after_signal:"53/16",
  E_locked_after_signal:"67/20",report_timing_value:"1/10",
  gross_early_report_value_at_accuracy_q:"max(0,3q/5-7/20)",
  gross_late_report_value_at_accuracy_q:"max(0,3q/4-3/5)",
  accuracy_required_for_positive_early_value:"q>7/12",
  accuracy_required_for_positive_late_value:"q>4/5",
  robust_theta_interval:["1/4","3/4"],
  maximin_no_report:"111/40",maximin_with_free_optional_report:"111/40",
  largest_early_report_cost_at_q_3_4_for_Bayes_improvement:"1/10",
  configurations,assertions,
  synthetic:true,observed_paid_customer_data:false,confirmed_report_licenses:false,
  identified_joint_network_laws:false,scientific_novelty_claim:false
};
if(typeof module!=="undefined" && typeof require!=="undefined" && require.main===module)
 console.log(JSON.stringify(result,null,2));
