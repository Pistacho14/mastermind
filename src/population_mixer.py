import random
from .population_sorter import population_sorter
from .contants import WEIGHTS


def population_mixer(current_population, secret_code, offspring):
    next_gen_patterns = [p.copy() for p in offspring.values()]
    next_gen = {}

    actual_population_candidates = []
    actual_population_weights = []

    for ranking, individuals in population_sorter(
        current_population, secret_code
    ).items():
        for individual in individuals:
            actual_population_candidates.append(individual)
            actual_population_weights.append(WEIGHTS[ranking])

    while len(next_gen_patterns) < len(current_population):
        selected = random.choices(
            actual_population_candidates, weights=actual_population_weights
        )[0]

        next_gen_patterns.append(selected.copy())

    for individual_id, peg_pattern in enumerate(next_gen_patterns, start=1):
        next_gen[individual_id] = peg_pattern

    return next_gen
