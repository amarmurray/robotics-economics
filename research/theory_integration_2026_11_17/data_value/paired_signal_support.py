#!/usr/bin/env python3
"""Exact finite audit of three-way qualification, report and demand coupling.
No empirical input, network certification or dollar calibration is supplied.
Run: python paired_signal_support.py
"""
from collections import defaultdict
from fractions import Fraction
import json

def z_interval(n, x, m):
    assert 0 <= x <= n and 0 <= m <= n
    return max(0, x + m - n), min(x, m)

def premium_units(q, x, m, z):
    assert z_interval(q,x,m)[0] <= z <= z_interval(q,x,m)[1]
    d_a = 2*z-m
    d_b = 2*x + m-q-2*z
    return abs(d_a) + abs(d_b) - abs(d_a+d_b)

def compatible_interval(n, q, x, m, x0, m0, agreement):
    """Sharp integer z_C interval conditional on C/non-C margins & global agreement."""
    n0 = n-q
    lo,hi = z_interval(q,x,m)
    lo0,hi0 = z_interval(n0,x0,m0)
    # agreement= n - (x+x0) - (m+m0) + 2*(z+z0)
    numerator = agreement-n+x+x0+m+m0
    if numerator % 2: return None
    total_z=numerator//2
    lo=max(lo,total_z-hi0)
    hi=min(hi,total_z-lo0)
    if lo>hi:return None
    return lo,hi

def sharp_premium_interval(q,x,m,lo,hi):
    # convex piecewise linear => maximum at endpoints;
    # minimum achieved at clipped roots or a plateau between them
    critical={lo,hi}
    for numerator in (m, 2*x+m-q):
        for z in (numerator//2, (numerator+1)//2):
            if lo<=z<=hi: critical.add(z)
    vals=[premium_units(q,x,m,z) for z in critical]
    return min(vals),max(vals)

def run():
    verified=0; worlds=0
    # Enumerate all integer contingency tables for C and non-C with 6 parent tokens.
    # Validate both feasible z support and sharp premium envelopes for all fixed observed margins.
    n=6
    for q in range(n+1):
        n0=n-q
        for x in range(q+1):
            for m in range(q+1):
                for x0 in range(n0+1):
                    for m0 in range(n0+1):
                        observed=defaultdict(list)
                        lo,hi=z_interval(q,x,m)
                        lo0,hi0=z_interval(n0,x0,m0)
                        for z in range(lo,hi+1):
                            for z0 in range(lo0,hi0+1):
                                agree=n-(x+x0)-(m+m0)+2*(z+z0)
                                observed[agree].append((z,z0,premium_units(q,x,m,z)))
                                worlds+=1
                        for agree,table in observed.items():
                            I=compatible_interval(n,q,x,m,x0,m0,agree)
                            assert I is not None
                            actual_z={z for z,z0,d in table}
                            assert actual_z==set(range(I[0],I[1]+1))
                            bound=sharp_premium_interval(q,x,m,*I)
                            assert bound==(min(d for _,_,d in table),max(d for _,_,d in table))
                            verified+=1
    # 16 parent tokens, 8 C and 8 outside. Margins of both groups symmetric.
    args=(16,8,4,4,4,4,12)
    I=compatible_interval(*args)
    assert I==(2,4)
    sharp=sharp_premium_interval(8,4,4,*I)
    assert sharp==(0,8)
    rows=[]
    for z in range(I[0],I[1]+1):
        z0=6-z
        cells_c=(z,4-z,4-z,8-4-4+z)
        cells_0=(z0,4-z0,4-z0,z0)
        assert sum(cells_c)==8 and sum(cells_0)==8
        assert 2*(z+z0)==12
        d=premium_units(8,4,4,z)
        rows.append(dict(triple_AA_C=z,AA_nonC=z0,group_C_cells_AA_AB_BA_BB=list(cells_c),group_nonC_cells_AA_AB_BA_BB=list(cells_0),gross_flexibility_premium=str(Fraction(d,16)),net_premium_after_hypothetical_cost_1_4=str(Fraction(d-4,16))))
    assert [r['gross_flexibility_premium'] for r in rows]==['0','1/4','1/2']
    # Two-world prior on endpoints, perfect safe shadow audit before hardware commitment.
    prior_audit_gain=(max(Fraction(0),Fraction(0)-Fraction(1,4))+max(Fraction(0),Fraction(1,2)-Fraction(1,4)))/2 - max(Fraction(0),(Fraction(0)+Fraction(1,2))/2-Fraction(1,4))
    assert prior_audit_gain==Fraction(1,8)
    return dict(status='pass',model='synthetic original-parent two-stratum C/notC',enumerated_joint_worlds=worlds,exhaustively_checked_margin_agreement_configs=verified,example_parent_units=16,example_known_pair_margins={'q':'1/2','x':'1/4','m':'1/4','x0':'1/4','m0':'1/4','overall_agreement':'3/4'},sharp_triple_AA_C_interval=['1/8','1/4'],sharp_flexibility_value_interval=['0','1/2'],example_worlds=rows,hypothetical_equal_prior_perfect_paired_audit_decision_gain='1/8',has_real_robot_or_buyer_measurements=False,has_signed_physical_policy=False,has_independent_novelty_review=False)
if __name__=='__main__':
    print(json.dumps(run(),indent=2))
