# Q8 — An unloaded case is not a completed order: service-bundle topology and the economics of reuse

**Research date: November 17, 2026.** Input accepted branch at e70be8625d9b3f73b700bddeaa422c68769984d0. **Status:** source-grounded physical-workflow contrast, sharp partial-identification result and exact synthetic economic counterexample. This is not a measured reliability estimate, causal learning-transfer effect, field trial, calibrated return or claimed novel theorem.

## 1. The question and the change in economic unit

Can strong robot case-handling performance on deployed **inbound unloading** establish the commercial value of transferring its experience to **outbound mixed-case picking**? Not without specifying which complete customer service is accepted and the joint reliability of its required components. A technical transfer edge between two task names is not automatically an economic opportunity edge.

For unloading, a physical lift-and-conveyor handoff is one intermediate output. The customer may require further scanning, sortation, receipt acknowledgment and safe flow into storage. For case picking, the robot must locate and identify required SKUs, handle the correct quantities, travel between locations, build a suitable pallet, update warehouse management and meet the dispatch requirement. A correct motion is not necessarily a completed order. These are complementary requirements forming an acceptance hyperedge, not interchangeable pairwise moves.

The current within-platform evidence is unusually useful because it isolates different observation classes without pretending the sites constitute a matched experiment:

- **Operational source:** DHL Group's May 13, 2025 release confirms commercial Stretch unloading in North America since 2023, reports **up to 700 cases/hour**, and discusses integrated conveyor/palletizer operations. Its planned additional units and **case-picking expansion are described in an MOU**, not as a delivered case-pick acceptance panel. [S1]
- **Unloading production links:** Boston Dynamics describes robotic box grasp, placement onto conveyors and multipick release into downstream sorting [S2]. Its named Gap case describes Label Sense to orient cartons for scanners, directly showing why a grasp/placement event is not sufficient for downstream acceptance [S5]. Arvato describes existing separate scanning, pallet building and sortation systems alongside incoming Stretch unloading [S6]. These are vendor/customer descriptions, not independent case-level ledgers.
- **Target design and product:** Boston Dynamics currently markets case-picking functionality, describing mixed-SKU palletized orders and Orbit/WMS integration [S3]. Its product manager describes case selection across multiple locations and WMS order updates [S4]. The inspected product page has no publication date or named DHL accepted-order panel; a current advertised capability does not prove completion of DHL's earlier planned expansion or empirically measured transfer.
- **Outside option:** Dematic describes voice-directed human mixed-case picking and more automated picking/sortation systems as alternatives [S7]. Actual matched-site costs and quality remain unobserved; an alternative must not be assumed unavailable.

The included EVIDENCE.json records source-reported, product-described, marketed, intended and unidentified edges separately. It never converts a case-per-hour claim into accepted outbound orders per hour.

## 2. A sharp partial-identification result

Consider a target order requiring k component success events A_1,...,A_k on the **same target evaluation distribution**. Their marginal probabilities s_i=P(A_i) may be observed, but the complete-service success rate g=P(all A_i) is bounded by

    max(0, sum_i s_i - (k-1)) <= g <= min_i s_i.

**Proof:** the intersection is contained in every event (upper bound). Its failure is the union of individual failures; applying the union bound gives g >= 1-sum_i (1-s_i). These bounds are sharp for suitable joint distributions. For equal 5% failure marginals on three legs, perfectly overlapping failures produce g=.95, disjoint failures produce g=.85, and independent failures produce g=(19/20)^3=6859/8000=.857375. Marginal success .95 does **not** identify whether the whole service succeeds 85% or 95% of the time. This is standard probability theory, not a new theorem.

The distinction is a practical identification problem. Even when the target-specific marginal events are measured, the joint complete-order distribution is not recovered without dependence information. Measurements from *source unloading* are an even weaker basis: they do not necessarily identify the target marginals in the first place.

## 3. Connect accepted service to customer demand and investment

A qualified operator attempts A<=K service bundles; probability g are accepted, giving expected accepted output q=g*A. Let customer final-output revenue evaluated at q be R(q)=a*q-b*q²/2 (b>0), attempted-bundle resource cost c*A, and failed-bundle corrective/manual completion cost h*(A-q). Gross customer-provider operating profit is

    G(A;g)=((a+h)*g-(c+h))*A - b*g²*A²/2.

The optimizing attempt quantity for g>0 is

    A*=min(K,max(0,[(a+h)*g-(c+h)]/(b*g²))).

For g=0 choose A=0. The customer retains an outside alternative worth Pi0. A two-part resource-reimbursement and surplus-capture institution gives the provider rho*max(0,G(A*;g)-Pi0), and the provider may **decline entry** rather than pay fixed qualification investment F. Therefore strict entry requires

    rho*max(0,G(A*;g)-Pi0) > F.

This is a conditional single-provider decision, not an industry equilibrium or supplier bargaining model. R is evaluated at expected quantity rather than E[R(random realized quantity)], so the model is a deterministic fluid approximation; quantity variance and correlated completion across jobs require a correction before interpreting a finite operation. Rework cost h is borne as stipulated and must be contractually verified. No incremental data-value premium is added.

If K binds and participation holds, entry is equivalent to

    (a+h)*K*g - (c+h)*K - b*K²*g²/2 > Pi0+F/rho.

Other branches must use the exact optimizer above.

## 4. Exact synthetic counterexample and falsification

All figures are **normalized, hypothetical inputs**, not robotics benchmark values. Fix a=10, b=2, c=1, h=2, K=4, Pi0=16, rho=1, F=2. For the relevant domain A*=4 and G=48g-12-16g². Entry occurs only when g>(6-sqrt(6))/4, approximately **.88762756**, on the increasing, capacity-binding branch.

- A one-component accepted-handling service with g=.95 yields G=479/25=19.16; net entry advantage is 29/25=1.16, and entry is preferred.
- A three-component target order with every individual marginal success still .95 but independent legs has g=6859/8000=.857375, G=17.39252975 and net entry advantage -0.60747025, so it is not qualified economically.
- Without independence, the same three marginals allow g anywhere in [.85,.95], straddling the entry boundary. Coincident failure events would support entry and disjoint failures would not. Even complete knowledge of the marginal scores and model prices fails to point-identify the investment decision.
- Increasing the target demand intercept from 10 to 12 makes entry attractive at the independent acceptance value without technical improvement. Reducing provider capture to one-half makes entry unattractive even at g=.95. A technical ranking is not a private-value ranking.

**Comparability:** This example equalizes abstract service units to isolate acceptance compounding. Actual unloaded cartons, scanner-accepted received cartons and completed outbound orders have different denominators, marginal costs, customer values and deadlines. Neither the published 700 cases/hour maximum nor any vendor page supplies g, a, K, Pi0, F or rho here.

The exact Fraction-based CPU implementation is workflow.py with 18 passing scoped tests in test_workflow.py. Every case has genuine no-entry, cash/qualification and customer participation alternatives. The floating-point square root is used only for reporting the displayed threshold; other calculations are rational. The tests and source match locally validated Git blob IDs. Historical repository CI and independent review were not run.

## 5. Empirical estimand and minimum dataset

**Estimand:** incremental change in *accepted target orders and target qualification cost* from exposure to a defined, rights-eligible source-unloading dataset, holding the same target acceptance standard and appropriately matching target site, robot configuration/policy, implementation support, order mix, labor alternative and decision date. An experiment varying training-data exposure is preferable; a credible quasi-experimental treatment needs its own assumptions and cannot be inferred from the observed MOU.

A useful observation row includes (site, date, robot hardware, policy/training version, order identifier, required cases and SKUs, all component failure events jointly, completed-pallet correctness/stability, WMS confirmation, deadline, retained human interventions/repair minutes, adaptation/verification labor, support expenses, reuse rights, customer alternative, contract service/fee, payer cash and financing). Capture rejected opportunities as well as funded sites. Separate gross case movements, accepted customer services, actual billable activities and collected receipts. These are not interchangeable.

**Negative control:** a physically handled Gap inbound carton whose label orientation prevents automated scanning demonstrates an acceptance dependency without providing a causal failure-rate estimate. A negative transfer finding would be unchanged target complete-order acceptance and unchanged total target qualification effort despite more successful source case handling. A positive claim requires held-out, matched target improvements or reduced qualification resources plus the commercial connection to attainable paid service.

This is the **workflow/capability** resolution of the production atlas, not the requested numeric BEA sector backbone or an observed supplier-customer-payment panel. Earlier BEA download barriers remain on record; do not rerun the same inaccessible retrieval route without a changed capability. The main paper's novelty remains unselected.

## 6. Next research problem

Connect this acceptance hyperedge to Q7's manufacturer/field/customer-learning choice: the source's case movements affect future value only through observed joint accepted target service, qualification resources, customer demand and rights/contract collection. The next bounded model should choose whether to fund **held-out qualification evidence** for the new workflow versus investing the same budget in established unloading capacity, with fixed target service standards and credible alternative contracts. In parallel seek an event-level workflow dataset; do not generate another scalar-learning toy simply because a coefficient can be changed.

### Primary sources (checked November 17, 2026)

[S1] DHL Group, May 13, 2025: https://group.dhl.com/en/media-relations/press-releases/2025/dhl-group-signs-mou-with-boston-dynamics-and-accelerates-cross-business-automation-strategy.html

[S2] Boston Dynamics, current trailer unloading page; page publication date unavailable: https://bostondynamics.com/solutions/warehouse-automation/trailer-unloading/

[S3] Boston Dynamics, current case picking page; page publication date unavailable: https://bostondynamics.com/solutions/warehouse-automation/case-picking/

[S4] Boston Dynamics product-manager blog, date not established from inspected page: https://bostondynamics.com/blog/taking-mobile-case-handling-beyond-the-container/

[S5] Boston Dynamics, Gap Inc. customer account, date not established: https://bostondynamics.com/case-studies/stretch-helps-gap-inc-deliver-for-its-customers/

[S6] Boston Dynamics, Arvato customer account, date not established: https://bostondynamics.com/case-studies/stretch-improves-safety-and-throughput-for-arvato/

[S7] Dematic, case-picking alternatives, date not established: https://www.dematic.com/en-us/solutions/suite-of-intralogistics-systems/case-pick-systems/
