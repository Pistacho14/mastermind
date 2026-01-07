from .contants import KEY_PEG_RED, KEY_PEG_WHITE


def check_fitness(genes, secret_code):
    fitness_score = 0
    remaining_allels = []
    secret_code_remaining = []

    for allel, chosen_allel in zip(genes, secret_code):
        if allel == chosen_allel:
            fitness_score += KEY_PEG_RED
        else:
            remaining_allels.append(allel)
            secret_code_remaining.append(chosen_allel)

    for allel in remaining_allels:
        if allel in secret_code_remaining:
            fitness_score += KEY_PEG_WHITE
            secret_code_remaining.remove(allel)
        else:
            continue

    return fitness_score
