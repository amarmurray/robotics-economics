const results = (function run(){
 let checks=0,cases=0;const near=(x,y)=>{checks++;if(Math.abs(x-y)>1e-9)throw Error(`${x} != ${y}`)},assert=x=>{checks++;if(!x)throw Error("assertion")};
 // Three binary reports: source, relation, and direct target.
 function bayes(a,b,d){let probs={};for(let x of [-1,1])for(let m of [-1,1])for(let e of [-1,1])for(let f of [-1,1])for(let g of [-1,1]){let theta=x*m,k=[x*e,m*f,theta*g].join(","),p=(1+a*e)*(1+b*f)*(1+d*g)/32;probs[k]??=[0,0];probs[k][theta===1?1:0]+=p;}return Object.values(probs).reduce((s,v)=>s+Math.max(...v),0)}
 for(let i=0;i<=10;i++)for(let j=0;j<=10;j++)for(let k=0;k<=10;k++){let a=i/10,b=j/10,d=k/10;near(bayes(a,b,d),(1+Math.max(a*b,d))/2);cases++}
 function game(p,q,j,cA=1.5,cB=2,D=10,s=6){let eq=[];const out=(x,y)=>{let A=p*x-j*x*y/2,B=q*y-j*x*y/2;return {x,y,A,B,awards:A+B,uA:x*(D*(p-j*y)-cA),uB:y*(D*(q-j*x)-cB),real:D*(A+B)-cA*x-cB*y+s*B}};for(let x of [0,1])for(let y of [0,1]){let ga=D*(p-j*y)-cA,gb=D*(q-j*x)-cB;if((x?ga>=-1e-9:ga<=1e-9)&&(y?gb>=-1e-9:gb<=1e-9))eq.push(out(x,y))}if(j>0){let x=(q-cB/D)/j,y=(p-cA/D)/j;if(x>1e-9&&x<1-1e-9&&y>1e-9&&y<1-1e-9)eq.push(out(x,y));}for(let r of eq){if(r.x>0&&r.x<1)near(r.uA,0);if(r.y>0&&r.y<1)near(r.uB,0);near(r.A+r.B,r.awards)}return eq}
 let ordinary=game(.5,.5,.25),exclusive=game(.7,.5,.35),broadcastCommon=game(.7,.7,.7),broadcastIndependent=game(.7,.7,.49);
 assert(ordinary.length===1&&exclusive.length===1&&broadcastCommon.length===3&&broadcastIndependent.length===1);near(ordinary[0].uA,1);near(exclusive[0].uA,5.5);near(exclusive[0].real-ordinary[0].real,-.75);near(broadcastIndependent[0].real-ordinary[0].real,2.08);
 // Source acquisition increment under higher mapping quality and optional direct evidence.
 for(let i=0;i<=10;i++)for(let k=i;k<=10;k++)for(let j=0;j<=10;j++)for(let l=j;l<=10;l++)for(let m=0;m<=10;m++){let a=i/10,A=k/10,b=j/10,B=l/10,d=m/10;let delta=t=>Math.max(A*t,d)-Math.max(a*t,d);assert(delta(B)>=delta(b)-1e-9);cases++}
 const a0=.4,a1=.8,b0=.3,b1=.8,d=.2,w=10,c=.8,inc=(b,d)=>w/2*(Math.max(a1*b,d)-Math.max(a0*b,d));near(inc(b0,d),.2);near(inc(b1,d),1.6);near(inc(b1,.7),0);assert(inc(b0,d)<c&&inc(b1,d)>c);
 let priceCases=[];for(let outside of [.5,2,8]){let cap=Math.min(4.5,outside),p=Math.min(cap,1.2),chosen=p>=.8?"external":"outside";priceCases.push({outside,cap,price:chosen==="external"?p:null,chosen,externalMargin:chosen==="external"?p-.8:0});}
 return {checks,cases,ordinary,exclusive,broadcastCommon,broadcastIndependent,priceCases,source:{old:inc(b0,d),mapped:inc(b1,d),directSubstitute:inc(b1,.7),cost:c},scope:"Synthetic finite posterior/entry enumeration; no empirical calibration or full CI"}
})();
console.log(JSON.stringify(results,null,2));
