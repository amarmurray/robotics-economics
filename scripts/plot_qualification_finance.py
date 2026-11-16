"""Render the analytically derived diagnostic partition from its saved result."""
from pathlib import Path
from fractions import Fraction
import json
import sys

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from model.qualification_finance import build


def plot():
    data = json.loads((ROOT/'model/results/qualification_finance.json').read_text())
    if data != build():
        raise SystemExit('Stale model artifact; run python -m model.qualification_finance')
    p = data['phase']
    low = float(Fraction(p['investment_demand_threshold']))
    high = float(Fraction(p['deployment_demand_threshold']))
    funding = float(Fraction(p['funding_threshold']))
    xmax, ymax = p['demand_intercept_bounds'][1], p['transfer_capacity_bounds'][1]
    colors = {'retain':'#DDE5ED', 'H':'#4E79A7', 'L':'#D6A550'}
    plt.rcParams.update({'svg.hashsalt':'qualification-finance-v1','font.size':11})
    fig, ax = plt.subplots(figsize=(9,5.4))
    for x,y,w,h,c in [(0,0,high,funding,'retain'), (0,funding,low,ymax-funding,'retain'),
                       (high,0,xmax-high,funding,'L'), (low,funding,xmax-low,ymax-funding,'H')]:
        ax.add_patch(Rectangle((x,y),w,h,color=colors[c],linewidth=0))
    ax.plot([low,xmax],[funding,funding],color='#23364A',lw=1.3)
    ax.plot([low,low],[funding,ymax],color='#23364A',ls='--',lw=1.3)
    ax.plot([high,high],[0,funding],color='#23364A',ls='--',lw=1.3)
    ax.text(3,1,'H\nretain cash',ha='center',va='center',color='#23364A',fontsize=13)
    ax.text(9.8,.5,'L\nqualify + commission',ha='center',va='center',color='#23364A')
    ax.text(9.2,1.5,'H\nqualify + commission',ha='center',va='center',color='white')
    ax.set(xlim=(0,xmax),ylim=(0,ymax),xlabel='Customer revenue intercept a (normalized currency per output)',
           ylabel='Permitted pre-service transfer capacity τ (currency)',
           title='Demand determines what a funding link changes')
    ax.set_xticks([0,4,low,high,10,12],['0','4','32/5','38/5','10','12'])
    ax.set_yticks([0,1,2])
    ax.spines[['top','right']].set_visible(False)
    fig.text(.08,.025,'Synthetic two-window model; fixed engineering. Dashed boundaries are demand ties.\n'
             'τ = 1 admits funding. No credit, transfer costs, empirical calibration or ownership prediction.',
             fontsize=9,color='#394B59')
    fig.tight_layout(rect=(0,.1,1,1))
    out=ROOT/'model/results/qualification_finance_phase.svg'
    fig.savefig(out,metadata={'Date':None,'Description':'Inputs: model/results/qualification_finance.json; derivation: research/theory/qualification_finance.md'})
    preview=ROOT/'work/qualification_finance_phase.png'
    preview.parent.mkdir(exist_ok=True)
    fig.savefig(preview,dpi=120)
    plt.close(fig)
    print(out)


if __name__=='__main__':
    plot()
