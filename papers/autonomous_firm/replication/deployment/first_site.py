from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from decimal import Decimal as D

q = np.arange(1,13)
v = np.linspace(0,300,1801)
value = q[:,None]*(16-q[:,None]) + (1-.9**q[:,None])*v
advantage = value.max(axis=0) - np.maximum(76,v-20)
lo,hi = 12/(1-.9**8),68/.9**12
assert abs(lo-21.07)<.001 and abs(hi-240.77)<.003
for i in range(3001):
    V=D(i)/10
    best,qstar = max((n*(16-n)+(1-D('.9')**n)*V,n) for n in range(1,13))
    assert (best>max(76,V-20)) == (lo<float(V)<hi)
    if V in (0,22,100,250):
        print('V',V,'A blocks',qstar,'A value',best,'outside option',max(76,V-20))
fig,ax=plt.subplots(figsize=(8.3,2.43),layout='constrained')
ax.axhline(0,color='#64747b',lw=1)
ax.fill_between(v,advantage,0,where=advantage>=0,color='#d3e9e1',interpolate=True)
ax.plot(v,advantage,color='#146b62',lw=2.5)
for loc,label,dx in ((lo,'21.07',3),(hi,'240.77',4)):
    ax.scatter([loc],[0],c='#0d524c',zorder=4,s=18)
    ax.annotate(label,(loc,0),(loc+dx,-9),fontsize=9,color='#194640')
ax.set(xlim=(0,300),ylim=(-22,50),xlabel='Value of the target order, V',ylabel='Advantage of A',yticks=[-20,0,20,40])
ax.spines[['top','right']].set_visible(False)
ax.spines[['bottom','left']].set_color('#b7c4c4')
ax.grid(axis='y',alpha=.16)
ax.tick_params(length=0,colors='#394e59')
fig.savefig(Path(__file__).resolve().parents[2]/'figures/regime.png',dpi=220)
