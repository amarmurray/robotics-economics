import unittest
import numpy as np
from study import payoff, policy, tape, FEE
from renewal import solve, evaluate, fixed_frontier


class ReferenceChecks(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.pay = payoff()
        cls.data = tape(89722,350,"ordinary")

    def test_observable_distribution(self):
        for pos in (.07,.11):
            laws=[]
            for true,p in ((False,.25),(True,.75)):
                bp=(.19 if pos==.11 else .13)+(.015 if true else -.015)
                mass=np.array((p,1-p))
                admitted=np.array((bp,.32-bp))/mass
                kept=np.array((pos,.18-pos))/(mass*admitted)
                self.assertTrue(np.all((admitted<=1)&(kept<=1)))
                laws.append(np.r_[mass*admitted*kept,(mass*admitted*(1-kept)).sum(),1-mass@admitted])
            np.testing.assert_allclose(*laws)

    def test_clamped_and_matched_archive(self):
        env=self.pay,self.pay
        base=policy(self.data,(0,"late"),"ordinary","none",env)[0]
        for kind,clamp in (("roster",True),("archive",False)):
            got=policy(self.data,(2,"late"),"ordinary",kind,env,clamp)[0]
            np.testing.assert_allclose(got[:,0],base[:,0]-2*FEE)
            np.testing.assert_allclose(got[:,1:],base[:,1:])

    def test_delayed_last_report_expires(self):
        env=self.pay,self.pay
        base=policy(self.data,(0,"late"),"late","none",env)[0]
        last=policy(self.data,(1,"late"),"late","roster",env)[0]
        np.testing.assert_allclose(last[:,0],base[:,0]-FEE)

    def test_fixed_schedule_matches_sequential_filter(self):
        trace=np.zeros((12,len(self.data[0])),bool)
        trace[[0,5,11]]=True
        replay=evaluate(self.data,None,6,self.pay,self.pay,FEE,trace)
        fixed=policy(self.data,(3,"spread"),"ordinary","roster",(self.pay,self.pay))
        np.testing.assert_allclose(replay[0],fixed[0][:,0])
        np.testing.assert_array_equal(replay[2],fixed[1])

    def test_bellman_dominates_fixed_and_respects_budget(self):
        plans,values=solve(self.pay,FEE,1.,6)
        frontier=fixed_frontier(self.pay)
        for s,index in ((0,1340),(1,660)):
            best=max(g[s]-len(d)*FEE for d,g in frontier)
            self.assertGreaterEqual(values[s,6,index]+1e-7,best)
        n=evaluate(self.data,plans,6,self.pay,self.pay,FEE)[1]
        self.assertTrue(np.all((n>=0)&(n<=6)))


if __name__=="__main__":
    unittest.main()
