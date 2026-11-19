// Finite original-buyer offer support and policy-specific quality drift.
// Node.js, no dependencies. All amounts normalized synthetic contribution units.
"use strict";
function check(x,message){if(!x)throw Error(message)}
const status=(L,U,delta,offer)=>offer<=L-delta?"yes":offer>=U+delta?"no":"unknown";
const J=(a,b)=>({R:6,X:5+5*a,G:5+5*b,E:-1+5*(a+b)});
function enumerate({post=false}={}){
 const A=post?[8]:[5,6,7,8],B=post?[5]:[5,6,7,8];
 const shifts=[-1,0,1], bounds={R:[Infinity,-Infinity],X:[Infinity,-Infinity],G:[Infinity,-Infinity],E:[Infinity,-Infinity]};
 let cases=0;
 for(const wa of A)for(const wb of B)for(const da of shifts)for(const db of shifts){
   const v=J(Number(wa+da>=7),Number(wb+db>=7));
   for(const k of Object.keys(bounds)){bounds[k][0]=Math.min(bounds[k][0],v[k]);bounds[k][1]=Math.max(bounds[k][1],v[k]);}
   cases++;
 }
 return {cases,bounds};
}
const prior=enumerate(),audit=enumerate({post:true});
const w1=J(1,0),w2=J(0,1);
const result={model:"finite_original_buyer_quality_and_quote_support",date:"2026-11-19",prior,audit,
 baselineBands:{A:[5,9],B:[5,9],delta:1,posted:7,initialStatus:status(5,9,1,7)},
 targetAdditionalQuotes:{A:"accepted at 8",B:"refused at 6",A_status:status(8,9,1,7),B_status:status(5,6,1,7)},
 worlds:{A_wtp8_B_wtp5:w1,A_wtp5_B_wtp8:w2},
 twoWorldEqualPrior:{preReportBestExpected:7.5,postReportBestExpected:10,perfectReportGrossValue:2.5},
 physicalCap:{incumbentNet6:6,A_ifAcceptedGross5:5,B_ifAcceptedGross5:5,XfixedCost1:1,GfixedCost1:1,EfixedCost7:7,EupperNet:9},
 notes:["All buyer values and operator constraints are synthetic.","The audit is assumed accurate, costless and non-disruptive for reported gross value; real costs enter once.","This integer enumeration checks a general continuous-threshold analytical statement, not proves it."]};
check(prior.cases===144&&audit.cases===9,"count");
for(const [x,y] of [["R",[6,6]],["X",[5,10]],["G",[5,10]],["E",[-1,9]]])check(JSON.stringify(prior.bounds[x])===JSON.stringify(y),"prior "+x);
for(const [x,y] of [["R",[6,6]],["X",[10,10]],["G",[5,5]],["E",[4,4]]])check(JSON.stringify(audit.bounds[x])===JSON.stringify(y),"audit "+x);
check(w1.X===10&&w1.G===5&&w2.X===5&&w2.G===10,"reversal");
check(result.twoWorldEqualPrior.postReportBestExpected-result.twoWorldEqualPrior.preReportBestExpected===2.5,"EVPI");
check(result.targetAdditionalQuotes.A_status==="yes"&&result.targetAdditionalQuotes.B_status==="no","classification");
console.log(JSON.stringify(result,null,2));