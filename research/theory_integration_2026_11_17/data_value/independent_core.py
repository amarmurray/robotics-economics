"""Independent stdlib verification of the main theoretical illustrations."""
from math import erf, sqrt, exp, pi

def quality(s, tau=1):
    return erf(tau/sqrt(2*s))

def variance(stock, source, ground, c):
    return 1/(.2+stock+source)+c/(1+ground)

def option(stock, budget=8):
    baseline=30*quality(variance(stock,0,0,4))
    best=(0, 'old',0,0)
    for name,c,fee in [('old',4,0),('new',.25,8)]:
        for source in range(budget-fee+1):
            for ground in range(budget-fee-source+1):
                v=30*quality(variance(stock,source,ground,c))-baseline-fee-source-ground
                if v>best[0]: best=(v,name,source,ground)
    return best

def evsi(prior=.5,accuracy=.8, high=7,low=-1,outside=5):
    base=max(prior*high+(1-prior)*low,outside)
    after=0
    for good in (True, False):
        h=accuracy if good else 1-accuracy
        l=1-h
        weight=prior*h+(1-prior)*l
        posterior=prior*h/weight
        after+=weight*max(posterior*high+(1-posterior)*low,outside)
    return after-base

if __name__=='__main__':
    assert option(0)[1:]==('old',2,4)
    assert option(2)[1:]==('new',0,0)
    assert abs(evsi()-.2)<1e-12
    # Normal threshold derivative changes sign at S=tau^2/3.
    second=lambda s: exp(-1/(2*s))/(sqrt(2*pi)*2*s**3.5)*(3*s-1)
    assert second(1)>0>second(.1)
    print('Independent Gaussian, exact-discrete-menu, curvature and EVSI checks passed')
    print(option(0),option(2),evsi())
