# Source data as information versus admitted capability: a controlled production-value comparison

**19 November 2026 UTC.** This chapter continues *When Capabilities Become Production* and the November 22 four-estimand synthesis, not a new numbered problem or claim of independently novel causal inference. All prices, controller payoffs, signal accuracies, and approvals in the worked example are **synthetic**; there was no robot training, customer experiment or deployment authorization.

## The missing distinction in the source-to-production chain

The existing source-regime experiment identifies the economic value of a *complete adaptive policy* when approved whole-network randomization and support hold. It cannot by itself determine whether valuable source data (i) **tell management which already-qualified continuation to choose**, (ii) **alter a controller's qualified target competence**, or (iii) **change which original customer orders, target states and failures arise**. These are different interventions. A source trajectory copied from routine customer service may inform a shadow diagnostic without changing actuation; training on it may alter physical action, joint qualification and policy-induced occupancy. Neither improvement is a dataset price. Both enter the same optimized accepted-service production objective `V(Q;omega)` and dynamic value `J`.

The useful conceptual correction is to compare **disclosure of an independently validated signal** against **admission of a source-trained controller or alternative qualified embodiment** with one fixed pre-source customer-order universe. A four-arm physical experiment is only a *conditional design*: unapproved continuations cannot be valued as if deployable. Source data from field trajectories, failures/recovery, teleoperation, deliberate probing, simulation, synthetic generation and public/pretraining retain different provenance, rights, training effects and sensor/report support.

## Controlled finite environment

Let `z` be a pre-source latent customer/production opportunity, distributed `p(z)`. Let `c=0` retain a certified incumbent controller and `c=1` admit a separately approved learned controller, or a specifically identified changed-body service menu. For each allowed post-report complete policy `a in M_c`, `y_c(a,z)` is **net captured contribution over the entire remaining customer-network horizon**, computed through qualified `V(Q;omega)`. The definition includes original orders (served, rejected, displaced or expired), shared operators/dispatch, commercial demand, outside providers, recovery and real resources; it is not an independent robotics benchmark score. A qualified incumbent or credible specialist remains in `M_c`.

A validated pre-choice signal `s` has conditional kernel `K(s|z)`; withholding it means the planner sees only the prior. First hold this **same kernel** fixed across `c`, and require that *disclosure alone* changes neither physical service, customer choices nor allowed actions except through the chosen continuation policy. The planner may ignore the signal. For an uninformative report `i=0` and disclosed report `i=1`, define the gross policy values

```
W(c,0) = max_{a in M_c} sum_z p(z) y_c(a,z)
W(c,1) = sum_s P(s) max_{a in M_c} sum_z p(z|s) y_c(a,z).
```

These are conditional expected **complete-production** values, including optimal stage-two selection. They exclude only explicitly itemized first-stage costs `k_c` of making `c=1` available and `k_i` of generating/validating/disclosing `s`; deduct those costs **once**, not again as a fictitious data premium. With source-sensitive report generation `K_c`, use `W(c,i;K_c)` and do **not** call the cross-`c` difference a controlled identical-information mechanism.

**Proposition (optional information and admission interaction).** For each fixed `c`, if the more informative signal Blackwell-dominates the weaker one, the same qualified action menu remains feasible, and observing/reporting it is noninvasive, then `I_c = W(c,1)-W(c,0) >= 0` before real report costs. An admissible policy seeing the richer signal can garble/ignore it and reproduce any weaker-signal decision rule. Let `C_i=W(1,i)-W(0,i)`. Then the exact cross-difference is

```
Delta = W(1,1)-W(1,0)-W(0,1)+W(0,0) = I_1-I_0 = C_1-C_0.
```

The **sign of Delta is unrestricted**. A learned controller can substitute for information by making a formerly risky target policy robust, or complement information by making a state-contingent customer recipe worthwhile only when a reliable diagnostic selects it. The statement requires **no** positive additive transfer coefficient, independent qualifications or automatic data-to-dollars map. If the learned controller is *optional* and retaining `c=0` is free and feasible under the expanded menu, optimized value cannot fall merely from its availability; a comparison of forced `c=1` may fall after costs or changed resources. Invasive observation, changed K, safety-forced responses or nonretained policies break the relevant monotonicity conditions.

This is established Blackwell decision theory and the finite factorial identity—not a new information-theoretic theorem. It is useful here because the outcome is **qualified full-network economic production**, not technical score, and the two independently controllable interventions specify an actual identification target.

## Constructive complement and substitute worlds with a competent alternative

Consider equally likely economically relevant high and low customer states. An independently qualified specialist `S` produces **3/4** normalized net contribution in either state; a retained safe fallback `F` produces zero. Existing approved continuation G produces **(3,-1)**; the negative number is opportunity displacement and operational cost, **not an unsafe unapproved maneuver**. An approved alternative target continuation T initially produces **(0,-6)**. A symmetric report identifies the economically relevant state correctly with probability `q in [1/2,1]`. Every post-report action remains in the same approved menu `{F,S,G,T}` in this illustration.

Under `c=0` without a report, G yields 1, above S=3/4, so `W(0,0)=1`. With perfect disclosure, choose G when high and S when low: `W(0,1)=15/8`, information value `7/8`.

Two technically different learnings produce opposite interactions:

| Controller intervention | High,low G | High,low T | `W(1,0)` | `W(1,1)` | `Delta` |
| --- | --- | --- | ---: | ---: | ---: |
| **Substitute:** learning repairs low-state G cost | (3,1) | (0,-6) | 2 | 2 | **-7/8** |
| **Complement:** learning unlocks high-state T | (3,-1) | (4,-6) | 1 | 19/8 | **+1/2** |

In the substitute world G is now economically preferable regardless of the report: the best information can do is reveal a decision already made. In the complement world T remains unattractive when states are pooled (its unconditional payoff is -1), but it overtakes G after a sufficiently precise **high** report. The positive interaction comes from an *action-switching boundary*, not an imposed positive `x*g` term. T's source-trained capability must be independently qualified in the high-state complete customer service before any real admission; the synthetic table does not certify it.

For report accuracy `q`, conditional posterior under a positive signal equals `q`. G beats specialist S if posterior high exceeds `7/16`. For `q >= 1/2` the baseline report policy has gross value

```
W(0,q) = 1                    if 1/2 <= q <= 9/16
       = 2q - 1/8            if 9/16 < q <= 1.
```

In the complement world T overtakes G on the positive report only once `q > 5/6` (because `10q-6 > 4q-1`). Thus

```
W(1,q) = 1                    if 1/2 <= q <= 9/16
       = 2q - 1/8            if 9/16 < q <= 5/6
       = 5q - 21/8           if 5/6 < q <= 1.
```

The interaction is zero until the high-report posterior crosses `5/6`, and then equals `3q-5/2`. This illustrates **endogenous complementarity from economically optimized policy choice**, including a certified specialist baseline, even when raw sensor accuracy grows smoothly.

With illustrative *additional* source-training/qualification expense `k_c=3/10` and separately incremental signal acquisition/validation expense `k_i=9/10`, the complement world yields these complete net choices at `q=1`: retain=1; disclosure only=`39/40`; trained controller only=`7/10`; **both=`47/40`**. Neither paid investment alone beats retained production, but their combined accepted service wins by `7/40`. The combination breaks even with retaining production only if `q>193/200` in this specific payoff/cost example; less well-grounded diagnostic claims cannot justify the paired acquisition. No number is a field estimate, wage-equivalent service dollar, observed qualification pass rate or actual price.

**Important separation:** the example keeps the signal acquisition channel independent of current production. When field source learning changes which customer states are visited, report kernels, qualified actions or demand, the four `W` arms are *different complete policies* but a simple controlled "information effect" is not identified without freezing or separately measuring that mechanism. Existing policy-induced support and same-world bounds apply. A signal can be predictive yet economically worthless if a competent specialist dominates every allowed alternative in every state.

## Identification, support and competing production policies

A physically approved policy-closed whole-network experiment can randomize independently (a) frozen incumbent vs separately qualified learned controller **admission** and (b) a nonactuating validated report **withheld vs displayed**, provided both are compatible, pre-source order denominators and market populations are fixed, source rights are cleared, and learning, dispatch, operators and customer demand are not shared across nominal units. Then arm means identify the *controlled policy interaction* `Delta` directly, without identifying individual cross-controller qualification overlap. Stage-two action randomization plus target-state joint qualification tests are needed to interpret the mechanism, not merely to measure its economic mean. Use independent networks or valid interference-aware designs; robot-level A/B tests sharing one dispatcher do not qualify.

If a cell lacks physically approved action support, it is **not a policy arm**. If it is approved but unobserved, bounds `L_{11} <= W(1,1) <= U_{11}` imply the outer interaction interval `[L_{11}-W(1,0)-W(0,1)+W(0,0), U_{11}-W(1,0)-W(0,1)+W(0,0)]`; common hidden market regimes can tighten it. These are missing-support results, not permission to conduct unsafe exploration. Cross-source report generation that changes `K`, post-treatment conditioning on failures and unmeasured customer-order displacement defeat a causal "capability-versus-information" label even if a four-arm *average policy* interaction is identified.

Empirically discriminating records: frozen data snapshot/provenance by source modality; signed actuation and nonactuating/report separation; source and policy hashes, diagnostic confusion **by original customer opportunity and support stratum**, joint complete target qualification (not separate marginals), original accepted/failed/reassigned/unattempted order panel, qualified specialist, operator recovery and shared dispatch loads, resource and cost ledger, and independent approved network assignment. The signal's commercial-state accuracy cannot be borrowed from an offline imitation benchmark. The technology choice remains more source observations vs target grounding vs different embodiment under the same whole-horizon `J` and resource opportunity cost.

## Prior-art boundary and implications for November 22

Blackwell, *Equivalent Comparisons of Experiments*, **Annals of Mathematical Statistics** 24(2):265–272 (1953), DOI https://doi.org/10.1214/aoms/1177729032, supplies information ordering (publisher bibliographic metadata verified 19 Nov 2026). Murphy, *Optimal Dynamic Treatment Regimes*, JRSS B 65(2):331–355 (2003), DOI https://doi.org/10.1111/1467-9868.00389, supplies stagewise decision rules; Stensrud et al., *Separable Effects for Causal Inference in the Presence of Competing Events*, JASA, DOI https://doi.org/10.1080/01621459.2020.1765783, demonstrates that treatment-component separation needs distinct interventions and causal assumptions in a *different medical setting*. The source comparison here is not a claim to reproduce their competing-event theorem. DDA https://arxiv.org/abs/2606.10127 already models production as a data source and future data value; Appendix B covers complementarity. No independent scientific novelty review has been completed.

The November 22 synthesis should now distinguish five layers: source/provenance, **information report**, controller/embodiment **qualification**, jointly accepted customer service, and dynamic customer demand/resource/cash feedback. The algebra and synthetic examples do not pass the science gate. The next proof/evidence question remains whether a **versioned, independently approved controller/report intervention** can preserve customer/dispatcher/operator separation and identify `y_c(a,z)` from original-order complete production, or whether only partial support is defensible. Theory remains the main workstream through December 6; December 25 23:59 Eastern remains the final target.
