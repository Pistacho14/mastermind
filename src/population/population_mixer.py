import random
from .population_sorter import population_sorter
from src.utils.constants import WEIGHTS


def population_mixer(current_population, secret_code, offspring):
    new_generation = {}
    current_population_candidates = []
    current_population_weights = []

    for rank, individuals in population_sorter(current_population, secret_code).items():
        for individual in individuals:
            current_population_candidates.append(individual)
            current_population_weights.append(WEIGHTS[rank])

    new_generation_genes = list(offspring.values())

    while len(new_generation_genes) < len(current_population):
        selected_genes = random.choices(
            current_population_candidates, weights=current_population_weights
        )[0]

        new_generation_genes.append(selected_genes)

    for individual_id, genes in enumerate(new_generation_genes, start=1):
        new_generation[individual_id] = genes

    return new_generation
