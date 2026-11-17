"""Synthetic macro/micro observational-equivalence benchmark. Not BEA observations.
Python 3.10+ standard library only. Run: python -m unittest -v test_sector_bridge
"""
from fractions import Fraction as F

SECTORS=('materials','manufacturing','health_services')
USE=((F(5),F(30),F(10)),(F(10),F(10),F(10)),(F(5),F(5),F(15)))
OUTPUT=(F(100),)*3
FINAL=(F(55),F(70),F(75))
VALUE_ADDED=(F(80),F(55),F(65))
LABOR=(F(40),)*3
TASK_E1=(F(0),F(30),F(10))
TASK_E2=(F(0),F(10),F(30))

def validate():
    for i in range(3):
        assert sum(USE[i])+FINAL[i]==OUTPUT[i], ('row',i)
        assert sum(USE[j][i] for j in range(3))+VALUE_ADDED[i]==OUTPUT[i],('column',i)
        assert 0<=LABOR[i]<=VALUE_ADDED[i]

def opportunities(eligible,fee=F(15),provider_cost=F(12)):
    validate()
    assert all(0<=e<=l for e,l in zip(eligible,LABOR))
    return {name:{'eligible':eligible[i],'retained':LABOR[i]-eligible[i],
                  'customer_buys':eligible[i]>fee,
                  'customer_gain':max(F(0),eligible[i]-fee),
                  'provider_profit':fee-provider_cost if eligible[i]>fee else F(0)}
            for i,name in enumerate(SECTORS)}

def propagate(final_demand_delta):
    """Exact square synthetic industry matrix, NOT raw commodity-by-industry BEA Use."""
    validate()
    n=3
    a=[[USE[i][j]/OUTPUT[j] for j in range(n)] for i in range(n)]
    m=[[F(i==j)-a[i][j] for j in range(n)]+[F(final_demand_delta[i])] for i in range(n)]
    for k in range(n):
        p=next((i for i in range(k,n) if m[i][k]),None)
        if p is None:raise ValueError('Singular I-A')
        m[k],m[p]=m[p],m[k]
        q=m[k][k];m[k]=[v/q for v in m[k]]
        for i in range(n):
            if i!=k:
                t=m[i][k];m[i]=[v-t*w for v,w in zip(m[i],m[k])]
    return tuple(row[-1] for row in m)

def conditional_feedback(eligible,destination,fee=F(15),beta=F(10),pass_through=F(1)):
    """Illustration only: matched-output avoided wage less fee / sector gross output."""
    if not 0<=pass_through<=1 or beta<0:raise ValueError('Invalid response')
    i=SECTORS.index(destination)
    gain=opportunities(eligible,fee)[destination]['customer_gain']
    dy=beta*pass_through*gain/OUTPUT[i]
    shock=[F(0)]*3;shock[i]=dy
    return dy,propagate(shock)

if __name__=='__main__':
    validate()
    for name,tasks,sector in (('E1',TASK_E1,'manufacturing'),('E2',TASK_E2,'health_services')):
        dy,dx=conditional_feedback(tasks,sector)
        print(name, 'customer',opportunities(tasks),'final demand',dy,'gross output',dx)
