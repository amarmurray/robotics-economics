'use strict';
// Synthetic exact half-unit arithmetic; run with node.
const run = function run() {
  const P=[10,12,14,16], NONE=null;
  let checks=0;
  const eq=(a,b,msg)=>{checks++;if(a!==b)throw Error(msg+": "+a+" != "+b)};
  const choice=(values,offers)=>{
    let best=0, picked=-1;
    for(let j=0;j<2;j++){
      if(offers[j]===NONE)continue;
      const u=values[j]-offers[j];
      if(u>best || (u===best && picked===-1)){best=u;picked=j;}
    }
    return picked;
  };
  const profit=(values,offers,costs,K)=>{
    const j=choice(values,offers);
    return (j===-1?0:offers[j]-costs[j])-K;
  };
  const menus=qual=>{
    const rows=[];
    for(const a of (qual.includes(0)?[NONE,...P]:[NONE]))
      for(const b of (qual.includes(1)?[NONE,...P]:[NONE]))
        rows.push([a,b]);
    return rows;
  };
  const argbest=(w,c,K,q)=>{
    let val=-Infinity,menu=null;
    for(const m of menus(q)){
      const v=profit(w,m,c,K);
      if(v>val){val=v;menu=m;}
    }
    return {profit_halves:val,menu_halves:menu};
  };
  const robust=(W,c,K,q)=>{
    let val=-Infinity,menu=null;
    for(const m of menus(q)){
      const v=Math.min(...W.map(w=>profit(w,m,c,K)));
      if(v>val){val=v;menu=m;}
    }
    return {profit_halves:val,menu_halves:menu};
  };
  const ref=[16,12], c=[6,0];
  const fixed={X:profit(ref,[14,NONE],c,4),G:profit(ref,[NONE,14],c,2),E:profit(ref,[14,14],c,6),R:4};
  eq(fixed.X,4,"fixed X");eq(fixed.G,-2,"fixed G");eq(fixed.E,2,"fixed E");
  const priced={X:argbest(ref,c,4,[0]),G:argbest(ref,c,2,[1]),E:argbest(ref,c,6,[0,1]),R:{profit_halves:4}};
  eq(priced.X.profit_halves,6,"priced X");eq(priced.G.profit_halves,10,"priced G");eq(priced.E.profit_halves,6,"priced E");
  const worlds=[[16,10],[10,16]];
  const worldResults=worlds.map(w=>({X:argbest(w,[2,0],4,[0]),G:argbest(w,[2,0],2,[1])}));
  eq(worldResults[0].X.profit_halves,10,"world1 X");eq(worldResults[0].G.profit_halves,8,"world1 G");
  eq(worldResults[1].X.profit_halves,4,"world2 X");eq(worldResults[1].G.profit_halves,14,"world2 G");
  const supports=[];
  for(const a of [16,17])for(const b of [10,11])supports.push([a,b]);
  const certificate={X:robust(supports,[2,0],4,[0]),G:robust(supports,[2,0],2,[1]),E:robust(supports,[2,0],10,[0,1]),R:{profit_halves:6}};
  eq(certificate.X.profit_halves,10,"robust X");eq(certificate.G.profit_halves,8,"robust G");eq(certificate.E.profit_halves,4,"robust E");
  for(const w of supports){
    eq(profit(w,[16,NONE],[2,0],4),10,"X guaranteed");
    eq(profit(w,[NONE,10],[2,0],2),8,"G guaranteed");
    eq(choice(w,[12,14]),0,"joint A dominance");
  }
  const naiveSeparate=profit([16,16],[14,NONE],[0,0],0)+profit([16,16],[NONE,14],[0,0],0);
  const jointChoice=profit([16,16],[14,14],[0,0],0);
  eq(naiveSeparate,28,"naive separately");eq(jointChoice,14,"exclusive buyer");
  const dualOneBuyer=(lambda)=>2*lambda+Math.max(0,14-lambda);
  const dualTwoBuyer=(lambda)=>lambda+2*Math.max(0,14-lambda);
  eq(Math.min(...Array.from({length:29},(_,j)=>dualOneBuyer(j))),14,"per-buyer dual");
  eq(Math.min(...Array.from({length:29},(_,j)=>dualTwoBuyer(j))),14,"capacity dual");
  for(const w of [[16,12],[16,13],[17,12],[17,13]]) {
    for(const m of menus([0,1])){
      const j=choice(w,m);
      if(j!==-1){checks++;if(w[j]-m[j]<0)throw Error("suboptimal buyer choice");}
      const p=profit(w,m,[2,0],10);
      checks++;if(p>Math.max(0,...m.filter(t=>t!==null))-10)throw Error("gross upper failed");
    }
  }
  return {schema:"joint_choice_robust_pricing_v1",units:"integer half-contribution-units; divide by 2",price_grid_halves:P,checks, fixed,priced,worldResults,certificate,naiveSeparate_halves:naiveSeparate,jointChoice_halves:jointChoice,oneBuyerTwoResourcesDual_halves:14,twoBuyerOneResourceDual_halves:14,interpretation:"All valuations, costs, demand supports and complete qualified recipes are synthetic; verified enumeration is not a scientific novelty or physical experiment."};
};
console.log(JSON.stringify(run(), null, 2));
