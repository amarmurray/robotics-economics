"use strict";
const run=function run(){
 let checks=0;const ck=(x,m)=>{checks++;if(!x)throw Error(m)};
 function payoff(h,k,good){
   const ready=1+(k?(good?0:2):h+1)+k;
   const jobs={A:[3,4],C:[2,5],B:[3,6]};let best=-Infinity;
   function rec(t,used,v,renew){
     best=Math.max(best,v-k);
     for(const j of Object.keys(jobs)){
       if(used.includes(j)||t+1>jobs[j][1]||(j==="B"&&!renew))continue;
       rec(t+1,[...used,j],v+jobs[j][0],renew||(j==="A"&&k===1&&good&&t+1<=3));
     }
   }
   rec(ready,[],0,false);ck(best===(!k?5:good?7:1),"queue optimum");return best;
 }
 const worlds=[];
 for(let n=0;n<=12;n++){
  let G=0,GK=0,short=0,long=0,count=0;
  for(let h=0;h<2;h++)for(let i=0;i<12;i++){
   const good=i<(h===0?n:12-n);count+=+good;
   const a=payoff(h,0,good),b=payoff(h,1,good);G+=a;GK+=b;short+=h===0?b:a;long+=h===1?b:a;
  }
  const best=Math.max(G,GK,short,long);
  ck(G===120&&GK===96&&count===12,"fixed aggregate");ck(short===72+6*n&&long===144-6*n,"conditional");ck(best===120+Math.max(0,6*n-48)+Math.max(0,24-6*n),"positive part");ck((best>132)===(n<2||n>10),"E crossing");
  worlds.push({p_numerator:n,denominator:12,values_24ths:{G,GK,short,long,best,E:132}});
 }
 let robust=-Infinity;
 for(let q0=0;q0<=12;q0++)for(let q1=0;q1<=12;q1++){const worst=Math.min(1440-48*q0+24*q1,1440+24*q0-48*q1);ck(worst<=1440,"randomized endpoint");robust=Math.max(robust,worst)}
 ck(robust===1440,"robust skip");ck(Math.min(...worlds.filter(w=>w.p_numerator>=11).map(w=>w.values_24ths.short))===138,"audit lower");
 return {synthetic:true,checks,worlds,robust_G_family:5,assumed_E:5.5};
};
console.log(JSON.stringify(run(),null,2));
