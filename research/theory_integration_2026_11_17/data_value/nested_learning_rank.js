function study(){
const T=[[1,0,.25],[0,1,.25]],D=[[1,0,-1],[0,1,-1]],z=[1,1,1],c=[2,.5,.5];
const dot=(a,b)=>a.reduce((v,x,i)=>v+x*b[i],0),add=(a,b,h=1)=>a.map((x,i)=>x+h*b[i]),det=A=>A[0][0]*A[1][1]-A[0][1]*A[1][0],norm=a=>Math.hypot(...a);
const forms={exponential:{f:s=>1-Math.exp(-s),df:s=>Math.exp(-s)},rational:{f:s=>s/(1+s),df:s=>1/(1+s)**2}};
let checks=0;function assert(ok){if(!ok)throw Error("check "+checks);checks++}
const close=(a,b,t=1e-9)=>assert(Math.abs(a-b)<=t);
const h=.001;
const fd=(f,z)=>D.map(d=>(f(add(z,d,h))-f(add(z,d,-h)))/(2*h));
const out={};
for(const [key,{f,df}] of Object.entries(forms)){
 const q=(r,z)=>f(dot(T[r],z)); const grad=T.map((row,r)=>D.map(d=>df(dot(row,z))*dot(row,d)));
 const est=T.map((_,r)=>fd(z=>q(r,z),z));
 grad.forEach((row,r)=>row.forEach((x,j)=>close(est[r][j],x,1e-6)));
 close(det(grad),.5*df(1.25)**2);
 assert(det(grad)>0);
 // Two identical economic panels cannot reveal two dimensions even under rank-two technical transfer.
 const collapsed=[fd(z=>q(0,z)+q(1,z),z),fd(z=>2*(q(0,z)+q(1,z)),z)];
 close(det(collapsed),0);
 // Unknown scalar index: two different differentiable panel functions of a common index.
 const a=[.9,.2,.4],k=z=>dot(a,z),u=z=>f(k(z)),v=z=>f(k(z))**2;
 const nullRows=[fd(u,z),fd(v,z)],trueRows=[D.map(d=>df(k(z))*dot(a,d)),D.map(d=>2*f(k(z))*df(k(z))*dot(a,d))];
 close(det(trueRows),0);
 // finite difference central approximation: known gradient error; bound based on observed row norms.
 const err=nullRows.map((row,r)=>norm(row.map((x,j)=>x-trueRows[r][j])));
 assert(Math.abs(det(nullRows))<=err[0]*norm(nullRows[1])+err[1]*norm(nullRows[0])+err[0]*err[1]+1e-12);
 // Controlled C preserves total exposure and changes the first target's effective source stock.
 close(z.reduce((a,b)=>a+b),c.reduce((a,b)=>a+b));const s0=dot(T[0],z),s1=dot(T[0],c),delta=.5;
 const dg0=f(s0+delta)-f(s0),dg1=f(s1+delta)-f(s1);
 assert(dg1<dg0);
 const threshold=dg0/dg1;
 close(threshold,key==="exponential"?Math.exp(s1-s0):((1+s1)*(1+s1+delta))/((1+s0)*(1+s0+delta)));
 // Two capacity regimes straddle the predicted interaction boundary, not an optimization claim.
 const below=.8*threshold,above=1.2*threshold;
 assert(below*dg1-dg0<0);assert(above*dg1-dg0>0);
 out[key]={technical_gradient:grad,determinant:det(grad),finite_difference:est,scalar_null_determinant:det(trueRows),collapsed_economic_determinant:det(collapsed),baseline_grounding_gain:dg0,coordination_grounding_gain:dg1,capacity_ratio_threshold:threshold,interaction_below:below*dg1-dg0,interaction_above:above*dg1-dg0};
}
return {checks,source_transfer:T,composition_directions:D,baseline:z,coordinated:c,forms:out,synthetic:true,field_calibration:false,full_repository_ci:false}
}
if(typeof module!=="undefined"&&require.main===module) console.log(JSON.stringify(study(),null,2));
