# Worker occupancy carryover, shared source broadcasts and economically sufficient cross-site histories

**22 November 2026.** One continuation of *When Capabilities Become Production* (integrated Models A/B), not a new standalone Q-number. **Scientific acceptance OPEN.** This chapter follows [the previous shared-broadcast three-date model](SHARED_BROADCAST_MULTIDATE_POLICY.md). It studies the same source/grounding/embodiment allocation problem when a recovery worker used by learning or production remains busy in a later customer service window. All numerical service returns below are **synthetic conditional expected net original-buyer payments**, never measured robotics economics.

## 1. Full-stack environment and information timing

A lawfully retained source trajectory, failure/recovery or field pilot can produce a common learner checkpoint L. Target grounding/teleoperation, simulation, synthetic and public/pretrained inputs can also affect qualification and demand, but are separate interventions with separate legality, safety and compute/curation cost. Denote by P a source-acquisition and possible productive-pilot program, D a deliberate target-grounding alternative, and E a new embodiment with its own manufacturing and recovery resources. A no-training, retained safe controller R is always available where qualified. No extra value premium is added to complete continuation receipts.

There are dates t=0,1,2,3. At t=0, P generates a checkpoint L; source acquisition costs/rights and receipts are accounted in r0 (set net r0=0 solely in the illustration). At t=1, after L and a lawful report W, the producer may perform a source-informed B pilot if L=1 or retain R. At t=2, it observes **predispatch** safe qualification, eligible original-buyer orders, known contractual expected-net-payment classes and the shared worker's actual availability. It can serve at most one of the two new site orders (or the safe incumbent R) because there is **one robot-time slot**; a target also requires the shared recovery/teleoperation worker. At t=3 the same opportunity reappears, with demand, qualification and worker availability affected by the t=2 action. A distinct E embodiment only creates simultaneous production if it actually adds an independent robot-time and recovery/worker slot.

Write S_t=(S_t1,S_t2) where S_ti=1 requires a signed safe qualification, a genuine eligible predispatch original customer order and an admissible expected-paid contract class at site i. H_t=1 is a busy shared target worker; F_t=1-H_t. Realized customer acceptance, refunds and cleared payment occur **after** the dispatch decision. The weights v_ti(h) are contractual conditional **expectations** estimated from prospective original buyer evidence, not an oracle that reveals eventual receipts. When both sites want the one worker, only one can be served within the stipulated common deadline. The t=0 and t=1 learning actions, t=2 dispatch and t=3 service together form one legal-history policy; there is no separate data-value cash entry.

The general finite-horizon Bellman problem is J_a= sup_(legal pi) E_a[sum_(t=0)^3 beta^t r_t], with the authorized old R policy included in every compatible menu. Its transition kernel K_a jointly maps source checkpoint, buyer responses, learner qualifications, service outcome, worker carryover, rights and future observations. It need not factor as independent technical learning × demand × recovery. The static resource-price and qualification results in the integrated manuscript are operating subproblems, not alternative accounting of this same continuation.

## 2. Exact carryover and learner-feedback identity

For a t=2 legal history h with worker free and a safely ordered new service, compare the permitted target T with old R. Suppose the t=3 operating value is r_3R + d_3 1{F_3=1,S_31 or S_32=1}, with d_3>=0, after observing both eligible orders before dispatch. Define p_a(h)=Pr(F_3=1,(S_31 or S_32)=1 | h, do a), for a in {R,T}. Then

    V_2(h) = r_2R + beta E[V_3 | h,do R]
             + 1{T lawful and safe at h}
               [ (r_2T-r_2R) + beta*d_3 (p_T(h)-p_R(h)) ]_+.       (1)

The first term on the right plus the reference continuation is the paid value of safely retaining R. The positive-part term is an **endogenous economic option**, simultaneously pricing current service and its effect on later qualification, orders and available operator capacity.

**Proof.** Conditional on the lawfully observed h, there are only two legal actions when T is admitted: R and T. Both must be evaluated using their action-specific, full remaining paid return. The date-3 optimal conditional expected receipt is r_3R+d_3 p_a(h) for a at date 2. Subtract the R value from the T value and take the larger. If T is unqualified, has no original order or H_2=1, the target action does not belong to the feasible menu and (1) reduces to R. This is conditional Bellman algebra, not a claim of new MDP theory.

A terminal worker-price certificate cannot determine p_T-p_R from its average utilization or task-success rate. Let q_a=Pr(S_31 or S_32 | h,do a) and j_a=Pr(H_3=1,S_31 or S_32 | h,do a). Then p_a=q_a-j_a, so (1)'s action increment is exactly

    delta_2(h) + beta*d_3 [q_T-q_R-j_T+j_R].                       (2)

A customer-demand qualification gain q_T-q_R can be outweighed by a larger **joint** recovery-occupancy term j_T-j_R. Correlation among two site orders further alters q_a because Pr(S_31 or S_32)=Pr(S_31)+Pr(S_32)-Pr(S_31 S_32). No independence is assumed.

At date 1, pilot B is conditioned on L and lawful W, never on unrevealed future H_2 or orders. In a finite W environment its incremental paid value, relative to R, is

    sum_w Pr(L=1,W=w) [
      (r_1B-r_1R) +
      beta ( E[V_2 | L=1,W=w,do B] - E[V_2 | L=1,W=w,do R] )
    ]_+.                                                          (3)

Equation (3) follows by conditional maximization over the legal pilot choice on each W atom, assuming the same initial state and common old fallback. The date-2 value V_2 already includes date-3 production; adding an independent "data option premium" to (3) would double-count it. Where B changes which reports are available at t=2, each V_2 uses that action's legally available filtration, not clairvoyant cross-arm reports.

## 3. A fully specified four-date counterexample

Normalize beta=1. At date 0, P produces L=1 with probability 1/2. If L=0, no new target is qualified and the old R safely yields 2 at each t=1,2,3: full value 6. With L=1 and date-1 R, the initial receipt is 2; at t=2 the two target eligibility signals are either 00 or 11, equally likely, with H_2=0. At t=2, R is preferable even if both targets order. A t=2 R when the worker is free gives t=3 target eligibility probability 1/2 and a free worker, so its dates 2+3 expected receipts are 2 + (2+2·1/2)=5. Thus the complete post-L date-1 R policy is worth 2+5=7.

With L=1, the alternative B is a safely qualified productive pilot yielding r_1B=7/4 net, versus r_1R=2. It is **not forced**. B changes the t=2 two-site predispatch eligibility pair: the four states 00,10,01,11 each have probability 1/4. Both sites therefore individually have an eligibility rate 1/2, the same as under date-1 R; their **joint** overlap and union differ. Under B, the recovery worker is busy at t=2 with probability 1/2. There is no lawful t=1 signal revealing which of these t=2 states will occur; H_2 and S_2 become visible only immediately before the t=2 dispatch.

For both B worlds, at t=2 old R yields 2 and safely avoids use of the **target-specific** worker. If H_2=0 and t=2 R is selected, t=3 has an eligible new original-buyer service with probability 1/2 and F_3=1; hence t=2+3 expected R-policy value 5. If H_2=1, R runs today while the worker recovers by date 3 with probability 1/2; conditional on recovery a qualified buyer orders with probability 1/2, giving dates 2+3 value 2+[2+2(1/2)(1/2)]=9/2. These are stipulated jointly feasible worker-recovery transitions, not marginal multiplications across unknown field data.

If H_2=0 and exactly one site orders, safely dispatching target T at date 2 earns 9/4 expected paid net; the targeted field episode broadcasts a new checkpoint that creates one eligible date-3 original-buyer service while leaving the recovery worker free. Its dates 2+3 value is 9/4+4=25/4, versus 5 for R; T is selected. If H_2=0 and both sites order simultaneously, the attempted target service leaves the worker occupied at date 3, even though an eligible buyer would exist. Then T would yield 9/4+2=17/4, below the old R path 5, so the optimal controller retains R. Under H_2=1, T is physically inadmissible regardless of its technical qualification. These four outcome rules specify a valid action-conditioned law; accepted/cleared payments are conditional expectations, never observed ahead of dispatch.

Define h=Pr(H_2=1|L=1,do B), s=Pr(exactly one site orders|L=1,do B), and z=Pr(H_2=0, exactly one eligible site|L=1,do B). Exhausting the t=2 predispatch states yields the **exact** optimal B continuation

    C_B = 5 - (1/2)h + (5/4)z.                                   (4)

Therefore the date-1 B-versus-R complete-program difference conditional on L=1 is

    (7/4+C_B) - 7 = -1/4 -(1/2)h +(5/4)z.                        (5)

For the stipulated P checkpoint probability, optimized P value equals

    J_P = 13/2 + (1/2)[-1/4-(1/2)h+(5/4)z]_+.                   (6)

At fixed h=s=1/2, the sharp Fréchet support is 0<=z<=1/2. **This is a genuine occupancy–information interaction, not a new qualification percentage.** The lower bound is achieved when the busy worker coincides with the two singleton orders; the upper bound when it coincides with 00 and 11. The two potential-outcome worlds can be coupled through a single uniform latent U in {00,10,01,11} so both satisfy worker carryover and the same legal t=1 non-observation; no inconsistent arm-specific marginals are selected independently.

- **Diversified recovery:** H_2=1 on U=00 or 11. Then z=1/2, C_B=43/8, B's complete value conditional on L=1 is 57/8 > R's 7 and J_P=105/16.
- **Synchronized recovery:** H_2=1 on U=10 or 01. Then z=0, C_B=19/4, B's complete value conditional on L=1 is 13/2 < R's 7 and J_P=13/2.

Both worlds have identical date-2 B-potential site-specific order/qualification marginals, identical date-2 B-potential two-site joint eligibility distribution, identical mean worker busy rate, identical t=1 receipts, and the same action-conditional date-2-to-3 response rule. Their **optimized future intervention distributions differ**, precisely because the legal adaptive policy responds to the distinct joint histories. Their different cross-date coupling alone determines whether the productive pilot is worth doing. A naive “B always yields better target technical skill” explanation is false. Source availability remains free and optional; the synchronized world simply declines an economically costly/worker-congesting training decision.

As an explicit comparison, stipulated E preserves the old three date R payments of 6 and adds **genuinely independent** embodiment/worker service with gross expected net receipts 9/16 and additional owned-capacity/manufacturing/operator costs 1/32: J_E=209/32. Thus 105/16 > 209/32 > 13/2, so the investment winner switches without changing any site-specific technical success marginal or mean worker utilization. E must not be credited as independent if it borrows the same worker or robot slot. Target grounding D remains in the common action set, but this illustrative P/E comparison does **not** estimate or rule out D; its full legally admissible kernel and costs must be identified before ranking it.

**Sharp conditional identification theorem.** In this finite example, if only h=s=1/2 and the stipulated conditional service/recovery reward schedule are known, the attainable optimized P-value set is the whole interval [13/2,105/16]. Proof: z is bounded by the two-event Fréchet inequalities; the lower/upper above are attained by coherent H_2 assignments to the four equally likely S_2 states, and mixtures of those two joint kernels attain every intermediate z. Equation (6) is continuous, nondecreasing in z, and flat where the optimal pilot remains R. Consequently neither P>E nor E>P is certified by those marginals. If the reward schedule, rights or post-t2 transition is also uncertain, this interval is not a valid unconditional outer bound; uncertainty must be applied to the **complete** lawful kernel.

## 4. What transports, and what does not

A stagewise q_y or s_y certificate transports to an adaptive connected-fleet policy **only** when the conditional law covers all reachable legal histories and action kernels needed by that policy, including worker carryover and customer order/no-offer states, and when the original-buyer conditional payoff and retained R options are kept. The earlier decision-sensitive Bellman-residual theorem remains the general tool: a certificate from a single logged R path or only from separately fitted Q/O/F marginals does not upper-bound every other legal optimizer. This chapter supplies one explicit small network in which the missing joint history matters despite identical per-site qualifications and even identical site-pair order patterns.

One-sided improvement in worker recovery can weakly improve optimized production under a controlled monotone coupling that leaves qualification, customer demand, rights and all other resources fixed and permits an old policy to ignore extra availability. If the worker-recovery intervention also changes which source data reaches the learner, when customers order, or what safely admitted recipes exist, that coupling is no longer established and the monotonicity claim cannot simply be applied. Locally, on a strict B-selected branch in the example, increasing the recovery probability from the H_2=1 state by dmu increases complete P value at rate Pr(L=1) h · 2 Pr(S_3|recovered,R) = h/2, but is zero through the same channel when the optimal date-1 choice is R. This is a policy-occupancy resource value, **not** a universal posted operator wage.

The model is falsified or must be changed if target and R actually share the same worker, the robot-time slot is independent, target orders arrive after dispatch reservation, sequential site orders fit before a deadline, H_2 cannot affect H_3, safe recovery is not approved, after-service payments fail to clear, or E cannot provide physically independent capacity. A better operator queue model would explicitly track arrival time, service duration and next-open slot, not infer a transition from mean busy fractions. The alternative generalist-versus-specialist and source-versus-grounding choice requires actual matched accepted original-buyer service rows, target qualification and training rights before a numerical investment certificate is possible.

## 5. Evidence discrimination and closest foundations

See [prospective evidence protocol](WORKER_CARRYOVER_EVIDENCE.md), [exact executable](worker_carryover_exact.js), [recorded results](worker_carryover_results.json), [independent Python Fraction audit](worker_carryover_fraction.py), [student exercises](WORKER_CARRYOVER_EXERCISES.md) and [separate solutions](WORKER_CARRYOVER_SOLUTIONS.md). Collect **all** original eligible/no-offer windows at both sites, including those not served, timestamped Q and conditional expected payment categories at t=2/t=3, actual post-service acceptance/clearing, L/W lineage and signed cross-site rights, safety/rollback approvals, worker occupancy/recovery and t=1/t=2 randomization at the whole connected-cluster level. Crucial estimand is z under the legal B policy, not “robot learning improved 50%.” An accepted-only episode sample cannot recover z, since H=1 removes exactly the opportunities needed to value learning.

This is conditional MDP/Bellman, finite-event Fréchet and capacity allocation reasoning. [Farboodi–Koh–Xia, *Data-Driven Automation* (June 2026)](https://arxiv.org/abs/2606.10127) already features endogenous heterogeneous production data and complementary spillovers. [Hoque et al., *Fleet-DAgger* (2022)](https://arxiv.org/abs/2206.14349) models limited fleet human-supervisor attention, while [Wang et al., *HECTOR* (April 2026)](https://arxiv.org/abs/2604.10892) considers human-centered dynamic fleet coordination. Those works do **not** independently identify the specific original-buyer cleared-payment and multi-site worker-history responses used here. The candidate *synthesis* is a source-to-qualified-paid-service causal test of worker-congested fleet learning and optional embodiment investment, **not** a proven novel mathematical law.

No original customer paid panel, approved P/D/SG/E physical intervention, signed data rights, independently validated network kernel, original numerical BEA/BLS interindustry coefficient or peer novelty review exists in the available research. The November 22 scientific acceptance gate remains **OPEN**; November 29 evidence strengthening and the December 6 contribution decision remain; final deliverable target is December 25, 2026, 23:59 America/New_York.
