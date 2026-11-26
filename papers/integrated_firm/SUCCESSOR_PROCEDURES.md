# When does the firm improve how it improves?

## The opportunity missing from a tiny firm

The small integrated firm has four possible execution-model increments. It can produce two research-procedure generations, but most parameter cases do not find that investment worthwhile. That is useful discipline. It also limits the economic question the small state space can answer: a procedure is reusable across tasks, so its return depends on how many distinct improvements remain.

This extension varies the number of recipient tasks while retaining the parent model's production recipes, market process, research costs, qualification technology and outside contracts. It derives the recipient payoff from operating decisions. It does not attach an assumed fleet-value coefficient to a procedure.

The extension is a **staged, prefunded restriction of the general environment**, not the full concurrent economy with all its constraints active. There is a research window, followed by eight operating periods. Installed equipment is fixed. Each recipient faces its own local physical/digital markets and has its own operating pools. A reserved research facility can conduct one project per window. The shared cash account is sufficiently funded to make the budget nonbinding; a sufficient bound is reported. This isolation lets us solve the recursion mechanism and expose what must be reintroduced in the longer competitive model.

## 1. Derive the recipient's payoff

Each recipient starts with the parent technology's arm, physical model 0 and digital model 0. A qualified improvement raises that recipient's digital model to 1. Improvements address distinct task families, so qualifying one recipient does not automatically qualify every recipient. The reusable object is the research procedure.

The operating firm chooses accepted physical/digital service and human/agent recipes under four human and seven compute units. Scope, installed assets and model levels are then fixed during the eight operating periods. Optimal current net operating receipts are:

| Digital model | Demand state 0 | Demand state 1 |
| --- | ---: | ---: |
| 0 | 7 | 8 |
| 1 | 10 | 13 |

These numbers come from [core.py](core.py)'s feasible service program. The source model earns 7 by mixing one physical job with one digital-agent job in state 0, and 8 by serving two digital jobs with people in state 1. The improved model earns 10 in state 0 and 13 in state 1; the latter includes one physical and two digital services. The upgrade changes both resource use and the service mix.

The demand state starts at 0 when the operating phase opens and persists with probability \(3/4\). Over eight periods,

\[
\Pi_0=59.00390625,\qquad
\Pi_1=89.01171875,
\]

so the value of one additional qualified target is

\[
G=\Pi_1-\Pi_0=30.0078125.
\]

This \(G\) is an output of the production model. It includes optimized pricing and substitution into accepted services. It is not a reward for benchmark accuracy, an assigned price of data, or a return paid before customers arrive.

The operating continuation also has a closed form. At operating date \(t\), the chance of demand state 0 is \((1+2^{-t})/2\). The expected incremental margin is therefore \(4-2^{-t}\), giving \(G_L=4L-2(1-2^{-L})\). Setting \(L=8\) recovers the computed gain exactly.

Because the local markets and operating pools are independent in this restriction, terminal operating value with \(k\) qualified recipients is \(N\Pi_0+kG\). Common final-market demand or shared support would break this additive reduction and require a coupled operating continuation.

## 2. Exact research problem

Let \(r\) be remaining research windows, \(n\) remaining unqualified targets, and \(\psi\in\{0,1,2\}\) the best retained procedure. Both inherited source archives are available. The firm can stop, train a target, develop a successor internally, contract for either project, or buy a guaranteed successor license. Previously qualified procedures remain available.

Using procedure \(m\leq\psi\),

\[
\alpha_m=(2+m)/4,\qquad
\rho_m=1/2+m/4
\]

are target-qualification and successor-qualification probabilities. Each operation uses one research window. Internal training costs \(5\), internal procedure development \(6\), contracted training \(8\), contracted procedure development \(9\), and a guaranteed successor license \(13\). These invoices include the parent technology's human/compute/provider requirements and one tick for the active research facility. Stopping uses no resources. All outcomes are observed before the next window.

Define \(W(r,n,\psi)\) as incremental value above operating all recipients with their original models. Then \(W(0,n,\psi)=W(r,0,\psi)=0\), and training with method \(m\) has value

\[
-5+\alpha_m\{G+W(r-1,n-1,\psi)\}
 +(1-\alpha_m)W(r-1,n,\psi).
\]

When \(\psi\) is below the permitted cap, developing the successor has value

\[
-6+\rho_mW(r-1,n,\psi+1)
 +(1-\rho_m)W(r-1,n,\psi).
\]

Contracted actions replace the relevant invoice. Licensing has value

\[
-13+W(r-1,n,\psi+1).
\]

The Bellman value is the maximum of these alternatives and zero. It jointly chooses the research sequence and the eventual production gains. The \(G\) credited at qualification is an algebraic allocation of terminal operating value. It cannot be spent as cash during research.

A sufficient prefunding bound is \(13R+15LN\), where \(R\) is the number of research windows, \(L=8\) the operating horizon, and 15 the maximum full operating-pool outlay per local market-period. This bound even ignores customer receipts. Consequently no selected path relies on an imaginary early payment for learning. Initial principal is excluded from incremental value.

## 3. Hold research time fixed and vary the target population

The table holds \(R=16\) research windows, the operating horizon, prices, costs and qualification technology fixed. Values are expected **incremental net receipts**, after research costs, above all recipients operating with their original models.

| Distinct target tasks | Procedures fixed at 0 | Can produce procedure 1 | Can also produce procedure 2 | First action with both generations available |
| --- | ---: | ---: | ---: | --- |
| 2 | 40.0101 | 40.0101 | 40.0101 | Train a target |
| 4 | 79.7711 | 81.3450 | 81.3479 | Develop procedure 1 |
| 8 | 144.3459 | 173.3710 | 179.9733 | Develop procedure 1 |
| 12 | 159.8024 | 241.8939 | 278.8125 | Develop procedure 1 |

The eight-target economy is the clearest second-generation case. Allowing procedure 2 adds \(179.9733-173.3710=6.6023\) ticks after reoptimizing both programs. The full contingent policy qualifies all eight targets by the operating date, using research and an expensive guaranteed license where a sequence of failures makes insurance valuable. The results record separately whether the second procedure is developed or licensed.

The comparison changes a productive technology menu. It does **not** compare an intelligent firm with an ordinary organization forbidden to plan contingently. A capable fixed contingent organization allowed the same procedures, observations and contracts can implement the full optimum. The positive result belongs to producing and acquiring a reusable research input, not to naming the firm recursive or training the allocator with RL.

There is no theorem that the number of targets always raises every kind of internal research. At twelve targets and a one-generation cap, the optimum starts by buying a license. Under tighter deadlines, a contract's certainty can be worth more than the lower expected invoice of internal research.

## 4. Hold the target population fixed and change the deadline

For \(N=8\), the two-generation program has value \(174.0625\) with 10 research windows, \(179.9733\) with 16, and \(180.0569\) with 20. The first action is a license under the tight deadline and internal development with more time.

More available time weakly increases optimized value because the firm can preserve its old schedule. It does not require more actual research spending or a higher internal-ownership share. The value of additional time falls as the probability of completing the useful research agenda approaches one.

The exact operating gain is invariant across these deadline comparisons. This isolates timing from a change in the target's product market.

## 5. Local and global implications

Within a region of parameters in which the optimal policy is unchanged, the value is affine in the derived recipient gain \(G\). Its derivative is the expected number of qualified targets. Across regions, the upper envelope changes slope and the preferred initial action can switch between direct training, procedure development and licensing.

For a narrow expected-time calculation, improving target success from \(3/4\) to 1 saves \(N/3\) expected training windows across \(N\) remaining independent targets. Producing that improvement with success probability \(3/4\) takes \(4/3\) expected windows. Thus \(N>4\) is the threshold for reducing the expected total time in this *uncapped repeat-until-success calculation*, before comparing cash costs, deadlines or intermediate service. It is a useful diagnostic of why a tiny opportunity set can obscure the mechanism. It is not the optimum's full threshold: the exact deadline problem includes option value, completion risk and external licenses.

The finite economy still saturates. Once every target is qualified and procedure 2 retained, further research has no payoff. Sustained recursive growth would require new target arrival, further procedure generations, changing research reliability and resources, demand and strategic entry. This extension solves two generations and an endogenous recipient stake; it does not solve that growth problem.

## 6. Replication and interpretation boundary

[cohorts.py](cohorts.py) solves the dynamic program and independently propagates its optimal policy distribution. [cohort_results.json](cohort_results.json) records choices, expected qualifications, actual outlays, the routes to the second procedure, the prefunding bound and the identity

\[
W=G\,\mathbb E[\text{qualified targets}]
-\mathbb E[\text{research outlay}].
\]

An additional rational-arithmetic checker reconstructs the operating margins and the complete Bellman recursion. These checks are independent implementations by the same writer, not independent scientific review.

The next integration step is to restore concurrent production/research and shared recipient resources while preserving enough distinct tasks for second-generation improvement to matter. The subsequent competitive horizon must retain the common posterior and rivals' changed opportunities. Its continuation values must again be solved, not borrowed unchanged from this independent-market restriction.

