# Paired target evidence, conditional report validity and the economic option created by source learning

**20 November 2026 — same November 22 Models A–B original-buyer gate in When Capabilities Become Production.** This extends [regime-conditioned qualification and flexibility](REGIME_CONDITIONED_QUALIFICATION_AND_FLEXIBILITY.md) without switching questions. That result used a calibrated target-report kernel conditional on joint qualification. The present question is what survives when that kernel does **not** transport across source-selected qualification histories, even though all one-way qualification and report tables, and overall report accuracy, have been recorded. Results are standard probability/decision mathematics applied to a conditional robotics economy; not scientific novelty, actual robot performance, a dataset market price, a certified rescue procedure or empirical customer value.

## Environment, timing and the physically signed menu

Consider the original procurement parent plus robot/dispatch/operator cluster as the unit. Before embodiment lock, heterogeneous source development yields Q=(Q_A,Q_B), and C denotes both complete-service specialist embodiments physically qualified, Q=11. Original customer regime T is A or B. A target report Y is A or B before the optional post-report embodiment choice. R is an independently admitted, retained complete policy contributing 2 normalized original-service units in either regime. A physically signed specialist E_A or E_B contributes 4 in the matching regime and 0 otherwise; these are **stipulated accepted-service contribution values**, inclusive of demand, customer receipts, variable operator usage and contract consequences under one unchanged offer, not benchmark scores. Policy F can choose either qualified specialist *after Y* and retains R. Policy L must choose one installed body before Y, can abstain in favor of independently qualified R after observing Y, and cannot use the uninstalled body. F and L are assumed signed as *whole buyer–robot–operator* policies with the same feasible resources and rights. Neither is inferred safe from a qualification score. Outside C, F and L have the same qualified body options and cancel in their difference.

The relevant joint history mass within C is

- q=P(C), x=P(C,T=A), m=P(C,Y=A), z=P(C,T=A,Y=A).

Its four nonnegative complete cells in order (T=A,Y=A), (A,B), (B,A), (B,B) are (z, x-z, m-z, q-x-m+z). The sharp Fréchet support for z given q,x,m is

\[
I_C=[\ell_C,u_C]=[\max(0,x+m-q),\min(x,m)].
\]

Importantly, q is the **same-development-run joint qualification probability**; neither independence of specialist pass events nor a fixed positive source-transfer coefficient is assumed. Observed q,x,m alone do not reveal the triple overlap z.

## Proposition: conditional information-use value without a calibrated source-invariant report

Let d_A=2z-m and d_B=2x+m-q-2z. In the stipulated customer production table, the gross flexibility difference equals

\[
D(F,L;z)=|d_A|+|d_B|-|d_A+d_B|
=4\,\operatorname{dist}(z,B),
\]
\[
B=\left[\min\left\{\frac m2,\frac{2x+m-q}{2}\right\},
          \max\left\{\frac m2,\frac{2x+m-q}{2}\right\}\right].
\]

Here dist is Euclidean distance on the real line to a closed interval. Consequently, if z belongs to any nonempty, **attainable** closed interval I=[l,u], its sharp gross production-option interval is

\[
D_{\min}=4\,\operatorname{dist}(I,B),\qquad
D_{\max}=4\max\{\operatorname{dist}(l,B),\operatorname{dist}(u,B)\}.
\]

The distance between intervals is zero if they intersect. These are sharp relative to the stated joint-law restrictions and the fixed signed menu/market payoff table. If *only* q,x,m are observed, D_min=0: the conditionally independent coupling z=xm/q (for q>0) lies in I_C and B. Thus **a positive-cost hardware-switching option cannot be robustly justified on these pairwise statistics alone**, even with known separate qualification/demand and qualification/report margins. This is not a statement that more optional free data lowers value, or that hardware flexibility has no value.

**Proof.** Conditional on Y=A, switching from R to E_A has full-parent increment +2 in regime A and -2 in B, contributing 2d_A in expectation; E_B contributes -2d_A. On Y=B, analogous increments are ±2d_B. F chooses the better available body after the report and improves over R by 2(|d_A|+|d_B|). L chooses one body before the report and may abstain after each Y, improving by 2 max{(d_A)_++(d_B)_+, (-d_A)_++(-d_B)_+}. Their difference is |d_A|+|d_B|-|d_A+d_B|. Since d_A=2(z-m/2), d_B=-2(z-(2x+m-q)/2), the sum of absolute distances minus twice the separation of their zeros equals four times distance to the interval between the zeros. Distance to an interval is convex and piecewise linear, attaining its maximum over I at an endpoint and its minimum at the projection of I toward B. The cell construction attains every z∈I_C. The independence coupling z=xm/q is valid and yields report differences of the same sign, hence D=0. QED.

This is a *conditional production option*, not a standalone data premium added above an already optimized future J. If F costs k more than L in counted embodiment, switching, validation and opportunity resources, net incremental value is D-k. The old L/R option must remain genuinely admissible for the optional-set comparison. If the source training itself is forced, costly or removes legacy rights, its impact is evaluated separately within J.

## Proposition: sharp bounds using unconditional report accuracy but no triple pairing

Suppose both C and its complement N have observed two-way margins. Define q_0=1-q, x_0=P(N,T=A), m_0=P(N,Y=A), and their sharp AA overlap z_0∈I_0=[max(0,x_0+m_0-q_0),min(x_0,m_0)]. Suppose also the **whole-parent** agreement rate a=P(Y=T) is known, but the source-/qualification-specific report kernel is not.

Writing original regime share π=x+x_0 and overall A-report share M=m+m_0, the globally observed agreement implies

\[
S=\frac{a-1+\pi+M}{2}=z+z_0.
\]

Hence the sharp triple-overlap identified set is

\[
I=I_C\cap[S-u_0,\ S-\ell_0].
\]

It is empty if the supplied margins and agreement cannot coexist. Otherwise, insert I into the preceding distance formulas for sharp D bounds. **Proof:** the total probability of agreement is 1-π-M+2(z+z_0). Every point of I permits z_0=S-z in I_0, and every such pair yields two nonnegative four-cell contingency tables with exactly the observed margins; no other restrictions are assumed. A finer four-cell Q histogram or measured selection restrictions can shrink this set, but cannot be silently assumed.

Global accuracy a is not a conditional kernel P(Y|T,Q). In particular, the preceding chapter's inversion m=(1-α)q+(2α-1)x is valid only under the stated source-/qualification-conditional symmetric report kernel; substituting unconditional a for α can be wrong despite excellent aggregate report accuracy. A *truly calibrated* predecision P(Y|T,Q,H), or observed triple same-parent Q×T×Y, supplies additional identifying restrictions.

## Exact observational-equivalence counterworld: same report accuracy, opposite hardware choice

Take a synthetic population of sixteen equal-weight original-parent units. Eight have C and eight N. In **both** worlds, each group has T=A mass 4/16 and Y=A mass 4/16; thus the same Q×T and Q×Y two-way tables, q=1/2, x=m=1/4 and π=M=1/2. The *overall* report agreement is 12/16=3/4 in both. No changed price, customer regime prevalence or qualification marginal drives the difference.

| World | C cells (AA,AB,BA,BB), units | N cells (AA,AB,BA,BB), units | D(F,L) |
| --- | --- | --- | --- |
| Source-selected signal weak where both bodies qualify | (2,2,2,2) | (4,0,0,4) | 0 |
| Matched signals in both groups | (3,1,1,3) | (3,1,1,3) | 1/4 |
| Source-selected signal strong where both qualify | (4,0,0,4) | (2,2,2,2) | 1/2 |

Because S=3/8 and z_0∈[0,1/4], the *sharp* z interval is [1/8,1/4] and the D interval is [0,1/2]. All three table rows realize it. Global report accuracy cannot tell whether the information is concentrated in the source-created deployment option or in histories where there is no switching option. If physically signed F costs 1/4 more than L, the two endpoint worlds give opposite **net** preferences (-1/4 and +1/4). Neither endpoint is a measured robotics deployment.

Under a *hypothetical, declared equal prior on these endpoint worlds*, an error-free, legally available **shadow pairing audit before irreversible embodiment commitment** yields gross expected decision improvement 1/8: before the audit max{0,E[D]-1/4}=0, while after learning the world E[max{0,D-1/4}]=1/8. After an irreversible commitment with no future option to act, the **decision** value of the same audit is zero even if its information content remains high. The shadow audit does not authorize an unapproved robot policy or by itself prove buyers will pay the stipulated 4/2 amounts.

## Consequence for X versus G versus E and the November 22 gate

This establishes a more discriminating boundary than an extra unconditioned source dataset or another calibration accuracy number. Additional X source episodes can change both the joint qualification event C and the report/demand overlap z by selecting different visited states and commercial regimes; distinct field, recovery, teleoperation, simulation, synthetic and public/pretrained inputs need separate, matched causal interventions, rights, computation and curation. Target grounding G can change *the report kernel itself* and sometimes physical observation-closed recovery. New embodiment E can create or remove a qualified action and move the irreversible lock. Their economic effects belong in the existing physically admitted optimized original-buyer V and dynamic investment J; no benchmark percentage is mapped directly to money and no continuation premium is counted twice.

The proper actual-investment comparison is over the **same original policy-closed buyer–robot–operator population**, with approved complete R/X/G/E interventions, source-specific Q×T×Y before decision, the original offer and refusals, accepted completed service and paid receipts, shared operator displacement, cohort interference, time and rights. For partially identified common worlds Ω, a robust d-over-e statement requires inf over Ω of J_d(ω)-J_e(ω)≥0, rather than subtracting independently attainable pointwise upper and lower numbers. Complete-policy randomization can identify arm means without identifying every latent triple cell; neither strategy physically approves unsigned X or resolves unoffered original customer purchases by assumption.

The prospective [same-parent gate audit](PAIRED_TARGET_SIGNAL_EMPIRICAL_GATE.md) and [exact rational audit](paired_signal_support.py) make the test falsifiable. Without actual signed F/L policies, paired original demand/report/qualification, receipt support and cross-policy assignment, this remains a conditional *structural* calculation and the November 22 acceptance gate **OPEN**.

## Closest foundations and limits

This is a conditional application of elementary Fréchet coupling, finite Bayesian decision rules, Blackwell-style option value and partial-identification decision theory. Brooks, Frankel and Kamenica, *Comparisons of Signals*, AER 114(9), September 2024, https://doi.org/10.1257/aer.20230430, explicitly explains why the joint relation of different signals matters. Manski, *Statistical Treatment Rules for Heterogeneous Populations*, Econometrica 72(4), 2004, https://doi.org/10.1111/j.1468-0262.2004.00530.x, and Montiel Olea, Qiu and Stoye, *Decision Theory for Treatment Choice Problems with Partial Identification*, https://arxiv.org/abs/2312.17623, supply closely related ambiguity/decision foundations. Farboodi, Koh and Xia, *Data-Driven Automation*, https://arxiv.org/abs/2606.10127, section 5 and Appendix B already incorporate future data value and complementarity, so neither is claimed new. This synthesis has not undergone independent originality review. The numerical certificate is a synthetic internal test, not a mathematical proof or a physical experiment. Full repository CI, official numerical BEA–BLS interindustry join, and original buyer paid customer panel remain absent. Original December 25, 2026, 23:59 Eastern cutoff and all milestone definitions remain unchanged.
