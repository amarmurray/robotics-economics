function audit(){
 let cases=0,checks=0;
 function check(x){if(!x)throw Error("failed assertion "+checks);checks++;}
 function bounds(N,M,B,H){return [Math.max(0,N-B),Math.min(M,N-Math.ceil(B/H))]}
 for(let N=1;N<=4;N++)for(let H=1;H<=4;H++){
  const seen=new Map();
  function enumerate(i,M,B,A){
   if(i===N){const key=M+","+B;const v=seen.get(key)||[Infinity,-Infinity];seen.set(key,[Math.min(v[0],A),Math.max(v[1],A)]);cases++;return}
   for(let m=0;m<=H;m++)for(let b=0;b<=H-m;b++)if(m+b>0)enumerate(i+1,M+m,B+b,A+(b===0?1:0))
  }
  enumerate(0,0,0,0);
  for(const [key,v] of seen){let [M,B]=key.split(",").map(Number);let [l,u]=bounds(N,M,B,H);check(v[0]===l);check(v[1]===u)}
 }
 const published=[{period:2,N:51482,T:106611,M:81073,otherRoutes:[4380,9252,11907]},{period:3,N:54822,T:114111,M:87742,otherRoutes:[4091,9975,12303]}].map(z=>{let B=z.T-z.M;let [l,u]=bounds(z.N,z.M,B,z.T);return {...z,B,tableRouteSum:z.M+z.otherRoutes.reduce((a,b)=>a+b,0),allDS:[l,u],allDSShare:[l/z.N,u/z.N],affectedNonDS:[z.N-u,z.N-l],hypotheticalCap4:bounds(z.N,z.M,B,4)}});
 check(published[0].tableRouteSum===106612);check(published[1].tableRouteSum===114111);check(published[1].allDS[0]===28453);check(published[1].allDS[1]===54821);
 return {cases,checks,published,field_calibration:false,full_repository_ci:false};
}
console.log(JSON.stringify(audit(),null,2));
