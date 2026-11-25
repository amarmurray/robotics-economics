"""Checks for Learning and Capital in Robotic Production. Run with Python 3 and NumPy."""

from dataclasses import dataclass
from fractions import Fraction
from itertools import product

import numpy as np


def radius(matrix):
    return float(max(abs(np.linalg.eigvals(matrix))))


def survival(loss):
    return np.eye(len(loss)) - np.diag(loss)


@dataclass
class Economy:
    capital_loss: np.ndarray
    method_loss: np.ndarray
    fund_loss: np.ndarray
    order_response: np.ndarray
    learning: np.ndarray
    earned_cash: np.ndarray
    method_cash: np.ndarray
    starts_from_methods: np.ndarray
    starts_from_funds: np.ndarray

    def first_generation_channels(self):
        capital_life = np.diag(1 / self.capital_loss)
        method_life = np.diag(1 / self.method_loss)
        funding_life = np.diag(1 / self.fund_loss)
        method_stock = method_life @ self.learning @ capital_life
        qualification = self.starts_from_methods @ method_stock
        cash = self.starts_from_funds @ funding_life @ self.earned_cash @ capital_life
        cash_on_installed_fleet = self.starts_from_funds @ funding_life @ self.method_cash @ method_stock
        return self.order_response @ capital_life, qualification, cash, cash_on_installed_fleet

    def state_transition(self):
        methods, funds = len(self.method_loss), len(self.fund_loss)
        return np.block([
            [survival(self.capital_loss) + self.order_response, self.starts_from_methods, self.starts_from_funds],
            [self.learning, survival(self.method_loss), np.zeros((methods, funds))],
            [self.earned_cash, self.method_cash, survival(self.fund_loss)],
        ])

    def dated_impulse(self, periods, allow_descendants):
        """Propagate one seed of each type in parallel. Each column is a separate experiment."""
        types = len(self.capital_loss)
        k = np.eye(types)
        h = np.zeros((len(self.method_loss), types))
        w = np.zeros((len(self.fund_loss), types))
        starts = [k.copy()]
        for _ in range(periods):
            new_starts = self.order_response @ k + self.starts_from_methods @ h + self.starts_from_funds @ w
            next_k = survival(self.capital_loss) @ k
            if allow_descendants:
                next_k += new_starts
            next_h = survival(self.method_loss) @ h + self.learning @ k
            next_w = survival(self.fund_loss) @ w + self.earned_cash @ k + self.method_cash @ h
            k, h, w = next_k, next_h, next_w
            starts.append(new_starts)
        return np.asarray(starts)

    def discounted_first_generation(self, beta):
        k, h, w = len(self.capital_loss), len(self.method_loss), len(self.fund_loss)
        auxiliary = np.block([
            [survival(self.method_loss), np.zeros((h, w))],
            [self.method_cash, survival(self.fund_loss)],
        ])
        entry = np.hstack((self.starts_from_methods, self.starts_from_funds))
        incoming = np.vstack((self.learning, self.earned_cash))
        capital_exposures = np.linalg.solve(np.eye(k) - beta * survival(self.capital_loss), np.eye(k))
        responses = np.linalg.solve(np.eye(h+w) - beta * auxiliary, incoming @ capital_exposures)
        return beta * self.order_response @ capital_exposures + beta**2 * entry @ responses


def example():
    # At the reference of a binding revolving-finance constraint I=W/exp(-h),
    # W=1 and h=0 give unit derivatives with respect to both W and h.
    return Economy(
        capital_loss=np.ones(2), method_loss=np.ones(2), fund_loss=np.ones(2),
        order_response=np.zeros((2, 2)), learning=np.array([[0.4, 0.6], [0.1, 0.4]]),
        earned_cash=np.full((2, 2), 0.2), method_cash=np.zeros((2, 2)),
        starts_from_methods=np.eye(2), starts_from_funds=np.eye(2),
    )


def check_states_and_generations():
    rng = np.random.default_rng(173)
    cases = 0
    for types, methods, funds in ((1, 2, 1), (2, 3, 1), (3, 2, 2)):
        for scale in (0.03, 0.18, 0.45):
            for _ in range(7):
                economy = Economy(
                    rng.uniform(0.4, 0.95, types), rng.uniform(0.4, 0.95, methods),
                    rng.uniform(0.4, 0.95, funds), rng.uniform(0, scale/3, (types, types)),
                    rng.uniform(0, scale, (methods, types)),
                    rng.uniform(0, scale, (funds, types)), rng.uniform(0, scale, (funds, methods)),
                    rng.uniform(0, 0.7, (types, methods)), rng.uniform(0, 0.7, (types, funds)),
                )
                generation = sum(economy.first_generation_channels())
                direct = economy.dated_impulse(180, allow_descendants=False)
                np.testing.assert_allclose(direct[1:].sum(axis=0), generation, rtol=1e-11, atol=1e-13)
                np.testing.assert_allclose(economy.discounted_first_generation(1), generation)
                growth = radius(economy.state_transition())
                assert (radius(generation) > 1) == (growth > 1)
                np.testing.assert_allclose(radius(economy.discounted_first_generation(1/growth)), 1, atol=1e-10)
                beta = 0.45
                weighted = np.power(beta, np.arange(len(direct)))
                first = economy.discounted_first_generation(beta)
                np.testing.assert_allclose(np.einsum('t,tij->ij', weighted[1:], direct[1:]), first)
                assert radius(first) < 1
                with_descendants = economy.dated_impulse(180, allow_descendants=True)
                reported = np.einsum('t,tij->ij', weighted, with_descendants)
                expected = np.linalg.solve(np.eye(types) - first, np.eye(types))
                np.testing.assert_allclose(reported, expected, rtol=1e-10, atol=1e-12)
                cases += 1
    return cases


def gate_checks():
    def admissions(h, cash, applicants, bays):
        profitable = applicants * np.clip((4 + 2*h) / 10, 0, 1)
        fundable = cash / (2 - h/2)
        installable = bays + h/5
        return min(profitable, fundable, installable)

    step = 1e-5
    # Profitable prospects, revolving funds, then commissioning bays bind.
    for args, expected in [((40, 10, 25), (2, 0)), ((4, 30, 20), (0.5, 0.5)),
                           ((30, 30, 1), (0.2, 0))]:
        cash, sites, bays = args
        dh = (admissions(step, cash, sites, bays) - admissions(-step, cash, sites, bays)) / (2*step)
        dw = (admissions(0, cash+step, sites, bays) - admissions(0, cash-step, sites, bays)) / (2*step)
        np.testing.assert_allclose([dh, dw], expected, atol=1e-8)

    # A dated balance integral differs from counting the date of first payment.
    stages = [(5, 2), (2, 3)]
    occupied = sum(balance * duration for balance, duration in stages)
    assert occupied == 16 and Fraction(48, occupied) == 3

    for benefit, linear_cost, curvature in product((0, 2, 8), (0, 1, 4), (1, 3, 10)):
        chosen = float(np.clip((benefit-linear_cost)/curvature, 0, 1))
        candidates = np.linspace(0, 1, 501)
        def surplus(z):
            return (benefit-linear_cost)*z - curvature*z*z/2
        assert surplus(chosen) + 1e-12 >= np.max(surplus(candidates))


def threshold_checks():
    cases = 0
    values = (Fraction(0), Fraction(1, 4), Fraction(3, 5), Fraction(9, 10))
    links = (Fraction(0), Fraction(1, 5), Fraction(1, 2), Fraction(1), Fraction(3, 2))
    for a, d, b, c in product(values, values, links, links):
        limit = (1-a)*(1-d)
        rho = radius(np.array([[a,b],[c,d]],dtype=float))
        exact = b*c - limit
        if exact == 0:
            assert abs(rho-1) < 1e-12
        else:
            assert (rho > 1) == (exact > 0)
        cases += 1
    return cases


def bounded_economy(generation, seed, eligible, periods):
    n = np.asarray(seed, dtype=float)
    for _ in range(periods):
        n = -eligible * np.expm1(-(generation @ n) / eligible)
    return n


def check_compounding_and_timing():
    e = example()
    orders, qualification, cash, interaction = e.first_generation_channels()
    generation = orders + qualification + cash + interaction
    assert max(radius(qualification), radius(cash)) < 1 < radius(generation)
    assert max(generation.diagonal()) < 1
    np.testing.assert_allclose(e.dated_impulse(2, False)[2], generation)
    np.testing.assert_allclose(radius(e.state_transition()), np.sqrt(radius(generation)))
    print(f"Illustrative learning-only root {radius(qualification):.4f}, cash-only root "
          f"{radius(cash):.4f}, combined root {radius(generation):.4f}.")

    # Arrival changes timing; missing a time-sensitive opportunity changes mass.
    gross = Fraction(5, 4)
    beta = Fraction(9, 10)
    survival_per_period = Fraction(17, 20)
    one_period = (0, gross, 0, 0)
    three_periods = (0, 0, 0, gross)
    assert sum(one_period) == sum(three_periods)
    discount = lambda stream: sum(beta**t * amount for t, amount in enumerate(stream))
    assert discount(one_period) > discount(three_periods)
    countdown = np.array([[0, 0, float(gross)], [1, 0, 0], [0, 1, 0]])
    assert float(gross) > radius(countdown) > 1
    np.testing.assert_allclose(radius(countdown)**3, float(gross))
    assert gross*survival_per_period > 1 > gross*survival_per_period**3

    eligible = np.array([10.0, 14.0])
    slim = np.array([0.001, 0.002])
    high = eligible * 0.9
    positive = bounded_economy(generation, slim, eligible, 1500)
    np.testing.assert_allclose(positive, bounded_economy(generation, high, eligible, 1500))
    assert np.all((positive > 0) & (positive < eligible))
    assert max(bounded_economy(generation*0.8, high, eligible, 1500)) < 1e-10
    critical = generation / radius(generation)
    assert max(bounded_economy(critical, high, eligible, 15000)) < 0.004
    print("Two-type bounded cohort, sustained additional starts per generation:",
          np.round(positive, 4).tolist())

    # Independent finite perturbation of one edge in a stable discounted economy.
    kernel = e.discounted_first_generation(0.8)
    seed = np.array([1.0, 0.0])
    values = np.array([3.0, 1.5])
    identity = np.eye(2)
    z = np.linalg.solve(identity-kernel, identity)
    for j,i in product(range(2), repeat=2):
        perturb = np.zeros((2,2))
        perturb[j,i] = 1e-5
        def value(matrix):
            return values @ np.linalg.solve(identity-matrix, seed)
        difference = (value(kernel+perturb) - value(kernel-perturb)) / 2e-5
        analytic = (values @ z)[j] * (z @ seed)[i]
        np.testing.assert_allclose(difference, analytic, rtol=1e-8)


def capital_adjustment_checks():
    # Solve each site's investment first-order condition by bisection, then compare
    # realized slopes with the fixed-fleet and mobile-capital predictions.
    price, rent = 1.7, 1.3
    step = 1e-5
    for alpha in (0.2, 0.35, 0.55, 0.7):
        def outcomes(log_method):
            a = np.exp(log_method)
            def mpk(k):
                return alpha*a*k**(alpha-1)
            low, high = 1e-8, 1.
            while price*mpk(high) > rent:
                high *= 2
            for _ in range(80):
                mid = (low+high)/2
                if price*mpk(mid) > rent:
                    low = mid
                else:
                    high = mid
            fleet = (low+high)/2
            return np.log([fleet, mpk(fleet), mpk(0.05)])
        slopes = (outcomes(step)-outcomes(-step))/(2*step)
        np.testing.assert_allclose(slopes, [1/(1-alpha), 0, 1], atol=1e-8)

    # A second calculation perturbs all states through time, then asks for a
    # target machine's physical MPK where extra machines have diminishing product.
    e = example()
    transition = e.state_transition()
    baseline = np.ones(transition.shape[0])
    seed = np.zeros_like(baseline)
    seed[0] = 1
    def target_mpk(x):
        return 0.5*x[3]/np.sqrt(x[1])
    grad = np.array([0, -0.25, 0, 0.5, 0, 0])
    def evolve(x, periods):
        for _ in range(periods):
            x = baseline + transition @ (x-baseline)
        return x
    for lag in range(9):
        up = target_mpk(evolve(baseline+step*seed, lag))
        down = target_mpk(evolve(baseline-step*seed, lag))
        predicted = grad @ np.linalg.matrix_power(transition, lag) @ seed
        np.testing.assert_allclose((up-down)/(2*step), predicted, atol=1e-8)


def upstream_checks():
    # Finite log differences of independent market-clearing calculations.
    step = 1e-5
    for elasticity in (0.5, 1.7, 4.0):
        def deliveries(log_b):
            b = 2*np.exp(log_b)
            y = (3+b)**(-elasticity)
            return np.log([y, b*y])
        slopes = (deliveries(step) - deliveries(-step)) / (2*step)
        share = 2/5
        np.testing.assert_allclose(slopes, [-elasticity*share, 1-elasticity*share], atol=1e-9)
    attempts, failure, usable = np.array([100,120]), np.array([0.20,0.10]), 0.5
    assert np.diff(attempts*(1-failure)).item() > 0
    assert np.diff(attempts*failure*usable).item() < 0


if __name__ == "__main__":
    gate_checks()
    states = check_states_and_generations()
    thresholds = threshold_checks()
    check_compounding_and_timing()
    capital_adjustment_checks()
    upstream_checks()
    print(f"Verified {states} state systems and {thresholds} two-type thresholds, plus "
          "admissions, collection, lags, saturation, redesign, capital adjustment and upstream responses.")
