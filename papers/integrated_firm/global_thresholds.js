// Exact global best responses in the accepted four-block economy.
// Parameter path: (1,1,floor(S/2),ceil(S/2)), entry date 3, kit price 4.
// CPU only; no new technology, payoff premium, or fitted coefficient.
'use strict';
const fs=require('fs'),path=require('path'),crypto=require('crypto');
const sourceHashes={
 'service_window.js':'eee77cfda63e9e61478026e57a15f50d0f7545cb6300337615c9c5bedce5370f',
 'staggered_window.js':'9e705e070964de703383f2c75d7b3c89b9f868427e47a19ac86ef72e4068efae',
 'concurrent_window.js':'cd32e8e36e21d31f716fb427553649277644e6306227aeff0c6efc3de8556de7'
};
function source(name){const s=fs.readFileSync(path.join(__dirname,name),'utf8');if(crypto.createHash('sha256').update(s).digest('hex')!==sourceHashes[name])throw Error('Changed antecedent: '+name);return s;}
function makeStudy(requestMixed=false){
 const a=source('concurrent_window.js');
 const accelerate=new Function(a.slice(a.indexOf('function acceleratedSource('),a.indexOf('\nconst compact='))+';return acceleratedSource;')();
 let s=accelerate(source('service_window.js'),source('staggered_window.js'));
 function patch(a,b){if(!s.includes(a))throw Error('Diagnostic source mismatch: '+a);s=s.replace(a,b);}
 patch('let e=null,n=0;for(let i=0;i<aa.length;i++)', 'let rootEquilibria=[];let e=null,n=0;for(let i=0;i<aa.length;i++)');
 patch('continue;n++;', 'continue;n++;if(h===c.T)rootEquilibria.push({generated_wealth:v.map(x=>x/scale),a:aa[i].a,b:bb[j].a});');
 patch('let result={v:e.v,a:aa[e.i].a,b:bb[e.j].a,n};', `
  let rootDiagnostic=null,rootMixed=null;
  if(h===c.T){
   const plain=a=>a.a.q===1&&a.a.b[0]==='order'&&a.a.r[0]==='none'&&a.a.keep===0&&a.a.ng===0;
   const learn=a=>a.a.q===1&&a.a.b[0]==='order'&&a.a.r[0]==='develop'&&a.a.keep===1&&a.a.ng===1;
   const left=[aa.find(plain),aa.find(learn)],right=[bb.find(plain),bb.find(learn)];
   if([...left,...right].every(Boolean)){
    const v=left.map(a=>right.map(b=>value(a,b)));
    rootDiagnostic=v.map(row=>row.map(w=>w.map(x=>x/scale)));
    const gcd=(a,b)=>b?gcd(b,a%b):Math.abs(a);
    const fraction=(n,d)=>{if(d<0){n=-n;d=-d;}const g=gcd(n,d)||1;return {n:n/g,d:d/g};};
    const q=fraction(v[1][0][0]-v[0][0][0],v[0][1][0]-v[0][0][0]-v[1][1][0]+v[1][0][0]);
    const p=fraction(v[0][1][1]-v[0][0][1],v[1][0][1]-v[0][0][1]-v[1][1][1]+v[0][1][1]);
    if(p.d>0&&q.d>0&&p.n>0&&p.n<p.d&&q.n>0&&q.n<q.d){
     const target0=(q.d-q.n)*v[0][0][0]+q.n*v[0][1][0];
     const target1=(p.d-p.n)*v[0][0][1]+p.n*v[1][0][1];
     let gap0=-Infinity,gap1=-Infinity;
     for(const a of ga.all){let u=(q.d-q.n)*value(a,right[0])[0]+q.n*value(a,right[1])[0];if(!Number.isSafeInteger(u))throw Error('mixed precision');gap0=Math.max(gap0,u-target0);}
     for(const b of gb.all){let u=(p.d-p.n)*value(left[0],b)[1]+p.n*value(left[1],b)[1];if(!Number.isSafeInteger(u))throw Error('mixed precision');gap1=Math.max(gap1,u-target1);}
     const mix=[];let num=[0,0];
     for(let i=0;i<2;i++)for(let j=0;j<2;j++){
      const w=(i?p.n:p.d-p.n)*(j?q.n:q.d-q.n);mix.push({a:left[i].a,b:right[j].a,w});
      for(let k=0;k<2;k++)num[k]+=w*v[i][j][k];
     }
     if(!num.every(Number.isSafeInteger))throw Error('mixed total precision');
     rootMixed={valid:gap0===0&&gap1===0,probability_research:[p,q],den:p.d*q.d,mix,num,generated_wealth:num.map(x=>x/(p.d*q.d*scale)),max_deviation_numerator:[gap0,gap1],deviation_denominator:[q.d*scale,p.d*scale],checked_actions:[ga.all.length,gb.all.length]};
    }
   }
  }
  let result={v:e.v,a:aa[e.i].a,b:bb[e.j].a,n,rootEquilibria,rootDiagnostic,rootMixed};
  if(REQUEST_MIXED&&h===c.T){if(!rootMixed?.valid)throw Error('No certified two-action root mix');result={...result,v:rootMixed.num.map(x=>x/rootMixed.den),num:rootMixed.num,mix:rootMixed.mix,cert:{den:rootMixed.den}};}
 `);
 s='const REQUEST_MIXED='+JSON.stringify(requestMixed)+';\n'+s;
 patch('root:root.mix??[root.a,root.b],', 'root:root.mix??[root.a,root.b],root_equilibria:root.rootEquilibria,root_diagnostic:root.rootDiagnostic,root_mixed_certificate:root.rootMixed,');
 return new Function(s+';return windowStudy;')();
}
function summarize(r){
 const sum=k=>r.dated?.reduce((s,row)=>s+row[k],0);
 return {...r,generated_wealth:r.wealth?.map(w=>w-10000),totals:r.status==='solved'?Object.fromEntries(['jobs','customer_surplus','develop','internal','orders','assembly','licenses','successor','retain'].map(k=>[k,sum(k)])):null};
}
function solve(n,concurrent=true,cap=2,rule=1){
 if(!Number.isInteger(n)||n<1||n>337)throw Error('n outside funded integer domain [1,337]');
 return {n,...solveShifts(2*n+1,concurrent,cap,rule)};
}
function solveShifts(S,concurrent=true,cap=2,rule=1,requestMixed=false){
 if(!Number.isInteger(S)||S<2||12*(S+2)+3*620>10000)throw Error('S outside funded integer domain');
 const early=[1,1,Math.floor(S/2)],N=S-early[2],study=makeStudy(requestMixed);
 const result=study({N,early,entry:3,kitPrice:4,concurrent,only:['scale_'+cap],rules:[rule],license:100,contractDev:100,developCompute:1,developBase:3,budget:30000000}).results[0];
 return {later_shifts:S,calendar:[...early,N],concurrent,cap,rule,requestMixed,...summarize(result)};
}
function record(r,kind='primary'){
 const spec={S:r.later_shifts,concurrent:r.concurrent,cap:r.cap,rule:r.rule,requestMixed:r.requestMixed??false};
 const fields=['status','reason','generated_wealth','wealth_numerator','wealth_denominator','totals','dated','profiles','states','deviations','fullDev','kernelPairs'];
 if(kind==='selection')fields.push('root_equilibria','root_diagnostic');
 if(kind==='mixed')fields.push('root_mixed_certificate');
 return {spec,result:Object.fromEntries(fields.filter(k=>r[k]!==undefined).map(k=>[k,r[k]]))};
}
function reproduce(group='all'){
 const expected=JSON.parse(fs.readFileSync(path.join(__dirname,'global_thresholds_results.json'),'utf8'));
 const kinds=group==='all'?['primary','selection','mixed']:[group],cache=new Map();let checked=0;
 for(const kind of kinds){
  if(!expected[kind])throw Error('Unknown result group '+kind);
  for(const item of expected[kind]){
   const key=JSON.stringify(item.spec);let result=cache.get(key);
   if(!result){const c=item.spec;result=solveShifts(c.S,c.concurrent,c.cap,c.rule,c.requestMixed);cache.set(key,result);}
   if(JSON.stringify(record(result,kind))!==JSON.stringify(item))throw Error('Replay mismatch '+kind+' '+key);
   checked++;process.stderr.write('verified '+kind+' '+key+'\n');
  }
 }
 return {status:'verified',group,records:checked,distinct_solves:cache.size};
}
module.exports={solve,solveShifts,sourceHashes,record,reproduce};
if(require.main===module){
 if(process.argv[2]==='--reproduce')console.log(JSON.stringify(reproduce(process.argv[3]||'all'),null,2));
 else if(process.argv[2]==='--shifts')console.log(JSON.stringify(solveShifts(Number(process.argv[3]),process.argv[4]!=='exclusive',Number(process.argv[5]||2),Number(process.argv[6]||1),process.argv[7]==='mixed'),null,2));
 else {const n=Number(process.argv[2]||4),concurrent=process.argv[3]!=='exclusive',cap=Number(process.argv[4]||2),rule=Number(process.argv[5]||1);console.log(JSON.stringify(solve(n,concurrent,cap,rule),null,2));}
}
