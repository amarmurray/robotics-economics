#!/usr/bin/env python3
"""Exact synthetic two-service qualified production, no field calibration.

Run: python nonseparable_robot_demand.py
Only Python stdlib; every optimum enumerates all polygon vertices, edge stationary
points, and the unconstrained stationary point of a strictly concave quadratic.
"""
from fractions import Fraction as F
from itertools import combinations
import json


def feasible(x, y, cap_a, cap_b, op, ua):
    return x >= 0 and y >= 0 and x <= cap_a and y <= cap_b and ua*x + y <= op


def gross(x, y, a, b, gamma):
    return a*x + b*y - 2*x*x - 2*y*y - 2*gamma*x*y


def maximum(gamma, cap_a, op, ua=F(1), cap_b=F(1)):
    a, b = F(9) + gamma/F(2), F(7) + gamma/F(2)
    # m*x+n*y=k, with the other side the permissible halfspace.
    edges = [(F(1),F(0),F(0)), (F(1),F(0),cap_a),
             (F(0),F(1),F(0)), (F(0),F(1),cap_b), (ua,F(1),op)]
    candidates = []
    det = F(4) - gamma*gamma
    candidates.append(((2*a-gamma*b)/(2*det), (2*b-gamma*a)/(2*det)))
    for (m,n,k),(r,s,l) in combinations(edges,2):
        d = m*s-n*r
        if d:
            candidates.append(((k*s-n*l)/d,(m*l-k*r)/d))
    for m,n,k in edges:
        x0,y0 = ((k/m,F(0)) if m else (F(0),k/n))
        tx,ty=n,-m
        directional=(a-4*x0-2*gamma*y0)*tx+(b-4*y0-2*gamma*x0)*ty
        curvature=4*(tx*tx+ty*ty+gamma*tx*ty)
        t=directional/curvature
        candidates.append((x0+tx*t,y0+ty*t))
    valid=[(gross(x,y,a,b,gamma),x,y) for x,y in candidates if feasible(x,y,cap_a,cap_b,op,ua)]
    return max(valid)


def fstr(x): return str(x)


def main():
    costs={"R":F(0),"X":F(1,4),"G":F(11,10),"E":F(11,5)}
    policies={"R":(F(1,2),F(1),F(1)),
              "X":(F(1),F(1),F(1)),
              "G":(F(1,2),F(1),F(1,2)),
              "E":(F(1,2),F(3,2),F(1))}
    results={}
    for gamma in (F(-1),F(1)):
        a,b=F(9)+gamma/2,F(7)+gamma/2
        # Both worlds display the same accepted complete-service mix and prices.
        assert (a-2*F(1,2)-gamma*F(1,2),b-2*F(1,2)-gamma*F(1,2))==(8,6)
        world={}
        for name,(ca,op,ua) in policies.items():
            value,x,y=maximum(gamma,ca,op,ua)
            world[name]={"q_a":fstr(x),"q_b":fstr(y),"gross":fstr(value),"net":fstr(value-costs[name])}
        results[f"gamma_{gamma}"]=world
    neg,pos=results["gamma_-1"],results["gamma_1"]
    assert [(neg[p]["gross"],pos[p]["gross"]) for p in ("R","X","G","E")]==[("7","7"),("43/6","15/2"),("33/4","8"),("37/4","35/4")]
    assert (neg["G"]["net"],pos["X"]["net"])==("143/20","29/4")
    assert F(neg["G"]["net"]) > max(F(neg[k]["net"]) for k in ("R","X","E"))
    assert F(pos["X"]["net"]) > max(F(pos[k]["net"]) for k in ("R","G","E"))
    # Entire supported cross-demand interval, not only a fresh parameter draw.
    for n in range(-40,41):
        gamma=F(n,40)
        exact_x=(F(3)-gamma)/(F(4)-2*gamma)
        formulas={"R":F(7),
                  "X":F(5)+gamma/2+(F(3)-gamma)**2/(F(4)-2*gamma),
                  "G":(F(65)-gamma)/8,
                  "E":F(9)-gamma/4}
        for p,(ca,op,ua) in policies.items():
            value,x,y=maximum(gamma,ca,op,ua)
            assert value==formulas[p]
            if p=="X": assert (x,y)==(exact_x,F(1)-exact_x)
        diff=formulas["X"]-costs["X"]-formulas["G"]+costs["G"]
        assert diff==(5*gamma*gamma-21*gamma+2)/(40*(gamma-2))
        ranked={p:formulas[p]-costs[p] for p in policies}
        assert max(ranked,key=ranked.get)==("X" if diff>0 else "G")
        # A risk-neutral, noninterfering ex-ante X/G lottery can hedge a common gamma.
        half_mix=(ranked["X"]+ranked["G"])/2
        assert half_mix==F(561,80)+gamma*gamma/(16*(2-gamma))
        assert half_mix>=F(561,80)>F(7)
    # G and E both release the same operator constraint in the two-service world.
    for gamma in (F(-1),F(1)):
        vge,_,_=maximum(gamma,F(1,2),F(3,2),F(1,2))
        vG=F(results[f"gamma_{gamma}"]["G"]["gross"])
        vE=F(results[f"gamma_{gamma}"]["E"]["gross"])
        vR=F(results[f"gamma_{gamma}"]["R"]["gross"])
        assert vge == vE
        assert vge-vG-vE+vR < 0
    # By contrast, each accepted job needs both tasks; production is Leontief.
    p,O,u,delta,e=F(8),F(1),F(2),F(1,2),F(1,2)
    bundled=lambda O,u: p*min(F(1),O/u)
    cross=bundled(O+e,u-delta)-bundled(O,u-delta)-bundled(O+e,u)+bundled(O,u)
    assert cross==F(2,3)
    results["joint_qualification"]={"gross_interaction_G_E":fstr(cross)}
    print(json.dumps({"type":"exact_synthetic_two_service_demand","scenario":results,"field_calibrated":False},indent=2,sort_keys=True))

if __name__=="__main__": main()
