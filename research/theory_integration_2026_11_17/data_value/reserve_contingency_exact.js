"use strict";
function run(){
 let assertions=0,laws=0;const ck=(v,m)=>{assertions++;if(!v)throw Error(m)};
 const N=8, results={}; 
 // atoms O,D,S: overload, normal dual's eligible licensed successor, stagger's eligible licensed successor.
 function visit(n,left){if(n.length!==7){for(let i=0;i<=left;i++)visit([...n,i],left-i);return}n=[...n,left];
 const sum=f=>n.reduce((v,c,i)=>v+c*f(i),0),p=sum(i=>i>>2),q=sum(i=>((i>>1)&1)),hs=sum(i=>i&1),j=sum(i=>(i>>2)*(i&1));
 if(p!==2||q!==2||hs!==2||n[6]+n[7]!==0)return;laws++;
 const cell=(o,a)=>sum(i=> (i>>2)!==o?0:a==="F"?4:a==="S"?5+4*(i&1):a==="D"?8+2*((i>>1)&1):8);
 const solve=reserve=>[0,1].reduce((v,o)=>v+Math.max(...(o===0?["F","S","D"]:reserve?["F","S","K"]:["F","S"]).map(a=>cell(o,a))),0)-5*N-(reserve?7:0);
 const G=solve(false),GK=solve(true),Rk=4*N-7,E=3*N;
 ck(G===22+4*j,"G formula");ck(GK===20+Math.max(8,2+4*j)-7,"GK formula");ck(Math.max(G,GK,Rk,E,0)===Math.max(G,Rk),"combined dominated");
 ck(sum(i=>5+4*(i&1))===48,"forced stagger identical");
 ck(GK-G===Math.max(0,6-4*j)-7,"option formula");
 ck((G>Rk)===(j>=1),"rank exact grid");
 results[j]={G:G/N,GK:GK/N,Rk:Rk/N,E:E/N,forcedStagger:6,witness:n};
 }
 visit([],N);ck(Object.keys(results).length===3,"sharp endpoint support");
 ck(results[0].G===2.75&&results[2].G===3.75&&results[0].Rk===3.125,"endpoint values");
 // Verify the contrast and positive-part transport bound independently across finite arbitrary cell values.
 let transport=0;for(let a=-4;a<=4;a++)for(let b=-4;b<=4;b++)for(let c=-4;c<=4;c++)for(let e=-4;e<=4;e++){const ideal=Math.max(0,b-a),actual=Math.max(c,e)-a;ck(Math.abs(actual-ideal)<=Math.max(Math.abs(c-a),Math.abs(e-b)),"max Lipschitz transport");transport++}
 return {synthetic:true,assertions,laws,transportCases:transport,grid:results,sharp_j:[0,.25],threshold_j:3/32}
}
console.log(JSON.stringify(run(),null,2));
