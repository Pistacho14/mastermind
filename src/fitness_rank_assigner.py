def fitness_rank_assigner(individual, fitness_score, ranked_population):
    ranks = [
        (0, "H"),
        (5, "G"),
        (10, "F"),
        (15, "E"),
        (20, "D"),
        (25, "C"),
        (30, "B"),
        (float("inf"), "A"),
    ]

    for limit, rank in ranks:
        if fitness_score <= limit:
            ranked_population[rank].append(individual)
            break

    return ranked_population
