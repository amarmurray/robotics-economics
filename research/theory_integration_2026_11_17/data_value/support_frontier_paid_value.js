(function() {
"use strict";
let checks=0;
const ok=(a,s)=>{checks++;if(!a)throw Error(s);};
const S=40,E=55;
const sg=q=>Math.max(S,q);
const spread=cap=>({lower:sg(0)-E,upper:sg(cap)-E});
for(let q=0;q<=80;q++){
 ok(sg(q)>=S,"optional old fallback");
 ok(spread(80).lower<=sg(q)-E && sg(q)-E<=spread(80).upper,"unseen full-policy interval");
 for(let p=0;p<=100;p++){
  ok((p*S+(100-p)*q)/100<=sg(q)+1e-10,"commitment mixture");
 }
}
for(let q=0;q<=50;q++){ok(sg(q)-E<=-5,"verified full-horizon cap");}
const D2=3*(-15)-3*(-15)-15;
ok(D2===-15,"Möbius lower coalition");
let dualMin=Infinity,dualWitness=null,dualCases=0;
for(let l=0;l<=100;l++)for(let m=0;m<=100;m++)if(l+m>=100){
 dualCases++;const value=(50*l+100*m)/100;
 if(value<dualMin){dualMin=value;dualWitness={l,m};}
}
ok(dualMin===50&&dualWitness.l===100&&dualWitness.m===0,"LP dual primal 0.5");
const twoStage=50+50*80/100;
const adaptive=40+60*50/100;
ok(twoStage===90&&twoStage>E,"future data creates economically important service");
ok(adaptive===70&&adaptive>E,"adaptive continuation expands policy class");
const robustLowerE=54,robustUpperSG=Math.max(41,50);
ok(robustLowerE-robustUpperSG===4,"hypothetical simultaneous confidence bound");
const tvObserved=0.01*0.8;
ok(Math.abs(tvObserved-0.008)<1e-12,"1 pct logging error");
ok(Math.abs(100*tvObserved-0.8)<1e-12,"optimal occupancy ratio");
const results={
status:"Synthetic mathematical checks, not original-buyer measurements or robots",
lowerCoalition:{D2,hypotheticalF_T_M:[-15,-15,-15]},
allSources:{noCap:spread(80),signedFullHorizonCap:spread(50),units:"hundredths of normalized accepted-and-paid contribution"},
dual:{primal:50,minimum:dualMin,witness:dualWitness,feasibleGridPairs:dualCases},
statisticalIllustration:{supportedSG:[39,41],offSupportCeilingSG:50,supportedE:[54,56],EgapAtLeast:4,realConfidenceData:false},
invalidStaticCaps:{futureLearnedPaidTotal:twoStage,postFailureAdaptivePaidTotal:adaptive},
logging:{explorationFraction:0.01,meanTV:tvObserved,optimizerDensityRatio:100,optimizerGap:0.8},
checks
};
if(typeof module!=="undefined" && typeof require!=="undefined" && require.main===module)console.log(JSON.stringify(results,null,2));
return results;
})();
