"""Site selection and successive hardware vintages in The full-stack robotic firm.

Run with Python 3.10 or later. Exact checks use only the standard library.
To regenerate the paper's figure, add --figure PATH.svg (Matplotlib required).
"""
import argparse
from dataclasses import dataclass
from fractions import Fraction as F
from itertools import product
from math import exp, log
from pathlib import Path


STATES = ("control", "mechanical")
REPORTS = ("none", "control", "mechanical")
POLICIES = tuple(product((0, 1), repeat=len(REPORTS)))
HALF = F(1, 2)
QUARTER = F(1, 4)


def prior(state, p):
    return p if state == "mechanical" else 1 - p


def policy_build(policy, state, revealed):
    report = state if revealed else "none"
    return policy[REPORTS.index(report)]


def timed_value(cost, control_gain, mechanical_gain, p, timely):
    """Switching surplus over the standard design with conclusive or late evidence."""
    expected_gain = (1 - p) * control_gain + p * mechanical_gain
    ordinary = max(0, expected_gain - cost)
    informed = (1 - p) * max(0, control_gain - cost) + p * max(0, mechanical_gain - cost)
    return ordinary + timely * (informed - ordinary)


def diagnostic_value(cost, control_gain, mechanical_gain, p):
    """Value of perfectly revealing the bottleneck before the factory decision."""
    mean = (1 - p) * control_gain + p * mechanical_gain
    if cost <= control_gain or cost >= mechanical_gain:
        return F(0)
    if cost <= mean:
        return (1 - p) * (cost - control_gain)
    return p * (mechanical_gain - cost)


def policy_cells(p, q_control, q_mechanical, policy):
    """Enumerate actual states and reports, including informative nonarrival."""
    for state, q in zip(STATES, (q_control, q_mechanical)):
        for revealed, probability in ((False, 1 - q), (True, q)):
            yield state, policy_build(policy, state, revealed), prior(state, p) * probability


def raw_policy_value(cost, control_gain, mechanical_gain, p, q_control, q_mechanical):
    gain = dict(zip(STATES, (control_gain, mechanical_gain)))
    return max(
        sum(weight * built * (gain[state] - cost)
            for state, built, weight in policy_cells(p, q_control, q_mechanical, policy))
        for policy in POLICIES
    )


def check_site_rule():
    checked = 0
    for p, a_c, a_m, cost, q in product(
            (F(0), QUARTER, HALF, 1 - QUARTER, F(1)),
            (0, 2), (4, 6), range(-1, 9), (F(0), QUARTER, 1 - QUARTER, F(1))):
        formula = timed_value(cost, a_c, a_m, p, q)
        optimal = raw_policy_value(cost, a_c, a_m, p, q, q)
        assert optimal == formula
        base = timed_value(cost, a_c, a_m, p, 0)
        assert optimal - base == q * diagnostic_value(cost, a_c, a_m, p)
        if 0 < p < 1:
            delta_q, beta = HALF, F(3, 4)
            for margin in (F(0), F(1, 8), F(1, 2), F(1)):
                lower = a_c + margin / (beta * delta_q * (1 - p))
                upper = a_m - margin / (beta * delta_q * p)
                direct = beta * (raw_policy_value(cost, a_c, a_m, p, 1 - QUARTER, 1 - QUARTER)
                                 - raw_policy_value(cost, a_c, a_m, p, QUARTER, QUARTER))
                assert (direct > margin) == (lower < cost < upper)
        checked += 1
    # In this sensor, silence completely reveals the constraint too.
    informative_silence = raw_policy_value(4, 0, 6, HALF, 0, 1)
    assert informative_silence == 1
    assert timed_value(4, 0, 6, HALF, HALF) == HALF
    return checked


def faster_gap(k, routine, unusual, deadline):
    return exp(-k * routine * deadline) - exp(-k * unusual * deadline)


def check_reporting_speed():
    cases = 0
    for routine, multiple, deadline in product((0.3, 1, 1.8), (1.5, 3, 4), (0.4, 1, 2.5)):
        unusual = routine * multiple
        peak = log(unusual / routine) / ((unusual - routine) * deadline)
        values = [faster_gap(peak * i / 12, routine, unusual, deadline) for i in range(61)]
        assert max(range(len(values)), key=values.__getitem__) == 12
        assert all(a < b for a, b in zip(values[:12], values[1:13]))
        assert all(a > b for a, b in zip(values[12:], values[13:]))
        cases += 1
    return cases


def funded_surplus(cost, a_c, a_m, p, joint):
    """Choose a hardware policy after funding and the report are observed."""
    total = F(0)
    gains = dict(zip(STATES, (a_c, a_m)))
    for (funded, timely), mass in joint.items():
        if not funded:
            continue
        reports = STATES if timely else ("none",)
        for report in reports:
            state_mass = {s: mass * prior(s, p) for s in STATES if report in ("none", s)}
            total += max(0, sum(weight * (gains[s] - cost) for s, weight in state_mass.items()))
    return total


def check_funding():
    cases = 0
    for both, fund_only, report_only in product(range(5), repeat=3):
        if both + fund_only + report_only > 4:
            continue
        joint = {(True, True): F(both, 4), (True, False): F(fund_only, 4),
                 (False, True): F(report_only, 4), (False, False): 1 - F(both + fund_only + report_only, 4)}
        for cost in (1, 3, 5):
            ordinary = timed_value(cost, 0, 6, HALF, 0)
            predicted = F(both + fund_only, 4) * ordinary + F(both, 4) * diagnostic_value(cost, 0, 6, HALF)
            assert funded_surplus(cost, 0, 6, HALF, joint) == predicted
            cases += 1
    positive = {(True, True):HALF, (False, False):HALF}
    negative = {(True, False):HALF, (False, True):HALF}
    assert funded_surplus(4, 0, 6, HALF, positive) == HALF
    assert funded_surplus(4, 0, 6, HALF, negative) == 0
    return cases


def build_given(state, p, q, cost, a_c, a_m):
    mean = (1 - p) * a_c + p * a_m
    gain = a_m if state == "mechanical" else a_c
    return (1 - q) * int(mean > cost) + q * int(gain > cost)


def check_independent_batches():
    # Unit counts differ by block. Each batch has separate orders, crew and funding.
    blocks = [(0, 8, 5, 2), (0, 8, 2, 3), (1, 6, 0, 4), (1, 6, 7, 2)]
    cases = 0
    for p, q in product((F(1, 3), HALF, F(2, 3)), (QUARTER, HALF, F(1))):
        ordinary = realized = positive = negative = 0
        for a_c, a_m, cost, units in blocks:
            mean = (1 - p) * a_c + p * a_m
            ordinary += units * int(mean > cost)
            realized += units * sum(prior(s, p) * build_given(s, p, q, cost, a_c, a_m) for s in STATES)
            if a_c < cost < a_m:
                if mean > cost:
                    negative += units
                else:
                    positive += units
        assert realized - ordinary == q * (p * positive - (1 - p) * negative)
        cases += 1
    return cases


@dataclass(frozen=True)
class Site:
    name: str
    margin: F
    timely: F
    candidate: F = F(0)


@dataclass(frozen=True)
class Outcome:
    profit: F = F(0)
    first_special: F = F(0)
    second_special: F = F(0)
    old_orders: F = F(0)

    def plus(self, other):
        return Outcome(self.profit + other.profit, self.first_special + other.first_special,
                       self.second_special + other.second_special, self.old_orders + other.old_orders)

    def scaled(self, n):
        return Outcome(self.profit * n, self.first_special * n, self.second_special * n, self.old_orders * n)


FIRST_SITES = (Site("routine", F(2), QUARTER), Site("unusual", F(11, 8), 1 - QUARTER))


def second_sites(access, rights):
    routine = Site("routine", F(2), QUARTER, QUARTER)
    if not access:
        return (routine,)
    capture = 1 - QUARTER if rights else QUARTER
    return (routine, Site("unusual", HALF, 1 - QUARTER, capture))


def fill_orders(state, specialized, hard_orders):
    # Each new machine has one window. At commissioning, choose the best qualified buyer.
    choices = [0, 4]
    if specialized and state == "mechanical":
        choices.append(hard_orders)
    return max(choices)


def final_dispatch(state, specialized, candidate):
    base = fill_orders(state, specialized, 14) - 4 * specialized
    options = [Outcome(F(base), second_special=F(specialized))]
    if candidate:
        orders, unit_margin, training = 2, 2, 1
        options.append(Outcome(F(base + orders * unit_margin - training),
                               second_special=F(specialized), old_orders=F(orders)))
    return max(options, key=lambda o:o.profit)


def choose_from_reports(site, continuation):
    """Backward induction. Hardware is chosen using only the report. Ties retain standard."""
    total = Outcome(site.margin)
    for report in REPORTS:
        options = []
        for hardware in (0, 1):
            value = Outcome()
            for state in STATES:
                if report != "none" and report != state:
                    continue
                prob = (1 - site.timely) if report == "none" else site.timely
                value = value.plus(continuation(state, hardware).scaled(HALF * prob))
            options.append(value)
        total = total.plus(max(options, key=lambda o:o.profit))
    return total


def solve_three_vintages(rights):
    next_by_access, next_site = {}, {}
    for access in (False, True):
        options = []
        for site in second_sites(access, rights):
            def final(state, h):
                return final_dispatch(state, h, False).scaled(1 - site.candidate).plus(
                    final_dispatch(state, h, True).scaled(site.candidate))
            options.append((site.name, choose_from_reports(site, final)))
        next_site[access], next_by_access[access] = max(options, key=lambda item:item[1].profit)
    def first(state, h):
        service = fill_orders(state, h, 10) - 4 * h
        return Outcome(F(service), first_special=F(h)).plus(next_by_access[bool(h and state == "mechanical")])
    beginnings = {site.name:choose_from_reports(site, first) for site in FIRST_SITES}
    name, outcome = max(beginnings.items(), key=lambda item:item[1].profit)
    return name, outcome, beginnings, next_site, next_by_access


def enumerate_three_vintages(rights):
    """Evaluate whole contingent plans directly, independently of backward induction.

    The candidate affects only an old machine, so its profitable training decision
    separates from all factory decisions. Future routine qualification always occurs.
    """
    tables = {}
    for access in (False, True):
        plans = []
        for site, rule in product(second_sites(access, rights), POLICIES):
            earning = site.margin
            for state, built, mass in policy_cells(HALF, site.timely, site.timely, rule):
                # Compute every feasible pair of deployment and training actions.
                choices = [4, 14] if built and state == "mechanical" else [4]
                for got, freq in ((False, 1 - site.candidate), (True, site.candidate)):
                    gains = [use + trained * 3 - built * 4 for use in [0, *choices] for trained in range(1 + int(got))]
                    earning += mass * freq * max(gains)
            plans.append(earning)
        tables[access] = plans
    best = None
    count = 0
    for site, rule in product(FIRST_SITES, POLICIES):
        first = site.margin
        access = F(0)
        for state, built, mass in policy_cells(HALF, site.timely, site.timely, rule):
            unlocked = bool(built and state == "mechanical")
            first += mass * ((10 if unlocked else 4) - 4 * built)
            access += mass * unlocked
        for ordinary, unlocked in product(tables[False], tables[True]):
            value = first + (1 - access) * ordinary + access * unlocked
            best = value if best is None else max(best, value)
            count += 1
    return best, count


def check_vintages():
    rows = []
    for rights in (False, True):
        name, outcome, first, choices, after = solve_three_vintages(rights)
        optimal, count = enumerate_three_vintages(rights)
        assert outcome.profit == optimal
        assert name == ("unusual" if rights else "routine")
        assert choices == {False:"routine", True:"unusual" if rights else "routine"}
        assert after[True].profit - after[False].profit == int(rights)
        assert first["unusual"].profit - first["routine"].profit == (F(1, 8) if rights else - F(1, 8))
        expected = Outcome(F(59, 4), F(3, 8), F(25, 32), F(7, 8)) if rights else Outcome(F(29, 2), F(1, 8), F(7, 8), HALF)
        assert outcome == expected
        rows.append((rights, name, outcome, count))
    return rows


def check_factory_yield():
    # Enumerate the binary production outcomes, then compare with the marginal rule.
    checked = 0
    lot_values = {}
    for yield_rate, capacity in product((QUARTER, F(2, 5), HALF, F(4, 5), F(1)), (0, 1, 2, 5)):
        values, room = [], []
        for starts in range(9):
            expected_fill, probability_open = F(0), F(0)
            for conforms in product((0, 1), repeat=starts):
                good = sum(conforms)
                mass = yield_rate**good * (1 - yield_rate)**(starts - good)
                expected_fill += mass * min(good, capacity)
                probability_open += mass * int(good < capacity)
            values.append(10 * expected_fill - starts)
            room.append(probability_open)
        increments = [b - a for a, b in zip(values, values[1:])]
        assert increments == [10 * yield_rate * prob - 1 for prob in room[:-1]]
        assert all(a >= b for a, b in zip(increments, increments[1:]))
        lot_values[yield_rate, capacity] = (values.index(max(values)), max(values))
        checked += len(increments)
    assert lot_values[F(2, 5), 1][0] == 3 and lot_values[F(4, 5), 1][0] == 2
    assert 1 - F(3, 5)**3 == F(98, 125) and 1 - F(1, 5)**2 == F(24, 25)
    return checked


def best_quote(ceiling, cost):
    """Optimal effective quote for uniform willingness to pay, on the stated interior."""
    assert 0 <= cost <= ceiling
    price = (ceiling + cost) / 2
    return price, (ceiling - price) / ceiling


def check_market_entry():
    # Evaluate monetary quotes (including refusal and its ordinary continuation)
    # against the smooth optimum. All interior optima in this grid are grid points.
    cases = 0
    for ceiling in (F(3), F(4), F(6)):
        for base_cost, learning, burden in product((1, 2), (F(0), HALF, 1), (F(0), HALF, 1)):
            if not 0 <= base_cost - learning + burden <= ceiling:
                continue
            effective, acceptance = best_quote(ceiling, base_cost - learning + burden)
            monetary = effective - burden
            if monetary < 0:
                continue
            quotes = [F(i, 4) for i in range(int(4 * ceiling) + 1)]
            def gain(quote):
                purchase = max(F(0), 1 - (quote + burden) / ceiling)
                return purchase * (quote - base_cost + learning)
            assert max(map(gain, quotes)) == gain(monetary)
            assert gain(monetary) == (ceiling - (base_cost - learning + burden))**2 / (4 * ceiling)
            assert gain(monetary) == acceptance * (monetary - base_cost + learning)
            cases += 1

    # Joint all-vintage solution with posted future offers. The seller chooses the
    # contract, price and second factory policy; buyers can decline to ordinary work.
    for burden in (F(0), HALF, F(2, 3), F(3, 4), F(1), F(3, 2), F(2)):
        routine = second_sites(False, False)[0]
        def second_value(site):
            def recourse(state, hardware):
                return final_dispatch(state, hardware, False).scaled(1 - site.candidate).plus(
                    final_dispatch(state, hardware, True).scaled(site.candidate))
            return choose_from_reports(site, recourse).profit
        fallback = second_value(routine)
        best = fallback
        for rights in (False, True):
            fee = burden if rights else F(0)
            effective, _ = best_quote(F(4), F(2) - int(rights) * F(3, 2) + fee)
            quotes = {F(i, 8) for i in range(33)} | {effective - fee}
            for price in quotes:
                if price < 0:
                    continue
                bought = max(F(0), 1 - (price + fee) / 4)
                unusual = Site("unusual", price - 1, 1 - QUARTER, 1 - QUARTER if rights else QUARTER)
                best = max(best, bought * second_value(unusual) + (1 - bought) * fallback)
        access = best - fallback
        prediction = max(QUARTER, (F(7, 2) - burden)**2 / 16)
        assert access == prediction
        names = []
        for site in FIRST_SITES:
            def first(state, hardware):
                opens = hardware and state == "mechanical"
                profit = fill_orders(state, hardware, 10) - 4 * hardware + (best if opens else fallback)
                return Outcome(profit)
            names.append(choose_from_reports(site, first).profit)
        assert (names[1] > names[0]) == (access > HALF)
        if burden == 0:
            assert access == F(49, 64)
        cases += 1
    return cases


def plot_figure(path):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from matplotlib.ticker import MaxNLocator
    plt.rcParams.update({"font.family":"DejaVu Sans", "font.size":9, "svg.fonttype":"none",
                         "svg.hashsalt":"full-stack-firm", "pdf.fonttype":42})
    fig, axes = plt.subplots(1, 2, figsize=(8.0, 3.05))
    teal, rust = "#12615c", "#90411f"
    costs = [6 * i / 300 for i in range(301)]
    speeds = [4.5 * i / 300 for i in range(301)]
    panels = ((costs, [0.5 * diagnostic_value(z, 0, 6, .5) for z in costs], "Cost of changing the batch", "Installed obligations"),
              (speeds, [1.5 * faster_gap(k, 1, 4, 1) for k in speeds], "Common increase in reporting speed", "Learning speed"))
    for ax, (xx, yy, xlabel, title) in zip(axes, panels):
        ax.plot(xx, yy, color=teal, linewidth=2.4, label="Value of the earlier diagnosis")
        ax.axhline(.4, color=rust, linestyle="--", linewidth=1.4, label="Current margin forgone")
        ax.fill_between(xx, .4, yy, where=[y > .4 for y in yy], interpolate=True, color="#b0dacf", alpha=.75)
        ax.set(xlabel=xlabel, ylim=(0, .84), xlim=(0, xx[-1]))
        ax.set_title(title, loc="left", weight="bold", fontsize=11)
        ax.yaxis.set_major_locator(MaxNLocator(5))
        ax.grid(axis="y", color="#d6e0dc", linewidth=.6)
        ax.spines[["top", "right"]].set_visible(False)
        ax.spines[["left", "bottom"]].set_color("#9bada8")
    axes[0].set_ylabel("Contribution per opportunity")
    handles, labels = axes[0].get_legend_handles_labels()
    fig.legend(handles, labels, loc="lower center", ncol=2, frameon=False)
    fig.subplots_adjust(left=.092, right=.99, bottom=.3, top=.88, wspace=.27)
    metadata={"Date":None} if path.suffix == ".svg" else {}
    fig.savefig(path, metadata=metadata)
    plt.close(fig)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--figure", type=Path, help="Optional paper figure, e.g. figure.svg")
    args = parser.parse_args()
    print(f"Single-batch policies and site cutoffs: {check_site_rule()} settings.")
    print(f"Reporting-speed comparisons: {check_reporting_speed()} rate and deadline settings.")
    print(f"Joint liquidity/report laws: {check_funding()} comparisons.")
    print(f"Posted prices, customer participation and reuse in the vintage model: {check_market_entry()} settings.")
    print(f"Factory starts versus realized conformance: {check_factory_yield()} marginal schedules.")
    print(f"Optional batch totals: {check_independent_batches()} comparisons.")
    for rights, site, outcome, plans in check_vintages():
        print(f"Future trace reuse {rights}, first site {site}: {outcome}; {plans} contingent plans.")
    if args.figure:
        plot_figure(args.figure)
