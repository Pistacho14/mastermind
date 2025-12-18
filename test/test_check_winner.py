import pytest
from src.check_winner import check_winner

@pytest.mark.parametrize(
    'population, expected_return',
    [
        ({'A': [1],'B': [],'C': [],'D': [],'E': [],}, True),
        ({'A': [],'B': [1, 2, 3, 4],'C': [],'D': [5],'E': [],}, False),
        ({'A': [],'B': [],'C': [1, 2],'D': [3, 4],'E': [5, 6],}, False),
        ({'A': [],'B': [],'C': [],'D': [],'E': [],}, False),

    ],
)

def test_check_winner(population, expected_return):
    assert check_winner(population) == expected_return
