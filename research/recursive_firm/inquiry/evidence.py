"""Price static selection in published test tables. All calculations use exact fractions."""
import csv
import json
from collections import defaultdict
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from statistics import mean


HERE = Path(__file__).resolve().parent
ROBOT_MODELS = ("RT-1-X", "Octo", "RT-2-X", "OpenVLA")
PRIOR_DIGITAL_PAIR = ("gpt-4-turbo", "claude-3-opus")


@dataclass
class Case:
    label: str
    family: str
    score: dict


def read_rows(name):
    with (HERE / name).open(newline="") as source:
        return list(csv.DictReader(source))


def robot_cases():
    groups = defaultdict(list)
    for r in read_rows("robot_scores.csv"):
        score = {m: 100 * Fraction(r[m]) / int(r["trials"]) for m in ROBOT_MODELS}
        groups[r["embodiment"]].append(Case(r["task"], r["category"], score))
    return groups


def digital_cases():
    raw = read_rows("agent_scores.csv")
    return [Case(domain, domain, {r["model"]:Fraction(r[domain]) for r in raw})
            for domain in ("retail", "airline")]


def best_models(cases, menu):
    totals = {m:sum(c.score[m] for c in cases) for m in menu}
    highest = max(totals.values())
    return [m for m in menu if totals[m] == highest]


def score(cases, models):
    # Uniform tie-breaking among the options selected using training information.
    return mean(mean(c.score[m] for m in models) for c in cases)


def pooled_and_conditioned(cases, menu):
    fixed = best_models(cases, menu)
    by_family = defaultdict(list)
    for c in cases:
        by_family[c.family].append(c)
    family_score = sum(len(group) * score(group, best_models(group, menu))
                       for group in by_family.values()) / len(cases)
    fixed_score = score(cases, fixed)
    hindsight = mean(max(c.score[m] for m in menu) for c in cases)
    return dict(fixed_models=fixed, fixed=fixed_score, family=family_score,
                task_hindsight=hindsight, static_family_gain=family_score-fixed_score,
                remaining_within_family=hindsight-family_score)


def heldout(cases, menu):
    pooled, local = [], []
    for i, target in enumerate(cases):
        rest = cases[:i] + cases[i+1:]
        relatives = [c for c in rest if c.family == target.family]
        pooled.append(score([target], best_models(rest, menu)))
        local.append(score([target], best_models(relatives or rest, menu)))
    return dict(pooled=mean(pooled), family=mean(local), family_gain=mean(local)-mean(pooled))


def run():
    robots = robot_cases()
    digital = digital_cases()
    robot_report = {}
    for name, cases in robots.items():
        other = [c for n, group in robots.items() if n != name for c in group]
        selected_elsewhere = best_models(other, ROBOT_MODELS)
        robot_report[name] = dict(tasks=len(cases), in_sample=pooled_and_conditioned(cases, ROBOT_MODELS),
            leave_one_task_out=heldout(cases, ROBOT_MODELS), other_embodiment_choice=selected_elsewhere,
            other_embodiment_score=score(cases, selected_elsewhere))
    return dict(units="percentage points of the published score; equal weight per task within embodiment or per digital domain",
                robots=robot_report, digital={
                    "previous_pair":pooled_and_conditioned(digital, PRIOR_DIGITAL_PAIR),
                    "all_reported":pooled_and_conditioned(digital, list(digital[0].score))})


if __name__ == "__main__":
    (HERE / "results.json").write_text(json.dumps(run(), indent=2, default=float) + "\n")
