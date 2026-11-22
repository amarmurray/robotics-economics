# Program-dependent buyer demand and joint recovery: the limit of old-policy audits

**22 November 2026 — integrated *When Capabilities Become Production*, Models A/B, scientific gate OPEN.** This chapter continues [the original-buyer/queue audit and information timing](JOINT_BUYER_QUEUE_AUDIT_AND_TIMING.md) without retaining its demand-invariance and known-G-paid-response assumptions. It asks what can be learned about **source-generated productive data P, licensed target grounding G, and an independently resourced embodiment E** when intervention-specific original-buyer orders, qualifications and recovery work all change, G is permitted but historically unattempted, and customer observations are selected by prior policy. This is a **conditional mathematical example, not field robotics evidence or independently established novelty**.

## 1. Complete histories and qualification-constrained production

Consider a connected cluster with a scarce robot and **one** recovery worker, two service dates, an old feasible controller R, and an upfront choice of P/G/E. A globally coherent potential history \(\omega\) specifies, under *each lawful action*, buyer eligibility and actual original orders (including no-orders), target qualification, recovery-job arrival and clearance, accepted service/payment and causal learner transfer. A single \(\mu\) assigns mass to these **cross-action histories**. A nonanticipative policy's net economic contribution is \(V_\pi(\mu)=\mathbb E_\mu[\sum_t \delta^t(\text{cleared customer production}_t-\text{incremental resources}_t)]\). Data's subsequent effect is already in later qualified production; there is no additional continuation-data premium.

For any predispatch eligible episode \(X\in\{0,1\}\), old date-3 buyer order \(Z\), source recovery incident \(J_P\), and grounding-specific target qualification \(Q_G\), original target-bundle order \(D_G\), worker-free indicator \(F_G\), a feasible fixed-menu pair is

\[
V_{P,T}=\mathbb E[(1-X)Z+rX+X(1-J_P)Q_PD_P]-c_P,\tag{1}
\]
\[
V_{G,C}=\mathbb E[(1-X)Z+XF_G\{v_GQ_GD_G+Z(1-Q_GD_G)\}]-c_G.\tag{2}
\]

At date 2 the firm knows \(X\), **not** late \(Z,Q,D,F\). The source T earns actual accepted paid service \(rX\); its learner qualifies \(Q_P\), market response becomes \(D_P\), and a new incident makes the worker unavailable at date 3. Grounding C consumes a lawful source-data/alignment package and a target-calibration dispatch, may produce an incident, and upgrades **one** date-3 service to bundle value \(v_G\) when qualified, demanded and worker-free; otherwise it can fill that **same single slot** with the old original service \(Z\), if free. There is no concurrent phantom second paid service. Both investments have the *option* to select R before incurring program costs; forbidden actions are absent from the menu. E must truly bring separate hardware and recovery resources, not merely a nominal extra model.

The cross-market economic benefit of transfer is therefore not \(Q_G\) or task accuracy alone. Under a **fixed, justified policy and resource table**, it is driven by overlap of qualification, induced buyer demand and the queue-free event, with the outside-service offset as in (2). Report selection and support matter to identifying those intersections.

## 2. General support and sufficiency statement

Let \(\mathcal O\) be the sigma-field of lawfully observed old/P potential histories and any old-policy reporting mask, while G has **zero observed assignment probability**. Let \(\mathcal M\) be a finite convex set of complete-history laws satisfying every justified physical, legal and observational restriction.

**Proposition (support-separation).** If two laws \(\mu_0,\mu_1\in\mathcal M\) have the same restriction to \(\mathcal O\) but different values of a G policy, *no audit measurable only with respect to \(\mathcal O\)*, including a complete audit of old customer orders, point-identifies that G policy or its rank. This is true even if selected old invoices are replaced by unselected complete records. Conversely, for a finite legal policy menu, a lawful **supported intervention-specific** audit identifies pairwise value differences whenever its joint moments span the corresponding complete-history payoff contrasts on the feasible common-law fiber. This is the elementary finite linear identification/row-span criterion from the previous chapter, not a new statistical theorem. An audit of G marginals need not span their economically crucial joint paid-service event.

*Proof.* Every old-audit outcome distribution is a measurable pushforward of \(\mu|_{\mathcal O}\); equal restrictions imply equal audit distributions, while differing \(V_G\) make G unidentifiable. For a supported linked audit represented by \(B\mu=b\), any contrast in the row span of \(A;B\) is constant on the fiber \(\{\mu\geq0:A\mu=a,B\mu=b\}\). Necessity requires appropriate feasible directions, as before. There is **no** positivity extrapolation from old outcomes to a permitted but untried G response; any cross-action restriction must be defended separately.

## 3. Exact physically coherent counterworlds with endogenous demand

Use invented **normalized paid original-customer contributions**. There are independent fair bits \(X,Z,J_P\). Historical R serves the original \(Z\) at date 3 and earns \(V_R=1/2\). On \(X=1\), P makes an accepted source dispatch worth \(r=1/2\), trains a qualified new target recipe \(Q_P=1\), and induces a target original buyer order \(D_P=1\); its recovery job \(J_P\) is fair and prevents late paid service if present. On \(X=0\), R is retained. This is a deliberately strong *synthetic causal* learner/market response, not a claim about real robots:

\[
V_P=\Pr(X=0,Z=1)+\tfrac12\Pr(X=1)+\Pr(X=1,J_P=0)=\tfrac34.
\]

G performs a licensed target-grounding/calibration on \(X=1\), costs \(1/16\) *if chosen*, and produces action-specific \((Q_G,D_G,F_G)\). Its qualified target bundle yields \(v_G=9/2\) in the sole late service slot; otherwise, if the worker is free, old \(Z\) may be served. The G action changes the *composition* of original buyer orders: \(D_G\) is not frozen at old \(Z\), although both have marginal order probability \(1/2\). The G target learner and recovery transition are also endogenous to G. The triple is independent of old \(X,Z,J_P\), **an illustrative but unverified cross-action restriction**.

Suppose, in a deliberately stronger *oracle-information* case, all three G bits and all their **pairwise** tables are individually certified fair and pairwise independent. Such tables are **not** identified by old zero-support logs. The entire conditional G three-bit family is

\[
\Pr_t(Q_G=q,D_G=d,F_G=f)=
\begin{cases}1/4-t,&q+d+f\text{ even},\\t,&q+d+f\text{ odd},\end{cases}
\quad 0\leq t\leq1/4.\tag{3}
\]

All three marginals equal \(1/2\) and all pairwise joint-success probabilities equal \(1/4\), for **every** \(t\). Yet the paid triple-success event is exactly \(\Pr(Q_GD_GF_G=1)=t\). At \(t=0\), G's even-parity support excludes any fully qualified, demanded and worker-free target order. At \(t=1/4\), odd-parity support includes \(111\) with probability \(1/4\). Either law has a real, conserved single worker queue: \(J_G=1-F_G\), with zero or one job at the final service date. P and G potential responses are encoded jointly in the same complete-history law and cannot be selected adversarially using different arm-specific worlds.

The G terminal expected paid contribution when chosen is
\[
\Pr(X=0,Z=1)+\tfrac12\{(9/2)t+(1/2)(1/2-t)\}-1/16
=\boxed{V_{G,C}(t)=5/16+2t}.\tag{4}
\]
The one-slot outside-service term \((1/2)(1/2-t)\) follows because \(Z\) is fair and independent of the G triple. The old policy R is available for free, giving \(V_G^{\mathrm{option}}(t)=\max\{1/2,5/16+2t\}\). A genuinely independent embodiment has stipulated **all-in** contribution \(V_E=23/32\).

**Result (sharp investment ambiguity).** At \(t=0\), \(P=3/4>E=23/32>G^{option}=1/2\). At \(t=1/4\), \(G^{option}=13/16>P=3/4>E=23/32\). More generally G overtakes P **iff \(t>7/32\)**; the entire sharp G-calibration interval is \([5/16,13/16]\), and the optimized optional-G interval is \([1/2,13/16]\). These are sharp under the *stipulated* common-law family (3), since every \(t\) is attained by a nonnegative conserved joint history. They are not market thresholds, estimated transfer parameters or measurable robot ROI.

This rejects the inference “same technical qualification rate, same customer-order rate, and same downtime rate implies same data value.” It also rejects the stronger inference from **every separate G pairwise table**: the unresolved triple overlap can reverse the full investment winner. Crucially, actual zero G action support provides **less**, not more, identification than the already-strong hypothetical oracle pairwise premise.

## 4. Implementable regret, information, and what a lawful audit can do

Suppose the firm does not know \(t\) before the irrevocable date-2 program commitment. P yields \(3/4\) in every world; independent E, old R and optional no-action G are dominated. The maximin **expected paid contribution** chooses P at \(3/4\), despite a favorable G oracle yielding \(13/16\). For an *ex-ante randomized* lawful menu, let \(\lambda\) be probability of G **calibration**, \(1-\lambda\) of P. Its worst regret relative to the environment-specific oracle is
\[
\max\{\lambda(3/4-5/16),(1-\lambda)(13/16-3/4)\}
=\max\{7\lambda/16,(1-\lambda)/16\}.
\]
Thus \(\lambda^*=1/8\) and worst regret \(7/128\); pure P's worst regret is \(1/16\). Randomization is chosen *before* seeing \(t\); this is not a clairvoyant mixed kernel and does not assert permission to run an unapproved experiment. The objective differs from maximin paid production and is stated expressly.

Under an equal prior on the two endpoint laws, a **perfect, lawful precommitment** report of the population regime increases expected optimal value from \(3/4\) to \((3/4+13/16)/2=25/32\), an information ceiling \(1/32\). A report after irreversible choice of P is worth zero here. By contrast, *any* old-R/P buyer/worker audit, including perfect original no-order logging, remains identically distributed at both endpoints, and therefore cannot reveal \(t\): its decision value about G under this constructed model is exactly zero. Observing just the G marginal or pairwise tables also fails; a rights-cleared, jointly linked G learner × buyer-order × worker-transition observation with **actual lawful causal action support** is the discriminating evidence. Without allowed G trials, the correct result is partial identification, not fabricated positivity.

## 5. Limits, competing assumptions, and research integration

Equation (3) is a synthetic coupling designed to falsify a tempting inference, not a claim of universal parity physics. The independence between old R and latent G responses is unverified; genuine cross-arm monotonicity, physical queue-transition restrictions, demand elasticity, learned model interactions and bounds on treatment discordance could narrow the range, but must be evidenced rather than assumed. Larger recovery jobs can carry to more dates and create operator congestion; then complete histories and adaptive Bellman policies replace this terminal example. If G is a purely offline training step without a physical calibration dispatch, \(J_G\) may be structurally zero and the comparison changes. Costly forced training may reduce net contribution while free, safely optional data availability cannot reduce the optimized feasible-policy value if it removes no old option and imposes no hidden resource/rights cost.

**Closest foundations:** Farboodi, Koh and Xia, *Data-Driven Automation* (NBER WP 35320, June 2026, https://www.nber.org/papers/w35320) already formalize endogenous production data and cross-task spillovers; finite Fréchet/partial-identification results (Manski, 2005, https://doi.org/10.1016/j.ijar.2004.10.006), dynamic regime constraints (Sakaguchi, 30 July 2025, https://doi.org/10.3982/QE2288), and positivity-limited longitudinal intervention comparisons (McClean et al., 2024, https://arxiv.org/abs/2410.13522) are relevant prior mathematical and causal foundations. No independent contribution/novelty review was performed; only bounded primary-source metadata was checked on 22 November 2026.

The same theory extends beyond one customer cluster through a qualified production menu, scarce resource-price certificates, complementary service bundles, and multilayer customer and supplier propagation. For an actual robotics opportunity atlas, track each end market's *accepted original-service recipe, eligible offers/no-offers, cleared buyer payment, embodiment and recovery-worker resources, and source-data permissions* before any economic valuation. Endogenous demand under G/P must be measured at the connected-cluster level; a technical benchmark percentage cannot be multiplied by a fabricated dollar price. Production-output and manufacturing input edges, customer-demand response, capital allocation, organizational access and rights remain unresolved full-program dimensions, not displaced by this small example.

[Prospective evidence and support-zero protocol](ENDOGENOUS_PROGRAM_RESPONSE_EVIDENCE.md), [exact replication](ENDOGENOUS_PROGRAM_RESPONSE_REPLICATION.md), [executable integer model](endogenous_response_exact.js), [independent Fraction audit](endogenous_response_fraction.py), [saved results](endogenous_response_results.json), [student exercises](ENDOGENOUS_PROGRAM_RESPONSE_EXERCISES.md) and [separate solutions](ENDOGENOUS_PROGRAM_RESPONSE_SOLUTIONS.md).

**Exact next question.** Can lawful *preintervention* source and site covariates plus independently verified physical conservation and bounded causal-response variation yield a nonvacuous, **implementable** P/G/E regret certificate when G has no historical action support and reporting is selected, without assuming the joint grounded paid event is known? Prove which inequalities survive arbitrary cross-arm dependence; then select a rights-feasible target validation design and pursue a genuine official quantitative production backbone. Do not retroactively call this November 22 scientific acceptance: it remains OPEN. Theory majority through December 6; final deadline December 25, 2026, 23:59 America/New_York.

