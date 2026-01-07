import pytest
from src.genetics.reproduction import reproduction


@pytest.mark.parametrize(
    "father, mother, offspring, counter, expected_offspring",
    [
        (
            ["Red", "Red", "Yellow", "Yellow"],
            ["Yellow", "Yellow", "Red", "Red"],
            {},
            3,
            {
                3: ["Red", "Red", "Red", "Red"],
                4: ["Yellow", "Yellow", "Yellow", "Yellow"],
            },
        ),
        (
            ["Cyan", "Purple", "Orange", "Yellow"],
            ["Yellow", "Green", "Red", "Orange"],
            {},
            1,
            {
                1: ["Cyan", "Purple", "Red", "Orange"],
                2: ["Yellow", "Green", "Orange", "Yellow"],
            },
        ),
    ],
)
def test_reproduction(father, mother, offspring, counter, expected_offspring):
    assert reproduction(father, mother, offspring, counter) == expected_offspring
