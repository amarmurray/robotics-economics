"use strict";
/* Endogenous intervention-selection and production-value benchmark.
   Source: private theoretical construction, not robot training or field estimates.
   Run: node intervention_selection.js
*/
const Intervention = (() => {
  function checkProb(v, name) {
    if (typeof v !== "number" || !Number.isFinite(v) || v < 0 || v > 1)
      throw new RangeError(name + " must be in [0,1]");
  }
  function likelihood({exposure, gate = 1, prior = .5, pHigh = .75, pLow = .25}) {
    for (const [n,v] of Object.entries({exposure,gate,prior,pHigh,pLow})) checkProb(v,n);
    const cHigh = exposure * gate * pHigh;
    const cLow = exposure * gate * pLow;
    const positive = prior * cHigh + (1-prior) * cLow;
    return {
      positive, cHigh, cLow,
      postPositive: positive ? prior*cHigh/positive : null,
      postNegative: positive === 1 ? null : prior*(1-cHigh)/(1-positive),
      missedError: exposure*(1-gate)*(prior*pHigh+(1-prior)*pLow)
    };
  }
  function policy({exposure,gate=1,prior=.5,pHigh=.75,pLow=.25,
    current=0,target=5,sourceHigh=9,sourceLow=1,learning=1,early=true,
    logExposure=false}) {
    const l = likelihood({exposure,gate,prior,pHigh,pLow});
    function terminal(z, post, weight) {
      if (weight <= 0) return 0;
      const reusable = post*sourceHigh+(1-post)*sourceLow+learning*z;
      return weight*Math.max(target,reusable);
    }
    let t=0;
    if (early && !logExposure) {
      if (l.positive) t += terminal(1,l.postPositive,l.positive);
      if (l.positive < 1) t += terminal(0,l.postNegative,1-l.positive);
    } else if (early) {
      const qH=gate*pHigh, qL=gate*pLow;
      const c1 = prior*qH+(1-prior)*qL;
      if (1-exposure) t+=terminal(0,prior,1-exposure);
      if (exposure*c1>0) t+=terminal(1,prior*qH/c1,exposure*c1);
      if (exposure*(1-c1)>0)
        t+=terminal(0,prior*(1-qH)/(1-c1),exposure*(1-c1));
    } else {
      // Same physical updates for each acquired correction; route must be committed
      // before the correction signal is revealed.
      t=Math.max(target,prior*sourceHigh+(1-prior)*sourceLow+learning*l.positive);
    }
    return {current,terminal:t,total:current+t,...l};
  }
  function results() {
    const routine=policy({exposure:.25,current:6});
    const probe=policy({exposure:1,current:5});
    const specialist=policy({exposure:0,current:6.3});
    return {
      setting:"synthetic, undiscounted two-date provider contribution",
      menu:{routine,probe,specialist},
      delayed:{
        routine:policy({exposure:.25,current:6,early:false}).total,
        probe:policy({exposure:1,current:5,early:false}).total
      },
      noPhysicalLearning:{
        routine:policy({exposure:.25,current:6,learning:0}).total,
        probe:policy({exposure:1,current:5,learning:0}).total
      },
      strongerTargetOnly:{
        routine:policy({exposure:.25,current:6,target:6.25}).total,
        probe:policy({exposure:1,current:5,target:6.25}).total
      },
      costlessRoutineRelevantData:policy({exposure:1,current:6}).total,
      observationalEquivalence:{
        lowExposureHighGate:likelihood({exposure:.25,gate:1}),
        highExposureLowGate:likelihood({exposure:1,gate:.25}),
        sameLoggedRateDifferentMisses:likelihood({exposure:1,gate:.5,pHigh:.375,pLow:.125})
      }
    };
  }
  function runTests() {
    let tests=0;
    const near=(a,b,name)=>{if(!(Math.abs(a-b)<=1e-11))throw Error(name+" "+a+" != "+b);tests++;};
    const yes=(ok,name)=>{if(!ok)throw Error(name);tests++;};
    const z=results(),r=z.menu.routine,p=z.menu.probe,s=z.menu.specialist;
    near(r.positive,1/8,"routine correction probability");
    near(p.positive,1/2,"probe correction probability");
    near(r.postPositive,3/4,"posterior correction");
    near(r.postNegative,13/28,"posterior absence");
    near(p.postNegative,1/4,"probe negative posterior");
    near(r.terminal,43/8,"routine terminal");
    near(p.terminal,13/2,"probe terminal");
    near(r.total,91/8,"routine total");
    near(p.total,23/2,"probe total");
    near(s.total,113/10,"specialist total");
    yes(p.total>r.total&&r.total>s.total,"global observed menu choice");
    near(z.delayed.routine,89/8,"delayed routine");
    near(z.delayed.probe,21/2,"delayed probe");
    yes(z.delayed.routine>z.delayed.probe,"delay reverses choice");
    near(z.noPhysicalLearning.routine,45/4,"no learning routine");
    near(z.noPhysicalLearning.probe,11,"no learning probe");
    yes(z.noPhysicalLearning.routine>z.noPhysicalLearning.probe,"physical channel matters");
    near(z.strongerTargetOnly.routine,399/32,"better target routine");
    near(z.strongerTargetOnly.probe,97/8,"better target probe");
    yes(z.strongerTargetOnly.routine>z.strongerTargetOnly.probe,"strong alternative reversal");
    near(z.costlessRoutineRelevantData,25/2,"free relevant data in production");
    yes(z.costlessRoutineRelevantData>p.total,"free production byproduct");
    const a=z.observationalEquivalence.lowExposureHighGate;
    const b=z.observationalEquivalence.highExposureLowGate;
    const c=z.observationalEquivalence.sameLoggedRateDifferentMisses;
    near(a.positive,b.positive,"identical aggregate corrections");
    near(b.positive,c.positive,"identical gated correction rate");
    yes(b.missedError>c.missedError,"different ungated risks");
    near(b.missedError,3/8,"missed error world 1");
    near(c.missedError,1/8,"missed error world 2");
    for(const e of [.01,.1,.25,.5,.9,1]){
      const early=policy({exposure:e}),delayed=policy({exposure:e,early:false});
      yes(early.terminal+1e-11>=delayed.terminal,"early report cannot hurt at exposure "+e);
      const logged=policy({exposure:e,logExposure:true});
      yes(logged.terminal+1e-11>=early.terminal,"exposure log cannot hurt "+e);
    }
    // Kernel proof sanity: Bernoulli(q_hi*p_H) thinned with q_lo/q_hi
    // reproduces Bernoulli(q_lo*p_H) for each latent state.
    for(const ph of [.1,.25,.75,.9]){
      near((.8*ph)*(.2/.8),.2*ph,"Blackwell thinning "+ph);
    }
    for(const bad of [{exposure:-.1},{exposure:1.1},{exposure:.5,gate:-1}]) {
      let threw=false;try{likelihood(bad)}catch(e){threw=e instanceof RangeError;}
      yes(threw,"probability bounds");
    }
    return {pass:tests,model:"intervention_selection.js",calibrated:false};
  }
  return {likelihood,policy,results,runTests};
})();
if (typeof module !== "undefined" && module.exports) {
  module.exports=Intervention;
  if (require.main===module) console.log(JSON.stringify({tests:Intervention.runTests(),results:Intervention.results()},null,2));
}
