from .check_fitness import check_fitness
from .fitness_rank_assigner import fitness_rank_assigner

def population_sorter(population, secret_code):

    sorted_population = {'A': [], 'B': [], 'C': [], 'D': [], 'E': []}
    for individual in list(population.keys()):
        fitness_score = check_fitness(population.get(individual), secret_code)
        sorted_population = fitness_rank_assigner(individual, fitness_score, sorted_population)
    return sorted_population
