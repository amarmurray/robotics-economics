# Endogenous economic anchors: renewal, backlog, and coefficient drift

24 November 2026 UTC (23 November Eastern) — continuation of [cross-cluster occupancy](CROSS_CLUSTER_OCCUPANCY_CONTRAST.md), within *When Capabilities Become Production*. The purpose is to replace a common-anchor assumption, not assert another universal sign on data value.

## 1. Separate the occupancy of retained production from its conditional economics

Let i index a fixed lawful early program (routine P, grounding G, embodiment E), and let H_i be the joint pre-dispatch history under that program on the original cluster denominator. A_i(h) is a specified feasible retained schedule including a null fallback when its old recipe is infeasible. It is not a promise that the old schedule remains physically available after sunk resources have been used. Write its expected remaining net contribution as a_i(h), and the expected increment from the actually implementable alternative schedule as g_i(h). Both include lawful continuation; no additional data premium. Early contribution/cost c_i is accounted for once. Then J_i=c_i+E_i[a_i+g_i].

Choose any common reference function a*(u) of a common feature u(H_i) and write a_i(h)=a*(u(h))+d_i(h). The exact comparison is

    J_G-J_E = c_G-c_E + <mu_G^u-mu_E^u,a*>
             + E_G d_G-E_E d_E + E_G g_G-E_E g_E.

The first term involving mu is distribution transport, the next is conditional coefficient/recipe drift. Equality of u marginals cancels only the reference part, not d. Conversely, identical conditional anchor functions do not cancel when the pushforwards differ. This identity is a bookkeeping theorem from conditional expectations; it does not require matched latent counterfactuals. If a* is approximate, compare its residual by the coupling argument in the preceding chapter; if |d_i(h)|<=D_i(h), a conservative drift bound is E_G D_G+E_E D_E. For asymmetric drift use lower G and upper E. When g and d depend on the same constrained schedule, one should optimize their **sum** over the same law, not independently combine their attainable extrema and call that sharp.

### Exact finite support certificate

For finite original cluster types, let a joint structural type encode physically admissible potential histories and their fixed lawful policy payoffs, with one shared initial population. Exclude types that violate staffing, timing, buyer budget or rights. Let q be the distribution on this support, Mq=m the available population audit moments (including mass one) and q>=0. For fixed policies, net payoff contrast is v'q. The sharp lower value given this model is min v'q over that polytope; any vector lambda with M'lambda<=v on the admitted types yields the lower certificate lambda'm. This follows simply by multiplication by q; LP duality gives equality for nonempty bounded feasible sets. Interval moments can be incorporated by inequalities and corresponding dual signs. Unsupported types are not zero-filled; add them with conservative payoff bounds or restrict the estimand explicitly. For multiple policies, fix the candidate rule before taking the worst case. Directly observed full-policy net contrast suffices for a fixed decision if the programs can be randomized on the complete interference cluster; it need not identify all counterfactual cells.

A useful special case is the case where retained and upgraded production consume the same released slot. Increasing expected retained renewal can mechanically reduce the mass of upgrade opportunities. A dual certificate should exploit this cross-component restriction, including when both price and renewal occupancy drift. The following exact witness demonstrates the strength of that restriction.

## 2. One released worker, endogenous buyer renewal, and different anchor coefficients

All arms receive 2 units of current accepted contribution before the next slot; early grounding additionally costs 1/2 including curation and opportunity cost. Each arm has an original A customer whose distinct follow-up purchase is authorized by R_i=1. A shared worker is cleared for the next deadline iff W_i=1. The retained qualified A schedule earns 6 additional units only if R_i W_i=1; all costs of that accepted service are already netted. R_i is authorization, not receipt. In this stylized case conditional accepted completion is guaranteed when scheduled with clearance; the general model does not assume this. R_i and W_i are observed before dispatch. Changes in earlier service, validation and backlog can change their joint law; no invariance of R or W under intervention is assumed.

G can instead accept an additional B order paying 4, using exactly the same worker slot. A licensed report H_G makes its upgraded qualification plus B purchase authorization usable when W_G=1. H is defined on cleared slots only; W=0 means not available for the decision, not a measured technical failure. G chooses A when R_G=1 and cleared, else B if cleared and H_G=1; otherwise idle. This is optimal for the specified menu and prices, including the coefficient perturbations below. No simultaneous dispatch. E supplies an independently qualified and staffed B recipe paying 2 at committed cost 7/4, without consuming A's worker. Thus it adds 1/4 to its own retained anchor. E's original A renewal/clearance law may differ from G's.

The same original population has the following *within-arm* audit marginals (these are assumptions/synthetic measurements):
    Pr(R_i=1)=Pr(W_i=1)=3/4 for G,E;
    Pr(W_G=1,H_G=1)=1/2.
Write x=Pr_G(RW), e=Pr_E(RW), z=Pr_G(W(1-R)H). The feasible moment polytope is exactly
    1/2<=x,e<=3/4, 0<=z<=3/4-x.
Proof: Frechet intersection bounds give the first pair. The worker restriction gives the last inequality. Conversely, the G atoms (W,R,H)=(1,1,1),(1,1,0),(1,0,1),(1,0,0),(0,1,unavailable),(0,0,unavailable) have masses
    (1/2-z, x-1/2+z, z, 3/4-x-z, 3/4-x, x-1/2).
E atoms (W,R)=(1,1),(1,0),(0,1),(0,0) have masses
    (e,3/4-e,3/4-e,e-1/2).
These are nonnegative and sum to one on the stated domain. Any pair of such arm marginals can coexist in a common structural law by drawing potential arm-specific shocks jointly (their product is one witness) before assignment. This is not a claim that physical cross-arm outcomes are independent in reality; it establishes attainability in this restricted model. No cross-arm equality of renewal or clearance is imposed. A fixed P arm with x_P=1/2 gives J_P=5 and can be retained as an ex ante option.

Hence
    J_G=3/2+6x+4z,    J_E=9/4+6e,
    J_G-J_E=-3/4+6(x-e)+4z.
The sharp G range is [9/2,6]: its minimum is x=1/2,z=0, maximum x=3/4,z=0, since 6x+4z<=3+2x<=9/2. E ranges [21/4,27/4]. The sharp difference is [-9/4,3/4], realized with respectively (x,e,z)=(1/2,3/4,0),(3/4,1/2,0). Thus equal arm-specific renewal and worker marginals cannot certify common retained-production economics. Indeed the upper endpoint occurs when G serves no B at all: G's superiority there is entirely a retained A joint renewal/clearance advantage net of cost. Labeling all improved returns as B-specific technical transfer would be incorrect.

## 3. A sharper joint certificate with changed coefficients

Permit net A renewal contribution to be 6+delta_G under G and 6+delta_E under E, |delta_G|,|delta_E|<=1/8. Permit B under G to pay 4+delta_B, |delta_B|<=1/4. These are bounds on actual accepted-service contribution conditional on the relevant schedule/event (or constants as in the sharp witness); not on a benchmark. They preserve A-before-B because even the lowest A payoff exceeds the highest B payoff. E's independently staffed B increment remains stipulated. Suppose an original-denominator matched audit establishes
    x-e>=1/8, z>=1/16.
Then the exact contrast becomes
    -3/4+6(x-e)+4z+delta_G*x-delta_E*e+delta_B*z.
A naive separate bound using x,e<=3/4 yields 3/64. But the same cleared worker gives x+z<=3/4, and the audit implies e<=x-1/8. Consequently x+e<=11/8-2z. For any allowed coefficients,
    contrast >= -3/4+6(x-e)-(x+e)/8+(15/4)z
             >= -11/64+4z >= 5/64.
Sharpness: x=11/16,e=9/16,z=1/16 and (delta_G,delta_E,delta_B)=(-1/8,+1/8,-1/4) satisfy the common-law atom constraints and attain 5/64. This proof is for the continuous finite-type moment polytope, not a grid approximation. The stronger bound comes from **conservation of the very same worker slot**, not new technical data or a narrower assumed coefficient range. With multiple simultaneous queues, analogous bounds require an actual schedule feasibility set; adding unrelated marginal extrema is conservative, not necessarily sharp.

At common known prices, the fixed ranking uses a single scalar paid contrast. If one needs to compare across varying common A and B prices without rerunning the audit, the two independent moments x-e and z suffice; if A prices differ by arm, x,e,z separately suffice. These ranks are minimal among linear moment summaries for the indicated price families on the relative interior of the full-dimensional feasible region: a linear summary of lower rank has a nonzero kernel direction in those coordinates, and an arbitrarily small feasible perturbation along it changes at least one price contrast. For a single known price vector the single linear combination is sufficient; no claim that three measurements are necessary for that one decision. If actual prices vary with the state, unweighted counts no longer suffice: measure actual conditional paid contributions or bound their residual on supported joint schedules. If a direct trial observes whole-program net receipts, all these decompositions are optional interpretive tools rather than identification requirements.

## 4. Countermodels and mechanism

A free routine source that reproduces G's complete lawful reports, retained A response, clearance, qualifications and feasible continuation at no incremental prefix cost achieves J_G+1/2, strictly dominating committed G in this witness. Free data access alone does not guarantee that transition. A shared-staff E countermodel supplies the B recipe but not another worker, so E can use B only in cleared A-slack states and pays the same committed investment. Its contribution is 2+6e+2(3/4-e)-7/4=7/4+4e, at most 19/4 < P=5. The old routine option remains available ex ante. In the independent E arm B's fixed 2 is earned from its own new slot; do not simply preserve that payment when staffing changes.

The general insight is that learning's effect on the installed productive base is not a residual nuisance. It changes how scarce resources are used, and may compensate for (or eliminate) the incremental market value of new skills. The same downstream capability may have lower conditional marginal value precisely because earlier learning created more valuable retained production. Model A prices the feasible joint menu; Model B determines its occurrence, resource slack and cash cost. This connects data acquisition and embodiment substitution without treating data as an independent premium.

## 5. Foundations and limits

The finite-support LP, Frechet bounds and conditional expectation identities are standard. As related partial-identification practice, Li, Litvin and Manski (2022), [arXiv:2208.03381](https://arxiv.org/abs/2208.03381), abstract checked 24 November UTC, studies the insufficiency of coarse trial subgroup summaries for conditional response. It is not a claim of identical application or comprehensive prior-art review. DDA Farboodi, Koh and Xia, [arXiv:2606.10127v1](https://arxiv.org/abs/2606.10127v1), abstract rechecked via [RePEc](https://econpapers.repec.org/paper/arxpapers/2606.10127.htm) after direct arXiv access failed; sections 5 and Appendix B are prior foundations per earlier recorded reading, not newly reviewed here. Candidate contribution: joint resource-feasible, policy-induced economic moment and drift certificates for heterogeneous data/embodiment decisions, not an independently novel theorem. No field results, real buyer/worker panel, signed rights, independent staffing validation or numeric official BEA edge claimed. No new official quantitative source route was established in this tranche.

See [evidence](ENDOGENOUS_ANCHOR_DRIFT_EVIDENCE.md), [exact checker](endogenous_anchor_drift_exact.js), [record](endogenous_anchor_drift_results.json), [independent checker](endogenous_anchor_drift_fraction.py), [exercises](ENDOGENOUS_ANCHOR_DRIFT_EXERCISES.md) and [solutions](ENDOGENOUS_ANCHOR_DRIFT_SOLUTIONS.md). Next derive a time-expanded conservation certificate when the retained-versus-upgrade choice itself changes the next period's joint renewal, worker backlog and legally available data; the one-slot bound is insufficient when carrying forward commitments. Retain the same original-order denominator and fixed lawful continuation, and distinguish direct full-policy audit from a reusable price/queue sensitivity basis. November 22 gate OPEN; final December 25 23:59 Eastern unchanged.
