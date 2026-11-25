// Run: node sequential_compatibility.js
// All inputs are synthetic; see companion proof.
function study(){
 const eps=1e-9;let checks=0;function check(x,msg){if(!x)throw Error(msg);checks++}
 const states=[{t:0,e:0},{t:0,e:1},{t:1,e:0},{t:1,e:1}];
 function solve({a=.9,b=.5,q=1,r=.9,H=4,B=20,w=2,base=.2,A=[.8,.8],D=[.1,.1],E=[.3,.3],F=6,beta=1,allowed=["none","target","source","embodiment"]}={}){
  const prior=states.map(s=>(s.t?a:1-a)*(s.e?b:1-b));
  const evidence=(s,n,j)=>1-(1-base)*Math.pow(1-A[s.e],n)*(j==="B"?1-D[s.e]:j==="E"?1-E[s.e]:1);
  const final=(mass,h,j,fee=0)=>{let z=mass.reduce((x,y)=>x+y,0);if(z<eps)return {v:0,cur:0,ev:0,n:0,B:0,E:0};const n=Math.min(2,Math.floor(h/2));const cur=4*n+(j==="B"||j==="E"?B:0)-fee;const ev=mass.reduce((sum,p,i)=>sum+p*evidence(states[i],n,j),0)/z;return {v:cur+beta*w*ev,cur,ev,n,B:+(j==="B"),E:+(j==="E")}};
  const combine=arr=>{let out={v:0,cur:0,ev:0,n:0,B:0,E:0};for(const [p,x] of arr)for(const k in out)out[k]+=p*x[k];return out};
  const best=arr=>arr.reduce((x,y)=>y.v>x.v+eps?y:x);
  const after=(mass,h)=>{let z=mass.reduce((x,y)=>x+y,0);if(z<eps)return final(mass,h,"none");let opts=[final(mass,h,"none")];if(h>=2)for(const parity of [0,1]){
   const yes=mass.map((m,i)=>((states[i].t^states[i].e)===parity?m:0));const no=mass.map((m,i)=>m-yes[i]);const p=yes.reduce((a,b)=>a+b,0)/z;
   opts.push(combine([[p,best([final(yes,h-1,"none"),final(yes,h-2,"B")])],[1-p,final(no,h-1,"none")]]))}
   return best(opts)};
  const routes={none:after(prior,H)};
  if(H>=1)for(const [key,field,acc] of [["target","e",q],["source","t",r]]){const reports=[0,1].map(report=>{const mass=prior.map((p,i)=>p*(states[i][field]===report?acc:1-acc));const prob=mass.reduce((x,y)=>x+y,0);return [prob,after(mass,H-1)]});routes[key]=combine(reports)}
  if(H>=3)routes.embodiment=final(prior,H-3,"E",F);
  const candidates=allowed.filter(x=>routes[x]);let chosen=candidates.reduce((x,y)=>routes[y].v>routes[x].v+eps?y:x);return {chosen,routes,optimal:routes[chosen]};
 }
 const witness=solve(),old=solve({allowed:["none","source","embodiment"]});
 check(witness.chosen==="target","target selected");check(old.chosen==="none","baseline selected");check(witness.optimal.cur>old.optimal.cur,"current value");check(witness.optimal.B>old.optimal.B&&witness.optimal.n<old.optimal.n,"signed adoption");check(witness.optimal.ev<old.optimal.ev,"less next evidence");
 const flipped=solve({A:[.1,.1],D:[.8,.8]}),flippedOld=solve({A:[.1,.1],D:[.8,.8],allowed:["none","source","embodiment"]});check(flipped.optimal.ev>flippedOld.optimal.ev,"opposite propagation");
 const high=solve({w:25});check(high.chosen!=="target","continuation changes choice");
 let cases=0;
 for(const a of [.5,.7,.9,1])for(const b of [.5,.7,1])for(const q of [.5,.75,1])for(const H of [2,3,4,5])for(const B of [5,12,20])for(const w of [0,2,20]){
  const args={a,b,q,H,B,w};const x=solve(args),y=solve({...args,allowed:["none","source","embodiment"]});check(x.optimal.v>=y.optimal.v-eps,"option monotonicity");for(const s of Object.values(x.routes))check(s.ev>=-eps&&s.ev<=1+eps,"valid next probability");if(b===.5&&H===4&&w===0){check(x.routes.source.v<=x.routes.none.v+eps,"source alone cannot improve parity; occupied slot");let p=.5+.5*(2*a-1)*(2*q-1);let target=Math.max(4,p*B+(1-p)*4);check(Math.abs(x.routes.target.v-target)<eps,"target closed form")}cases++;
 }
 // Analytic successor difference under the specified fixed service branches.
 let formulaCases=0;
 for(const a of [.6,.8,.9,1])for(const q of [.5,.75,1])for(const ua of [0,.1,.5,.8,1])for(const ub of [0,.1,.5,.8,1]){
  const x=solve({a,q,A:[ua,ua],D:[ub,ub],w:0});const p=.5+.5*(2*a-1)*(2*q-1);
  const pred=.8*(p*(ub-ua)-.5*ub*(1-ua));
  check(Math.abs(x.routes.target.ev-x.routes.none.ev-pred)<eps,"successor formula");formulaCases++;
 }
 const threshold=4.4/.512;
 check(solve({w:threshold-.01}).chosen==="target","below dynamic cutoff");
 check(solve({w:threshold+.01}).chosen==="none","above dynamic cutoff");
 const selection=[{label:"success high evidence",p:.5,uSuccess:.9,uFail:.1,next:.45},{label:"success low evidence",p:.5,uSuccess:.1,uFail:.9,next:.05}];check(selection[0].p===selection[1].p&&selection[0].next>selection[1].next,"selection counterexample");
 return {cases,formulaCases,checks,witness,old,flipped,flippedOld,high,threshold,selection,scope:"Synthetic finite Bayesian decisions and analytic formula checks; no field calibration or full CI."}
}
console.log(JSON.stringify(study(),null,2));
