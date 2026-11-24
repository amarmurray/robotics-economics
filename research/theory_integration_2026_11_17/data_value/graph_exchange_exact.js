"use strict";
function run(){
 let assertions=0;const ck=(b,m)=>{assertions++;if(!b)throw Error(m)};
 const edges=[[0,2],[0,3],[1,2],[1,3]],bits=m=>edges.map((_,i)=>i).filter(i=>m>>i&1),ok=m=>{const a=bits(m).flatMap(i=>edges[i]);return new Set(a).size===a.length};
 const matches=Array.from({length:16},(_,i)=>i).filter(ok),weight=(m,w)=>bits(m).reduce((a,i)=>a+w[i],0);
 const best=(mask,w,cap=2)=>Math.max(...matches.filter(m=>(m&mask)===m&&bits(m).length<=cap).map(m=>weight(m,w)));
 const comp=(M,N)=>{let rem=M^N,cs=[];while(rem){let g=rem&-rem;let grow=true;while(grow){let old=g;for(const i of bits(rem))if(bits(g).some(j=>edges[i].some(v=>edges[j].includes(v))))g|=1<<i;grow=old!==g}cs.push(g);rem^=g}return cs};
 let graphCases=0;
 for(let old=0;old<16;old++)for(let neu=old;neu<16;neu++)if((old&neu)===old)
 for(let z=0;z<81;z++){let w=edges.map((_,i)=>Math.floor(z/3**i)%3);let wo=w.map((v,i)=>v+(i===0?-1:0));
 const M=matches.find(m=>(m&old)===m&&weight(m,wo)===best(old,wo));const anchor=weight(M,w);let exchange=0;
 for(const N of matches)if((N&neu)===N){let C=comp(M,N);let gain=0;for(const g of C){ck(ok(M^g),"component feasible");gain+=Math.max(0,weight(M^g,w)-anchor)}
 const use=C.filter(g=>weight(M^g,w)>anchor).reduce((a,g)=>a^g,M);ck(ok(use)&&(use&neu)===use,"positive components compose");ck(weight(use,w)-anchor===gain,"gain additive");exchange=Math.max(exchange,gain);}
 ck(best(neu,w)-best(old,wo)===anchor-best(old,wo)+exchange,"exchange identity");graphCases++;}
 let laws=0;const N=16,pos=x=>Math.max(0,x);
 for(let q=0;q<=N;q++)for(let b=0;b<=N;b++)for(let x=Math.max(0,q+b-N);x<=Math.min(q,b);x++){laws++;
 for(let s of [0,2,16]){const gain=16-s,expected=pos(gain*x-4*q);
 let maxPolicy=0;for(let a=0;a<2;a++)for(let b=0;b<2;b++)maxPolicy=Math.max(maxPolicy,a*(gain*x-4*q)-b*4*(N-q));
 ck(expected===maxPolicy,"nonanticipating policy");
 for(let A=0;A<2;A++)for(let B=0;B<2;B++){let mask=1+(A?2:0)+(B?4:0);ck(best(mask,[16+s,16,16,0])===16+s+gain*A*B,"weighted complement");ck(best(mask,[16+s,16,16,0],1)===16+s,"parent cap");}}}
 const value=x=>pos(pos(16*x-32)-16)/256;
 ck(value(0)===0&&value(4)===1/16&&value(8)===5/16,"three laws");
 ck(value(4)<1/8&&value(8)>1/4&&value(7)===1/4&&value(6)<1/4,"strict cutoff");
 ck(best(9,[16,0,0,16],1)===16&&best(9,[16,0,0,16],2)===32,"parent cap invalidates disjoint local flips");
 return {synthetic:true,assertions,graphCases,probabilityLaws:laws,grounding:[value(0),value(4),value(8)],strengthening:1/8,independentEmbodiment:1/4,groundingThresholdIntersection:7/16,combinedGroundingIncrementWhenStrengthened:(14*8-32-16)/256};
}
console.log(JSON.stringify(run(),null,2));
