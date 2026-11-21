"""Exact policy replay, decentralized agreements, posterior sampling and sensitivity checks."""
from collections import Counter
from dataclasses import replace
from itertools import product
import json
import math
import random

from economy import Decision, Economy, State, Tape, hour_price, run, solve, value, with_rights


class Contract:
    """A jointly signed table of feasible actions, compiled before deployment."""
    def __init__(self, policy):
        self.fallback = policy.fallback
        self.dispatches = {k: d.action for k, d in policy.dispatch_cache.items()}
        self.training = {k: d.action for k, d in policy.training_cache.items()}
        self.assets = {k: d.action for k, d in policy.hardware_cache.items()}

    def dispatch(self, t, state, hours, compute):
        return Decision(0, self.dispatches[t, state, hours, compute])

    def posttrain(self, t, state, hours, compute):
        return Decision(0, self.training[t, state, hours, compute])

    def hardware_decision(self, state):
        return Decision(0, self.assets[state])


def event_rates(e):
    return (e.hard_probability, e.sim_pass, e.arm_transfer, e.mobile_transfer, e.amendment)


def ledger(policy, e, hours):
    metrics = Counter()
    actions = Counter()
    for bits in product((False, True), repeat=5):
        chance = math.prod(p if b else 1-p for b, p in zip(bits, event_rates(e)))
        if chance == 0:
            continue
        record = run(policy, e, hours, Tape(*bits))
        for key in ("net", "digital", "plant", "depot", "desk_hours", "floor_hours"):
            metrics[key] += chance * record[key]
        actions[record["samples"][0]] += chance
    return {k: round(v, 8) for k, v in metrics.items()}, dict(actions)


def pair(e):
    outputs = [ledger(solve(e, h), e, h)[0] for h in (0, 1)]
    return {"no_hour": outputs[0], "one_hour": outputs[1],
            "difference": {k: round(outputs[1][k]-outputs[0][k], 8) for k in outputs[0]},
            "first_dispatch": solve(e, 1).dispatch(0, State(), 1, e.compute).action}


def arrangements(base):
    configurations = {
        "deployment_only_sealed_fixed_assets": replace(with_rights(base, "sealed"), compute=0, hardware=("installed",)),
        "hardware_operator_no_corpus": replace(with_rights(base, "settlement"), compute=0),
        "model_supplier_fixed_customer_assets": replace(base, hardware=("installed",)),
        "local_updates_no_cross_site_training": with_rights(base, "local"),
        "full_stack_sealed": with_rights(base, "sealed"),
        "full_stack_settlement_only": with_rights(base, "settlement"),
        "full_stack_mixed_rights_arm_sealed_mobile_portable": replace(base, arm_rights="sealed"),
        "full_stack_mixed_rights_arm_portable_mobile_sealed": replace(base, mobile_rights="sealed"),
        "portable_locked_capital": replace(base, amendment=0),
        "portable_per_case_agreement": replace(base, amendment=0.4),
        "portable_standing_authority": base,
        "portable_no_posttraining_compute": replace(base, compute=0),
    }
    return {name: pair(env) for name, env in configurations.items()}


def negotiate(gain, provider_share, cost, increment=0.25):
    """A field operator quotes transfers within its private gain; the partner may refuse."""
    provider_uplift = provider_share * gain
    field_uplift = (1-provider_share) * gain
    offers = []
    for i in range(math.floor((field_uplift+1e-10)/increment)+1):
        transfer = i * increment
        offers.append(transfer)
        if provider_uplift + transfer >= cost:
            return {"adopt": True, "offers": offers, "net_provider": provider_uplift+transfer-cost,
                    "net_field": field_uplift-transfer, "total_gain": gain-cost}
    return {"adopt": False, "offers": offers, "net_provider": 0, "net_field": 0, "total_gain": 0}


def procure_licenses(gains, bids, captured_share):
    """Procure any subset of offered site rights with a Clarke pivot payment to each seller."""
    def best_package(available):
        feasible = [sources for sources in gains if set(sources) <= available]
        def private_surplus(sources):
            return captured_share * gains[sources] - sum(bids[s] for s in sources)
        # The offer table lists the empty and smaller packages first for equal surpluses.
        selected = max(feasible, key=lambda sources: round(private_surplus(sources), 10))
        return selected, private_surplus(selected)

    available = set(bids)
    selected, surplus = best_package(available)
    payments = {}
    for site in selected:
        _, outside = best_package(available - {site})
        payments[site] = round(bids[site] + surplus - outside, 8)
    gross = gains[selected]
    return {"licenses": list(selected), "payments": payments,
            "sponsor_net": round(captured_share * gross - sum(payments.values()), 8),
            "uncaptured_operating_gain": round((1 - captured_share) * gross, 8),
            "seller_gains_at_truthful_bids": {s: round(payments[s] - bids[s], 8) for s in selected},
            "joint_gain_at_truthful_bids": round(gross - sum(bids[s] for s in selected), 8)}


def license_market(e):
    # Evaluate separately from the operating margins already collected at the two sites.
    packages = ((), ("arm",), ("mobile",), ("arm", "mobile"))
    scenarios = {}
    for hours in (0, 1):
        sealed = value(with_rights(e, "sealed"), hours)
        gains = {}
        for sites in packages:
            rights = replace(e, arm_rights="portable" if "arm" in sites else "sealed",
                             mobile_rights="portable" if "mobile" in sites else "sealed")
            gains[sites] = round(value(rights, hours) - sealed, 8)
        bids = {"arm": 6, "mobile": 2}
        scenarios[str(hours)] = {
            "operating_gain_above_sealed": {"+".join(p) or "sealed": gains[p] for p in packages},
            "full_claim_arm_offer_only": procure_licenses(gains, {"arm": 6}, 1),
            "full_claim_both_offers": procure_licenses(gains, bids, 1),
            "half_claim_both_offers": procure_licenses(gains, bids, .5)}
    return {"license_sellers_reservation_costs": {"arm": 6, "mobile": 2}, "by_hours": scenarios}


def governance(e):
    fast, slow = e, replace(e, amendment=0.4)
    coordinated = solve(fast, 1)
    table = Contract(coordinated)
    standing, _ = ledger(coordinated, fast, 1)
    bilateral, _ = ledger(table, fast, 1)
    base = value(slow, 1)
    surplus = standing["net"] - base
    # Public order books available to the manager and to both contracting parties.
    desk = replace(e, desk_orders=10, plant_orders=0, depot_orders=1)
    mixed = replace(e, desk_orders=1, plant_orders=5, depot_orders=6)
    average = replace(e, desk_orders=5.5, plant_orders=2.5, depot_orders=3.5)
    modes = {}
    succession = {}
    for h in (0, 1):
        tables = [Contract(solve(env, h)) for env in (desk, mixed)]
        fixed = Contract(solve(average, h))
        flexible = sum(value(env, h)/2 for env in (desk, mixed))
        prewritten = sum(ledger(book, env, h)[0]["net"]/2 for book, env in zip(tables, (desk, mixed)))
        pooled = sum(ledger(fixed, env, h)[0]["net"]/2 for env in (desk, mixed))
        modes[str(h)] = {"best_uniform_mandate": pooled, "joint_amendment": flexible,
                         "bilateral_book_on_observed_orders": prewritten, "value_of_conditioning": flexible-pooled}
        # A named representative is replaced with probability 1/2. Both parties
        # re-sign in time with probability 0.4. A transferable book survives.
        personal = 0.0
        enduring = 0.0
        for j, env in enumerate((desk, mixed)):
            for replaced, rp in ((False,.5),(True,.5)):
                for timely, tp in ((False,.6),(True,.4)):
                    chance = .5*rp*tp
                    authorized = not replaced or timely
                    plan = tables[j] if authorized else fixed
                    personal += chance*ledger(plan, env, h)[0]["net"]
                    enduring += chance*ledger(tables[j], env, h)[0]["net"]
        renewal_gain = enduring-personal
        agreement = negotiate(renewal_gain, 0.25, 0.5)
        succession[str(h)] = {"personal_reconsent": personal, "transferable_book": enduring,
                              "joint_office_gross": flexible, "gross_value_of_survival": renewal_gain,
                              "private_offer_for_joint_office": agreement,
                              "joint_office_after_cost_or_fallback": personal + agreement["total_gain"]}
    return {"one_hour": {"per_case_40pct_on_time": base, "integrated_timely": standing["net"],
                         "independent_prewritten_complete_book": bilateral["net"],
                         "collectively_authorized_dispatch": standing["net"], "gross_timeliness_gain": surplus},
            "setup_cost_one": negotiate(surplus, 0.25, 1),
            "setup_cost_three": negotiate(surplus, 0.25, 3),
            "public_demand_experiment_by_hours": modes, "turnover_by_hours": succession}


def tape_for(e, rng):
    return Tape(*(rng.random() < p for p in event_rates(e)))


def scenario_grid(e):
    signs = {name: Counter() for name in ("add_retrofit_to_installed", "add_fixture_to_installed",
                                         "add_fixture_to_retrofit", "allow_code_without_trajectory")}
    prices = []
    cases = 0
    for desk, arm, depot, hard, wages, transfers, fixture in product(
            (1, 7), (0, 3), (2, 7), (0.25, 0.75), ((2, 7), (5, 12)), ((0.8, 0.2), (0.2, 0.8)), (6, 14)):
        env = replace(e, desk_orders=desk, plant_orders=arm, depot_orders=depot, hard_probability=hard,
                      desk_wage=wages[0], floor_wage=wages[1], arm_transfer=transfers[0],
                      mobile_transfer=transfers[1], fixture_cost=fixture)
        menus = [("installed",), ("installed", "retrofit"), ("installed","fixture"), e.hardware]
        variants = [replace(env, hardware=menu) for menu in menus]
        variants += [with_rights(env, "sealed"), with_rights(env, "settlement"), with_rights(env, "local")]
        rows = [(value(v, 0), value(v, 1)) for v in variants]
        for h in (0, 1):
            assert rows[3][h] + 1e-8 >= max(rows[1][h], rows[2][h])
            assert min(rows[1][h], rows[2][h]) + 1e-8 >= rows[0][h]
            assert rows[3][h]+1e-8 >= rows[6][h] >= rows[5][h]-1e-8
            assert rows[5][h]+1e-8 >= rows[4][h]
        lifts = [b-a for a,b in rows]
        assert min(lifts) >= env.urgent_receipt-1e-8
        for name, (after,before) in zip(signs, ((1,0),(2,0),(3,1),(5,4))):
            delta = lifts[after] - lifts[before]
            signs[name]["positive" if delta > 1e-8 else "negative" if delta < -1e-8 else "zero"] += 1
        prices.append(lifts[3])
        cases += 1
    return {"cases": cases, "sign_of_change_in_hour_price": signs,
            "full_portable_hour_price_range": [min(prices), max(prices)]}


def posterior_sampling(e):
    """Learn from licensed, separately validated updates in recurring deployment batches."""
    arms = (replace(e, arm_transfer=0.8, mobile_transfer=0.2),
            replace(e, arm_transfer=0.2, mobile_transfer=0.8))
    policies = [Contract(solve(env, 1)) for env in arms]
    output = {}
    train_n, test_n, seeds = 24, 1000, tuple(range(12))
    for truth, train_env in enumerate(arms):
        observations, final_sources = Counter(), Counter()
        block_counts = [Counter(), Counter()]
        profit = Counter()
        probabilities = []
        for seed in seeds:
            rng = random.Random(1100 + seed)
            market = random.Random(2500 + seed)
            odds = 0.0
            for k in range(train_n):
                belief = 1 / (1 + math.exp(-odds))
                policy_id = 0 if rng.random() < belief else 1
                record = run(policies[policy_id], train_env, 1, tape_for(train_env, market))
                block_counts[int(k >= train_n//2)][record["samples"][0]] += 1
                for donor, passed in record["evidence"]:
                    observations[donor] += 1
                    likelihood = [env.arm_transfer if donor == "arm" else env.mobile_transfer for env in arms]
                    if not passed:
                        likelihood = [1-p for p in likelihood]
                    odds += math.log(likelihood[0]/likelihood[1])
            belief = 1 / (1 + math.exp(-odds))
            probabilities.append(belief if truth==0 else 1-belief)
            # Compile an expected-economics policy from the posterior for a fresh deployment.
            # In this two-shift, one-hour study at most one portable source can be updated.
            learned_env = replace(e, arm_transfer=0.2+0.6*belief, mobile_transfer=0.8-0.6*belief)
            learned = Contract(solve(learned_env, 1))
            first = learned.dispatch(0, State(), 1, e.compute).action
            final_sources[first] += 1
            candidates = {"posterior": learned, "known_law": policies[truth],
                          "cash_only": Contract(solve(train_env, 1, "cash")),
                          "arm_first": Contract(solve(train_env, 1, "arm_first"))}
            heldout = random.Random(6000 + seed)
            for _ in range(test_n):
                tape = tape_for(train_env, heldout)
                for name, candidate in candidates.items():
                    profit[name] += run(candidate, train_env, 1, tape)["net"]
        output["arm_high" if truth==0 else "mobile_high"] = {
            "mean_posterior_on_true_law": round(sum(probabilities)/len(seeds), 6),
            "validation_events_by_source": observations, "training_first_dispatch_by_half": block_counts,
            "first_dispatch_12_frozen_policies": final_sources,
            "heldout_net_per_batch": {k: round(v/(len(seeds)*test_n), 5) for k,v in profit.items()}}
    return {"train_batches_per_seed": train_n, "fresh_batches_per_seed": test_n, "seeds": seeds,
            "worlds": output}


def results():
    e = Economy()
    assets = {"+".join(menu): pair(replace(e, hardware=menu)) for menu in
              (("installed",), ("installed", "retrofit"), ("installed", "fixture"), e.hardware)}
    witness = replace(e, desk_orders=0, plant_orders=1, depot_orders=2, hardware=("installed","retrofit"))
    policy = solve(witness, 2)
    paired = {name: run(policy, witness, 2, Tape(True,True,passed,False,True))
              for name,passed in (("arm_candidate_passes",True),("arm_candidate_fails",False))}
    return {"units": "normalized contribution per batch, teleoperation wage excluded",
            "architectures": arrangements(e), "hardware_comparisons": assets, "governance": governance(e),
            "license_market": license_market(e), "paired_sampling_witness": paired,
            "sensitivity": scenario_grid(e), "learning": posterior_sampling(e)}


if __name__ == "__main__":
    print(json.dumps(results(), indent=2))
