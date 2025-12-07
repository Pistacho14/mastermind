def calculate_individual_fitness(individual, peg_pattern, chosen_pegs):

    KEY_PEG_RED = 10
    KEY_PEG_WHITE = 5
    score = 0
    for peg in peg_pattern:
        chosen = [i for i, x in enumerate(chosen_pegs) if x == peg]
        if chosen == []:
            continue
        elif peg_pattern.index(peg) in chosen:
            score += KEY_PEG_RED
        else:
            score += KEY_PEG_WHITE * len(chosen)
    return score
