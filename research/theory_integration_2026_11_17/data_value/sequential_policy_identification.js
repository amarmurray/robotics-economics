"use strict";
function check(x,m){if(!x)throw Error(m)}
function near(a,b){return Math.abs(a-b)<1e-12}
function choices(n,k){const a=[];function recur(s,b){if(b.length===k){a.push(b.slice());return}for(let i=s;i<=n-k+b.length;i++){b.push(i);recur(i+1,b);b.pop()}}recur(0,[]);return a}
const y0=[20,21,19,22,20,18],y1=[24,20,23,25,18,22];
const assignments=choices(6,3);check(assignments.length===20,"20 balanced allocations");
let numeratorSum=0;for(const idx of assignments){const s=new Set(idx);for(let i=0;i<6;i++)numeratorSum+=s.has(i)?y1[i]:-y0[i]}
const sumDifference=y1.reduce((v,y,i)=>v+y-y0[i],0);
check(sumDifference===12&&numeratorSum===120,"unbiased finite randomization enumeration");
check(numeratorSum/60===sumDifference/6,"exact mean difference");
const delta=(r)=>2*r-.6;
check(near(delta(3/4),.9)&&near(delta(1/5),-.2),"conditional net return");
check(near(delta(3/4)/2,.45)&&near(delta(1/5)/2,-.1),"eligible weighting");
check(near(delta(.3),0),"decision threshold");
const bound=(R,alpha,n)=>2*R*Math.sqrt(Math.log(4/alpha)/(2*n));
const n=Math.ceil(2*16*Math.log(80)/(.5*.5));
check(n===561&&bound(4,.05,n)<=.5&&bound(4,.05,n-1)>.5,"confidence precision, not power");
console.log(JSON.stringify({synthetic:true,balanced_assignments:20,unbiased_expected_effect_tenths:numeratorSum/60,finite_population_effect_tenths:sumDifference/6,conditional_r_three_quarters:".9",conditional_r_one_fifth:"-.2",population_pi_one_half_high:".45",population_pi_one_half_low:"-.1",break_even_conditional_success:".3",independent_bounded_precision:{range:4,alpha:.05,target_halfwidth:.5,equal_arms_each:n,actual_halfwidth:bound(4,.05,n),power_study:false},field_effect:false,physical_approval:false},null,2))