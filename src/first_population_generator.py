from .peg_pattern_generator import genes_generator
from .contants import POPULATION_SIZE


def initial_population_generator():
    initial_population = {}
    for individual in range(1, POPULATION_SIZE + 1):
        initial_population[individual] = genes_generator()
    return initial_population
