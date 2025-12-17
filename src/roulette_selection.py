import random


def roulette_selection(population_sorted):
    reproducible_population = population_sorted.copy()
    weights = {'A': 0, 'B': 5, 'C': 10, 'D': 15, 'E': 20, 'F': 25}
    valid_ranking = []
    valid_weights = []
    individuals_eliminated = []



    for ranking, individual in reproducible_population.items():
        if individual:
            valid_ranking.append(ranking)
            valid_weights.append(weights[ranking])

        while len(valid_ranking) > 3:
            eliminado = random.choices(valid_ranking,weights=valid_weights,k=1)[0]

            eliminated_ranking_index = valid_ranking.index(eliminado)

            individuals_eliminated.append(eliminado)

            valid_ranking.pop(eliminated_ranking_index)
            valid_weights.pop(eliminated_ranking_index)


    for ranking in list(reproducible_population.keys()):
        if ranking not in valid_ranking or ranking in individuals_eliminated:
            del reproducible_population[ranking]

    return reproducible_population
