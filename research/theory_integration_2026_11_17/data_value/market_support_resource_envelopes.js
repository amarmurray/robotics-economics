function model(){
 const gcd=(a,b)=>{a=a<0n?-a:a;b=b<0n?-b:b;while(b){const r=a%b;a=b;b=r;}return a||1n;};
 const q=(x,y=1n)=>{x=BigInt(x);y=BigInt(y);if(y<0n){x=-x;y=-y;}if(!y)throw Error("zero");const g=gcd(x,y);return [x/g,y/g];};
 const plus=(a,b)=>q(a[0]*b[1]+b[0]*a[1],a[1]*b[1]),minus=(a,b)=>q(a[0]*b[1]-b[0]*a[1],a[1]*b[1]),over=(a,b)=>q(a[0]*b[1],a[1]*b[0]),fmt=a=>a[1]===1n?String(a[0]):String(a[0])+"/"+a[1];
 let checks=0;const same=(a,b)=>{checks++;if(fmt(a)!==fmt(b))throw Error(fmt(a)+" != "+fmt(b));};
 const G=q(6),M=q(7),k=q(1,2),one=q(1),zero=q(0);
 const forced=[minus(minus(zero,k),G),minus(minus(M,k),G)];
 same(forced[0],q(-13,2));same(forced[1],q(1,2));
 const rollback=[minus(minus(G,k),G),minus(minus(M,k),G)];
 same(rollback[0],q(-1,2));same(rollback[1],q(1,2));
 const supported=q(13,2),n=q(3);
 const low=over(plus(supported,plus(G,G)),n),hi=over(plus(supported,plus(M,M)),n);
 same(low,q(37,6));same(hi,q(41,6));
 const net=[minus(minus(low,k),G),minus(minus(hi,k),G)];
 same(net[0],q(-1,3));same(net[1],q(1,3));
 const critical=minus(hi,G);same(critical,q(5,6));same(minus(M,G),one);
 same(minus(hi,low),q(2,3));same(minus(minus(hi,low),q(1,3)),q(1,3));
 same(minus(M,q(2)),q(5));same(minus(M,G),q(1));
 return {kind:"exact synthetic normalized whole-service contribution; NOT field data",observedWholeNetworkGross:{GG:"6",XG:"7",GX:"7"},forcedAllXGrossPossible:["0","7"],forcedAllXCostHalfNetDifference:forced.map(fmt),validIdenticalEnvironmentRollbackAllXCostHalfNetDifference:rollback.map(fmt),threeIndependentCatchments:{observedAllXGross:"13/2",unsupportedCount:2,fullXGrossFiniteRegisterBounds:[fmt(low),fmt(hi)],allXCostHalfVsG6NetBounds:net.map(fmt),width:"2/3",widthAfterOneMoreFullPolicyObservation:"1/3",costDominanceThreshold:fmt(critical)},oneSlotGrossCeiling:"7",unobservedAllXCostDominanceThreshold:"1",checks};
}
if(typeof module!=='undefined' && require.main===module) console.log(JSON.stringify(model(),null,2));
