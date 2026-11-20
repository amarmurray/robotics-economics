# Shared learners, source exposure, and qualified economic production

**20 November 2026.** The same November 22 original-buyer Models A–B gate of *When Capabilities Become Production*. A continuation of [sequential source-policy identification](SOURCE_POLICY_SEQUENTIAL_IDENTIFICATION.md), not a detached question or claim of novelty. No robot, buyer or model was operated or trained in this research tranche.

## 1. Which intervention actually produces the data value?

Retain the common economic objective \(J(\pi)=E[\sum_t\beta^t(\text{captured paid contribution}_t-\text{all development, rights, production, displaced-service and operator costs}_t)]\). A complete policy \(\pi\) includes acquisition, compute and curation, signed controller and embodiment, original customer menus and acceptance, shared physical/human resources, qualified services, failures, preattempt safe fallback, and future policy-generated data. Its continuation value already contains future learning. There is no second premium added for data.

A source assignment on robot 1 can change the weights later used on robot 2. Both can require the same operator and customer demand can be for an inseparable bundle. Therefore the correct causal unit is at least the **connected learner-update, robot, human-operator and customer-order network**, rather than two nominal independent robot identities. Let \(s_i\in\{X,G\}\) be source-program X or target-grounding G in two acquisition slots, and \(U(s_1,s_2)\) the shared training/update rule. Define \(J(s_1,s_2)\) as the complete original-network net contribution of the resulting admitted policy, rather than a benchmark transfer score. Field, failure/recovery, teleoperation, simulator, synthetic and public/pretrained X inputs remain distinct versions whose rights and causal effects must be separately established.

Define the conditional source effect \(\Delta_X(G)=J(X,G)-J(G,G)\), \(\Delta_X(X)=J(X,X)-J(G,X)\), and complete-policy interaction
\[
\Gamma=J(X,X)-J(X,G)-J(G,X)+J(G,G).
\]
This factorial interaction combines learning, qualification, buyer willingness to purchase, resources and known costs. It is **not** automatically a neural transfer coefficient.

## 2. Positive source marginals do not imply all-X support — proposition and proof

Suppose the fully logged training-program distribution is \(P(GG)=1/2\), \(P(XG)=P(GX)=1/4\), and \(P(XX)=0\). Each source slot sees X with probability 1/4, and both mixed treatments and GG have known randomized assignments. Let signed-policy net captured contribution on every **observed** original buyer/robot/operator history be \(J(GG)=6\) and \(J(XG)=J(GX)=5\). The logged law and its expected contribution \(11/2\) are the same in two hypothetical worlds:

| Net contribution | World L | World H |
| --- | ---: | ---: |
| GG | 6 | 6 |
| XG or GX | 5 | 5 |
| Unlogged but hypothetically signed XX | 3 | 8 |
| \(\Gamma\) | −1 | 4 |
| \(J(XX)-J(GG)\) | −3 | 2 |
| \(\Delta_X(X)\) | −2 | 3 |

Both worlds have identical records of source assignments, observed technical qualification, buyer offer version and paid outcomes for all supported arms; all *unsupported* XX potential outcomes can differ. Thus the sign of economic interaction, and whether more X source data defeats G, reverse without any possible statistical distinction from the logger. The observed marginal \(\Delta_X(G)=5-6=-1\) is identical. Since the two complete-world laws agree on every observable event, **no estimator can point-identify XX's value from these data alone**. This is a standard observational-equivalence proof, not a new causal theorem. Sampling more supported GG/XG/GX histories does not repair missing XX exposure.

A consistent synthetic production accounting is two original customer-service orders with gross captured contribution ceilings 4 and 5, two operator slots, and development cost 1: GG gross7, either mixed gross6, XX gross4 or9. Hypothetically certified E yields net6, and incumbent R has net2. The construction does not map technical pass rates to money. Binary qualification may be identical while paid service volume, operator burden or customer purchase differs.

## 3. Physical admission versus statistical support

**Unsigned XX:** its controller/body/operator state is not physically admissible. An economic hypothetical cannot authorize deployment or be ranked as a live option. An offline, licensed, fixed-hardware source comparison may be possible, but does not measure original paid XX service.

**Signed XX with zero joint assignment propensity:** the policy is feasible but *not statistically identified* under this logging design. Per-slot positivity gives no valid reciprocal weight for a zero-probability whole-network exposure. Under a real complete-network deployment randomization to all signed arms, the previous sequential/whole-policy results apply with stable assignment versions and interference closure.

A conservative conditional bound is available if actual service-price/capacity certificates limit *gross* original-network contribution by U, trained-policy cost c is known, and the independently signed incumbent R is a feasible **after-cost, preattempt fallback** with no missing resource displacement:
\[
J(XX)\in[J(R)-c,U-c].
\]
For the synthetic gross ceiling U=4+5=9, c=1 and R=2, the interval is [1,8]. Consequently \(\Gamma\in[-3,4]\) and XX minus GG lies in [−5,2]. For this deliberately unrestricted unobserved XX cell, the bounds are sharp: all eight integer completions, as well as continuous values between endpoints if permitted, are observationally equivalent. An unsigned controller has no implementable policy value regardless of these bounds. If incumbent R is not physically retainable after training, or there are additional opportunity costs, the stated lower bound fails. No **real** resource-price certificate or customer receipt has been produced here.

Do not interpret World L's relatively poor **forced, costly** XX program as proving that freely available optional X data has negative optimal value. If extra lawful X data is costless to receive and the previous weights, license rights and R/GG policy remain genuinely feasible, the expanded policy set contains the old one; maximizing over a superset cannot reduce J. Forced retraining, compute crowdout, licensing conflict and irreversible updates remove that set inclusion.

## 4. Network-closed randomized policy evaluation — proposition

Let \(c=1,...,N\) index disjoint **update-connected** original customer–learner–robot–operator clusters with genuinely no shared controller updates, learning input, operators or interference across clusters. Randomly assign each whole cluster a fully signed development/deployment policy \(a\) at known \(p_c(a)>0\), preserving prelisted buyer cohorts, exact commercial version, service refusal/unattempted orders, successful work, actual collected receipts and complete costs. Consistency and no cross-cluster interference then give the usual Horvitz–Thompson identity
\[
E\left[\frac{1}{N}\sum_{c=1}^N\frac{1\{A_c=a\}W_c}{p_c(a)}\right]=\frac1N\sum_{c=1}^N W_c(a).
\]
Proof: apply randomization expectation to each summand, then linearity. Under four-arm signed factorial GG/XG/GX/XX assignment, a full-network intervention contrast identifies the **total policy** source interaction, not isolated modality transfer. Adequate independent cluster count and appropriate variance estimation remain necessary. Sequential adaptivity is permitted only with positive propensity for the entire *observed history including learner-update version*, per the prior theorem.

Shared weights flowing between treatment and control invalidate the network boundary. If a company has one mutable global model, the meaningful cluster might be its entire company fleet; calling each robot an independent randomized unit is pseudoreplication. Time-crossover experiments require independent resetting/transport assumptions for controller memory and changing customer demand. If an external-interference envelope \(|W_c(\mathbf A)-W_c^0(A_c)|\le\epsilon_c\) were separately validated, the mean policy-evaluation error would be at most \(N^{-1}\sum_c\epsilon_c\) by the triangle inequality. No such envelope has been measured.

## 5. Mechanism attribution and original customer production remain separate

A whole-policy source portfolio trial may rank X versus G versus E without identifying every latent source-qualification–demand–report interaction, as the preceding sequential theorem establishes. **But it cannot attribute the contrast to teleoperation, recovery data, simulation or pretraining** if source mixes, hardware, rights and compute co-vary. A separate, matched causal technical experiment must hold starting model, embodiment/firmware, compute, curation, license permissions and accepted-service evaluation recipe constant. It should measure joint Q and target report/demand correlations, source-conditioned technical transfer, failed attempts and physical compatibility. It must not presume technical benchmark percentages are revenue.

The economic channel requires linked natural original-buyer offered/refused/unserved orders, independent qualification and safety signatures, jointly feasible operator allocation, accepted delivery and **paid receipts**, not RLDS episode reward or invoice face value. A purchased bundle can create positive *economic* complementarity even with technically additive source effects; an improved Q can be economically worthless if a market fails to purchase or a shared operator cannot deploy. Retain the existing D1/D2 mechanism decomposition, process complementarity, resource dual prices, dynamic data/teleoperation and embodiment-option results; do not add a separate data price to J.

## 6. Closest prior art and empirical discrimination

These mathematical tools are established: Aronow and Samii (2017), *Estimating Average Causal Effects Under General Interference*, https://doi.org/10.1214/16-AOAS1005 (design/exposure and weighted inference); Papadogeorgou, Mealli and Zigler (2017), https://arxiv.org/abs/1711.01280 (cluster/population allocation); Jeunen (2023), *A Common Misassumption in Online Experiments with Machine Learning Models*, https://arxiv.org/abs/2304.10900 (pooled-model interference); Murphy (2003), https://doi.org/10.1111/1467-9868.00389 (dynamic regimes); Farboodi, Koh and Xia's DDA (2026), https://arxiv.org/abs/2606.10127 (§5 already values future production data; Appendix B covers aggregation complementarity). Our conditional integration is **not independently established scientific novelty**.

The decisive falsification experiment first maps immutable learner-update components, sources and rights, firmware/hardware and buyer/operating interference. If XX is unsigned, only separately authorized offline matched-source technical qualification is permissible. If a complete XX physical policy is signed, lawful, jointly assigned in update-closed networks and accompanied by original accepted/paid customer service, it can distinguish the two counterworlds. No such evidence is currently established. Neither DROID/OXE episode metadata nor vendor announcements replace it. The Nov22 Models A–B scientific gate stays OPEN, as do Nov29 and Dec6; theory remains the majority through Dec6 and final target Dec25 2026 23:59 America/New_York.
