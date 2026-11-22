"use strict";
// Finite fully synthetic two-site connected-network program: common exogenous
// broadcast/recovery/customer regime U, one unknown mixture weight theta.
// All entries are complete accepted-and-cleared *net* program contributions
// in tenths of an invented unit; no direct benchmark-to-dollar mapping.
// Each row is the conditional value of a lawful full-history policy (U=0,U=1).
let assertions=0;
function assert(x,msg){assertions++;if(!x)throw Error(msg);}
const P=[[20,40],[15,50]]; // retained R; production-generated learning
const E=[[19,39],[15,45]]; // retained R after E capex; extra physical capacity
function score(row,n,d){return row[0]*(d-n)+row[1]*n;}
function upper(rows,n,d){return Math.max(...rows.map(r=>score(r,n,d)));}
function gcd(a,b){while(b!==0){[a,b]=[b,a%b];}return Math.abs(a);}
function frac(n,d){if(d<0){n=-n;d=-d;}const g=gcd(n,d);return [n/g,d/g];}
function candidates(groups){
  const out=new Map([["0/1",[0,1]],["1/1",[1,1]]]);
  for(const rows of groups)for(let i=0;i<rows.length;i++)for(let j=i+1;j<rows.length;j++){
    const a=rows[i],b=rows[j];
    let n=a[0]-b[0],d=(b[1]-b[0])-(a[1]-a[0]);
    if(d===0)continue;
    [n,d]=frac(n,d);
    if(n>=0&&n<=d)out.set(n+"/"+d,[n,d]);
  }
  return [...out.values()].sort((x,y)=>x[0]*y[1]-y[0]*x[1]);
}
function envelope(A,B){
  return candidates([A,B]).map(([n,d])=>({
    theta:n+"/"+d,
    p_num:upper(A,n,d), e_num:upper(B,n,d),
    denominator:10*d,
    gap_num:upper(A,n,d)-upper(B,n,d)
  }));
}
const exact=envelope(P,E);
assert(JSON.stringify(exact.map(x=>x.theta))===JSON.stringify(["0/1","1/3","2/5","1/1"]),"joint breakpoints");
const gapMin=Math.min(...exact.map(x=>x.gap_num/x.denominator));
const gapMax=Math.max(...exact.map(x=>x.gap_num/x.denominator));
assert(Math.abs(gapMin-0.1)<1e-12,"sharp paired lower envelope");
assert(Math.abs(gapMax-0.5)<1e-12,"sharp paired upper envelope");
let grid=0;const D=600;
for(let n=0;n<=D;n++){
  const p=upper(P,n,D),e=upper(E,n,D);
  assert(p-e>=D,"P optimized minus E optimized >= 1/10");
  assert(p>=score(P[0],n,D),"retained lawful policy P");
  assert(e>=score(E[0],n,D),"retained lawful policy E");
  grid++;
}
assert(Math.min(...P.map(x=>x[0]))===15,"low performance costly forced P pilot exists");
assert(score(P[0],0,1)>score(E[0],0,1),"retained comparator after E capex");
const independent_lower=Math.min(...P.map(x=>x[0])) /*not optimizer*/;
const actual_independent_optimistic=upper(P,0,1)-upper(E,1,1);
assert(actual_independent_optimistic===-25,"separately optimized rectangular programs cannot certify");
const eCap=E[1];
assert(P.every(row=>!(row[0]>=eCap[0]+1&&row[1]>=eCap[1]+1)),"no single P action gives 0.1 statewise premium to E capacity");
// A fixed mixture uses pilot with probability rho: comparing to an E
// optimizer that knows theta, theta=0 requires rho<=1/5,
// while theta=1 requires rho>=1/2. No fixed mixture can do both.
let uniformly_dominating_mixtures=0;
for(let n=0;n<=1000;n++){
  const r=n/1000;
  if((20*(1-r)+15*r)>=19 && (40*(1-r)+50*r)>=45)
    uniformly_dominating_mixtures++;
}
assert(uniformly_dominating_mixtures===0,"no ex-ante fixed P mixture beats ex-post E envelope");
// Compare a P policy fixed before the unknown theta to an E program that can
// choose its policy separately at every theta (an information-asymmetric oracle).
// Endpoint gaps are 1/10-rho/2 and -1/2+rho; best worst-case rho=2/5.
const rStar=2/5;
assert(Math.abs(Math.min(0.1-0.5*rStar,-0.5+rStar)+0.1)<1e-12,
       "sharp fixed-P versus theta-tailored-E maximin gap");
for(let n=0;n<=1000;n++){
 const rho=n/1000;
 assert(Math.min(0.1-0.5*rho,-0.5+rho)<=-0.1+1e-12,
        "no fixed P mixing beats -1/10 minimax gap");
}
const alternateE=[[19,39],[22,45]];
const alt=envelope(P,alternateE);
assert(upper(P,0,1)-upper(alternateE,0,1)===-2,"common factor does not force P dominance at low type");
assert(upper(P,1,1)-upper(alternateE,1,1)===5,"same factor permits reverse sign");
assert(upper(P,7,12)===upper(alternateE,7,12),"alternate exact reversal theta=7/12");
for(let n=0;n<=D;n++){
 const gap=upper(P,n,D)-upper(E,n,D);
 assert(gap>=D && gap<=5*D,"complete coupled envelope on fine grid");
}
const result={
  model:"two-site shared broadcast/recovery/customer regime, unknown common theta",
  legal_programs:{P:["retained R","productive source-data pilot"],E:["R after purchased E","independent embodied capacity"]},
  conditional_paid_net_values_tenths:{P,E}, 
  exact_breakpoints_and_values:exact,
  sharp_coupled_gap_interval:["1/10","1/2"],
  independent_program_extrema_lower_gap:"-25/10",
  no_fixed_P_action_randomization_dominates_theta_specific_E_optimizer:true,
  alternate_E_signed_gap:["-2/10 at theta=0","0 at theta=7/12","+5/10 at theta=1"],
  maximin_fixed_P_versus_theta_tailored_E:"-1/10 at pilot probability 2/5",
  exhaustive_theta_grid_denominator:D,assertions,
  synthetic:true,measured_robots:false,signed_field_evidence:false,independently_new_theorem:false
};
if(typeof require!=="undefined"&&typeof module!=="undefined"&&require.main===module)console.log(JSON.stringify(result,null,2));
return result;
