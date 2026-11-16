"""Exact synthetic checks of reconstructed financing mechanisms; not calibration."""
from fractions import Fraction as Q


def check():
    # Implementable deterministic pooling contract, including both outside options.
    cash=(Q(5),Q(1));contributions=(Q(3),Q(1));shares=(Q(5),Q(5))
    terminal=tuple(b-c+r for b,c,r in zip(cash,contributions,shares))
    assert terminal==(7,5) and all(t>=b for t,b in zip(terminal,cash))
    assert sum(contributions)==4 and sum(shares)==10
    # Holmstrom–Tirole: preserve the viability restriction for BOTH technologies.
    R=Q(10);private=Q(1);I=Q(15,2);A=Q(3,2)
    pledge=[]
    for high,low in [(Q(4,5),Q(2,5)),(Q(9,10),Q(16,25))]:
        assert high*R>I>low*R+private
        rent=private/(high-low)
        assert 0<=rent<=R and (high-low)*rent==private
        pledge.append(high*(R-rent))
    assert pledge==[Q(6),Q(72,13)] and pledge[0]>=I-A>pledge[1]
    # Bergemann–Hege: no-success Bayes updates and two independent value calculations.
    initial=alpha=Q(3,4);lam=Q(1,2);c=Q(4);delta=Q(9,10);path=[]
    while alpha*R>c:
        path.append(alpha)
        alpha=alpha*(1-lam)/(1-alpha*lam)
    assert path==[Q(3,4),Q(3,5),Q(3,7)] and alpha==Q(3,11)
    recursive=Q(0)
    for a in reversed(path):
        recursive=a*lam*R-c*lam+delta*(1-a*lam)*recursive
    direct=sum(delta**t*(initial*(1-lam)**t*lam*R-c*lam*((1-initial)+initial*(1-lam)**t))
               for t in range(len(path)))
    assert recursive==direct==Q(3781,1600)
    # Exact feasibility of terminal success-share interval, including threshold tie.
    for j in range(1,101):
        a=Q(j,100)
        lower=c/(a*R);upper=1-c/(a*R)
        assert (0<=lower<=upper<=1)==(a*R>=2*c)
    print('Pooling balances, both incentive examples, Bayesian path/value and 100 terminal share intervals verified.')


if __name__=='__main__':check()
