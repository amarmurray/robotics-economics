"use strict";
const run = function run(){
 let checks=0;const ck=(v,m)=>{checks++;if(!v)throw Error(m)};
 const rows=[];
 for(let j=0;j<=8;j++){
  const atoms=[];for(let s=0;s<2;s++)for(let y=0;y<2;y++)for(let z=0;z<2;z++)atoms.push({s,y,z,n:(s+y+z)%2===1?j:8-j});
  const sum=f=>atoms.reduce((a,t)=>a+t.n*f(t),0);
  ck(sum(()=>1)===32,"eligible mass");for(const k of ["s","y","z"])ck(sum(t=>t[k])===16,"first moment");for(const [a,b] of [["s","y"],["s","z"],["y","z"]])ck(sum(t=>t[a]*t[b])===8,"pair");
  const x=sum(t=>t.s*t.y*t.z);ck(x===j,"triple");
  const skip=3*64-64+2*32+sum(t=>8*t.s+2*t.s);
  const take=3*64-64+2*32+sum(t=>8*t.s+2*t.s*(1-t.y)+10*t.s*t.y*t.z);
  ck(skip===352,"skip value");ck(take===336+10*j,"take value");
  // Optional G and later M with independent ex ante randomization. g,q are probabilities in eighths.
  for(let g=0;g<=8;g++)for(let q=0;q<=8;q++){
   const value64x64=(8-g)*8*256+g*((8-q)*skip+q*take);
   ck(value64x64===16384+g*768+g*q*(10*j-16),"policy expansion");
   if(j===0)ck(value64x64<=352*64,"robust upper");
  }
  rows.push({j,eligible:32,s:16,sy:8,sz:8,yz:8,x,skip,take,known_best:Math.max(skip,take),independent_E:384,free_P_skip:416});
 }
 ck(rows[0].take<384&&rows[8].take>384,"ranking reversal");
 ck(rows.filter(t=>t.x>=7).every(t=>t.take>=406),"joint audit grid");
 // Walsh characters certify degree <=2 moments miss the triple interaction.
 const cube=[];for(let s=0;s<2;s++)for(let y=0;y<2;y++)for(let z=0;z<2;z++)cube.push([s,y,z]);
 const chars=Array.from({length:8},(_,m)=>cube.map(t=>t.reduce((v,x,i)=>v*((m>>i)&1?2*x-1:1),1)));
 for(let a=0;a<8;a++)for(let b=0;b<8;b++)ck(chars[a].reduce((v,x,i)=>v+x*chars[b][i],0)===(a===b?8:0),"orthogonal basis");
 ck(cube.reduce((v,t,i)=>v+t[0]*t[1]*t[2]*chars[7][i],0)===1,"missing triple payoff");
 return {synthetic:true,units:"1/64",checks,rows,robust_G_family:352,retained_R:320,independent_E:384,free_P_skip:416,shared_E_committed:256};
};
console.log(JSON.stringify(run(),null,2));
