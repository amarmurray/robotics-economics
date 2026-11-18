"use strict";
// Finite response-type diagnostic for the integrated Q, omega, V, J framework.
// All payoffs are synthetic normalized *captured accepted-service contribution*.
// No robot benchmark rate, dollar valuation, or external dataset is implied.
const TYPES = [
  { id:"HD", h:1, d:1, R:13, G:7, E:6, S:5, recovery:{R:2,G:2,E:1,S:1} },
  { id:"H0", h:1, d:0, R:5, G:7, E:6, S:5, recovery:{R:2,G:2,E:1,S:1} },
  { id:"LD", h:0, d:1, R:5, G:9, E:6, S:5, recovery:{R:2,G:2,E:1,S:1} },
  { id:"L0", h:0, d:0, R:5, G:7, E:6, S:5, recovery:{R:2,G:2,E:1,S:1} }
];
const ROUTES = ["R","G","E","S"];
function check(condition, message){ if(!condition) throw Error(message); }
function close(a,b){return Math.abs(a-b)<1e-10;}
function distribution(t){check(t>=0 && t<=.5,"t outside Frechet");return [t,.5-t,.5-t,t];}
function expected(route,t){
 const q=distribution(t);
 return TYPES.reduce((a,k,i)=>a+q[i]*k[route],0);
}
function gap(t){return expected("R",t)-expected("G",t);}
function mix(x,t){check(x>=0&&x<=1,"x outside simplex");return x*expected("R",t)+(1-x)*expected("G",t);}
function oracle(t){return Math.max(...ROUTES.map(r=>expected(r,t)));}
function regret(x,t){return oracle(t)-mix(x,t);}
function jointFromSignal(m, sensitivity, falsePositive, pD=.5){
  check(sensitivity>falsePositive,"uninformative or inverse test");
  return (m-falsePositive*pD)/(sensitivity-falsePositive);
}
function lowerOnInterval(route,l,u){return Math.min(expected(route,l),expected(route,u));}
function pairedBounds(l,u){return {lower:gap(l),upper:gap(u)};}
function dualLowerAtType(k){return -2-2*k.d;}
function runModel(){
 let checks=0;
 function test(x,m){check(x,m);checks++;}
 test(TYPES.every(k=>Math.max(...Object.values(k.recovery))<=2),"base routes safe");
 for(let i=0;i<=100;i++){
   const t=i/200,q=distribution(t);
   test(close(q.reduce((a,b)=>a+b,0),1),"normalization");
   test(close(q[0]+q[1],.5)&&close(q[0]+q[2],.5),"H and D marginals");
   test(close(expected("R",t),5+8*t),"R formula");
   test(close(expected("G",t),8-2*t),"G formula");
   test(close(gap(t),-3+10*t),"paired gap");
   test(close(expected("E",t),6)&&close(expected("S",t),5),"alternatives");
   test(TYPES.every(k=>dualLowerAtType(k)<=k.R-k.G),"LP dual validity");
   test(close(mix(.2,t),7.4),"hedge equalization");
   test(oracle(t)>=7.4-1e-10,"oracle lower bound");
   test(close(pairedBounds(.36,.44).lower,.6),"audited R certificate");
   test(close(pairedBounds(.1,.22).upper,-.8),"audited G certificate");
   // Dual certificate -2 -2*P(D) = -3; attained at t=0.
 }
 let maxMin=-Infinity,bestX=null;
 for(let j=0;j<=1000;j++){
   const x=j/1000;
   const min=Math.min(mix(x,0),mix(x,.5));
   if(min>maxMin){maxMin=min;bestX=x;}
 }
 test(close(bestX,.2)&&close(maxMin,7.4),"maximin mixture optimum");
 test(close(Math.min(...ROUTES.map(r=>lowerOnInterval(r,0,.5)).filter(Number.isFinite)),5),"baseline sanity");
 test(close(Math.max(...ROUTES.map(r=>lowerOnInterval(r,0,.5))),7),"pure maximin 7");
 let minOracle=Infinity;
 for(let i=0;i<=1000;i++)minOracle=Math.min(minOracle,oracle(i/2000));
 test(close(minOracle,7.4),"oracle minimax is 7.4");
 test(close(minOracle-maxMin,0),"population-law oracle adds zero maximin value when fractional hedge feasible");
 test(close(minOracle-7,.4),"pure indivisible route benefits by 0.4");
 let minimaxRegret=Infinity, regretX=null;
 for(let j=0;j<=1000;j++){
    const x=j/1000;
    const loss=Math.max(regret(x,0),regret(x,.5));
    if(loss<minimaxRegret){minimaxRegret=loss;regretX=x;}
 }
 test(close(regretX,.4)&&close(minimaxRegret,1.2),"minimax regret differs from maximin");
 test(close(Math.max(regret(.2,0),regret(.2,.5)),1.6),"maximin hedge regret");
 test(close(Math.min(mix(.4,0),mix(.4,.5)),6.8),"regret policy guarantee");
 test(close(jointFromSignal(.34,.9,.1),.3625),"calibrated lower joint");
 test(close(jointFromSignal(.4,.9,.1),.4375),"calibrated upper joint");
 test(close(pairedBounds(0,.5).lower,-3)&&close(pairedBounds(0,.5).upper,2),"sharp no-coupling bounds");
 test(close(pairedBounds(.36,.44).upper,1.4),"audited upper");
 const safetyExample={
   budget:2,
   rare_bad_path_probability:1/10000,
   recovery_if_good:1,
   recovery_if_bad:3
 };
 safetyExample.expectedRecovery=(1-safetyExample.rare_bad_path_probability)*safetyExample.recovery_if_good+safetyExample.rare_bad_path_probability*safetyExample.recovery_if_bad;
 safetyExample.pathwiseFeasible=safetyExample.recovery_if_bad<=safetyExample.budget;
 test(safetyExample.expectedRecovery<2&&!safetyExample.pathwiseFeasible,"expected use does not establish hard support");
 const preAudit={
    known_marginals:{transfer_H:.5,registered_D:.5},
    unidentified_joint_t:[0,.5],
    routes:ROUTES.reduce((m,r)=>(m[r]={at_t0:expected(r,0),at_t_half:expected(r,.5),maximin:lowerOnInterval(r,0,.5)},m),{}),
    paired_R_minus_G:pairedBounds(0,.5),
    best_pure:{route:"G",worst_case:7},
    best_fractional:{routine_fraction:.2,grounding_fraction:.8,worst_case:maxMin},
    oracle_population_joint:{worst_case:minOracle,pure_upgrade:.4,fractional_upgrade:0},
    minimax_regret:{routine_fraction:regretX,worst_regret:minimaxRegret,guarantee:6.8,maximin_policy_regret:1.6},
    calibrated_report:{sensitivity:.9,false_positive:.1,observed_joint_Z_D:[.34,.4],implied_joint_H_D:[jointFromSignal(.34,.9,.1),jointFromSignal(.4,.9,.1)]},
    audited_R_favoring:{joint_interval:[.36,.44],paired_bounds:pairedBounds(.36,.44)},
    audited_G_favoring:{joint_interval:[.1,.22],paired_bounds:pairedBounds(.1,.22)}
 };
 return {model:"complete_response_type_coupled_identification",preAudit,safetyExample,checks,synthetic:true};
}
if(typeof module!=="undefined"){module.exports={TYPES,distribution,expected,gap,mix,oracle,regret,jointFromSignal,runModel};}
if(typeof require!=="undefined" && typeof module!=="undefined" && require.main===module){console.log(JSON.stringify(runModel(),null,2));}
