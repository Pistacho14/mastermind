from .check_fitness import check_fitness
from .fitness_rank_assigner import fitness_rank_assigner

def population_sorter(population, secret_code):

    sorted_population = {'A': [], 'B': [], 'C': [], 'D': [], 'E': []}
    for individual in list(population.keys()):
        fitness = check_fitness(population.get(individual), secret_code)
        fitness_rank_assigner(individual, fitness, sorted_population)
    return sorted_population
