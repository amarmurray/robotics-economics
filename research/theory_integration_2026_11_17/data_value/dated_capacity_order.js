function run(){
 const INF=1e9;let checks=0,cases=0;function ok(x){checks++;if(!x)throw Error("check "+checks)}
 function permutations(a){return a.length===0?[[]]:a.flatMap((x,i)=>permutations(a.filter((_,j)=>j!==i)).map(t=>[x,...t]))}
 function feasible(n,edges){const d=Array.from({length:n},(_,i)=>Array.from({length:n},(_,j)=>i===j?0:INF));for(const [u,v,w] of edges)d[u][v]=Math.min(d[u][v],w);for(let k=0;k<n;k++)for(let i=0;i<n;i++)for(let j=0;j<n;j++)if(d[i][k]<INF&&d[k][j]<INF)d[i][j]=Math.min(d[i][j],d[i][k]+d[k][j]);return {yes:d.every((r,i)=>r[i]>=0),d}}
 function box(edges,id,l,u){edges.push([0,id,u],[id,0,-l])}
 function diff(edges,a,b,l,u){edges.push([a,b,u],[b,a,-l])}
 function orderEdges(order,panel){return order.slice(1).map((v,i)=>[panel[v],panel[order[i]],0])}
 const orders=permutations([0,1]);
 function ordered(panelEdges){return orders.filter(o=>panelEdges.every(e=>feasible(5,[...e,...orderEdges(o,[1,2]),...orderEdges(o,[3,4])]).yes))}
 let seed=31721;const r=n=>{seed=(Math.imul(seed,1664525)+1013904223)>>>0;return seed%n};
 for(let c=0;c<1200;c++){
  const edges=[];for(let i=1;i<=4;i++){const l=r(4),u=l+r(4-l);box(edges,i,l,u)}
  for(const [a,b] of [[1,3],[2,4],[1,2],[3,4]]){const l=r(7)-3,u=l+r(4);diff(edges,a,b,l,u)}
  const all=feasible(5,edges);let brute=false;const possible=[false,false];let lo=Infinity,hi=-Infinity;
  for(let a=0;a<4;a++)for(let b=0;b<4;b++)for(let c=0;c<4;c++)for(let d=0;d<4;d++){const x=[0,a,b,c,d];if(edges.every(([u,v,w])=>x[v]-x[u]<=w)){brute=true;lo=Math.min(lo,d-c);hi=Math.max(hi,d-c);if(a<=b&&c<=d)possible[0]=true;if(b<=a&&d<=c)possible[1]=true}}
  ok(all.yes===brute);const actual=ordered([edges]);ok(actual.some(o=>o[0]===0)===possible[0]);ok(actual.some(o=>o[0]===1)===possible[1]);if(brute){ok(all.d[3][4]===hi);ok(-all.d[4][3]===lo)}cases++
 }
 const make=(a,b)=>{const e=[];for(let i=1;i<=4;i++)box(e,i,i<=2?4:4,i<=2?6:12);diff(e,1,3,a[0],a[1]);diff(e,2,4,b[0],b[1]);return e};
 const e1=make([5,6],[0,1]),e2=make([0,1],[5,6]);const p1=feasible(5,e1),p2=feasible(5,e2);
 ok(-p1.d[3][4]===2);ok(-p2.d[4][3]===2);ok(ordered([e1,e2]).length===0);
 const nested=[[[4,8],[8,8]],[[4,4],[4,8]]];ok(nested.every(p=>p[1].every((v,i)=>v>=p[0][i])));ok(nested[0][0][1]-nested[0][0][0]>nested[0][1][1]-nested[0][1][0]);ok(nested[1][0][1]-nested[1][0][0]<nested[1][1][1]-nested[1][1][0]);
 // Exact two-date integer recipes; a late slot cannot replace early capacity or late inspection.
 function production(late,qualified,support){let best=0;for(let x=0;x<=1;x++)for(let y=0;y<=1;y++)if(y<=late&&y<=support&&y<=qualified)best=Math.max(best,4*x+6*y);return best}
 const levels=[0,1].map(m=>[0,1].map(i=>[0,1].map(k=>production(k,+(m===i),1))));
 ok(JSON.stringify(levels)===JSON.stringify([[[4,10],[4,4]],[[4,4],[4,10]]]));ok(production(1,1,0)===4);
 return {checks,cases,interval_panel1_min_A_minus_B:-p1.d[3][4],interval_panel2_min_B_minus_A:-p2.d[4][3],compatible_orders:ordered([e1,e2]),nested_levels:nested,dated_recipe_levels:levels,field_calibration:false,full_repository_ci:false}
}
console.log(JSON.stringify(run(), null, 2));
