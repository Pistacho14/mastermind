import random
from .contants import MUTATION_CHANCE, ALLELS


def mutation(child):
    for i in range(4):
        if random.random() < MUTATION_CHANCE:
            mutated_allel = random.choice(ALLELS)
            while mutated_allel == child[i]:
                mutated_allel = random.choice(ALLELS)
            child[i] = mutated_allel
    return child
