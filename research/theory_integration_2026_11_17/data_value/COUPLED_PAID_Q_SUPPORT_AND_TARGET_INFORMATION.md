# Coupled paid-Q support, demand information and source-to-production value

**22 November 2026.** A further chapter of *When Capabilities Become Production*, not a separate numbered question. The November 22 Models A/B scientific gate remains OPEN. This is a conditional theorem and reproducible synthetic economic example, **not** measured robotics returns, a signed deployment program, or an independent scientific-novelty claim.

## The actual gap after lawful-menu support

The preceding [lawful-menu theorem](LAWFUL_MENU_SUPPORT_AND_SHARP_REGRET.md) identified an original-buyer state-specific value of a demand report when physically and contractually legal robot actions have partially supported complete paid-production Q values. Its sharp upper bound assumed rectangular uncertainty in the two buyer-specific Q differences. But a **single shared learner, robot fleet and operator pool** generally couples the feasible economic outcomes. Those couplings can make a seemingly conservative rectangular answer substantially loose. Merely evaluating endpoints of a shared quality range can then miss the *maximum* information value entirely.

The immediate substantive question is: **which economically supported shared-learner restrictions can sharpen an original-buyer production decision, and which restrictions are merely assumed from an ML benchmark?** The answer here is a tractable conditional geometry, not a claim of real identification. It also separates a target-demand signal from physical target grounding that changes paid qualification.

The common objective remains
\[
J_k=\sup_{\pi\in\Pi_k}\mathbb E_k\Big[\sum_{t=0}^{H-1}r_t\Big]-I_k,\qquad k\in\{R,S,G,SG,E\},
\]
where the per-period return is finally **accepted and cleared original-buyer production** net of uniquely counted dispatch, robot/operator, teleoperation, compute, curation, coordination, rights and settlement costs. All lawful future adaptation, learning-generated new embodiments/recipes, recovery and induced customer production are in the continuation Q and **not** a separately added data premium. \(I_k\) includes only upfront incremental program costs not already in \(r_t\). Old qualified controllers remain available where physically and legally preserved. Free optional data availability cannot reduce the optimized gross value under the same feasible environment; forced/costly training can reduce net value. Distinct field successes, field failures/recoveries, teleoperation, simulation/synthetic and public/pretrained sources retain separate provenance and rights.

## 1. Conditional state and support

Work at one signed, fixed full-history decision state, with original-buyer order \(z\in\{A,B\}\), ex-ante eligible-market weights \(p,1-p\), \(0<p<1\), and **both** recipes \(a,b\) already certified physically qualified and lawfully usable in both states. \(a\) is the old retained controller. The signal under examination reveals the order before selecting the first action; without it, only a common pre-report action may be chosen. Ordinary subsequent observations and legal adaptive recovery remain in the state-action Q. The signal neither changes paid willingness to pay, future learner transitions nor legal menus in this specialization.

Let \(Q(z,u;\theta)\) be **whole-horizon original-buyer net paid continuation** at that full history/action, not a task benchmark. Conditional on a validated shared-payoff model, suppose
\[
d_A(\theta)=Q(A,b;\theta)-Q(A,a;\theta)=\theta-\alpha,\qquad
d_B(\theta)=Q(B,b;\theta)-Q(B,a;\theta)=\theta-\beta,\quad\alpha<\beta.
\tag{1}
\]
Here \(\theta\) is an *economically calibrated shared quality factor*, not a universal scalar robot intelligence measure; \(\alpha,\beta\) are buyer-specific **economic break-even** intercepts, not merely benchmark task-qualification cutoffs. The slopes of one, the known thresholds, the fixed original-buyer mix, and the fixed lawful menu are **strong conditional information-structure assumptions**, not empirical findings. A shared checkpoint may still have buyer-specific, nonlinear or correlated paid effects; if so (1) must be rejected, relaxed to an audited convex feasible set, or left unidentified.

The (post-report minus blind) optimized *gross* original-buyer information value is
\[
L(\theta)=p(d_A)_+ +(1-p)(d_B)_+
-\big[pd_A+(1-p)d_B\big]_+.
\tag{2}
\]
No extra signal premium is added to \(J_{SG}\); this is the difference between two production policies, already inside the same value table.

## 2. Exact shared-factor information theorem and proof

**Proposition (tent-shaped information value).** Put \(\bar\alpha=p\alpha+(1-p)\beta\). Under the above legal common-menu and conditional paid-Q restrictions,
\[
L(\theta)=
\begin{cases}
0,&\theta\le\alpha,\\
p(\theta-\alpha),&\alpha<\theta\le\bar\alpha,\\
(1-p)(\beta-\theta),&\bar\alpha<\theta<\beta,\\
0,&\theta\ge\beta.
\end{cases}\tag{3}
\]
Its global maximum is \(p(1-p)(\beta-\alpha)\), attained at the **interior** factor \(\bar\alpha\). On an audited factor interval \([\ell,u]\), the **sharp** lower and upper information-value bounds are
\[
\underline L=\min\{L(\ell),L(u)\},\qquad
\overline L=L\big(\min\{u,\max\{\ell,\bar\alpha\}\}\big).
\tag{4}
\]
Both endpoints are attainable under a feasible complete-history factor set that actually contains the interval; if only an outer interval is known, these are outer bounds, not sharp for the unknown true set.

*Proof.* Relative to always choosing \(a\), a buyer-aware dispatcher adds \(p(d_A)_++(1-p)(d_B)_+\). Blind precommitment adds \([pd_A+(1-p)d_B]_+\); the old-a continuation cancels. For \(\theta\le\alpha\) or \(\theta\ge\beta\), both differences have the same sign, giving zero information loss. For \(\alpha<\theta<\beta\), \(d_A>0>d_B\); the loss is \(\min\{p(\theta-\alpha),(1-p)(\beta-\theta)\}\). These lines cross at \(\theta=\bar\alpha\), with height \(p(1-p)(\beta-\alpha)\). The function is globally single-peaked, flat at zero beyond the thresholds. Therefore its minimum over any closed interval occurs at an interval endpoint and its maximum at the projected peak. QED.

**Why the earlier rectangular maximum is not sharp under shared learning.** If one uses only the coordinate bounds \(\theta\in[\alpha,\beta]\), then \(d_A\in[0,D]\), \(d_B\in[-D,0]\), \(D=\beta-\alpha\), and discards their coupling, the rectangular upper bound is \(\min\{p,1-p\}D\). But the shared-factor maximum is only \(p(1-p)D\). For equal buyer weights and unit spread the rectangle permits the impossible combination \((d_A,d_B)=(1,-1)\), suggesting an upper information value \(1/2\), while the true line \(d_B=d_A-1\) peaks at \((1/2,-1/2)\) with information value \(1/4\). Both feasible *factor endpoints* yield zero. An endpoint-only search would incorrectly call the information value zero throughout. **Dependence can tighten a bound while moving its optimizer to an interior history.**

This difference is about the structure of the **paid relative-Q feasible set**, not a learning-transfer novelty claim or empirical return. If the common-factor restriction has not been established from original-buyer complete paid outcomes, it is not permissible to replace the broad rectangle with the tighter segment.

## 3. General lawful coupled polyhedral Q support

A linear common factor is not required for the following **finite-dimensional geometric method**. Let \(\mathcal C\subset\mathbb R^2\) be a nonempty compact convex polytope of **jointly feasible original-buyer relative paid-Q vectors** \((d_A,d_B)\), derived from justified common learner/operator/buyer/rights constraints. Do not form it by treating independent learned task-skill marginals as dollars. For any \(d\in\mathcal C\), (2) is zero in same-sign quadrants; in the quadrant \(d_A\ge0\ge d_B\),
\[
L(d)=\min\{p d_A,(1-p)(-d_B)\},
\tag{5}
\]
with the reversed analogue in the other opposite-sign quadrant.

**Proposition (exact polyhedral partition).** Partition \(\mathcal C\) by \(d_A=0\), \(d_B=0\), and the blind-dispatch tie line \(p d_A+(1-p)d_B=0\). On each resulting closed convex cell, \(L\) is affine. Consequently its sharp global minimum and maximum over the complete supported polytope occur at **vertices of the partition cells**, including boundary intersections not vertices of the original \(\mathcal C\). This remains valid for line segments or singletons.

*Proof.* For fixed signs of the two relative Q values and fixed sign of their weighted sum, each positive-part term in (2) is either its linear argument or zero. Their combination is therefore affine on that cell. A linear functional on a compact polytope attains extrema at its vertices; take the finite union of the cell vertices. The partition does not enlarge or delete \(\mathcal C\), hence the extrema are sharp conditional on \(\mathcal C\)'s genuine attainable support. QED.

An equivalent maximum algorithm solves two elementary linear programs: in \(d_A\ge0\ge d_B\), maximize \(t\) subject to \(d\in\mathcal C\), \(t\le p d_A\), \(t\le(1-p)(-d_B)\); repeat after swapping the signs. Zero is attainable if a supported same-sign vector exists. The accompanying exact Fraction polygon-clip checker enumerates the cell vertices. Its numerical agreement tests the implementation, not the theorem.

This repairs a specific inference error: **for nonrectangular, jointly constrained original-buyer paid responses, rectangular endpoint formulas can be conservative, but testing only extreme parameter values is not a valid replacement.** Nonconvex lawful action constraints, unverified rights or global learner spillovers require separate components, not unexamined convexification.

## 4. Target grounding is not the buyer report

There are at least two distinct interventions frequently called "grounding." **Information grounding** reveals original-buyer order/report without changing lawful recipes or paid Q, as in (2). **Physical/technical target alignment** changes source-to-qualification transfer or a qualified recipe's paid continuation, possibly also its legal menu and resource demand. They should not share a scalar G parameter by definition.

For a fixed qualified menu, suppose one target-alignment intervention lowers buyer-A's economic break-even intercept from \(\alpha\) to \(\alpha'\le\alpha\), without changing capacity, costs, rights, buyer mix or old action. Its addition to *buyer-aware optimized paid production* is
\[
T(\theta)=p\{(\theta-\alpha')_+-(\theta-\alpha)_+\}.
\tag{6}
\]
\(T(\theta)\) is nondecreasing in \(\theta\): it is zero below \(\alpha'\), grows linearly until \(\alpha\), then plateaus. Hence a larger source-trained shared factor and this particular kind of technical alignment have nonnegative increasing differences in qualified **production** even while the *incremental value of demand information* \(L(\theta)\) falls after \(\bar\alpha\). This is an exact conditional complement/substitute distinction; it does **not** establish a positive intrinsic neural-data cross-derivative. If grounding first makes an action lawful or physically qualified, the action menu itself changes, and (6) is not the correct unmodified model.

Thus observing a weaker marginal report dividend after more source learning is **not negative transfer**. It can mean the source-trained recipe has become sufficiently generalist that the same dispatch is efficient under both buyers. If extra data merely becomes freely available, keeping the old policy remains possible.

## 5. The actual source/grounding/embodiment investment estimand

With a genuine order report, the two certified recipes and fixed original market, the **gross** SG production contribution, including all conditional future paid value already in Q, is
\[
V_{SG}(\theta)=B + p(\theta-\alpha)_+ +(1-p)(\theta-\beta)_+,
\quad B=pQ(A,a)+(1-p)Q(B,a).
\tag{7}
\]
The net program uses \(J_{SG}=V_{SG}-C_{SG}\) with once-counted additional costs. Equation (7) is nondecreasing in \(\theta\); the nonmonotone information dividend of (3) does not contradict that fact. Source mixtures and costly acquisition select a reachable \(\theta\), but field/failed-recovery, T teleoperation, M simulation/synthetic and public pretrained streams must remain distinct actions with lineage, compute and rights rather than a homogeneous pool.

If, **only as a hypothetical additional fully supported structure**, a legal E program with its own paid embodiment has \(J_E(\theta)=e_0+\lambda\theta-C_E\) under the *same* shared factor and original eligible buyer market, then \(J_{SG}-J_E\) is piecewise affine. Its **sharp extrema on a real shared-factor interval** occur at \(\ell,u\) and any \(\alpha,\beta\) in the interval. This follows by partitioning at the positive-part kinks. A real E embodiment changes action and physical capacity sets and generally **cannot** be assigned this affine form without complete physical/paid evidence. If E's paid response is unknown, the SG-versus-E sign remains unidentified. A synthetic bound on \(L\) alone is not a signed SG/E investment result.

In Model A, fixed approved service menus and original-buyer Q can in principle give a complete finite production LP with scarce robots/operators, resource shadow prices and complementary qualification bundles. Model B additionally includes data-generated future services, linked checkpoint and rights transitions, demand response, flexible embodiments, operator spillovers, recovery and multi-period customer capture. In Model B, apply (1)–(7) only at history cells where Q already includes lawful adaptive continuation and the support restriction is defensible; otherwise use the earlier full-horizon Bellman/resource-price and policy-support bounds. Never transport a one-decision tent into a global program ranking without those conditions.

## 6. Reproducible counterworld and prospective discriminator

A small, **synthetic normalized complete-paid-Q** construction takes \(p=1/2,\alpha=0,\beta=1,\theta\in[0,1]\). Old \(a\) has full Q 1 in each buyer state and new lawful \(b\) has \(Q(A,b)=1+\theta\), \(Q(B,b)=\theta\). The assumed shared learner forces both together. The report value is \(L(\theta)=\min\{\theta/2,(1-\theta)/2\}\), with zero endpoint values and maximum 1/4 in the interior. An unjustified rectangular relaxation yields 1/2. The **gross** buyer-aware SG paid contribution is \(1+\theta/2\), monotone; neither any assumed cost nor a task benchmark was turned into dollars. A triangular coupled feasible set also has maximum 1/4, not 1/2. The data are invented exclusively to test identification logic.

Prospective evidence must link the **same checkpoint/learner and originally eligible buyer offer cohort** to full buyer-conditional, lawfully approved accepted/cleared Q. The common-factor slope and intercept restrictions require matched complete-service, conditional multi-buyer outcomes and common robot/operator/rights exposure; benchmark transfer cannot validate them. Separate matched interventions must record order/no order, report acquisition, learner and source provenance, physical target alignment, new embodiment eligibility, hours/robot/operator opportunity costs, refunds, rights to train/retain/reuse and future licensed paid service. Do not condition the original cohort on success. If shared-learner dependence, nonlinear transfer, newly learned embodiments or policy-induced demand change the support, widen the feasible Q set rather than calling the parametric certificate empirical.

The [prospective support protocol](COUPLED_PAID_Q_EVIDENCE.md), [exact Python checker](coupled_paid_q_certificate.py), [record](coupled_paid_q_certificate_results.json), [independent integer checker](coupled_paid_q_independent.js), and [separate exercises](COUPLED_PAID_Q_EXERCISES.md)/[solutions](COUPLED_PAID_Q_SOLUTIONS.md) make the conditional statement falsifiable. No authorized whole-SG/E robotic comparison, original-buyer receipts, signed rights/transition envelopes, or actual common-factor paid-Q restriction exists yet.

## 7. Bounded prior art, external official source and gate

This uses established positive-part, value-of-information, finite-menu, convex-polyhedral, robust-decision and dynamic-production mathematics. Blackwell's information comparison, Manski's partial identification, process-flexibility/LP duality, interference-aware designs and MDP state abstractions are prior foundations. Farboodi, Koh and Xia's *Data-Driven Automation* (June 2026, https://arxiv.org/abs/2606.10127) already values future data in production and discusses complementary data aggregation in Appendix B; those are not claimed as innovations here. The possible *economic synthesis* is in empirically joining source provenance, full paid qualifications, buyer-order signals, scarce shared robot/operator/embodiment resources, legal reuse and recursively generated customer-service options.

For the wider empirical topology agenda, the official BLS inter-industry page (https://www.bls.gov/emp/data/input-output-matrix.htm; page modified August 27, 2026) now links a 1997–2025 historic and 2035 projected research archive at https://www.bls.gov/emp/input-output/input-output.zip. That direct ZIP source was located but **not successfully downloaded in this run**, so no numeric coefficient, sector edge or production ranking was extracted or invented. BEA's official industry I/O documentation is at https://www.bea.gov/itable/input-output and https://www.bea.gov/resources/guide-interactive-industry-input-output-accounts-tables. A valid direct public byte retrieval and a documented sector crosswalk remain future steps, not evidence of a passed quantitative gate.

**November 22 synthesis finding:** The integrated paper's scientific bottleneck is now explicit. A legally and physically qualified production menu, buyer-specific paid Q, its jointly constrained feasible support, and the entire rights/learner/operator continuation are needed to rank source+target acquisition against an embodiment. Lower-order task benchmarks and a stronger purely synthetic inequality cannot substitute for signed paid-service data. **November 22 Models A/B acceptance remains OPEN**; prioritize the coherent theory and empirical design through December 6, then narrow scope before claiming unverified value. The original November 29, December 6/13/18/23/24 and December 25 23:59 Eastern milestones remain in force.
