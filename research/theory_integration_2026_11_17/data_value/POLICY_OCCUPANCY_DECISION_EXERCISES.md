# Student exercises — dynamic buyer-data decision sufficiency

All cash-contribution units in the [chapter](POLICY_OCCUPANCY_DECISION_SUFFICIENCY.md) are **synthetic**; do not infer robotics productivity.

1. **Telescoping.** For a finite horizon with a full-information V* and any legal report-blind policy μ, derive the expectation identity for \(\sum_t(V_t^*-Q_t^*)\) and identify which policy generates the occupancy measure. Explain why an average under only the retained R logging controller is generally invalid.
2. **Different meanings of "sufficient".** Explain why two histories with unequal return kernels for an unchosen action may still admit zero compression loss. Construct a two-stage example where an action-optimal common first move nevertheless produces positive second-stage regret if a later licensed report is hidden.
3. **Model A/B toy calculation.** For A/B equally likely, accepted pilot=1/5, retained a paid only for A, source-learned b paid only for B, embodiment e paid 3/4 under either, and pilot G_info revealing the buyer only in SG, compute R, S, G, SG and E full and report-blind values. Deduct SG cost 1/5 and E cost 1/20 and rank the two alternatives.
4. **Identified signs.** Starting from coarse SG-E=-2/5 and bounds \(0\le R_{SG}\le1/2,\ R_E=0\), derive the investment identified outer interval. State what action-relative full-Q and policy occupancy evidence would be needed for a strict sign.
5. **Data and legal counterfactuals.** Explain what changes if the B-serving b controller is not yet physically approved, if G_info merely improves a benchmark rather than revealing the buyer, or if pilot-induced data changes future customer orders. Distinguish optional free data from forced re-training.
