/** Calendar receipt / qualification prototype. Synthetic normalized inputs.
 * One active Poisson qualification program; qualified service continues while
 * training on a separate resource. Constant collected cash rates, no borrowing
 * limits in HJB. All programs and returns for ONE disclosed recipient.
 * RK4 is numerical, not a proof. See CALENDAR_FINANCE_CONTINUATION.md. */
export function iexp(k,t){if(!(k>0&&t>=0))throw Error("domain");return -Math.expm1(-k*t)/k;}

export function itexp(k,t){if(!(k>0&&t>=0))throw Error("domain");const x=k*t;if(x<1e-3)return t*t*(.5-x/3+x*x/8-x*x*x/30+x**4/144);return (-Math.expm1(-x)-x*Math.exp(-x))/(k*k);}

export function fixedPaths(T,{a=2,mu=1.2,v=4.5,W=10,c=1}={}){const I=iexp(a,T),J=itexp(a,T),K=iexp(mu,T);const staged=v*a*J+W*(T-I-a*J)-c*(I+a*J);const joint=W*(T-K)-c*K;return{staged,joint,gap:staged-joint};}

export function slopeAndLimit({a=2,mu=1.2,v=4.5,W=10,c=1}={}){return{shortQuadratic:(a*v-mu*(W+c))/2,longDifference:v/a+(W+c)*(1/mu-2/a)};}

export function hamiltonian(y,rates,programs){return rates.map((r,s)=>r+Math.max(0,...programs.filter(p=>(s|p.adds)!==s).map(p=>p.rate*(y[s|p.adds]-y[s])-p.cost)));}

export function rk4(y,h,f){const add=(v,k,d)=>v.map((x,i)=>x+d*k[i]);const k1=f(y),k2=f(add(y,k1,h/2)),k3=f(add(y,k2,h/2)),k4=f(add(y,k3,h));return y.map((x,i)=>x+h*(k1[i]+2*k2[i]+2*k3[i]+k4[i])/6);}

export function optimal(T,{rates=[0,4.5,0,10],programs=[{name:"A",adds:1,rate:2,cost:1},{name:"B",adds:2,rate:2,cost:1},{name:"joint",adds:3,rate:1.2,cost:1}],step=.001}={}){if(T<0||step<=0)throw Error("domain");let y=rates.map(()=>0);const N=Math.max(1,Math.ceil(T/step)),h=T/N;for(let k=0;k<N;k++)y=rk4(y,h,x=>hamiltonian(x,rates,programs));const scores=programs.map(p=>({name:p.name,score:p.rate*(y[p.adds]-y[0])-p.cost}));scores.push({name:"stop",score:0});scores.sort((a,b)=>b.score-a.score);return{values:y,initialAction:scores[0].name};}

export function cashBuffer(costs,collections){if(costs.length!==collections.length)throw Error("length");let gap=0,peak=0;for(let i=0;i<costs.length;i++){if(costs[i]<0||collections[i]<0)throw Error("cash");gap+=costs[i]-collections[i];peak=Math.max(peak,gap);}return peak;}

export function stageCompletion({T,B,a=2,b=2,c=1,v=4.5}){if(!(T>=0&&B>=0&&a>0&&b>0&&c>0&&v>=c))throw Error("domain");const m=Math.min(T,B/c);if(!m)return 0;const first=-Math.expm1(-a*m);const second=Math.abs(a-b)<1e-10?a*m*Math.exp(-b*T):a*Math.exp(-b*T)*(-Math.expm1(-(a-b)*m))/(a-b);return Math.max(0,Math.min(1,first-second));}

export function jointCompletion({T,B,advance=0,mu=1.2,c=1}){if(!(T>=0&&B>=0&&advance>=0&&mu>0&&c>0))throw Error("domain");return -Math.expm1(-mu*Math.min(T,(B+advance)/c));}

export function advanceToMatch({prob,T,B,mu=1.2,c=1}){if(!(prob>=0&&prob<1&&T>=0&&B>=0&&mu>0&&c>0))throw Error("domain");const time=-Math.log1p(-prob)/mu;return time>T+1e-10?Infinity:Math.max(0,c*time-B);}
