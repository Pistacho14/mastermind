import random
from .contants import WEIGHTS, EXPLOTATION_PERCENTAGE


def roulette_selection(population_sorted):
    population_sorted = population_sorted.copy()
    individual_reproducible = []
    individuals_weights = []
    reproducible_population = {}
    counter = 1

    for ranking, individuals in population_sorted.items():
        for individual in individuals:
            individual_reproducible.append(individual)
            individuals_weights.append(WEIGHTS[ranking])

    while len(reproducible_population) < EXPLOTATION_PERCENTAGE:
        selected_individual = random.choices(
            individual_reproducible, weights=individuals_weights
        )[0]

        reproducible_population[counter] = selected_individual.copy()
        counter += 1

    return list(reproducible_population.values())
