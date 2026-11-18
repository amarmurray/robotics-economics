"use strict";
/* Sequential, policy-induced reachable support and customer qualification.
   Pure synthetic finite-state check; no physical robot or market calibration.
   Run: node sequential_support.js
*/
const SequentialSupport = (() => {
  const check=(x,k)=>{if(!Number.isFinite(x)||x<0||x>1)throw RangeError(k);};
  function evaluate(v={}) {
    const c=Object.assign({
      prior:.5,firstHigh:.75,firstLow:.25,
      exposureHigh:1,exposureLow:1,
      qualifyHigh:.75,qualifyLow:.25,
      delta:8,secondCost:3,specialist:1,firstCost:.25
    },v);
    for(const k of ["prior","firstHigh","firstLow","exposureHigh",
       "exposureLow","qualifyHigh","qualifyLow"])check(c[k],k);
    if(["delta","secondCost","specialist","firstCost"].some(k=>c[k]<0||!Number.isFinite(c[k])))
      throw RangeError("finite nonnegative production inputs required");
    const highWeight=c.prior*c.firstHigh;
    const lowWeight=(1-c.prior)*c.firstLow;
    const correction=highWeight+lowWeight;
    const jointSuccess=highWeight*c.exposureHigh*c.qualifyHigh+
                       lowWeight*c.exposureLow*c.qualifyLow;
    const bConditional=correction>0 ? jointSuccess/correction : 0;
    const bOption=c.delta*bConditional-c.secondCost;
    const old=Math.max(0,c.specialist);
    const post=Math.max(0,c.specialist,bOption);
    const withProbe=-c.firstCost+(1-correction)*old+correction*post;
    const noProbe=old;
    return {correction,posteriorHigh:correction>0?highWeight/correction:null,
      jointSuccess,bConditional,bOption,post,old,withProbe,noProbe,
      optimalFirst:withProbe>noProbe?"probe":withProbe<noProbe?"routine":"tie",
      optimalSecondAfterCorrection:post===bOption && post>old?"updated-B":
        post===old && old>0?"specialist":"retained-A",
      ...{inputs:c}};
  }
  // Independent event-tree enumeration, not the closed-form formula:
  // h -> first corrected/not -> if corrected second exposure and qualification.
  function tree(v={}) {
    const c=Object.assign({
      prior:.5,firstHigh:.75,firstLow:.25,
      exposureHigh:1,exposureLow:1,
      qualifyHigh:.75,qualifyLow:.25,
      delta:8,secondCost:3,specialist:1,firstCost:.25
    },v);
    const hw=[[c.prior,c.firstHigh,c.exposureHigh,c.qualifyHigh],
             [1-c.prior,c.firstLow,c.exposureLow,c.qualifyLow]];
    let weights=[0,0],success=0;
    for(const [p,r,e,s] of hw){
      weights[1]+=p*r;weights[0]+=p*(1-r);
      for(const [ex,px] of [[0,1-e],[1,e]]) {
        for(const [y,py] of [[0,1-s],[1,s]]) {
          success+=p*r*px*py*ex*y;
        }
      }
    }
    const valueB=weights[1]>0?c.delta*success/weights[1]-c.secondCost:0;
    const specialist=Math.max(0,c.specialist),chosen=Math.max(specialist,valueB);
    return {firstCorrected:weights[1],jointSuccess:success,
      withProbe:-c.firstCost+weights[0]*specialist+weights[1]*chosen,
      noProbe:specialist};
  }
  function summaries(){
    const positive=evaluate(),negative=evaluate({qualifyHigh:.25,qualifyLow:.75});
    const noReach=evaluate({exposureHigh:0,exposureLow:0});
    const freeFirst=evaluate({firstCost:0});
    return {setting:"synthetic selected-reachability, two safe deployment episodes and held-out qualification",
      positive,negative,noReach,freeFirst,
      unselectedMeanQualification:.5,
      independencePrediction:.25,
      assumptions:"A already qualified; first correction enables optional B access; separately qualified specialist available; validated B is stochastic; no unmonitored unsafe robot experiments."};
  }
  function tests(){
    let n=0;
    function near(a,b,k){if(Math.abs(a-b)>1e-12)throw Error(k+": "+a+" vs "+b);n++;}
    function yes(x,k){if(!x)throw Error(k);n++;}
    const z=summaries(),p=z.positive,q=z.negative;
    near(p.correction,.5,"same first correction");
    near(q.correction,.5,"same opposite correction");
    near(p.posteriorHigh,.75,"selected posterior");
    near(q.posteriorHigh,.75,"posterior remains");
    near(p.jointSuccess,5/16,"positive selected joint");
    near(q.jointSuccess,3/16,"negative selected joint");
    near(p.bConditional,5/8,"positive cond success");
    near(q.bConditional,3/8,"negative cond success");
    near(p.bOption,2,"positive incremental B");
    near(q.bOption,0,"negative incremental B");
    near(p.post,2,"positive post decision");
    near(q.post,1,"negative specialist dominates");
    near(p.withProbe,5/4,"positive probe value");
    near(q.withProbe,3/4,"negative probe value");
    near(p.noProbe,1,"competent baseline");
    near(q.noProbe,1,"negative competent baseline");
    yes(p.optimalFirst==="probe","probe worthwhile when linked");
    yes(q.optimalFirst==="routine","probe rejected when anti-linked");
    yes(p.optimalSecondAfterCorrection==="updated-B","B selected");
    yes(q.optimalSecondAfterCorrection==="specialist","specialist retained");
    yes(p.jointSuccess>1/4&&q.jointSuccess<1/4,"joint product wrong both ways");
    near(z.noReach.jointSuccess,0,"zero support");
    near(z.noReach.withProbe,3/4,"no support probe loses");
    near(z.freeFirst.withProbe,3/2,"free first correction option");
    for(const v of [{},{qualifyHigh:.25,qualifyLow:.75},
      {firstHigh:0,firstLow:0},{exposureHigh:0,exposureLow:0},
      {prior:.1,firstHigh:.8,firstLow:.15,exposureHigh:.3,exposureLow:.9,qualifyHigh:.4,qualifyLow:.95},
      {prior:.95,firstHigh:.2,firstLow:.7,exposureHigh:.9,exposureLow:.1,qualifyHigh:.9,qualifyLow:.2}]) {
       const a=evaluate(v),b=tree(v);
       near(a.correction,b.firstCorrected,"tree first");
       near(a.jointSuccess,b.jointSuccess,"tree joint");
       near(a.withProbe,b.withProbe,"tree policy");
       near(a.noProbe,b.noProbe,"tree baseline");
       yes(a.post>=a.old,"optional after correction");
    }
    for(const k of ["firstHigh","qualifyLow","exposureHigh"]){
      let fails=false;try{evaluate({[k]:-1})}catch(e){fails=e instanceof RangeError;}
      yes(fails,"probability input "+k);
    }
    return {assertions:n,independent_event_tree:true,calibrated:false,physical_experiment:false};
  }
  return {evaluate,tree,summaries,tests};
})();
if(typeof module!=="undefined" && module.exports){
  module.exports=SequentialSupport;
  if(require.main===module)console.log(JSON.stringify({tests:SequentialSupport.tests(),results:SequentialSupport.summaries()},null,2));
}
