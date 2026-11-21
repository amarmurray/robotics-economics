"use strict";
// Conditional original-buyer finite-sample design; synthetic, not field robotics evidence.
// Run: node finite_sample_paid_program.js
function run(){
  var assertions=0, scenarios=0;
  function check(ok,msg){assertions++;if(!ok)throw Error(msg);}
  function close(a,b,tol,msg){check(Math.abs(a-b)<(tol||1e-10),msg+" actual "+a+" expected "+b);}
  var alpha=0.05, log=Math.log(2/alpha);
  function radius(ns,ne,a){return Math.sqrt(0.5*(144/ns+64/ne)*Math.log(2/a));}
  function budgetCriterion(ns,ne){return 144/ns+64/ne;}
  var best={score:Infinity,ns:0,ne:0};
  for(var ns=1;ns<100;ns++){
    var ne=100-ns,score=budgetCriterion(ns,ne);
    if(score<best.score)best={score:score,ns:ns,ne:ne};
    scenarios++;
  }
  check(best.ns===60&&best.ne===40,"fixed budget optimal allocation 3/2");
  close(best.score,4,1e-12,"optimal coefficient 400/100");
  var bestCost={score:Infinity,ns:0,ne:0};
  for(var s=1;s<40;s++){
    var e=160-4*s;if(e<=0)continue;
    var sc=budgetCriterion(s,e);
    if(sc<bestCost.score)bestCost={score:sc,ns:s,ne:e};
    scenarios++;
  }
  check(bestCost.ns===30&&bestCost.ne===40,"unequal cost optimum");
  close(bestCost.ns/bestCost.ne,0.75,1e-12,"cost-weighted ratio");
  var cases=[
    {k:0.5,q:0.5,delta:2,choice:"SG"},
    {k:0.25,q:0.5,delta:-1,choice:"E"},
    {k:0.5,q:0.75,delta:0,choice:"tie"},
    {k:1/3,q:0.5,delta:0,choice:"tie"}
  ];
  for(var z of cases){
    var sg=12*z.k-1,e=8*z.q-1,d=sg-e;
    close(d,z.delta,1e-12,"example gap");
    check((d>0?"SG":d<0?"E":"tie")===z.choice,"example ranking");
  }
  // Even perfect joint technical qualification and buyer marginals need not reveal their paid copula.
  var correlated=[[0,0],[1,1]],anticorrelated=[[0,1],[1,0]];
  function moment(w,idx){return w.reduce(function(s,r){return s+r[idx];},0)/2;}
  function joint(w){return w.reduce(function(s,r){return s+r[0]*r[1];},0)/2;}
  for(var w of [correlated,anticorrelated]){
    close(moment(w,0),0.5,1e-12,"qualification marginal");
    close(moment(w,1),0.5,1e-12,"willingness marginal");
  }
  check(joint(correlated)===0.5&&joint(anticorrelated)===0,"opposite paid coupling");
  // Sharp conditional exact one-arm report ambiguity: a=12*k-1, b in [3,5].
  for(var t=0;t<=600;t++){
    var k=t/1200,sg=12*k-1;
    check(!(sg>5),"SG alone cannot strictly dominate all E at E upper 5");
    if(k<=1/3)check(sg<=3+1e-10,"E weak lower-envelope dominance");
    scenarios++;
  }
  function binomial(n,p){
    if(p===0)return Array.from({length:n+1},function(_,i){return i===0?1:0;});
    if(p===1)return Array.from({length:n+1},function(_,i){return i===n?1:0;});
    var x=new Array(n+1);x[0]=Math.pow(1-p,n);
    for(var j=0;j<n;j++)x[j+1]=x[j]*(n-j)/(j+1)*p/(1-p);
    return x;
  }
  function exactCoverage(ns,ne,k,q,a){
    var p=binomial(ns,k),u=binomial(ne,q),r=radius(ns,ne,a),truth=12*k-8*q;
    var total=0,bad=0;
    for(var i=0;i<=ns;i++)for(var j=0;j<=ne;j++){
      var wt=p[i]*u[j];
      total+=wt;
      if(Math.abs(12*i/ns-8*j/ne-truth)>r+1e-12)bad+=wt;
    }
    close(total,1,2e-11,"enumerated binomial mass");
    check(bad<=a+1e-9,"Hoeffding coverage exact binomial enumeration");
    return {k:k,q:q,noncoverage_probability:bad};
  }
  var outcomes=[];
  for(var p0 of [0.125,0.25,0.5]){
    for(var q0 of [0.5,0.625,0.75]){
      outcomes.push(exactCoverage(360,240,p0,q0,alpha));
      scenarios++;
    }
  }
  var fullCostMinN=Math.floor(800*log/4)+1;
  check(fullCostMinN===738,"conservative margin two n threshold");
  var safeN=738, nS=Math.round(0.6*safeN), nE=safeN-nS;
  check(2*radius(nS,nE,alpha)<2,"margin 2 sufficient with n 738");
  var smaller=737,s2=Math.round(0.6*smaller),e2=smaller-s2;
  check(2*radius(s2,e2,alpha)>=2,"n 737 insufficient for conservative certificate");
  // Matched pair random swap estimator: two equal-weight clusters with fixed outcomes.
  var yS=[11,-1],yE=[7,-1];
  var d0=yS[0]-yE[1],d1=yS[1]-yE[0];
  close((d0+d1)/2,(yS[0]+yS[1]-yE[0]-yE[1])/2,1e-12,"paired swap unbiased");
  check(d0>=-8&&d0<=12&&d1>=-8&&d1<=12,"paired outcome bounds");
  var r600=radius(360,240,alpha), rpair=20*Math.sqrt(log/(2*300));
  check(rpair>r600,"universal matched-pair range bound not automatically tighter");
  var output={
    type:"conditional_synthetic_finite_sample_no_real_robots",
    assumptions:"Independent interference-closed eligible-buyer clusters, frozen lawful whole-program policies, binary complete settled paid-service events, fixed normalized contributions/costs",
    outcome_menu:{SG:"12*k-1, k in [0,1/2]",E:"8*q-1, q in [1/2,3/4]",decision_gap:"12*k-8*q"},
    example_worlds:cases.map(function(c){return {k:c.k,q:c.q,SG_net:12*c.k-1,E_net:8*c.q-1,gap:c.delta,choice:c.choice};}),
    qualifications_same_marginals:{concordant_k:joint(correlated),discordant_k:joint(anticorrelated)},
    confidence:{alpha:alpha,estimate:"12*sample_mean_SG-8*sample_mean_E",radius_formula:"sqrt((144/n_SG+64/n_E)*ln(2/alpha)/2)",cost_minimum_100_clusters:{n_SG:best.ns,n_E:best.ne,coefficient:best.score},unequal_cost_160:{c_SG:4,c_E:1,n_SG:bestCost.ns,n_E:bestCost.ne},sufficient_margin_2_sample_clusters:fullCostMinN,radius_at_600_clusters:r600,matched_pair_radius_300_pairs:rpair},
    enumerated_coverage_outcomes:outcomes,
    assertions:assertions,scenarios:scenarios
  };
  return output;
}
if(typeof module!=="undefined"&&module.exports){module.exports={run};}
if(typeof require!=="undefined"&&require.main===module){process.stdout.write(JSON.stringify(run(),null,2)+"\n");}
