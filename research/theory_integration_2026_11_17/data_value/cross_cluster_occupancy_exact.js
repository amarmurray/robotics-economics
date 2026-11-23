"use strict";
const run = function(){
let checks=0;const ck=(ok,msg)=>{checks++;if(!ok)throw Error(msg)};
const rows=[];
for(let k=0;k<=8;k++){
 const atoms=[];for(let x=0;x<2;x++)for(let h=0;h<2;h++)for(let y=0;y<2;y++)atoms.push({x,h,y,n:(x+h+y)%2?8-k:k});
 const sum=f=>atoms.reduce((a,t)=>a+t.n*f(t),0);ck(sum(()=>1)===32,"mass");
 for(const [a,b] of [["x","h"],["x","y"],["h","y"]])for(let i=0;i<2;i++)for(let j=0;j<2;j++)ck(sum(t=>+(t[a]===i&&t[b]===j))===8,"pair cells");
 const hit=t=>+(t.x===0&&t.h===1&&t.y===1);
 ck(sum(hit)===k,"joint paid displacement opportunity");
 // 1/128 contribution units: rewards in quarters, atom mass /32.
 const P=sum(t=>8+24*t.x),G=P-64+sum(t=>16*hit(t)),E=P+32;
 ck(P===640&&G===576+16*k&&E===672,"policy scores");
 ck(sum(t=>Math.max(8+24*t.x,t.h*t.y?24:8))-64===G,"joint scheduling");
 const bad=sum(t=>8+24*t.x+(t.h*t.y?24:8))-64;
 ck(bad>G,"illegal local summation");
 for(let a0=-4;a0<=4;a0++)for(let a1=-4;a1<=4;a1++)for(let d=-1;d<=1;d++){
   const anchor=t=>8+24*t.x+(t.x?a1:a0);
   const p=sum(anchor),g=p-64+sum(t=>(16+d)*hit(t)),e=p+32;
   const exact=sum(t=>Math.max(anchor(t),anchor(t)+(t.x===0&&t.h*t.y?16+d:0)))-64;
   ck(exact===g,"joint retained anchor and upgrade");
   ck(g-p===-64+(16+d)*k,"anchor residual cancels across prefixes");
   ck(Math.abs((g-p)-(G-P))<=k,"matched contrast residual bound");
   if(k>=7)ck(g-e>=9,"strict audit despite anchor errors");
 }
 rows.push({even_mass_numerator:k,denominator:128,P,G,E,free_matching_P:G+64,committed_shared_E:P-224,illegal_local_sum:bad,joint_hit_mass_numerator:k,joint_hit_mass_denominator:32});
}
ck(rows[0].G<rows[0].E&&rows[8].G>rows[8].E,"rank reversal");
ck(rows[7].G-rows[7].E===16,"exact audit margin");
return {synthetic:true,checks,units:"1/128 normalized contribution",rows,audit_G_minus_P_lower:41,audit_G_minus_E_lower:9,anchor_error_quarters:[-4,4],incremental_error_quarters:[-1,1]};
};
console.log(JSON.stringify(run(),null,2));
