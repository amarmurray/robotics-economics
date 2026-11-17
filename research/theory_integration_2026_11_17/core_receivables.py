"""Exact analytical submodel: dated A collections and B qualification.

All units and hazards synthetic. Separate from the optional SciPy finite-slot
production-displacement LP in receivable_model.py.
"""
from math import exp, expm1


def effort(h, K, c, v, d):
    """Optimal cumulative B exposure if A production is never displaced."""
    if min(h,K,c,v,d) < 0 or c == 0:
        if c == 0 and min(h,K,v,d)>=0: return h
        raise ValueError('invalid nonnegative inputs')
    return min(h, K/c + min(1.,v/c)*max(0.,h-d))


def survival_completion(h, K, c, v, d, b):
    """Pr(B acquired before h) allowing pause and A collections."""
    if b < 0: raise ValueError('negative hazard')
    return -expm1(-b*effort(h,K,c,v,d))


def sustainable_share(c,v,eta):
    """Limit share of B learning when activity displaces A production."""
    if c<=0 or v<0 or not 0<=eta<=1: raise ValueError('invalid inputs')
    return min(1.,v/(c+v*(1-eta)))


def full_effort_bridge(h,K,c,v,d,eta):
    """Minimum immediate A-stage cash advance to attempt B nonstop to h."""
    if min(h,K,c,v,d)<0 or not 0<=eta<=1: raise ValueError('invalid')
    return max(0.,c*min(d,h)-K,c*h-eta*v*max(0.,h-d)-K)


def pledgeable_full_effort(h,b,W,beta,d_ab=0.):
    """Risk-neutral zero-discount expected lender claim on AB collected cash."""
    if min(h,b,W,beta,d_ab)<0 or beta>1: raise ValueError('invalid')
    x=max(0.,h-d_ab)
    if b==0:return 0.
    return beta*W*(x+expm1(-b*x)/b)


def staged_probability(T,B,cA,cB,a,b,v,d,steps=20000):
    """Midpoint-integrated A success density then optimal separable B learning.

    Numeric quadrature with step count fixed for portability; not an exact
    integral evaluator. Compare with the SciPy implementation in the archive.
    """
    if min(T,B,cA,cB,a,b,v,d)<0 or cA==0 or steps<1:raise ValueError('invalid')
    cap=min(T,B/cA)
    ds=cap/steps
    total=0.
    for i in range(steps):
        s=(i+.5)*ds
        total+=a*exp(-a*s)*survival_completion(T-s,B-cA*s,cB,v,d,b)*ds
    return total
