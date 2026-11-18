"use strict";
/* Bounded residual network interference: finite synthetic CPU diagnostic.
   No customer measurement, approved safety policy, or data-to-dollar calibration. */
function run() {
  let checks=0;
  function assert(p,label){checks++;if(!p)throw Error(label);}
  function close(x,y,label){assert(Math.abs(x-y)<1e-10,label+" "+x+" "+y);}
  const baseline=7, wA=.7, g=.5, wB=.3, c=.03, ownAError=.02;
  function conditionalLower(localUpper, residual){
    return wA*g-wB*(localUpper+residual)-c-ownAError;
  }
  close(conditionalLower(.6,.25),.045,"conditional net gain");
  close(conditionalLower(.6,.4),0,"sharp residual budget");
  close(conditionalLower(.6,.5),-.03,"sign reversal at looser remainder");
  assert(conditionalLower(.6,.25)>0,"conditional economic certificate");
  assert(conditionalLower(.6,.5)<0,"inadequate economic certificate");
  for(let i=0;i<=200;i++){
    const s=.2+.4*i/200;
    const residual=-.25+.5*(200-i)/200;
    const aChange=-ownAError+2*ownAError*(i%11)/10;
    const gain=wA*g-wB*(s+residual)-c+aChange;
    assert(gain>=conditionalLower(.6,.25)-1e-10,"bounded coupled total "+i);
  }
  // A complete finite-state persistent-regime Markov model. State=(Q,D).
  const states=[0,1,2,3], H=["good","bad"], actions=["R","G"];
  const q=s=>s%2, d=s=>Math.floor(s/2);
  function clamp(x){return Math.max(0,Math.min(1,x));}
  function kernel(s,a,h,approx=false) {
    const pq=clamp(.18+.35*q(s)+(a==="G"?.27:.10)+(h==="good"?.08:0)-(approx?.02:0));
    const pd=clamp(.42+.22*d(s)+.12*q(s)+(a==="R"?.10:.02)+(h==="good"?.05:0)+(approx?.015:0));
    return [(1-pq)*(1-pd),pq*(1-pd),(1-pq)*pd,pq*pd];
  }
  function tv(P,Q){return P.reduce((sum,p,i)=>sum+Math.abs(p-Q[i]),0)/2;}
  let epsilon=0;
  for(const h of H)for(const s of states)for(const a of actions){
    const P=kernel(s,a,h),Q=kernel(s,a,h,true);
    close(P.reduce((x,y)=>x+y,0),1,"true mass");
    close(Q.reduce((x,y)=>x+y,0),1,"surrogate mass");
    epsilon=Math.max(epsilon,tv(P,Q));
    assert(tv(P,Q)<=.035+1e-12,"marginal coupling bound");
  }
  const r=(s,a)=>.5*q(s)*d(s)-(a==="G"?.15:0);
  const terminal=s=>2*q(s)*d(s);
  const policies={
    adaptive:(t,s)=>t===0?"R":(q(s)===0?"G":"R"),
    retained:()=> "R"
  };
  function value(policy,h,approx=false) {
    let flow=[0,0,1,0], v=0; // initial Q=0,D=1
    for(let t=0;t<2;t++) {
      const next=[0,0,0,0];
      for(const s of states) {
        const a=policies[policy](t,s),prob=flow[s],K=kernel(s,a,h,approx);
        v+=prob*r(s,a);
        for(const s2 of states)next[s2]+=prob*K[s2];
      }
      flow=next;
    }
    for(const s of states)v+=flow[s]*terminal(s);
    return v;
  }
  const onePolicyBound=epsilon*(.65+2)+epsilon*2;
  const table=[];
  for(const h of H){
    const x={regime:h};
    for(const p of Object.keys(policies)){
      x[p+"_actual"]=value(p,h,false);
      x[p+"_near"]=value(p,h,true);
      assert(Math.abs(x[p+"_actual"]-x[p+"_near"])<=onePolicyBound+1e-10,"policy coupling "+h+p);
    }
    const diffActual=x.adaptive_actual-x.retained_actual;
    const diffNear=x.adaptive_near-x.retained_near;
    assert(Math.abs(diffActual-diffNear)<=2*onePolicyBound+1e-10,"paired same regime");
    x.delta_actual=diffActual;x.delta_near=diffNear;
    table.push(x);
  }
  // Distinct θ across time is NOT allowed in the same-regime comparison.
  const lowerSame=Math.min(...table.map(x=>x.delta_near))-2*onePolicyBound;
  for(const x of table)assert(x.delta_actual>=lowerSame-1e-10,"same-world robust lower");
  // An arbitrarily close recovery law can change hard capacity feasibility.
  const eta=.001;
  function recovery(e) {return [{pair:"00",p:.8+e},{pair:"10",p:.1-e},{pair:"01",p:.1-e},{pair:"11",p:e}];}
  function recoverInfo(e){
    const rows=recovery(e),P=rows.map(x=>x.p);
    close(P.reduce((x,y)=>x+y,0),1,"recovery mass");
    const m1=P[1]+P[3],m2=P[2]+P[3];
    close(m1,.1,"recovery marginal 1");
    close(m2,.1,"recovery marginal 2");
    return {peak:rows.some(x=>x.p>0&&x.pair==="11")?2:1,p:P};
  }
  const safe=recoverInfo(0),rare=recoverInfo(eta);
  close(tv(safe.p,rare.p),2*eta,"tiny recovery TV");
  assert(safe.peak===1&&rare.peak===2,"arbitrarily small risk invalidates hard peak cap");
  const missedIn1000=Math.pow(1-eta,1000);
  assert(missedIn1000>.36&&missedIn1000<.37,"no observed joint event with finite trials");
  return {
    scope:"conditional synthetic bounded-network data value, not field estimates or physical safety",
    assertions:checks,
    selective:{baseline,local_spillover_upper:.6,unobserved_spillover_bound:.25,
      network_cost:c,ownA_unobserved_total_loss:ownAError,
      robust_increment_lower:conditionalLower(.6,.25),
      total_lower:baseline+conditionalLower(.6,.25),
      residual_break_even:.4,
      loose_remainder_lower:conditionalLower(.6,.5)},
    sequential:{epsilon_one_step_tv:epsilon,one_policy_value_error_ceiling:onePolicyBound,
      paired_difference_error_ceiling:2*onePolicyBound,
      same_regime_robust_paired_lower:lowerSame,rows:table},
    recovery:{same_per_site_probability:.1,rare_joint_probability:eta,
      TV_from_disjoint:tv(safe.p,rare.p),safe_support_peak:safe.peak,rare_support_peak:rare.peak,
      probability_of_no_joint_event_in_1000_trials:missedIn1000},
    limitations:{identified_network_remainder:false,feasibility_certified:false,field_data:false,prior_art_novelty:false,repository_ci:false}
  };
}
const result=run();
if(typeof console!=="undefined"&&typeof process!=="undefined") console.log(JSON.stringify(result,null,2));
result;
