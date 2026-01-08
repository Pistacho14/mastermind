import pytest
from src.population.population_mixer import population_mixer


@pytest.mark.parametrize(
    "current_population, secret_code, offspring, population_length",
    [
        (
            {
                1: ["Red", "Cyan", "Yellow", "Purple"],
                2: ["Green", "Green", "Yellow", "Purple"],
                3: ["Red", "Red", "Cyan", "Cyan"],
                4: ["Orange", "Purple", "Green", "Yellow"],
                5: ["Cyan", "Green", "Purple", "Red"],
                6: ["Yellow", "Yellow", "Red", "Green"],
            },
            ["Green", "Yellow", "Red", "Cyan"],
            {
                101: ["Red", "Green", "Yellow", "Purple"],
                102: ["Cyan", "Cyan", "Yellow", "Green"],
                103: ["Orange", "Purple", "Red", "Green"],
            },
            6,
        ),
    ],
)
def test_population_mixer(
    current_population, secret_code, offspring, population_length
):
    assert (
        len(population_mixer(current_population, secret_code, offspring))
        == population_length
    )
