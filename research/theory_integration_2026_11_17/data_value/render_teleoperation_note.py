"""Render the reader note with ReportLab; the full derivations remain in Markdown.
Dependencies: reportlab, matplotlib. Model/tests themselves use stdlib only.
"""
from pathlib import Path
from fractions import Fraction as F
from dataclasses import replace
import argparse
import io
from xml.sax.saxutils import escape

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import mathtext
from matplotlib.font_manager import FontProperties
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
                                PageBreak, Image, KeepTogether)
from reportlab.lib.enums import TA_LEFT

from teleoperation import Model, State, Solver

ROOT = Path(__file__).resolve().parent
NAVY = colors.HexColor("#16304A")
TEAL = colors.HexColor("#007F86")
GRAY = colors.HexColor("#526170")
LIGHT = colors.HexColor("#EAF1F5")
INK = colors.HexColor("#1D2731")

def build(output: Path):
    output.parent.mkdir(parents=True, exist_ok=True)
    fonts = Path("/usr/share/fonts/truetype/dejavu")
    for name, filename in [("DejaVu","DejaVuSans.ttf"),
                           ("DejaVu-Bold","DejaVuSans-Bold.ttf"),
                           ("DejaVu-Oblique","DejaVuSans-Oblique.ttf")]:
        pdfmetrics.registerFont(TTFont(name, str(fonts/filename)))
    pdfmetrics.registerFontFamily("DejaVu", normal="DejaVu", bold="DejaVu-Bold",
                                  italic="DejaVu-Oblique", boldItalic="DejaVu-Bold")
    styles = {
        "title": ParagraphStyle("title",fontName="DejaVu-Bold",fontSize=25,leading=30,
                                textColor=NAVY,spaceAfter=16),
        "subtitle": ParagraphStyle("subtitle",fontName="DejaVu",fontSize=12,leading=17,
                                   textColor=GRAY,spaceAfter=14),
        "h1": ParagraphStyle("h1",fontName="DejaVu-Bold",fontSize=17,leading=22,
                             textColor=NAVY,spaceAfter=12),
        "h2": ParagraphStyle("h2",fontName="DejaVu-Bold",fontSize=12,leading=17,
                             textColor=TEAL,spaceBefore=12,spaceAfter=7),
        "body": ParagraphStyle("body",fontName="DejaVu",fontSize=10,leading=14.3,
                               textColor=INK,spaceAfter=8),
        "small": ParagraphStyle("small",fontName="DejaVu",fontSize=8.6,leading=12.2,
                                textColor=GRAY,spaceAfter=7),
        "cell": ParagraphStyle("cell",fontName="DejaVu",fontSize=9.2,leading=13,
                               textColor=INK),
        "head": ParagraphStyle("head",fontName="DejaVu-Bold",fontSize=9.2,leading=13,
                               textColor=colors.white),
        "callout": ParagraphStyle("callout",fontName="DejaVu-Bold",fontSize=12,
                                  leading=18,textColor=NAVY,spaceAfter=3),
    }
    story = []
    def p(text, kind="body"):
        story.append(Paragraph(text,styles[kind]))
    def gap(h=8):
        story.append(Spacer(1,h))
    def eq(tex, width=470):
        buffer = io.BytesIO()
        mathtext.math_to_image("$"+tex+"$", buffer, dpi=190, format="png",
                              prop=FontProperties(size=15), color="#16304A")
        buffer.seek(0)
        im=Image(buffer)
        scale=min(72/190,width/im.imageWidth)
        im.drawWidth=im.imageWidth*scale
        im.drawHeight=im.imageHeight*scale
        im.hAlign="LEFT"
        story.extend([Spacer(1,7),im,Spacer(1,11)])
    def table(rows, widths):
        parsed=[[Paragraph(escape(str(v)),styles["head" if i==0 else "cell"])
                 for v in row] for i,row in enumerate(rows)]
        t=Table(parsed,colWidths=widths,repeatRows=1,hAlign="LEFT")
        t.setStyle(TableStyle([
            ("BACKGROUND",(0,0),(-1,0),NAVY),
            ("ROWBACKGROUNDS",(0,1),(-1,-1),[colors.white,LIGHT]),
            ("VALIGN",(0,0),(-1,-1),"TOP"),
            ("LEFTPADDING",(0,0),(-1,-1),9),
            ("RIGHTPADDING",(0,0),(-1,-1),9),
            ("TOPPADDING",(0,0),(-1,-1),6.5),
            ("BOTTOMPADDING",(0,0),(-1,-1),6.5),
            ("LINEBELOW",(0,-1),(-1,-1),0.5,colors.HexColor("#CFD9E1"))]))
        story.extend([t,Spacer(1,10)])
    def page(label):
        story.append(PageBreak())
        p(label,"h1")
    def box(text):
        t=Table([[Paragraph(text,styles["callout"])]],colWidths=[480])
        t.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,-1),LIGHT),
                               ("BOX",(0,0),(-1,-1),0.6,colors.HexColor("#B6D4D9")),
                               ("LEFTPADDING",(0,0),(-1,-1),14),
                               ("RIGHTPADDING",(0,0),(-1,-1),14),
                               ("TOPPADDING",(0,0),(-1,-1),12),
                               ("BOTTOMPADDING",(0,0),(-1,-1),12)]))
        story.extend([t,Spacer(1,14)])

    p("ROBOTICS ECONOMICS / CONTINUING THEORY","small")
    p("Teleoperation and<br/>economic data value","title")
    p("When capabilities become production<br/>Research note | November 17, 2026 | Private working edition","subtitle")
    box("A lower-margin teleoperated job can be the best first deployment when it reveals whether the next data acquisition is worth paying for.")
    p("This note develops Amar's teleoperation seed inside the existing production, qualification and data-transfer argument. The mechanism concerns how current work produces useful observations and how those observations change the next investment. It does not presume that every intervention teaches a transferable skill.")
    p("Three consequences of one episode","h2")
    table([
        ["Channel","Economic object"],
        ["Current service","Accepted work delivered now, including retained human assistance and all operating inputs."],
        ["Physical learning","A change in the future policy or joint qualification distribution."],
        ["Information","A change in which future acquisition, embodiment or deployment is worth choosing."]
    ],[125,355])
    p("A positive task-performance effect is evidence of technical usefulness. Net economic value additionally depends on customer demand, usable capacity, competent alternatives, acquisition cost and value capture. Information can also be valuable without an immediate performance improvement.")
    p("Use the same accounting boundary","h2")
    eq(r"J_t(s)=\max_a\{m_t(a;s)+\beta\,\mathbb{E}[J_{t+1}(s')\mid s,a]\}")
    p("Current contribution includes customer payment minus operator compensation and other real operating costs. The continuation value already contains future benefits from the data. Adding a second data premium would double count them.")
    p("Status: conditional derivations, exact synthetic examples, primary-source checks and a proposed empirical test. No robot training, customer calibration or scientific novelty finding.","small")

    page("1. Put the market price in the operating problem")
    p("Let w_r be payment per accepted service unit and w_H the teleoperator's compensation per unit of time. The two prices affect different parts of the decision. If a quoted w_r instead denotes remote labor, relabel it w_H; what matters is separating the service sold from its human input.")
    p("For a finite quantity N, compare a qualified robot costing c_R per accepted unit with the best competent human/specialist alternative costing c_A. Both receive the same customer payment and use the same relevant capacity. Retaining the alternative gives:")
    eq(r"W=N\{\max(0,w_r-\min(c_A,c_R))-\max(0,w_r-c_A)\}")
    p("With five orders, robot cost 2 and alternative cost 6, the incremental value is 0 at payment 1, 5 at payment 3, and 20 at payments 6, 8 or 12. Once both modes are profitable, the benefit is the cost saving on the same quantity. A higher output price does not indefinitely multiply the value of the dataset.")
    p("The broader production network still matters","h2")
    p("The formula changes when learning unlocks previously unserved orders, changes capacity, removes a bottleneck or opens a new value-chain position. Then the new qualified recipe must enter the existing operating optimization. Its value cannot be inferred from a benchmark improvement alone.")
    p("A productive source job also has an opportunity cost: it occupies time that could deliver another service. We compare all actions with the same scarce slot, rather than treating profitable production as a free way to collect data.")
    p("How this uses Data-Driven Automation","h2")
    p("The intended source is Farboodi, Koh and Xia, arXiv:2606.10127. Production-generated data and forward-looking data value are established starting points there. This continuation makes the human intervention, transfer uncertainty, timing and qualified customer-service comparison explicit. The full chapter records the inspected source passages and their limits.")
    p("An appropriate economic-ML objective","h2")
    p("Choose a production and acquisition policy to maximize accepted-service contribution over time. Keep technical learning objectives as competent comparators. A policy maximizing qualification probability can rationally acquire more data than the economic optimum because it does not deduct the same opportunity costs.")
    box("The useful unit is a decision-relevant data-generating activity, evaluated against the best feasible alternative use of its resources.")

    page("2. A complete local policy comparison")
    p("There are two stationary operating slots. Routine work earns c each time. Source activity S creates one source batch and earns s; target activity G creates grounding, earns g and reveals a transfer signal Z. Define opportunity costs k_S = c - s and k_G = c - g.")
    p("Let F_H(x,g) be the terminal production value for transfer condition H and acquired batches x,g. The function may include useful partial learning, joint qualification and retained alternatives. Final validation makes usable recipes observable before service. The early report affects acquisition decisions, not the payoff of a fixed batch combination.")
    p("Define source-only net value B_S, grounding-only net value B_G, and M(Z), the posterior gain from adding the source batch after grounding. Then the exact best incremental value is:")
    eq(r"\Delta J^*=\max\{0,\ B_S,\ B_G+\mathbb{E}[(M(Z)-k_S)_+]\}")
    p("Proof in three steps","h2")
    p("<b>Source first.</b> If source collection provides no relevant information before the next decision, the remaining choice is routine work or a precommitted pair. Source-only value is B_S.")
    p("<b>Grounding first.</b> After the report, acquire the source only if M(Z) exceeds its opportunity cost. Pointwise optimization gives the expected positive-part term.")
    p("<b>Exhaust the menu.</b> Grounding first can always imitate a precommitted pair, and can decline the source. Routine first cannot improve on the best single-batch choice. These alternatives cover the stated two-slot menu.")
    p("Separate information from learning","h2")
    eq(r"I=\mathbb{E}[(M(Z)-k_S)_+]-(\mathbb{E}[M(Z)]-k_S)_+\geq0")
    p("Jensen's inequality proves the value of receiving the report before the acquisition commitment. Strict value requires posterior outcomes on both sides of the decision boundary. This is an established information-value argument applied to endogenous data acquisition, not a novelty claim.")
    p("Scope: one batch of each type, stationary availability, commuting physical effects, no source signal before slot two, and no discounting inside this short comparison. The executable dynamic program also checks declared alternatives and a changing source deadline.","small")

    page("3. A noisy diagnostic that changes the deployment")
    p("Synthetic parameters: routine contribution 3, source contribution 1, target-grounding contribution -1. Thus source and grounding opportunity costs are 2 and 4. The two batches unlock future incremental contribution 20 only in a reusable regime, whose prior probability is 1/4. The target report is 95% accurate in either regime.")
    table([
        ["Policy","Expected value"],
        ["Routine in both slots","6.0"],
        ["Always buy source and grounding","5.0"],
        ["Ground first; buy source after a favorable report","6.2"],
        ["Same choices, but report delayed or uninformative","6.0"],
        ["Ground first with a perfect report","6.5"]
    ],[380,100])
    p("A favorable report occurs with probability 11/40 and raises the reuse posterior to 19/22. An unfavorable report lowers it to 1/58. Acquire the source after the former and return to routine production after the latter.")
    eq(r"\Delta J=20(19/80)-4-2(11/40)=1/5")
    p("The adaptive policy obtains the new capability with probability 19/80, below the precommitted pair's 1/4, but earns more. It saves acquisition opportunity cost in unfavorable states. No separate valuation bonus is assigned to the data.")
    fig,ax=plt.subplots(figsize=(6.7,2.65),dpi=170)
    xs=[F(k,100) for k in range(50,101)]
    ys=[float(Solver(replace(Model(),accuracy=a)).solve(2,State())[0]) for a in xs]
    ax.plot([float(x) for x in xs],ys,color="#007F86",lw=2.6,label="Optimal adaptive policy")
    ax.axhline(6,color="#758391",ls="--",lw=1.5,label="Routine alternative")
    ax.axhline(5,color="#B4824B",ls=":",lw=1.8,label="Commit to both batches")
    ax.scatter([.95],[6.2],color="#16304A",s=28,zorder=4)
    ax.annotate("95% report: 6.2",(.95,6.2),xytext=(.73,6.4),
                arrowprops={"arrowstyle":"-","color":"#16304A"},fontsize=8.5)
    ax.set(xlabel="Diagnostic accuracy (synthetic)",ylabel="Total expected contribution",ylim=(4.8,6.68))
    ax.spines[["top","right"]].set_visible(False)
    ax.grid(axis="y",alpha=.17)
    ax.legend(loc="upper left",fontsize=7.3,frameon=False)
    fig.tight_layout()
    buf=io.BytesIO();fig.savefig(buf,format="png",dpi=170);plt.close(fig);buf.seek(0)
    story.append(Image(buf,width=450,height=178))
    p("The curve changes report informativeness only; fixed-batch learning outcomes remain unchanged. Exact rational arithmetic and independent contingent-policy enumeration agree.","small")

    page("4. Boundaries that change the answer")
    p("Useful partial learning preserves the mechanism","h2")
    p("The prior chapter's Gaussian source/grounding information model supplies a second terminal technology. Grounding alone now has positive value. The optimal early-report objective is approximately 6.83813, compared with 6.35865 when the same report arrives too late. Allowing repeated source or grounding batches does not alter that particular optimum.")
    p("This is a numerical alternative-formulation check. The Gaussian tolerance is a scalar evaluation proxy, not industrial qualification. It is not evidence that real robot learning follows the chosen curve.","small")
    table([
        ["Challenge","What happens in the declared example"],
        ["Competent specialist","A direct target route worth 9 after a -4 current contribution yields total value 8, beating 6.2."],
        ["Source demand expires","With source access only in slot one and prior 1/2, source first yields value 10. Waiting for diagnosis loses the opportunity."],
        ["Useful routine by-product","If routine production supplies the same source batch without forgone contribution, early and delayed reports both yield 7: the acquisition-timing premium is zero."],
        ["Standalone experiment","A perfect laboratory diagnostic with current contribution -2 yields 5.5, below the noisier productive diagnostic."],
        ["Shared qualification","One joint success with probability 1/4 is worth 5 for a 20-unit complete recipe; independent multiplication would incorrectly give 1.25."]
    ],[133,347])
    p("Higher wages can move human work earlier","h2")
    eq(r"J(w_H)=\sup_\mu\{G_\mu-w_HH_\mu\}")
    p("With a fixed feasible policy set and other prices, optimized value is convex and nonincreasing in the teleoperator wage; optimal total discounted human hours weakly fall. This follows by adding the optimality inequalities at two wages.")
    p("Current hours need not fall. Four future human hours cost 2 at wage 1/2, beating one current teaching hour plus three nonlabor units. At wage 2, teaching costs 5 versus 8 for later manual work. Current teaching rises while total human time falls. The statement is conditional, not a wage-equilibrium result.")

    page("5. A test that connects learning to economics")
    p("Observed technical evidence","h2")
    p("ThriftyDAgger's cable-routing Table 3 reports 12/15 autonomous and 15/15 intervention-aided successes. Its intervention/action statistics condition on successful episodes. We checked the text and rendered page; these observations supply no customer prices or data values.")
    p("HIL-SERL distinguishes human reward examples, demonstrations and online corrections: separate inputs rather than one count of teleoperation hours.")
    p("Two complementary empirical treatments","h2")
    p("<b>Physical learning:</b> vary inclusion of specified teleoperation data from matched starting policies, with fixed allowed compute and evaluation. Separate autonomous capability from assisted service. Count failures, resets and monitoring in cost.")
    p("<b>Information timing:</b> keep initial grounding fixed; reveal a non-safety transfer report before or after the next acquisition choice. Preserve operational permissions and routine/specialist options. Test predictive validity and acquisition adaptation.")
    p("The mechanism fails if the report is uninformative, arrives after commitment or cannot alter the next choice. Opportunity expiry also invalidates the stationary ordering claim. These are discriminating tests, not a completed field experiment.")
    p("Next theoretical question","h2")
    box("Derive the information produced by selectively chosen interventions. When a source fleet becomes more autonomous, does it supply fewer corrections useful to a different target?")
    p("Continue the same model with intervention-state selection, deliberate probes, simulation and retained safe policies. Preserve fleet, coordination, manufacturing, embodiment, customer-access and rights choices. November 22 remains the synthesis review; December 6 the contribution decision; December 25 the verified-package target.")
    p("Primary references and full materials","h2")
    p("Farboodi, Koh & Xia: arxiv.org/abs/2606.10127. Ross, Gordon & Bagnell: proceedings.mlr.press/v15/ross11a.html. Hoque et al.: proceedings.mlr.press/v164/hoque22a.html. Luo et al.: hil-serl.github.io.","small")
    p("Full assumptions and proofs: TELEOPERATION_DATA_VALUE.md. Reproduction: teleoperation.py and test_teleoperation.py. Separate proof ledger, evidence JSON, exercises and solutions accompany the chapter in the existing data_value directory. The mathematical proofs, source observations and synthetic computations are labeled separately.","small")
    p("No matched customer panel, industry calibration, independent review or publication-novelty claim. This note advances the living argument; it does not mark a scientific gate complete.","small")

    def footer(canv,doc):
        canv.saveState()
        canv.setStrokeColor(colors.HexColor("#D4DFE8"))
        canv.line(54,43,558,43)
        canv.setFont("DejaVu",8)
        canv.setFillColor(GRAY)
        canv.drawString(54,30,"Robotics Economics | Private theory note | 17 November 2026")
        canv.drawRightString(558,30,str(doc.page))
        canv.restoreState()
    doc=SimpleDocTemplate(str(output),pagesize=(612,792),
                          rightMargin=66,leftMargin=54,topMargin=43,bottomMargin=58,
                          title="Teleoperation and Economic Data Value",
                          author="Robotics Economics Research Program")
    doc.build(story,onFirstPage=footer,onLaterPages=footer)
    print(output)

if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--output",type=Path,required=True)
    args=parser.parse_args()
    build(args.output)

