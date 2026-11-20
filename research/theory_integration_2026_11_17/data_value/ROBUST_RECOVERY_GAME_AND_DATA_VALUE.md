# Finite physical recovery games: a constructive admission test inside qualified production

**20 November 2026 UTC — continuing the November 22 integrated scientific audit of *When Capabilities Become Production*.** This is a conditional finite-state mathematical design, **not** a certified robotics controller, tested safety architecture, actual original-customer outcome or new control-theory result. The November 22 gate remains open.

## Problem and distinction

The preceding sequential-fallback chapter defined the X-first, R-after-failure physical recipe as \(Q_F=X+(1-X)H\), but left its most consequential variable \(H\)—whether the **complete** original service can still be recovered—structurally unverified. This chapter gives a *constructive conditional method* for checking H against a disclosed finite, disturbance-complete network abstraction, rather than inferring it from a superior upgraded-controller success rate or a retained binary executable.

A network state \(s\in S\) contains physical configuration, workpiece condition, service clock and remaining SLA, human/robot/operator allocation and displaced jobs, access and licensed dispatch permissions, and the versioned controller. The finite model has a safe subset \(K\), a terminal *physically delivered-and-qualified* service subset \(G\subset K\), legal old-controller recovery actions \(A_R(s)\), and a nonempty set \(T_R(s,a)\subset S\) of physically possible successor states including admissible disturbances. A step consumes one unit of the relevant service horizon; any heterogeneous execution duration must be represented by intermediate clock states. This finite conservative model must include all known failure transitions and cross-network resource use, not just nominal robot joint trajectories. Customer order/offer/payment support is a **different** predicate and must not be smuggled into G by assuming customer acceptance.

## Constructive winning-region proposition

For \(t=0,\ldots,H\), let \(W_0=G\), and recursively
\[
W_t=W_{t-1}\cup\{s\in K:\exists a\in A_R(s)\ {\rm with}\ \varnothing\ne T_R(s,a)\subseteq W_{t-1}\}.
\]
Under perfect observation, finite \(S\), correctly specified transition support, dynamically selectable *permitted* old actions, and an absorbing terminal goal, \(W_t\) is **exactly** the network states from which some R-only contingency strategy ensures fully qualified physical service within \(t\) more steps for *every* allowed disturbance. This is ordinary finite safety/reachability-game dynamic programming, not a novel theorem. Its proof is backward induction; see [proof ledger](ROBUST_RECOVERY_GAME_PROOFS.md).

For a *fixed* one-step source-trained proposal X at original state \(s\), let \(T_X(s)\) include **all** its possible first-step outcomes, not merely observed postfailure states. If X first-step safety is guaranteed, the source-trained X-first/old-R-after-failure plan is robustly qualified within remaining horizon \(t\) **if and only if**
\[
\emptyset\ne T_X(s)\subseteq W_{t-1}.
\]
This criterion includes X successes in G and insists that every nonsuccessful X outcome has a feasible R rescue in the remaining physical and contractual horizon. It is an iff only within the stated X-first-then-R-only action class and exact complete model. If permitted recovery includes other controllers or a new embodiment, augment the action game and label the extra resources explicitly; do not pretend it proves feasibility of bare R rollback.

A preaction selector \(\pi(s)\) that chooses X only at such admitted states and otherwise chooses an old winning strategy preserves R's **robust original success set** within the same closed network, provided each original \(s\in W_t\) is observed before acting and no unmodeled policy-induced customer/operator spillover occurs. It does *not* automatically preserve realized successes that R happened to obtain in states outside its robust winning set, and it says nothing about legal purchase, realized receipts or extra data/verification cost. A safety game whose possible successors omit a rare tail cannot establish real-world safety.

A useful negative comparative static: enlarging the *disturbance support* for fixed R actions (without changing legal actions, safe/goal sets or horizon) weakly **shrinks** each W and cannot enlarge X admission; adding new independently resourced feasible recovery actions can enlarge W but requires actual qualification and rights. A larger source-training dataset alone changes neither property unless it changes the certified transition or observation model.

## Exact finite demonstrator

The committed [self-contained source](robust_recovery_game.js) / [stored result](robust_recovery_game_results.json) uses states \`initial\`, \`done\`, \`retry\`, \`blocked\`, \`expired\`, \`fault\`. The original R can finish from \`initial\` or \`retry\` in one step; \`blocked\` means no remaining operator, \`expired\` means no remaining contract time, and \`fault\` is an unsafe physical state. Within a two-step initial horizon, old recovery admits \`done\`, \`initial\` and \`retry\`, but not those three failure states.

| Proposed possible X first-step outcomes | Robust X-first/R-retry admissible? | Reason |
| --- | --- | --- |
| \`done\` or \`retry\` | Yes, *inside the model* | Every possible state is complete or R-recoverable with one step left |
| \`done\`, \`retry\`, or \`blocked\` | No | A shared operator can be unavailable after an X failure |
| \`done\`, \`retry\`, or \`expired\` | No | A recoverable workpiece still misses the service deadline |
| \`done\` or \`fault\` | No | A possible X first step violates the modeled physical safety set |

All 31 nonempty subsets of the five possible outcomes are enumerated, and only the three nonempty subsets of \{\`done\`,\`retry\`\} are admitted. The source executed 47 internal assertions; an independent Python set-enumeration check agreed with both winning sets and all three admitted outcome subsets. These are *synthetic logic checks*, not a safety test for any robot.

This is a **structural** result: an apparently high mean X qualification, or a highly informative field-failure dataset, cannot establish the universal successor condition unless independently validated support coverage and a physical recovery proof exist. Conversely, a genuine signed conservative reachability abstraction can reject unsafely optimistic X without estimating any buyer-value parameter. The old stored R policy is an economically valuable *option* even when X is excluded.

## Integrate the safety game with economic source-data value

**Model A, market-conditioned production:** let \(\mathcal P_{\rm certified}(z)\) be complete R/X/G/E recipes whose time-expanded safety, rights, operator and embodiment resources have been qualified for original eligible network \(z\), with permitted menus and customer choices recorded separately. The customer production LP/integer program \(V(\mathcal P_{\rm certified};\omega)\) optimizes *actually accepted complete service* subject to full finite resource and buyer constraints. It does not sum individual technical skill percentages, nor treat a robust R rescue as free operator time. The certified gate changes the feasible recipe set; procurement budgets, price/quality response and substitution determine whether that changed set earns money.

**Model B, endogenous learning:** a source batch \(D^X\), target grounding \(D^G\), a new embodiment \(E\), or production-generated recovery trajectories may change the model, reachable network states, certified action set, subsequent data visitation and buyer orders. At time t, choose only approved full policies:
\[
J_t(b,s)=\max_{a\in\mathcal A_{\rm admitted}(b,s)}
\left\{m(b,s,a)-c_{\rm data,rights,compute}(a)+
\beta\mathbb E[J_{t+1}(b',s')\mid b,s,a]\right\}.
\]
Here \(b\) is information/learning state, \(m\) is fully netted **current** accepted production contribution (after scarce operator displacement, not arbitrary benchmark-to-dollar conversion), and the continuation term is the **only** future data/learning value. The old feasible policy remains selectable if genuinely preserved; free optional data cannot lower the maximized gross option value in a common environment, while forced training/changed markets need not be beneficial. Data rights are necessary when field recovery logs or teleoperation input are reused.

Target grounding may expand W by supporting reachable rescue in previously unsupported original buyer states. A newly embodied spare may expand W only if operator pools, access rights and safety reachability are genuinely independent. Additional source data may improve average X technical rates but fail to expand W where rare, consequential post-X transitions remain. This is a falsifiable mechanism distinction, not an assumption of positive additive data transfer. Simulation, synthetic data, public/pretrained data, teleoperation, field successes, intervention and failure/recovery trajectories each require their own source lineage and tested target transfer.

## What the November 22 scientific gate can and cannot accept

**Conditional mathematical findings:** finite robust recovery under fully specified transitions, baseline physical retention under a certified selector, and an admissibility-versus-exposure separation inside optimized production. **Unidentified field propositions:** a signed complete network abstraction, bounded unseen X failures and disturbance coverage, SLA-compatible old recovery, reproducible original customer accepted-service orders, net operator displacement and proper X/G/E experiment permissions. A separate whole-network randomized-arm value comparison can estimate *expected* policy contribution under suitable assignment even when no casewise physical recovery is certified, but it cannot be interpreted as a safety certificate or an isolated source-transfer mechanism.

Prior work: Aubin, “A Survey of Viability Theory,” *SIAM Review* (1990), https://doi.org/10.1137/0328044; Alshiekh et al., “Safe Reinforcement Learning via Shielding,” *AAAI* (2018), https://doi.org/10.1609/aaai.v32i1.11797; Laroche et al., safe policy improvement with baseline bootstrapping, *ICML* (2019), https://proceedings.mlr.press/v97/laroche19a.html. Their viability/shield/expected-return methods are foundations; this paper's potential contribution, if independently established, would lie in the **integrated economic treatment of qualified original-customer production, endogenous heterogeneous data and certified whole-network recipe feasibility**, not rediscovery of safety games or DDA §5 data value / Appendix B complementarities.

**Next exact gap:** audit whether original eligible buyer/operator network boundary and signed time-expanded X-failure support exist for even one actual R/X/G/E comparison. If no, preserve sharp conditional claims and unidentified empirical ranking, and test an alternative allowed whole-network estimate. Do not certify a robot, infer X/G investment ranking, manufacture demand or create a nominal new threshold. November 22 remains OPEN. Final December 25, 2026, 23:59 Eastern unchanged.
