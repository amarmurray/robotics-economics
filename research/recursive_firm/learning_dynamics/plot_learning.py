"""Render the published fleet paths. Rebuild after running run_study.py."""
import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter


def draw():
    folder=Path(__file__).parent
    results=json.loads((folder/"fleet_results.json").read_text())
    paths=results["learning_paths"]
    styles=(("incidents","Incident review","#41576e","--","o"),
            ("patched_incidents","Patch + incident review","#a84629","-","s"),
            ("patched_coverage","Patch + coverage reviews","#087d70","-","^"))
    plt.rcParams.update({"font.family":"DejaVu Sans","svg.fonttype":"none","svg.hashsalt":"rft-feedback",
                         "axes.spines.top":False,"axes.spines.right":False})
    fig,axes=plt.subplots(1,2,figsize=(9.1,4.0),sharey=True)
    for ax,field,title in zip(axes,("gate","capability"),("Digital routing","Mobile robot action")):
        for name,label,color,ls,marker in styles:
            curve=paths[name]
            xs=[int(t) for t in curve]
            ys=[curve[str(t)][field] if field=="gate" else curve[str(t)][field][2] for t in xs]
            ax.plot(xs,ys,label=label,color=color,ls=ls,marker=marker,ms=4,lw=2)
        ax.set_title(title,loc="left",fontsize=13)
        ax.set_xticks([12,24,36,48,72])
        ax.set_xlabel("Operating shift")
        ax.grid(axis="y",alpha=.20)
        ax.yaxis.set_major_formatter(PercentFormatter(1,decimals=0))
        ax.set_ylim(.56,1.015)
    axes[0].set_ylabel("Unassisted stage accuracy")
    fig.suptitle("Repairing the digital stage changes what the mobile stage learns",
                 x=.065,ha="left",fontsize=15,weight="bold",y=.98)
    fig.legend(*axes[0].get_legend_handles_labels(),loc="lower center",ncol=3,frameon=False,
               bbox_to_anchor=(.51,.01),fontsize=9)
    fig.subplots_adjust(left=.08,right=.98,top=.78,bottom=.24,wspace=.15)
    fig.savefig(folder/"learning_paths.svg",metadata={"Date":None,"Description":
                "Unassisted digital and mobile stage accuracy across 96 paired synthetic worlds. Common first 12 shifts."})
    plt.close(fig)


if __name__ == "__main__":
    draw()
