# Competence, coordination, and the limits of physical replication

First mechanism reconstruction, theory phase checkpoint 1. This is a reconstruction of a selected worked mechanism, not replication of the whole paper or a claim of novelty.

## Source and reading boundary

Alex Imas, Andrew Koh, and Shane Legg, *Organizing Intelligence*, author PDF dated **October 29, 2026**, retrieved November 16 UTC (November 15 Eastern), 2026. [Primary PDF](https://storage.googleapis.com/deepmind-media/papers/organizing-intelligence.pdf). SHA-256: `f763c6c2d8de4b653cd6d78ec96ec0ee206360cb4ea7e8c6d432c34e1100553a`. The supplied arXiv discovery entry is `2611.05417`; version equivalence has not been checked. Do not substitute its date for the inspected PDF's date.

Read the worked environment in §2.1–2.2 (printed pp. 3–7), formal primitives in §3.1, equilibrium definition in §4.1–4.2, and the concentration statement/discussion in §5.2 (Proposition 3, p. 33). The remaining proofs, especially the concentration proof, are not yet reconstructed. A local downloaded source lives in ignored `work/theory_sources/`; the URL and hash permit recovery without redistributing the paper.

## Mechanism card

**Question.** Why can better individual competence fail to produce larger organizations, while better coordination changes the returns to scale?

**Agents and primitives.** Humans have heterogeneous vectors of productive skills and coordination, fixed supplies, and outside options. Copies of a machine type have a common vector and can be rented without quantity limit at per-copy cost. A firm selects its size and composition. The worked example has two productive skills, six coders `(9,1,.75)`, six writers `(1,9,.75)`, and two coordinators `(1,1,.97)`. Firm competence is the harmonic mean of average skills. Coordination changes the scale term. Output faces either deep or finite demand.

**Information and solution concept.** These are known profiles, not learning states or beliefs. The formal paper combines competitive continuation (price/wage taking, break-even, no profitable entry, labor clearing) with replacement stability against a proposed alternative industry and transfers. Its surplus equivalence relies on that specified concept; it is not ordinary oligopoly pricing or the private provider problem below.

**Assumptions doing the work.** Complementary productive skills; aggregation of skills within firms; separability of competence from the size term at fixed composition; copyable AI at a rental price; no robot manufacture, physical qualification, payer-specific liquidity, or customer learning transition in this worked mechanism. Do not infer from these omissions that the whole paper considers every possible physical constraint and rejects it.

## Reconstructed worked result

Let `m>0` be continuous firm size, `L>0` competence, `y` average coordination, and `phi=7/4`. The example's output per worker is

`g(m)=L exp(phi*m/(1+m)) (1+m)^(y-1)`.

Thus

`d log(g)/dm = [phi - (1-y)(1+m)]/(1+m)^2`.

For `y<1` and `phi>1-y`, the unique interior maximum is

`m*=phi/(1-y)-1`.

The numerator decreases strictly with m, so its single zero changes the derivative from positive to negative. This proves global optimality on positive m. If `phi<=1-y`, g decreases on positive m and the supremum is at the lower boundary; with a minimum admissible size, maximize there. For `y>=1`, the derivative is positive at every finite m (at `y=1`, productivity increases toward the finite asymptote `L exp(phi)`). The distinction between a bounded asymptote and unbounded growth matters: the paper's Proposition 3 expressly excludes its knife-edge coordination exponent of one.

Holding composition fixed, multiplying L does not change m*. In contrast, `dm*/dy=phi/(1-y)^2>0` in the interior region. This is a productivity-maximizing size result, not an unconditional profit-maximizing fleet-size theorem.

For six coders, `L=2/(1/9+1)=9/5` and `y=3/4`, hence `m*=6`. Total output is about 29.8. Twelve coders in one firm produce about 57.2, whereas two size-six firms produce about 59.5. Equal coder/writer weights have average skills `(5,5)`, so L becomes 5 even though every individual specialist has standalone L=1.8. This reproduces the selected paper example's complementarity and size calculations. The executable check uses the source's functional form; numerical agreement verifies transcription and arithmetic, not its empirical validity.

**What is not established.** Proposition 3 is an asymptotic equilibrium claim as market depth grows, under the paper's formal assumptions. It is not a prediction that any finite robotics market tips to a single firm when an observed coordination score exceeds one. Our calculation neither replicates its equilibrium nor tests that threshold empirically.

## Changed assumption: finite physical replication

For a fixed recipe of physical units, suppose size is restricted to `0<m<=K`, with K the number of compatible, commissioned, supported units available this period. Under the same productivity objective and an interior unconstrained optimum, `m_hat=min(K,m*)`; when y>=1, `m_hat=K`. This is an immediate restricted-domain result. Better coordination still changes productivity, but need not change feasible scale. Expanding K requires a separate investment/delivery/qualification transition.

Moreover, even with abundant hardware, finite downstream demand can reverse the size implication. If useful sales are bounded by D, and each installed unit costs r>0, a simple alternative objective is `p min(F(m),D)-r*m`. Once output reaches D, adding units strictly lowers profit. Improving L can reduce the smallest fleet needed to serve D. Thus fixed-composition competence independence of the productivity-maximizing size does not imply competence independence of the profitable physical fleet. This is a change of objective and constraint, not a counterexample to the authors' theorem.

## Robotics mapping and proposed extension

| Source mechanism | Robotics interpretation | Boundary that must change |
| --- | --- | --- |
| Copies at rental cost | Reusing a policy/model on compatible robots | Qualified hardware, delivery, support, rights, and cash do not replicate for free |
| Complementary skill averages | A configured service may need sensing, mobility, manipulation, recovery | Physical capabilities may require a joint bundle; averaging skill vectors need not make a service feasible |
| Coordination changes scale | Shared supervision, routing and exception handling | Congestion, latency and correlated failure need separate evidence |
| Competence changes level | Better rate, reliability, accepted work | A benchmark improvement need not change complete-service output |
| Market depth supports scale | Customer output can absorb additional service | Customer revenue, procurement authority and funding differ from aggregate willingness to pay |

The proposed extension is a **private two-period investment problem**: a deployment yields cash, a directional cost/capability change, and access to a customer demand curve; costly investment changes supported capacity. This explicitly replaces unlimited contemporaneous replication. It does not yet explain endogenous legal firm boundaries or solve the source paper's equilibrium. See [the model and derivation](deployment_investment.md).

The [next seed mechanism](data_driven_automation.md) now distinguishes endogenous accumulation and directed spillovers from this known-transition investment problem. Its long-run and welfare propositions remain unreplicated.
