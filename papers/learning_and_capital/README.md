# Learning and Capital in Robotic Production

*Working theory for the RoboEcon program · November 25, 2026*

**Under what conditions does deploying a robot today cause more robotic capital to be deployed tomorrow, and where does that capital go?** Buying a machine adds productive capacity in a particular place. Operating it can also produce knowledge usable in other places and cash that its owner can invest again. Those three benefits can reach three different firms. The direction of automation depends on how their decisions fit together.

### The economic premises

A body, a technician and a commissioning bay occupy time in one location. A validated control policy or diagnostic procedure can be copied to several compatible machines. Operating experience arises from actions actually taken. A fleet can run longer while encountering fewer of the failures another fleet needs to understand. Finally, a technically viable project needs a customer, someone willing to absorb the installation cost, and resources available on the dates they are required. A machine can be ready to work before a financier recovers the cash needed for the next installation.

These asymmetries give us three maps of the same economy. The **production network** specifies who supplies which input to which customer. The **learning network** specifies where experience can change a future production decision. The **financing network** specifies who receives cash from one deployment and can commit it to another. The three maps can overlap or cross. A packaging line may supply a hospital, teach a gripper supplier something useful in food fulfillment, and remit its cash to an owner investing in a third market.

Our central economic object is the **matrix of induced deployments**. An entry gives the additional funded installations of one type ultimately caused by a marginal installation of another type, before counting what those new installations induce in turn. It is relative to ordinary production that also learns and invests. Its units are installations per installation. It counts a serviceable deployment of a specified embodiment at a specified kind of site. Downloads, announced orders and transfers between business units have different units.

The model yields two distinct meanings of faster progress. Earlier delivery of the same usable knowledge can accelerate adoption in calendar time. Changing who can use a lesson, whether it arrives before its opportunity expires, or how soon working capital is released can also change how much adoption a generation of machines induces. Two end markets that each fail to sustain additional investment on their own can sustain it together. We derive when that is possible and when diminishing opportunities limit its extent.

*When Capabilities Become Production* supplies the feasible operating alternatives. *Recursive Firm Theory* supplies the choices that change how experience is generated and used. Here the adoption decisions of subsequent firms feed back into the distribution of productive capital. [Production manuscript](https://github.com/amarmurray/robotics-economics/blob/e8cc97fed54e3815dda113bac3a7b4a333955331/research/theory_integration_2026_11_17/data_value/WHEN_CAPABILITIES_COMPACT_DRAFT.md) · [Recursive-firm network study](https://github.com/amarmurray/robotics-economics/blob/6951d24824287b11056e62e3e5221f818086ef5c/research/recursive_firm/network_mpk/README.md)

<!-- page -->

## 1. The marginal product of a particular robot

A deployment type specifies an embodiment, task stage, end market, controlling firm and operating window. Two firms can work in the same industry and occupy different positions in the three networks. A digital agent may dispatch jobs or review evidence from many physical sites. The robots, the available technical labor and permission to install a release remain site-specific.

Let $Y_m$ be original service accepted in end market $m$ at a given quality and deadline. Let $K_i$ be installed units of embodiment and site type $i$. At a stated service mix or fixed set of weights for selecting among feasible orders, define the column of marginal physical products

$$J_{mi}=\frac{Y_m^*(K+\Delta K_i e_i)-Y_m^*(K)}{\Delta K_i}.$$

Each coordinate has units of accepted service per added machine over the window. Operating or support hours can be perturbed separately. Other endowments, initial knowledge and original demand are fixed in this comparison, while dispatch can adapt. If several schedules tie, specify a dispatch rule or report a range. More capital can redirect work away from one market while increasing total value. For different final services, aggregation requires weights and counts each final service once.

The **operating value** of an additional machine includes savings in scarce human time, maintenance or shutdowns even when final volume is fixed. Its **investment value** is the difference in discounted private contribution between the best feasible programs with and without buying it, net of acquisition once. Both programs can use ordinary experience. Market prices, data rights, capital costs and spillovers to others separate this value from the physical marginal product.

A simple restriction gives the sign of the immediate effect. A final job needs one machine stage and one support stage. With demand $D$, installed robot capacity $K$, support hours $H$, and stage rates $a,b$, output is $\min(D,aK,bH)$. Improving execution can raise existing throughput and exhaust demand so that another machine adds zero units. Improving human exception handling can instead release a binding support constraint and make the next machine productive. Identical gains on a robot benchmark need not move the same coordinate of $J$.

What makes this about programmable production? The site at which a machine works determines both its immediate product and the experience available to change $a$, $b$, or a different firm's technology. Amazon's Robin study documents a fleet that ranked candidate grasps using results from attempted picks, across differing workcells and tooling. That establishes a physical route from operations into a policy update. How much transferable knowledge or additional capital a particular shift caused is a separate empirical quantity. [Li et al., *Demonstrating Large-Scale Package Manipulation*](https://roboticsproceedings.org/rss19/p023.pdf)

<!-- page -->

## 2. Data generation, collection and the firm's choice

A source site $i$ encounters $A_i$ attempts per period. They include recoveries and failed jobs. The operating policy selects the cases attempted. Let $q_{0i}$ be the useful records per attempt obtained in ordinary work, after accounting for novelty at the margin. Investigation intensity $z_i$ between zero and one adds $q_{1i}z_i$ records per attempt in this restriction. These rates are conditional on the current corpus and operating policy. A million nearly identical records can carry little additional evidence.

Let $t_{ji}$ be the marginal validated change in method $j$ per useful source record, inclusive of compatibility and permissions for that use. It can differ across embodiments. One retained record can benefit several recipients. A second copy at the same recipient confers value only through its incremental effect. The firm's discounted captured value per unit of that change is $\beta^{\ell_{ji}}\lambda_{fj}$ when usable after lag $\ell_{ji}$. Use joint expectations if event quality, permission and the opportunity to use a result are related.

Suppose incremental collection costs per attempt are $\omega_i z_i+\kappa_i z_i^2/2$, with $\kappa_i>0$. The linear term includes displaced productive work. With locally constant marginal values, yields and transfer, an interior choice equates marginal cost with the sum of marginal *captured* returns. Including corners gives

$$z_i^*=\mathrm{clip}_{[0,1]}\left(\frac{q_{1i}\sum_j\beta^{\ell_{ji}}\lambda_{fj}t_{ji}-\omega_i}{\kappa_i}\right).$$

This is why data richness has several dimensions. A site can generate unusual cases yet collect little when the operator cannot use the results and no beneficiary pays. A model supplier may attach greater value to a correction than the host that pays for human review. A license, a contingent payment or common ownership can change collection. Equal feasible rights, timing and financial claims yield equal incentives in this restriction.

Full-stack ownership is one way to connect operating, learning and financing decisions. A digital agent that can schedule machines may still depend on a customer to approve cross-site training or an owner to release cash. Autonomy concerns which of those decisions an agent can actually revise. The typology follows from control over these links and the resources they use. Different products, sites and contracts within one firm can have different degrees of recursion.

There is also feedback *against* learning. With incident-only collection, useful records per period equal attempts times the failure probability times the conditional usable yield per failure. If failures become rarer faster than attempts and conditional yield rise, the evidence stream contracts while successful production can expand. Deliberate sampling of normal work offers an alternative and consumes resources. Rights expiration or a change in embodiment can further reduce the useful life of the stock.

Write $L_{ji}$ for the net marginal additions to validated method $j$ per extra period of an active deployment of type $i$. In the simple source above this is incremental attempts times useful yield times validated transfer. In a constrained fleet it includes displaced attempts and review elsewhere. A recursive firm can invest to change $L$, the release lag, or the collection policy itself. A better executor changes present performance. A better rule for experimentation changes what the next unit of field access can discover. [Study of endogenous incident supply](https://github.com/amarmurray/robotics-economics/blob/6951d24824287b11056e62e3e5221f818086ef5c/research/recursive_firm/learning_dynamics/README.md)

<!-- page -->

## 3. Capital velocity and the decision to install

Operating turnover is qualified work per installed machine-period. Commissioning velocity is installations per crew-period. Both can rise while the cash available for the next purchase stays tied up. We use **financial capital velocity** for how often a unit of revolving funds can be committed, recovered and recommitted. If each installation ties up $c_j$ dollars for $T_j$ periods, each start occupies $c_jT_j$ dollar-periods. With financing base $W_j$, a balanced pipeline can start at most $W_j/(c_jT_j)$ installations per period. The turnover of identical fully occupied dollars is $1/T_j$. For staged collections use $m_j=\int b_j(s)\,ds$, the area under the outstanding recoverable cash balance of one project. Advance payments and interim releases change this area. Count permanent asset cost in the investment calculation. [Little's flow and occupancy relation](https://doi.org/10.1287/opre.9.3.383)

Let $\nu_j$ fresh eligible candidate sites arrive per period with heterogeneous one-time integration costs distributed as $F_j$. Each requires one standardized installation. Write $v_j$ for the private value of its incremental services given the deployed capital of other firms and validated method stock $h$, less the machine price and before the site-specific integration cost. For example, with a constant incremental operating margin $\pi_j(h)$, a commissioning lag $d_j$, a discount factor $\beta<1$, and per-period retirement probability $\delta_j$ after commissioning,

$$v_j(h)=\frac{\beta^{d_j}\pi_j(h)}{1-\beta(1-\delta_j)}-P_j.$$

This valuation includes the operating alternatives in Section 1. A move in market prices, the volume that qualifies or the division of savings can change private margin. In the solved restriction the private operating path used by the candidate is stationary after commissioning. With forward-looking price or policy changes use the expected discounted path instead.

Available starts are the minimum of profitable applicants, financeable starts and a physical installation ceiling $S_j$.

$$I_j(K,h,W)=\min\{\nu_j F_j(v_j(K,h)),\ W_j/m_j(h),\ S_j(K,h)\}.$$

The expression assumes applicants draw on equal cash-time within type and capacity can be assigned among eligible applicants. It applies to balanced pipelines, or to cohorts contracting for a cash-time budget. A transient rollout with dated receivables requires the outstanding balances by vintage.

A faster payment to a deployer may also tie up the customer’s funds sooner. For a small reallocation of revolving cash and comparable machines, the effect on total starts is the cash moved times the difference in starts per additional dollar at the two firms. It can be negative when the customer was the more constrained adopter. An acceleration of collections for one firm does not establish faster capital turnover for the entire chain.

When profitability binds, the response to a method improvement is proportional to the density of sites *at their investment threshold*, $\nu_j F'_j(v_j)\partial_h v_j$. When cash binds it is $-I_j\partial_h\log m_j$ at fixed $W_j$. When available machines or commissioning crews bind, it is $\partial_h S_j$. At ties compare both feasible regimes. Thus a higher physical marginal product can coexist with flat installation, and faster release of working capital can expand deployment with identical execution capability. Symbotic reports that customer advances and work performed before invoicing both occur. Its disclosure supports distinguishing these clocks. Identifying a binding financing constraint requires further evidence. [Symbotic, contract balances](https://www.sec.gov/Archives/edgar/data/1837240/000183724026000009/sym-20251227.htm)

<!-- page -->

## 4. Closing the loop between firms

Consider marginal changes around ordinary production and investment over one decision period. The vectors $k,h,w$ are changes in active installed units by type, stocks of validated methods, and available revolving financing bases by owner. The diagonal matrices $S_K,S_H,S_W$ give the fractions of these increments retained each period. Put $D_X=I-S_X$ with strictly positive diagonal losses. Funds can be distributed or reallocated outside the modeled pool. The return of an installation's original working capital is already included in its cash-time requirement.

In a locally constant operating and contracting regime let $C$ and $B$ be the derivatives of the *same* admissions decision in Section 3 with respect to methods and financing. Let $U$ give new starts due to a change in the orders or physical capacity available to another firm, holding methods and funds fixed. For example, extra downstream output induces upstream demand for components. At a profitable-applicant threshold its installation effect is the induced component demand times the resulting change in the candidate project’s value per component, times the density of eligible candidates at that threshold. An incumbent supplier with spare capacity may fill those orders with no new installation. Let $P$ be additional net cash retained for investment per active unit and $R$ the change in retained cash due to better methods on the incumbent base at fixed units. Transfers across owners are tracked at the receiving fund. The three dated equations are

$$k_{t+1}=S_K k_t+U k_t+C h_t+B w_t,$$

$$h_{t+1}=S_H h_t+Lk_t,\qquad w_{t+1}=S_Ww_t+Pk_t+Rh_t.$$

The installation equation allows a one-period decision-to-operation lag. Longer lags appear below. $P$ and $R$ are new net cash accruing to the financing base after costs and distributions. Adding recovered principal to either would count the same dollars twice. The method equation assumes constant marginal collection and transfer within the regime. If firms redesign their policies in response to the impulse, the coefficients must include the responses or the regimes must be solved separately.

**Proposition 1.** Over an installation's remaining life, the matrix of first-generation additional deployments is

$$G=\left(U+CD_H^{-1}L+BD_W^{-1}P+BD_W^{-1}RD_H^{-1}L\right)D_K^{-1}.$$

The four paths are **additional orders or complementary capacity**, **experience that qualifies sites or shortens their cash tie-up**, **cash earned by additional machines**, and **learning that raises retained cash on the existing fleet**. Each path ends at a funded installation. The last factor counts the expected active periods of each source machine. The inverse loss rates inside each path count the usable periods of the method or funding increment. No data premium is added to customer revenue.

On a reachable, strongly connected component with nonnegative marginal responses, additional deployment fades across generations when the largest eigenvalue $\rho(G)$ is below one. It amplifies locally when that eigenvalue exceeds one. At one the linear benchmark is on its boundary. The comparison is for the *increment* over ordinary replacement and learning. For two types each below replacement in isolation, the condition for joint amplification is exactly

$$g_{12}g_{21}>(1-g_{11})(1-g_{22}).$$

<!-- page -->

## 5. The speed and extent of automation

Let $G_\ell$ count first-generation installations arriving $\ell$ periods after the source. Its sum over all lags is $G$. If $b_t$ is an external seed of new starts, the linear sequence of additional starts satisfies

$$n_t=b_t+\sum_{\ell\ge1}G_\ell n_{t-\ell}.$$

**Proposition 2.** Moving an otherwise identical response to an earlier date leaves $G$ unchanged. It raises the discounted value of a positive dated response. In the amplifying regime it raises the calendar growth rate if the accelerated link participates in the active irreducible component. In an amplifying component the gross calendar growth factor $r>1$ satisfies $\rho(\sum_\ell r^{-\ell}G_\ell)=1$. Earlier lags increase the left side at the old $r$, so the new solution is larger. A common time shift does not by itself create a self-sustaining component. An earlier release that preserves a license, beats obsolescence or lowers the cash tied up per start can also increase the entries of $G$. It can then change the extent of adoption. These conclusions separate a pure delay change from changes in realized technical yield, demand, financing or entry incentives.

**Proposition 3. A bounded economy can sustain a positive additional deployment rate.** Take a fresh cohort of $m_j>0$ eligible opportunities of each type in each generation. Ordinary adoption is already accounted for. Feasible offers induced by the current deployments independently reach the remaining sites, which can adopt at most once. In a continuum with uniform Poisson matching, the average number of offers per site of type $j$ is $(Gn)_j/m_j$. Unused duplicate offers lapse in that cohort. The exact expected mass of new deployments in the continuum is

$$n'_j=m_j\left[1-\exp\left(-\frac{(Gn)_j}{m_j}\right)\right].$$

For a primitive nonnegative $G$, a one-off positive seed fades to zero if $\rho(G)\le1$. If $\rho(G)>1$, every strictly positive seed converges to one positive, finite deployment flow. Overlap between offers limits the share of each cohort that adopts. This is a specified saturation mechanism with replenishing eligible cohorts. Other scarcity or price changes can produce other long-run paths. In finite populations an individual seed can still die out by chance.

The distribution follows from the same object. Under a primitive, fixed $G$, the shares of types in successive marginal generations approach its normalized positive right eigenvector. A high standalone $MPK_r$ and a large eventual share of new machines are different predictions. Type units and any expenditure weights have to be specified. A one-way transfer can make the recipient much more productive. When each market is below replacement on its own, sustained amplification requires a sufficiently strong return path. It may run through demand, reinvested cash or shared learning. Crowding out another firm's deployment or training on harmful transfers can give signed responses. Those cases require the full controlled transition and actual feasible alternatives.

The distinction matters commercially. More fleet hours, faster releases and cheaper inference can bring the same contracts forward. A new approved embodiment, timely cross-customer rights, or a financing change can enlarge the number of viable contracts and establish a return path between markets. Measured robot sales alone can look similar early in both transitions. Dated first use, qualification failures, expired opportunities and subsequent capital commitments distinguish them.

<!-- page -->

## 6. Where the marginal product of capital rises and falls

Suppose a release improves the method used by an installed fleet. On impact we observe what existing machines can do with that release. After firms have had time to buy machines, change the dispatch policy or hire technicians, we observe the productivity of a different fleet. A comparison of mature sites can miss the very improvement that induced them to install.

Consider one price-taking site producing accepted service $Y=aK^\alpha$, with $0<\alpha<1$. The parameter $a$ summarizes the method and the complementary inputs held fixed here. Let $p$ be the service price and $u$ the competitive rental cost per machine-period. Start at a positive interior optimum. Over an operating window in which the fleet cannot change, a one-percent increase in $a$ raises physical $MPK_r=\alpha aK^{\alpha-1}$ by one percent. Once the site can adjust its entire fleet, the interior investment condition is

$$p\alpha a(K^*)^{\alpha-1}=u,\qquad \frac{d\log K^*}{d\log a}=\frac{1}{1-\alpha}.$$

At unchanged service and rental prices, the improvement ultimately appears in a larger fleet and higher output. Its long-run marginal physical product returns to $u/p$. A site held at a binding fleet ceiling can instead exhibit a rising marginal product and flat investment. If the ceiling is then released, the site can add robots while its measured marginal product is falling. The timing of measurement and the state of the complementary inputs determine what an observation of $MPK_r$ means. A changing price or service mix must be recorded separately.

The same reasoning applies across markets. Write $x=(K,h,W)$ for the levels of capital, methods and revolving funds, and $T$ for the block transition in Section 4. Let $e_i^K$ place one unit of type $i$ in the capital block and zero in the other states. Around a stationary regime, the first-order change in the marginal physical product of machine $j$ for final service $m$, per small initial addition of machine $i$, at date $t$ is

$$\nabla_x J_{mj}(\bar x)^\top T^t e_i^K.$$

This is a response of *another marginal product*, with units of service per target machine per source machine. It differs from the matrix counting new installations. Local demand schedules and other exogenous resources are held fixed, while induced orders and the dispatch rule are included in the service map. Funds may have no direct effect on an already paid-for shift and still matter at later dates through $T$. At a binding constraint or a discrete change of embodiment, replace the derivative with the two feasible differences on either side of the change. Even where every adoption link is positive, the marginal-product response can have either sign.

<!-- page -->

## 7. How the transformation travels through the value chain

A downstream improvement can shrink an upstream industry that supplies its learning data. Let one final unit require $b$ units of an upstream input at price $p_U$. Suppose other unit cost $c_0$ is constant, final competition passes through costs, and final demand is $y=A(c_0+p_Ub)^{-\epsilon}$ with $\epsilon>0$. Define the upstream cost share $s=p_Ub/(c_0+p_Ub)$. Upstream sales are $x_U=by$. Then

$$\frac{d\log y}{d\log b}=-\epsilon s,\qquad \frac{d\log x_U}{d\log b}=1-\epsilon s.$$

When an improved method saves upstream material, final buyers demand more. Upstream volume contracts if $\epsilon s<1$ and expands if $\epsilon s>1$. If useful upstream records are produced in proportion to volume, the stream feeding the next downstream improvement moves with upstream volume. The downstream firm can therefore improve its present product while eroding a source of its future productivity. Inspection of successes, product redesign or a change in retention rights can alter that transmission. Similarly, total labor in a role equals its hours per unit times volume. A lower routine-labor requirement per unit can coexist with more total technical review after the market expands.

The existing network study traces a packaging plant, digital dispatch, retail fulfillment and hospital supply. Its synthetic economies show how a new hospital specification can expand accepted hospital work and contract upstream work. Here the response of upstream evidence and cash can also change *future* installations. This is a causal hypothesis about successive cohorts. Public input-output accounts measure buyer–supplier relationships. Transfer tests, contracts and settlement records are needed to measure the other two networks. [RoboEcon network study](https://github.com/amarmurray/robotics-economics/blob/6951d24824287b11056e62e3e5221f818086ef5c/research/recursive_firm/network_mpk/README.md) · [BEA requirements tables](https://www.bea.gov/resources/guide-interactive-industry-input-output-accounts-tables)

| Firm position | Which additional deployment it may induce |
| --- | --- |
| Site operator paid for accepted service | A faster local policy can release labor or cash. If the next buyer cannot use the update, the gain can end at that site. |
| Model or component supplier serving many operators | A record from one customer can improve several eligible fleets. A per-use royalty, a flat fee and competitive pass-through give the supplier different incentives to acquire that record. |
| Integrated fleet owner or deployer | A loss of volume in one unit can be covered by a gain or newly available funds elsewhere. A shared commissioning crew or financing line can also displace another launch. |
| Consortium of independent firms | A timely contingent license and shared funding can implement the same decision as an integrated organization. Missing rights, delays or separate claimants can break the return path. |

Opening cross-customer reuse can widen technical reach while reducing the originator’s willingness to pay for investigation. For example, under two-supplier competitive procurement a given improvement in qualification earns less private margin when a rival can already supply the same low-cost method. Rights can therefore change both the destinations reached and the amount collected at the source. [Competitive learning model](../autonomous_firm/When_Faster_Learning_Pays.md)

<!-- page -->

## 8. The value of changing how the firm learns

The firm can spend an engineer-week to change evidence collection or validation. It can buy an adapter, delegate release authority to a digital agent, or renegotiate a milestone that releases cash sooner. Each action may change the *matrix* of future opportunities. This gives the higher-order decision an economic price.

Let $G_\beta=\sum_\ell\beta^\ell G_\ell$, assume $\rho(G_\beta)<1$, and set $Z=(I-G_\beta)^{-1}$. For an initial vector of new deployments $b$ and discounted direct net value $v$ per installation, the value attributable to these seeds is $v^\top Zb$. A redesign can also change the value of work on already installed machines even if it induces no new start. Include that direct incumbent effect separately when it is outside the seed account. Use real net value for the whole chain or the firm's own cash claims for a private decision. Direct values are attributed once and exclude benefits from descendant installations. Cash available for reinvestment is a financing state. The same operating surplus contributes to real value only once. In an environment where only one link changes locally,

$$\frac{\partial(v^\top Zb)}{\partial (G_\beta)_{ji}}=(v^\top Z)_j(Zb)_i.$$

The right factor counts how much activity reaches the source. The left values the destination and what it can induce. A source with little direct operating margin can therefore merit a scarce learning investment. A frequently visited source can have little incremental value when no additional recipient can use or finance the result. For a finite redesign, compare the two complete discounted systems and charge real design and displacement costs. When $v$ or $b$ changes, include those differences too. When a rival responds, recompute the links, prices and private claims under that response. The production of learning capacity is a choice inside the theory.

**Discriminating observations.** To measure physical $MPK_r$, use additional machines or service blocks at known staffing, demand and deadlines, recording declined jobs and fallback, as well as deliveries. To measure $L$, compare fresh compatible sites under ordinary updating and a changed sampling or release rule, at matched executor, rights and budget. Collect all attempted work, its condition and its path to a validated release. To estimate $C$ and $B$, follow all eligible prospects, including refusals. Observe when qualification, cash headroom or a commissioning slot becomes available. A change in payment milestones at unchanged machine performance is especially informative where finance binds.

To distinguish a timing response from wider adoption, compare installation dates *and cumulative funded starts* across cohorts after long enough for routine learning to catch up. Record contracts or technical regimes that expire while sites wait. Test for cross-site spillovers where sites share methods but no material input, and for demand-only effects where they share a supplier but no evidence rights. Common demand, hardware upgrades and subsidized financing can generate correlated installations without one site causing the next. The target is a causal marginal response from independent variation or identified bounds. A count of later customers at the same vendor cannot identify a matrix entry by itself.

To aggregate, retain the joint distribution of final-work vectors, labor mix, data yields, rights, cash occupation and eligible adopters at each investment threshold. Weight physical service by defined end-market units or explicit valuations, private gains by their recipient, and aggregate real output by original final demand. Large rollouts require updating marginal products and constraints as production moves. The model delivers a local propagation law and one bounded long-run economy. Sector-specific estimates of the links and the response of prices, wages, entry and financing supply are the next empirical and equilibrium questions.

<!-- page -->

## Appendix. Derivations and replication

**First-generation accounting.** Group the method and funding states into one vector. Write $A=(C\ B)$, let $E$ stack $L$ above $P$, and let $M$ have diagonal blocks $S_H,S_W$, lower-left block $R$ and zero upper-right block. Suppress all induced deployments while attributing the first generation from the seed. A source still operating $s$ periods after installation contributes $E S_K^s$ to the other states. Those increments last through $M^u$ after $u$ more periods. A subsequent start arrives at lag $s+u+2$. Hence

$$G_\ell=U S_K^{\ell-1}+\sum_{s+u+2=\ell} A M^u E S_K^s.$$

Here the first term of the dated kernel is the direct operating route. Inverting the triangular blocks gives the four paths in Proposition 1. More generally, the discounted kernel is

$$G_\beta=[\beta U+\beta^2 A(I-\beta M)^{-1}E](I-\beta S_K)^{-1}.$$

Setting the discount factor to one recovers $G$. The matrices $M$ and $S_K$ here have spectral radii below one. With signed interactions the accounting of first-round paths still applies, but the nonnegative comparison theorem need not. For the positive two-type case in the text, the determinant of $I-G$ changes sign at the stated threshold because both diagonal entries of $G$ are below one. The Perron root crosses one there.

**Bounded cohorts.** Denote the map in Proposition 3 by $\Phi$. It is increasing, bounded above by $m$, with derivative $G$ at zero. At every active positive coordinate, $1-\exp(-x)<x$ for $x>0$. A positive fixed point therefore requires $\rho(G)>1$ by multiplication by a positive left Perron vector. A nonzero boundary fixed point is excluded by irreducibility. When $\rho(G)\le1$, monotone iteration from $m$ decreases to zero and bounds all trajectories after one step. When $\rho(G)>1$, a sufficiently small positive multiple of the right Perron vector is a strict lower solution. Iteration from it and from $m$ gives positive fixed points. They coincide because $\Phi(\alpha x)<\alpha\Phi(x)$ for positive $x$ and $\alpha>1$ coordinatewise. Scaling either fixed point up to touch the other at one coordinate would contradict this inequality. Every strictly positive seed can be bounded below by a sufficiently small such lower solution. The upper bound applies after the first step. Here each generation is a fresh cohort with one common decision date.

**Economic lineage.** Data-Driven Automation treats data as a task-specific byproduct with spillovers, derives an automation frontier and studies endogenous capital accumulation. The economics of nonrival data explains why ownership affects access and why one record can support multiple users. Production-network economics establishes how substitution and bottlenecks propagate shocks. Organizing Intelligence distinguishes reproducible expertise from the capacity to coordinate it. Our question is which other firm can turn a given shift’s orders, experience or cash into a qualified and funded deployment that generates further experience of its own. The matrix and occupancy mathematics are established tools. [Farboodi, Koh and Xia](https://arxiv.org/abs/2606.10127) · [Jones and Tonetti](https://doi.org/10.1257/aer.20191330) · [Baqaee and Farhi](https://doi.org/10.3982/ECTA15202) · [Imas, Koh and Legg](https://arxiv.org/abs/2611.05417)

The [Python replication](replication.py) uses NumPy. It compares direct simulations of stocks and installation dates with the derived responses and checks capital adjustment and input demand independently. Its economies are illustrative.

[PDF reading edition](Learning_and_Capital_in_Robotic_Production.pdf) · [Applied foundations and proposed paper openings](../How_Deployment_Changes_Robot_Productivity.md)
