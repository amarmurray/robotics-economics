# Supported policies and the economic ceiling of unobserved data transfer

**November 21, 2026. Same When Capabilities Become Production / November 22 Models A–B original-buyer SG/E choice; science gate OPEN.** The preceding policy-occupancy theorem required Q-reference history/action support under *both* possibly optimizing P and Q policies to transport pooled learner, robot, operator, buyer and settlement values. That support may be unobtainable. This continuation derives a second, independently checkable route: retain a valid paid-production floor for approved, supported **complete policies** and use a physically and contractually valid full-horizon opportunity ceiling for the rest. It does not turn missing logs into zero error or assume a novel source-trained action is safe.

## Common economic object

For program a in {S,G,SG,E} and optional data coalition A subset {F,T,M}, let Pi(a,A) be the whole class of physically legal nonanticipating strategies. A complete strategy includes qualification and fallback, operator/robot slots, original customer offers and declined orders, settlement and refunds, future learning and production-generated new service, checkpoint lineage, rights and evolving buyer demand. Field successes and failure/recovery, teleoperation and simulation/synthetic inputs are distinct; public/pretrained inputs remain separately indexed. Optimized J(a,A)=sup_pi E[Y(pi)] counts net accepted and finally paid horizon value, including continuation, acquisition, labor and manufacturing costs exactly once. Policies retained by genuinely free optional data access remain available, but forced train mixtures and new resource/rights obligations may reduce value.

For each a,A partition *complete* lawful policies into supported O and unsupported U, with O nonempty. Assume simultaneous valid value intervals l_pi <= V_P(pi) <= u_pi for every pi in O. These may be obtained from original-buyer target paid-program evidence, or an actual program-to-reference comparison with pi-specific full-horizon controlled-kernel occupancy support and its uncertainty. They are NOT task benchmark scores. Assume a defensible **whole-horizon upper bound** C_U on every policy in U (and do not assume an unverified physical action is legal).

## Proposition 1: policy-support envelope

    L(a,A)=sup_(pi in O) l_pi
    <= J_P(a,A)
    <= U(a,A)=max{ sup_(pi in O) u_pi, C_U }.                  (1)

Omit C_U if U is empty. For SG and E independently, strict SG ranking is warranted when L_SG>U_E; strict E ranking when L_E>U_SG. For S,G,SG,E a unique ranking follows when one candidate's L exceeds every alternative's U. The intervals are sharp in a *finite rectangular policy-payoff model* if each independent payoff interval can be attained and all unsupported policies can simultaneously lie no higher than L. In a shared learner/market, joint cross-policy restrictions can make these merely outer bounds.

**Proof.** Every supported strategy is feasible in the full legal menu, hence optimizing over the menu dominates its lower value and the largest lower endpoint. Every feasible strategy belongs to O or U, and is respectively bounded above by its u_pi or by C_U. Taking the supremum proves (1). Endpoint attainability in the stipulated rectangular finite menu is immediate by assigning supported strategy values to their lower/upper endpoints and unsupported values accordingly. No independence of qualification events or additive source effect is required for the *outer* inequalities. This is standard max-of-intervals/partial identification, not a new abstract theorem.

**Connection to preceding occupancy proof.** A pi-specific supported interval can use |V_P(pi)-V_Q(pi)| <= R min{1, Σ_t E_(Q,pi,t) TV(P_t,Q_t)}, plus defensible buyer-market and sampling corrections. That only requires logged support for the selected pi. It does **not** license replacing the actual optimizer's unknown support with the behavior logger's error. All other lawful but uncovered complete policies are bounded separately via C_U. The route becomes useful when signed counterfactual physical limits are stronger than ignorance about transition probabilities.

## Proposition 2: production resource-price upper certificates

Define a full-horizon catalog of original-customer qualified accepted-and-settled service types r and nonnegative delivered intensities x_r. Let v_r bound each capturable paid unit; A_kr its physical and organizational resource consumption, b_k an all-policy horizon capacity, and d_r an upper offered-and-eligible customer volume valid **under any policy-induced demand/price response**. For a complete lawful policy whose cumulative production falls inside those constraints, the optimistic resource relaxation is

    V_P(pi) <= C = max_{x>=0, A x<=b, x<=d} v'x - c_min.       (2)

Here c_min is a valid unavoidable net cost lower bound; uncertain costs are otherwise omitted to maintain an upper bound. The standard dual relaxation yields

    C = min_{lambda>=0, mu>=0, A'lambda+mu>=v}
                 b'lambda+d'mu - c_min                         (3)

when the LP is feasible, bounded and has standard strong duality. **Every dual-feasible price vector** is an independently checkable weak-duality upper certificate (even without an optimum). Integral dispatch only reduces the set and cannot exceed the LP relaxation. This reuses the paper's resource-price certificates, not a second financial data premium.

The catalog and capacities must include potential new E embodiments, dynamic learned services, other buyer markets if legally served, future qualified recipes, operator recovery, manufacturing and data-sharing rights. A one-period bound is not a horizon bound. No source benchmark accuracy, target grounding score or teleoperation label directly determines the v, d or b of actual accepted-and-settled buyer production. If an original buyer can be induced to offer new orders by success, d must bound that response too. If these facts are unverified, C is an *assumption*, not an empirical certificate.

## Counterworld 1: identical supported evidence, opposite all-source investment winners

Illustrative original buyer contribution is normalized in hundredths of an accepted-and-finally-settled service, NOT a dollar estimate. SG has a legal old whole-horizon safe strategy paying 40/100. The E embodiment independently has a supported legal strategy paying 55/100, under its own feasible resources. Every empty, single and paired coalition of field F, licensed teleoperation T and simulation/synthetic M admits only SG safe; hence the observed SG−E contrast is -15/100 in all seven lower coalitions and inclusion-exclusion gives D2=-15/100.

With all F,T,M optionally available, suppose a new SG **complete ex-ante mutually exclusive** risky strategy becomes permissible but is not logged. Its expected complete paid contribution q may lie in [0,80/100]. Then J_SG(full)=max(40/100,q) and

    J_SG(full)-J_E(full) in [-15/100,+25/100].                (4)

At q=0 E wins; at q=.80 SG wins. Both worlds share every observed lower-coalition and safe-only customer outcome and retain old policy optionality. Learning generated a higher-order economic option, not a proved third-order additive technical mechanism. Even infinite safe-only observations do not settle the investment.

Now **suppose**, rather than assert in the field, a signed complete-horizon original-buyer/order and robot/operator capacity restriction can prove q<=50/100 for every lawful risky complete policy. Then (4) tightens to [-15/100,-5/100] and E strictly dominates without executing that risky controller. One simple normalized LP certificate for risky has paid value ceiling 1/unit, settled intensity <=1/2 from a genuinely valid resource cap, demand <=1 and c_min=0. Its primal optimum is .5 and dual witness lambda=1,mu=0, giving .5. E has a *different* certified embodiment capacity; it is not mistakenly constrained by risky SG's cap. This is a **conditional** production ceiling, not a measured robot success rate. If only the ex-ante safe/risky commitment choice is legal, no convex randomization improves max{safe,q}. A finite simultaneous sampling *illustration* with SG safe [39,41]/100, risky upper 50/100 and E [54,56]/100 guarantees E by >=4/100; no such real confidence event was observed.

## Counterworld 2: invalid static caps under adaptation and endogenous production data

The upper cap must cover complete strategies, not first actions. If safe success .40 is followed by a **physically approved second attempt** that, conditional on safe failure, succeeds and settles with probability .50, then expected total paid service probability becomes .40+.60(.50)=.70. Ex-ante max(.40,.50) was not a true ceiling on this contingent policy. Conversely, a second attempt may be disallowed by operating hours, physical safety or paid-service contract; it must not be invented as feasible.

If first-date finally paid production occurs with probability .50 and, conditional on its authorized data, a future second original-buyer service pays with probability .80, two-date expected paid deliveries total .50+.50(.80)=.90. A .50 **first-date** paid cap cannot prove E=.55 dominates this complete policy. The second date uses its own qualified service, opportunity, physical resources, acceptance and cleared settlement; counting the .40 expected second paid service inside J is correct, while adding a separate data premium would double count. If rights prohibit the learning, the transition cannot be assumed. Both examples are synthetic countermodels, not tested robot economics.

## Interpretation and Nov22 Models A/B gate

Model A, with fixed customer cohort and signed qualified production recipes, can sometimes produce real upper prices and floors. Model B, with recursive learner updates, cross-fleet shared model/data, price and order responses, target grounding, physical embodiment changes and scarce operator coordination, needs **all those paths inside the horizon model** for (2) to be valid. This does not dispense with the earlier pooled-versus-isolated network bridge, full-network exposure or high-order source interaction problem. Source coalition second-order extrapolation is still conditional on an economically two-local reference; the direct supported-policy interval is an alternative whose intersection with a correctly established reference-transport interval can tighten the investment decision. An empty intersection falsifies at least one premise.

The discriminating next audit is a complete lawful SG/E policy menu (including adaptation), matched original eligible buyer/order and paid settlement support for each observed policy, and **signed upper demand, service and resource ceilings for the unsupported policies across the future learning horizon**. If neither an E program nor its counterfactual upper envelope is available, no claim of SG superiority follows. This deliberately replaces another marginal-task benchmark run with a falsifiable economic production restriction.

**Closest prior art and scientific status.** This is classical partially identified decision making (Manski, *Partial Identification of Probability Distributions*, 2003, DOI 10.1007/b97478), LP duality, and robust dynamic planning (Iyengar 2005, DOI 10.1287/moor.1040.0129; Nilim and El Ghaoui 2005, DOI 10.1287/opre.1050.0216). Data-Driven Automation §5 and Appendix B already model future data value and complementary aggregation. The integrated **qualified original-buyer accepted-and-paid production** application is a candidate synthesis, not proved independent novelty. [Prospective field evidence](SUPPORT_FRONTIER_EVIDENCE.md), [executed exact synthetic source](support_frontier_paid_value.js), [result](support_frontier_paid_value_results.json), and [separate exercises](SUPPORT_FRONTIER_EXERCISES.md)/[solutions](SUPPORT_FRONTIER_SOLUTIONS.md). No real eligible buyer receipts, signed SG/E study, physical risk/salvage admission, measured q cap, verified learner transfer effect, numeric official BEA/BLS input-output edge, complete CI or independent peer novelty audit were obtained. November 22 acceptance remains **OPEN**, theory majority through December 6, final December 25 2026 23:59 America/New_York unchanged.
