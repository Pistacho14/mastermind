import pytest
from src.utils.check_winner import check_winner


@pytest.mark.parametrize(
    "population, expected_return",
    [
        (
            {
                "A": [["Purple", "Purple", "Orange", "Orange"]],
                "B": [],
                "C": [],
                "D": [],
                "E": [],
                "F": [],
                "G": [],
                "H": [],
            },
            True,
        ),
        (
            {
                "A": [],
                "B": [
                    ["Orange", "Orange", "Red", "Cyan"],
                    ["Purple", "Purple", "Orange", "Yellow"],
                    ["Purple", "Purple", "Yellow", "Red"],
                    ['Purple', 'Purple', 'Yellow', 'Purple'],
                ],
                "C": [],
                "D": [['Purple', 'Orange', 'Purple', 'Purple']],
                "E": [],
                "F": [],
                "G": [],
                "H": [],
            },
            False,
        ),
        (
            {
                "A": [],
                "B": [],
                "C": [['Cyan', 'Green', 'Orange', 'Orange'], ['Purple', 'Orange', 'Purple', 'Purple']],
                "D": [['Yellow', 'Purple', 'Orange', 'Yellow'], ['Red', 'Cyan', 'Yellow', 'Red']],
                "E": [['Purple', 'Yellow', 'Yellow', 'Red'], ['Purple', 'Orange', 'Purple', 'Green']],
                "F": [],
                "G": [],
                "H": [],
            },
            False,
        ),
        (
            {
                "A": [],
                "B": [],
                "C": [],
                "D": [],
                "E": [],
                "F": [],
                "G": [],
                "H": [],
            },
            False,
        ),
    ],
)
def test_check_winner(population, expected_return):
    assert check_winner(population) == expected_return
