# When Capabilities Become Production — coupled identification and the economic value of learning what to learn

**Private integrated theory continuation, November 18, 2026.** Extends [ENDOGENOUS_DEMAND_PERSISTENT_TRANSFER.md](ENDOGENOUS_DEMAND_PERSISTENT_TRANSFER.md), not a new paper/model number. All numerical payoffs below are invented normalized captured contribution from whole accepted customer service; no measured robot effects, real prices or scientific novelty are claimed.

## 1. The unresolved question

The earlier full-history result makes a valid comparison under *known* conditional transfer/customer-demand/qualification/recovery kernels with one persistent regime. But actual routine logs can leave those kernels jointly unidentified. Which policy comparison survives the *same* admissible full law, and can a safe diagnostic identify the joint feature that changes that comparison? The answer cannot be obtained by plugging separate marginal technical success rates, marginal order probabilities and average operator utilization into a product.

Retain the four canonical objects. \(Q_t\) is a body, retained controller menu, jointly qualified service recipes, rights and approved resources. \(\omega_t\) contains customer orders (including zero), contract capture, alternative specialists and scarce resources. \(V(Q_t;\omega_t)\) is optimized accepted customer contribution. For a full history-dependent feasible policy \(\pi\), \(J(\pi;m)\) counts actual period accepted contribution and acquisition costs *once*, and terminal \(V\) once, under the same complete world \(m\). Source field experience, recoveries, teleoperation, simulation and pretrained/public/synthetic inputs alter learning and observation kernels differently; they have no common exogenous unit price.

## 2. Finite response-type law and a sharp paired certificate

Let \(k\in\{1,\ldots,K\}\) index **complete potential-history response types** for an initially eligible independent customer/learning pool. A type specifies, for each allowed initial route and every reachable report, route-induced future orders, retained controller and safe visit support, corrections/qualification, accepted service, peak recovery, and feasible fallback. A type's persistent source-to-target alignment does **not** reset after reports. The joint population distribution \(q_k\) is unknown. Feasible laws form
\[
 {\cal Q}=\{q\geq0:\mathbf1^\top q=1,\;Aq=b\}. \tag{CI1}
\]
Rows of \(A\) are **jointly compatible, pretreatment-referenced** observed moments; e.g. safely audited target demand, random route assignment with complete follow-up, joint held-out service, and recovery-gate events. A genuine incomplete measurement instead gives interval rows \(\underline b\leq Aq\leq\overline b\). It is incorrect to construct \(A\) from an unexplained post-treatment subgroup as though all policies had the same customer mix.

For any *fixed complete-history* policy \(\pi\), including a predeclared action after each observable report and a retained specialist fallback, let \(v_{\pi k}\) be its **total** discounted net accepted-service contribution on response type \(k\). Then
\[
  J(\pi;q)=v_\pi^\top q,\quad
  L_{\pi,\sigma}=\min_{q\in{\cal Q}}(v_\pi-v_\sigma)^\top q. \tag{CI2}
\]
This is a sharp linear-programming bound **relative to the response-type set actually admitted**. It compares two counterfactual policies under the SAME \(q\). It does not require independent qualification, fixed customer demand or independently redrawn transfer regimes. For equalities only, compact nonempty \({\cal Q}\) yields the dual certificate
\[
 L_{\pi,\sigma}=\max_{\lambda_0,\lambda}
 \{\lambda_0+\lambda^\top b:\,
 \lambda_0+\lambda^\top A_{\cdot k}\leq v_{\pi k}-v_{\sigma k}\quad\forall k\}. \tag{CI3}
\]
A feasible dual witness gives a transparent *economic lower certificate* in terms of actually observed moments. A missing coupling observable can leave that certificate very weak even when every individual skill marginal is precisely measured.

**Qualification and scope.** When a structural model instead constrains the same latent kernel at multiple histories by products, conditional independence, interference, or invariant customer-response functions, its exact identified set need not be a polytope. The unrestricted response-type polytope is then a **relaxation**, yielding a conservative lower certificate; sharpness holds only relative to CI1, not automatically to that smaller structural model. Conditioning policies on the result of a paid diagnostic changes \(v_{\pi k}\) and its calendar/resource transitions; a diagnostic is *not* an added future data premium.

**Hard resource admissibility.** For each policy and response type with positive probability in **some** \(q\in{\cal Q}\), inspect every actual attempted continuation after its report. If approved remaining operator/recovery capacity is \(B(H)\), require its peak and cumulative exposure to be within \(B(H)\), or a certified preattempt abort/fallback. This is a union-of-possible-support check. Expected recovery below \(B\) is insufficient. An unsafe type cannot be removed merely because it was unseen in finitely many trials. If one allows probabilistic risk limits, that is a different explicitly authorized criterion.

## 3. Exact joint-identification counterexample and economic ranking

Let \(H\) indicate a latent source-to-target alignment regime **persistent within a learning pool**, and let \(D\) be a registered pre-action high-value target customer opportunity class. Both have marginal probability \(1/2\); their dependence is not known. The post-action **orders and acceptable production** differ by route and type. Define \(t=\Pr(H=1,D=1)\); its Fréchet identified interval is \([0,1/2]\). The four complete types have masses \(q=(t,1/2-t,1/2-t,t)\), in the order \((H,D),(H,\neg D),(\neg H,D),(\neg H,\neg D)\).

All four route policies are safely executable by construction with peak operator requirement at most 2 and a usable qualified fallback. Their totals already subtract real costs and count captured customer production once:

| Complete response type | R: routine production/data | G: target grounding | E: changed embodiment | S: qualified specialist |
| --- | ---: | ---: | ---: | ---: |
| H and D | 13 | 7 | 6 | 5 |
| H and not D | 5 | 7 | 6 | 5 |
| L and D | 5 | 9 | 6 | 5 |
| L and not D | 5 | 7 | 6 | 5 |

Interpretation: R preserves 5 units of qualified contribution and in aligned high-opportunity pools enables a further captured order worth 8. G, net of deliberate alignment and foregone production, preserves 7 and additionally qualifies/captures an order worth 2 in misaligned high-opportunity pools. E and S remain competent safe alternatives. This is a *constructed pair of controlled service/order response functions*, not a universal transfer technology or a benchmark-to-dollar conversion. The active customer opportunity \(D\) is measured **before** treatment, but its **realized order and accepted production** still depend on the route.

Consequently
\[
  J_R(t)=5+8t,\qquad J_G(t)=8-2t,\qquad J_E=6,\quad J_S=5,
\]
\[
  L_{R,G}=-3,\quad U_{R,G}=2,\qquad J_R-J_G=10t-3. \tag{CI4}
\]
Both extremes are feasible complete worlds with **identical H and D marginals**; one prefers G, the other R. Adding limitless separate marginal samples does not reveal \(t\). If a valid *joint* audit yields \(t\in[\ell,u]\), the sharp R−G interval becomes \([10\ell-3,10u-3]\). Strict R superiority requires \(\ell>0.3\), and strict G superiority requires \(u<0.3\), against the complete R/G policies in this table. E and S are dominated by G throughout this example, not assumed ineffective in the general theory.

A simple dual witness to \(L_{R,G}=-3\) uses \(\lambda_0=-2\), coefficient 0 on \(\Pr(H)\), and coefficient \(-2\) on \(\Pr(D)\): the affine lower claim \(-2-2D\leq v_R-v_G\) holds **for all four types** and its expectation is \(-3\). The \(t=0\) joint law attains it. That is a fully explicit LP primal/dual proof rather than numerical optimization masquerading as a theorem.

## 4. Robust production, opportunity regret, and the surprising limit of a population diagnostic

Suppose independent opportunities permit ex-ante fractional routing with **no controller-pool interference, fixed resource charges and linearly additive contribution**. Route R on fraction \(x\), G on \(1-x\). Its value is
\[
 J_x(t)=8-3x+(10x-2)t.
\]
The best **maximin captured contribution** equalizes exposure to \(t\): \(x=1/5\) yields \(J_x(t)=37/5=7.4\) for all admissible \(t\); no other mixture of R,G,E,S can beat this because at \(t=3/10\) every pure route yields at most \(37/5\). The best pure maximin is G with floor 7. Thus a feasible fleet mix can substitute for one kind of *population-law uncertainty*.

A different objective produces a different fleet: for regret relative to a clairvoyant route choice at the **same** \(t\),
\[
 \sup_t[\max\{J_R,J_G,J_E,J_S\}-J_x]
 =\max\{3x,\,2(1-x)\}.
\]
The minimax-regret mix is \(x=2/5\), worst regret \(6/5=1.2\), but guaranteed production only 6.8. The maximin \(x=1/5\) instead has worst regret 1.6. These are different, legitimate risk/decision objectives; neither should silently substitute for the other.

**Negative result for information value.** Consider a physically safe, perfectly informative *population audit* revealing \(t\) before route allocation but not revealing each future customer's own latent \(H\). With only an **indivisible pure** investment, worst-case value rises from 7 to \(\min_t\max\{J_R,J_G,J_E,J_S\}=7.4\), giving a maximum robust gross audit value of 0.4. With unrestricted fractional fleet mixing, the robust value was **already 7.4**; the same perfect population audit has **zero incremental maximin guarantee**, although it improves realized choices away from the worst-case \(t=0.3\). Any positive cost makes the oracle audit unattractive on that narrow maximin criterion. This is ordinary zero-sum minimax convexification, not a novel value-of-information theorem, and **not** a statement that diagnostics cannot improve expected/Bayesian value or that learning an *individual* regime before an action is worthless. Indivisibilities, changing demand, interference, diagnostic learning effects and pathwise safety restrictions can restore positive robust value.

## 5. What a safe joint diagnostic would have to observe

The commercially relevant target is \(t=\Pr(H=1,D=1)\), not entropy reduction or a correction count. Suppose a *preauthorized safe*, independently validated diagnostic yields a binary report \(Z\), with sensitivity \(s=\Pr(Z=1\mid H=1,D)\) and false-positive rate \(f=\Pr(Z=1\mid H=0,D)\) **constant across D**, with \(s>f\). If baseline \(\Pr(D)=1/2\), then
\[
 m=\Pr(Z=1,D=1)=\tfrac12 f+(s-f)t,\qquad
 t=\frac{m-f/2}{s-f}. \tag{CI5}
\]
This is an **assumption-laden measurement bridge**, not directly observed H. With externally valid \(s=0.9,f=0.1\), an illustrative simultaneous interval \(m\in[0.34,0.40]\) implies \(t\in[0.3625,0.4375]\), hence a strictly positive R−G difference of at least \(0.625\). A separate valid \(t\in[0.10,0.22]\) would certify G over R by at least \(0.8\). Sensitivity/false-positive uncertainty, site selection, report-dependent recovery, changed body versions or a diagnostic that itself trains the controller widen or invalidate the inversion; they must enter the **same complete law**. The raw report/label rate alone is not certification.

A practical diagnostic must additionally pass the **support test**: if a rare positive-support report path requires recovery 3 while the authorized remaining budget is 2, it is inadmissible regardless of its average cost or statistical accuracy. An approved abort-before-attempt might yield a safe but weaker report and is a *different action*. Safety cannot be established by failing to see the rare tail in a finite dataset.

If \((Z=1,D=1)\) is independently auditable as a Bernoulli event and \(s,f,\Pr(D)\) are truly calibrated, Hoeffding gives a provisional sample error radius \(\sqrt{\log(2/\alpha)/(2n)}\) for its sample mean at confidence \(1-\alpha\). For a *hypothetical* sample mean 0.37 and \(s=.9,f=.1\), R superiority requires the lower bound on \(m\) exceed 0.29. At 95% nominal confidence, a sufficient \(n\geq 289\) meets that specific inequality. This ignores uncertainty in diagnostic calibration, panel clustering, selection and repeat orders; it is **not** a recommended real sample size or proof that such an experiment can be ethically operated.

## 6. Empirical falsification and the December agenda

The smallest informative study is **not** more source logs alone. Register all pre-action customer opportunities (including later zero orders), baseline D, specialist service and approved recovery budgets; hold controller/embodiment lineage and rights fixed. Where safety allows, independently validate Z against held-out target service *and* missing-gate/recovery behavior across D strata. Randomly assigned R/G/E/S independent learning pools and full subsequent customer-order follow-up identify **mean total policy differences** without observing both potential outcomes on the same unit, provided positivity, compliance/ITT definition, stable interference and complete capture; our need for a joint \(t\) is specifically due to the *incomplete marginal evidence/structural model*, not an assertion that experiments must literally observe both potential outputs per customer. A crossover/twin-robot design only supports matched counterfactual restrictions if interference/washout and shared demand truly hold.

Discriminating failure modes: (i) \(s,f\) drift by D, so CI5 is invalid; (ii) R and G change follow-on demand outside the pre-registered D response structure; (iii) real H classification is not safely obtainable; (iv) source data are a free sufficient production byproduct, making deliberate G redundant; (v) customer work is not jointly qualified, or rare recovery exceeds the cap; (vi) independent fleet mixing itself changes learning and order capture. None is concealed by introducing a fixed transfer coefficient.

**Closest prior art and novelty discipline (source metadata/abstract/HTML reviewed 18 November 2026):** DDA (Farboodi, Koh, Xia, arXiv:2606.10127) already has productive data spillovers, planner value and aggregation; Manski, *Econometrica* 72 (2004), doi:10.1111/j.1468-0262.2004.00530.x, studies treatment rules under data; Montiel Olea, Qiu and Stoye, *Decision Theory for Treatment Choice Problems with Partial Identification*, arXiv:2312.17623 (HTML June 2025 revision), explicitly finds maximin welfare may ignore data under partial identification; Khan, Saveski and Ugander, *Off-policy evaluation beyond overlap: partial identification through smoothness*, arXiv:2305.11812, already uses LP bounds under overlap failures and explicit smoothness assumptions. Ordinary LP duality, Fréchet bounds, minimax mixtures and diagnostic inversion are **prior mathematics**. Our contribution candidate is the integrated economic/physical/empirical robotics interface—qualified whole-service production, endogenous customer demand, retention, source acquisition and strict recovery support—not a claim to have invented partial identification or zero-value information.

**Exact next proof/measurement gap:** which validated restrictions on the joint *route-induced order × qualification × peak recovery* response kernel remain after conditioning on actual customer site, controller lineage and approved safe diagnostic? Test a second learning/demand function and an empirically plausible interference model before declaring the CI1 response-type relaxation physically tight. Carry this into the November 22 synthesis and Models A/B accounting review; keep the BEA/BLS numerical production backbone, actual matched service panel, independent review and scientific contribution decision explicitly open. Final target: December 25, 2026 23:59 Eastern.