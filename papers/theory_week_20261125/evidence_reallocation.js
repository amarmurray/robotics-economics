// Synthetic two-market allocation; no empirical parameters. Run: node evidence_reallocation.js
const assert=(x,msg)=>{if(!x)throw Error(msg)};
const close=(a,b,tol=1e-6)=>Math.abs(a-b)<tol;
const clamp=(x,a,b)=>Math.max(a,Math.min(b,x));
function allocation(B,I,g,e,u,w){
  const cap=Math.min(B,I), m0=g*cap;
  const candidates=[];
  function add(lo,hi,rate,E){
    const m=clamp((rate*w*(1+E)-u)/(u+w),lo,hi);
    const i=Math.min(I,m/g), a=(m-g*i)/e, y=B-i-a;
    candidates.push({m,i,a,y,value:u*Math.log1p(Math.max(0,y))+w*Math.log1p(m)});
  }
  add(0,m0,g,B);
  if(B>I) add(m0,m0+e*(B-I),e,B+(g/e-1)*I);
  return candidates.reduce((a,b)=>a.value>b.value?a:b);
}
function source(p,x,P){
  const B=P.H-(P.h0+P.h1*(1-p))*x,I=P.r*(1-p)*x;
  const q=allocation(Math.max(0,B),I,P.g,P.e,P.u,P.w);
  return {...q,x,B,I,accepted:p*x,total:q.value+(p*P.v-P.c)*x-P.d*x*x/2};
}
function optimize(p,P){
  let l=0,h=Math.min(P.K,P.D/p,P.H/(P.h0+P.h1*(1-p)));
  for(let t=0;t<100;t++){const a=(2*l+h)/3,b=(l+2*h)/3;if(source(p,a,P).total<source(p,b,P).total)l=a;else h=b}
  return source(p,(l+h)/2,P);
}
function run(){
  let checks=0;const check=(x,s)=>{assert(x,s);checks++};
  // Independently enumerate feasible incident and reference hours on a grid.
  for(const B of [0,1,3,8])for(const I of [0,.4,1,5,10])for(const g of [1.5,3])for(const e of [.5,1])for(const u of [.4,1,4])for(const w of [.5,1,3]){
    if(g<=e)continue;
    const z=allocation(B,I,g,e,u,w);let best=-Infinity;
    for(let j=0;j<=40;j++){const i=Math.min(I,B)*j/40;for(let k=0;k<=40;k++){const a=(B-i)*k/40,y=B-i-a,m=g*i+e*a;best=Math.max(best,u*Math.log1p(y)+w*Math.log1p(m))}}
    check(z.value+1e-10>=best,"grid optimum");
    check(z.i>=-1e-9&&z.i<=I+1e-9&&z.a>=-1e-9&&z.y>=-1e-9&&close(z.y+z.i+z.a,B),"feasible");
    check(close(z.m,g*z.i+e*z.a),"evidence account");
  }
  const base={h0:.5,r:.5,g:3,e:1,u:1,w:1,K:30,D:100,v:1,c:0,d:.1};
  let examples=[];
  for(const h1 of [.5,1.5]){
    const P={...base,h1,H:8+10*(base.h0+h1*.2)};
    const a=source(.8,10,P),b=source(.81,10,P);
    check(a.a>0&&a.y>0&&b.a>0&&b.y>0,"mixed regime");
    check(close((b.m-a.m)/.01,.5*(h1-1)*10),"fixed exposure derivative");
    examples.push({h1,baseline:a,next:b,mpkr:[2+.2*a.m,2+.2*b.m]});
  }
  let endogenous=null;
  // Verify comparative statics in interior mixed regimes, and find a counterexample
  // to the fixed-exposure sign under increasing paid marginal demand.
  for(const h1 of [.5,1.5,3])for(const v of [.8,1.5,3,5])for(const d of [.08,.2,.4])for(const H of [8,16,28]){
    const P={...base,h1,v,d,H};const p=.8,eps=1e-4,z=optimize(p,P),lo=optimize(p-eps,P),hi=optimize(p+eps,P);
    const maxX=Math.min(P.K,P.D/p,P.H/(P.h0+P.h1*(1-p)));
    if(z.x<.01||z.x>maxX-.01||Math.min(z.a,z.y,lo.a,lo.y,hi.a,hi.y)<.01)continue;
    const alpha=P.g/P.e-1,k=P.h0+(P.h1-alpha*P.r)*(1-p),kp=-(P.h1-alpha*P.r);
    const E=z.B+alpha*z.I,m=z.m,y=z.y,UE=-P.u/(1+y)**2,WE=-P.w/(1+m)**2;
    const mE=P.e*UE/(UE+P.e**2*WE),VE=P.u/(1+y),VEE=UE*(1-mE/P.e);
    const xp=(P.v-kp*VE+k*kp*z.x*VEE)/(P.d-k*k*VEE);
    const Ep=-kp*z.x-k*xp;
    check(close((hi.x-lo.x)/(2*eps),xp,.003),"endogenous attempt response");
    check(close((hi.m-lo.m)/(2*eps),mE*Ep,.003),"endogenous evidence response");
    if(!endogenous&&-kp*z.x>0&&Ep<-.01)endogenous={P,z,xp,Ep,fixedExposureSlope:mE*(-kp*z.x),optimizedSlope:mE*Ep,observedSlope:(hi.m-lo.m)/(2*eps)};
  }
  check(endogenous!==null,"reversal witness");
  return {checks,examples,endogenous,field_calibrated:false};
}
console.log(JSON.stringify(run(),null,2));
