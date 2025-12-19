def fitness_rank_assigner(individual, fitness_score, sorted_population):

    if fitness_score <= 10:
        sorted_population['E'].append(individual)
    elif fitness_score <= 20:
        sorted_population['D'].append(individual)
    elif fitness_score <= 25:
        sorted_population['C'].append(individual)
    elif fitness_score <= 30:
        sorted_population['B'].append(individual)
    else:
        sorted_population['A'].append(individual)

    return sorted_population
