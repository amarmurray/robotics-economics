# Capability combinations and the boundary of the firm

Theory checkpoint 2. Jun Chen, Matthew Elliott and Andrew Koh, *Capability accumulation and conglomeratization in the information age*, **Journal of Economic Theory 210 (2023), 105647**, DOI [10.1016/j.jet.2023.105647](https://doi.org/10.1016/j.jet.2023.105647). Published version, available online March 31, 2023, retrieved November 16 UTC, 2026 from the [Cambridge repository](https://www.repository.cam.ac.uk/items/a6f02629-4e08-41ef-8212-1e771d928069). [PDF](https://www.repository.cam.ac.uk/bitstreams/3606d0ae-9ee7-498e-a357-2ee9fbc38683/download), SHA-256 `d25c0f9e40675c717f774726ff2f54cff5880335bad84be92848ab04963763be`. The published PDF identifies CC BY licensing; no affiliation or endorsement of this research is inferred.

## Mechanism card

**Question.** When do overlapping markets' demands for capabilities support larger conglomerates?

**Primitives.** A finite capability set A; firms hold disjoint subsets F_i in the baseline, with unassigned capabilities S. Each market j values a subset M_j, and relevant firm capabilities are `theta_ij=F_i intersect M_j`. Firm and market hypergraphs have the same capability nodes but different edges. A market edge is **a set of capabilities valued in competition**, not an automatic all-or-nothing physical-service requirement.

**Agents, timing and information.** First-stage firms can procure unassigned capabilities, enter, merge or demerge/dispose. Second-stage firms compete in quantities, with capabilities fixed and known. Market-specific costs decrease strictly as the relevant capability set expands. No-capability cost is at least the demand intercept, so a firm needs a relevant capability to profitably enter. Demand restrictions give unique Cournot equilibrium. Firms pay increasing, strictly discretely convex maintenance cost kappa of the number of capabilities held, with kappa(0)=0.

**Solution concept.** Stable industry structures admit no strictly jointly net-profitable procurement, demerger, merger or entry. This is not the same as a single provider's intertemporal allocation or the replacement-stable equilibrium of *Organizing Intelligence*. The inspected baseline evaluates profitability of deviations; it does not impose our dated payer-specific qualification budgets.

**Assumptions doing the work.** Disjoint capabilities (relaxed later in the paper); market overlap and cost advantages; freedom to demerge; increasing convex maintenance costs. “Valued capabilities” and the stronger “complementary capabilities” condition are extra restrictions for some results, not maintained throughout. The latter requires combined gross profit after a merger to be at least the sum before, with a stated strictness condition. The authors explicitly note that ordinary Cournot mergers need not be profitable, so this is substantive, not implied by a hypergraph picture.

**Reading boundary.** Inspected §§2–2.5, Lemma 1 and Proposition 1, and §3.1's proof discussion (printed pp. 6–15). Reconstructed Proposition 1(i)'s upper-bound mechanism below. Lower bounds, random-network thresholds and later extensions are not independently replicated.

## Reconstructing the upper bound

The source's Proposition 1(i) states that in any stable industry structure the largest firm's capability count is at most the size of the largest connected component of the market hypergraph. The paper proves this using Lemma 1: unused/redundant capabilities can be disposed of, and a disconnected induced graph of the markets in which a firm makes positive profits admits a weakly gross-profitable demerger. Convex maintenance costs make the corresponding net gain strict.

A direct reconstruction of the component argument is instructive. Suppose a firm spans two different **global market components** with r and s capabilities. No market values capabilities from both components. Split the firm along those boundaries. Within each market its relevant capability set and its rivals are unchanged; the other component's new firm has no relevant capabilities there and cannot profitably produce. Hence the original gross-profit total can be preserved. Strictly increasing discrete increments of kappa imply

`kappa(r+s)-kappa(r) = sum_(h=1)^s [kappa(r+h)-kappa(r+h-1)] > kappa(s)-kappa(0)`

for positive r,s. Therefore `kappa(r+s)>kappa(r)+kappa(s)`, so the split raises net profit. A stable firm cannot span components, which implies the upper bound. This reconstructs the upper-bound logic under the baseline's freedom to split and absence of cross-component benefits/costs outside the stated profit function. It is not a proof of the proposition's tightness or uniqueness clauses.

**Changed assumption.** If a split removes a shared financing arrangement and blocks an otherwise profitable investment, preserving gross operating technology need not preserve attainable continuation profits. Alternatively, a separate-firm contract may retain exactly that financing arrangement. Neither a learning edge nor a common balance sheet alone establishes a reason for legal integration. A dynamic extension must specify which rights, funding transfers and obligations survive a split.

## Prior-art consequence for this program

Capability/market hypergraphs, recombination and organizational bounds are already central to this paper. They cannot be claimed as our invention. Physical joint qualification is also not automatically the same as its cost-reducing market-relevance set: an unqualified sensor/actuator pair may produce no accepted service until both are ready, whereas a relevant subset can compete in the source model.

The next [joint qualification and payment model](qualification_finance.md) explicitly separates (i) an all-required service bundle, (ii) who must fund each prerequisite, and (iii) permitted transfers before service begins. It derives a standard network-flow feasibility characterization and an exact deployment comparison. The flow theorem itself is established mathematics, and the comparison remains a diagnostic rather than a verified original contribution. Its value is identifying the **funding cut** an empirical case must measure, and preventing an unsupported inference from shared technology to shared ownership.
