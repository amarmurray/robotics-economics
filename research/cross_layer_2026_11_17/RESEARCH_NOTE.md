# Q7 — Manufacturing experience, field learning, customer access, and heterogeneous capture

**November 17, 2026.** Input branch: 2692e1a526c72597b217e5d1c11715d2262ae20d. Synthetic exact benchmark and empirical identification design. **Not** an estimated robotics model, a demonstrated original contribution, or a completed first paper. Model and tests: cross_layer.py and test_cross_layer.py. A fuller executed-session note and outputs are also preserved in the accompanying research package.

## Question

An industrial deployment can change three economically distinct states: (M) manufacturing experience, which affects the supplier's real production cost but not necessarily the invoice it charges; (F) destination-relevant field experience, which can lower provider qualification cost only when transfer and rights actually permit reuse; (C) customer relationships, operations and commercial discovery, which change demand for qualified future output. These are directed, typed relationships among different actors, not one generic data/learning stock. The source deployment also generates dated provider cash.

We ask when a lower-current-cash hybrid source is worth choosing over (i) a factory-embedded source generating current receipts and supplier learning, (ii) a field/customer source, or (iii) no source, while retaining a credible competing investment in an already-qualified A configuration.

## Exact environment

The provider starts with liquid cash B0=7. Each source has one preexisting unit of qualified service and produces net provider cash via final-demand choice: customer revenue R(q)=a*q-b*q²/2, resource cost c*q, capacity K=1, outside alternative Pi0=0, and an assumed two-part tariff reimbursing costs plus rho=4/5 of operating surplus. With b=2,c=2, source demand intercepts 37/4,8,27/4,2 produce current provider cash 5,4,3,0. Their synthetic experience vectors (manufacturer X, field L, customer access C) are respectively (2,0,0), (0,2,1), (1,1,2) and (0,0,0). Manufacturer experience is incremental usable process knowledge, not number of robots built; L is target-useful experience rather than data quantity; C is a hypothetical commercial signal rather than observed market share. The no-source option has no accepted output.

At the next date, available cash is B_s=7+m_s. The operator can retain cash; acquire one additional incumbent A unit for 6 yielding incremental future provider profit 52/5, net 22/5; or purchase and qualify exactly one S specialist for target market B. The menu excludes simultaneously purchasing A and S; that is an explicit simplification.

B customer inverse demand is induced by R(q)=a_B*q-2*q²/2, marginal service cost 3, best alternative profit 2, capture 4/5, and qualified S capacity 2. Its intercept is a_B=12+zeta*C, baseline zeta=2. Quantity and adoption are chosen endogenously subject to the outside option and capacity.

The specialist's provider invoice is p_S=8-3*kappa*X, while the manufacturer's real production resource cost is u_S=7-3*X. Usable qualification expense Q=7-3*delta*L. Kappa and delta each lie in [0,1], representing supplier price pass-through and usable field-experience cost saving, not ownership percentages or inferred contract terms. The provider's total entry obligation is I_s=15-3*kappa*X_s-3*delta*L_s. It must be paid out of B_s before future service. No credit, terminal salvage or hidden strategic-learning premium is introduced. Real supplier cost reductions and invoice transfers are counted only once.

For a realized specialist order, supplier gross margin on the model's bounded cost accounting is 1+3*(1-kappa)*X. Alternative G sales, manufacturer overhead, previous source economics, incentives and contract bargaining are omitted; this is not a supplier full-firm strategy model.

## Result 1 — Financeability is not optimal sequencing

For hybrid source, target provider operating profit is 16, source cash is 3, available investment budget is 10, and qualification plus invoice is 15-3*(kappa+delta). Hybrid specialist entry becomes **financeable** when

    kappa + delta >= 5/3.

Once financeable it dominates that source's incumbent expansion in this parameterization; hybrid source value is V_H=4+3*(kappa+delta). For all kappa in [0,1], the factory source's specialist option is worse than the incumbent investment, so factory total V_F=5+22/5=47/5. The field source likewise chooses incumbent and has V_D=4+22/5=42/5; no-source total is 22/5. Hybrid is strictly preferred globally only when

    kappa + delta > 9/5.

At equality, the declared tie rule favors the cash-richer factory source. The interval [5/3,9/5] is a funded but privately suboptimal source/target expansion. With delta=1, kappa=2/3 funds the specialist, while kappa>4/5 is required to choose the hybrid over the factory. At kappa=81/100, hybrid total provider value is 943/100 versus factory 47/5; supplier margin on the specialist order is 157/100. At kappa=4/5 the source choices tie and the selected factory policy places no specialist order. This is a conditional threshold, not a general theorem of vertical integration.

## Result 2 — Destination demand is an independent gate

Under full rights and the capacity-binding, participating B-service regime, hybrid continuation profit is (8/5)*(a-2), where a is the *base* B demand intercept before access uplift. Its total source value is (8/5)*(a-2)-6. Against factory's incumbent source value 47/5, the hybrid is strictly preferred locally if a>93/8=11.625. At a=11, factory wins; at a=12, hybrid wins. Far below this region, the B customer may not participate or may demand less than capacity. The exact optimizer, not this interior simplification, applies there. At sufficiently high a the factory's own specialist option must also be rechecked.

In the baseline exact simulation, hybrid wins (total 10) and factory/field total 47/5 and 42/5. Eliminating **any one** of invoice manufacturing savings, usable field-learning rights, or access-driven B demand restores factory as winner. Each is an assumption about a distinct economic link. A positive policy benchmark transfer cannot by itself calibrate qualification cost, customer willingness to pay or supplier invoice reductions.

## Accounting and counterarguments

On any realized specialist sale, provider total value plus manufacturer margin equals current provider cash plus B operating profit less actual manufacturer resource cost and actual qualification resource cost. The provider's invoice cancels against supplier receipts. It is wrong to add invoice savings and manufacturing real cost savings as separate combined social benefits. Conditional on more future experience being freely usable and old policies retained, the feasible set expands; a harmful-learning theorem requires actual new costs or restrictions rather than forced replacement.

A finite exact enumerator compares retain/incumbent/specialist choices for each source. Fifteen scoped Python unittest cases passed, plus ten evidence-schema/identity checks. Checks include analytic boundaries, source cash derivation, all three ablations, nonnegative payer cash, supplier conservation, free-rights monotonicity, demand participation/saturation, and exact deterministic JSON regeneration. Fresh historical repository CI and independent referee review were not performed.

Known omissions: simultaneous mixed portfolios, time to build, field-learning uncertainty, contingent renegotiation, strategic demand competition, risk pricing, warranty/support tails, physical safety qualification constraints, supplier margin on alternatives, and endogenous selection/production of source experience. Results are synthetic conditional models; novelty against existing contracting and learning-by-doing prior art remains unselected.

## Evidence and measurement design

Primary source case A: [Jabil/Apptronik, February 25 2025](https://www.jabil.com/news/apptronik-jabil-collaborate.html) announces Jabil as manufacturer and factory-pilot test site, with Apollo units validated during manufacturing. This connects *organizational roles*, not measured production savings.

Primary source case B: [Apptronik Robot Park, June 30 2026](https://apptronik.com/news-collection/welcome-to-robot-park-where-apptroniks-apollo-goes-to-work) describes real-world training data gathered at dedicated and customer/partner sites. Actual task-to-task qualification savings, customer rights, adaptation and commercial payoffs are not published in the inspected release.

Primary source case C: [DHL/Boston Dynamics 2022 agreement](https://www.dhl.com/us-en/home/press/press-archive/2022/dhl-supply-chain-to-invest-usd15-million-to-further-automate-warehousing-via-boston-dynamics-collaboration.html), [2023 Stretch first commercial unloading](https://www.dhl.com/us-en/home/press/press-archive/2023/dhl-supply-chain-achieves-first-commercial-deployment-of-boston-dynamics-stretch-robot.html), and [May 13 2025 MOU](https://group.dhl.com/en/media-relations/press-releases/2025/dhl-group-signs-mou-with-boston-dynamics-and-accelerates-cross-business-automation-strategy.html) evidence customer deployment, operational feedback and a contemplated >1,000-unit follow-on/case-picking ambition. The MOU is not proof of delivery or paid receivables. A separate [DHL integration release](https://group.dhl.com/en/media-relations/press-releases/2026/dhl-supply-chain-accelerates-automation-deployments-with-stv-robotics-softbot-platform.html) bears a March 17, **2025** page date despite a 2026 URL path, and describes digital coordination, not field-to-qualification transfer.

DHL's May 2025 release uses an 'up to 700 cases/hour' throughput measure, while its [FY2025 annual report](https://reporting-hub.group.dhl.com/2025-fy/en/) mentions 'up to 500 cases/hour.' They cannot be subtracted to infer productivity changes without comparable tasks, deployment contexts, definitions and vintages.

The evidence ledger records source-reported links, hypothesized links and absent coefficient values separately. These cases are distinct enterprises and not a matched joint panel.

A discriminating test needs (manufacturer, BOM/configuration, actual build cohort, supplier contract, source/target task, customer site, service acceptance protocol, decision date). Observe supplier real costs versus invoice pass-through (kappa), comparable target qualification effort with vs without source experience and explicit data rights (delta), and qualified customer opportunities and signed receipts versus alternatives (zeta). Record rejected as well as funded projects, loan terms and contemporaneous capital. Confounders include contemporaneous embodiment redesign, customer selection, site difficulty, integration upgrades, and final-market growth. Public releases cannot identify the three effects.

**Next substantive question:** obtain at least one matched source-to-target physical-workflow contrast (e.g. DHL unloading versus planned case picking), integrate the three-gate mechanism into the central paper, and test whether competent contracts or development delays eliminate it. Do not create another generic synthetic learning stock without corresponding evidence.
