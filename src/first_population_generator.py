from .peg_pattern_generator import peg_pattern_generator

def first_population_generator(population):

    first_population = {}
    for individuo in range(1, population + 1):
        first_population[individuo] = peg_pattern_generator()
    return first_population
