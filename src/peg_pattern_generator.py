import random

def peg_pattern_generator():

    pegs = ['Red','Cyan','Yellow', 'Purple', 'Green', 'Black', 'White', 'Orange']
    peg_pattern = []
    for _ in range(4):
        peg_pattern.append(random.choice(pegs))

    assert isinstance(peg_pattern,list)
    return peg_pattern
