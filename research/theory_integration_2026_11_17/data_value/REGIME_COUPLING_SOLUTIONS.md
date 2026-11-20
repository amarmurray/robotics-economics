# Instructor solutions — regime-conditioned data value

Separate from the [student problems](REGIME_COUPLING_EXERCISES.md). All results refer only to the synthetic complete-policy model.

1. **Regime coupling:** x≤π and x≤q since it is an intersection; θ=A outside Q11 has mass π−x≤1−q, so x≥π+q−1, while x≥0. Thus x∈[max(0,π+q−1),min(π,q)]. Allocate x of the θ=A mass to Q11 and the remaining π−x among Q10/Q01/Q00 up to their aggregate 1−q; allocate θ=B as each cell's residual. This construction works at either endpoint and every interior point.

2. **Embodiment lock:** Set d_A=x−(1−α)q and d_B=x−αq. F's Q11 baseline uplift is 2(|d_A|+|d_B|). L's is 2 max{(d_A)_++(d_B)_+,(−d_A)_++(−d_B)_+}. Their difference equals [(2α−1)q−2|x−q/2|]_+. When q>0 and x is sufficiently far from q/2, both post-report posterior signs agree and no contingent body switch helps, even though Y has nonzero marginal accuracy.

3. **Measurement:** m=(1−α)q+(2α−1)x. Balanced: m=(1/4)(2/5)+(1/2)(1/5)=1/5. Skewed: m=1/10+(1/2)(7/20)=11/40. Inversion requires α>1/2, same eligible Q11 population, independently stable/calibrated conditional kernel, no selective report omission and no menu response induced by measurement. It identifies the *coupling*, not paid contribution nor physical permission.

4. **Sharp envelope:** At q=2/5, x∈[0,2/5], D∈[0,1/5]; at q=4/5, x∈[3/10,1/2], D∈[1/5,2/5]. Against incremental cost 3/20, first case is **unranked** (some feasible worlds below/above cost), second is robustly positive **conditional on the stipulated physical and buyer assumptions**. Neither establishes a field investment ranking.

5. **Unsupported original service:** Let μ vary in a supported convex joint history/regime polytope C and allowed f range over full physically signed contingent cluster policies. For fixed buyer contribution r, W(μ)=max_f L_f(μ). Compute inf_C W using epigraph linear constraints t≥L_f(μ); compute sup_C W as max_f sup_C L_f(μ). If admissible original-market contribution entries r are unknown, use an explicitly justified jointly attainable payoff uncertainty set; for a truly rectangular interval, lower/upper r endpoints suffice. No technical qualification makes a policy safe, and physical approval alone supplies neither full-parent causal overlap nor market receipt rows. Do not assign unsigned X to production or convert benchmark percentages directly into revenue.
