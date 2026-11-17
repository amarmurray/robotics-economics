"""Research kernel for qualification networks and economic learning returns.

Integer allocation and finite qualification lotteries use exact rational arithmetic.
LP certificates use scipy/HiGHS; learning curves use floating-point elementary math.
These are mathematical/synthetic checks, not calibrated robotics parameters.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
from math import exp, expm1, factorial, isfinite, log, log1p, prod
import json
from pathlib import Path


@dataclass(frozen=True)
class Network:
    capacity: tuple[int, ...]
    demand: tuple[int, ...]
    value: tuple[F, ...]

    def __post_init__(self):
        if not self.capacity or not self.demand or len(self.demand) != len(self.value):
            raise ValueError('Nonempty resources and aligned task demand/value required')
        if any(type(x) is not int or x < 0 for x in self.capacity + self.demand):
            raise ValueError('Exact allocation requires nonnegative integer capacities/demands')
        if sum(self.capacity) > 18 or any(v < 0 for v in self.value):
            raise ValueError('Enumeration limited to 18 supply units; values nonnegative')

    def edges(self):
        return tuple(product(range(len(self.capacity)), range(len(self.demand))))

    def check(self, edges):
        es = frozenset(edges)
        if not es.issubset(self.edges()):
            raise ValueError('Edge endpoint outside the specified production network')
        return es

    def solve(self, edges) -> F:
        """Exact maximum accepted-service contribution, including idle alternative."""
        es = self.check(edges)
        slots = tuple(i for i, k in enumerate(self.capacity) for _ in range(k))
        choices = {i: tuple(j for j in range(len(self.demand)) if (i,j) in es)
                   for i in range(len(self.capacity))}
        @lru_cache(None)
        def dp(t, remaining):
            if t == len(slots):
                return F(0)
            best = dp(t+1, remaining)
            for j in choices[slots[t]]:
                if remaining[j]:
                    rest = list(remaining); rest[j] -= 1
                    best = max(best, self.value[j] + dp(t+1, tuple(rest)))
            return best
        return F(dp(0, self.demand))

    def table(self, base, candidates):
        base = self.check(base); candidates = tuple(candidates)
        self.check(candidates)
        if len(set(candidates)) != len(candidates) or base.intersection(candidates):
            raise ValueError('Candidate qualifications must be distinct and absent from base')
        return tuple(self.solve(base | {e for i,e in enumerate(candidates) if mask >> i & 1})
                     for mask in range(1 << len(candidates)))


def chain(k: int):
    """k complementary missing links; all incumbently served tasks worth > final task."""
    if type(k) is not int or k < 1 or k > 18:
        raise ValueError('Chain length in 1..18 required')
    net = Network((1,)*k, (1,)*k, tuple(F(k-j) for j in range(k)))
    base = frozenset((i, i-1) for i in range(1,k))
    candidates = tuple((i,i) for i in range(k))
    return net, base, candidates


def _check_table(values):
    n = (len(values)-1).bit_length()
    if len(values) != 1 << n:
        raise ValueError('Table must have 2**n entries in bit-mask order')
    if any(values[m | (1 << i)] < values[m]
           for m in range(len(values)) for i in range(n) if not m >> i & 1):
        raise ValueError('Optional qualification must not reduce attainable value')
    return n


def expected_gain(values, probabilities):
    n = _check_table(values)
    ps = tuple(F(p) for p in probabilities)
    if len(ps) != n or any(p < 0 or p > 1 for p in ps):
        raise ValueError('One valid activation probability per qualification required')
    return sum((values[m]-values[0]) * prod(ps[i] if m >> i & 1 else 1-ps[i]
               for i in range(n)) for m in range(1 << n))


def leading_order(values, rates=None, exponents=None):
    """Exact leading exponent/coefficient for independent p_e(t)~rate_e*t**beta_e."""
    n = _check_table(values)
    rates = tuple(F(x) for x in (rates if rates is not None else [1]*n))
    exponents = tuple(F(x) for x in (exponents if exponents is not None else [1]*n))
    if len(rates) != n or len(exponents) != n or any(x < 0 for x in rates) or any(x <= 0 for x in exponents):
        raise ValueError('Nonnegative rates and positive exponents required')
    terms = []
    for mask in range(1, 1 << n):
        ids = [i for i in range(n) if mask >> i & 1]
        if values[mask] > values[0] and all(rates[i] > 0 for i in ids):
            terms.append((sum(exponents[i] for i in ids),
                          (values[mask]-values[0])*prod(rates[i] for i in ids), mask))
    if not terms:
        return None, F(0), ()
    power = min(t[0] for t in terms)
    active = [t for t in terms if t[0] == power]
    return power, sum(t[1] for t in active), tuple(t[2] for t in active)


def joint_two(values, p1, p2, joint):
    if len(values) != 4:
        raise ValueError('Two-qualification table required')
    _check_table(values)
    p1,p2,joint = map(F,(p1,p2,joint))
    if not (0 <= p1 <= 1 and 0 <= p2 <= 1 and max(F(0),p1+p2-1) <= joint <= min(p1,p2)):
        raise ValueError('Joint probability violates Frechet bounds')
    kappa = values[3]-values[1]-values[2]+values[0]
    return values[0]+(values[1]-values[0])*p1+(values[2]-values[0])*p2+kappa*joint


def learning_allocation(budget, slopes, prior=None):
    """Optimal precommitted allocation for independent p_i=1-exp(-a_i*(z_i+u_i)).

    KKT water-filling for the log of the probability all required links qualify.
    Constant positive payoff multiplier does not change the budget-conditional allocation.
    """
    budget=float(budget); slopes=tuple(map(float,slopes))
    prior=tuple(map(float,prior if prior is not None else [0]*len(slopes)))
    if not isfinite(budget) or budget < 0 or not slopes or len(prior)!=len(slopes):
        raise ValueError('Finite nonnegative budget and aligned nonempty vectors required')
    if any(not isfinite(a) or a <= 0 for a in slopes) or any(not isfinite(z) or z < 0 for z in prior):
        raise ValueError('Finite positive slopes and nonnegative prior experience required')
    if budget == 0:
        return (0.0,)*len(slopes)
    def allocation(lam):
        return tuple(max(0.0,log1p(a/lam)/a-z) for a,z in zip(slopes,prior))
    hi=1.0
    while sum(allocation(hi)) > budget:
        hi *= 2
        if not isfinite(hi):
            raise ArithmeticError('Budget too small for stable floating-point allocation')
    lo=0.0
    for _ in range(180):
        mid=(lo+hi)/2
        if sum(allocation(mid)) > budget: lo=mid
        else: hi=mid
    return allocation(hi)


def success_probability(effort, slopes, prior=None):
    xs=tuple(map(float,effort)); aa=tuple(map(float,slopes))
    zz=tuple(map(float,prior if prior is not None else [0]*len(xs)))
    if not xs or len(xs)!=len(aa) or len(xs)!=len(zz) or any(x<0 for x in xs+zz) or any(a<=0 for a in aa):
        raise ValueError('Aligned nonnegative effort/prior and positive slopes required')
    return prod(-expm1(-a*(z+x)) for x,a,z in zip(xs,aa,zz))


def homogeneous_probability(budget,k,a=1.0):
    if budget < 0 or type(k) is not int or k<1 or a<=0:
        raise ValueError('Nonnegative budget, positive integer k and a required')
    return (-expm1(-a*budget/k))**k


def homogeneous_derivatives(budget,k,a=1.0):
    if k<1 or a<=0 or budget<0:
        raise ValueError('Invalid homogeneous learning parameters')
    y=exp(-a*budget/k)
    first=a*y*(1-y)**(k-1)
    if k==1: second=-a*a*y
    elif k==2 and budget==0: second=a*a/2
    else: second=(a*a/k)*y*(1-y)**(k-2)*(k*y-1)
    return first,second


def break_even(k,a=1.0):
    """Minimum gross reward W for positive net reward W*P(R)-R, no borrowing.

    For k=1 the zero-effort infimum applies; for k>1 positive root exp(x)=1+k*x.
    """
    if type(k) is not int or k<1 or a<=0:
        raise ValueError('Positive integer k and a required')
    if k==1:
        return {'x':0.0,'effort':0.0,'reward':1/a}
    lo=1e-8; hi=max(2.0,2*log(k)+2)
    for _ in range(180):
        mid=(lo+hi)/2
        if expm1(mid)-k*mid>0: hi=mid
        else: lo=mid
    x=(lo+hi)/2; effort=k*x/a
    return {'x':x,'effort':effort,'reward':effort/(-expm1(-x))**k}


def optimal_total(budget,reward,k,a=1.0):
    """Global homogeneous precommitted effort choice, including no investment."""
    if budget<0 or reward<0 or k<1 or a<=0:
        raise ValueError('Invalid effort/reward parameters')
    def gain(r): return reward*homogeneous_probability(r,k,a)-r
    candidates=[0.0,float(budget)]
    if k==1:
        if reward*a>1: candidates.append(min(float(budget),log(reward*a)/a))
    else:
        inflection=k*log(k)/a
        if reward*homogeneous_derivatives(inflection,k,a)[0]>1:
            lo=inflection; hi=max(2*inflection,1.0)
            while reward*homogeneous_derivatives(hi,k,a)[0]>1: hi*=2
            for _ in range(180):
                mid=(lo+hi)/2
                if reward*homogeneous_derivatives(mid,k,a)[0]>1: lo=mid
                else: hi=mid
            peak=(lo+hi)/2
            if peak<=budget: candidates.append(peak)
    r=max(candidates,key=lambda x:(gain(x),-x))
    if gain(r)<1e-12: r=0.0
    return {'effort':r,'gain':gain(r),'success_probability':homogeneous_probability(r,k,a)}


def rational_probability(budget,k,a=1.0):
    """Alternative concave technical response p(u)=a*u/(1+a*u)."""
    if budget<0 or type(k) is not int or k<1 or a<=0:
        raise ValueError('Invalid rational-learning parameters')
    return (a*budget/(k+a*budget))**k


def rational_break_even(k,a=1.0):
    if type(k) is not int or k<1 or a<=0:
        raise ValueError('Invalid rational-learning parameters')
    if k==1: return {'effort':0.0,'reward':1/a}
    effort=k*(k-1)/a
    return {'effort':effort,'reward':effort/rational_probability(effort,k,a)}


def adaptive_gross(values,rates,budget):
    """Numerical Bellman-ODE solution for observed, retained independent Exp acquisitions.

    One unit of effort can target one missing qualification at a time. Known
    rates; no cost penalty inside gross reward. Does not model joint acquisitions.
    """
    from scipy.integrate import solve_ivp
    import numpy as np
    n=_check_table(values); rates=tuple(map(float,rates))
    if n!=len(rates) or any(a<=0 for a in rates) or budget<0:
        raise ValueError('Aligned positive rates and nonnegative budget required')
    initial=np.array(list(map(float,values)))
    if budget==0: return float(initial[0])
    def rhs(t,y):
        out=np.zeros(len(y))
        for mask in range(len(y)):
            out[mask]=max([0.0]+[rates[i]*(y[mask|(1<<i)]-y[mask])
                         for i in range(n) if not mask>>i&1])
        return out
    r=solve_ivp(rhs,(0,float(budget)),initial,rtol=1e-10,atol=1e-13,max_step=min(.02,float(budget)/10))
    if not r.success: raise ArithmeticError(r.message)
    return float(r.y[0,-1])


def adaptive_chain(budget,reward,k,a=1.0):
    """Optimal cost-aware homogeneous retained-qualification policy.

    Each missing qualification arrives after Exp(a) units of paid effort;
    successes are observed/retained. Total paid effort is at most budget.
    Stop is available; no calendar discount, demand drift, or borrowing.
    Solves the triangular Bellman ODE with exponential-polynomial pieces.
    """
    if budget<0 or reward<0 or type(k) is not int or k<1 or a<=0:
        raise ValueError('Invalid adaptive-chain parameters')
    v=a*reward; tau=a*budget
    def integral(poly): return [0.0]+[c/(i+1) for i,c in enumerate(poly)]
    def evaluate(poly,x):
        out=0.0
        for c in reversed(poly): out=out*x+c
        return out
    def at(level,x,kind='value'):
        if level['m']==0: return {'value':v,'probability':1.0,'cost':0.0}[kind]
        if not level['available'] or x<=level['start']: return 0.0
        constant={'value':v-level['m'],'probability':1.0,'cost':float(level['m'])}[kind]
        return constant+exp(-x)*evaluate(level[kind],x)
    levels=[{'m':0,'available':True,'start':0.0,'value':[], 'probability':[], 'cost':[]}]
    for m in range(1,k+1):
        previous=levels[-1]
        if v<=m:
            levels.append({'m':m,'available':False,'start':None,'value':[], 'probability':[], 'cost':[]})
            continue
        if m==1: start=0.0
        else:
            lo=previous['start']; hi=max(lo+1,1.0)
            while at(previous,hi)<1:
                hi*=2
                if hi>700: raise ArithmeticError('Threshold beyond stable exponential-polynomial domain')
            for _ in range(180):
                mid=(lo+hi)/2
                if at(previous,mid)<1: lo=mid
                else: hi=mid
            start=(lo+hi)/2
        level={'m':m,'available':True,'start':start}
        for kind,constant in (('value',v-m),('probability',1.),('cost',float(m))):
            poly=integral(previous[kind])
            poly[0]-=evaluate(poly,start)+constant*exp(start)
            level[kind]=poly
        levels.append(level)
    last=levels[-1]
    gain=at(last,tau)/a; probability=at(last,tau,'probability'); cost=at(last,tau,'cost')/a
    # Tiny cancellation noise at a threshold is not a negative optimal value.
    return {'gain':max(0.0,gain),'success_probability':max(0.0,probability),
            'expected_expenditure':max(0.0,cost),
            'start_budget':last['start']/a if last['available'] else None,
            'thresholds':[z['start']/a if z['available'] else None for z in levels[1:]],
            'unlimited_budget_value':max(0.0,reward-k/a)}


def sequential_success(budget,k,a=1.0):
    """Continue one qualification at a time, retaining success; exponential effort thresholds.

    P(sum of k independent Exp(a) thresholds <= budget). Not a general optimal
    stopping theorem or an empirical learning technology. scipy gammainc is stable.
    """
    if budget<0 or k<1 or a<=0: raise ValueError('Invalid sequential parameters')
    from scipy.special import gammainc
    return float(gammainc(k,a*budget))


def lp_value(A,b,c):
    import numpy as np
    from scipy.optimize import linprog
    A=np.asarray(A,dtype=float); b=np.asarray(b,dtype=float); c=np.asarray(c,dtype=float)
    if A.shape != (len(b),len(c)) or not all(np.isfinite(x).all() for x in (A,b,c)):
        raise ValueError('Finite aligned LP arrays required')
    if not len(c): return 0.0
    r=linprog(-c,A_ub=A,b_ub=b,bounds=(0,None),method='highs')
    if not r.success: raise ValueError(f'LP infeasible/unbounded or solver failure: {r.message}')
    return -float(r.fun)


def common_certificate(A,b,c,newA,newc):
    """Find ONE old optimal dual supporting all new recipes; numerical certificate."""
    import numpy as np
    from scipy.optimize import linprog
    A=np.asarray(A,dtype=float); b=np.asarray(b,dtype=float); c=np.asarray(c,dtype=float)
    N=np.asarray(newA,dtype=float); d=np.asarray(newc,dtype=float)
    old=lp_value(A,b,c)
    if N.shape != (len(b),len(d)): raise ValueError('New recipes have wrong dimensions')
    allA=np.column_stack((A,N)); allc=np.concatenate((c,d))
    r=linprog(np.zeros(len(b)), A_ub=-allA.T,b_ub=-allc,
              A_eq=b.reshape(1,-1),b_eq=[old],bounds=(0,None),method='highs')
    if r.status not in (0,2): raise ArithmeticError(r.message)
    return {'exists':r.status==0,'dual':r.x.tolist() if r.success else None,
            'old_value':old,'new_value':lp_value(allA,b,allc)}


def network_arrays(net,edges):
    import numpy as np
    es=tuple(sorted(net.check(edges)))
    A=np.zeros((len(net.capacity)+len(net.demand),len(es)))
    for col,(i,j) in enumerate(es): A[i,col]=1; A[len(net.capacity)+j,col]=1
    return A,np.array(net.capacity+net.demand,dtype=float),np.array([float(net.value[j]) for i,j in es])


def jsonable(x):
    if isinstance(x,F): return {'exact':str(x),'decimal':float(x)}
    if isinstance(x,dict): return {str(k):jsonable(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)): return [jsonable(v) for v in x]
    return x


def results():
    net,base,cand=chain(3); values=net.table(base,cand)
    richer=Network(net.capacity,(2,1,1),net.value)
    rvalues=richer.table(base,cand)
    chain2,b2,c2=chain(2); v2=chain2.table(b2,c2)
    substitute=Network((1,),(1,1),(F(1),F(1))).table((),((0,0),(0,1)))
    A,b,c=network_arrays(chain2,b2)
    certificates=[]
    for selected in ((c2[0],),(c2[1],),c2):
        newA,_,newc=network_arrays(chain2,selected)
        certificates.append(common_certificate(A,b,c,newA,newc))
    return jsonable({
        'status':'Conditional mathematical results and synthetic checks; no empirical calibration or publication-novelty claim',
        'chain3':{'values_by_mask':values,'leading_order':leading_order(values),
                  'higher_local_demand_values':rvalues,'higher_local_demand_order':leading_order(rvalues)},
        'old_optimal_dual_common_certificate':certificates,
        'dependence':{'marginals':'1/5 each','joint_lower':F(0),'joint_independent':F(1,25),'joint_upper':F(1,5),
            'complementary_gains':[joint_two(v2,F(1,5),F(1,5),q)-v2[0] for q in (F(0),F(1,25),F(1,5))],
            'substitute_gains':[joint_two(substitute,F(1,5),F(1,5),q) for q in (F(0),F(1,25),F(1,5))]},
        'learning_thresholds':{k:break_even(k) for k in (1,2,3,4,6)},
        'alternative_response_thresholds':{k:rational_break_even(k) for k in (1,2,3,4,6)},
        'reward10_k3':{B:optimal_total(B,10,3) for B in (0,1,2,3,4,5,6,10)},
        'adaptive_reward10_k3':{B:adaptive_chain(B,10,3) for B in (0,1,2,3,4,5,6,10)},
        'batch_sequential_k3':{B:{'batch':homogeneous_probability(B,3),'sequential':sequential_success(B,3)} for B in (0.01,0.1,0.5,1,2,4)},
        'heterogeneous_learning':{'slopes':[0.5,1,2],'budget':3,
             'allocation':learning_allocation(3,[0.5,1,2]),
             'with_prior':[2,0,0], 'allocation_with_prior':learning_allocation(3,[0.5,1,2],[2,0,0])},
    })


if __name__=='__main__':
    import argparse
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=Path(__file__).with_name('results.json'))
    args=parser.parse_args()
    args.output.write_text(json.dumps(results(),indent=2,sort_keys=True)+'\n')
    print(f'Wrote {args.output}')
