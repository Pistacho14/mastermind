def check_fitness(peg_pattern, chosen_pegs):

    KEY_PEG_RED = 10
    KEY_PEG_WHITE = 5
    fitness_score = 0
    remaining_pegs = []
    chosen_pegs_remaining = []

    for peg, peg_choose in zip(peg_pattern, chosen_pegs):
        if peg == peg_choose:
            fitness_score += KEY_PEG_RED
        else:
            remaining_pegs.append(peg)
            chosen_pegs_remaining.append(peg_choose)

    for peg in remaining_pegs:
        if peg in chosen_pegs_remaining:
            fitness_score += KEY_PEG_WHITE
            chosen_pegs_remaining.remove(peg)
        else:
            continue

    return fitness_score
