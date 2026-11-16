# Production creates data, but not automatically a financeable deployment

Theory checkpoint 1 continuation. Maryam Farboodi, Andrew J. Koh and Anchi Xia, *Data-Driven Automation*, NBER Working Paper 35320, **June 2026**. [Inspected primary PDF](https://www.nber.org/system/files/working_papers/w35320/w35320.pdf), retrieved November 16 UTC / November 15 Eastern, 2026. SHA-256 `bb4bde26fd798a3395b7722ddca99acee254fd2dee38546074579abcc7326aac`. The user-supplied arXiv entry `2606.10127` has not been compared version by version. The NBER cover identifies a working paper, not peer-reviewed publication.

## Mechanism card and reading boundary

Read the introduction and §2–2.1, especially equations (1)–(2), Assumption 1 and Definition 2 (printed pp. 7–11), to reconstruct the state/production feedback. The long-run automation, welfare and growth propositions and their proofs remain to be checked. Their abstract or introductory descriptions are not our replications.

**Question.** How does heterogeneous production generate heterogeneous data that both improves automated tasks and changes which tasks can profitably use capital?

**Primitives and agents.** A continuum of tasks enters CES final-good production, with elasticity sigma. Intermediate output is linear in labor and capital: `y_i=psi_L*l_i+psi_Ki(A_i(D))*k_i`. Baseline aggregate capital and labor are fixed. Labor and capital are perfect substitutes within a task. Capital productivity is `psi_Ki=f_i*A_i(D)^eta`, with `0<eta<1`; f_i is positive, bounded, and weakly decreasing in the ordered task index. The initial stock is bounded, continuous and strictly decreasing. These order restrictions support their indexed automation-boundary analysis; arbitrary finite matrices should not be claimed to inherit every theorem.

**Information and equilibrium.** At each date, data stocks are given; final and intermediate producers maximize profits, with rental rate, wage and factor allocations determined in equilibrium. Automation depends on productivity **and factor prices**, not capability alone. The baseline is not the single provider's privately financed customer portfolio in our Model B.

**Transition and directed transfer.** Equation (2) is `D_i(t)=D_i(0)+integral_0^t y_i(s) ds`. Production by either input generates task data. There is no data depreciation in this specification. Effective target data is `A_i(D)=integral W(i,j)D_j dj`, where **j is source and i is target**, and W is nonnegative and need not be symmetric. The paper explicitly describes block structure as nesting finite-sector patterns. A block calculation must incorporate task-mass weights; our unit-weight illustration below is an adapted finite mechanism, not a numerical replication of a continuum equilibrium.

**Assumptions doing the work.** Producing output supplies usable data at the specified rate; nonnegative spillovers; persistent data; diminishing returns in effective data; and perfect within-task factor substitution. The framework does not by itself price a robotics-specific processing, qualification or physical-delivery program. Treating a positive graph edge as already paid and deployable would skip those choices. Negative transfer requires changing this nonnegative effective-data mechanism, not silently assigning a negative W and retaining its results.

## Reconstructed local implication

For a finite block representation with weights absorbed into W, `A_i=sum_j W_ij D_j`. At strictly positive A_i, differentiation gives

`partial psi_i / partial D_j = eta*f_i*A_i^(eta-1)*W_ij`.

Thus an extra unit of source j data can benefit several targets, but the benefit is weighted by direction, baseline effective data and the target's productivity coefficient. For a differentiable continuation objective V(psi), the chain rule gives

`partial V / partial D_j = sum_i V_psi_i*eta*f_i*A_i^(eta-1)*W_ij`.

This is our elementary derivation from the source's technology, **not one of the authors' welfare propositions**. V_psi_i must come from the specified economic objective; substituting arbitrary centrality weights would beg the question. At an entry/qualification threshold V may be nondifferentiable; use discrete differences instead. At A_i=0 the derivative can be singular for eta<1, so the formula is not asserted there.

## A finite counterexample to unweighted reach ranking

Take unit-weight task blocks, `W=[[1,0],[1/2,1]]`, `D=(4,1)`, `f=(1,1)` and `eta=1/2`. Effective data is `(4,3)` and productivity `(2,sqrt(3))`. One additional unit generated at source 1 changes productivity to `(sqrt(5),sqrt(7/2))`; the same data increment at source 2 changes it to `(2,2)`.

Source 1 reaches two targets whereas source 2 reaches one. Nevertheless, if only target 2 has incremental economic value in the modeled window, source 2's gain `2-sqrt(3)` strictly exceeds source 1's gain `sqrt(7/2)-sqrt(3)`, since `4>7/2`. This is an exact algebraic comparison, not an empirical transfer estimate, and it does not solve the source paper's equilibrium. A zero marginal value at target 1 could arise from a saturated market or missing qualification; it is an explicit scenario assumption. The example defeats the claim that unweighted reach alone ranks economically valuable data production.

## Proposed robotics extension and prior-art consequence

Allow source eligibility `e_j` to reflect collection quality/rights and let effective target gain require separately funded adaptation/qualification and supported hardware. Keep those as distinct transitions: data possession, permission, candidate construction, validation and operational deployment. The economic continuation weights then depend on customer demand, capturable surplus and the payer who can fund the prerequisite. No additional strategic premium is added to the continuation value.

Crucially, **directed spillovers and endogenous data production are already in this seed paper**. Merely adding a learning graph is not our contribution. The open candidate is the interaction of that graph with complementary physical qualification and a different cash/payment graph at the enterprise level. That candidate still needs the Chen–Elliott–Koh capability-combination audit and a concrete distinguishing result.

Next check: reconstruct one specific source proposition and its proof assumptions, rather than infer long-run automation from connectivity in a finite, financed robotics graph. The illustrative counterexample above and the [two-period calculation](deployment_investment.md) are deliberately much narrower than the source's general-equilibrium results.
