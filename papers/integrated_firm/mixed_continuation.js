'use strict';
// Exact mixed continuation in the accepted S=10 four-block game.
function makeStudy(base,w,a){
 const accelerate=new Function(a.slice(a.indexOf("function acceleratedSource("),a.indexOf("\nconst compact="))+";return acceleratedSource;")();let s=accelerate(base,w);
 function patch(a,b){if(!s.includes(a))throw Error("source mismatch: "+a);s=s.replace(a,b)}
 patch("let scale=16**h;", "let scale=16**h*F[h];");
 patch("v0+=w*u*t[0];v1+=w*u*t[1]","v0+=w*u*t[0]*F[h]/F[h-1];v1+=w*u*t[1]*F[h]/F[h-1]");
 patch("if(!e)throw Error(\"no pure equilibrium \"+id);",`if(!e){
 let mat=aa.map(a=>bb.map(b=>value(a,b))),candidates=[];
 const gcd=(a,b)=>b?gcd(b,a%b):Math.abs(a);
 const frac=(n,d)=>{if(d<0){n=-n;d=-d}if(!d)return [0,0];let g=gcd(n,d);return [n/g,d/g]};
 const u=(x,y,n,d)=>{let v=(d-n)*x+n*y;if(!Number.isSafeInteger(v))throw Error("precision");return v};
 for(let i=0;i<aa.length;i++)for(let k=i+1;k<aa.length;k++)for(let j=0;j<bb.length;j++)for(let l=j+1;l<bb.length;l++){
  let a=mat[i][j],b=mat[i][l],c=mat[k][j],d=mat[k][l];
  let [qn,qd]=frac(c[0]-a[0],b[0]-a[0]-d[0]+c[0]),[pn,pd]=frac(b[1]-a[1],c[1]-a[1]-d[1]+b[1]);
  if(!(qn>0&&qn<qd&&pn>0&&pn<pd))continue;
  let v0=u(a[0],b[0],qn,qd),v1=u(a[1],c[1],pn,pd);
  if(mat.some(row=>u(row[j][0],row[l][0],qn,qd)>v0)||mat[i].some((_,z)=>u(mat[i][z][1],mat[k][z][1],pn,pd)>v1))continue;
  candidates.push({i,k,j,l,pn,pd,qn,qd,v:[v0/qd,v1/pd],matrix:[a,b,c,d].map(v=>v.map(x=>x/scale))});
 }
 if(!candidates.length)throw Error("no pure equilibrium and no certified 2x2 "+id);
 if(candidates.some(m=>!m.v.every(Number.isSafeInteger)))throw Error("no pure equilibrium candidate scale gap "+id);
 candidates.sort((a,b)=>rule*(b.v[0]+b.v[1]-a.v[0]-a.v[1])||b.v[0]-a.v[0]);
 const m=candidates[0],{i,k,j,l,pn,pd,qn,qd}=m,den=pd*qd;
 if(F[h]/F[h-1]%den!==0)throw Error("no pure equilibrium scale gap "+JSON.stringify({id,m,den}));
 let gap0=-Infinity,gap1=-Infinity;
 for(const a of ga.all){gap0=Math.max(gap0,u(value(a,bb[j])[0],value(a,bb[l])[0],qn,qd)-m.v[0]*qd);fullDev++}
 for(const b of gb.all){gap1=Math.max(gap1,u(value(aa[i],b)[1],value(aa[k],b)[1],pn,pd)-m.v[1]*pd);fullDev++}
 if(gap0!==0||gap1!==0)throw Error("unreduced mixed deviation");
 let mix=[];for(const [x,p] of [[i,pd-pn],[k,pn]])for(const [y,q] of [[j,qd-qn],[l,qn]])mix.push({a:aa[x].a,b:bb[y].a,w:p*q});
 let feeCertificate=null;
 if(id==="3,1,0,0,0,0,0,1348,1,1,1,0,0,0,0,0,1348,1,1"&&rule===1){
  if(JSON.stringify(m.matrix)!==JSON.stringify([[133,128],[130.5,131],[132.25,129.25],[131,129.125]]))throw Error("unexpected certificate matrix");
  feeCertificate=[];
  for(const [fn,fd,qn,qd,pn,pd] of [[0,1,3,5,24,25],[1,2,1,1,4,5]]){
   const U=a=>u(fd*value(a,bb[j])[0]-fn*scale*a.a.ng,fd*value(a,bb[l])[0]-fn*scale*a.a.ng,qn,qd);
   const W=b=>u(fd*value(aa[i],b)[1]-fn*scale*b.a.ng,fd*value(aa[k],b)[1]-fn*scale*b.a.ng,pn,pd);
   const g0=ga.all.map(a=>U(aa[i])-U(a)),g1=gb.all.map(b=>W(bb[j])-W(b));
   if(U(aa[i])!==U(aa[k])||W(bb[j])!==W(bb[l])||Math.min(...g0,...g1)<0)throw Error("fee certificate");
   feeCertificate.push({fee:[fn,fd],p:[pn,pd],q:[qn,qd],slack_numerators:[g0,g1],slack_denominators:[fd*qd*scale,fd*pd*scale]});
  }
 }
 let result={v:m.v,mix,cert:{den},n:0};MIX.push({id,scale,m,den,mix,candidates:candidates.length,checked:[ga.all.length,gb.all.length],max_deviation_numerator:[gap0,gap1],feeCertificate});memo.set(id,result);return result;
 }`);
 patch("mixDen=root.cert?.den??1","mixDen=1");
 patch("let h=c.T-t,nd=new Map()","let h=c.T-t,dateDen=F[h]/F[h-1],nd=new Map()");
 patch("let w=baseWeight*profile.w;","let w=baseWeight*profile.w*dateDen/(e.cert?.den??1);if(!Number.isSafeInteger(w))throw Error('weight precision');");
 patch("let wt=w/(mixDen*16**t)","let wt=w/(mixDen*dateDen*16**t)");
 patch("}}if([...nd.values()]", "}}mixDen*=dateDen;if([...nd.values()]");
 patch("for(let i=0;i<2;i++)if(wealth[i]", "if(![...wealth,...cash,den].every(Number.isSafeInteger))throw Error('ledger precision');for(let i=0;i<2;i++)if(wealth[i]");
 s="const F=[1,1,1,125,125],MIX=[];"+s;
 return new Function(s+";return {windowStudy,MIX}")();
}
function run(base,w,a,concurrent=false,cap=2,rule=1){
 const s=makeStudy(base,w,a);
 const result=s.windowStudy({N:5,early:[1,1,5],entry:3,kitPrice:4,concurrent,only:["scale_"+cap],rules:[rule],license:100,contractDev:100,developCompute:1,developBase:3,budget:30000000}).results[0];
 return {spec:{concurrent,cap,rule},result,mixed_subgames:s.MIX};
}
const hashes={"service_window.js":"eee77cfda63e9e61478026e57a15f50d0f7545cb6300337615c9c5bedce5370f","staggered_window.js":"9e705e070964de703383f2c75d7b3c89b9f868427e47a19ac86ef72e4068efae","concurrent_window.js":"cd32e8e36e21d31f716fb427553649277644e6306227aeff0c6efc3de8556de7"};
if(typeof module!=='undefined'){module.exports={makeStudy,run};if(require.main===module){const fs=require('fs'),path=require('path'),crypto=require('crypto');const src=Object.entries(hashes).map(([n,h])=>{const s=fs.readFileSync(path.join(__dirname,n),'utf8');if(crypto.createHash('sha256').update(s).digest('hex')!==h)throw Error('changed '+n);return s});const expected=JSON.parse(fs.readFileSync(path.join(__dirname,'mixed_continuation_results.json'),'utf8'));for(const e of expected.runs){const {concurrent,cap,rule}=e.spec;const got=run(...src,concurrent,cap,rule);if(JSON.stringify(got)!==JSON.stringify(e))throw Error('replay mismatch '+JSON.stringify(e.spec));}console.log('verified '+expected.runs.length+' runs');}}
