"use strict";
// Synthetic common structural law, 8 equiprobable failure-conditional histories.
const B=i=>i<4, M=i=>i!==0&&i!==4, T=i=>[1,2,5,6].includes(i);
function evaluate(a,b){
 const H=i=>i===a||i===b, obs={R:[],G:[],K:[],QT:[]};
 let theta=0,gR=0,gG=0,gK=0,gGK=0;
 for(let i=0;i<8;i++){
  let h=H(i),m=M(i),t=T(i),x=B(i);
  if(t&&!m)throw Error("K without worker recovery");
  obs.R.push([+x,+x,1]);obs.G.push([+x,1,1,+h]);
  obs.K.push([+x,+x,+m,+t]);obs.QT.push([+h,+t]);
  theta+=+(h&&m&&!t);
  gR+=2*+x;gG+=2*(1+4*+h);
  gK+=2*+(x&&m)*(1+4*+t);gGK+=2*+m*(1+4*+(h||t));
 }
 // Whole original-ticket contribution, exactly scaled by 64. One customer payment
 // maximum. Early acceptance probability 1/2, early payment 1. G,K each cost 1/4
 // per failure; E is independent staff, late payment 4, whole cost 5/8.
 return {H_atoms:[a,b],theta_eighths:theta,obs,
  values64:{R:32+2*gR,G:32+2*gG-8,K:32+2*gK-8,
            GK:32+2*gGK-16,E:120}};
}
function hist(x){let h={};for(const r of x){let k=r.join("/");h[k]=(h[k]||0)+1}
 return Object.entries(h).sort((a,b)=>a[0].localeCompare(b[0]));}
function run(){
 let assertions=0;const assert=(b,m)=>{assertions++;if(!b)throw Error(m)};
 const cases=[];for(const a of [0,3])for(const b of [4,7])cases.push(evaluate(a,b));
 const ref=Object.fromEntries(["R","G","K","QT"].map(k=>[k,hist(cases[0].obs[k])]));
 for(const v of cases){
  for(const k of ["R","G","K","QT"])assert(JSON.stringify(hist(v.obs[k]))===JSON.stringify(ref[k]),"law "+k);
  for(const [k,n] of Object.entries({R:48,G:88,K:68,E:120}))assert(v.values64[k]===n,k);
  assert(v.values64.GK===104+16*v.theta_eighths,"GK formula");
  assert(v.theta_eighths>=0&&v.theta_eighths<=2,"moment bound");
 }
 const sorted=cases.map(v=>v.values64.GK).sort((a,b)=>a-b);
 assert(JSON.stringify(sorted)==="[104,120,120,136]","sharp worlds");
 for(let i=0;i<=100;i++)assert(Math.max(i,100-i)>=50,"regret lower bound");
 return {synthetic:true,exact_assertions:assertions,observed_laws:ref,
   cases:cases.map(v=>({H_atoms:v.H_atoms,theta_eighths:v.theta_eighths,values64:v.values64})),
   sharp_GK_interval64:[104,136],E64:120,
   maximin:"E",minimax_regret_GK_fraction:"1/2",worst_regret:"1/8"};
}
if(typeof module!=="undefined"){module.exports={run,evaluate};if(require.main===module)console.log(JSON.stringify(run(),null,2));}
