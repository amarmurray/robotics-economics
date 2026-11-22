"use strict";
// Deterministic integer-exact lawful predispatch production report model.
// Run: node lawful_signal_partition_model.js (no dependencies).
function group(z){let out=[];for(let i=0;i<z.length;i++){let j=out.findIndex(t=>t.key===z[i]);if(j<0)out.push({key:z[i],hs:[i]});else out[j].hs.push(i);}return out.map(t=>t.hs);}
function bits(n){let k=0;while(n){k+=n&1;n>>=1;}return k;}
function cellBest(q,menu,hs){const A=q[0].length;let best=-Infinity;for(let a=0;a<A;a++){if(!hs.every(h=>(menu[h]&(1<<a))!==0))continue;let v=hs.reduce((s,h)=>s+q[h][a],0);if(v>best)best=v;}return best;}
function full(q,menu){let v=0;for(let h=0;h<q.length;h++){let b=cellBest(q,menu,[h]);if(b===-Infinity)return -Infinity;v+=b;}return v;}
function observed(q,menu,z){let v=0;for(const hs of group(z)){let b=cellBest(q,menu,hs);if(b===-Infinity)return -Infinity;v+=b;}return v;}
function brute(q,menu,z,L){const G=group(z),n=G.length;let best=-Infinity;function rec(i,labels){if(i===n){let sum=0;for(let k=0;k<L;k++){const hs=[];for(let j=0;j<n;j++)if(labels[j]===k)hs.push(...G[j]);if(hs.length){const v=cellBest(q,menu,hs);if(v===-Infinity)return;sum+=v;}}best=Math.max(best,sum);return;}for(let k=0;k<L;k++)rec(i+1,[...labels,k]);}rec(0,[]);return best;}
function actionSubset(q,menu,z,L){const G=group(z),A=q[0].length;let best=-Infinity;for(let mask=1;mask<(1<<A);mask++){if(bits(mask)>L)continue;let total=0,ok=true;for(const hs of G){let v=-Infinity;for(let a=0;a<A;a++)if((mask&(1<<a))&&hs.every(h=>menu[h]&(1<<a)))v=Math.max(v,hs.reduce((s,h)=>s+q[h][a],0));if(v===-Infinity){ok=false;break;}total+=v;}if(ok)best=Math.max(best,total);}return best;}
function optimalCommon(q,menu,z){return group(z).every(hs=>{const target=hs.map(h=>cellBest(q,menu,[h]));for(let a=0;a<q[0].length;a++)if(hs.every((h,j)=>(menu[h]&(1<<a))&&q[h][a]===target[j]))return true;return false;});}
function run(){
  let checks=0,infeasible=0;
  for(let v=0;v<64;v++){let x=v,q=Array.from({length:3},()=>Array.from({length:2},()=>{let d=x&1;x>>=1;return d;}));
    for(let m=0;m<27;m++){let k=m,menu=Array.from({length:3},()=>{const d=k%3;k=Math.floor(k/3);return d+1;});
      for(let s=0;s<8;s++){const z=Array.from({length:3},(_,i)=>(s>>i)&1);
        for(let L=1;L<=3;L++){const a=brute(q,menu,z,L),b=actionSubset(q,menu,z,L);if(a!==b)throw Error("action-subset theorem failed");checks++;}
        const o=observed(q,menu,z),f=full(q,menu),c=optimalCommon(q,menu,z);
        if((o===f)!==c)throw Error("observable-block optimality failed");checks++;
        if(o===-Infinity)infeasible++;
      }
    }
  }
  const q=[[1,0],[0,1],[1,0]],m=[3,3,3],coarse=[0,0,1],fine=[0,1,0],noval=[0,0,0];
  const test={unrestricted:full(q,m),coarse:observed(q,m,coarse),fine:observed(q,m,fine),no_signal:observed(q,m,noval),
     coarse_min_L1:brute(q,m,coarse,1),coarse_min_L2:brute(q,m,coarse,2),fine_L2:brute(q,m,fine,2)};
  if(JSON.stringify(test)!==JSON.stringify({unrestricted:3,coarse:2,fine:3,no_signal:2,coarse_min_L1:2,coarse_min_L2:2,fine_L2:3}))throw Error("synthetic values");
  const E=0.75, net={SG_legal_coarse:2/3,SG_legal_fine:1,SG_fine_after_cost_eighth:1-1/8,E};
  if(!(net.SG_legal_coarse<E && net.SG_fine_after_cost_eighth>E))throw Error("investment sign");
  return {model:"lawful_signal_partition_model",test,net,checks,unimplementable_cases:infeasible,
    robust_uncertain_Q:{hidden_regret_deterministic:1,hidden_regret_optimal_randomized:0.5,revealed_regret:0},
    limitations:"synthetic normalized accepted-paid Q; no field data; zero menu/report cost except indicated case"};
}
const result=run();
if(typeof console!=="undefined")console.log(JSON.stringify(result,null,2));
result;
