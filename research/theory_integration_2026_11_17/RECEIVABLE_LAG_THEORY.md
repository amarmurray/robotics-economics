# Accepted production, dated collections and shared learning capacity
*Integrated continuation of When Capabilities Become Production · November 17, 2026*

## Question and change to the existing theory

Result 8 permitted service A to remain qualified and productive while a separate development program attempted service B. Its original self-funding illustration assumed that A's collected net cash arrived immediately and B development did not reduce A production. Both assumptions can reverse the investment ranking. The strongest countermodel also allows an operator to **pause B, keep A producing, collect mature invoices, and resume B without losing validated progress**. This continuation repairs those assumptions in the same production/qualification argument; it is not a new standalone paper. All parameters and example returns are synthetic.

A is an accepted **complete customer service** relative to a credible human, specialist or other automation alternative. Let v>=0 be the deployer's actual earned net cash rate on accepted A output (not customer savings, robot cycles, or billed cash). Upon A qualification there is K>=0 truly available cash. Time h remains to qualify B. Development effort u(t) lies in [0,1], costs c u(t) per date, and produces a retained B qualification event at hazard b u(t). At full development intensity, fraction eta in [0,1] of A production can still operate; at zero intensity all of A can produce. Service A earns v[1-(1-eta)u(t)] net cash, collected exactly d time units after work is accepted. Safety coverage, qualification, rights and customer acceptance remain binding, rather than being relaxed by the algebra.

Until B success, the **cash state**, not the invoice balance, is

\[
C(t)=K-c\int_0^t u(z)\,dz+
v\int_0^{(t-d)_+}[1-(1-\eta)u(z)]\,dz\geq0,\quad 0\leq t\leq h. \tag{R1}
\]

This is not an equilibrium estimate: receivables may be disputed, refunded or legally owned by another actor. Those observations would change v and d or invalidate the payer contract entirely.

### Proposition R1: production-backed qualification as an exposure problem

For an unchanged hazard b, one B success and no uncertainty on the no-success path except the exponential event, any feasible control with cumulative exposure E(h)=integral(u) produces completion probability 1-exp(-b E(h)). Its maximum equals 1-exp(-b E*(h)), where E* is the maximal feasible accumulated learning exposure.

**Proof:** the event's survivor function solves S'(t)=-b u(t) S(t); conditional on not yet qualifying B, the effort/collections path can be selected predictably. The only signal is B's occurrence, after which development stops. Under these assumptions a feasible no-success schedule completely determines survival. This is standard event-hazard reasoning, not novel stochastic control. If successful A production or B hazards are stochastic, or prior failed trials change the hazard, this reduction is no longer sufficient.

### Proposition R2: exact result when A production is genuinely independent of B training

For c>0 and eta=1 the maximal cash-feasible exposure is

\[
\boxed{E^*(h)=\min\left\{h,\ {K\over c}+
 \min\left(1,{v\over c}\right)(h-d)_+\right\}.} \tag{R2}
\]

For c=0 it is h. **Proof:** before the first A collections, development can use at most K/c effort units. Beyond date d, learning cannot run faster than one unit per calendar time or, absent a saved balance, faster than v/c paid effort per collection time. Combining the initial-stock and subsequent-flow limits with E<=h yields the bound. It is attained by learning while cash is available, pausing if the initial cash is exhausted before invoices mature, and continuing after maturity at the physically and cash-feasible rate. Saved initial cash is used when valuable. This is a deterministic continuous-fluid cash-scheduling result, and depends crucially on costless pausing with retained B progress and legal continued A production.

If A is first acquired at random time s at rate a while costing c_A continuously, with starting cash B and no initial service cash, its success can occur only before min(T,B/c_A). After A success K(s)=B-c_A s, h=T-s and B-learning effort cost c_B. Thus the exact two-stage qualification probability is

\[
P(AB\ {\rm by}\ T)=
 \int_0^{\min(T,B/c_A)}a e^{-as}
 \bigl[1-e^{-b E^*(T-s;B-c_A s,c_B,v,d)}\bigr]\,ds. \tag{R3}
\]

The already-tested immediate-collection integral is recovered at d=0 when v>=c_B.

**Correction of an earlier overstatement.** A compulsory continuously running B trial can fail from cash exhaustion before a delayed invoice arrives. But a competent firm that can pause B need not abandon the qualification program: it may operate the accepted A service and resume upon collection. For the synthetic a=b=2, T=2, B=.5, c_A=c_B=1, v=4.5:
- Immediate collection and optimal B pacing: completion probability 0.613804919940.
- One-unit collection lag, compulsory continuously running B: 0.264241117657.
- The same one-unit lag, **pause and collect allowed**: 0.546572343960.

The difference arises without changing technical learning or buying an additional robot. These are theoretical probabilities, not observed warehouse rates. If the customer deadline h is no later than the first invoice maturity d, A's earned work cannot finance B *within that horizon* without an enforceable credit arrangement. A contractual test that forbids pauses can remove the optional policy; this must be observed rather than assumed.

### Proposition R3: a production resource shared with research changes the sustainable learning rate

If learning consumes the productive machine or the scarce supervisor, set eta<1 in R1. For fixed finite d, finite K, c>0, v>0 and divisible time-sharing, the maximum long-run effort fraction obeys the exact identity

\[
\boxed{\lim_{h\to\infty}{E^*(h)\over h}=
\min\left\{1,{v\over c+v(1-\eta)}\right\}.} \tag{R4}
\]

**Upper-bound proof:** writing E(t)=integral_0^t u, nonnegative cash gives
c E(h)+v(1-eta)E(h-d) <= K+v(h-d), for h>=d. Because E(h)-E(h-d)<=d, we obtain [c+v(1-eta)]E(h)<=K+v(h-eta d). Divide by h and take limsup, then intersect with E(h)<=h.

**Attainability:** let x=min(1,v/[c+v(1-eta)]). Keep A producing with u=0 until its d-lagged initial invoices begin collecting; thereafter use constant effort u=x. Initial collections from all-A production exceed or cover c x, and after the receipt lag reflects time-sharing the received rate v[1-(1-eta)x] equals or exceeds c x. Hence finite initial delay and zero initial cash do not prevent eventual duty share x. Asymptotic upper and lower bounds coincide. For v=0, positive c gives a zero limiting share.

This result exposes a crucial distinction from the immediately collectible, separate-equipment example. If eta=1 and v>=c, full-time B learning is ultimately self-funded. If eta=0, sustainable B learning is capped strictly below one, at v/(c+v), because each hour of B learning displaces the A service that funds it. A fixed finite one-time loan changes a transient balance but not this limiting physical/financial ratio. Manufacturing additional capacity or coordinating a second specialist can change eta; improved customer access and accepted net payment change v; learning-model benchmark progress alone does not mechanically change either.

For finite h and eta<1, R1 yields a linear program in dated u(t). The separately preserved and tested SciPy/NumPy time-bucket solver maximizes effort while checking every bucket-end cash balance; the published standard-library core contains R2–R6. In a 12-period synthetic calculation with initial cash zero, one-period collection lag, v=2 and c=1, the discrete effort share is 2/3 when eta=0, versus 11/12 when eta=1. The long-run limits are 2/3 and 1 respectively. These are numerical checks, not proofs of the continuum result or calibration.

### Proposition R4: a checkable success-contingent lender test (not free money)

Suppose an actual financier can legally advance F **at A success**, receiving up to beta of the deployer's *net collected AB receipts* W after B succeeds. The lender is risk neutral, bears the loss when B never qualifies, has no funding/friction costs or discounting, and has uncontested senior rights. AB earnings replace, rather than add again to, already modeled A operating income. B is pursued continuously at u=1 while unqualified. On that no-success path,

\[
C(t)=K+F-ct+\eta v(t-d)_+.
\]

The exact minimum date-zero advance required to sustain that uninterrupted B program through h is

\[
F_{\min}=\left[\max\left\{c\min(d,h),\ ch-\eta v(h-d)_+\right\}-K\right]_+. \tag{R5}
\]

The maximum expected AB cash collections pledgeable to the lender under full-time B exposure, with AB collection delay d_AB, are

\[
\Pi_{\rm full}=\beta W\left[
 (h-d_{AB})_+-
 {1-e^{-b(h-d_{AB})_+}\over b}
 \right]. \tag{R6}
\]

**Proof:** the maximum no-success cash deficit occurs at an endpoint of the two linear cash segments before and after d. The lender's expected claim integrates beta W times the probability B has succeeded by the AB receipt date. With stated enforceability and risk-neutral assumptions, an advance funding the entire uninterrupted plan is financially possible within **this contract class** if and only if F_min<=Pi_full. If it fails, it rules out this particular success-only pledge, not all supplier finance, non-refundable customer development payments, external equity, post-horizon claims or intermittent development.

For K=.25, c=1, d=1, h=2, eta=1, full effort requires F_min=.75. The synthetic lender claim at b=2, W=10, beta=.2, d_AB=0 has expected collected value about 3.018315638889. Lender participation is mechanically possible at zero required return in this stylized contract, but the provider must surrender that share. A positive customer surplus or a large invoice face value does not independently imply pledgeability, lending approval or optimal provider investment.

### Relation to source evidence, existing literature and further tests

DHL Group's **May 13, 2025** release reports commercially deployed Stretch unloading beginning in 2023, describes case picking as a future application target and discusses co-development/co-investment. It does **not** establish that the same robot simultaneously produces A and learns B, or reveal received cash or acceptance for B: https://group.dhl.com/en/media-relations/press-releases/2025/dhl-group-signs-mou-with-boston-dynamics-and-accelerates-cross-business-automation-strategy.html .

Bocola and Bornstein's *Macroeconomics of Trade Credit*, NBER Working Paper 31026, originally March 2023 and revised **June 2026**, analyzes firm-to-firm finance and the discounting of supplier receivables: https://www.nber.org/papers/w31026 . Amberg, Jacobson, von Schedvin and Townsend's *Curbing Shocks to Corporate Liquidity*, NBER Working Paper 22286 (2016), later *Journal of Political Economy* (2021), studies how firms adjust supplier/customer trade-credit duration under liquidity shocks: https://www.nber.org/papers/w22286 . These are important established precedents. Our propositions are conditional applications of liquidity conservation, hazard processes and productive resource allocation, **not claimed as original general mathematical discoveries**.

A discriminating joint panel would link accepted complete orders and alternatives, robot/site/task training exposure, concurrent accepted A production and safety staffing, earned net customer receipts, invoicing and actual bank collection dates, customer order expiry, receivable ownership, lender rights and disbursement dates, subsequent B acceptance and the feasible human/specialist outside option. Advertised pick rates, generic data volumes and signed MOUs cannot fill those missing links. A decisive rejection of the separable bridge would be that B training stops A production, or that no customer actually pays the entity assumed to finance B. If paused experiments destroy learning progress, the R2 policy is infeasible.

**Next intellectual step in the SAME paper:** make customer order demand for A and AB endogenous and compare net-profit-maximizing effort and stop policies against expansion of incumbent qualified capacity. Incorporate shared human supervision and actual collection rights into the service-production recipe rather than substituting a loan for technological capability. The November 22 integrated review and December 25 final deadline remain unchanged.

**Reproduction:** the repository's standard-library core is \`core_receivables.py\` with \`test_core_receivables.py\`. Ten tests were run against byte-identical source. A more extensive independently checked SciPy time-bucket LP, quadrature and seventeen scoped tests were preserved locally in the research package, but are **not represented here as committed Git code**. All numbers are synthetic.
