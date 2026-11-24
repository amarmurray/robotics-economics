"use strict";
function run(){
 const N=128;let checks=0;const ck=(b,m)=>{checks++;if(!b)throw Error(m)};
 const pos=x=>Math.max(0,x);
 // Integer masses; no fractional service dispatch. q=compatible pair mass, m=potential successor mass, s=positive report mass, x=intersection.
 const gain=(q,m,s,x)=>pos(6*x-s)+pos(6*(m-x)-(q-s));
 const grid=16;let worlds=0;
 for(let q=0;q<=grid;q++)for(let m=0;m<=q;m++)for(let s=0;s<=q;s++){
  const lo=Math.max(0,m+s-q),hi=Math.min(m,s);let mx=-1;
  for(let x=lo;x<=hi;x++){
   worlds++;
   const g=gain(q,m,s,x);const g0=pos(6*m-q);
   ck(g>=g0&&g<=5*m,"report envelope");
   ck(g===Math.max(0,6*x-s,6*(m-x)-(q-s),6*m-q),"four lawful policies");
   mx=Math.max(mx,g);
  }
  ck(mx===Math.max(gain(q,m,s,lo),gain(q,m,s,hi)),"sharp fixed report marginal upper");
  if(q>0)ck(gain(q*q,m*q,s*q,m*s)===q*pos(6*m-q),"independence attains lower");
 }
 // Enumerate actual dated schedules. One date-1 slot, one date-2 slot, two total buyer authorizations.
 const value=(a,b,match,newCtrl,success,budget)=>{
  const first=[{pay:0,used:0,j:false}];
  if(a||b)first.push({pay:4,used:1,j:false});
  if(a&&b&&match&&newCtrl)first.push({pay:3,used:1,j:true});
  let best=0;
  for(const f of first)for(const next of [0,2,8]){
   if(next===8&&!(f.j&&success))continue;
   if(f.used+Number(next>0)>budget)continue;
   best=Math.max(best,f.pay+next);
  }
  return best;
 };
 for(let a=0;a<=1;a++)for(let b=0;b<=1;b++)for(let k=0;k<=1;k++)for(let z=0;z<=1;z++){
  const old=value(a,b,k,0,z,2),neu=value(a,b,k,1,z,2);
  ck(old===2+4*Number(a||b),"old schedules");
  ck(neu===old+5*a*b*k*z,"new schedules with known success");
  ck(value(a,b,k,1,z,1)===4*Number(a||b)||(!(a||b)&&value(a,b,k,1,z,1)===2),"one total slot");
 }
 const q=64,m=40,s=40;
 ck(gain(q,m,s,25)===176,"uninformative report");
 ck(gain(q,m,s,40)===200,"perfect report");
 ck(176-64<128&&200-64>128,"embodiment ranking reversal");
 ck(value(1,1,1,1,1,2)===11&&value(1,1,0,1,1,2)===6,"compatibility distinct from counts");
 ck(11>2+4+4,"singleton-calibrated additive upper fails");
 ck(5*32-64<128,"uniform joint cap ranks E");
 ck(176>128,"free matching routine ranks above E");
 return {synthetic:true,assertions:checks,grid_laws:worlds,denominator:N,original_compatible_mass:"1/2",success_mass:"5/16",report_positive_mass:"5/16",uninformative_intersection:"25/128",perfect_intersection:"5/16",gain_before_cost:[176/N,200/N],grounding_increment:[112/N,136/N],independent_embodiment_increment:1,cap_one_quarter_grounding_upper:0.75,free_routine_increment:176/N,known_success_compatible_value:11,incompatible_value:6};
}
console.log(JSON.stringify(run(),null,2));
