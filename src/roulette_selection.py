import random


def roulette_selection(population_sorted):
    reproducible_population = population_sorted.copy()
    weights = {'A': 0, 'B': 2, 'C': 10, 'D': 25, 'E': 35}
    valid_ranking = []
    valid_weights = []
    individuals_eliminated = []



    for ranking, individual in reproducible_population.items():
        if individual:
            valid_ranking.append(ranking)
            valid_weights.append(weights[ranking])

    while len(valid_ranking) > 3:
        eliminado = random.choices(valid_ranking,weights=valid_weights,k=1)[0]

        eliminated_index = valid_ranking.index(eliminado)

        individuals_eliminated.append(eliminado)

        valid_ranking.pop(eliminated_index)
        valid_weights.pop(eliminated_index)


    return [ind for group in reproducible_population.values() for ind in group]