from fractions import Fraction as F
from itertools import product
from math import tanh
from scipy.optimize import brentq
import matplotlib.pyplot as plt
from pathlib import Path
import numpy as np
actions=(0,1)
def award(a,b):
    costs=[30-8*a,30-8*b]
    price=max(costs)
    prof=[max(0,price-costs[i])-3*t for i,t in enumerate((a,b))]
    return prof+[30-price]
for a,b in product(actions,repeat=2):
    outcome=award(a,b)
    assert sum(outcome)==8*max(a,b)-3*(a+b)
    print(a,b,outcome)
assert (1-F(5,8))*8-3==0
for events in [((0,0),(0,1),(1,0),(1,1)),((0,0),(1,1))]:
    m=[sum(o) for o in events]
    avg=lambda values:F(sum(values),len(values))
    assert avg(m)==1
    print('one slot and second slot',avg([12*min(1,n) for n in m]),avg([12*max(0,n-1) for n in m]))
import matplotlib
fig,ax=plt.subplots(figsize=(7.25,2.4),layout="constrained")
x=np.linspace(-3.3,3.3,350)
for spill,c in ((.25,'#13675f'),(.50,'#a24f34')):
    y=(1-spill)*np.tanh(.4*x)-.25*x
    ax.plot(x,y,lw=2.3,color=c,label=f'{spill:.0%} spillover')
    root=brentq(lambda v:(1-spill)*tanh(.4*v)-.25*v,.00001,3) if spill<.375 else 0
    if root:
        assert abs(.5*(1+tanh(.4*root))-.82928483)<.00001
        ax.scatter([-root,root],[0,0],s=35,color=c,zorder=3)
ax.axhline(0,color='#708188',lw=.8);ax.axvline(0,color='#99a4a9',lw=.7)
ax.legend(frameon=False,loc='upper right',fontsize=9)
ax.set(xlabel='Current lead in reusable capability, x',ylabel='Change in lead',xlim=(-3.3,3.3))
ax.spines[['top','right']].set_visible(False)
fig.savefig(Path(__file__).resolve().parents[2]/'figures/competitive_feedback.png',dpi=190)
