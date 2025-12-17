import pytest
from src.fitness_rank_assigner import fitness_rank_assigner


@pytest.mark.parametrize(
    "individual, fitness_score, population_sorting_system, sorted_population ",
    [
        (1,
         30,
         {'A': [],'B': [],'C': [],'D': [],'E': [],},
         {'A': [],'B': [1],'C': [],'D': [],'E': [],}
         ),

        (2,
         10,
         {'A': [],'B': [],'C': [],'D': [],'E': [],},
         {'A': [],'B': [],'C': [],'D': [],'E': [2],}
         ),

        (3,
         20,
         {'A': [],'B': [],'C': [],'D': [],'E': []},
         {'A': [],'B': [],'C': [],'D': [3],'E': []}
         ),

        (4,
         0,
        {'A': [],'B': [],'C': [],'D': [],'E': []},
        {'A': [],'B': [],'C': [],'D': [],'E': [4]}
        ),

        (5,
         30,
         {'A': [],'B': [],'C': [],'D': [],'E': []},
         {'A': [],'B': [5],'C': [],'D': [],'E': []}
         ),

        (6,
         25,
         {'A': [],'B': [],'C': [],'D': [],'E': []},
         {'A': [],'B': [],'C': [6],'D': [],'E': []}
         ),

        (7,
         15,
         {'A': [],'B': [],'C': [],'D': [],'E': []},
         {'A': [],'B': [],'C': [],'D': [7],'E': []}
         ),

        (8,
         40,
         {'A': [],'B': [],'C': [],'D': [],'E': []},
         {'A': [8],'B': [],'C': [],'D': [],'E': []}),
    ],
)
def test_population_sorter(individual, fitness_score, population_sorting_system, sorted_population):
    assert fitness_rank_assigner(individual, fitness_score, population_sorting_system) == sorted_population
