"use strict";
// Synthetic exact 8-atom identification/production diagnostic; integers only.
function failUnless(x,msg){if(!x)throw Error(msg)}

function moments(weights){const n=weights.reduce((a,b)=>a+b,0);const m=[0,0,0,0,0,0,0];for(let i=0;i<8;i++){const a=+STATES[i][0],b=+STATES[i][1],d=+STATES[i][2],w=weights[i];m[0]+=w*a;m[1]+=w*b;m[2]+=w*d;m[3]+=w*a*b;m[4]+=w*a*d;m[5]+=w*b*d;m[6]+=w*a*b*d;}return {n,m};}

function bounds(n,m){const [a,b,d,ab,ad,bd]=m;return [Math.max(0,ab+ad-a,ab+bd-b,ad+bd-d),Math.min(ab,ad,bd,n-a-b-d+ab+ad+bd)];}

function allCompositions(n,k,fn){const a=Array(k).fill(0);function visit(i,left){if(i===k-1){a[i]=left;fn(a.slice());return;}for(let x=0;x<=left;x++){a[i]=x;visit(i+1,left-x);}}visit(0,n);}

function parity(t){return [2-t,t,t,2-t,t,2-t,2-t,t];}

function main(){
 let count=0;const observed=new Map();
 allCompositions(8,8,w=>{count++;const {n,m}=moments(w);const key=m.slice(0,6).join(",");const prev=observed.get(key)||{lo:9,hi:-1};prev.lo=Math.min(prev.lo,m[6]);prev.hi=Math.max(prev.hi,m[6]);observed.set(key,prev);const [lo,hi]=bounds(n,m);failUnless(lo<=m[6]&&m[6]<=hi,"invalid sharp interval");});
 for(const [key,r] of observed){const m=key.split(",").map(Number);const [lo,hi]=bounds(8,m);failUnless(r.lo===lo&&r.hi===hi,"sharp interval not attained for "+key);}
 const p=[0,1,2].map(t=>{const {n,m}=moments(parity(t));failUnless(n===8&&m.slice(0,6).join(",")==="4,4,4,2,2,2"&&m[6]===t,"parity moment fail");return {triple_numerator:t,atom_numerators:parity(t),x_value_tenths:26+10*t,g_value_tenths:36,e_value_tenths:35,retain_value_tenths:30};});
 failUnless(p[0].x_value_tenths<36&&p[1].x_value_tenths===36&&p[2].x_value_tenths>36,"choice flip fail");
 const withoutInfo=Math.max((p[0].x_value_tenths+p[2].x_value_tenths)/2,36,35,30);const withPerfectWorldInformation=(Math.max(26,36,35,30)+Math.max(46,36,35,30))/2;
 failUnless(withoutInfo===36&&withPerfectWorldInformation===41,"hypothetical information value fail");
 return {model:"endogenous joint market-demand / target-qualification coupling",probability_denominator:8,composition_tables_checked:count,moment_patterns_exactly_verified:observed.size,bounds_are_sharp_over_all_rational_8_atom_tables_with_denominator_8:true,parity_worlds:p,counterfactual_choice:"G at t=0; tie X/G at t=1/8; X at t=1/4",net_value_tenths:{routine_qualified_incumbent:30,grounding:36,new_embodiment:35,source_training_world_low:26,source_training_world_high:46},hypothetical_equal_prior_EVPI_tenths:withPerfectWorldInformation-withoutInfo,field_evidence:false,physical_approval:false,full_repo_ci:false,independent_review:false};
}
const STATES=["000","001","010","011","100","101","110","111"];
if (require.main === module) console.log(JSON.stringify(main(),null,2));
module.exports = {moments,bounds,parity,main};
