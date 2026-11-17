# Q5 — Manufacturing experience, supplier pass-through, and embodiment specialization

**November 17, 2026.** Input branch at Q4 `0699815703d758b80f37348a23ada2a2ccc6d430`. Substantive theory, synthetic exact enumeration, and primary-source comparison. **No empirical learning-curve estimate or demonstrated original-paper novelty.** All numerical prices and capacity values are synthetic normalized units. This is a constructive model of the joint customer-demand, manufacturing and heterogeneous-capital decision, not an industrial deployment forecast.

## Economic environment

The upstream production process of robot manufacturing and the downstream *productive service of the robots* are different. Date-zero purchases of generalist G units create manufacturing experience **X=number built**, while date-zero deployment in market A generates separately determined provider cash. This is not teleoperation data, policy training or cumulative robot-hours. At date one the operator can retain cash, expand G in A, qualify G or specialist S for B, purchase tooling that lowers *new* unit costs, or redeploy existing G if separately qualified.

Customer output is endogenous within each market under the continuing benchmark `R_j(q)=a_j q - b_j q²/2`, service cost `c_j q`, and best feasible alternative profit `Π0_j`. With capacity K, `q*=min(K,max(0,(a-c)/b))` and net provider operating profit under an *assumed two-part surplus-share* is `P_j(K)=ρ_j max(0,(a-c)q*-b q*²/2-Π0_j)`. Fixed hourly RaaS, customer liquidity constraints and competitor response are not implied by that assumption.

Let manufacturer real resource costs after X units be `u_e(X)=u_e0-λ_e X` for embodiment e in {G,S}, valid only on a finite positive-cost domain. Deployer invoices after transfer of the savings are `p_e(X)=p_e0-κ λ_e X` with `0≤κ≤1`. **κ is a contractual pass-through assumption**, not a price fitted from a public announcement. The manufacturer retains `(1-κ)λ_e X` extra gross margin per comparable unit under unchanged terms. Consolidated resource value should count a cost reduction **once**; invoice reductions and supplier-resource savings cannot be added as separate net gains.

The operator starts with cash B0 and chooses n0≤2 G units for source A, costing n0 p_G0. Collections are P_A(n0). Date-one available cash is `B1=B0-n0*p_G0+P_A(n0)`. Date-one investments are jointly budget-constrained and include actual new-unit invoices, once-only S design/qualification if any, once-only B customer integration if any, optional tooling, and retained liquidity. Salvage values are terminal *only*, never financing for earlier purchases. A finite exact enumeration checks the allowed portfolio; no multi-firm equilibrium or unbounded dynamic optimum is claimed.

## Conditional threshold: how manufacturing learning changes the profitable embodiment

Take one new B unit, with G accepted-output capacity r_G and S capacity r_S>r_G, same B operating cost c_B and capture share ρ_B. Require both alternatives to be adopted and *capacity binding*, and suppose no other capital use is displaced. With S fixed qualification F_S, invoice salvage share s and common B integration cost (which cancels), S is preferred when

`ρ_B[(a_B-c_B)(r_S-r_G) - b_B(r_S²-r_G²)/2] > (1-s)[p_S(X)-p_G(X)] + F_S.`

Thus the interior demand-intercept boundary is

`a_B*(X) = c_B + b_B(r_S+r_G)/2 + { (1-s)[p_S0-p_G0 - κ(λ_S-λ_G)X]+F_S }/[ρ_B(r_S-r_G)]`.

Its derivative is `da_B*/dX=-(1-s)κ(λ_S-λ_G)/[ρ_B(r_S-r_G)]`. **More generalist manufacturing experience can move specialized entry closer or farther away** depending on directed cross-embodiment cost learning, the contract's pass-through and the productive capacity difference. This is a conditional comparative static, not a general claim that learning favors humanoids or specialization. Absent pass-through, the manufacturer's resource-cost improvement may not change the deployer's invoice hurdle. If capital binds, an additional funding condition must be checked. If demand saturates below either capacity or participation fails, use the full piecewise model; this threshold does not apply.

In an illustrative exact comparison `c=3,b=2,ρ=4/5,r_G=1,r_S=2,F_S=2,p_G0=6,p_S0=9,s=0`, the threshold without learning is `49/4=12.25`. After X=2 generalist builds and full pass-through with `λ_S=2,λ_G=1`, the threshold falls to `39/4=9.75`; without pass-through it remains 12.25; with specialist transfer `λ_S=1/2` it rises to `27/2=13.5`. Exact operating-profit comparisons at adjacent demand points are checked by the attached tests.

## Separating financeability from private value

One synthetic test sets `B0=18,p_G0=6,p_S0=9,` and new-S design+integration costs 4. Two G source units cost 12 and return P_A(2)=24/5 of date-zero receipts, so date-one cash is `B1=54/5=10.8`. The source deployment is **current-period net negative**, and generates X=2 manufacturer experience. A specialized S unit serving attractive market B returns `P_B(2)=124/5` and can instead be purchased directly at total initial cost 13, generating direct private value `59/5=11.8`.

After manufacturing experience the S unit's invoice is `9-4κ`, so the source-first S entry requires `13-4κ` cash at date one. The date-one **funding** condition is `κ≥11/20=.55`. Given the same subsequent S deployment, the source-first **private-value** difference over direct purchase is `4κ-12/5`, so its strict value condition is `κ>3/5=.60`. These are not interchangeable thresholds. In the full finite portfolio, κ=1 chooses initial G=2 followed by specialized B entry, with net value `67/5=13.4`; κ=0 instead chooses direct S entry, net value `59/5=11.8`. Disabling physical manufacturing learning or weakening the target customer demand also removes the source-first choice. The exact tests check affordability, tie-breaks, customer adoption and accounting conservation. With optional G redeployment the ranking can change again: eligibility, support, site-specific qualification and retained A business must be observed, not assumed away.

**Distinguish learning stocks.** Manufacturing experience X, control-policy learning, teleoperation/simulation evidence, delivery/qualification experience and customer-access knowledge are separate. Supplier manufacturing scale, supplier real input cost, invoice prices, supported machine supply and economically penetrated robot service are also separate outcomes.

## Actual source relationships, and what they cannot identify

- **M1, Apptronik–Jabil, February 25, 2025:** announced manufacturing collaboration and pilot internal production tasks (sorting, kitting, line delivery and assembly-adjacent work). [Issuer release](https://apptronik.com/news-collection/apptronik-and-jabil-collaborate-to-scale-production). No project-specific realized supplier unit cost, invoice pass-through or qualified output ratio was supplied.
- **M2, Agility RoboFab, September 18, 2023:** announced a factory in Oregon with *planned/nameplate* >10,000 Digit units/year capability; not realized cumulative builds. [Issuer release](https://www.agilityrobotics.com/content/opening-robofab-worlds-first-factory-for-humanoid-robots).
- **M3, IFR, September 24, 2026:** reported >600,000 industrial robot installations globally in 2025 and nearly 38,500 in the US; neither measures humanoid OEM production learning. [Industry association](https://ifr.org/ifr-press-releases/news/five-million-robots-now-operate-in-factories-globally).
- **M4, Apptronik Elevate, June 24, 2025:** announced specialized industrial automation beyond humanoid morphology. [Issuer release](https://apptronik.com/news-collection/apptronik-announces-creation-of-elevate-robotics). A diversification decision is not evidence of successful transfer.
- **M5, Gray–Tomlin–Roth (2009):** *Outsourcing to a Powerful Contract Manufacturer: The Effect of Learning-by-Doing*. Published abstract inspected; dynamic contract-manufacturer learning and make/buy choice are prior art. [DOI](https://doi.org/10.1111/j.1937-5956.2009.01024.x).
- **M6, Balasubramanian–Lieberman (2011):** learning by doing and industry concentration already analyzed; only published abstract inspected. [DOI](https://doi.org/10.1111/j.1467-6451.2011.00450.x).

The public observations do **not** estimate κ, λ_G, λ_S, their relative magnitude, design/qualification F_S, or actual profitability. No research-policy paper evidence is repurposed as manufacturing-cost evidence. The adjoining source/evidence ledger in the downloadable full package is explicit about null effects and unmatched relationships.

**Falsifiable empirical design:** match manufacturer × shared component family × product generation × actual completed production cohort × purchasing contract, with real BOM, yields, factory utilization, design changes, resource costs, invoices and pass-through covenants; join to task-specific supported output and target customer demand under the same acceptance requirements. Test relative realized invoice changes `p_S-p_G`, and whether those change qualified—not merely proposed—deployment selection, controlling for current build scale and concurrent redesign. Manufacturer experience must be separated from policy and field-operations data. Without such data, treat every coefficient as unidentified.

**Paper relevance and next question.** This supports the broader paper's thesis that production, learning and payment links need distinct network edges. The fact that manufacturer learning affects specialization is not itself novel. Next attempt a joint comparison of manufacturing know-how, target-useful operating experience and contractual cash rights in a matched B workflow; seek a mechanism-specific identification restriction rather than adding another generic learning stock.
