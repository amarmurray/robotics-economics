// ROBUST POLICY IDENTIFICATION — synthetic CPU-only finite tests, no robot/safety evidence.
// Execute in strict JS/V8; no external packages, network, or source-derived calibrated parameters.
"use strict";
function near(a,b,eps=1e-10){return Math.abs(a-b)<=eps;}
let assertions=0;
function check(condition,message){assertions++;if(!condition) throw Error("assertion "+assertions+": "+message);}
function frechet(pB,pC){return [Math.max(0,pB+pC-1),Math.min(pB,pC)];}
function cells(p,q){return [1-2*p+q,p-q,p-q,q];} // 00,10,01,11 when equal component marginals p
function validCells(c){return c.every(x=>x>=-1e-12)&&near(c.reduce((a,b)=>a+b,0),1);}
function V_R(q){return 1+8*q;}
function V_E(q){return 8*q;}
const S=6;
const rF=frechet(.75,.75),eF=frechet(.9,.9);
check(near(rF[0],.5)&&near(rF[1],.75),"R Frechet");
check(near(eF[0],.8)&&near(eF[1],.9),"E Frechet");
const independent={R:[V_R(rF[0]),V_R(rF[1])],E:[V_E(eF[0]),V_E(eF[1])]};
check(near(independent.R[0],5)&&near(independent.R[1],7),"independent R");
check(near(independent.E[0],6.4)&&near(independent.E[1],7.2),"independent E");
check(V_R(.75)>V_E(.8)&&V_R(.5)<V_E(.9),"opposite ranking feasible");
let minR_E=Infinity,minR_S=Infinity,maxR_E=-Infinity,admissible=0;
for(let i=0;i<=250;i++){
  const qR=.5+i*.001;
  for(let j=0;j<=100;j++){
    const qE=.8+j*.001;
    const cR=cells(.75,qR),cE=cells(.9,qE);
    check(validCells(cR)&&validCells(cE),"copula feasible");
    if(qE-qR<=.10000000001){
      admissible++;
      minR_E=Math.min(minR_E,V_R(qR)-V_E(qE));
      maxR_E=Math.max(maxR_E,V_R(qR)-V_E(qE));
      minR_S=Math.min(minR_S,V_R(qR)-S);
      check(V_R(qR)>V_E(qE),"paired robust dominance");
      check(V_R(qR)>S,"paired specialist");
    }
  }
}
check(admissible>0,"nonempty paired identified set");
check(near(minR_E,.2),"sharp paired bound");
check(near(minR_S,.6),"sharp specialist bound");
check(near(maxR_E,1+8*.75-8*.8),"max paired difference");
function productiveWorld(z,h){return 1+(h==="X"?(2+6*z):(8-6*z));}
function terminalReward(action,h){return action===h?8:2;}
function diagnosticByEnumeration(alpha,h,c=0){
  return alpha*terminalReward(h,h)+(1-alpha)*terminalReward(h==="X"?"Y":"X",h)-c;
}
function diagnosticClosed(alpha,c=0){return 2+6*alpha-c;}
function diagnosticRobust(alphaLower,c=0){return diagnosticClosed(alphaLower,c);}
const mix=.5,productiveMaximin=Math.min(productiveWorld(mix,"X"),productiveWorld(mix,"Y"));
check(near(productiveMaximin,6),"productive maximin");
for(let i=0;i<=1000;i++){
  const z=i/1000;
  const v=Math.min(productiveWorld(z,"X"),productiveWorld(z,"Y"));
  check(v<=6+1e-12,"no no-signal policy exceeds six");
}
for(let j=50;j<=100;j++){
  const alpha=j/100;
  for(const h of ["X","Y"]){
    check(near(diagnosticByEnumeration(alpha,h,.1),diagnosticClosed(alpha,.1)),"regime report enumeration");
  }
}
const thresh=(4+.1)/6;
check(near(thresh,41/60),"diagnostic threshold");
check(diagnosticRobust(.6,.1)<6&&diagnosticRobust(.7,.1)>6,"interval refinement choice");
check(near(diagnosticRobust(.6,.1),5.5)&&near(diagnosticRobust(.7,.1),6.1),"example payoffs");
function robustPathwiseDiagnostic(alpha,budget=2.1,wrongTerminal=1){
  const first=1,correct=1;
  return first+correct<=budget && (alpha>=1-1e-14 || first+wrongTerminal<=budget);
}
check(robustPathwiseDiagnostic(.7,2.1,1),"uniform safe follow on");
check(!robustPathwiseDiagnostic(.99,2.1,2),"even 99% unsafe recovery");
check(robustPathwiseDiagnostic(1,2.1,2),"structurally revealing exception");
check(robustPathwiseDiagnostic(.99,3,2),"increased budget");
const n=400,delta=.05,observed=.8;
const lower=observed-Math.sqrt(Math.log(4/delta)/(2*n));
check(lower>41/60&&lower<.73&&lower>.72,"hypothetical conditional Hoeffding bound");
const results={
  schema:"robust_policy_identification_synthetic_v1",
  provenance:"purely synthetic, no field calibration or safety authorization",
  marginals:{routine:.75,redesign:.9},
  frechet:{routine:rF,redesign:eF},
  independentValueIntervals:independent,
  pairedUpperGain:.1,
  pairedSharpMinDifference:minR_E,
  pairedSharpVsSpecialist:minR_S,
  pairedAdmissibleGridWorlds:admissible,
  productiveMaximin:productiveMaximin,
  diagnosticAdditionalCost:.1,
  diagnosticAccuracyThreshold:thresh,
  diagnosticAtLowerPoint6:diagnosticRobust(.6,.1),
  diagnosticAtLowerPoint7:diagnosticRobust(.7,.1),
  hypotheticalValidation:{perRegimeN:n,perRegimeCorrect:320,confidence:1-delta,lowerAccuracy:lower},
  pathwise:{noRecoveryMismatch:robustPathwiseDiagnostic(.7,2.1,1),rareRecovery99:robustPathwiseDiagnostic(.99,2.1,2),budget3:robustPathwiseDiagnostic(.99,3,2)},
  assertions:assertions,
  independentReview:false,
  historicalCI:false,
  actualRoboticsEvidence:false
};
return results;
