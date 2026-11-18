# Instructor solutions — coupled transfer and customer evidence

**Separate from [student exercises](COUPLED_IDENTIFICATION_EXERCISES.md), 18 November 2026.**

### 1. Sharp coupled law and dual

For types (H,D), (H,not D), (not H,D), (not H,not D), the masses are (t,.5−t,.5−t,t). Nonnegativity means 0<=t<=.5. R=5+8t, G=8−2t, so R−G=10t−3 in [−3,2]. At t=0 the masses are (0,.5,.5,0) and the difference is −3; at t=.5 they are (.5,0,0,.5) and difference is 2. A valid typewise dual lower certificate is d(type)>=−2−2D: typewise d=(6,−2,−4,−2), while RHS=(-4,-2,-4,-2). Taking expectations gives −2−2(.5)=−3, meeting the primal.

### 2. Maximin versus regret

For R fraction x, J=8−3x+(10x−2)t. If x<=.2, worst t=.5 and floor 7+2x; if x>=.2, worst t=0 and floor 8−3x. Equalizing gives maximin x=.2 and guarantee 7.4. G (7 minimum), E (6), S (5) cannot improve it: at t=.3 all are <=7.4. Clairvoyant G is preferable when t<.3, R when t>.3. Worst regret of x is max{3x,2(1−x)}, minimized x=.4 with regret 1.2; its production floor is 6.8, while maximin x=.2 has worst regret 1.6. Robot indivisibility, site-correlated demand, common training, scarce human sharing or mixing prohibitions defeat linear fractional feasibility.

### 3. Population oracle value

With indivisible investment, best pre-oracle pure maximin is G=7. Revealed t permits choosing max(R,G) for each t; its worst t=.3 yields 7.4, so robust gross gain .4, before audit cost. With linear fractional mixing, ex-ante x=.2 already guarantees 7.4, and t=.3 bounds the oracle worst value by 7.4; gain zero. The oracle gives **population** t, not individual H; Bayesian priors over t, per-customer signals, endogenously acquired qualifications and alternative risk criteria yield different information values.

### 4. Calibrated report

Let s=.9, f=.1. Conditional-invariance across D gives m=.1*.5+(.9−.1)t=.05+.8t. Thus t in [(.34−.05)/.8,(.40−.05)/.8]=[.3625,.4375]. R−G in [10*.3625−3,10*.4375−3]=[.625,1.375], strictly R-favoring. If s/f depend on D, the inversion can be invalid; if H is defined only by an unapproved physical attempt, Z cannot be presumed safe or identified without a different valid bridge.

### 5. Rare unsafe tail and valuation chain

Mean operator use is .9999*1+.0001*3=1.0002, below 2, but positive support at 3 violates the hard pathwise cap. An authorized **preattempt** abort/certified recovery at <=2 can be considered, with separately validated reporting properties. Economic valuation must link exact source/controller treatment to future *held-out whole-service* acceptance and recovery-feasible production, then to registered customer opportunities/orders/captured net contribution relative to old controller, specialist, changed body and productive free-data options. Current production displacement, rights, curation and training cost enter once; future data improves Q and hence continuation V and is not an added data sale premium absent an actual separate right/contract.