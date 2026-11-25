/* Exact finite audit; run with node. */
function run(){
  let checks=0,cases=0;
  function check(x){checks++;if(!x)throw Error("failed at "+checks)}
  function bounds(f0,f1,p,g,c,a,b,r,s,h){
    let t=Math.max(0,p-a,p+g-f0),m=Math.max(0,t-b);
    return [Math.max(0,g-r,c-s),f1-f0+Math.min(f0,g+c-m+h)];
  }
  const pop=x=>{let n=0;while(x){n+=x&1;x>>=1}return n};
  // Independently enumerate all event sets on each canonical finite universe;
  // exact violation vectors, then compare all nonnegative upper-budget vectors.
  for(let n=0;n<=4;n++)for(let f0=0;f0<=n;f0++){
    const F=(1<<f0)-1,M=(1<<n)-1,groups=new Map();
    for(let P=0;P<=F;P++)for(let G=0;G<=F;G++)for(let C=0;C<=M;C++)for(let Z=0;Z<=M;Z++){
      let p=pop(P),g=pop(G),c=pop(C),z=pop(Z);
      let key=[p,g,c].join(","),rec=[pop(P&~G),pop(P&~C),pop(G&~Z),pop(C&~Z),pop(Z&F&~(G|C)),z];
      if(!groups.has(key))groups.set(key,[]);
      groups.get(key).push(rec);
    }
    for(const [key,rows] of groups){
      const [p,g,c]=key.split(",").map(Number);
      for(let a=0;a<=p;a++)for(let b=0;b<=p;b++)for(let r=0;r<=g;r++)for(let s=0;s<=c;s++)for(let h=0;h<=f0;h++){
        if(g<p-a||c<p-b)continue;
        let seen=0;
        for(const [aa,bb,rr,ss,hh,z] of rows)if(aa<=a&&bb<=b&&rr<=r&&ss<=s&&hh<=h)seen|=1<<z;
        const [lo,hi]=bounds(f0,n,p,g,c,a,b,r,s,h);let expected=0;
        for(let z=lo;z<=hi;z++)expected|=1<<z;
        check(seen===expected);cases++;
      }
    }
  }
  const args=[10,12,6,7,6];
  const examples=[bounds(...args,0,0,0,0,0),bounds(...args,1,0,0,0,0),bounds(...args,1,0,1,0,1),bounds(...args,6,6,7,6,10)];
  check(JSON.stringify(examples)===JSON.stringify([[7,9],[7,10],[6,11],[0,12]]));
  return {checks,cases,examples,scope:"all finite set laws through four equal-mass histories, all integer upper-budget vectors, exact attained sets; synthetic not field evidence"};
}
console.log(JSON.stringify(run(),null,2));
