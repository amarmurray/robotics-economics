function run(){
 let checks=0,cases=0;
 const ok=x=>{if(!x)throw Error("assert "+checks);checks++};
 const pc=x=>{let n=0;while(x){x&=x-1;n++}return n};
 const rows={};
 for(let n=1;n<=6;n++){
  const m=1<<n; const groups={};
  for(let w1=0;w1<m;w1++)for(let w0=w1;;w0=(w0-1)&w1){
   for(let s=0;s<m;s++){
    const a=pc(w0),b=pc(w1),z=pc(s),j=pc(w1&s);
    const v=[0,a,j,b],delta=v[3]-v[2]-v[1]+v[0];
    ok(delta===pc((w1^w0)&~s)-pc(w0&s));
    ok(delta>=b-a-Math.min(b,z)&&delta<=b-a-Math.max(0,b+z-n));
    const key=[a,b,z].join(",");const g=groups[key]??[Infinity,-Infinity];g[0]=Math.min(g[0],delta);g[1]=Math.max(g[1],delta);groups[key]=g;cases++;
   }
   if(!w0)break;
  }
  for(const [k,[lo,hi]] of Object.entries(groups)){const [a,b,z]=k.split(",").map(Number);ok(lo===b-a-Math.min(b,z));ok(hi===b-a-Math.max(0,b+z-n))}
  rows[n]=Object.keys(groups).length;
 }
 const examples=[0b11000001,0b00000111].map(s=>{const w0=15,w1=63,n=8,v=8,cG=4,j=pc(w1&s);return {w0,w1,s,counts:[pc(w0),pc(w1),pc(s),j],net:{P:0,G:v*pc(w0)/n-cG,C:v*j/n,CG:v*pc(w1)/n-cG},interaction:v*(pc(w1)-pc(w0)-j)/n}});
 ok(examples[0].net.CG>examples[0].net.C);ok(examples[1].net.CG<examples[1].net.C);
 // Arbitrary baseline routine and incremental G readiness: check pointwise identity.
 for(let k=0;k<64;k++){
  const [H,L,T,S,W0,B]=Array.from({length:6},(_,i)=>(k>>i)&1);const W1=W0|B;
  const q=(c,g)=>H*(L|(c&S)|(g&T))*(c?W1:W0);
  ok(q(1,1)-q(1,0)-q(0,1)+q(0,0)===H*(1-L)*T*((W1-W0)*(1-S)-W0*S));
 }
 return {checks,cases,groupsByN:rows,examples,scope:"synthetic integer enumeration; no field calibration"};
}
if(typeof module!=='undefined')module.exports=run;
if(typeof require!=='undefined'&&require.main===module)console.log(JSON.stringify(run(),null,2));
