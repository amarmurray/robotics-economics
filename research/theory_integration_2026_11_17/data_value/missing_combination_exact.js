function checkModel(){
 const types=[[0,0,0,0,0,0],[0,1,0,0,0,0],[0,1,0,0,0,1],[0,1,0,0,1,1],[1,1,0,0,0,0],[1,1,0,0,1,1],[1,1,0,1,0,1],[1,1,0,1,1,1],[1,1,1,1,1,1]];
 let checks=0,cases=0,groups=0,strata=0,examples=[];
 const assert=x=>{checks++;if(!x)throw Error("assertion "+checks)};
 for(let n=1;n<=10;n++){
 const a=new Map(),b=new Map();
 function visit(i,left,tot,u,counts){
 if(i===types.length-1){
 const z=tot.map((x,j)=>x+left*types[i][j]),v=u+left*types[i][0]*types[i][4],cc=[...counts,left];cases++;
 const [f0,f1,p,g,c,h]=z,d=f1-f0;
 assert(h>=Math.max(g,c)&&h<=Math.min(f1,c+g-p+d));
 assert(h>=c+Math.max(0,g-v)&&h<=c+Math.min(g-p,f0-v)+d-c+v);
 for(const [map,key] of [[a,[f0,f1,p,g,c].join(",")],[b,[f0,f1,p,g,c,v].join(",")]]){
 const x=map.get(key)??new Set();x.add(h);map.set(key,x);
 }
 if(n===8&&f0===6&&f1===8&&p===2&&g===4&&c===5&&(h===5||h===8)&&!examples.some(e=>e.h===h))examples.push({h,counts:cc,u:v,net:{P:2,G:2.5,C:5,CG:h-1.5},types});
 return;
 }
 for(let k=0;k<=left;k++)visit(i+1,left-k,tot.map((x,j)=>x+k*types[i][j]),u+k*types[i][0]*types[i][4],[...counts,k]);
 }
 visit(0,n,[0,0,0,0,0,0],0,[]);
 for(const [key,hs] of a){groups++;const [f0,f1,p,g,c]=key.split(",").map(Number),lo=Math.max(g,c),hi=Math.min(f1,c+g-p+f1-f0);assert(hs.size===hi-lo+1);for(let h=lo;h<=hi;h++)assert(hs.has(h))}
 for(const [key,hs] of b){strata++;const [f0,f1,p,g,c,u]=key.split(",").map(Number),lo=c+Math.max(0,g-u),hi=c+Math.min(g-p,f0-u)+f1-f0-c+u;assert(hs.size===hi-lo+1);for(let h=lo;h<=hi;h++)assert(hs.has(h))}
 }
 assert(examples.length===2);assert(examples.some(e=>e.net.CG<e.net.C)&&examples.some(e=>e.net.CG>e.net.C));
 return {checks,cases,groups,strata,examples,scope:"Exact equal-mass finite response-type enumeration, n=1..10; synthetic, not empirical or proof"};
}
console.log(JSON.stringify(checkModel(),null,2));
