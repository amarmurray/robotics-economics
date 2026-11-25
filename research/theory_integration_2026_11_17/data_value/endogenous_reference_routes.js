"use strict";
function study(){
 let checks=0,cases=0;function ok(x){if(!x)throw Error("check "+checks);checks++}
 function solve(jobs,caps,e,tool,setup,fee,beta=1){
  const rem=caps.slice(); if(tool){rem[0]-=setup;if(rem[0]<0)return {value:-Infinity,counts:[0,0],dates:[]}}
  let best={value:-Infinity};
  function rec(j,val,dates){
   if(j===jobs.length){if(val>best.value+1e-10){let counts=[0,0];dates.forEach((t,i)=>{if(t>=0)counts[jobs[i].type]++});best={value:val,counts,dates:dates.slice()}}return}
   const x=jobs[j];rec(j+1,val,[...dates,-1]);
   const dur=Math.min(x.old,e?x.donor:Infinity,tool?x.newExt:Infinity,tool&&e?x.newDonor:Infinity);
   for(let t=0;t<=x.deadline&&t<rem.length;t++){if(rem[t]<dur)continue;rem[t]-=dur;rec(j+1,val+beta**t*x.v,[...dates,t]);rem[t]+=dur}
  }
  rec(0,tool?-fee:0,[]);return best
 }
 function subset(jobs,H,e,t,setup,fee){
  let max=0;if(t&&H<setup)return -Infinity;
  for(let m=0;m<2**jobs.length;m++){let h=t?setup:0,v=0;for(let j=0;j<jobs.length;j++)if(m>>j&1){const x=jobs[j];h+=Math.min(x.old,e?x.donor:Infinity,t?x.newExt:Infinity,t&&e?x.newDonor:Infinity);v+=x.v}if(h<=H)max=Math.max(max,v)}
  return max-(t?fee:0)
 }
 function pair(jobs,H,setup,fee,beta=1){return [0,1].map(e=>{let old=solve(jobs,H,e,0,setup,fee,beta),fresh=solve(jobs,H,e,1,setup,fee,beta);return {old,fresh,best:fresh.value>old.value?fresh:old}})}
 const small={type:0,v:4,old:2,donor:2,newExt:2,newDonor:2,deadline:0};
 const large={type:1,v:12,old:5,donor:3,newExt:3,newDonor:3,deadline:0};
 const subst=pair([small,small,large],[4],1,1);
 const comp=pair([small,small,{...large,donor:4,newExt:4,newDonor:1}],[4],1,1);
 function exp(p,arr,key){return (1-p)*arr[0][key].value+p*arr[1][key].value}
 function response(arr,key){return [0,1].map(i=>.5*(arr[1][key].counts[i]-arr[0][key].counts[i]))}
 function source(arr,k){return {oldPremium:exp(.75,arr,"old")-exp(.25,arr,"old")-k,newPremium:exp(.75,arr,"best")-exp(.25,arr,"best")-k,oldResponse:response(arr,"old"),newResponse:response(arr,"best")}}
 const s=source(subst,1.5),c=source(comp,2.5);ok(s.oldPremium>0&&s.newPremium<0);ok(c.oldPremium<0&&c.newPremium>0);ok(subst[0].best.counts[0]===0&&subst[0].old.counts[0]===2);ok(comp[1].best.counts[0]===1&&comp[1].old.counts[0]===0);
 const timing=pair([{...large,deadline:1}],[4,5],1,1,.8)[0],expiry=pair([large],[4,5],1,1,.8)[0];
 ok(timing.old.dates[0]===1&&timing.best.dates[0]===0&&timing.best.counts[1]===timing.old.counts[1]);ok(expiry.old.counts[1]===0&&expiry.best.counts[1]===1);
 for(let H=1;H<=7;H++)for(let setup=0;setup<=H;setup++)for(let fee=0;fee<=3;fee++)for(let dd=1;dd<=5;dd++)for(let ne=1;ne<=5;ne++)for(let nd=1;nd<=5;nd++){
  const jobs=[small,small,{...large,donor:dd,newExt:ne,newDonor:nd}];let a=pair(jobs,[H],setup,fee);
  for(let e=0;e<2;e++){ok(a[e].old.value===subset(jobs,H,e,0,setup,fee));ok(a[e].fresh.value===subset(jobs,H,e,1,setup,fee));ok(a[e].best.value>=a[e].old.value)}
  const G0=a[0].fresh.value+fee-a[0].old.value,G1=a[1].fresh.value+fee-a[1].old.value;
  const interaction=(a[1].best.value-a[0].best.value)-(a[1].old.value-a[0].old.value);
  ok(interaction===Math.max(0,G1-fee)-Math.max(0,G0-fee));ok(a[1].best.value>=a[0].best.value);ok(Math.abs(interaction)<=Math.abs(G1-G0));cases++
 }
 return {checks,cases,substitution:{cells:subst,source:s},complementarity:{cells:comp,source:c},timing,expiry,scope:"Synthetic schedule enumeration and independent subset formula; not empirical or proof"};
}
console.log(JSON.stringify(study(),null,2));
