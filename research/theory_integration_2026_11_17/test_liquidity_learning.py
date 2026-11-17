import unittest
from dataclasses import replace
from fractions import Fraction as F
from liquidity_learning import Parameters, a_invoice, solve, no_learning, scenarios, choices, financed_shared_lag2_paths

class ExactCashBellmanTests(unittest.TestCase):
    def test_concave_accepted_service_invoice(self):
        self.assertEqual([a_invoice(7,q) for q in range(3)],[0,7,12])
        self.assertGreater(a_invoice(7,1)-a_invoice(7,0),a_invoice(7,2)-a_invoice(7,1))

    def test_invoice_maturity_not_billing(self):
        for lag in (1,2):
            p=Parameters(m=7,lag=lag)
            _,_,_,_,policy=solve(p)
            pending=(0,)*(lag-1)+(a_invoice(p.m,2),)
            self.assertEqual(policy[(1,2,pending,False)], "shared_A1" if lag==1 else "produce_A2_B0")

    def test_exact_three_demand_states_one_period_collection(self):
        for m,prem in ((4,F(0)),(7,F(4)),(11,F(26,5))):
            p=Parameters(m=m,lag=1)
            v,_,_,_,_=solve(p)
            self.assertEqual(v-no_learning(p),prem)

    def test_exact_lag_two_zero_learning_premium(self):
        for m in (4,7,11):
            p=Parameters(m=m,lag=2)
            v,_,_,_,_=solve(p)
            self.assertEqual(v,no_learning(p))

    def test_independent_baseline_accounting(self):
        for lag in (1,2):
            for m in (4,7,11):
                p=Parameters(lag=lag,m=m)
                self.assertEqual(no_learning(p),F(4+4*((2*m-2)-2)))

    def test_route_premiums_at_t1_if_funded(self):
        # Independent hand-calculated comparison of t1 one-trial strategies.
        for m in (4,7,11):
            shared=2*F(3,4)*14-13-(m-3)
            specialist=2*F(9,10)*14-20
            self.assertEqual(shared,F(11-m))
            self.assertEqual(specialist,F(26,5))

    def test_route_feasibility_before_spending(self):
        for m in (4,7,11):
            cash=2*m
            p=Parameters(m=m,lag=1)
            acts=[x[0] for x in choices(p,cash,False)]
            self.assertEqual('shared_A1' in acts,m>=7)
            self.assertEqual('specialist_A2' in acts,m>=11)

    def test_no_accepted_service_no_B(self):
        p=Parameters()
        acts=list(choices(p,100,False))
        self.assertTrue(all('B1' not in a[0] for a in acts))
        self.assertTrue(all(a[0] not in ('shared_A2',) for a in acts))

    def test_specialist_preserves_A_output(self):
        p=Parameters(m=11)
        acts={name:(cost,invoice) for name,cost,invoice,_ in choices(p,100,False)}
        self.assertEqual(acts['specialist_A2'],(22,20))
        self.assertEqual(acts['shared_A1'],(14,11))

    def test_cash_relaxes_but_net_payoff_does_not_necessarily_increase_with_m(self):
        p_low=Parameters(m=4,lag=1,starting_cash=10)
        p_high=Parameters(m=7,lag=1,starting_cash=10)
        self.assertGreater(solve(p_low)[0]-no_learning(p_low),solve(p_high)[0]-no_learning(p_high))

    def test_lag_not_welfare_cost_when_fully_financed_and_receivables_valuable(self):
        p1=Parameters(m=7,lag=1,starting_cash=20)
        p2=replace(p1,lag=2)
        self.assertEqual(solve(p1)[0],solve(p2)[0])

    def test_lag_two_effect_can_disappear_with_more_initial_cash(self):
        p=Parameters(m=7,lag=2,starting_cash=20)
        self.assertGreater(solve(p)[0],no_learning(p))

    def test_finance_blocks_entry_without_changing_gross_opportunity(self):
        p=Parameters(m=7,lag=1)
        q=replace(p,lag=2)
        self.assertEqual((p.p_shared,p.shared_cost,p.b_invoice,p.b_variable_cost),
                         (q.p_shared,q.shared_cost,q.b_invoice,q.b_variable_cost))
        self.assertEqual(solve(p)[0]-no_learning(p),4)
        self.assertEqual(solve(q)[0]-no_learning(q),0)

    def test_analytic_late_training_domination(self):
        for m in (4,7,11):
            self.assertLess(F(3,4)*14-13-(m-3),0)
            self.assertLess(F(9,10)*14-20,0)

    def test_independent_exhaustive_tree(self):
        # Separate enumeration of calendar cash dynamics; no call to the tested solver's action generator.
        def independent(p):
            def go(t,cash,pipe,qualified):
                if t==p.horizon: return F(cash+sum(pipe))
                available=cash+pipe[0]
                vals=[]
                for q in (1,2):
                    for b in (0,1) if qualified else (0,):
                        c=q+2*b
                        if available>=c:
                            inv=p.m*q-q*(q-1)+16*b
                            vals.append(go(t+1,available-c,pipe[1:]+(inv,),qualified))
                    if not qualified:
                        for name,k,prob in (("s",p.shared_cost,p.p_shared),("sp",p.specialist_cost,p.p_specialist)):
                            if name=="s" and q!=1:continue
                            c=q+k
                            if available>=c:
                                inv=p.m*q-q*(q-1)
                                next_pipe=pipe[1:]+(inv,)
                                y=go(t+1,available-c,next_pipe,True)
                                n=go(t+1,available-c,next_pipe,False)
                                vals.append(prob*y+(1-prob)*n)
                return max(vals)
            return go(0,p.starting_cash,(0,)*p.lag,False)
        for lag in (1,2):
            for m in (4,7,11):
                p=Parameters(m=m,lag=lag)
                self.assertEqual(solve(p)[0],independent(p))

    def test_enforceable_loan_has_principal_cancellation(self):
        for fee in (0,1,3,4):
            path=financed_shared_lag2_paths(fee)
            expected=F(3,4)*path['success']['terminal_equity']+F(1,4)*path['failure']['terminal_equity']
            self.assertEqual(expected-44,4-fee)

    def test_loan_repayment_is_not_contingent_on_qualification_success(self):
        path=financed_shared_lag2_paths(1)
        self.assertEqual(path['failure']['t4_repayment_cash_before'],27)
        self.assertEqual(path['success']['t4_repayment_cash_before'],39)
        self.assertEqual(path['failure']['repayment'],13)
        self.assertTrue(all(x['t4_repayment_cash_before']>=x['repayment'] for x in path.values()))

    def test_all_synthetic_states_pass_exact_type(self):
        for lag in (1,2):
            for m in (4,7,11):
                v,_,states,_,_=solve(Parameters(m=m,lag=lag))
                self.assertIsInstance(v,F)
                self.assertGreater(states,0)

if __name__=='__main__': unittest.main()
