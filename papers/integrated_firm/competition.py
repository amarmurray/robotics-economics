#!/usr/bin/env python3
"""Two-period public-state Cournot restriction of the integrated firm's technology.

The inherited production/finance/research menus are core.py menus, not reduced
payoff coefficients. End-market prices respond to both firms' accepted service.
Only the terminal continuation game is compressed: retained evidence, beliefs
and uncommercialized procedures have no terminal value in this stated economy.
"""
from dataclasses import asdict, replace
from functools import lru_cache
from itertools import product
import json
from core import Config, State, Firm

def describe(a):
    return {'physical':a.production.physical,'digital':a.production.digital,
            'research':a.research.name,'method':a.research.method,'build':a.build,
            'next_lab':a.next_lab,'outlay':a.outlay,'human':a.human,'tokens':a.tokens,
            'retain_physical':a.retain_physical,'retain_digital':a.retain_digital}

class Competition:
    def __init__(self,c=Config(),selection='low_indices'):
        self.c=c
        self.selection=selection
        self.f=Firm(c)
        self.terminal_count=0
        self.max_terminal_nash_residual=0.
        self.max_potential_residual=0.

    @lru_cache(None)
    def options(self,s):
        by_quantity={}
        for act in self.f.actions(s,1):
            q=(act.production.physical,act.production.digital)
            if q not in by_quantity or act.outlay<by_quantity[q].outlay:
                by_quantity[q]=act
        return tuple(by_quantity[q] for q in sorted(by_quantity))

    def profit(self,s,own,rival):
        return sum(q*(self.c.demand_intercepts[s.market][j]-2*(q+r))
                   for j,(q,r) in enumerate(zip(own,rival)))

    @lru_cache(None)
    def terminal(self,s0,s1):
        self.terminal_count+=1
        actions=[self.options(s0),self.options(s1)]
        qs=[[(a.production.physical,a.production.digital) for a in row] for row in actions]
        matrices=[[],[]]
        potentials=[]
        for i,a in enumerate(actions[0]):
            row0=[];row1=[];pot=[]
            for j,b in enumerate(actions[1]):
                row0.append(self.profit(s0,qs[0][i],qs[1][j])-a.outlay)
                row1.append(self.profit(s1,qs[1][j],qs[0][i])-b.outlay)
                Q=[qs[0][i][m]+qs[1][j][m] for m in (0,1)]
                pot.append(sum(self.c.demand_intercepts[s0.market][m]*Q[m]-Q[m]**2
                               -qs[0][i][m]**2-qs[1][j][m]**2 for m in (0,1))-a.outlay-b.outlay)
            matrices[0].append(row0);matrices[1].append(row1);potentials.append(pot)
        n0,n1=len(actions[0]),len(actions[1])
        br0=[max(matrices[0][i][j] for i in range(n0)) for j in range(n1)]
        br1=[max(matrices[1][i]) for i in range(n0)]
        eq=[(i,j) for i,j in product(range(n0),range(n1))
            if matrices[0][i][j]>=br0[j]-1e-10 and matrices[1][i][j]>=br1[i]-1e-10]
        assert eq  # Exact-potential argument supplies existence for this terminal game.
        # Verify all unilateral potential changes against private profit changes.
        for i,j in product(range(n0),range(n1)):
            self.max_potential_residual=max(self.max_potential_residual,
                abs((potentials[i][j]-potentials[0][j])-(matrices[0][i][j]-matrices[0][0][j])),
                abs((potentials[i][j]-potentials[i][0])-(matrices[1][i][j]-matrices[1][i][0])))
        # Public continuation convention. It selects a Nash equilibrium, never
        # a collusive non-equilibrium quantity; ties are disclosed and recorded.
        tie_sign=-1 if self.selection=='low_indices' else 1
        i,j=max(eq,key=lambda ij:(matrices[0][ij[0]][ij[1]]+matrices[1][ij[0]][ij[1]],
                    min(matrices[0][ij[0]][ij[1]],matrices[1][ij[0]][ij[1]]),tie_sign*ij[0],tie_sign*ij[1]))
        self.max_terminal_nash_residual=max(self.max_terminal_nash_residual,
            br0[j]-matrices[0][i][j],br1[i]-matrices[1][i][j])
        wealth=(self.f.terminal(s0)+matrices[0][i][j],self.f.terminal(s1)+matrices[1][i][j])
        return wealth,qs[0][i],qs[1][j],len(eq)

    def root_actions(self,s):
        raw=list(self.f.actions(s,2))
        kept={}
        for a in raw:
            effect=a.research.effect
            if effect not in ('physical','digital'):effect='none'
            law=(a.research.success_one,a.research.success_zero) if effect!='none' else None
            key=(a.production.physical,a.production.digital,a.outlay,a.build,a.next_lab,effect,law)
            kept.setdefault(key,a)
        return tuple(kept.values()),len(raw)

    def last_states(self,s,a,rival_q,h,market):
        q=(a.production.physical,a.production.digital)
        cash=s.cash-a.outlay+self.profit(s,q,rival_q)
        base=State(arm=s.arm+int(a.build=='arm'),mobile=s.mobile+int(a.build=='mobile'),
                   reference=s.reference+int(a.build=='reference'),physical_model=s.physical_model,
                   digital_model=s.digital_model,cash=cash,internal_lab=a.next_lab,market=market,
                   physical_data=0,digital_data=0,procedure=0,odds_one=1,odds_zero=1)
        assert cash>=0
        effect=a.research.effect
        if effect not in ('physical','digital'):
            return ((1.,base),)
        p=a.research.success_one if h else a.research.success_zero
        return tuple((pr,replace(base,**{effect+'_model':getattr(base,effect+'_model')+int(v)}))
                     for v,pr in ((False,1-p),(True,p)) if pr>0)

    def solve(self,s0=State(),s1=State()):
        assert (s0.market,s0.odds_one,s0.odds_zero)==(s1.market,s1.odds_one,s1.odds_zero)
        acts0,raw0=self.root_actions(s0);acts1,raw1=self.root_actions(s1)
        p=s0.odds_one/(s0.odds_one+s0.odds_zero)
        A=[];B=[]
        for a in acts0:
            row0=[];row1=[]
            for b in acts1:
                v0=v1=0.
                qa=(a.production.physical,a.production.digital)
                qb=(b.production.physical,b.production.digital)
                # Conditional independence given H, not marginal independence.
                for h,ph in ((1,p),(0,1-p)):
                    if ph==0:continue
                    for m,pm in ((s0.market,self.c.market_persistence),(1-s0.market,1-self.c.market_persistence)):
                        for (wa,sa),(wb,sb) in product(self.last_states(s0,a,qb,h,m),self.last_states(s1,b,qa,h,m)):
                            values,_,_,_=self.terminal(sa,sb)
                            weight=ph*pm*wa*wb
                            v0+=weight*values[0];v1+=weight*values[1]
                row0.append(v0);row1.append(v1)
            A.append(row0);B.append(row1)
        br0=[max(A[i][j] for i in range(len(acts0))) for j in range(len(acts1))]
        br1=[max(row) for row in B]
        equilibria=[]
        for i,j in product(range(len(acts0)),range(len(acts1))):
            residual=max(br0[j]-A[i][j],br1[i]-B[i][j])
            if residual<1e-9:
                equilibria.append({'actions':[describe(acts0[i]),describe(acts1[j])],
                                  'wealth':[A[i][j],B[i][j]],
                                  'net_wealth_including_salvage':[A[i][j]-s0.cash,B[i][j]-s1.cash],
                                  'unilateral_deviation_gain':residual})
        return {'horizon':2,'config':asdict(self.c),'initial':[asdict(s0),asdict(s1)],
                'raw_root_action_counts':[raw0,raw1],'root_actions_after_exact_continuation_equivalence':[len(acts0),len(acts1)],
                'terminal_games_solved':self.terminal_count,
                'maximum_terminal_potential_identity_residual':self.max_potential_residual,
                'maximum_terminal_selected_nash_residual':self.max_terminal_nash_residual,
                'root_pure_equilibria':equilibria,
                'root_pure_equilibrium_count':len(equilibria),
                'minimum_pure_profile_max_deviation_gain':min(max(br0[j]-A[i][j],br1[i]-B[i][j]) for i,j in product(range(len(acts0)),range(len(acts1)))),
                'continuation_selection':'Among terminal pure Nash equilibria, maximize sum of operating profits; then minimum operating profit; then '+self.selection+'.'}

def run():
    result={}
    for selection in ('low_indices','high_indices'):
        for name,states in [('symmetric',(State(),State())),
                            ('inherited_digital_lead',(State(digital_model=1),State()))]:
            game=Competition(selection=selection)
            key=name+'_'+selection
            result[key]=game.solve(*states)
            assert result[key]['root_pure_equilibrium_count']>0
    # A stated technology for already admitted automated research workflows.
    # This is a model restriction, not an empirical estimate of human-free R&D.
    c=Config(research_human=0,training_tokens=1,procedure_tokens=1)
    s=State(cash=18,digital_data=1)
    for selection in ('low_indices','high_indices'):
        reviewed=Competition(Config(),selection=selection)
        reviewed_key='prefunded_reviewed_research_'+selection
        result[reviewed_key]=reviewed.solve(s,s)
        assert result[reviewed_key]['root_pure_equilibrium_count']>0
        game=Competition(c,selection=selection)
        key='automated_research_'+selection
        result[key]=game.solve(s,s)
        assert result[key]['root_pure_equilibrium_count']>0
    return result

if __name__=='__main__':
    result=run()
    with open('competition_results.json','w') as out:json.dump(result,out,indent=2);out.write('\n')
    print(json.dumps(result,indent=2))

