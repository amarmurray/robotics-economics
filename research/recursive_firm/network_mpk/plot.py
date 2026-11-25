"""Distributions over eligible sites and signed transmission of the packaging standard."""
import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


root = Path(__file__).resolve().parent
result = json.loads((root/"results.json").read_text())
node_names = ["Digital dispatch","Packaging plant","Fulfillment","Hospital supply"]
stats = result["regimes"]["baseline"]["nodes"]
data = result["transformations"]["standardization"]
plt.rcParams.update({"font.size":11,"svg.fonttype":"none","svg.hashsalt":"network-mpk-1",
                     "axes.spines.top":False,"axes.spines.right":False})
fig,axes = plt.subplots(1,2,figsize=(11,4.25),layout="constrained")
left,right = axes
for i,key in enumerate(result["node_order"]):
    s = stats[key]["ratio"]
    color = "#86551d" if i==0 else "#176b72"
    left.plot([s["p10"],s["p90"]],[i,i],linewidth=3,color=color)
    left.scatter(s["p50"],i,s=60,color=color,zorder=3)
left.axvline(1.,linestyle="--",linewidth=1.2,color="#555555")
left.text(1.02,2.7,"Purchase cost",fontsize=9,color="#555555")
left.set(yticks=range(4),yticklabels=node_names,ylim=(3.55,-.65),xlim=(-.05,1.83),
         xlabel="Discounted gain / initial purchase cost")
left.set_title("Value of the next capacity block",loc="left",fontweight="bold",fontsize=12)
right.axvline(0,linewidth=.8,color="#555555")
y=np.arange(4)
right.barh(y-.18,data["induced"]["mean"],height=.32,color="#247b84",label="Changed final sales mix")
right.barh(y+.18,data["engineering"]["mean"],height=.32,color="#d99043",label="Changed input recipe")
right.scatter(data["gross"]["mean"],y,marker="D",s=33,color="#242930",label="Combined change",zorder=4)
right.set(yticks=y,yticklabels=node_names,ylim=(3.6,-.65),xlabel="Change in stage work per period")
right.set_title("How a hospital packaging standard travels",loc="left",fontweight="bold",fontsize=12)
right.legend(loc="upper center",bbox_to_anchor=(.48,-.20),frameon=False,ncol=2,fontsize=8.5)
axes[0].grid(axis="x",alpha=.14)
axes[1].grid(axis="x",alpha=.14)
fig.savefig(root/"network_returns.svg",metadata={"Date":None})
