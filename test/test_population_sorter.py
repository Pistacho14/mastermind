import pytest
from src.population_sorter import population_sorter

@pytest.mark.parametrize(
    'individual,fitness_score,sorted_population',
    [
        (1, 35, {'A': [], 'B': [1], 'C': [], 'D': [], 'E': [], 'F': []}),
        (2, 10, {'A': [], 'B': [], 'C': [], 'D': [], 'E': [], 'F': [2]}),
        (3, 20, {'A': [], 'B': [], 'C': [], 'D': [], 'E': [3], 'F': []}),
        (4, 0,  {'A': [], 'B': [], 'C': [], 'D': [], 'E': [], 'F': [4]}),
        (5, 30, {'A': [], 'B': [], 'C': [5], 'D': [], 'E': [], 'F': []}),
        (6, 25, {'A': [], 'B': [], 'C': [], 'D': [6], 'E': [], 'F': []}),
        (7, 15, {'A': [], 'B': [], 'C': [], 'D': [], 'E': [7], 'F': []}),
        (8, 40, {'A': [8], 'B': [], 'C': [], 'D': [], 'E': [], 'F': []}),
    ],
)

def test_population_sorter(individual, fitness_score, sorted_population):
    assert population_sorter(individual, fitness_score) == sorted_population
