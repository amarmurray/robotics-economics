function run(){
 let checks=0;const ok=x=>{if(!x)throw Error("check "+checks);checks++};
 // integer count identity: q=r/d, penetration=r/n; no decimal inference.
 for(let n=1;n<=20;n++)for(let d=1;d<=n;d++)for(let r=0;r<=d;r++){ok(Math.abs((d/n)*(r/d)-r/n)<1e-12)}
 // fixed selected composition, moving extensive margin, opposite production effects
 const p={n:100000,d:3000,r:1710},gLow={n:100000,d:1000,r:600},gHigh={n:100000,d:4000,r:2400};
 ok(p.r/p.d<gLow.r/gLow.d);ok(gLow.r/gLow.d===gHigh.r/gHigh.d);ok(gLow.r<p.r&&gHigh.r>p.r);
 const N=7453438,D=241517,lo=Math.ceil(D*565/1000),hi=Math.ceil(D*575/1000)-1;
 ok(lo/D>=.565&&hi/D<.575);ok((lo-1)/D<.565&&(hi+1)/D>=.575);
 // bounds on gross receipts difference with known prices, unknown extensive rate in [0,1]
 for(let a=0;a<=10;a++)for(let b=0;b<=10;b++){const x=28*b/10*.5567-22*a/10*.57;ok(x>=-22*.57-1e-10&&x<=28*.5567+1e-10)}
 return {checks,observed:{N,D,delivered_share:D/N,reported_rounded_robot_share:.57,conditional_rounding_robot_count:[lo,hi],conditional_rounding_population_penetration:[lo/N,hi/N]},synthetic:{P:p,G_low:gLow,G_high:gHigh,conditional_robot_share:[.57,.6,.6],robot_population_share:[p.r/p.n,gLow.r/gLow.n,gHigh.r/gHigh.n]},field_causal_data_value:false,full_repository_ci:false};
}
console.log(JSON.stringify(run(),null,2));
