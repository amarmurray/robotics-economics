// JS deterministic exact eighth-grid conditional audit. Run: node joint_original_parent.js
function jointAudit(){
 const d=8;let checks=0,rectangles=0;
 const ck=x=>{checks++;if(!x)throw Error("check "+checks)};
 const formula=(la,ua,lb,ub)=>({one:[4*la+3*lb-3*Math.min(la,lb),4*ua+3*ub-3*Math.max(0,ua+ub-8)],bundle:[7*Math.max(0,la+lb-8),7*Math.min(ua,ub)]});
 for(let la=0;la<=d;la++)for(let ua=la;ua<=d;ua++)for(let lb=0;lb<=d;lb++)for(let ub=lb;ub<=d;ub++){
 let xlo=Infinity,xhi=-Infinity,ylo=Infinity,yhi=-Infinity;
 for(let a=la;a<=ua;a++)for(let b=lb;b<=ub;b++)for(let q=Math.max(0,a+b-d);q<=Math.min(a,b);q++){
 let x=4*a+3*b-3*q,y=7*q;xlo=Math.min(xlo,x);xhi=Math.max(xhi,x);ylo=Math.min(ylo,y);yhi=Math.max(yhi,y);}
 const f=formula(la,ua,lb,ub);ck(f.one[0]===xlo);ck(f.one[1]===xhi);ck(f.bundle[0]===ylo);ck(f.bundle[1]===yhi);rectangles++;
 }
 let n=0,oneLo=Infinity,oneHi=-Infinity,bunLo=Infinity,bunHi=-Infinity;
 for(let cA=3;cA<=5;cA++)for(let cB=3;cB<=5;cB++)for(let a=Math.max(0,cA-1);a<=Math.min(8,cA+1);a++)for(let b=Math.max(0,cB-1);b<=Math.min(8,cB+1);b++)for(let q=Math.max(0,a+b-8);q<=Math.min(a,b);q++){
 const x=4*a+3*b-3*q,y=7*q;oneLo=Math.min(oneLo,x);oneHi=Math.max(oneHi,x);bunLo=Math.min(bunLo,y);bunHi=Math.max(bunHi,y);n++;}
 const f=formula(2,6,2,6);ck(n===301);ck(f.one[0]===oneLo&&f.one[1]===oneHi);ck(f.bundle[0]===bunLo&&f.bundle[1]===bunHi);
 ck(4*4+3*4===28&&4*4+3*4-3*4===16);ck(7*0===0&&7*4===28);ck(28-2>24&&16-2<24);ck(28-2>24&&0-2<24);
 return {model:"joint_original_parent",date:"2026-11-20",grid_denominator:8,exact_assertions:checks,marginal_rectangles:rectangles,selection_completions:n,respondent_coverage:"3/4",respondent_C_marginals:["1/2","1/2"],mean_menu_drift_bounds:["1/8","1/8"],natural_marginal_bounds:["1/4","3/4"],one_slot_gross_numerators:f.one,all_or_none_bundle_gross_numerators:f.bundle,field_observations:false,physical_certification:false};
}
if (typeof module !== 'undefined') module.exports={jointAudit};
if (typeof require !== 'undefined' && typeof module !== 'undefined' && require.main===module) process.stdout.write(JSON.stringify(jointAudit(),null,2)+'\n');
