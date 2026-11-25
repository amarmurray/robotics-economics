# The full-stack robotic firm

*A model extension to The Production of Capability · November 25, 2026*

Take one firm that designs and manufactures robots, trains their models, integrates each workcell, and operates its own deployments for customers. It owns its machines and chooses where to install them. Customers buy accepted service and specify which observations can be retained. Component suppliers, lenders, labor markets and buyers sit outside the boundary. Internal manufacture makes hardware design and the composition of the installed fleet choices of this firm. The same owner can redirect a field observation to a training run, a factory change, a retrofit, or a different integration procedure. Each route consumes real resources and changes what the firm will observe next.

## The objects and their clocks

| Object | What the firm chooses | What carries forward |
| --- | --- | --- |
| Factory and hardware | Tooling, designs, sensor placement, batch size, quality control | Production capacity, manufacturing yield and dated batches of particular vintages |
| Model and inquiry | Which episodes to retain, label and train on, which fresh test to run | Candidate policies and diagnostic procedures, indexed by task and compatible hardware |
| Integration and operation | Fixturing, site selection, release, dispatch, escalation, field retrofits | Qualified site–vintage–policy combinations, service obligations and the next distribution of experience |
| Working capital | Procurement, work in process, commissioning and the timing of collections | Dated commitments, receivables, liquid funds and feasible starts |

Tooling changes new builds after a lead time. A software release can reach many surviving machines, subject to validation. A retrofit draws on field crews and can displace customer work. A fixture can improve one site immediately and remove the very failure that once revealed a design defect. A digital agent can select tests or schedule crews within its information and authority. Its changes to routing also change the observations available to the next training run.

## One allocation problem

Let the state contain factory tooling and unfinished batches, installed stock by site and vintage, policy and evidence stocks, qualified configurations, support commitments, resources and cash. Given customer orders, the firm allocates factory time, field hours, engineering, compute and money jointly. A period proceeds through decisions with dated information.

1. Commit builds and research against the current backlog and cash. Fabrication produces conforming units with design-dependent yield. Commissioning, retirement and retrofit update the stock by vintage. A unit still awaiting acceptance cannot fill a qualified order.
2. Dispatch eligible machines or use a human fallback. Record attempts, failures, overrides, accepted output and unattempted orders. The law of retained observations depends on the hardware, policy, fixtures, routing, instrumentation and permission. Multiple records of the same event can carry little additional information.
3. Use available evidence to select and test physical, software and integration changes. Release a candidate on the configurations for which the required checks fit the available capacity. Record separately what was discovered, what passed, and what actually ran.
4. Collect according to contract milestones and service terms. Pay for inputs, labor and already committed equipment. New starts must be fundable on the dates payments fall due. Cash from accepted work can fund the next experiment or hardware batch, which changes subsequent exposure.

With state $x$, feasible joint allocation $a$, transition $T$ and shocks $\epsilon$, value is $V(x)=\max_a E[\pi(x,a,\epsilon)+\beta V(T(x,a,\epsilon))]$. Here $\pi$ is net cash flow to ownership under a consistent financing convention. Internal transfer prices cancel. Evidence earns its value through future differences in feasible cash flows. Counting an imputed sale of training data internally would count the same benefit twice. For physical $MPK_r$, add one commissioned unit of a specified vintage at a specified site, hold the policy, other stocks and order book fixed, reoptimize dispatch, and measure the vector of additional accepted orders per period. The investment value of building an additional unit includes downstream learning, qualification, financing and displacement along both optimized paths.

## A solved hardware–model feedback

Consider one remaining service horizon after one field-learning opportunity. Hold the source order and the target fleet fixed across designs. A mechanical fix eliminates a fraction $h$ of otherwise informative failures. Conditional on an unresolved exposure, severity and the chance that its record transfers are stable. For an exact single-source case let $p$ be the initial probability of a useful failure on a designated source opportunity and $q$ the conditional probability of capturing a usable record. The fix changes source yield from $pq$ to $(1-h)pq$. The horizon contains $N$ other compatible, reachable target opportunities. Given a captured record, the expected incremental saving per target is $b$, relative to continued ordinary learning, after local costs. Assume these target savings survive the source redesign, commitments allow reuse, and a missing record earns zero incremental saving. Let $G$ be discounted net direct service gain from the fix across the affected work, inclusive of design, build and installation expense. Target learning benefits are excluded from $G$.

Under the ordinary evidence route the design change is worth

$$G-\beta hpqNb.$$

The same reliability improvement can pay for a small fleet and be deferred by a large compatible fleet if $G$ is held fixed, for instance when it affects one source cell and the downstream installed base varies. If all target machines receive the redesign and their residual need for the learned correction changes, substitute the design-specific target value in each state. A mechanical fix that removes the problem everywhere has fundamentally different economics.

Suppose an instrument costing $C$ can recover a fraction $\lambda$ of the **useful records lost to the fix**, for example by measuring force precursors on otherwise successful picks. Baseline recording is already in $q$. With no other use for the instrument, the optimized value of redesign relative to the original setup is

$$G-\beta hpqNb+\max\{0,\beta\lambda hpqNb-C\}.$$

This follows by comparing the original machine, the redesigned machine alone and the redesigned machine with instrumentation. Measurement and mechanical reliability are complements here even though mechanical reliability and failure-based learning are substitutes. If $G<\beta hpqNb$ but $G>\beta(1-\lambda)hpqNb+C$, instrumentation changes which hardware the firm manufactures. The firm can ship a more reliable machine precisely because it found a way to learn from success. A sensor already valuable on the original machine must be offered to both designs. More generally the interaction is the difference in its value across the two optimized designs. All choices satisfy the same minimum service and safety requirements. An external reference cell, simulator or existing archive enters whichever alternative can use it.

## How the effect propagates

**Across vintages.** The target term generalizes to $\sum_j N_j b_j$, with $b_j$ conditional on compatibility, remaining economic life, local qualification and spare complementary capacity. A sensor on newly built machines can be worth installing because its records improve *older* machines that never receive the sensor. The reverse also occurs. An imminent retirement can extinguish much of the incentive to instrument the next batch. Holding factory unit cost and order volumes fixed, the age and compatibility of the installed base can change the bill of materials.

**Across production and finance.** A correction can increase accepted units per robot at a binding task, leave total output fixed at a downstream bottleneck, or release a field crew to commission another site. Earlier acceptance can advance collection. If a balance $B$ is released $\Delta t$ earlier, the improvement is $B\Delta t$ in dollar-periods. An additional factory start occurs only if the cash arrives before a binding payment and tooling, components, orders and commissioning also permit the start. Faster cash recovery can otherwise advance the same batch or leave physical output unchanged.

**Across future data.** More installations can increase observation opportunities while better execution removes informative failures per attempt. With independent rare events the expected count is proportional to attempts times informative-event frequency times usable capture. Growth in attempts can offset falling event frequency. For a particular design decision it is the probability of an otherwise missed, transferable discovery that matters. If every new installation repeats a known fixture, counts can rise while little new design information arrives. Site selection and instrumentation jointly determine which future bottlenecks the firm can even diagnose.

## Empirical discriminator and open equilibrium

On operationally acceptable cells, compare a scheduled mechanical improvement with and without recording precursors. Include old-design cells with both instrumentation states. Match order mix, model version, retained-data rights, validation budgets and available fallback. Measure attempts and event frequency per exposure, predictive value of recorded successes on fresh physical tests, accepted service on *unmodified* target vintages, and the dates of collections and factory starts. The proposed mechanism predicts a larger gain from instrumentation after the failure-suppressing redesign when precursor capture restores transferable evidence. If a shared archive already supplies those cases or precursor traces fail on fresh jobs, that interaction can disappear. Stagger at the level of shared training and validation, or explicitly track which groups receive each update.

The unresolved equilibrium is whether the firm specializes its next deployments to accelerate progress on a common design, or preserves atypical sites because their rare exposures redirect future hardware and policy. Answering that requires solving site entry, endogenous evidence and successive hardware vintages together with customer demand. The solved comparison identifies one marginal incentive within that larger choice.
