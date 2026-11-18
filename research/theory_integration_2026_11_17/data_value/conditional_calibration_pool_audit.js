/* Synthetic conditional diagnostic and controller-pool audit. Node: node conditional_calibration_pool_audit.js */
function runAudit(){
const eps=1e-10;let checks=0;function assert(v,msg){checks++;if(!v)throw Error(msg)};const close=(a,b)=>Math.abs(a-b)<eps;
const worlds=[
{label:"low coupling",t:.29,mass:[.29,.21,.21,.29],zplus:[.29,.16,.05,0]},
{label:"high coupling",t:.39,mass:[.39,.11,.11,.39],zplus:[.34,.11,0,.05]}
];
for(const w of worlds){const a=w.mass,z=w.zplus;assert(close(a.reduce((x,y)=>x+y,0),1),"mass");assert(close(a[0]+a[1],.5),"H");assert(close(a[0]+a[2],.5),"D");for(let i=0;i<4;i++)assert(z[i]>=0&&z[i]<=a[i]+eps,"valid Z");assert(close(z[0]+z[1],.45),"pooled H TPR");assert(close(z[2]+z[3],.05),"pooled H FPR");assert(close(z[0]+z[2],.34),"pooled D/Z");assert(close(z.reduce((x,y)=>x+y,0),.5),"Z total");assert(close((5+8*w.t)-(8-2*w.t),10*w.t-3),"pair");}
const value=(x,t,k)=>8-3*x+(10*x-2)*t-k*x*(1-x);
let maxByK={};for(const k of [0,2.5,3,-3]){let best={x:0,value:-Infinity};for(let i=0;i<=1000;i++){const x=i/1000;const lower=Math.min(value(x,0,k),value(x,.5,k));if(lower>best.value+eps)best={x,value:lower};}maxByK[String(k)]=best;}
assert(close(maxByK["0"].x,.2)&&close(maxByK["0"].value,7.4),"independent optimum");
assert(close(maxByK["2.5"].value,7),"interference boundary");
assert(close(maxByK["3"].x,0)&&close(maxByK["3"].value,7),"mandatory pooled maximin");
assert(close(maxByK["-3"].x,.2)&&close(maxByK["-3"].value,7.88),"positive pool complement");
const isolatedNet=7.4-.5;assert(isolatedNet<7,"costly isolation");let oracleWorst=Infinity;for(let i=0;i<=1000;i++){const t=i/2000;const best=Math.max(5+8*t,8-2*t,6,5);oracleWorst=Math.min(oracleWorst,best)}assert(close(oracleWorst,7.4),"oracle");const pooledOraclePremium=oracleWorst-7;assert(close(pooledOraclePremium,.4),"premium");
const pooled={worstFreeMix:maxByK["0"].value,negativeInterferenceMaximin:maxByK["3"].value,positiveComplementMaximin:maxByK["-3"].value,isolationCost:.5,oracleWorst,oracleGrossValueWithPool:pooledOraclePremium};
const pair={m:.34,pooledSensitivity:.9,pooledFalsePositive:.1,identifiedT:[.29,.39],pairedDifference:[-.1,.9],invariantConditionalImpliedT:(.34-.05)/.8};
return {checks,worlds,pair,pooled,gridStep:1/1000,unit:"synthetic normalized per eligible pool"};
}
const results=runAudit();
if(typeof module!=='undefined'&&module.exports){module.exports={runAudit,results};if(require.main===module)console.log(JSON.stringify(results,null,2));}
