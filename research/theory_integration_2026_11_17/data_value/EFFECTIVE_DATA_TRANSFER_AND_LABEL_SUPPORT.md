# Source admission, archive provenance and the economics of transferable learning

20 November 2026 — integrated continuation of *When Capabilities Become Production*. The substantive question remains the source X versus target-grounding G versus new embodiment E versus retained R choice for signed original-customer production. This chapter adds a data-filter/learner-admission stage to the preceding [source-origin versus inclusion theorem](SOURCE_ORIGIN_VS_INCLUSION_SUPPORT.md). No claim of new statistical methodology, actual robot learning, customer receipts or scientific novelty.

## Which part of a proposed dataset can actually alter a qualified robot?

Let s index heterogeneous source types: production-generated trajectories, failures/recoveries, teleoperation, deliberate collection, simulation, synthetic rollouts and public/pretrained inputs. For a specified learner/task conditioning recipe, let w_s be the sampler proposal probability and r_s the probability a proposed *training unit* is admitted by its filter/decoder. With R=sum_s w_s r_s>0, its admitted source share is

    q_s = w_s r_s / R.

Define the unit at the stage where the filter operates: an individual **transition** in a loader that unbatches trajectories, not necessarily the source episode. A licensed archive can be available but contribute zero admitted language-conditioned examples, without implying that its image/action examples cannot benefit an image-goal learner. Nor does fixed source inclusion identify the value of **generating** new episodes using a different collection method.

**Conditional proposition (admission Jacobian).** If r is fixed with respect to w,

    partial q_i / partial w_s = (r_s/R) * [1{i=s} - q_i].

Let H(q;omega) be the expected net **optimized qualified original-customer production contribution** under a fixed, physically feasible deployment/embodiment/grounding menu, already accounting for scarce operator resources, original buyer demand, joint technical qualification and continuation. If H is a differentiable *assumed* reduced-form map from training mix into that value,

    partial H / partial w_s = (r_s/R) *
                    [H_s - sum_i q_i H_i],
    H_i = partial H / partial q_i.

Proof: quotient rule on q and chain rule. These are derivatives in positive unnormalized proposal weights; along the weight simplex use a sum-zero perturbation. If eligibility responds endogenously to source mix, evolving weights, preprocessing choices or target grounding, derivatives of r(w) must also enter. No mathematical identity determines H from episode counts or benchmark percentages. H is a separate technical-learning and accepted-service production response requiring matched measurement.

For two sources S,T with proposed S share w,

    qS = w*rS/[w*rS + (1-w)*rT],
    dqS/dw = rS*rT/[w*rS+(1-w)*rT]^2.

When rS,rT>0, to achieve desired admitted share p∈(0,1) choose w=(p/rS)/[(p/rS)+((1-p)/rT)]. If rS=0,rT>0, no nondegenerate proposal can yield positive admitted S share under this filter. Increasing w cannot repair that specific absent semantic/loader support. Reweighting can restore a share but not missing source contexts, labels, consent, action alignment, failure examples or the ability to execute qualified service.

**Explicit synthetic economic example, not transfer calibration.** Assume rS=1/4,rT=1 for a language-filtered two-group learner, and w=1/2. S's *admitted* share is 1/5, not 1/2. To reach admitted S share 1/2, set proposed w=4/5 if retention remains stable; extra rejected draws may add compute/curation costs. Under a deliberately stipulated complementary qualification production response H(q)=8q(1-q) normalized original-customer contribution, H(1/5)=32/25 while H(1/2)=2. A separately certified generalist E yields 3/2, so this conditional source-versus-embodiment ranking reverses. Nothing here converts robot benchmark scores into money. An actual net ranking must deduct distinct acquisition, annotation, update, rights, manufacturing and dispatch costs, and preserve feasible incumbent policies. Additional **free optional** raw data cannot lower the optimum if old policies remain nested; compulsory training, filters and fixed-budget displacement are different interventions.

## Inspecting the original Berkeley public implementation

Original [BridgeData V2 publisher](https://rail-berkeley.github.io/bridgedata/) reports 60,096 trajectories (50,365 teleoperated, 9,731 scripted pick-and-place) across 24 environments/13 skills with **CC BY 4.0 data** terms, separate from MIT source code. Its [CoRL/PMLR HTML abstract](https://proceedings.mlr.press/v229/walke23a.html) reports 53,896, an **unreconciled 6,200-count discrepancy**. Official [TFDS bridge catalog](https://github.com/tensorflow/datasets/blob/master/docs/catalog/bridge.md) lists a different processed train/test split (25,460/3,475, total 28,935) and has_language metadata. We do not infer which episodes changed, whether any were added/omitted or that the processed TFDS split corresponds to the same raw release. Code pin is not a raw zip SHA.

At pinned author [GitHub revision bc60a35b701a12021c8c95e9d8601274d3acd928](https://github.com/rail-berkeley/bridge_data_v2/commit/bc60a35b701a12021c8c95e9d8601274d3acd928):
- [Raw-to-NumPy converter](https://github.com/rail-berkeley/bridge_data_v2/blob/bc60a35b701a12021c8c95e9d8601274d3acd928/data_processing/bridgedata_raw_to_numpy.py), blob cefb75d01e64d89f981eaef400953b87dec844e0: **if lang.txt is absent, it encodes an empty language string**. It shuffles trajectories within dated collection folders before train/validation allocation and skips certain file/assertion failures. A fixed episode-level seed/split manifest is not apparent in that function; this is a potential reproducibility guard, **not proof** of author leakage or measured missing labels.
- [TFRecord converter](https://github.com/rail-berkeley/bridge_data_v2/blob/bc60a35b701a12021c8c95e9d8601274d3acd928/data_processing/bridgedata_numpy_to_tfrecord.py), blob 942b781da57eeffdc77572a170a0b663b9767282, serializes the language field, including empty fallback.
- [BridgeDataset loader](https://github.com/rail-berkeley/bridge_data_v2/blob/bc60a35b701a12021c8c95e9d8601274d3acd928/jaxrl_m/data/bridge_dataset.py), blob b7530beea77bd768cb52fb46382e590fcdfbcb2b, defaults to load_language=False and skip_unlabeled=False. When deliberately configured to filter on nonempty goals.language, it does so **after** sampling from source subdatasets and after unbatching trajectories. Thus r_s applies to the filtered training unit, not automatically to the fraction of episodes with language text. This filter is **not universally active**.
- [All-source configuration](https://github.com/rail-berkeley/bridge_data_v2/blob/bc60a35b701a12021c8c95e9d8601274d3acd928/experiments/configs/data_config.py), blob 8a1a10fb56cd2433850bf4316ce8ca0c20084bf7, groups scripted and other globs in a shared include list. Our equal-proposal example does **not** describe the actual authors' sampler.
- [Public issue #39](https://github.com/rail-berkeley/bridge_data_v2/issues/39), opened Feb 11, 2025, contains a user report of a scripted download lacking lang.txt. It is not independently verified raw-episode evidence.

## Causal and economic acceptance

Fixed lawful **archive inclusion** versus no inclusion on randomized *whole connected learner-update networks*, with all failed development attempts retained and common untouched heldout **joint target qualification**, can identify the intention-to-train effect of the specified complete learning recipes. Such cross-task transfer can be measured on a task not present in scripted training. It does not identify an equal-admitted-mixture effect without measured filtering and controlled compute. A feasible inclusion × goal-image/language-condition experiment would be a comparison of **entire learner recipes**, not automatically pure semantic-label mediation; if an arm has zero admitted source support it cannot be repaired statistically.

The acquisition choice for *new* teleoperation/scripted/simulation data needs separate source-context generator feasibility and randomization, rights, actual errors and costs. Any empirical **economic** data value then needs safely certified, actually assigned whole controller/embodiment/operator policies, report timing, original unchanged customer offer/refusal/completion/paid receipts, retained R alternative and resource costs. No downloaded episode, trained weights, signed field policy, customer payment, numeric official BEA interindustry transaction or external novelty review was obtained. Keep DDA §5 and Appendix B (future-data value and complementary aggregation), the multilinear qualification map and resource-price certificates as prior foundations, not new discoveries. Nov22 Models A–B scientific gate stays OPEN; Nov29 quantitative backbone and Dec6 contribution choice remain open; Dec25 2026 23:59 America/New_York unchanged.
