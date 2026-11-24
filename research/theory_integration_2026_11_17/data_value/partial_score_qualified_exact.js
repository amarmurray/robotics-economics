function run(){
 let checks=0; const ok=x=>{if(!x)throw Error("assert "+checks);checks++};const tol=1e-10;
 function bounds(m,n,strict){const d=1-(strict?0.5:1)/n;return [Math.max(0,(m-d)/(1-d)),Math.min(1,m/(strict?1:.5))];}
 function exhaustive(m,n,strict){let lo=Infinity,hi=-Infinity;const pts=[];for(let z=0;z<=n;z++)for(let h=0;h<=n-z;h++){const s=(n-z-h/2)/n,p=+(strict?z===0&&h===0:z===0);pts.push([s,p]);}for(const [s,p] of pts)for(const [t,q] of pts){if(Math.abs(s-t)<tol){if(Math.abs(m-s)<tol){lo=Math.min(lo,p,q);hi=Math.max(hi,p,q);}continue;}const w=(m-t)/(s-t);if(w>=-tol&&w<=1+tol){const x=w*p+(1-w)*q;lo=Math.min(lo,x);hi=Math.max(hi,x);}}return [lo,hi];}
 let cases=0;for(let n=1;n<=8;n++)for(let i=0;i<=100;i++)for(const strict of [true,false]){const a=bounds(i/100,n,strict),b=exhaustive(i/100,n,strict);ok(Math.abs(a[0]-b[0])<tol);ok(Math.abs(a[1]-b[1])<tol);cases++;}
 const scores={SFT:[.64,.66,.70,.70],RECAP:[.84,.82,.71,.70],HG_DAgger:[.60,.66,.76,.90],LWD_offline:[.72,.74,.83,.86],LWD_online:[.89,.90,.93,.92]};
 const rows=Object.entries(scores).map(([method,a])=>({method,mean:a.reduce((s,x)=>s+x,0)/4,strict_n8:a.map(m=>bounds(m,8,true)),positive_n8:a.map(m=>bounds(m,8,false)),strict_n5:a.map(m=>bounds(m,5,true))}));
 const composition=[336.6,88.8,39.2,187.9];ok(Math.abs(composition.reduce((s,x)=>s+x,0)-652.5)<tol);const shares=composition.map(x=>x/652.5);
 const synthetic=[{G:[.90,0],P:[.80,.80]},{G:[.90,.90],P:[.80,0]}];
 for(const w of synthetic){for(const [m,p] of [w.G,w.P]){const [l,u]=bounds(m,5,true);ok(p>=l-tol&&p<=u+tol);}}
 const net=synthetic.map(w=>10*(w.G[1]-w.P[1])-1);ok(net[0]===-9);ok(net[1]===8);
 return {checks,cases,rows,composition_hours:composition,source_shares:shares,strict_score_countermodels:synthetic,synthetic_net_increment:net,field_calibration:false,full_repository_ci:false};
}
if(typeof module!=='undefined')module.exports=run;
if(typeof require!=='undefined'&&typeof module!=='undefined'&&require.main===module)console.log(JSON.stringify(run(),null,2));
