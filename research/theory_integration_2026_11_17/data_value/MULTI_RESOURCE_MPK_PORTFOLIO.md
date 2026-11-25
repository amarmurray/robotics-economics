# Marginal productivity of a portfolio of robotic capital
25 November 2026 Eastern · Continuation of [network MPK](NETWORK_MPK_CUT_GEOMETRY.md) and the [economic primitives](ECONOMIC_OBJECTS_AND_ORACLE_GAP.md). No new paper or field estimate.

## Priors: why a robotic production function is not a sum of robot task rates

Embodied capital is rival over time; controller and data capital can be reused subject to rights and compute; coordination and target qualification determine which recipes can make a complete customer service. Unlike a homogeneous service-flow edge, a recipe may require several simultaneous inputs: a mobile platform, an arm, inspection, compute and a downstream buyer's deadline. An extra body is consequently a vector of dated resource increments, not necessarily a scalar increase in one activity. Learning may change the coefficients of a recipe (worker recovery minutes, handoff, failure remediations), admit a new one or change its future evidence lineage. The relevant output is accepted work net of actual variable costs, not intermediate gross activity. Demand for different end-market services prices their competing uses of the same resources. In a social account use final surplus; in a provider account use captured contribution, excluding double counted internal settlements.

Task allocation (Acemoglu–Restrepo), production-network aggregation (Baqaee–Farhi) and DDA's complementary data/forward-looking production (section 5 and appendix B) are antecedents, audited in the preceding chapters. The LP pricing result below is standard finite-dimensional perturbation analysis: see Basu, Martin and Ryan, *Strong Duality and Sensitivity Analysis in Semi-Infinite Linear Programming*, arXiv:1510.07531, abstract (26 October 2015, inspected 25 November 2026, https://arxiv.org/abs/1510.07531). They distinguish finite LP local dual pricing from possible failure in infinite-dimensional problems. We do not claim novelty for strong duality or its sensitivity results. The candidate robomicroeconomic synthesis is that learned, qualified recipe topology determines a **set** of feasible marginal robotic-capital valuations, and that the economically valuable data may change the joint portfolio return with no observable individual robot return.

## 1. Generalized cuts: resource price faces

At a lawful observed history h and fixed learning program g let each column j of A_g be a complete, jointly qualified service recipe's nonnegative dated resource incidence. Include distinct final demand constraints in A_g and b, so substitute recipes for one buyer cannot both collect the same receipt. Let v_g be net contribution by recipe, already deducting actual variable costs, and b strictly positive capacities (including demand). With divisible service, fixed coefficients, nonanticipating admission and nonempty bounded production set, write

    F_g(b)=max {v_g'x : A_g x<=b, x>=0}.
    D_g={p>=0 : A_g'p>=v_g}.
    F_g(b)=min_(p in D_g) p'b.

For finite menus, the pointed polyhedron D_g has finitely many vertices and, at positive b, all minimizers lie on a compact face O_g(b). A resource price here is a supporting certificate, not an observed wage or sale. Each feasible p supplies an upper cut-like plane, with all multi-input bundles priced jointly; ordinary network cuts are a special case. Without a valid graph reduction, do not add stage-level cut capacity as if it priced joint assembly, shared arms or operators. A nonnegative vector d is the net simultaneous increments actually supported by installing an embodiment (demand rows zero). Exact finite **gross** value:

    M_g(b;d)=F_g(b+d)-F_g(b)
            =min_(p in D_g) [(p'b-F_g(b))+p'd].                 (1)

Proof: substitute the LP dual at b+d and subtract F_g(b). All nonoptimal planes carry a nonnegative incumbent gap. If only a finite subset of feasible p is known, its minimum gives an upper bound; an actual feasible complete-service schedule supplies the lower bound. If the optimum at each endpoint is known, any p0 in O_g(b), p1 in O_g(b+d) imply

    p1'd <= M_g(b;d) <= p0'd.                                (2)

Indeed, F_g(b+d)<=p0'(b+d) and F_g(b)<=p1'b. Taking the largest endpoint lower and smallest initial upper is valid; not all independently chosen prices jointly identify the curve. In an integer schedule setting the LP only upper-bounds gross value. Subtracting two LP optima need not bound integer marginal value. Use feasible schedules and the resource-incidence certificate retaining the incumbent relaxation gap; e.g. L_new-U_old <= actual optimized increment <= U_new-L_old. A changed learning regime may change A, v, b or authorization. Evaluate (1) inside each fixed regime with its own D, rather than transporting the old optimal price without the [resource-incidence](RESOURCE_INCIDENCE_TRANSPORT.md) residual/gap test.

## 2. A local aggregation theorem and what individual MPK misses

Let B have columns d_i for the resources installed by each of I distinct body/coordination investments, and z>=0 be an investment direction (physical units; monetary denominators require the appropriate cost vector). At fixed b and g define

    m_g(z)=lim_(t down to 0) [F_g(b+t Bz)-F_g(b)]/t
          =min_(p in O_g(b)) z'B'p.                         (3)

For proof, select the minimum among finitely many dual vertices. Every inactive vertex has strictly positive incumbent gap, so for sufficiently small t the minimizing vertex belongs to the incumbent optimal face. Among that face select the smallest price of Bz. If capacities are positive the optimal face is compact and the minimum attained. Consequently m_g is positively homogeneous and superadditive on the nonnegative investment cone: m_g(z+z')>=m_g(z)+m_g(z'). This is about **local directional** derivatives; it does not assert globally increasing returns in capital or positive finite differences between all classes. Indeed F is concave in capacity and bounded by demand.

Write m_i=min_(p in O_g(b)) p'd_i. Then for every nonnegative portfolio z,

    m_g(z) >= sum_i z_i m_i.

Equality for a given z holds iff there exists a single incumbent optimal dual price minimizing every d_i with z_i>0. Proof: for any p each summand p'd_i-m_i>=0; the minimum of their positively weighted sum vanishes exactly at a common minimizer. The separate scalar MPKs aggregate to all positive portfolios iff this joint minimizer exists for all classes. When it does not, an additive capital index based on individual right derivatives misses the first-order gain from jointly relieving several bottlenecks. The projected dual face B'O is the relevant local sufficient object, not a particular arbitrarily chosen shadow price. This is classical convex LP geometry; economic content lies in which qualified/authorized recipes and dated resources induce that face, and how data shifts it. Portfolio units may be physical or monetary but cannot be mixed.

For finite increments, replace (3) by (1). Even within the same regime finite complementarity can be negative: two parallel one-resource recipes each worth one and sharing final demand three have b=(1,1,3); separately adding one unit to either gives +1, together gives only +1. Current local directions add but the finite portfolio hits the demand plane. Conversely the multi-input example below has strictly positive finite portfolio interaction. Thus the data acquisition question is not whether the technology is universally complementary; it is which feasible portfolio and price faces are reachable under the learning regime, on the relevant demand and capital scale.

## 3. Learning changes the portfolio value without changing any singleton

Two distinct end-market customers A and B pay synthetic net contributions 6 and 4; each has demand one. Both require one robot of class r, one of class s, and in routine program P one shared inspection unit. Incumbent capacities (r,s,inspection)=(1,1,1). Target grounding G supplies an independently qualified B recipe not requiring inspection; the old B recipe is retained. This can be represented by the dominating new column because receipts and all other incidences are identical. The inspection step is not actually removed unless a lawful matched qualification verifies the complete accepted recipe. No other assumptions about technical benchmark success are needed.

| Gross value | P | G |
| --- | ---: | ---: |
| Incumbent | 6 | 6 |
| Add one r only | 6 | 6 |
| Add one s only | 6 | 6 |
| Add one r and one s | 6 | 10 |

In both programs the separate right derivatives along r and s equal zero: the other class alone still caps output. Under P the pair is also blocked by shared inspection. Under G the pair serves both A and B. Locally the G portfolio slope in direction (1,1,0) is 4 until B's demand cap; the P slope is zero. The two separate measures miss that difference entirely. Adding bodies costs 1.5 each; target grounding costs .5. Relative to P at the incumbent, G alone costs .5 without added output; either single body under either program loses money; both bodies under P lose 3; G with the pair earns 4-3-.5=.5. The required complement is not an extra arbitrary data premium, but a real service. If lawful cheaper routine learning P achieves the same inspection release, G loses its distinct advantage. If an independent extra inspection resource costs less than .5 and supports B with both bodies, it may beat G; compare the same menu. No production or cost figures here come from a real company.

This example also demonstrates what a production-network map misses when it stores only each edge's average rate or each robot's independently measured marginal product: the joint resource incidence of a final recipe is a hyperedge-like accounting object. A public industry transaction edge can nominate a value-chain relationship but cannot supply this resource matrix or marginal return. A new embodiment that bundles r and s must be priced with its full net increment, cost, lead time, availability and actual qualifying service.

## 4. Whole-program test and the value of induced data

For complete dynamic Model B, the program and capital stock choose a lawful policy, changing future history, demand and usable source-specific exposure. For each pair (g,k), retain a feasible-policy lower L_g(k) and an upper U_g(k) from a Bellman supersolution valid for every reachable action/history. A stage LP can upper-bound reward or relax action feasibility only if all true feasible actions embed and subsequent transition/rights constraints are respected; never sum independent hindsight stage optima and call it an achievable policy. Then for capital increment d,

    L_g(k+d)-U_g(k) <= V_g(k+d)-V_g(k) <= U_g(k+d)-L_g(k).

For the interaction between G and P, subtract the upper P marginal from the lower G marginal and vice versa. This is a safe bound, not generically sharp with cross-arm dependence. Cost all four programs consistently and separately; if costs enter V already, do not subtract again. The local derivative statement (3) is not valid for changing model, changing price, indivisible investment or general dynamic reoptimization; compare finite policies in those cases.

To distinguish capacity-changing learning from exposure-changing learning, use the earlier two-date decomposition with a supported fixed exposure history: compare the added body on the same lawful checkpoint/data/rights and original demand; then compare independently followed incremental-production histories with retained exposure separated into field, recovery, teleop, simulation, synthetic and pretrained source channels. A frozen-exposure comparison is a diagnostic, not the independently evolving rival. If the same extra robots change the data mixture and future buyer set, there is no transport of a static price-face certificate unless those histories and transitions are represented. The dynamic value already includes future earned output and successor value; do not add an extra data asset premium.

## 5. Empirical discriminator

The matched comparison requires original simultaneously eligible customers, completed and paid service with variable costs and deadlines, the full dated resources and qualification/rights of plausible competing recipes (including unused alternatives), and actual body availability. Record whether r and s increments individually and jointly relax the same constraints, and separately whether the grounding actually changed inspection incidence. The key discriminator is a matched **portfolio** increment at a common checkpoint, plus a full independently evolving program to measure induced exposure and future qualification. If new-body or inspection-release experiments are unsafe/unavailable, independently verify feasible schedules and admissible upper dual planes; give only supported bounds. Distinguish analyst-censored qualifications from unavailable predispatch information. For aggregated end markets, estimate expected feasible terminal service and costs on original catchments; a single expected dual price or average resource matrix cannot generally identify the minimum of jointly varying price faces. See [whole-program validation](COMPACT_WHOLE_PROGRAM_VALIDATION.md).

Official numeric topology: 25 November verification of BEA [I-O interactive landing page](https://www.bea.gov/itable/input-output), last modified 13 November 2026, located the official [industry/commodity and NAICS concordance spreadsheet](https://www.bea.gov/sites/default/files/2023-10/BEA-Industry-and-Commodity-Codes-and-NAICS-Concordance.xlsx). The web reader rejected its XLSX content type and a direct download attempt failed. The [underlying detail interactive route](https://apps.bea.gov/iTable/?Categories=IoUnderlying&isURI=1&reqid=1602&step=6) and [2024 GVC supporting tables](https://apps.bea.gov/iTable/?reqid=157&step=1) expose navigation only in the available reader. Neither numeric cells nor the concordance contents were obtained. Do not claim a join with 2025–35 BLS data or infer resource incidences from these aggregate accounts. Historical official slice remains separate; no new commercial matched panel.

Reproduce with node multi_resource_mpk_portfolio.js. Seeded small LPs use independent primal and dual vertex enumeration with numerical pivot and tolerance checks; 8805 assertions across 400 generated LP configurations plus constructive complement and substitute cases. This is numerical validation of conditional mathematics, not exact rational enumeration, empirical evidence, full CI or independent novelty. The next constructive task is not another isolated portfolio example: connect a jointly observed feasible recipe-incidence matrix, its capacity/price face and lawful independently evolving exposure to the original order validation design. Establish a minimal informative jointly observed audit (or retain nonidentification) for capacity portfolio choice against routine data, deliberate grounding and additional embodiment. December 25 2026 23:59 Eastern unchanged.
