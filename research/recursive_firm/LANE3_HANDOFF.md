# Paper 3 — Lane 4, independent referee and operational-anchor handoff

**Owner:** Lane 3, one canonical manuscript, `research/recursive_firm/README.md`. **Input:** main `a03659f79395ce9b7d9c06235e660a0d5e704f76`; recursive source `af1cabb95772524db1b34dda3b2667a54c203b43`. This is a scoped handoff appendix, not a paper or referee report. [GATE_A_RECORD.json](GATE_A_RECORD.json) is the current Paper 3 claim/gate record; [SOURCE_DISPOSITION.md](SOURCE_DISPOSITION.md) records the source decisions. Calendar acceptance deadlines remain retired. No oracle exception was requested or used.

## A. Notation delta for Lane 4

The one shared register remains [CANON.md](../portfolio/CANON.md). Its Paper 3 status and typed aliases are synchronized by a small coordination update. Papers 1–2 and the Symbotic record are unchanged. The old portfolio state/CLAIMS entries are input-version records; for Paper 3 this named ledger supersedes their `A in progress` status and extends P3.1–P3.4 with P3.5. Lane 4 should merge these scoped deltas into its next cross-paper ledger refresh without changing another lane's gate.

### Shared objects and collisions

| Symbol / object in this revision | Shared-table relation and units | Collision / exact resolution |
| --- | --- | --- |
| $(x_t,m_t)$ | Economic state and retained procedure; $m_t=\psi_t$ in the existing CANON | P1's $m_j$ is cash-time occupancy. Keep P1 unchanged; use $\psi$ in cross-paper summaries or explicitly label $m^{proc}$ versus $m^{cash\text{-}time}$ |
| $K_t$, $q_t$ | Usable embodied capital and execution policy | $q$ is a policy here; when P2 uses speed/quality $q$, use $q^{exec}$ versus $q^{speed}$ in joint summaries |
| $\mu_t,D_t,R_t$ | Joint beliefs, retained evidence, lawful rights; $R_t$ includes the shared $R^{use}_{s\to j}$ | Evidence $D$ is not demand. Source demand is $D_s$; the MPK example uses $D_{job}$ |
| $H_t,B_t,\mathbf{AR}_t,\mathcal O_t$ | Dated resource capacities, spendable payer cash, due-date receivables, customer obligations | $B$ is always money. Old evidence-allocation $B$ becomes $H^{free}$. Cash and receivables never merge |
| $g_t,\chi_t$ | Organizational arrangement and operating/research phase | $g$ is not an evidence yield; yields use $g_I,g_R$ |
| $\mathcal A,\mathcal K,\mathcal U,o,\mathcal F_t$ | Feasible actions, full controlled transition/observation kernel, successor operator, observation, history filtration | Shared transfer kernel $\mathcal T_{s\to j}$ is a specified component of $\mathcal K$, not the whole production/finance law |
| $\pi,\Pi_i,V_i,r_{i,t},\beta$ | Policy, feasible policy class, claimant value, economic flow, discount factor | Local $\pi_g(a)$ is operating flow under arrangement $g$; it is explicitly different from policy $\pi$. Internal transfers cancel |
| $y^{acc}$, $MPK_r$, $\widehat{MPK}_{r,t}$ | Accepted service, directional physical capital product, state forecast | Neither $MPK_r$ nor its forecast is universally a reward. P3's example substitute is $H_{sub}$, not the hours budget |
| $e_{rec}$; $e_j=e_{{rec},j}$ | Conditional technical successor qualification yield; restricted counterpart to $p^{qual}_{s\to j}$ | Do not substitute observed pick success or source reliability for qualification. P3.5's commercially surviving probability is a different object |
| $\varepsilon_i$, $\lambda_{ev}$, $\lambda_e^{meas}$ | Reducible execution error, useful-record arrival probability, measurement reliability | Replace legacy ambiguous $e_i$ errors with $\varepsilon_i$; old reference yield $e$ with $g_R$. The subscript $e$ on graph parameters is an edge index |
| $\theta$ in P3.5 | Captured fraction of incremental cohort value, dimensionless | P2.5 uses latent design parameter $\theta$. Use $\theta_{cap}$ in cross-paper tables; never transfer the latent-parameter interpretation |
| $\gamma$ in P3.5; $\gamma_i$ in P3.2 | Evidence-starvation elasticity, dimensionless | Any P2 manufacturing curvature with the same glyph remains unchanged; cross-paper alias is $\gamma_{ev}$ |
| $d$, $L_t$, $w$, $s$, $X$ | Settlement lag; remaining cash bridge; operating outlay rate; guaranteed net cash rate; cash beyond bridge | $wd$ is peak working capital (money), not P1's integral cash-time occupancy (money × time). Recomputing $L_t$ prevents charging the initial bridge every generation |

### Proposition-local additions and translations

These local namespaces are explicitly defined in their owning proposition. Their use does not rename a shared object.

| Claim | Symbols introduced / revised | Meaning and translation boundary |
| --- | --- | --- |
| P3.1a | $j,p_j,k_j,G_0,c_j,e_j,S,W_j$ | Program index, current success, current cost/contribution, conditional successor spend/yield, next-cohort stake and program value. $S$ excludes value already in $G_0$ |
| P3.1b | $Z,T,Y_3,\mathcal D_3$ | Source assignment, post-production artifact passage, third-cohort outcome, factorial contrast. In joint tables write $T^{pass}$; this is not the transfer kernel or evidence delay |
| P3.1c | $D_{job},H_{sub},\Delta_a,\mathcal I,Z$ | Demand, qualified substitute, action-value difference, current information and forecast signal; local signal $Z$ is not the cohort treatment |
| P3.2a | $n,a_i,b_i,\alpha_i,v_i,\kappa_i,\gamma_i,a_0,\tau,\nu_i$ | Record count; error-curve scale/offset/exponent; exposure; arrival scale/elasticity; informative audit floor; fixed donor record multiple; record-growth exponent. $\tau$ here is a declared fixed record multiplier, not identified structural reliability |
| P3.2b | $p,u,h_0,h_1,r,H^{free},I^{elig},i,a,y,z,g_I,g_R$ | Reliability, source workload, hour coefficients, incident coefficient, free hours, incident-review cap, incident/reference/other-service hours, evidence and yields. Old source $B\to H^{free}$, $g\to g_I$, $e\to g_R$, $I\to I^{elig}$ |
| P3.2b | $\mathcal H,U,W,V,k(p),K_s,D_s,v_s,c_s,\kappa_u$ | Effective hours and service/recipient/optimized value; effective workload draw; source capacity/demand; unit contribution/cost and workload curvature. Old effective-resource $E\to\mathcal H$ and old curvature $d\to\kappa_u$; $d$ is reserved for settlement lag in P3.5 |
| P3.3a | $Z_i,U_e,\eta_e,M_e,Y_e,\tau_e^{str},\lambda_e^{meas}$ | Latent vertex, structural sign, measurement sign, stable pair relation, reading and the two reliabilities. Their product is identified only where the observation law identifies that product; repeats alone do not identify every structural parameter |
| P3.3b | $U,T,p_U,p_T,j,G_A,c_A,V_0,V_S,V_R$ | Novelty/transfer events, marginals/joint probability, benefit/cost and unaudited/source/recipient option values. Use $U^{nov},T^{tr}$ if crossing namespaces; $j=\Pr(U\cap T)$ is not a product without independence |
| P3.3c–d | $\ell,p_\ell(y),b_y,w_y,p_1,p_2,z$ | Hidden convention, roster/admission/retention masses, lane success probabilities and generating-function dummy. Legacy hidden $m\to\ell$; local PGF $z$ is formal, not validated evidence |
| P3.4a | $I,P,C_{in},C_{out},v_I,v_P,W_g,Q_g,U_g,r_g(a),\mathcal B_g,\mathcal T_g$ | Internal/partner arrangements, switch costs, mature flows/values, stay and full switching values, portability chance and Bellman operators. Operator $\mathcal T_g$ is not cross-firm transfer $\mathcal T_{s\to j}$ |
| P3.4b | $G_S,d_I,d_P,\rho,\zeta,\zeta^*$ | Captured speed stake, two qualification lags, frontier survival, discounted persistence and its fixed-pair peak. Legacy $w\to G_S$, $x\to\zeta$; $x$ is reserved for the economic state |
| P3.5 | $c,h,v_{op},G,f,\lambda_{ev},\delta_{obs},a,H_G,C,R_{rec},\Delta_{rec},\lambda_*$ | Direct cash outlay, shared hours, their present opportunity price, incremental cohort stake, unresolved-case index, arrival, preacceptance hazard, $a=\beta(1-\delta_{obs})$, receipt ceiling, economic cost, expected receipt, margin and arrival threshold. Bare $\lambda$ and $\Delta$ are local abbreviations |
| P3.5 | $T,\sigma_k,\mathsf s_k,J(\pi),N^*,I_t^{rec},\mathcal D$ | Evidence delay, initiation times, initiation economic state, incremental policy value, optimal weighted attempt count, successor inquiry and invariant dormant set. In joint summaries use $T_{ev}$ for delay; $\mathsf s_k=(x,m)$ avoids reusing evidence $z$ |
| P3.5 | $O_t(u),A_t(u),L_t,t_{fund},M,Y_n,L_{cycle},q_\beta,V_{regen}$ | Mandatory outlays, certain collections, peak cash deficit, sufficient financing-wait bound, refill periods, settled receipt, cycle time, discounted renewal factor and constructed policy value. $A_t$ collections is not A.COST intercept $A_\sigma$ |
| P3.5 | $p^{qual}_{commercial},z_{op},\eta,n_{stop},\bar G,S_{obs}(T)$ | Commercially surviving qualification probability, operating-profitability shifter, remaining-error factor, no-renewal stopping depth, stake bound and survival function. Profitability shifter $z_{op}$ replaces ambiguous evidence $z$ |
| P3.A.COST | $c,\sigma,A_\sigma,N_\sigma,n_{it},d_t^{obj},\mathcal C$ | Common per-attempt surcharge, complete contingent policy, cost-independent intercept, objective-weighted count, dated attempts, nonnegative objective weights and common-feasibility interval. Same direct-charge meaning as P3.5 only when that restricted cost accounts for the same resource |
| P3.A.COST | $A_i(h),N_i(h),A_i(h,a),N_i(h,a),S_1,S_2,x,y,v_1,v_2$ | Conditional continuation intercept/count and current-deviation variants; fixed matrix-game supports, mixes and values. Local history $h$ is not P3.5 hours; local mixes $x,y$ are not the economic state or accepted service |

**Required Lane 4 carry-through:** preserve the existing accepted-service, qualification, rights, three-network and cash-time definitions; incorporate aliases without silently changing P1/P2 mathematics. Route all new successor, scaling, identification and firm-boundary derivations here. Diagnostic portfolio/design work remains P2-owned. New independent monographs on these subjects remain prohibited.

## B. Gate B Referee Brief for an independent author

**Status: assignment-ready, not a report and not a Gate B pass.** The author/co-derivation and source-checking agents in this turn cannot count as the independent hostile referee. The referee should read the published commit, this brief, P3's claim record, the proof appendix, and the immutable source dispositions. Use the objection structure of [integrated_firm_referee.md](../../reviews/integrated_firm_referee.md). Do not invoke any solver or treat its availability as an instruction to do so.

### Claims and proof dependencies

| Claim to attack | Proof dependency | Exact retained scope / defeating case |
| --- | --- | --- |
| P3.1 successor value and the three-layer discriminator | A.1; randomized carrier/exclusion assumptions | A change in executor, answers, rights or selected surviving sites can mimic procedure lift. Value-of-information is standard; no generic RL advantage is claimed |
| P3.2 endogenous evidence speed and allocation | A.2 fluid law / concave frontier / interior FOCs | Informative positive reference floors, moving yields, capacity corners and profitable source expansion change the response. Passive starvation and active crowding must not be conflated |
| P3.3 observational equivalence and audit ranking | A.0 induction; A.3 likelihoods and Fréchet bounds | Repeated stable measurements, observable rejection reasons, tagged settlement or an informative asymmetric release can defeat particular equivalences |
| P3.4 integration then delegation / speed hump | A.4 contraction and derivative | Joint labs, reservable slots, informative failure and changing finance add alternatives/states; no optimized-envelope hump is claimed |
| P3.5 dynamic dormancy / self-funding | A.5 stopped-sum accounting, all-action invariance, cash prefix and regenerative construction | A hidden positive continuation, useful rollback, banked evidence, refunds, uncertain operating surplus, global obsolescence or nonrenewing stakes can defeat the relevant claim |
| P3.A.COST | A.6 common feasible tree and affine payoff / all-history comparisons | Finance-induced menu change, endogenous rival behavior and singular mixed supports invalidate the broader extrapolation |

### Mandatory axis (i): novelty and closest prior art

The shared four-work matrix in CANON remains authoritative. Extend its Paper 3 row using the following verified antecedents; do not declare priority from a title or abstract. Candidate contribution is the **particular integration of priced successor production, observation restrictions and dynamic economic regimes**. Standard dynamic programming, optional menus, learning, information value, ownership, payback and multi-round tests are not claimed as inventions.

| Primary work / inspected version | What already overlaps | Required referee challenge / reading boundary |
| --- | --- | --- |
| Teece, Pisano & Shuen (1997), [Dynamic Capabilities and Strategic Management](https://doi.org/10.1002/(SICI)1097-0266(199708)18:7%3C509::AID-SMJ882%3E3.0.CO;2-Z) | Organizational processes, assets and paths shaping adaptation and value capture | Does $(x,m)$ add a falsifiable restriction beyond dynamic capabilities? Publisher abstract/bibliography verified here; a complete source reconstruction remains the referee's work |
| Cohen & Levinthal (1990), [Absorptive Capacity](https://josephmahoney.web.illinois.edu/BADM%20545_Spring%202008/Paper/Cohen%20and%20Levinthal%20%281990%29.pdf) | Experience, prior knowledge and productive activity can build the ability to learn | Do the matched carrier and third-cohort comparison isolate something beyond absorptive capacity? Original article inspected; no priority clearance claimed |
| Stiglitz (1987), [Learning to Learn, Localized Learning and Technological Progress](https://www.cambridge.org/core/books/abs/economic-policy-and-technological-performance/learning-to-learn-localized-learning-and-technological-progress/13028124BFC3684156E164B58B4BDFBA) | Learning about how to learn and path/locality dependence | Can the new results be obtained by a standard learning-technology state? Official chapter record/summary verified; full theorem-by-theorem comparison remains open |
| Gittins (1979), [Bandit Processes and Dynamic Allocation Indices](https://aima.cs.berkeley.edu/~russell/classes/cs294/s11/readings/Gittins%3A1979.pdf); Cohn, Ghahramani & Jordan (1996), [Active Learning with Statistical Models](https://www.jair.org/index.php/jair/article/view/10158) | Sequential allocation, stopping and selective experiment/data acquisition | Is P3.5 a standard discounted experimental project with renamed primitives? Separate what is a useful application from what is a new result; identify which endogenous institutional state matters |
| Zelikman et al., [STOP](https://arxiv.org/abs/2310.02304), preprint 2023 / COLM 2024, v3 | Improvement of an improvement scaffold with a fixed base language model | Improving an improver is prior art. Fixed base weights do not nullify this antecedent. Does a supplied sandbox already suffice for the claimed result? |
| Srikanth et al., [AIDE²](https://arxiv.org/html/2609.26457v1), September 2026, v1 | Search over an inner research harness with the outer optimizer/models fixed in the principal run | Its stronger outer-improver test is inconclusive. Do not convert technical-budget gains into commercial return or stronger recursion than the source establishes |
| Luo et al., [Toward Recursive Self-Improvement in Physical AI](https://arxiv.org/html/2610.29677v1), October 2026, v1 | Already discusses payback before obsolescence and controlled successive-improver evaluation | Costly physical recursion and multi-round tests alone cannot establish novelty. The specific cash-prefix/invariance and evidence/crowding result must survive comparison; the source is a proposal/survey |
| Xiao et al., [ENPIRE](https://arxiv.org/html/2606.19980v2), 2026, v2 | Physical policy research through finalized reset, verification and safety interfaces | A competent agent can optimize a technical task inside those supplied interfaces. This is an explicit sufficiency boundary, not evidence that all economic institutions were endogenized |

### Mandatory axis (ii): functional forms and dynamic validity

Attack the geometric/power-law scalar threshold separately from the portable economics. A.5.6 already extends the cash-rich sign to any delay distribution ordered by first-order stochastic dominance with nonincreasing discounted survival. The all-action Bellman supersolution/invariant-set condition does not require a power law. Closed-form $\lambda_*$ does. Test whether changing utility, information acquisition timing, repeated payoff shape or joint uncertainty requires a different threshold/correspondence.

Specific required attacks: can an unprofitable first inquiry unlock a profitable later state; can an old executor create useful evidence; can evidence be banked before committing the cost; is a reserved external slot cheaper; does ordinary learning catch up while the inquiry waits; do direct costs or benefits double-count a receipt; does the cash plan count uncollected receivables; can a sufficiently long failure streak bankrupt the firm; does obsolescence destroy the entire operating core; and does frontier/stake renewal actually occur? Every exit must be included and defeated or remain outside the theorem's stated restriction.

P3.5 holds construction cost and technical yield fixed. Its regenerative chain **does not demonstrate that an improver becomes better at producing later improvers**, nor does positive expected project value prove pathwise self-financing. The proof constructs an operation-funded policy and excludes optimal permanent abandonment in its recurrent positive region; it does not solve the globally optimal cadence or the full strategic economy. A.COST's rival-withdrawal example remains an explicit warning against signing equilibrium responses from fixed-rival derivatives.

### Mandatory axis (iii): when agent-level RSI suffices

Require at least these cases: (1) a self-contained software sandbox where budget, evaluator, data access and deployment rights are supplied; (2) a physical lab with fixed human/reset/verification interfaces whose costs and access are exogenous; (3) a firm whose internal agent fully represents the relevant economic budget and objective, so the agent/firm distinction changes no feasible policy; and (4) equivalent external contracts implementing the same contingent program. A.0's implementation-equivalence lemma prevents an ownership premium by renaming controllers. Identify a concrete economic choice or omitted opportunity cost before insisting on firm-level analysis.

### Referee output and disposition standard

For each objection provide ID, target claim, severity, exact defeating construction or missing assumption, source/proof reference, and required narrowing. Gate B remains pending until a **different author** supplies the report and each retained claim survives or is narrowed. Acknowledging an objection that still defeats a retained claim is not resolution. No novelty or empirical pass is recorded by this brief.

## C. Gate C operational anchor proposal — Robin, complementary to Symbotic–Walmart

Lane 4's [Symbotic–Walmart record](../portfolio/empirical_target_symbotic.json) remains the contractual, rights and payment anchor, with **16 explicit nulls**. This turn changes neither its bytes nor its interpretation. It does not establish recursive improvement or estimate a learning transfer effect. Robin is a separate operational source, not a way to fill Symbotic's contractual nulls by analogy.

The [Robin packet](operational_anchor_robin.json) uses Li et al., *Demonstrating Large-Scale Package Manipulation via Learned Metrics of Pick Success*, RSS 2023, [arXiv v2](https://arxiv.org/html/2305.10272v2). The reported logs, failure selection and learned ranking map to evidence, sampling and execution. Malfunctioning suction cups motivate proposed monitoring; a measured wear law is not disclosed. These are author-reported operational facts, not independent replication or a measured inquiry-procedure transition.

The clean next observation is a versioned **sampling/test-selection procedure** carried to a fresh cell while matching the executor, evidence budget, rights and evaluator, followed by independently measured third-cohort successor production. Record all proposed procedures and failures; measure displaced accepted service and dated costs. Distinguish a researcher choosing a sampling rule from an organization learning how to construct better such rules. No outreach, experiment, data access or commercial execution is authorized or performed by this proposal.

Predeclared nulls include wear-to-margin elasticity, deliberate-sampling opportunity cost/intensity, appropriable share, lawful reuse rights, cross-cell causal transfer, successor yield, third-cohort lift, MPK, and the cost/cash/lag/hazard/arrival coefficients required by P3.5. Each has an identifying observation in the JSON. Public logs and reported sampling comparisons motivate those observables; they do not fill the nulls. Gate C remains pending after the separate Gate B pass.

## Completion and next falsifiable question

The publication comprises the canonical text, its proof/source/handoff appendices, scoped gate/claim record, Robin proposal, one small exact checker, and the necessary CANON/manifest coordination. Historical source files, Papers 1–2 and the Lane 4 evidence packet remain unchanged. The checker uses only Fraction arithmetic and runs below the specified two-second bound; its observed receipt is in GATE_A_RECORD. No other computational study was executed.

Next falsifiable question for the independent referee: **Does any feasible retained procedure, ordinary-learning action or equivalent outside arrangement escape the claimed invariant dormant set after all effects on cash, informative evidence and successor-production value are accounted for?** A defeating case narrows the basin; it does not justify restarting the frozen exhaustive loop.
