from fractions import Fraction as F

for N in [16,32,64]:
    vals=[]; audits=[]; checks=0
    for i in range(N//2,3*N//4+1):
        for j in range(N//2,3*N//4+1):
            for k in range(3*N//4-i+1):
                x,e,z=map(lambda v:F(v,N),(i,j,k)); m=F(1,2); w=r=F(3,4)
                a=[m-z,x-m+z,z,w-x-z,r-x,1-w-r+x]; b=[e,w-e,r-e,1-w-r+e]
                assert min(a+b)>=0 and sum(a)==sum(b)==1
                assert a[0]+a[1]==x and a[0]+a[2]==m and sum(a[:4])==w and a[0]+a[1]+a[4]==r
                g=F(3,2)+6*x+4*z; E=F(9,4)+6*e; vals.append((g,E,g-E)); checks+=1
                if x-e>=F(1,8) and z>=F(1,16):
                    d=-F(3,4)+F(47,8)*x-F(49,8)*e+F(15,4)*z
                    assert d>=F(5,64); audits.append((d,x,e,z))
    assert (min(v[0] for v in vals),max(v[0] for v in vals))==(F(9,2),F(6))
    assert (min(v[1] for v in vals),max(v[1] for v in vals))==(F(21,4),F(27,4))
    assert (min(v[2] for v in vals),max(v[2] for v in vals))==(-F(9,4),F(3,4))
    assert min(audits)==(F(5,64),F(11,16),F(9,16),F(1,16))
    print(N,checks,min(audits))
