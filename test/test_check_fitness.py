import pytest
from src.check_fitness import calculate_individual_fitness


@pytest.mark.parametrize(
    'peg_pattern,chosen_pegs,score',
    [
        (['Red','Red','Yellow','Yellow'], ['Cyan','Green','Purple', 'Orange'], 0),
        (['Red','Green','Yellow','Cyan'], ['Red','Green','Yellow', 'Cyan'], 40),
        (['Red','Cyan','Purple','Orange'], ['Red','Red','Purple', 'Purple'], 20),
        (['Red','Red','Red','Red'], ['Red','Cyan','Purple', 'Purple'], 10),

    ],

)

def test_calculate_individual_fitness(peg_pattern, chosen_pegs, score):
    assert calculate_individual_fitness(peg_pattern, chosen_pegs) == score
