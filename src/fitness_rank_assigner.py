def fitness_rank_assigner(individual, fitness_score, expected_rank):

    if fitness_score <= 10:
        expected_rank['F'].append(individual)
    elif fitness_score <= 20:
        expected_rank['E'].append(individual)
    elif fitness_score <= 25:
        expected_rank['D'].append(individual)
    elif fitness_score <= 30:
        expected_rank['C'].append(individual)
    elif fitness_score <= 35:
        expected_rank['B'].append(individual)
    else:
        expected_rank['A'].append(individual)

    return expected_rank
