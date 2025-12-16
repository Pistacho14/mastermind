def check_fitness(peg_pattern, chosen_pegs):

    KEY_PEG_RED = 10
    KEY_PEG_WHITE = 5
    score = 0
    pegs_remaining = []
    chosen_pegs_remaining = []

    for peg, peg_choose in zip(peg_pattern, chosen_pegs):
        if peg == peg_choose:
            score += KEY_PEG_RED
        else:
            pegs_remaining.append(peg)
            chosen_pegs_remaining.append(peg_choose)

    for peg2 in pegs_remaining:
        if peg2 in chosen_pegs_remaining:
            score += KEY_PEG_WHITE
            chosen_pegs_remaining.remove(peg2)
        else:
            continue

    return score
