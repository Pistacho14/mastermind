import pytest
from src.population.fitness_rank_assigner import fitness_rank_assigner


@pytest.mark.parametrize(
    "genes, fitness_score, ranked_population, expected_ranked_population ",
    [
        (
            ['Yellow', 'Purple', 'Orange', 'Yellow'],
            30,
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
            {
                "A": [],
                "B": [['Yellow', 'Purple', 'Orange', 'Yellow']],
                "C": [],
                "D": [],
                "E": [],
                "F": [],
                "G": [],
                "H": [],
            },
        ),
        (
            ['Cyan', 'Cyan', 'Yellow', 'Orange'],
            10,
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
            {
                "A": [],
                "B": [],
                "C": [],
                "D": [],
                "E": [],
                "F": [['Cyan', 'Cyan', 'Yellow', 'Orange']],
                "G": [],
                "H": [],
            },
        ),
        (
            ['Cyan', 'Red', 'Purple', 'Green'],
            20,
            {"A": [], "B": [], "C": [], "D": [], "E": [], "F": [], "G": [], "H": []},
            {"A": [], "B": [], "C": [], "D": [['Cyan', 'Red', 'Purple', 'Green']], "E": [], "F": [], "G": [], "H": []},
        ),
        (
            ['Red', 'Cyan', 'Purple', 'Red'],
            0,
            {"A": [], "B": [], "C": [], "D": [], "E": [], "F": [], "G": [], "H": []},
            {"A": [], "B": [], "C": [], "D": [], "E": [], "F": [], "G": [], "H": [['Red', 'Cyan', 'Purple', 'Red']]},
        ),
        (
            ['Purple', 'Orange', 'Purple', 'Green'],
            30,
            {"A": [], "B": [], "C": [], "D": [], "E": [], "F": [], "G": [], "H": []},
            {"A": [], "B": [['Purple', 'Orange', 'Purple', 'Green']], "C": [], "D": [], "E": [], "F": [], "G": [], "H": []},
        ),
        (
            ['Cyan', 'Orange', 'Purple', 'Green'],
            25,
            {"A": [], "B": [], "C": [], "D": [], "E": [], "F": [], "G": [], "H": []},
            {"A": [], "B": [], "C": [['Cyan', 'Orange', 'Purple', 'Green']], "D": [], "E": [], "F": [], "G": [], "H": []},
        ),
        (
            ['Red', 'Orange', 'Purple', 'Green'],
            15,
            {"A": [], "B": [], "C": [], "D": [], "E": [], "F": [], "G": [], "H": []},
            {"A": [], "B": [], "C": [], "D": [], "E": [['Red', 'Orange', 'Purple', 'Green']], "F": [], "G": [], "H": []},
        ),
        (
            ['Orange', 'Yellow', 'Purple', 'Orange'],
            40,
            {"A": [], "B": [], "C": [], "D": [], "E": [], "F": [], "G": [], "H": []},
            {"A": [['Orange', 'Yellow', 'Purple', 'Orange']], "B": [], "C": [], "D": [], "E": [], "F": [], "G": [], "H": []},
        ),
    ],
)
def test_fitness_rank_assigner(
    genes, fitness_score, ranked_population, expected_ranked_population
):
    assert (
        fitness_rank_assigner(genes, fitness_score, ranked_population)
        == expected_ranked_population
    )
