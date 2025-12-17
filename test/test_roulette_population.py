from src.roulette_selection import roulette_selection

def test_roulette_selection():
    assert len(roulette_selection({'A': [999],
                                   'B': [23,24,54,78],
                                   'C': [15],
                                   'D': [1],
                                   'E': [2, 3, 4, 5, 6, 7, 8, 9, 10],
                                   })) <= 3
