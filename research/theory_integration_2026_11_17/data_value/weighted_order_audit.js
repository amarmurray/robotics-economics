const run = function(){
 let checks=0,cases=0;const ok=x=>{if(!x)throw Error("check "+checks);checks++};
 const sum=x=>x.reduce((a,b)=>a+b,0);
 const comb=(n,k)=>{let a=[];function rec(start,left,l){if(!left){a.push(l);return}for(let i=start;i<=n-left;i++)rec(i+1,left-1,[...l,i])}rec(0,k,[]);return a};
 const range=(w,j)=>{const a=[...w].sort((x,y)=>x-y);return [sum(a.slice(0,j)),sum(a.slice(a.length-j))]};
 const width=(w,k,m)=>{const r=w.length,l=Math.max(0,k-m),u=Math.min(k,r),j=Math.max(l,Math.min(u,Math.floor(r/2)));const [a,b]=range(w,j);return b-a};
 for(let n=1;n<=7;n++)for(const w of [Array.from({length:n},(_,i)=>i*i),Array.from({length:n},(_,i)=>i<3?i-3:2*i+1),Array.from({length:n},(_,i)=>Math.floor(i/2)),Array.from({length:n},(_,i)=>i===n-1?50:i)]){
 for(let k=0;k<=n;k++)for(let m=0;m<=n;m++){let r=n-m,all=Infinity,contig=Infinity;
 for(const ids of comb(n,r)){const a=ids.map(i=>w[i]);let brute=0;
 for(let j=Math.max(0,k-m);j<=Math.min(k,r);j++){let vals=comb(r,j).map(s=>sum(s.map(i=>a[i])));const b=range(a,j);ok(b[0]===Math.min(...vals)&&b[1]===Math.max(...vals));brute=Math.max(brute,Math.max(...vals)-Math.min(...vals))}
 const q=width(a,k,m);ok(q===brute);all=Math.min(all,q)}
 for(let i=0;i<=n-r;i++)contig=Math.min(contig,width(w.slice(i,i+r),k,m));ok(all===contig);cases++}
 }
 const w=[1,2,3,10,20,21],k=3,m=2;let examples=comb(6,4).map(ids=>({remaining:ids.map(i=>w[i]),width:width(ids.map(i=>w[i]),k,m)})).sort((a,b)=>a.width-b.width);
 ok(examples[0].width===10);ok(range(w,k)[0]===6&&range(w,k)[1]===51);
 return {checks,cases,example:{weights:w,k,m,initial:range(w,k),best:examples[0],worst:examples.at(-1)},field_calibration:false,full_repository_ci:false};
};
console.log(JSON.stringify(run(),null,2));
