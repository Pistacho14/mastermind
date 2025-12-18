import random

def population_mixer(current_population, secret_code, offspring, population_sorted):

    next_gen_patterns = list(offspring.values())
    next_gen = {}

    WEIGHTS = {'B': 40,'C': 25,'D': 6,'E': 3}
    actual_population_candidates = []
    actual_population_weights = []

    for ranking, individuals in population_sorted.items():
        for individual_id in individuals:
            actual_population_candidates.append(current_population[individual_id])
            actual_population_weights.append(WEIGHTS[ranking])

    while len(next_gen_patterns) != len(current_population):
        selected_population = random.choices(actual_population_candidates,weights=actual_population_weights)
        next_gen_patterns.extend(selected_population)

    for individual, peg_pattern in enumerate(next_gen_patterns, start=1):
        next_gen[individual] = peg_pattern

    return next_gen
