# Proof ledger — conditional diagnostic calibration and shared-pool production

**18 November 2026.** Companion to [CONDITIONAL_CALIBRATION_AND_POOL_INTERFERENCE.md](CONDITIONAL_CALIBRATION_AND_POOL_INTERFERENCE.md). These are finite, conditional constructions, not empirical robot capabilities, original statistical mathematics or operational safety certification.

## 1. Sharp paired bounds with a D-dependent report kernel

Under \(\Pr(H=1)=\Pr(D=1)=1/2\), pooled sensitivity \(s=.9\), false-positive probability \(f=.1\), and \(m=P(Z=1,D=1)=.34\), the total false-positive *mass* is \(\Pr(H=0,Z=1)=f/2=.05\); false-negative mass \(\Pr(H=1,Z=0)=(1-s)/2=.05\). Decompose
\[
m=t-P(H=1,D=1,Z=0)+P(H=0,D=1,Z=1).
\]
Each error subevent lies in [0,.05], giving \(t\in[.29,.39]\). This is necessary. For sufficiency of **both endpoints** and the full interval under this exact margin set, the chapter's two worlds give feasible nonnegative eight-cell distributions at \(t=.29,.39\), each with the specified \(H,Z\) table and \(D,Z\) table. Their convex mixtures preserve every specified observed moment and continuously span all intermediate t. Thus **sharpness is relative to these margins and the unrestricted 2×2×2 response table**. If a real physical model additionally constrains \(Z\perp D\mid H\), this identified set shrinks; pooled sensitivity alone does not imply that conditional independence.

The chapter's low world has \((P(H,D),P(H,D,Z=1))=((.29,.21,.21,.29),(.29,.16,.05,0))\). The high world has \(((.39,.11,.11,.39),(.34,.11,0,.05))\). Their H-positive Z mass is .45, H-negative Z mass .05, D-positive Z mass .34, and overall Z mass .5. The same synthetic route payoffs \(J_R=5+8t, J_G=8-2t\) yield \(10t-3=-.1\) and \(+.9\), a ranking reversal.

If exact \(s_d=s=.9\), \(f_d=f=.1\) hold in both strata, \(m=.5f+(s-f)t\), so \(t=(.34-.05)/.8=.3625\), and the paired difference becomes +.625. That is the **stronger assumption's** conditional point value, not the result of pooled calibration. If \(m\in[.34,.40]\) instead of a point, unrestricted pooled calibration admits at least the sharp interval union \(t\in[.29,.45]\): for each fixed m, the bounds are \(m-.05\le t\le m+.05\); configurations exist throughout this particular interior range by varying the same endpoint tables. The corresponding paired interval is [-.1,1.5].

## 2. Exact maximin pool-interference threshold

For \(J_\kappa(x,t)=8-3x+(10x-2)t-\kappa x(1-x)\) on \(x\in[0,1]\), \(t\in[0,1/2]\), the worst-case t is 1/2 for \(x\le1/5\), and 0 for \(x\ge1/5\). Hence
\[
 \underline J_\kappa(x)=
 \begin{cases}7+2x-\kappa x(1-x),&x\le1/5,\\
 8-3x-\kappa x(1-x),&x\ge1/5.\end{cases}
\]
For \(\kappa\ge5/2\), on \(0\le x\le.2\), \(2x-\kappa x(1-x)\le0\) since \(1-x\ge.8\). On \(x\ge1/3\), \(8-3x\le7\) and the interference penalty is nonnegative. For \(x\in[.2,1/3]\), the needed \(1-3x\le(5/2)x(1-x)\) is equivalent to \((5x-1)(x-2)\le0\), true in that interval. Thus \(\underline J_\kappa(x)\le7\) for every x. At x=0, \(\underline J_\kappa=7\). With \(\kappa=3\), x=.2 returns \(7.4-3(.16)=6.92\).

At \(\kappa=-3\), the left branch is \(7+5x-3x^2\), strictly increasing for x≤.2, and the right branch is \(8-3x^2\), strictly decreasing for x≥.2. The unique optimum is x=.2 with \(7.4+3(.16)=7.88\). This is a *different pool mechanism*, not a change to observed pure-route payoffs.

## 3. An explicit random-pair mechanism and its limits

In a pair of eligible learning slots assigned R independently with probability x, \(\Pr(RG\text{ or }GR)=2x(1-x)\). A *net conditional per-slot contribution loss* L only when assignments are discordant yields expected loss \(2Lx(1-x)\), setting \(\kappa=2L\). A net gain from newly jointly qualified recipes has \(L<0\). The pair-selection formula is valid only for random independent assignment and a stable conditional L in the population under study; selection on persistent regime, shared operator congestion, interactions across more than two slots, and demand-induced ordering require a full-history pool kernel. No individual controlled intervention proves this quadratic transfer or the sign of L.

## 4. Optional policies and the value of the population audit

At \(\kappa=3\), the physical shared-pool mixtures yield maximin 7 by Proposition 2; pure retained G guarantees 7. Pure R, E and S remain admissible and do not exceed G's guarantee. If isolated mixtures are a permitted *different* action with per-slot incremental resource expense c=.5 when \(0<x<1\), the best independent mixed maximin before that expense is 7.4, so net ≤6.9; hence no optional isolated mix raises the 7 guarantee. Under perfect, free ex-ante revelation of **population t only**, the best pure route chosen with that information returns \(\max(5+8t,8-2t)\), minimized at t=.3 with value 7.4. For each fixed t, \(\kappa>0\) makes shared mixing a convex function of x (maximum at endpoints); costly isolated mixing never beats the best endpoint. Thus the maximal robust gross audit value is \(7.4-7=.4\). With c=0 and access to noninterfering mixing, the old 7.4 maximin hedge returns and the identical oracle has **zero** incremental robust guarantee. This is a feasible-menu counterexample to treating population-information value as inherent in the dataset.

No reduction in optimized value is inferred from *free, optional* availability of source data: the agent may decline new training and retain qualified prior policies. If unavoidable joint training changes the action set, its cost must be modeled as a separate action/resource constraint.

## 5. Identification, safety and prior foundations

Pure R/G assignments have \(x(1-x)=0\) for all \(\kappa\). Thus their full payoff distributions **cannot** identify the interaction parameter absent structural restrictions or actual mixed-pool assignment/accepted-service observations. Pure observation is compatible with \(\kappa=-3,0,3\) and their opposite maximin conclusions. The existing finite response-type LP remains valid as an outer bound if the unit of potential-history assignment is a *whole independent controller pool*, not a robot within a pool with interference; its sharpness still depends on the admitted type set and genuinely observed joint moments.

Known pathwise operator budgets must be enforced before comparing candidate route values. Rejection of an unsafe branch is a feasibility constraint, not an expected cost. See Hudgens–Halloran (2008), JASA 103:832–842, DOI 10.1198/016214508000000292 for **prior** two-stage randomization/interference foundations. Previous source-coupling, Fréchet, robust mixed-strategy and diagnostic calibration foundations remain credited.

## Verification ledger

A reproducible pure-JavaScript synthetic function and results artifact accompany this proof. Its finite-grid assertions check marginal equality, complete event tables, reversal, interference optima, prior independent hedge and conditional oracle values; an independent Python stdlib Fraction calculation was executed for the two endpoints and \(\kappa\in\{0,2.5,3\}\). Grids **do not prove** these propositions. Historical Node CI, clean-checkout replay, independent refereeing and physical/data calibration were not performed.

**Specific unresolved proof/measurement gap:** with controller pools larger than two and route-induced customer mix, characterize restrictions on the full joint qualification/recovery/order kernel that can be safely identified from cluster-assignment trials. The quadratic pair reduction does not extrapolate without measurement or justified higher-order bounds.
