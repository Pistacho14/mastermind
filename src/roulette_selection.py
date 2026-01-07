import random
from .contants import WEIGHTS, MAX_OFFSPRING


def roulette_selection(ranked_population):
    individuals = []
    weights = []

    for rank, population in ranked_population.items():
        for genes in population:
            individuals.append(genes)
            weights.append(WEIGHTS[rank])

    selected_individuals = []

    while len(selected_individuals) < MAX_OFFSPRING:
        selected_individual = random.choices(individuals, weights=weights)[0]
        selected_individuals.append(selected_individual.copy())

    return selected_individuals
