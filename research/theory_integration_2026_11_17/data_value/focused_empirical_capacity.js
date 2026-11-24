function run(){
 let checks=0,cases=0; const eq=(a,b)=>{checks++;if(a!==b)throw Error(`${a} != ${b}`)};
 function enumerate(cap,i=0,p=[]){if(i===cap.length)return [p];let o=[];for(let x=0;x<=cap[i];x++)o.push(...enumerate(cap,i+1,[...p,x]));return o}
 const sum=x=>x.reduce((a,b)=>a+b,0);
 function bounds(h,d,S){
 const l=h.map((v,i)=>v+d[i]),B=Math.max(...l),slack=l.map(v=>B-v),total=sum(d);
 const lower=Math.min(...d.map((v,i)=>slack[i]+Math.max(0,S-(total-v))));
 let upper=0;for(let k=0;k<=B;k++)if(d.every((v,i)=>k<=slack[i]+v)&&sum(slack.map(v=>Math.max(0,k-v)))<=S)upper=k;
 return [lower,upper]
 }
 for(let n=1;n<=3;n++)for(const h of enumerate(Array(n).fill(2)))for(const d of enumerate(Array(n).fill(3))){
 const B=Math.max(...h.map((v,i)=>v+d[i]));let groups={};
 for(const s of enumerate(d)){let S=sum(s),k=B-Math.max(...h.map((v,i)=>v+d[i]-s[i]));(groups[S]??=[]).push(k)}
 for(const [S,vals] of Object.entries(groups)){cases++;let [a,b]=bounds(h,d,+S);eq(a,Math.min(...vals));eq(b,Math.max(...vals));for(let K=0;K<=B+1;K++)for(const k of [a,b]){
 let saving=Math.max(0,B-K)-Math.max(0,B-k-K);eq(saving,Math.min(k,Math.max(0,B-K)));eq(saving>=0&&saving<=k,true);
 }}
 }
 const ex=bounds([2,0],[8,8],4);eq(ex[0],0);eq(ex[1],3);
 // Source percentages are reported rounded, conditional algebra only
 const observed={distanceReduction:0.62,driveRequirementReduction:0.31,reportedDriveSavingsUSD:500000000,period:"2017–2020",conditionalDistanceShare:31/62,actualShareIdentified:false};
 eq(observed.conditionalDistanceShare,0.5);
 return {checks,cases,synthetic:{h:[2,0],d:[8,8],totalReduction:4,peakReductionBounds:ex,preOwned:8,avoidedPurchaseBounds:[0,2]},observed,fieldCausalDataValue:false,fullRepositoryCI:false}
}
if (typeof module !== 'undefined' && require.main === module) console.log(JSON.stringify(run(),null,2));
