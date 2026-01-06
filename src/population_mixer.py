import random
from .population_sorter import population_sorter

def population_mixer(current_population, secret_code, offspring):

    next_gen_patterns = list(offspring.values())
    next_gen = {}

    WEIGHTS = {'B': 100, 'C': 45, 'D': 30, 'E': 10, 'F': 5, 'G': 3, 'H': 1}
    actual_population_candidates = []
    actual_population_weights = []

    for ranking, individuals in population_sorter(current_population, secret_code).items():
        for individual_id in individuals:
            actual_population_candidates.append(individual_id)
            actual_population_weights.append(WEIGHTS[ranking])

    while len(next_gen_patterns) < len(current_population):
        selected_population = random.choices(actual_population_candidates, weights=actual_population_weights)
        next_gen_patterns.append(selected_population)

    for individual, peg_pattern in enumerate(next_gen_patterns, start=1):
        next_gen[individual] = peg_pattern

    return next_gen
