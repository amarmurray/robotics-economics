"""Two-release network production and investment model. All technology inputs are synthetic."""
from dataclasses import dataclass
from functools import lru_cache

import numpy as np
from scipy.optimize import linprog

NODES = ("digital_dispatch", "packaging_plant", "fulfillment", "hospital_supply")
ROLES = ("handling", "technical_review", "clerical")
N = len(NODES)
EYE = np.eye(N)
ZERO = (0,) * N
OPTIONS = [ZERO] + [tuple(row.astype(int)) for row in EYE]
BETA = .92
# Hours per manually completed stage unit and per machine attempt.
MANUAL = np.array([[0., .15, .9], [.85, .18, .12], [1., .08, .12], [.68, .55, .24]])
SUPPORT = np.array([[0., .08, .05], [.10, .14, .03], [.08, .12, .06], [.12, .31, .08]])
WAGES = np.array([1.3, 2.5, 1.7])
RUN_COST = np.array([.17, .38, .35, .30])
COMPUTE = np.array([.55, .22, .30, .24])
BASE_K = np.array([5., 4., 3., 2.4])
BLOCK = np.array([2.4, 2.1, 2.4, 1.9])
FIRST_COST = np.array([6., 7., 6.5, 6.])
LAST_COST = np.array([3.6, 4.2, 3.9, 3.6])
Q = np.array([.82, .69, .75, .65])
DECAY = np.array([.04, .05, .05, .03])
# Row is the evidence source, column the affected release. A negative entry is interference.
GAIN = np.array([[.13,.10,.11,.07], [.02,.21,.12,-.06],
                 [.05,.08,.18,.12], [.02,-.04,.09,.24]])
LOG_DENSITY = np.array([5.8, 2.6, 3.5, 2.1])
RETENTION = np.array([.82, .85, .66, .55])
CLUSTER_SIZE = np.array([3.4, 1.7, 2.4, 1.1])
AUDIT_PRICE = np.array([.31,.35,.34,.39])
INTERNAL_PRICE = np.array([1.1, 2.4, 0., 0.])


@dataclass
class World:
    demand: np.ndarray
    labor: np.ndarray
    fixture: np.ndarray
    local_manual: np.ndarray
    compute: float
    price: np.ndarray
    next_demand: np.ndarray
    next_labor: np.ndarray


def draw(seed):
    rng = np.random.default_rng(seed)
    def variation(base, lo, hi):
        return np.array(base) * rng.uniform(lo, hi, len(base))
    demand = variation([3.1, 2.3, 5., 4.0], .68, 1.38)
    labor = variation([9., 4.6, 7.], .72, 1.3)
    return World(demand, labor, variation([13.,11.,7.,5.2], .74, 1.3),
                 variation([5.,5.7,4.8,3.8], .72, 1.35), rng.uniform(4.3,6.1),
                 variation([4.4,6.4,11.2,13.3], .90,1.10),
                 demand * rng.uniform(.80,1.35,N), labor * rng.uniform(.85,1.15,3))


def requirements(regime, period, topology="direct"):
    b = np.zeros((N,N))
    b[0,1:] = [.35,.55,.8]
    b[1,2:] = [.70,1.05]
    if regime == "standardization" and period == 1:
        # New packaging standard reduces upstream material per completed hospital lot.
        b[1,3] -= .50
    if topology == "cross_dock":
        # Move part of hospital preparation through the fulfillment operator. Keep
        # total embodied plant and dispatch requirements per hospital job identical.
        b[2,3] = .45
        b[0:2,3] -= b[0:2,2] * b[2,3]
    return b


@dataclass
class Operation:
    profit: float
    final: np.ndarray
    gross: np.ndarray
    attempts: np.ndarray
    human: np.ndarray
    machine_output: np.ndarray
    labor: np.ndarray
    ledger: np.ndarray
    machine_shadow: np.ndarray


@dataclass
class Policy:
    value: float
    source: int
    chance: float
    release: str
    last_no_signal: int
    last_signal: int
    account: np.ndarray
    first: Operation
    expected_final_next: np.ndarray
    expected_auto_next: np.ndarray


class Economy:
    def __init__(self, w, regime="baseline", topology="direct"):
        self.world, self.regime = w, regime
        self.operating = lru_cache(None)(self._operating)
        self.last = lru_cache(None)(self._last)
        self.network = [requirements(regime, t, topology) for t in (0,1)]
        self.require = [np.linalg.inv(EYE-b) for b in self.network]

    def clear(self):
        self.operating.cache_clear()
        self.last.cache_clear()

    def skill(self, period, source, scope):
        if period == 0:
            return Q
        q = Q - DECAY
        if self.regime == "controller_drift":
            q = q - [.03,.17,.02,.12]
        if source < 0:
            return q
        gain = GAIN[source] if scope == "pooled" else GAIN[source]*EYE[source]
        if self.regime == "controller_drift":
            gain = gain * np.where(EYE[source],1.,-.7)
        return np.clip(q + gain, .10, .98)

    def _operating(self, period, blocks, source=-1, scope="pooled", objective="contribution"):
        w = self.world
        demand = (w.demand if period == 0 else w.next_demand).copy()
        if self.regime == "hospital_surge" and period:
            demand[3] *= 1.8
        labor = (w.labor if period == 0 else w.next_labor).copy()
        if self.regime == "labor_remix" and period:
            # Exchange technical hours for handling hours at constant endowment wage value.
            lost_review = .30 * labor[1]
            labor[1] -= lost_review
            labor[0] += lost_review * WAGES[1] / WAGES[0]
        compute = w.compute * (.60 if self.regime == "compute_squeeze" and period else 1.)
        q = self.skill(period, source, scope)
        k = BASE_K + BLOCK * np.array(blocks)
        # Variables: final jobs sold, manual stage output, machine attempts.
        req = self.require[period]
        balances = np.hstack((req,-EYE,-np.diag(q)))
        labor_rows = np.hstack((np.zeros((3,N)),MANUAL.T,SUPPORT.T))
        compute_row = np.r_[np.zeros(2*N),COMPUTE]
        fixture_rows = np.hstack((req,np.zeros((N,2*N))))
        cost = np.r_[-w.price, MANUAL@WAGES, SUPPORT@WAGES + RUN_COST]
        if objective == "physical_frontier":
            cost[N:] = 0.
        res = linprog(cost,
                      A_eq=balances,b_eq=np.zeros(N),
                      A_ub=np.vstack((labor_rows,compute_row,fixture_rows)),
                      b_ub=np.r_[labor,compute,w.fixture],
                      bounds=[(0.,limit) for limit in np.r_[demand,w.local_manual,k]],
                      method="highs")
        if not res.success:
            raise RuntimeError(res.message)
        y,h,a = np.split(res.x,3)
        gross = req@y
        hours = h[:,None]*MANUAL + a[:,None]*SUPPORT
        flows = self.network[period] * gross[None,:]
        payments = INTERNAL_PRICE[:,None] * flows
        account = w.price*y - hours@WAGES - RUN_COST*a + payments.sum(axis=1)-payments.sum(axis=0)
        return Operation(float(account.sum()), y,gross,a,h,q*a,hours.sum(axis=0),account,
                         -res.upper.marginals[-N:].copy())

    def chance(self, base):
        # Independent informative clusters arrive as a thinned Poisson process.
        clusters = CLUSTER_SIZE * (4. if self.regime == "duplicate_logs" else 1.)
        retain = RETENTION.copy()
        if self.regime == "selective_retention":
            retain[[1,3]] *= .12
        return -np.expm1(-base.attempts*(1-Q)*LOG_DENSITY*retain/clusters)

    def _last(self, installed, source, scope):
        choices=[]
        for j,extra in enumerate(OPTIONS):
            blocks = tuple(np.add(installed, extra))
            op = self.operating(1,blocks,source,scope)
            extra_cost = LAST_COST * extra
            choices.append((op.profit-extra_cost.sum(),j-1,op,op.ledger-extra_cost))
        return max(choices,key=lambda x:x[0])

    def policy(self, installed, scope="open", source_option="optimize"):
        current = self.operating(0,installed)
        value, j, no, cash_no = self.last(installed,-1,"pooled")
        best = Policy(current.profit+BETA*value,-1,0.,"none",j,j,
                      current.ledger+BETA*cash_no,current,no.final,no.machine_output)
        if source_option == "none" or self.regime == "late_release":
            return best
        chances = self.chance(current)
        for s,prob in enumerate(chances):
            if source_option not in ("optimize",s):
                continue
            releases = ("local","pooled") if scope == "open" else (scope,)
            for release in releases:
                paid, j2, yes, cash_yes = self.last(installed,s,release)
                gain = BETA*prob*(paid-value)-AUDIT_PRICE[s]
                candidate = current.profit+BETA*value+gain
                if candidate <= best.value:
                    continue
                account = current.ledger + BETA*((1-prob)*cash_no+prob*cash_yes)-EYE[s]*AUDIT_PRICE[s]
                best = Policy(candidate,s,float(prob),release,j,j2,account,current,
                              (1-prob)*no.final+prob*yes.final,
                              (1-prob)*no.machine_output+prob*yes.machine_output)
        return best
