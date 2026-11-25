function run(){
let checks=0,pairs=0;const ok=x=>{if(!x)throw Error("assert "+checks);checks++};
function bounds(q){let [f0,f1,p,g,c,a,b,r,s,h]=q;let m=Math.max(0,p-a-b,p+g-f0-b);return [Math.max(0,g-r,c-s),f1-f0+Math.min(f0,g+c-m+h)]}
const all=[];for(let f0=0;f0<=2;f0++)for(let f1=f0;f1<=2;f1++)for(let p=0;p<=f0;p++)for(let g=0;g<=f0;g++)for(let c=0;c<=f1;c++)for(let a=0;a<=p;a++)for(let b=0;b<=p;b++)if(g>=p-a&&c>=p-b)for(let r=0;r<=g;r++)for(let s=0;s<=c;s++)for(let h=0;h<=f0;h++)all.push([f0,f1,p,g,c,a,b,r,s,h]);
for(const x of all)for(const y of all){const a=bounds(x),b=bounds(y),q=bounds(x.map((v,i)=>v+y[i]));ok(q[0]<=a[0]+b[0]&&q[1]>=a[1]+b[1]);pairs++}
const disjoint=[[5,5,0,5,0,0,0,0,0,0],[5,5,0,0,5,0,0,0,0,0]];
const same=[[5,5,0,5,5,0,0,0,0,0],[5,5,0,0,0,0,0,0,0,0]];
const summarize=x=>({pooled:bounds(x[0].map((v,i)=>v+x[1][i])),stratified:x.map(bounds).reduce((a,b)=>[a[0]+b[0],a[1]+b[1]],[0,0])});
const A=summarize(disjoint),B=summarize(same);ok(A.stratified.join()==="10,10");ok(B.stratified.join()==="5,5");ok(A.pooled.join()==="5,10"&&B.pooled.join()==="5,10");
return {checks,pairs,tuples:all.length,disjoint:A,coincident:B,field_calibration:false,full_repository_ci:false};
}
console.log(JSON.stringify(run(),null,2));
