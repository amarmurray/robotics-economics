from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from probe_checks import probe_value, LOCAL, POOLED
from physics_checks import run
from control_checks import errors
DIR=Path(__file__).resolve().parents[1]/'figures'
teal='#116c65'; red='#ac5337'; navy='#18303f'; grey='#52626b'
plt.rcParams.update({'font.size':10,'axes.spines.top':False,'axes.spines.right':False,
'axes.labelcolor':navy,'xtick.color':grey,'ytick.color':grey,'axes.edgecolor':'#a2b0b1',
'figure.facecolor':'white','savefig.facecolor':'white','legend.frameon':False})
def save(fig,name):
    fig.tight_layout(pad=1)
    fig.savefig(DIR/(name+'.png'),dpi=210,bbox_inches='tight',pad_inches=.06)
    plt.close(fig)
x=np.arange(0,3501,25)
f,a=plt.subplots(figsize=(7.1,2.65))
for mode,label,color in [(LOCAL,'Locally controlled budgets',teal),(POOLED,'Pooled budget',red)]:
    a.plot(x,[float(probe_value(mode,int(v))) for v in x],lw=2.8,color=color,label=label)
a.axhline(200,color=navy,ls=':',label='Probe fee ($200)')
a.set(xlabel='Contribution displaced by pooled training ($ per cohort)',ylabel='Gross value of the probe ($)',ylim=(-16,715),xlim=(0,3500))
a.legend(loc='upper left',fontsize=8.5,ncol=2);a.grid(axis='y',alpha=.18);save(f,'probe')
stats=run()
f,a=plt.subplots(figsize=(7.1,2.65))
sizes=[25,100,400,1600,6400]
for name,label,color in [('independent','Independent faults',teal),('common','Shared environment',red)]:
    vals=stats['expected_missed_fraction_by_fleet_size']
    a.plot(sizes,[100*vals[str(n)][name] for n in sizes],lw=2.5,marker='o',color=color,label=label)
a.axhline(.5,ls=':',color=red,alpha=.7)
a.set_xscale('log',base=4);a.set_xticks(sizes,labels=[str(n) for n in sizes])
a.set(xlabel='Fleet size at eight rescue slots per 100 clients',ylabel='Missed jobs (% of fleet)',ylim=(-.05,1.5))
a.legend(loc='upper right',fontsize=9);a.grid(axis='y',alpha=.18);save(f,'fleet')
f,a=plt.subplots(figsize=(7.1,2.45))
for d,l,c in [(False,'Current utilization',teal),(True,'One-period stale utilization',red)]:
    a.plot(errors(1.2,d,18),color=c,marker='o',ms=3,lw=2,label=l)
a.axhline(0,color=grey,lw=.6);a.set(xlabel='Price-update round',ylabel='Deviation from clearing price',xticks=[0,3,6,9,12,15,18])
a.legend(fontsize=8.5,loc='upper left');a.grid(axis='y',alpha=.18);save(f,'price_feedback')
