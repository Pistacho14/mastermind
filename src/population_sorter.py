from .check_fitness import check_fitness
from .fitness_rank_assigner import fitness_rank_assigner

def population_sorter(population, secret_code):

    sorted_population = {'A': [], 'B': [], 'C': [], 'D': [], 'E': []}
    for individual in list(population.keys()):
        fitness = check_fitness(population.get(individual), secret_code)
        fitness_rank_assigner(individual, fitness, sorted_population)
    return sorted_population

print(population_sorter({
    1: ['Red', 'Green', 'Yellow', 'Cyan'],
    2: ['Purple', 'Orange', 'Red', 'Green'],
    3: ['Yellow', 'Yellow', 'Cyan', 'Purple'],
    4: ['Green', 'Red', 'Orange', 'Orange'],
    5: ['Cyan', 'Purple', 'Green', 'Red'],
    6: ['Orange', 'Yellow', 'Red', 'Purple'],
    7: ['Green', 'Green', 'Cyan', 'Yellow'],
    8: ['Purple', 'Red', 'Orange', 'Cyan'],
    9: ['Yellow', 'Green', 'Purple', 'Red'],
    10: ['Orange', 'Cyan', 'Yellow', 'Green']
}, ['Green', 'Yellow', 'Red', 'Cyan']))
