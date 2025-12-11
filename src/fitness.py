def calculate_individual_fitness(peg_pattern, chosen_pegs):

    KEY_PEG_RED = 10
    KEY_PEG_WHITE = 5
    score = 0
    for peg, peg_choose in zip(peg_pattern, chosen_pegs):
        if peg != peg_choose:
            continue
        elif peg == peg_choose:
            score += KEY_PEG_RED
        else:
            score += KEY_PEG_WHITE

    return score
