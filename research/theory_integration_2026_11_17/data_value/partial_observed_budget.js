"use strict";
/*
 * Partial-observation safe-budget continuation, When Capabilities Become Production.
 * Synthetic two-slot customer bundle; no field estimates or safety certification.
 * Run: node partial_observed_budget.js
 */
const PartialObservedBudget = (() => {
  const EPS = 1e-11;
  const positive = (x,k) => {
    if (!Number.isFinite(x) || x < 0) throw new RangeError(k);
  };
  const probability = (x,k) => {
    positive(x,k);
    if (x > 1) throw new RangeError(k);
  };
  const maxChoice = candidates => candidates.reduce((best,c) =>
    c.value > best.value + EPS ? c : best);

  function settings(opts={}) {
    const delta = opts.delta === undefined ? 8 : opts.delta;
    const alphaG = opts.alphaG === undefined ? .99 : opts.alphaG;
    const alphaR = opts.alphaR === undefined ? .75 : opts.alphaR;
    const pBody = opts.pBody === undefined ? .9 : opts.pBody;
    const budget = opts.budget === undefined ? 2.1 : opts.budget;
    const eta = opts.eta === undefined ? 0 : opts.eta;
    const mode = opts.mode || "hard";
    positive(delta,"delta");positive(budget,"budget");
    for (const [k,p] of Object.entries({alphaG,alphaR,pBody,eta})) probability(p,k);
    if (alphaG < .5 || alphaR < .5) throw new RangeError("signal accuracy below .5");
    if (!["hard","chance","mean"].includes(mode)) throw new RangeError("mode");
    return {delta,alphaG,alphaR,pBody,budget,eta,mode};
  }
  const opFirst = {R:0,G:1,E:1,S:0};
  const flowFirst = {R:1,G:0,E:0,S:2};
  function emission(route,h,y,o) {
    if (route==="E" || route==="S") return y==="none" ? 1 : 0;
    const accuracy = route==="R" ? o.alphaR : o.alphaG;
    return y===h ? accuracy : 1-accuracy;
  }
  function outcome(route,action,h,o) {
    if (action==="specialist") return {flow:2,qualified:0,operators:0};
    if (action==="bodyTarget") return {flow:0,qualified:o.pBody,operators:1};
    const choice = action==="targetA" ? "A" : "B";
    const match = choice===h;
    return {flow:0,qualified:match?1:0,operators:match?1:2};
  }
  function routeTree(route, opts={}) {
    const o=settings(opts);
    if (!Object.hasOwn(opFirst,route)) throw new RangeError("route");
    const outcomes=[], decision={};
    let v=flowFirst[route];
    const labels=(route==="E"||route==="S") ? ["none"] : ["A","B"];
    for (const y of labels) {
      const cells=["A","B"].map(h=>({h,w:.5*emission(route,h,y,o)}));
      const pReport=cells.reduce((s,c)=>s+c.w,0);
      if (pReport < EPS) continue;
      const actions=route==="E" ? ["specialist","bodyTarget"] : ["specialist","targetA","targetB"];
      const candidates=[];
      for (const action of actions) {
        let risk=0, expectedOp=0, expectedValue=0;
        for (const c of cells) {
          if (c.w<=0) continue;
          const x=outcome(route,action,c.h,o);
          const w=c.w/pReport;
          risk+=w*Number(opFirst[route]+x.operators > o.budget+EPS);
          expectedOp+=w*(opFirst[route]+x.operators);
          expectedValue+=w*(x.flow+o.delta*x.qualified);
        }
        const allowed=o.mode==="hard" ? risk<=EPS :
                      o.mode==="chance" ? risk<=o.eta+EPS :
                      expectedOp<=o.budget+EPS;
        if (allowed) candidates.push({action,value:expectedValue,risk,expectedOp});
      }
      if (!candidates.length) throw Error("no safe terminal alternative");
      const best=maxChoice(candidates);
      decision[y]=best;
      outcomes.push({report:y,pReport,candidates,best});
      v+=pReport*best.value;
    }
    return {route,value:v,decisions:decision,branches:outcomes};
  }
  function treeSolve(opts={}) {
    const routes=["R","G","E","S"].map(r=>routeTree(r,opts));
    return {best:maxChoice(routes),routes};
  }
  function closedForm(opts={}) {
    const o=settings(opts);
    if (o.budget < 2) throw new RangeError("closed form assumes budget >=2");
    const gRisk= o.alphaG===1 ? 0 : 1-o.alphaG;
    const gExpected=3-o.alphaG;
    const gAllowed=o.mode==="hard" ? (o.alphaG===1 || o.budget>=3-EPS) :
       o.mode==="chance" ? (o.budget>=3-EPS || gRisk<=o.eta+EPS) :
       gExpected<=o.budget+EPS;
    const result={
      R:1+Math.max(2,o.alphaR*o.delta),
      G:Math.max(2,gAllowed ? o.alphaG*o.delta : -Infinity),
      E:Math.max(2,o.pBody*o.delta),
      S:2+Math.max(2,.5*o.delta)
    };
    return {routes:result,best:maxChoice(Object.entries(result).map(([route,value])=>({route,value}))),gAllowed};
  }
  function frechet(pB,pC) {
    probability(pB,"pB");probability(pC,"pC");
    return {lower:Math.max(0,pB+pC-1),upper:Math.min(pB,pC)};
  }
  function jointLaw(pB,pC,joint) {
    const f=frechet(pB,pC);
    if (!Number.isFinite(joint) || joint<f.lower-EPS||joint>f.upper+EPS)
      throw new RangeError("joint outside sharp bounds");
    return {both:joint,onlyB:pB-joint,onlyC:pC-joint,
      neither:1-pB-pC+joint};
  }
  function tests() {
    let n=0;
    const eq=(a,b,s)=>{if(Math.abs(a-b)>1e-9)throw Error(s+": "+a+" != "+b); n++;};
    const yes=(b,s)=>{if(!b)throw Error(s);n++;};
    for (const delta of [0,1,4,8,12,50])
      for (const alphaG of [.5,.75,.99,1])
        for (const budget of [2.1,3])
          for (const mode of ["hard","chance","mean"]) {
            const o={delta,alphaG,budget,mode,eta:.02};
            const a=treeSolve(o),b=closedForm(o);
            for(const r of a.routes)eq(r.value,b.routes[r.route],"tree/closed "+r.route);
            eq(a.best.value,b.best.value,"best tree/closed");
          }
    let t=treeSolve({delta:8,alphaG:1});
    eq(t.best.value,8,"perfect grounding wins");
    yes(t.best.route==="G","perfect G selected");
    t=treeSolve({delta:8,alphaG:.99});
    eq(t.best.value,7.2,"imperfect grounding hard budget");
    yes(t.best.route==="E","new body selected when noisy G blocked");
    const g=t.routes.find(r=>r.route==="G");
    eq(g.value,2,"no target feasible after noisy G with hard cap");
    t=treeSolve({delta:8,alphaG:.99,mode:"chance",eta:.02});
    eq(t.best.value,7.92,"chance-relaxed diagnostic");
    yes(t.best.route==="G","chance relaxed G");
    t=treeSolve({delta:8,alphaG:.99,mode:"chance",eta:.005});
    yes(t.best.route==="E","strict chance cap restores E");
    t=treeSolve({delta:8,alphaG:.99,budget:3});
    eq(t.best.value,7.92,"larger pathwise budget allows G");
    t=treeSolve({delta:8,alphaG:.99,mode:"mean"});
    eq(t.best.value,7.92,"expected budget wrongly admits G under hard cap");
    t=treeSolve({delta:0,alphaG:.99});
    eq(t.best.value,4,"two-period competent specialist baseline");
    yes(t.best.route==="S","zero demand picks specialist");
    const r=frechet(.75,.75),e=frechet(.9,.9);
    eq(r.lower,.5,"routine lower joint");eq(r.upper,.75,"routine upper joint");
    eq(e.lower,.8,"body lower joint");eq(e.upper,.9,"body upper joint");
    eq(1+8*r.lower,5,"routine lower production");
    eq(1+8*r.upper,7,"routine upper production");
    eq(8*e.lower,6.4,"body lower production");
    eq(8*e.upper,7.2,"body upper production");
    for(const [pB,pC,j] of [[.75,.75,.5],[.75,.75,.75],[.9,.9,.8],[.9,.9,.9],[.2,.8,0],[.2,.8,.2]]) {
      const q=jointLaw(pB,pC,j);
      eq(q.both+q.onlyB+q.onlyC+q.neither,1,"law normalized");
      eq(q.both+q.onlyB,pB,"B marginal");
      eq(q.both+q.onlyC,pC,"C marginal");
      yes(Object.values(q).every(v=>v>=-EPS),"nonnegative cells");
    }
    return {assertions:n,method:"two independent calculations: full H/report/action enumeration and closed Bellman form",synthetic:true,not_independent_review:true};
  }
  return {settings,routeTree,treeSolve,closedForm,frechet,jointLaw,tests};
})();
if (typeof module!=="undefined" && module.exports) {
  module.exports=PartialObservedBudget;
  if (require.main===module) console.log(JSON.stringify({tests:PartialObservedBudget.tests(),example:PartialObservedBudget.treeSolve({delta:8,alphaG:.99})},null,2));
}
