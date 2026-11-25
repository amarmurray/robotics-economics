function verify(){
const N=4,n=3,weights=[[9,5,1],[7,7,2],[4,2,0]];let checks=0,cases=0;
function assert(ok){if(!ok)throw Error("assertion "+checks);checks++}
function bounds(m,w,k){let lo=0,hi=0,prefix=0,a=[];for(let j=0;j<n;j++){a.push(m[j]);a.sort((x,y)=>y-x);prefix+=m[j];let dw=w[j]-(w[j+1]||0);lo+=dw*a.slice(0,k).reduce((x,y)=>x+y,0);hi+=dw*Math.min(k*N,prefix)}return[lo,hi]}
function value(bits,w,k){let sum=0;for(let t=0;t<N;t++){let q=0;for(let i=0;i<n;i++){if((bits[i]>>t)&1&&q<k){sum+=w[i];q++}}}return sum}
for(const w of weights)for(let k=0;k<=n;k++){let groups=new Map();for(let a=0;a<16;a++)for(let b=0;b<16;b++)for(let c=0;c<16;c++){let bits=[a,b,c],m=bits.map(x=>x.toString(2).replace(/0/g,"").length),key=m.join(","),v=value(bits,w,k),[lo,hi]=bounds(m,w,k);assert(v>=lo&&v<=hi);let z=groups.get(key)||[Infinity,-Infinity];groups.set(key,[Math.min(z[0],v),Math.max(z[1],v)]);cases++}for(const [key,z] of groups){let [lo,hi]=bounds(key.split(",").map(Number),w,k);assert(z[0]===lo&&z[1]===hi)}}
const baseline=value([3,0,0],[10,10,0],1)/N,coincident=value([3,3,0],[10,10,0],1)/N,disjoint=value([3,12,0],[10,10,0],1)/N;assert(baseline===5&&coincident===5&&disjoint===10);
return {checks,cases,worlds:{baseline,groundingCoincident:coincident,groundingDisjoint:disjoint,incrementalCost:2,net:[coincident-baseline-2,disjoint-baseline-2]},field_calibration:false,full_repository_ci:false}
}
console.log(JSON.stringify(verify(),null,2));
