import pytest
from src.offspring_generator import offspring_generator


@pytest.mark.parametrize(
    "reproducible_population, offspring",
    [
        (
            [["Red", "Red", "Yellow", "Yellow"], ["Yellow", "Yellow", "Red", "Red"]],
            {
                1: ["Yellow", "Yellow", "Yellow", "Yellow"],
                2: ["Red", "Red", "Red", "Red"],
            },
        ),
        (
            [
                ["Cyan", "Purple", "Orange", "Yellow"],
                ["Yellow", "Green", "Red", "Orange"],
            ],
            {
                1: ["Yellow", "Green", "Orange", "Yellow"],
                2: ["Cyan", "Purple", "Red", "Orange"],
            },
        ),
    ],
)
def test_offspring_generator(reproducible_population, offspring):
    assert sorted(offspring_generator(reproducible_population).values()) == sorted(
        offspring.values()
    )
