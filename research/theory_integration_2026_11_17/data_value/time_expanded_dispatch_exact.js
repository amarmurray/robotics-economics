"use strict";
const run = function(){
let checks=0;const ck=(x,m)=>{checks++;if(!x)throw Error(m)};
const N=64,s=32,a=20,b=14,dA=8,dB=8;
const A=[[1,1,20],[1,0,4],[0,1,4],[0,0,4]],B=[[1,1,1,14],[0,1,1,5],[1,0,1,5],[1,1,0,5],[0,0,0,3]];
ck(A.reduce((n,r)=>n+r[2],0)===s,"A mass");ck(B.reduce((n,r)=>n+r[3],0)===s,"B mass");
for(let j=0;j<2;j++)ck(A.reduce((n,r)=>n+r[j]*r[2],0)===24,"A margins");
for(let j=0;j<3;j++)ck(B.reduce((n,r)=>n+r[j]*r[3],0)===24,"B margins");
ck(A.reduce((n,r)=>n+r[0]*r[1]*r[2],0)===a,"A paid");
ck(B.reduce((n,r)=>n+r[0]*r[1]*r[2]*r[3],0)===b,"B paid");
ck(A.reduce((n,r)=>n+(1-r[0])*r[2],0)===dA,"A backlog");
ck(B.reduce((n,r)=>n+(1-r[0])*r[3],0)===dB,"B backlog");
let min=Infinity,max=-Infinity,auditMin=Infinity,n=0,na=0;
for(let qa=0;qa<=4;qa++)for(let kb=0;kb<=4;kb++)for(let pb=0;pb<=7;pb++){
n++;for(const [N,q] of [[dA,qa],[dB,kb],[b,pb]]){const t=[q,N/2-q,N/2-q,q];ck(t.every(x=>x>=0)&&t.reduce((x,y)=>x+y,0)===N,"lineage table");ck(t[0]+t[1]===N/2&&t[0]+t[2]===N/2,"same report and authorization margins")}
const qb=kb+pb,delta=qb-qa,e1=6*N+N/8,g1=6*(N-s)+5*s-N/8,e2=4*(N-s+a)+2*(s-dA-a)-dA,g2=4*(N-s)+8*b+2*(s-dB-b)-dB,e3=N+2*qa,g3=N+2*qb;
ck((N-s+a)+(s-dA-a)+dA===N,"E t2 capacity");ck((N-s)+b+(s-dB-b)+dB===N,"G t2 capacity");ck(qa<=dA&&qb<=b+dB,"predecessor conservation");
const D=g1+g2+g3-e1-e2-e3;ck(D===-N/4-s-2*a+6*b-3*(dB-dA)+2*delta,"reduced contrast");ck(D===-4+2*delta,"known t2");min=Math.min(min,D);max=Math.max(max,D);
if(delta>=8){na++;const lower=-16+7*delta-16;auditMin=Math.min(auditMin,lower);
for(const c of [7,9])for(const Dp of [23,25])for(const dg of [-1,1])for(const de of [-1,1]){const direct=-64+2*(Dp-c)*delta+dg*s-de*s;ck(direct>=4*lower,"drift bound")}}
}
ck(n===200&&min===-12&&max===18,"sharp nominal bounds");ck(auditMin===24,"sharp audit bound in 1/256 units");
return {synthetic:true,original_denominator:N,common_law_lineage_tables:n,audited_tables:na,scoped_assertions:checks,nominal_range:["-3/16","9/32"],audit_lower:"3/32",base_before_third_date:"-1/16",t2_paid_masses:{lost_A:"5/16",added_B:"7/32",backlog_A:"1/8",backlog_B:"1/8"},t3_overlap_ranges:{recovery_A:"[0,1/16]",recovery_B:"[0,1/16]",productive_B:"[0,7/64]"}};
};
console.log(JSON.stringify(run(),null,2));
