import pytest
from src.population_sorter import population_sorter

dict1 = {
    1: ['Red', 'Green', 'Yellow', 'Cyan'],
    2: ['Purple', 'Orange', 'Red', 'Green'],
    3: ['Yellow', 'Yellow', 'Cyan', 'Purple'],
    4: ['Green', 'Red', 'Orange', 'Orange'],
    5: ['Cyan', 'Purple', 'Green', 'Red'],
    6: ['Orange', 'Yellow', 'Red', 'Purple'],
    7: ['Green', 'Green', 'Cyan', 'Yellow'],
    8: ['Purple', 'Red', 'Orange', 'Cyan'],
    9: ['Yellow', 'Green', 'Purple', 'Red'],
    10: ['Orange', 'Cyan', 'Yellow', 'Green']
}

@pytest.mark.parametrize(
    'population, secret_code, sorted_population',
    [
        (
         dict1,
         ['Green', 'Yellow', 'Red', 'Cyan'],
         {'A': [],'B': [],'C': [1],'D': [2, 3, 4, 5, 6, 7, 8, 9, 10],'E': []}
        ),
    ],
)

def test_population_sorter(population, secret_code, sorted_population):
    assert population_sorter(population, secret_code) == sorted_population
