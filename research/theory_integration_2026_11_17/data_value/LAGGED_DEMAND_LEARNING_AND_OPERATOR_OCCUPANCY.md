# Lagged customer demand, productive learning and shared operator occupancy

**22 November 2026 — a continuation of *When Capabilities Become Production*, Models A/B; scientific gate OPEN.** This is the next conditional step after [endogenous original eligible orders and capacity](ENDOGENOUS_OFFER_NETWORK_AND_CAPACITY.md), not a separate topic. The results are finite stochastic-decision and Fréchet-coupling identities, with original mathematical derivations in this robotics economic environment. They are not established theoretical novelty, calibrated robot returns or evidence from authorized physical deployments.

## The common economic object and information structure

At each date a lawful full-network program selects productive original-customer service and incidental data P, deliberate target grounding/teleoperation or simulation D, source mixtures and shared posttraining, physical embodiment E, or retained qualified old R. The history contains the signed original buyer eligible-offer panel **including unserved orders**, paid-and-accepted service outcomes, learner checkpoint and qualification, safe robot/operator/recovery slots, customer relationship and subsequent demand, lawful data provenance/use/retention, curation/compute and manufacturing commitments. Field trajectories, failures/recoveries, teleoperation, simulations, synthetic material and public/pretrained data have distinct intervention-conditional learner kernels. Nothing guarantees positive additive source transfer or even ability to use the old controller if forced retraining changes the physical/legal policy.

For program a and its complete finite-horizon history H_t, the common value is

    J(a) = sup_{pi in lawful feasible policies} E_a[sum_t beta^t (cleared original-buyer receipts_t - every real operations, recovery, learning, training, data and capacity cost_t)] - initial cost(a).

Buyer prices, orders and accepted service may react to the whole connected-network intervention. Training-generated future qualified revenue is already inside J; adding a data-premium term double-counts it. For fixed a, V_t(H)=max_{lawful actions i}{r_t(H,i)+beta E_{K_a(.|H,i)} V_{t+1}(H')} is ordinary dynamic programming, but K_a is the joint order/qualification/operator/rights transition, not a task score.

## Proposition 1 — sharp delayed qualified-offer economic frontier

Consider a paid pilot at date 0 followed by a single date-1 original-buyer dispatch, beta=1. Old A is qualified, B is qualified at date 1 iff the **learned, safe and lawful** indicator Q=1. A and B make original eligible offers with indicators A,B, observed lawfully before dispatch. One operator can complete at most one; v_A >= v_B >= 0 are fixed net accepted-and-cleared service contributions conditional on lawful safe completion. The date-0 net paid contribution is g_a (possibly random). Then **exactly**

    J(a) = E_a[g_a] + v_A Pr_a(A=1)
           + v_B Pr_a(Q=1, B=1, A=0).                              (1)

The last term is NOT q*Pr(B)*(1-Pr(A)) without an additional joint independence assumption. It is the economically saleable intersection of trained and qualified B, an original B buyer offering, and the old high-priority A being absent. With q=Pr(Q), b=Pr(B), a=Pr(A), only these three marginals imply the **sharp** bounds

    L = max(0, q + b - a - 1);
    U = min(q, b, 1-a);
    E[g]+v_A*a+v_B*L <= J <= E[g]+v_A*a+v_B*U.                     (2)

These are identification bounds on a stipulated date-1 model, not confidence intervals, inter-arm causal identification, or blanket bounds on unrestricted infinite-horizon production. If buyer values differ in the other direction, the high-priority menu and intersection formula must be recomputed. If rights or safe recovery are missing, Q must incorporate their actual joint eligibility, not be a benchmark passing label.

**Proof.** For every outcome (Q,A,B), a paid A offer dominates any B offer because v_A >= v_B. Dispatch obtains v_A A+v_B Q B(1-A). Taking expectation proves (1). Let three events be Q, B and not-A. Their intersection is bounded above by the smallest marginal. The union bound on their three complements gives Pr(intersection)>=q+b+(1-a)-2, and nonnegativity gives L. For any three specified event marginals, both endpoints are attainable by feasible joint event tables (align the three events for U, and allocate their complements to cover the probability space as far as possible for L). The accompanying exact finite-table enumeration exhaustively attains both endpoints at every integer marginal triple on a six-atom grid. This is standard multi-event Fréchet geometry; the constructive event argument, not the computation, proves the continuum bound.

The economic observation is **joint learning–market–capacity complementarity**: qualification alone never proves economic transfer, and an additional offer can contribute zero when better-paid A and the shared operator are simultaneously occupied. The event Q,B,not-A is a same-date projection of a lagged causal transition from data production into qualified customer orders and scarce fleet production. Positive value under a fixed trial can be zero for the full optimized network; no generalized sign claim about P versus D versus E follows.

## Two complete causal counterworlds — pilot-created demand and learning

Use an explicitly synthetic two-date full program. Program P runs a genuinely paid original-buyer date-0 pilot with success S~Bernoulli(1/2), collecting a legally reusable field trace and qualifying B iff Q=S. The pilot earns S/4 in cleared contribution and consumes a real fixed 1/8 cost, so expected **net** g_P=0; the receipt is not ignored or counted twice. Under P, the later B original customer offers iff S=1 (a stipulated reputation/order response). The A customer offer follows either of two possible customer-network responses:

- **Staggered response W_stag:** A=1-S, B=S, Q=S. Successful paid pilots produce B orders in windows when A is absent; later optimized paid production is 1 with one operator.
- **Synchronized response W_sync:** A=S, B=S, Q=S. The same successful pilots generate B orders that overlap A; only one is serviced, and later paid production is 1/2.

Program D instead pays 1/16 for deliberately acquired target-specific data, whose B qualification Q~Bernoulli(1/2) is independent of future A and B original buyer offers, each independent Bernoulli(1/2). Retained A is always lawful and qualified. Its complete paid contribution is 1/2+1/8-1/16=9/16. Program E qualifies both buyer recipes with a genuinely independently operable second physical/recovery slot, both original buyer offers have marginal probability 1/2, and pays real embodiment/organizational cost 3/8: J_E=1-3/8=5/8. These are arm-specific feasible recipes, not equivalent training scores.

| Fully hypothetical market-response regime | J(P) | J(D) | J(E) | Optimal program |
|---|---:|---:|---:|---|
| P pilots stagger future offers | 1 | 9/16 | 5/8 | P |
| P pilots synchronize future offers | 1/2 | 9/16 | 5/8 | E |

In each world P and D have the **same** q=1/2 and identical individual A/B offer rates 1/2, and P's own date-0 paid pilot has identical marginal distribution and expected cost. Yet W_stag yields P>E>D while W_sync yields E>D>P. In particular, using only P's per-buyer future order, learner qualification and paid pilot averages leaves J(P) sharp between 1/2 and 1 by (2), straddling E. The differing *conditional customer response to the realized pilot outcome* is essential. These are distinct structural potential-response environments, not observed treatment effects or proof customers causally reorder demand in either direction. The R A controller is still available as an option throughout.

## Proposition 2 — recursive physical occupation can reverse optimal productive learning

At date 1 both A and B have lawful qualified current offers. One slot makes the producer choose either high immediate paid A for 1 or lower paid B for 3/4. Choosing B collects legally usable productive B service data that qualifies a new C recipe for date 2 with indicator Q_C; the C original customer is stipulated to offer precisely when the qualification/performance signal succeeds. Old A has a standing date-2 original buyer offer paying 1; C pays 2, and the higher-paying C is selected if feasible. However B service may leave the **same recovery/operator resource unavailable** at date 2: indicator H=1. Under choosing A now, assume no new C qualification or operator outage and date-2 paid production 1. Let q=Pr(Q_C=1|B chosen), h=Pr(H=1|B chosen), j=Pr(Q_C=1,H=1|B chosen); beta=1. The complete conditional choice difference is exactly

    Q_date1(B)-Q_date1(A)
       = (3/4-1) + [(1-h)+(q-j)-1]
       = -1/4-h+q-j.                                               (3)

**Proof.** If H=1, no date-2 service is possible even using old A; otherwise paid date-2 value is 1+Q_C, because the higher C order replaces A only when C's learned and demanded service is feasible. Therefore E[V2|B]=(1-h)+(q-j); E[V2|A]=1. Combine those complete continuations with immediate net paid receipts. There is no extra reward attached to the dataset.

At q=5/8 and h=1/4, the lawful coupling permits j in [0,1/4]. Equation (3) becomes 1/8-j. When recovery occupation and learning success are disjoint (j=0), selecting **B** is optimal by 1/8. When recovery occupation is concentrated on successful learning outcomes (j=1/4), selecting **A** is optimal by 1/8. Both worlds have the same technical learner success and the same operator downtime marginals; the economically decisive difference is the **shared-learner/recovery joint law**. Under an independently stipulated Q_C,H coupling j=5/32, A barely wins by 1/32. These are exact normalized payoff constructions, not deployment measured magnitudes or real policies.

For general current net receipts r_B,r_A, a standing old-service value v_A and a newly qualified demand-linked C value v_C>=v_A, the corresponding conditional improvement is

    (r_B-r_A) + beta[-v_A*h+(v_C-v_A)(q-j)],                       (4)

provided H is a complete outage, the C original offer is present iff Q_C, and no other future options or costs are suppressed. A second truly independent safe recovery slot changes equation (4); a second body sharing H does not. Conditional inalienable rights or inability to lawfully deploy C must be encoded in Q_C, potentially taking q to zero. With an arbitrary C-demand indicator O_C, replace q-j by Pr(Q_C,O_C,not-H) and retain the original A-demand state rather than imputing from robot successes.

## Why this matters for recursive production and its limits

Equations (1)–(4) put a **time-lagged economically usable transfer mechanism** inside the same optimized production network. Productive B service earns current receipts, generates or fails to generate permissioned source data, transfers to C qualification, changes future original buyer order response, and can consume scarce recovery capacity exactly when future qualified demand appears. This is not the claim that data universally has increasing returns or that every robot business has a reinforcing flywheel. The sign depends on the joint transition, market demand, rights, operator and embodiment architecture; old controllers remain optional only when the old lawful physical policy is still feasible.

Causal selection is critical: logging only selected successfully served B episodes cannot reconstruct Q_C against unserved B opportunities, date-0 buyer pilot counterfactuals, failed and recovered source traces, C orders never offered, or H at the same time as learner updates. Production-generated and deliberate data interventions must be compared as whole original-buyer/learner/operator network programs, ideally with independent connected-network assignment and audited predispatch observation. No robot-level A/B split is valid under shared broadcast or common human rescue. The sharp ranges in (2) and (3) are structural sensitivity envelopes conditional on known true marginals, not statistically estimated from the unavailable panel.

**Closest prior art and bounded audit (checked 22 November 2026):** DDA §5 already values future data in production and its Appendix B treats complementary aggregation; there is no new claim to those effects. Talluri and van Ryzin (2004, https://link.springer.com/book/10.1007/b139000) is prior capacity/revenue management. Standard Markov decision processes, learning-by-doing and partial identification cover the underlying formal machinery. On the **technical** side, *Learning while Deploying: Fleet-Scale Reinforcement Learning for Generalist Robot Policies* (Wang et al., arXiv:2605.00416, posted 1 May 2026, https://arxiv.org/abs/2605.00416) reports continual post-training on a 16-robot dual-arm fleet across eight manipulation tasks; *Learning from Fleet Experience* (Yu et al., arXiv:2610.25736, posted 19 October 2026, https://arxiv.org/abs/2610.25736) reports experience-based shared fleet learning up to 96 robots across five manipulation tasks. Their technical evaluations motivate a feasible learning-feedback channel but **do not** establish our intervention-conditional original-customer orders, cleared payments, legal rights, cross-site operator occupation, or dynamic marginal dollar value. Their reported technical percentages cannot be converted to dollars. This is a limited abstract/accessible-primary-text audit, not source replication or a novelty review.

**Reproducibility and teaching:** [exact standalone model](lagged_demand_operator_exact.js), [matching recorded results](lagged_demand_operator_results.json), [independent Fraction checker](lagged_demand_operator_fraction.py), [unpopulated original-buyer/rights exposure design](LAGGED_DEMAND_OPERATOR_EVIDENCE.md), [exercises](LAGGED_DEMAND_OPERATOR_EXERCISES.md) and [solutions](LAGGED_DEMAND_OPERATOR_SOLUTIONS.md). Main JS exact enumeration covers 1,716 eight-cell distributions on a 6-atom grid, exhausting all 343 marginal strata, and 165 recovery couplings on an 8-atom grid, 4,188 integer assertions. Grid tests complement, not substitute for, the analytic proof.

**Next exact proof/evidence gap:** identify a feasible, lawful multi-site exposure mapping that preserves both order arrivals (including no-orders) and Q/H recovery/learner correlations under an adaptive P/D/E choice; test a **policy-specific transition sensitivity certificate** when complete connected-network causal assignment is unavailable. Do not invent q, h, rights or market response from laboratory benchmarks. Maintain broader multilayer production/value chains, cash allocation, manufacturing, generalist/specialist and contracts rights work without allowing the next run to become finance only. November 22 Models A/B scientific acceptance OPEN; theory majority through December 6; deadline December 25, 2026 at 23:59 America/New_York.
