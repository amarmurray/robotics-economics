"""Verify the two-state policy by enumerating every stationary action pair."""
from itertools import product
import numpy as np
q=np.arange(1,13)
G=1-(1-np.array([.06,.12])[:,None])**q
m=q*(16-q)
R=np.column_stack((m+250*G,np.tile([230,76],(2,1))))
ready=np.array([[.25]*12+[0,0],[.95]*12+[.65,.65]])
i=np.arange(2)
winners=[]
for a in product(range(14),repeat=2):
    pr=ready[i,a]
    P=np.column_stack((1-pr,pr))
    W=np.linalg.solve(np.eye(2)-.9*P,R[i,a])
    candidates=R+.9*(W[0]+ready*(W[1]-W[0]))
    if np.allclose(W,candidates.max(axis=1)):
        winners.append((a,W))
assert len(winners)==1 and winners[0][0]==(12,11)
delta=np.diff(winners[0][1])[0]
for v,expected in [(0,[9.85,14.22]),(100,[47.99,78.37]),(250,[-29.13,40.30]),(500,[-148.11,-13.61])]:
    advantage=(m+v*G).max(axis=1)-max(76,v-20)+.9*np.array([.25,.30])*delta
    assert np.allclose(advantage,expected,atol=.005)
    print(v,advantage)
