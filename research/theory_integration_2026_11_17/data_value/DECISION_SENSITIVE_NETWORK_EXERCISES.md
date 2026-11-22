# Exercises — decision-sensitive dynamic production model

**Student version; do not read the separate solutions before attempting.** Use [the formal chapter](DECISION_SENSITIVE_NETWORK_PRODUCTION.md). All prices are hypothetical normalized net accepted-paid contributions.

1. Starting from the reference Bellman equation, derive the finite-horizon exact policy-specific signed residual/opportunity-gap identity for a full-history lawful policy. Explain why evaluating the residual only under the old logged R policy is insufficient to bound the true optimal value of SG.
2. In a two-date program, old A is always offered tomorrow at price 1, new C has price 2, and an outage prevents every date-2 service. B now earns 3/4, A now earns 1. With Pr(Q_C)=5/8, Pr(H)=1/4 and j=Pr(Q_C,H), derive exact J_B, J_A and J_P*. Find the *different* boundaries for comparing P against independent E=33/16 and for dispatching B instead of A.
3. Under fixed per-customer values but endogenous original A orders, expand the exact expected date-2 one-slot revenue into joint event probabilities for O_A, Q_C, O_C and H. Give one reason these moments cannot be recovered from a dataset of only robot-served completed tasks.
4. A reference kernel puts all mass on Q_C=0,H=1; a true kernel puts all mass on Q_C=1,H=1. Compute the TV distance and the date-2 paid production difference. State precisely why the same comparison need not be economically null when there is a later date after recovery.
5. Suppose an investigator has conditional residual bounds for every *logged* reference-policy action, but not for alternative legal learned C actions. Can this certify SG<E? State a sufficient additional support condition or an opportunity-ceiling alternative without assuming missing actions are forbidden.
