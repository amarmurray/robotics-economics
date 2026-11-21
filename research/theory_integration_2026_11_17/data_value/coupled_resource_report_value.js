'use strict';
function coupledAudit(){
 const weights=[2,1,1], points=[];
 let assertions=0, lower=Number.POSITIVE_INFINITY, upper=-1, maxAt=[], worstAt=[];
 const fineRule=[0,1,0];
 const payoff=(k,y,a)=>{ const A=[96,48,64+k],B=[64+k,64+k,64]; return a===0?A[y]:B[y];};
 for(let k=0;k<=32;k++){
   let fine=0, coarseA=0,coarseB=0,rule=0;
   for(let y=0;y<3;y++){
     const a=payoff(k,y,0),b=payoff(k,y,1),w=weights[y];
     fine+=w*Math.max(a,b);coarseA+=w*a;coarseB+=w*b;
     rule+=w*payoff(k,y,fineRule[y]);
     if((fineRule[y]===0?a:b)!==Math.max(a,b))throw Error("Rule");
   }
   const measured=fine-Math.max(coarseA,coarseB);
   const predicted=Math.min(16+k,64-k);
   if(measured!==predicted || rule!==fine)throw Error("Value "+k);assertions+=2;
   if(measured<lower){lower=measured;worstAt=[k]} else if(measured===lower)worstAt.push(k);
   if(measured>upper){upper=measured;maxAt=[k]} else if(measured===upper)maxAt.push(k);
   if([0,16,24,32].includes(k))points.push({lambda:`${k}/64`,fine:`${fine}/256`,coarse:`${Math.max(coarseA,coarseB)}/256`,value:`${measured}/256`,cost_one_eighth_decision:measured>=32?"weakly_covers":"does_not_cover"});
 }
 if(lower!==16||upper!==40||maxAt.length!==1||maxAt[0]!==24)throw Error("Extrema");assertions+=4;
 let rectangularMin=Number.POSITIVE_INFINITY,rectangularMax=-1,rectangularCases=0;
 for(let d1=0;d1<=32;d1++)for(let d2=-48;d2<=-16;d2++)for(let d3=0;d3<=32;d3++){
  const v=Math.min(2*d1+d3,-d2);rectangularMin=Math.min(rectangularMin,v);rectangularMax=Math.max(rectangularMax,v);rectangularCases++;
 }
 if(rectangularMin!==0||rectangularMax!==48)throw Error("Rectangle");assertions+=2;
 if(Math.min(2*0+0,-(-16))!==0)throw Error("Differential outside");assertions++;
 return {question:"Common outside paid-service opportunity ties signed original-customer report action margins across states. Does that tighten identified economic report value?",unit:"All raw policy and report-value numerators are divided by 256 normalized captured-contribution units.",structural_model:{report_probabilities:["1/2","1/4","1/4"],lambda_range:"[0,1/2]",margins:["1/2-lambda","-1/4-lambda","lambda"],admissible_fine_rule:"A for y1/y3; B for y2",common_customer_and_operator_capacity:true},results:{coupled_lower:"1/16",coupled_upper:"5/32",coupled_max_at_lambda:"3/8",rectangle_lower:"0",rectangle_upper:"3/16",noncommon_lambda_counterworld:"lambda_y=(1/2,0,0) produces zero report value",cost_1_8:"strictly covered iff 1/4<lambda<1/2; equal at endpoints 1/4 and 1/2"},checks:{lambda_grid_points:33,rectangular_vectors:rectangularCases,exact_integer_assertions:assertions,illustrative_cases:points},scope:"Hypothetical signed whole-network A/B, known report masses; no robot, accepted-paid original customer evidence or scientific novelty; fixed learner and common original outside opportunity."};
}
if (typeof require !== 'undefined' && require.main === module) console.log(JSON.stringify(coupledAudit(),null,2));
if (typeof module !== 'undefined') module.exports={coupledAudit};
