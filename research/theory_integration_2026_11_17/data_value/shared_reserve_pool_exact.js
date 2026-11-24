"use strict";
function run(){
 let assertions=0,cases=0,laws=0;const ck=(a,m)=>{assertions++;if(!a)throw Error(m)};
 const masks=n=>Array.from({length:1<<n},(_,i)=>i),count=m=>m.toString(2).replace(/0/g,"").length;
 const opt=(w,k,pen=()=>0)=>Math.max(...masks(w.length).filter(m=>count(m)<=k).map(m=>w.reduce((s,x,i)=>s+((m>>i)&1)*x,0)+pen(m)));
 const top=(w,k)=>w.map(x=>Math.max(0,x)).sort((a,b)=>b-a).slice(0,k).reduce((a,b)=>a+b,0);
 for(let a=-1;a<=3;a++)for(let b=-1;b<=3;b++)for(let c=-1;c<=3;c++){
 const w=[a,b,c];for(let k=0;k<=3;k++){const v=opt(w,k);ck(v===top(w,k),"top-k");ck(v===Math.min(...[0,...w.filter(x=>x>=0)].map(l=>k*l+w.reduce((s,x)=>s+Math.max(0,x-l),0))),"dual");for(let q=-2;q<=2;q++){ck(Math.abs(opt(w,k,m=>count(m)>=2?q:0)-v)<=Math.abs(q),"residual");cases++}}
 for(let k=1;k<3;k++)ck(top(w,k)-top(w,k-1)>=top(w,k+1)-top(w,k),"concavity")}
 const N=64,den=16*N,old=[N/2,0,0,N/2],oldPool=old.reduce((s,n,m)=>s+n*(m?64:0),0),oldNet=oldPool-38*N;
 const cG=6*N,G=Math.max(4*N-cG,-cG),oldFallback=oldNet-cG,E=N;ck(oldNet/den===-3/8,"old K");ck(G/den===-1/8,"trained base");ck(oldFallback/den===-3/4,"retained version");
 const rows=[];
 for(let p=0;p<=N;p++)for(let q=0;q<=N;q++)for(let j=Math.max(0,p+q-N);j<=Math.min(p,q);j++){
 const ns=[N-p-q+j,p-j,q-j,j];laws++;
 const pool=ns.reduce((s,n,m)=>s+n*Math.max(0,...[0,1,2].filter(a=>!a||(m&a)).map(a=>a===0?0:m===3?48:56)),0);
 ck(pool===56*(p+q)-64*j,"pooled identity");ck(pool<=56*(p+q),"isolated upper in penalty model");
 const trained=G+pool-38*N,GK=Math.max(trained,oldFallback),menu=Math.max(0,G,GK,E,oldNet);
 ck(GK>=oldFallback,"old policy retained");
 if(p===24&&q===24){ck(trained===2*N-64*j,"trained formula");ck(menu===Math.max(E,GK),"menu");ck((GK>E)===(j<1),"ranking");ck((GK===E)===(j===1),"tie");if(j===0||j===1||j===10||j===24)rows.push({j:j/N,expectedCalls:(p+q)/N,poolGross:pool/den,G:G/den,trainedVersion:trained/den,GK:GK/den,E:E/den,crossDifference:(GK-G-oldNet)/den,best:GK>E?"G+K":GK===E?"tie":"E"})}
 }
 ck(rows[0].GK===1/8&&rows[0].crossDifference===5/8,"disjoint");ck(rows.at(-1).GK===-3/4&&rows.at(-1).crossDifference===-1/4,"synchronized");ck(rows[0].poolGross>oldPool/den,"higher first slot");ck(56*48<64*64,"lower isolated call value");
 const joint=k=>opt([0,0],k,m=>m===3?3:0);ck(joint(1)-joint(0)===0&&joint(2)-joint(1)===3,"nonconcave joint recipe");
 return {assertions,cases,laws,den,oldPoolGross:oldPool/den,oldReserveNet:oldNet/den,rows,scope:"synthetic exact integer enumeration, retained ex ante old version; no full CI or field evidence"}
}
if(typeof module!=="undefined")module.exports=run;
if(typeof require!=="undefined"&&require.main===module)console.log(JSON.stringify(run(),null,2));
