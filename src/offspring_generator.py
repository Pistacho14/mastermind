import random
from .reproduction import reproduction


def offspring_generator(selected_population):
    selected_population = selected_population.copy()
    offspring = {}
    child_id = 1
    while len(selected_population) > 1:
        parents = random.sample(selected_population, 2)
        father, mother = parents
        offspring = reproduction(father, mother, offspring, child_id)
        selected_population.remove(father)
        selected_population.remove(mother)
        child_id += 2
    return offspring
