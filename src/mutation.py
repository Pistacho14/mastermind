import random
from .contants import MUTATION_CHANCE, COLORS

def mutation(individual, MUTATION_CHANCE, COLORS):
    individual = individual.copy()
    for i in range(4):
        if random.random() < MUTATION_CHANCE:
            nuevo = random.choice(COLORS)
            while nuevo == individual[i]:
                nuevo = random.choice(COLORS)
            individual[i] = nuevo
    return individual
