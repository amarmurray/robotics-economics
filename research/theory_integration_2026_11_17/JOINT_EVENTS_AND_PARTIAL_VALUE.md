# Joint qualification and intermediate productive states

**Continuation of *When Capabilities Become Production*, November 17, 2026.** This is an integrated proof/empirical section, not a separate Q-numbered paper or a claim of scientific novelty. The earlier independent-edge and terminal-only chain results remain valid under their assumptions; this section removes two of those assumptions. All rates and returns in the numerical example are explicitly **synthetic normalized units**.

## 1. Economically meaningful states and acquisition technologies

Let E be a finite, **typed** set of not-yet-qualified complete-service capabilities. State S ⊆ E records persistent successful qualifications. The current customer/contract state θ is fixed in this tranche. The terminal operating contribution f_θ(S) is the **optimized incremental economic value** of the best qualified accepted-service arrangement compared with the feasible incumbent alternative, evaluated consistently for one payer or for expressly declared joint surplus. Assume f_θ is bounded, nonnegative, and monotone: retaining optional qualifications cannot remove the incumbent policy. Intermediate states may already support accepted production. This differs from assuming a reward only when the entire qualification program is complete.

Acquisition program j is an admissible effort allocation with intensity λ_j > 0 and a **single** observed successful event that adds a specified set A_j ⊆ E: S → S ∪ A_j. One active program occupies one unit of effort capacity, successful qualifications are retained, and effort costs one cash unit per unit exerted. The operator may stop and collect f_θ(S), or spend at most b units of pathwise available cash/effort. A joint A_j is a genuine possible bundled qualification outcome (for example a verified full-stack upgrade), **not** two artificially independent skill labels. There is no production during a learning interval, no changing calendar demand, no loan, and no credit for unsold robot motions. The model does not infer event hazards from vendor press releases.

**Proposition A (finite-state investment equation).** Let H_S(b) be the maximum expected retained operating contribution at stopping minus actual paid acquisition effort, starting in S with remaining effort/cash capacity b. Then H_S(0)=f(S) and

\[
H'_S(b)=\left[\max_{j:S\cup A_j\neq S}\left\{\lambda_j\big(H_{S\cup A_j}(b)-H_S(b)\big)-1\right\}\right]_+,
\quad [x]_+ =\max(0,x),
\tag{A1}
\]

with H_E(b)=f(E) when E is fully qualified. The maximum over an empty program set has nonpositive continuation value and gives derivative zero. The solution is unique, bounded, and nondecreasing in b. Optimal behavior at each state/budget chooses a program attaining the positive maximum or stops if no such program exists.

**Derivation and verification.** Over a small active effort interval h, a program succeeds with probability λ_j h+o(h) and otherwise leaves S unchanged. Dynamic programming yields H_S(b+h)=max\{f(S), H_S(b)+h[λ_j(H_{S∪A_j}(b)−H_S(b))−1]+o(h)\}, giving (A1) where differentiable; the no-investment region is captured by the positive part. Because every nontrivial transition strictly enlarges S, solve the system backward over subset inclusion. Each resulting scalar ODE has a globally Lipschitz right-hand side with the already solved successor states and continuous initial value, so the value is unique. For verification, subtract accrued effort cost from the candidate continuation value along any controlled jump path: the dynamic equation makes the stopped process a supermartingale, with zero drift under a maximizing active program, and the terminal reward f(S) at stopping. Optional stopping on bounded effort yields the upper bound and the attaining policy. This is a standard controlled jump-process/Bellman argument; it is not a new general stochastic control theorem.

**Immediate investment corollary.** At b ↓ 0,

\[
H'_S(0+)=\left[\max_j\lambda_j\big(f(S\cup A_j)-f(S)\big)-1\right]_+.
\tag{A2}
\]

If this maximum is strictly positive, arbitrarily small available funding can be put to positive expected net use. If all program expressions are strictly negative, a nontrivial near-zero **stopping interval** exists, even though a valuable multi-step program may justify investment at a larger budget. The equality case is delicate: later gains can make the value grow at higher order and must not be declared a stopping interval by inspecting only the derivative. In particular, an individually concave learning technology need not imply an immediate economic benefit when the first successful state is unproductive.

For unlimited cash and no discount/demand expiry, memorylessness and the optional stop imply

\[
H_S(\infty)=\max\left\{f(S),\max_{j:S\cup A_j\ne S}\left[H_{S\cup A_j}(\infty)-1/\lambda_j\right]\right\}.
\tag{A3}
\]

This is valid because a chosen program reaches its successor almost surely with mean cost 1/λ_j and may be reconsidered after each observed success. It is **not** a claim that the same action is optimal for all finite funding levels or under time-decaying demand.

## 2. The structural order counts successful acquisition **events**, not labels

Define the productive event distance m(S) as the minimum number of admissible positive-rate success events along a path from S to a state T with f(T)>f(S), with m=∞ if none exists. With finite program sets, bounded intensities 0<λ_j≤Λ, a free option to stop, and gross reward (acquisition cost set to zero), optimal expected incremental contribution with maximum effort b is Θ(b^{m(S)}) for finite m(S) as b↓0. This is **not** a net-value asymptotic with paid effort.

**Upper bound:** positive increment requires at least m(S) actual qualification events. Under any adaptive policy the aggregate success intensity cannot exceed Λ per unit effort, so the count is stochastically dominated by Pois(Λb); bounded f yields O(b^m). **Lower bound:** choose one admissible m-event path with positive rates and follow it, switching programs after each success. The probability of realizing all m jumps within b is (∏_r λ_r)b^m/m! + O(b^{m+1}), by integrating the exponential waiting-time density over a simplex; the terminal gain is positive. Therefore the order is exactly m. This extends the earlier independent single-edge counting argument to **actual action-induced joint events**. It does not validate recoding one qualification as several fictional independent ones. If shared development changes two truly distinct qualified recipes in one observable event, it can reduce the economic order from two to one.

Partial productive states also change the order. If f({A})>f(∅), acquiring A alone yields first-order gross gain even if the full multi-service opportunity needs {A,B}. Consequently m is relative to the customer/contract state and competent alternative—not just to model size or how many advertised tasks exist.

## 3. A robust reversal in which the preferred learning program depends on available funding

Let E={A,B}. Qualification A delivers a complete, paid unloading service; B denotes a separate integration/order-acceptance capability, with no incremental final service without the physical qualification A. A+B unlock the additional complete-order workflow. For a **hypothetical** site, let f(∅)=0, f(A)=v, f(B)=0, f(A+B)=W≥v. Two independent targeted programs qualify one missing item each at intensity a. A joint full-stack program qualifies both together at intensity μ. Each program costs one unit per unit of actual effort. The customer outside option and the net value of fully accepted service are already reflected in f.

**Proposition B (short-budget targeted learning, long-budget joint learning).** Suppose

\[
 av>\mu W>1,\qquad \frac a2<\mu<a,\qquad v<W-1/a.
\tag{A4}
\]

For sufficiently small **positive** available budget b, targeting A is strictly optimal initially. For sufficiently large b, the joint event is strictly optimal initially. Proof: by (A2), the short-budget marginal net rates are av−1 for A, −1 for B and μW−1 for joint, so A uniquely wins. For the unlimited-budget problem, the state after A has value W−1/a>v (target B), the state after B has value W−1/a (target A), and the best targeted sequence from the initial state yields W−2/a. The joint program yields W−1/μ, which is strictly larger because μ>a/2. There is no other admissible event policy that can beat this statewise recursion (A3). Continuity of the finite-budget Bellman solution and convergence to the recursion imply the long-budget result. \(\square\)

A feasible parameter choice is a=2, μ=6/5, v=7, W=10. Initial net slopes are 13 for targeted A and 11 for joint; as b→∞ the best targeted route tends to 9 while joint tends to 55/6≈9.16667. The exact solved finite-state example selects A at b=0.05 and joint at b=4; H_∅(0.05)≈0.630254 and H_∅(4)≈9.120003. These numbers are generated by the scoped model and are neither estimates nor evidence of industrial profitability. Raising or lowering v by a customer-demand, contracting, or accepted-service change can reverse the small-budget policy **without altering the technical acquisition rates**.

This example defeats two overgeneralizations: (i) a one-shot shared model/embodiment learning event must always dominate staged qualification because it completes more technical edges, and (ii) a staged program must always dominate because the first state is productive. Either can be optimal, depending on the actual operating value of intermediate qualifications and available finance. At the same time, a joint program's technical event rate need not equal a product of marginal skill probabilities; that would change its statistical model.

## 4. Empirical anchor: unloading versus case picking is a plausible distinction, not a measured transition law

**Observed primary-source chronology.** DHL Group's **May 13, 2025** release states that Stretch was introduced commercially for DHL container unloading in North America in **2023**, describes subsequent rollout, and identifies **case picking as a priority to develop**, alongside integration with conveyors and palletizers. The document is an issuer statement, not a matched site-level causal evaluation: https://group.dhl.com/en/media-relations/press-releases/2025/dhl-group-signs-mou-with-boston-dynamics-and-accelerates-cross-business-automation-strategy.html . Boston Dynamics' currently available case-picking product page describes palletized order building, WMS integration through Orbit, and supported case-handling capacities: https://bostondynamics.com/solutions/warehouse-automation/case-picking/ . Product marketing is **not** proof that a particular DHL site, order mix, WMS setup, or customer has accepted case-picking service or made payments under it.

| Typed object | What the sources support | What remains unknown for this model |
|---|---|---|
| A: complete accepted unloading service | DHL described commercially deployed unloading beginning in 2023, with a specified case-handling workflow | Site-matched incremental cash f(A), cost of operator/rework, service-level compliance, and data rights |
| B: integration and complete-order acceptance | Vendor page describes WMS/Orbit and palletized order building as components of offered case picking | Whether any particular site needs a separate B qualification, exact acceptance threshold, and whether it works without A |
| A+B: second accepted service | Co-development and marketing support that the **service frontier** may differ from unloading | Site-level qualified A+B recipe, order rejection/rework, demand and customer payment; f(A+B) is unobserved |
| Joint acquisition event | A vertically integrated redesign could, in principle, establish several service qualifications together | No observed joint success probability/intensity μ or evidence that one intervention establishes A and B together |
| Competent alternative | Existing unloading and picking can be fulfilled by humans or other configured automation | Matched incremental avoidable paid work and outside cost, relevant capacity and service quality |

**Discriminating panel.** For a matched site/window, record accepted **complete orders** rather than grasp counts; end-to-end task route, item and quality requirements; qualification/validation events with timestamps and IDs; independent versus joint outcome of A and B; program expenditure and retained success; human/other automation baseline, intervention burden, switching time, WMS integration and legal rights; customer demand/price and actual receipts; aborted runs and unsuccessful trials (to estimate hazards rather than only successful elapsed time). Capture operator and manufacturer cash separately. Pre-specify the distinct qualification units before computing their interaction Γ=f(A+B)−f(A)−f(B)+f(∅).

A negative test: if the targeted A change alone already delivers both complete services under the customer's acceptance standard, B is not a distinct necessary qualification and the assumed graph is wrong. Another: if f(A)=0 after the best incumbent alternative is included, the initial targeting incentive may vanish, overturning the case in Proposition B. A further negative test is that digital orchestration may supply a competent A+B recipe without joint robotic capability; that changes f. We should **not** estimate λ_j from announced throughput or treat advertised case-handling as paid complete-order output.

## 5. Prior work, verification and live research next step

This finite-state Bellman problem is an application of established continuous-time stochastic control and staged R&D budgeting. The operating graph extends the existing process-flexibility literature (Jordan and Graves 1995) and qualification complementarities parallel established O-ring/reliability arguments. Roberts and Weitzman's early funding-criteria work and Dutta's 1997 R&D budget model are close conceptual predecessors; see the parent manuscript's source ledger for precise reading scope. Our **candidate contribution** is not the Bellman equation, power law, or a manufactured threshold. It is a measurement-linked connection between accepted service topology, joint acquisition technologies, and the economics of *which* robotic production frontier a provider can finance and reach. Novelty requires deeper proof and prior-art review plus real measurement.

**Checks actually performed:** \`python -m unittest -v test_joint_acquisition\` passed 13 scoped tests, including exact single-event closed form, exact free two-event Erlang baseline, independent finite-step Bellman approximation, budget-dependent policy comparison, and retained-state monotonicity. The new code is \`joint_acquisition.py\`, with a reproducible \`results.json\`. The continuous ODE is numerically solved to specified tolerances; the finite-step independent check is approximate. Proofs above are analytical for the stated assumptions; tests are neither proofs nor empirical validation. No historical repo CI was run. The code and tests are compared to their Git blob hashes at publication.

**Exact next theoretical action:** Make the terminal operating value f(S) **date-dependent and partially realized as actual production receipts during qualification**, separating the customer benefit from the deployer's cash and the manufacturer’s transfer/rights. Establish whether the policy reversal survives a competent paid-pilot or supplier-financed alternative once financing is allowed. Preserve all earlier industrial production atlas and milestone requirements; do not move to a new isolated research question.
