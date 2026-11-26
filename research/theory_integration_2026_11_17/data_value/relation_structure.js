"use strict";
// Run: node relation_structure.js
const check = function(){
  let checks=0,graphCases=0,portfolioCases=0;
  const assert=(x,msg)=>{checks++;if(!x)throw Error(msg)};
  const near=(x,y)=>Math.abs(x-y)<1e-9;
  const edges=[];for(let i=0;i<4;i++)for(let j=i+1;j<4;j++)edges.push([i,j]);
  const label=(s,i)=>((s>>i)&1)?-1:1;
  const sign=(s,e)=>((s>>e)&1)?-1:1;
  for(let mask=0;mask<64;mask++){
    const obs=edges.map((_,e)=>e).filter(e=>mask&(1<<e));
    const adj=Array.from({length:4},()=>[]);for(const e of obs){const [i,j]=edges[e];adj[i].push(j);adj[j].push(i)}
    const comp=Array(4).fill(-1);let c=0;
    for(let i=0;i<4;i++)if(comp[i]===-1){const q=[i];comp[i]=c;while(q.length){const u=q.pop();for(const v of adj[u])if(comp[v]===-1){comp[v]=c;q.push(v)}}c++}
    const r=obs.length-4+c;
    for(let pat=0;pat<64;pat++)if((pat&mask)===pat){
      let match=[];for(let s=0;s<16;s++)if(obs.every(e=>label(s,edges[e][0])*label(s,edges[e][1])===sign(pat,e)))match.push(s);
      const LH=match.length/16, LL=2**(-obs.length);
      assert(near(LH/LL,match.length?2**r:0),"cycle likelihood");
      for(let e=0;e<6;e++)if(!(mask&(1<<e))&&match.length){
        const [i,j]=edges[e];const mu=match.reduce((sum,s)=>sum+label(s,i)*label(s,j),0)/match.length;
        assert(near(Math.abs(mu),comp[i]===comp[j]?1:0),"prediction support");
        for(const p of [.1,.4,.8]){
          const post=p*LH/(p*LH+(1-p)*LL);
          const conditionalMean=p*LH*mu/(p*LH+(1-p)*LL);
          assert(near(Math.abs(conditionalMean),comp[i]===comp[j]?post:0),"posterior predictive");
        }
      }
      graphCases++;
    }
  }
  const q=(a,p,d)=>(1+Math.max(a*p,d))/2;
  const V=(p,markets,K,a0,a1,cost)=>{
    let best=null;
    for(const u of [0,1])for(let mask=0;mask<(1<<markets.length);mask++){
      const ix=markets.map((_,i)=>i).filter(i=>mask&(1<<i));if(ix.length>K)continue;
      const a=u?a1:a0, probs=ix.map(i=>markets[i].fixed??q(a,p,markets[i].d));
      const val=ix.reduce((sum,i,k)=>sum+markets[i].w*probs[k],0)-u*cost;
      const row={val,u,ix,starts:probs.reduce((s,x)=>s+x,0),successor:ix.reduce((s,i,k)=>s+(markets[i].e??0)*probs[k],0)};
      if(!best||val>best.val+1e-12)best=row;
    }return best;
  };
  const audit=(p,k,f)=>{const z=p+(1-p)*2**(-k);return z*f(p/z)+(1-z)*f(0)};
  const opt=(p,k,c,f)=>{const stop=f(p);if(k===0||p===0||p===1)return stop;const z=(1+p)/2;return Math.max(stop,-c+z*opt(p/z,k-1,c,f)+(1-z)*f(0))};
  for(const p of [.1,.25,.4,.6,.9])for(const a0 of [.2,.4,.8])for(const a1 of [a0,1])for(const d of [0,.3,.7,1])for(const w of [3,10])for(const K of [1,2])for(const cost of [0,.5,2]){
    const markets=[{w,d,e:1},{w:7,fixed:1,e:2}];const f=p=>V(p,markets,K,a0,a1,cost).val;
    for(let k=1;k<=3;k++){
      const z=p+(1-p)*2**(-k);assert(near(z*(p/z),p),"posterior martingale");
      assert(audit(p,k,f)>=f(p)-1e-9,"optional audit");
      if(k>1)assert(audit(p,k,f)>=audit(p,k-1,f)-1e-9,"free repeated audit");
      assert(opt(p,k,.2,f)>=f(p)-1e-9,"optimal stopping");
      let ev=0;for(let pat=0;pat<(1<<k);pat++){const h=pat===0?1:0,l=2**(-k),pr=p*h+(1-p)*l;ev+=pr*f(p*h/pr)}
      assert(near(ev,audit(p,k,f)),"event tree");
    }
    portfolioCases++;
  }
  const examples={};
  for(const [key,p,markets,K,a0,a1,cost] of [
    ["induced",.4,[{w:10,d:.3}],1,.4,.8,.5],
    ["displaced",.6,[{w:10,d:.3}],1,.2,1,.5],
    ["startsDecline",.4,[{w:12,d:0,e:0},{w:9.2,fixed:1,e:1}],1,1,1,0]
  ]){
    const z=(1+p)/2,base=V(p,markets,K,a0,a1,cost),pass=V(p/z,markets,K,a0,a1,cost),fail=V(0,markets,K,a0,a1,cost);
    examples[key]={base,pass,fail,passProbability:z,auditGross:z*pass.val+(1-z)*fail.val-base.val,expectedUpgrade:z*pass.u+(1-z)*fail.u,expectedStarts:z*pass.starts+(1-z)*fail.starts,expectedSuccessor:z*pass.successor+(1-z)*fail.successor};
  }
  assert(examples.induced.base.u===0&&examples.induced.expectedUpgrade>0,"upgrade induced");
  assert(examples.displaced.base.u===1&&examples.displaced.expectedUpgrade<1,"upgrade displaced");
  assert(examples.startsDecline.auditGross>0&&examples.startsDecline.expectedStarts<examples.startsDecline.base.starts,"positive value fewer starts");
  return {checks,graphCases,portfolioCases,examples,field_calibration:false,full_repository_ci:false,scope:"Synthetic finite graph patterns, posterior and independent event-tree enumeration; conditional theory"};
};
const result=check();
if(typeof module!=="undefined" && module.exports) module.exports={check};
if(typeof require!=="undefined" && require.main===module) console.log(JSON.stringify(result,null,2));
