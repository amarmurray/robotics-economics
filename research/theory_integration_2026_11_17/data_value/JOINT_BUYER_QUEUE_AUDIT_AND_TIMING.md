# A decision-sufficient longitudinal audit under a conserved recovery queue

**22 November 2026 — continuation of *When Capabilities Become Production*, Models A/B; scientific gate OPEN.** This is a constructive continuation of [the support-zero common-law theorem](STRUCTURAL_ZERO_COMMON_LAW_AND_AUDIT.md), [sequential audit/positivity result](LONGITUDINAL_AUDIT_AND_POLICY_SUPPORT.md) and [physical multiple-job network](GLOBALLY_COUPLED_MULTI_JOB_PRODUCTION.md). It does **not** treat an independent audit as an alternative to an authorized intervention. All numerical values are invented normalized *accepted-and-paid original-customer production contributions*, **not** robot measurements, observed profits or dollars inferred from a benchmark.

## 1. The precise question

Can a lawfully linked original-buyer/worker report — rather than an exhaustive causal reconstruction — certify when productive source learning P beats licensed target grounding G or an independently staffed embodiment E, when choices are made at *different dates*? Under what conditions does that single report fail because the grounding action has no historical support, the intervention changes customer demand, or the report arrives after the irreversible choice?

This extends, rather than replaces, the exact common-law polytope
\[
\mathcal M=\{\mu\in\Delta(\Omega):A\mu=q,\ C\mu=d\}
\]
from the previous chapter. A complete scenario \(\omega\) encodes **joint potential learner, buyer, physical-queue, settlement, and rights histories** across all *lawful* actions. A deterministic nonanticipative policy \(i\) has net contribution \(f_i^\top\mu\): every period's physically qualified, accepted and paid production is included once, with costs and forgone other services included. The same \(\mu\) prices all P/G/E choices. Forbidden actions are excluded; permitted but historically absent actions remain in the menu with unidentified causal outcomes unless an additional *justified* structural restriction is declared. Nothing in this theorem makes actual robot source data, a teleoperation episode, a simulation rollout, a synthetic trajectory or a pretrained corpus interchangeable.

## 2. General proposition: economic rank sufficiency of an audit

Let \(A\mu=q\) include precisely the actually supportable linked-history observations and physical constraints, and let \(B\mu=b\) denote an additional truthful, rights-permitted audit. For a finite menu of fully specified nonanticipative policies \(i=0,\ldots,m\), let \(v_i=f_i-f_0\).

**Proposition.** If each \(v_i\) belongs to the row span of the stacked matrix \((A;B)\), every policy comparison \(f_i^\top\mu-f_j^\top\mu\) is constant on each nonempty post-audit fiber. In particular, optimizing over policies does not require point-identification of the whole joint physical law. Conversely, when the fiber has relative interior in its affine hull and some \(v_i\) is not orthogonal to the fiber's feasible difference space, that *contrast value* is not point-identified; its **ranking** might nevertheless be invariant if the entire contrast interval has one sign.

**Proof.** The audit's feasible differences \(\delta=\mu-\nu\) satisfy \(A\delta=B\delta=0\). A row-span contrast has \(v_i^\top\delta=0\), and hence all contrasts \(v_i-v_j\) agree for every pair of feasible laws. Conversely any feasible difference with \(v_i^\top\delta\ne0\) changes that contrast; relative interior permits sufficiently small signed perturbations in the feasible direction while keeping nonnegativity. This is an elementary linear identification theorem, not a newly discovered statistical method. For policies whose outcomes are unidentified because the action itself was not attempted, no rows about *old-policy buyer outcomes* can generally span the missing action-specific payoff.

This extends to fully dynamic policy-dependent learning and shared-operator workload because each **fixed** nonanticipative policy has a linear payoff functional on the law of complete potential histories. It emphatically does not assert that a static row-span check on separate datewise marginals suffices; the correct \(\Omega\), legal policy menu, and interference-closed physical constraints must be constructed first.

## 3. A physically conserved, two-window original-buyer example

At date 2 a single robot/worker cluster observes its current recovery backlog \(H\in\{0,1\}\) and an original customer's eligible source-service order \(Y\in\{0,1\}\). When \(H=1\), the worker must complete the inherited job and no extra source dispatch is feasible at date 2; that inherited job clears before date 3. Define the **predispatch** eligible opportunity \(A=1\{H=0,Y=1\}\). The independent date-3 original customer order is \(Z\in\{0,1\}\), not observed before the date-2 dispatch. An existing retained safe controller R for P declines this extra service, leaving the worker free at date 3. A source-qualified productive dispatch T can be taken **only** when \(A=1\), generates a contractually accepted date-2 service worth \(r=3/4\), and causes exactly one recovery job that occupies the shared worker at date 3. Therefore
\[
W_3^R=1,\qquad W_3^T=1-A;\qquad
V_{P,R}=E[Z],\quad V_{P,T}=E[Z]+rE[A]-E[AZ].
\]
There is no concurrent date-3 service in the \(A=T=1\) path, no phantom second worker and no ability to observe \(Z\) before the date-2 commitment. Qualification of T and the \(3/4\) **paid customer contribution** are *stipulated*, not inferred from historical benchmark results. Productive trajectories generated by T may aid later learning, but this deliberately terminal horizon gives them **no unsupported extra data premium**. A longer-lived learner would require a new continuation kernel.

Grounding G reuses rights-cleared existing data to qualify a distinct *date-3 bundled service*, yielding the **same** original \(Z\) service with an additional assumed \(k=1/2\) paid contribution **only when** A also held, at an all-in \(1/32\) qualification/licensing cost. It does not count a second robot-time service; it raises the value of the one accepted date-3 bundle. It does not make a date-2 T dispatch, so that worker is clear. Thus
\[
V_G=E[Z]+kE[AZ]-1/32.
\]
The independent embodiment E has an additional chassis, independent worker, and an independently supported other original-buyer accepted service, stipulated net \(V_E=9/16\). All fractions are **normalized synthetic contributions**, not prices. The old feasible recipe remains optional within P; the comparison does not force costly T learning.

**Demand-invariance and support qualification.** This elementary example imposes **one shared \(Z\) order and one A across P and G**, conditional on fixed demand, safe accepted qualification and contractual paid reward coefficients. Actual source/grounding can change \(Z^P,Z^G\), learner eligibility, reporting, recovery duration and future buyer behavior; then a linked old-policy A,Z audit does **not** identify the whole-program policy contrast. No recorded G-target action is available here to validate \(k\). The example is a conditional face of the full finite-history model, not an inference that these physical or commercial invariances hold.

## 4. Exact pairwise-equivalent common laws and a *single* economic audit moment

Suppose preexisting records reveal all three **pairwise** tables among H,Y,Z, each of the binary pairs being fair and independent. They do not legally or technically link the triple H,Y,Z at the original-buyer/worker episode level. The entire one-parameter family of globally coherent joint laws is
\[
\mu_\tau(h,y,z)=1/8+\tau(-1)^{h+y+z},\quad -1/8\le\tau\le1/8.
\]
Each of the eight scenario masses is nonnegative, and summing over any one bit cancels the \(\tau\) term. In particular \(E[A]=1/4,\ E[Z]=1/2\), while the **missing linked-history moment**
\[
b=E[AZ]=\Pr(H=0,Y=1,Z=1)=1/8+\tau\ \in[0,1/4]
\]
is not fixed by *any* one-variable or pairwise buyer/worker rate. The joint moment is economically decisive because it measures the original late buyer who would be **displaced** by productive source service T, and simultaneously the original bundle whose **value** can be unlocked by grounding G.

For a **known supported** \(r=3/4,k=1/2\) and cost, the exact optimized program values are
\[
P(b)=\tfrac12+[\tfrac3{16}-b]_+,\qquad
G(b)=\tfrac{15}{32}+\tfrac b2,\qquad
E(b)=\tfrac9{16}.
\tag{1}
\]
The optimal P dispatch is T when \(b<3/16\), retained R when \(b>3/16\), with indifference at the boundary. The *investment* ordering changes earlier: **P is uniquely best for \(b<1/8\)**; **E is uniquely best for \(1/8<b<3/16\)**; **G is uniquely best for \(b>3/16\)**. Equalities yield ties. This is an exact three-investment reversal with a single globally valid law, *not* three unrelated arm-specific adverse scenario selections. The exact ranking boundaries are artificial consequences of the stipulated buyer coefficients and should never be extrapolated as robotics-industry thresholds.

**Proof.** Under R, date-3 paid production is \(E[Z]=1/2\). Under T, the conditional period-2 worker-clear opportunity A produces \(rE[A]=3/16\), but blocks date-3 paid Z precisely on AZ, losing b; optimizing retains R when the gain is negative. G has the same date-3 original order and one only-one-slot grounded premium \(b/2\), less \(1/32\) total cost. E is independent. Directly compare (1): \(P>E\iff b<1/8\), and \(G>E\iff b>3/16\); outside those regions the remaining option is below E. Construction of \(\mu_\tau\) for every b proves sharpness over the full pairwise observational class.

A **lawful truthful triple-link audit that identifies b** makes the policy ordering point-identified **conditional on the already supported paid/qualification and demand-invariance coefficients**. It is not necessary to observe every robot state or reconstruct a rich neural transfer kernel for this narrow menu. If A,Z are privacy-prohibited from linkage, the audit is not available; a pairwise collection from another source cannot be silently equated to the missing b.

## 5. When should that information arrive?

The report below reveals the *population-law parameter* b, not the future realized episode's buyer Z. The report is exogenous, licensed, perfectly accurate and free in this illustrative comparison. The planner's stipulated prior places probability 1/3 on each law \(b=0,1/8,1/4\). Three feasible acquisition times differ:

1. **Before program and dispatch commitment:** select P/G/E and, if P, its future nonanticipative R/T policy after seeing b. This produces \((11/16+9/16+19/32)/3=59/96\).
2. **After P/G/E is irreversible but before the date-2 R/T dispatch rule is set:** precommit to one program; a P manager may still tailor R/T to b. The best choice is P, worth \((11/16+9/16+1/2)/3=7/12\).
3. **After both program and R/T rule are irreversible:** b cannot change either choice. The best prior policy is P-T or E, both worth \(9/16\).

Thus the gross perfect-report ceiling of \(5/96\) separates into a **program-timing option of \(1/32\)** and a **remaining dispatch-timing option of \(1/48\)**. The earlier information weakly dominates later information because it leaves all later admissible policies available; the strict gaps here depend on the stipulated prior, known payoffs and *report arrival before the relevant irreversible choice*. A paid audit must subtract its actual cost; if its result affects later connected-cluster learning or buyer demand, its intervention changes the kernel and a simple Blackwell comparison need not apply.

A no-report **maximin** whole-program policy chooses independent E, guaranteeing \(9/16\): the feasible law \(b=1/8\) upper-bounds *every* feasible pure/mixed policy by \(9/16\), and E attains that guarantee for every b. The favorable environment-specific oracle P/G maxima cannot be booked by an uninformed deployer.

## 6. Failure of old-policy audit under a permitted-but-untried grounding action

The preceding exact ranking assumes \(k=1/2\) is a **known, legally supported causal paid-service uplift** of the grounding action. Suppose grounding is permitted but never applied and k is unknown in \([0,1/2]\). Even a completely observed H,Y,Z triple with \(b=1/4\) yields
\[
G=\tfrac12+\tfrac k4-\tfrac1{32}\in[15/32,19/32].
\]
The same *fully audited old customer histories* then permit G to lose to E (\(k=0\)) or beat E (\(k=1/2\)). This is a structural action-support zero, not a data-quality problem. The audit can identify *demand/queue alignment* b while leaving *technical target qualification, conditional paid uplift and induced buyer/operator response under G* uncertain. If grounding violates data rights, G is excluded from the legal menu; no uncertainty bound is an invitation to deploy it.

This separation also holds with genuinely endogenous demand: observing \(Z^R\) does not supply \(Z^G\), and a pilot that changes next-period orders or learner transfer must be evaluated using action-specific potential histories. A negative observed result for one forced training recipe does not violate optional-free-data monotonicity; training cost and service displacement matter for net program comparison.

## 7. Experimental discriminators and broader theory placement

A usable **original-buyer numerator and denominator** is a *full eligible offer/no-offer registry*, including queue-blocked and unserved dates, linked within permissible rights to accepted service recipe, hardware/worker occupancy, report timestamps, controller choice, qualification, cleared payment and costs. The decisive observation is the episode-level cross moment AZ. A mere site-level benchmark, mean downtime, pairwise customer conversion or selected invoices cannot certify it.

This construction also clarifies the full research roadmap: a useful dataset increases the value of **different physically realizable production options**, not necessarily all skills equally. G can win when data-reuse alignment upgrades a late high-value bundle, P when a productive source slot is economically worthwhile despite later shared-recovery displacement, and E when an independent resource uncouples capacity. Downstream industry/value-chain propagation depends on actual qualified buyer demand, input bottlenecks, capability reuse and signed captures; do not convert this synthetic three-arm arithmetic into an interindustry matrix. No official numeric BEA/BLS coefficient was retrieved or estimated in this tranche.

The general finite-history row-span proposition and the timing order are established linear identification/decision-theory constructions. Closest foundations include Manski (2005), *Partial identification with missing data* (https://doi.org/10.1016/j.ijar.2004.10.006); Robins, Hernán & Brumback (2000), sequential treatment/positivity; and Farboodi, Koh & Xia, *Data-Driven Automation* (NBER WP 35320, June 2026, https://www.nber.org/papers/w35320), which already values production-generated future data and discusses aggregation complementarity. **No independent novelty, peer validation, empirical grounding or field deployment is claimed.**

[Prospective evidence and rights design](JOINT_BUYER_QUEUE_AUDIT_EVIDENCE.md), [exact rational replay](JOINT_BUYER_QUEUE_REPLICATION.md), [Python source](policy_audit_fraction.py), [independent integer code](policy_audit_integer.js), recorded outputs and [student exercises](JOINT_BUYER_QUEUE_EXERCISES.md)/[solutions](JOINT_BUYER_QUEUE_SOLUTIONS.md) accompany this theorem.

**Next exact intellectual obligation:** replace the demand-invariant and known-grounding-uplift restriction with an observationally plausible, **policy-dependent multi-date causal process** whose already authorized old action and new G action have different learning, buyer-order and recovery responses, while preserving safety/rights structural zeros and within-fleet interference. Derive *sharp and implementable* whole-program regret/rank bounds under **sequentially selected reports** and no false positivity; choose the smallest rights-feasible set of original-customer and physical-transition measurements that actually narrows those bounds. Obtain no unapproved trial, private data or outreach. Keep the evidence atlas, multilayer production/diffusion, capex/ownership, technical appendix, exercise solutions and first-paper path active. Nov22 science gate OPEN, theory majority through Dec6, Nov29 evidence goal and Dec25 2026, 23:59 Eastern final unchanged.
