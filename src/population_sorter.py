from .check_fitness import check_fitness
from .fitness_rank_assigner import fitness_rank_assigner


def population_sorter(current_population, secret_code):
    ranked_population = {
        "A": [],
        "B": [],
        "C": [],
        "D": [],
        "E": [],
        "F": [],
        "G": [],
        "H": [],
    }
    for genes in list(current_population.values()):
        fitness_score = check_fitness(genes, secret_code)
        ranked_population = fitness_rank_assigner(
            genes, fitness_score, ranked_population
        )
    return ranked_population
