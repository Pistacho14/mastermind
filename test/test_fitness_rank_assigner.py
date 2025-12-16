import pytest
from src.fitness_rank_assigner import fitness_rank_assigner


@pytest.mark.parametrize(
    "individual, fitness_score, population_sorting_system, sorted_population ",
    [
        (1,
         35,
         {'A': [],'B': [],'C': [],'D': [],'E': [],'F': []},
         {'A': [],'B': [1],'C': [],'D': [],'E': [],'F': []}
         ),

        (2,
         10,
         {'A': [],'B': [],'C': [],'D': [],'E': [],'F': []},
         {'A': [],'B': [],'C': [],'D': [],'E': [],'F': [2]}
         ),

        (3,
         20,
         {'A': [],'B': [],'C': [],'D': [],'E': [],'F': []},
         {'A': [],'B': [],'C': [],'D': [],'E': [3],'F': []}
         ),

        (4,
         0,
        {'A': [],'B': [],'C': [],'D': [],'E': [],'F': []},
        {'A': [],'B': [],'C': [],'D': [],'E': [],'F': [4]}
        ),

        (5,
         30,
         {'A': [],'B': [],'C': [],'D': [],'E': [],'F': []},
         {'A': [],'B': [],'C': [5],'D': [],'E': [],'F': []}
         ),

        (6,
         25,
         {'A': [],'B': [],'C': [],'D': [],'E': [],'F': []},
         {'A': [],'B': [],'C': [],'D': [6],'E': [],'F': []}
         ),

        (7,
         15,
         {'A': [],'B': [],'C': [],'D': [],'E': [],'F': []},
         {'A': [],'B': [],'C': [],'D': [],'E': [7],'F': []}
         ),

        (8,
         40,
         {'A': [],'B': [],'C': [],'D': [],'E': [],'F': []},
         {'A': [8],'B': [],'C': [],'D': [],'E': [],'F': []}),
    ],
)
def test_population_sorter(individual, fitness_score, population_sorting_system, sorted_population):
    assert fitness_rank_assigner(individual, fitness_score, population_sorting_system) == sorted_population
