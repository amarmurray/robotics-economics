function run(){
 let checks=0,laws=0,intervals=0;const n=16,rows=[],ok=x=>{if(!x)throw Error("check "+checks);checks++};
 for(let a=0;a<=n;a++)for(let b=0;b<=n-a;b++)for(let c=0;c<=n-a-b;c++){
 const d=n-a-b-c; laws++;const atoms=[...Array(a).fill([0,0]),...Array(b).fill([0,1]),...Array(c).fill([1,0]),...Array(d).fill([1,1])];
 const p=atoms.reduce((s,[L,H])=>s+8*L*H,0),g=atoms.reduce((s,[L,H])=>s+8*H,0)-n,x=p+n,e=p+2*n;
 ok(p===8*d);ok(g===8*(b+d)-n);ok(g-p===8*b-n);ok(g-e===8*b-3*n);ok((g<=p)===(8*b<=n));ok((g>e)===(8*b>3*n));ok(x<=e);ok(g-p===8*b-n);
 const h=b+d,l=c+d,lo=Math.max(0,h+l-n),hi=Math.min(h,l);ok(d>=lo&&d<=hi);ok(g-8*hi-2*n<=g-e&&g-e<=g-8*lo-2*n);
 if(h===n/2&&l===n/2)rows.push({overlap:d/n,P:p/n,G:g/n,X:x/n,E:e/n,G_minus_E:(g-e)/n});
 }
 for(let h=0;h<=n;h++)for(let l=0;l<=n;l++){const v=[];for(let j=0;j<=n;j++)if(h-j>=0&&l-j>=0&&n-h-l+j>=0)v.push(8*(h-j)-3*n);ok(Math.min(...v)===8*(h-Math.min(h,l))-3*n);ok(Math.max(...v)===8*(h-Math.max(0,h+l-n))-3*n);intervals++}
 for(let k=0;k<=n;k++)ok(Math.min(4*k,4*(n-k))<=2*n);
 return {checks,laws,intervals,denominator:n,rows:rows.sort((a,b)=>a.overlap-b.overlap),synthetic:true,field_calibration:false,full_repository_ci:false};
}
console.log(JSON.stringify(run(),null,2));
