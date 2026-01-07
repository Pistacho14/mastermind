from .mutation import mutation
from .contants import MUTATION_CHANCE, COLORS


def reproduction(father, mother, offspring, counter):
    first_child = father[0:2] + mother[2:]
    second_child = mother[0:2] + father[2:]

    first_child = mutation(first_child, MUTATION_CHANCE, COLORS)
    second_child = mutation(second_child, MUTATION_CHANCE, COLORS)

    offspring[counter] = first_child
    offspring[counter + 1] = second_child

    return offspring
