# Production creates data, but not automatically a financeable deployment

Theory checkpoint 1 continuation. Maryam Farboodi, Andrew J. Koh and Anchi Xia, *Data-Driven Automation*, NBER Working Paper 35320, **June 2026**. [Inspected primary PDF](https://www.nber.org/system/files/working_papers/w35320/w35320.pdf), retrieved November 16 UTC / November 15 Eastern, 2026. SHA-256 `bb4bde26fd798a3395b7722ddca99acee254fd2dee38546074579abcc7326aac`. The user-supplied arXiv entry `2606.10127` has not been compared version by version. The NBER cover identifies a working paper, not peer-reviewed publication.

## Mechanism card and reading boundary

Read the introduction and §2–2.1, especially equations (1)–(2), Assumption 1 and Definition 2 (printed pp. 7–11), to reconstruct the state/production feedback. The initial checkpoint did not check the long-run propositions. The continuation below reconstructs Proposition 5 and its Appendix A.2 proof; the other long-run, welfare and growth propositions remain unchecked. Abstract or introductory descriptions are not replications.

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


## Continuation: what Proposition 5 actually assumes and proves

Inspected §4.1, Definition 4 and Proposition 5 (printed pp.27–28), and the complete Appendix A.2 proof (pp.54–60) of the same hashed NBER version. This is a reconstruction of the authors' argument, not an independent proof audit of all equilibrium existence/regularity results used by the paper.

**Author result.** Under their baseline economy, a uniformly strongly connected graphon yields full limit automation, meaning the measure of labor-produced tasks tends to zero, for every sigma>0 and eta in (0,1), with bounded initial data. This is not a claim that every task is automated by a finite date or that physical qualification finance is available.

Definition 4 requires a **single** finite n and epsilon>0 with W^(n)(i,j)>=epsilon for almost every pair. The kernel composition integrates over intermediate task mass. The source's informal “connectedness” shorthand must be read with this uniform condition. Ordinary directed reachability is insufficient to verify that particular hypothesis.

### Reconstructed proof chain

1. Let M(t)=integral D_i(t) di. The feasible labor-only allocation gives final output at least psi_L*L. The CES aggregate is no greater than integrated task output on the unit-mass space, so Mdot>=psi_L*L>0 and M diverges. This uses the baseline positive labor endowment and nondepreciating production-generated data.
2. If A_i>=bM, W<=1 implies A_j<=M for all j. With f bounded above and away from zero, the capital productivity ratio is at least lambda(b)=(f_min/f_max)*b^eta. Unit costs chi_i=min(r/psi_Ki,w/psi_L) then obey chi_i<=chi_j/lambda(b). CES demand gives y_i>=lambda(b)^sigma*y_j and hence y_i>=lambda(b)^sigma*Mdot. This implication does not assume task i is already capital-produced.
3. At aggregate-data doubling dates tau_m, normalize r-step exposure as h_m^r(i)=integral W^(r)(i,j)D_j(tau_m)dj/M(tau_m). It lies in [0,1]. The uniform condition gives h_m^n>=epsilon. Set a_n=min(epsilon,1), a_r=a_(r+1)/2 and S_m^r={h_m^r>=a_r}. From h_m^(r+1)=integral W(i,k)h_m^r(k)dk, membership in S_m^(r+1) implies integral over S_m^r of W(i,k)dk>=a_r: outside that set h<a_r, and inside h<=1.
4. Set b_1=a_1 and b_(r+1)=(a_r/2)*lambda(b_r/2)^sigma. If A_i>=b_r*M at a doubling date for i in S_m^r, nondepreciation keeps A_i>=b_r*M/2 until the next doubling. Step 2 supplies enough new output/data there to propagate the next lower bound. Inductively all tasks satisfy A_i>=b_n*M at tau_(m+n-1). Between doubling dates, A_i>=b_n*M/2. Thus eventually cM<=A_i<=M uniformly, for c=b_n/2>0.
5. Minimum capital productivity psi_min diverges while maximum productivity remains a bounded multiple. Suppose a positive measure delta of tasks remains labor-produced along a sequence of late dates. Dividing factor-market-clearing conditions gives r/w=[(L/K)*integral over capital tasks of psi_K^(sigma-1)/(measure(labor tasks)*psi_L^(sigma-1))]^(1/sigma). Uniform productivity comparability bounds this by C*psi_min^((sigma-1)/sigma), also when sigma<1 (use the lower productivity bound for the negative exponent). Therefore every task's capital-to-labor unit-cost ratio is at most C*psi_L*psi_min^(-1/sigma), tending to zero. All tasks would strictly prefer capital, contradicting the maintained positive labor-task measure. This proves the authors' limit claim under their assumptions.

The global factor-price step matters: the proof is not a statement that an isolated firm's positive spillover paths independently fund expansion. Physical capital productivity can grow without bound in the source model, within-task inputs substitute perfectly, and task/data retention is permanent. Physical throughput ceilings, retained human complements, adaptation bills and payment restrictions change the environment.

### Exact two-block check of the graph condition

Partition tasks into two equal-mass blocks. Take block values W=[[0,1],[1,0]]. Each block can reach the other, but odd kernel powers have only off-diagonal support and even powers only diagonal support. No single n has all four block values positive. Consequently this graph fails Definition 4. **This does not demonstrate that full automation fails**; failure of a sufficient hypothesis is not a counterexample to the conclusion.

Now give the first diagonal block weight d with 0<d<=1, keeping the second diagonal zero and off-diagonal weights one. Since each intermediate block has mass one-half, the second composed kernel has diagonal values (1+d^2)/2 and 1/2, and off-diagonal values d/2. Thus W^(2)>=d/2, and Definition 4 holds with n=2, epsilon=d/2. The zero second diagonal prevents using n=1. Ordinary matrix multiplication without the half-mass would be a normalization error.

For equal f, eta=1/2 and sigma=2, the proof's all-time lower coefficient is c=d^2/128. At d=1/10, c=1/12800. This is a conservative coefficient from the proof, not the exact limiting data ratio or a predicted deployment speed. Small positive links can satisfy the theorem while supplying a very weak bound; they do not identify a commercial deadline.

### Robotics extension: keep the missing financing premise visible

Consider two actors with a strictly positive learning kernel and unbounded candidate-policy capability, but a target that also requires a fixed one-unit operator qualification payment before operation. Let the operator start with zero cash, earn no other receipts, and lack borrowing and permitted incoming transfers. The provider may collect indefinitely and both may receive data. The operator funding cut remains -1 at every date, so the service cannot enter. This is an exact infeasibility counterexample in the *modified* environment, not a refutation of Proposition 5. Positive learning edges do not remove a cash obligation or create payment permissions.

The counterexample disappears if that obligation can be eliminated, the operator can accumulate other cash, or a sufficient early transfer/loan is available. Those are substantive mechanisms to measure. The point is to distinguish asymptotic technological/equilibrium automation from financeable entry into a qualified physical service, not to claim a new theorem by adding a permanent veto.
