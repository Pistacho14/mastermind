import random
from .reproduction import reproduction

def offspring_generator(reproducible_population):

    population = reproducible_population.copy()
    offspring = {}
    counter = 1
    while len(population) > 1:
        parents = random.sample(population, 2)
        father, mother = parents
        offspring = reproduction(father,mother, offspring, counter)
        population.remove(father)
        population.remove(mother)
        counter += 2
    return  offspring
