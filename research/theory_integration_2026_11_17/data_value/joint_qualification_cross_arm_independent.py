from fractions import Fraction as F
from scipy.optimize import linprog

T=[(0,0,0,0),(0,0,0,1),(0,1,0,1),(0,0,1,1),(0,1,1,1),(1,1,1,1)]
M=[T[i] for i in (0,2,3,5)]
W={
 'mono_low':(T,[(0,0,1),(0,2,2),(0,3,2),(0,5,3),(1,0,2),(4,0,1),(4,5,1),(5,0,4),(5,5,4)]),
 'mono_high':(T,[(0,0,5),(0,5,3),(1,4,2),(4,1,1),(4,5,1),(5,0,3),(5,1,1),(5,5,4)]),
 'mod_low':(M,[(0,0,2),(0,1,2),(0,2,2),(0,3,2),(1,0,1),(1,3,1),(2,0,1),(2,3,1),(3,0,4),(3,3,4)]),
 'mod_high':(M,[(0,0,5),(0,3,3),(1,2,2),(2,1,1),(2,3,1),(3,0,3),(3,1,1),(3,3,4)])
}
for key,(types,entries) in W.items():
 assert sum(k for i,j,k in entries)==20
 pa=[sum(F(k,20)*types[i][a] for i,j,k in entries) for a in range(4)]
 pb=[sum(F(k,20)*types[j][a] for i,j,k in entries) for a in range(4)]
 h=[sum(F(k,20)*types[i][a]*types[j][a] for i,j,k in entries) for a in range(4)]
 assert pa==pb==list(map(F,['2/5','1/2','1/2','3/5']))
 assert h[:3]==list(map(F,['1/5','1/4','1/4']))
 assert h[3]==F({'mono_low':'1/4','mono_high':'9/20','mod_low':'3/10','mod_high':'9/20'}[key])
 print(key, 'hSG',h[3], 'netSG',F(7,5)+8*h[3], 'E',4)
for f in T:
 for g in T:
  h=[f[i]*g[i] for i in range(4)]
  assert h[3]>=max(h[1],h[2])
  for a in (1,2):
   assert h[3] <= h[a]+f[3]-f[a]+g[3]-g[a]
for f in M:
 for g in M:
  h=[f[i]*g[i] for i in range(4)]
  assert h[3]+h[0]>=h[1]+h[2]
assert F(4,5)*6-1 == F(19,5)
# Independent floating LP corroboration; exact rational witnesses plus algebra are the proof.
for types in (T,M):
 n=len(types); eq=[];b=[]
 eq.append([1]*n*n);b.append(1)
 for task in (0,1):
  for a,p in enumerate([.4,.5,.5,.6]):
   eq.append([float((f if task==0 else g)[a]) for f in types for g in types]);b.append(p)
 for a,h in enumerate([.2,.25,.25]):
  eq.append([float(f[a]*g[a]) for f in types for g in types]);b.append(h)
 c=[float(f[3]*g[3]) for f in types for g in types]
 found=[]
 for sign in (+1,-1):
  res=linprog([sign*x for x in c],A_eq=eq,b_eq=b,bounds=(0,None),method='highs')
  assert res.success
  found.append(F(round(sum(x*y for x,y in zip(c,res.x))*20),20))
 assert found==([F(1,4),F(9,20)] if len(types)==6 else [F(3,10),F(9,20)])
 print('independent LP',len(types),'bounds',found)
