# Contracting can remove a payment bottleneck; incentives can restore one

Theory continuation, November 16, 2026 UTC. This audits the strongest alternative to the exogenous payment permissions in the [qualification model](qualification_finance.md). The results below are standard contracting/financing mechanisms and conditional illustrations. They do not establish novelty, robotics calibration, or a case for common ownership.

## Benchmark: separate firms can implement pooling

Consider one deterministic complete service with payer cash b_i>=0, prerequisites k_i>=0 and total later operating profit V>=0, already net of operating and terminal obligations. Let B=sum b_i and K=sum k_i. Interest and discounting are zero. No outside credit is available. All payers can make enforceable early transfers and assign future profit shares without contracting costs. Qualification, contributions and outcome are verifiable; there are no hidden actions. Each payer can instead retain its own cash, and unused cash remains owned by it. No extra strategic premium is added to V.

There is an individually rational contract implementing the service if and only if B>=K and V>=K. The first condition is the initial funding requirement. The second is necessary because aggregate terminal cash B-K+V must cover all outside options B.

For sufficiency choose contributions c_i in [0,b_i] totaling K. Complete early-transfer permissions route those contributions to the legal payers of k_i. Choose nonnegative future shares r_i totaling V with r_i>=c_i; this is possible because V>=K. Payer i finishes with b_i-c_i+r_i>=b_i. Thus legal separation by itself does not defeat pooling. The proof characterizes feasible agreements, not a unique bargaining equilibrium or a prediction about observed contract prices.

In the original example, H has cash (5,1), prerequisites (2,2) and V=10. A one-unit early transfer from provider to operator makes contributions (3,1). Equal future shares (5,5) produce terminal balances (7,5), exceeding both outside options. Total value is 12, compared with 10 for L's cash (2,2) and the same bundle/profit. H regains its ranking. The earlier reversal therefore needs an actual restriction beyond legal separation. If future shares cannot be reassigned, qualification is unverifiable, cash is restricted, or transfers/commitments have costs, this sufficiency construction need not apply.

## Primary financing source: Holmström–Tirole (1997)

Bengt Holmström and Jean Tirole, **Financial Intermediation, Loanable Funds, and the Real Sector**, *Quarterly Journal of Economics* 112(3), August 1997, pp.663–691, DOI [10.1162/003355397555316](https://doi.org/10.1162/003355397555316). Inspected university-hosted [published PDF](https://web.stanford.edu/~piazzesi/Reading/Holmstrom%26Tirole%20QJE%201997.pdf), retrieved November 16, 2026 UTC, SHA-256 `b37f22b446712f9fb961cc7f519673d838cb57011863b0df0519cffd2c39933c`. Read §II and §III.1, especially printed pp.667–671. The monitored-intermediary equilibrium and comparative statics are not replicated here.

**Mechanism card.** A risk-neutral entrepreneur has own assets A and a project costing I>A now. Verifiable future revenue is R on success and zero on failure. High effort succeeds with probability p_H; shirking succeeds with p_L<p_H and supplies a private benefit B_private. Actions are not contractible, investors require expected gross return g, and limited liability prevents negative terminal payments. The source assumes the high-effort project is economically viable and the low-effort project, including its private benefit, is not. Here B_private is deliberately distinguished from aggregate cash B in the preceding benchmark.

If the entrepreneur receives R_f on success, effort requires (p_H-p_L)*R_f>=B_private. Investors therefore cannot be promised more than

P = p_H*[R-B_private/(p_H-p_L)]

in expected repayment while inducing effort. Direct financing is feasible exactly when g*(I-A)<=P under the source's assumptions and admissible nonnegative shares. This is the authors' incentive constraint and direct-finance threshold, not our discovery. An inability to pledge all future value can prevent an otherwise positive-surplus project from borrowing. A gratuitous initial transfer does not automatically solve this: the donor must also receive an acceptable incentive-compatible return.

### A conditional performance/pledgeability reversal

Holding R and B_private fixed, let a technology change raise both effort-dependent success probabilities. Higher p_H alone does not guarantee higher pledgeable income if the effort gap shrinks. For differentiable primitives and Delta=p_H-p_L>0,

P' = p_H'*(R-B_private/Delta) + p_H*R' - p_H*B_private'/Delta + p_H*B_private*Delta'/Delta^2.

With a nonnegative pledgeable residual, p_H'>=0, R'>=0, B_private'<=0 and Delta'>=0 imply P'>=0. The last term can reverse that implication when Delta'<0. This is an elementary comparative static of the source formula, not a new financing theorem. It compares technologies; it does not equate Bayesian information with a change in physical success probabilities.

An exact synthetic pair uses R=10, B_private=1, I=15/2, A=3/2 and g=1. Technology A has (p_H,p_L)=(4/5,2/5). High-effort expected revenue is 8 and pledgeable income 6, exactly the external requirement I-A. Technology B has (9/10,16/25). High-effort expected revenue rises to 9, but pledgeable income falls to 72/13<6, so it cannot obtain the same direct financing. Both pairs satisfy the source viability restriction: low-effort expected revenue plus private benefit is respectively 5 and 37/5, each below I=15/2, while high-effort expected revenue exceeds I. This check matters: otherwise financing a low-effort project could invalidate the claimed comparison.

The possible robotics interpretation is an improvement that makes unattended operation more successful while reducing the incremental contribution of costly diligence. That interpretation remains a hypothesis; no inspected robotics source measures these probabilities or private benefits. A firm able to retain Technology A still has that option, so this example **does not** refute optional-policy monotonicity or show that more free data lowers its optimized value.

Nor can P be copied onto every edge of a payment graph. It is an aggregate claim capacity for a particular incentive problem. Multiple lenders cannot each pledge the same future receipts independently. Introducing it into the research kernel requires specifying who controls effort, who holds claims, observability, success-state customer receipts, and all repayments consistently.

## Closest dynamic source: Bergemann–Hege (2005)

Dirk Bergemann and Ulrich Hege, **The Financing of Innovation: Learning and Stopping**, *RAND Journal of Economics* 36(4), Winter 2005, pp.719–752. Inspected the [Yale-hosted published reprint](https://cpb-us-w2.wpmucdn.com/campuspress.yale.edu/dist/3/352/files/2011/01/Paper13_p1176.pdf), retrieved November 16, 2026 UTC, SHA-256 `22cde8eb4dd4c67605e61020c098c6f1a40707358f1ae045092fd3a3fc1541d8`. Its outer Cowles paper cover says 2006; the article itself is Winter 2005. The separate October 2004 discussion paper found in search is not silently substituted for this version.

Inspected the introduction and model/first-best/two-period sections, printed pp.719–727. OCR assisted reading; pp.719 and 724–726 were visually checked, including equations (1)–(5). The later infinite-horizon relationship versus arm's-length equilibrium and proofs are **not** reconstructed here. Abstract claims about their relative funding paths are not accepted as our replication.

**Mechanism card.** A project is good with prior alpha and otherwise cannot succeed. Spending c*gamma in a period yields success probability gamma conditional on a good project, with gamma in [0,lambda], lambda<1. Success pays a single R and terminates the project. No success updates the belief to

alpha_next = alpha*(1-gamma)/(1-alpha*gamma).

An initially wealthless entrepreneur can invest the supplied funds or divert them to immediate private consumption. Investment is observable but not verifiable under relationship financing, unobservable under arm's-length financing. The parties cannot commit to future contracts; the entrepreneur proposes current funding and a success share. Learning here is Bayesian discovery about a fixed project's viability, unlike physically creating a better policy. Dynamic funding, experimentation and agency are therefore already prior art.

**Reconstructed first-best benchmark.** The source gives full funding gamma=lambda while alpha*R>c, with stopping boundary alpha_star=c/R (ties can be treated as indifference). Conditional on repeated failures, beliefs only fall. If alpha*R<=c, subsequent failures cannot create a positive flow return, so continuation has no beneficial information option in this benchmark. The Bellman recursion is V(alpha)=max_gamma{alpha*gamma*R-c*gamma+delta*(1-alpha*gamma)*V(alpha_next)}. The source's full-funding solution accelerates positive-value experimentation; it is not a universal rule for experiments that can deliver favorable nonterminal news or create capabilities.

A synthetic check uses alpha_0=3/4, lambda=1/2, R=10, c=4 and delta=9/10. Fund at beliefs 3/4, 3/5 and 3/7, then stop after another failure at 3/11<2/5. Backward valuation gives V=3781/1600. This checks the specified first-best path, not the contracting equilibrium or empirical R&D returns.

**Reconstructed terminal contracting wedge.** In the final period of the source's two-period model, investor participation requires alpha*(1-s)*R>=c and entrepreneur incentive compatibility requires alpha*s*R>=c. For positive funding, both can hold iff alpha*R>=2c, whereas the first-best threshold is alpha*R>=c. With R=10 and c=4, terminal contracting needs alpha>=4/5; alpha=3/4 supports a positive first-best project but no terminal financing agreement. This is the source's equations (3)–(5), not our novel result. It explains why a contingent share contract can fail without assuming that a transfer is arbitrarily prohibited.

## Consequence for the first paper

Perfect contracts defeat the payment-network reversal; agency can restore financing limits, but that explanation is familiar. Adding moral hazard and calling the project robotic would not establish novelty. The next useful problem is whether directed production-generated experience changes *both* a qualified opportunity and its pledgeable receipts in a way that gives an additional testable restriction. Keep Bayesian information, physical capability, actor cash and incentive rents separate. Do not add an elaborate agency state until that proposed restriction is explicit.

Source discovery used Exa: two targeted searches returned ten candidate entries across the two named-paper lookups, deduplicated to the two inspected primary papers plus bibliographic/version entries. Search results were not treated as checked proofs. The arithmetic is reproducible with `python scripts/check_contracting_foundations.py`.
