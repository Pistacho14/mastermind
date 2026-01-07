import pytest
from src.population.population_sorter import population_sorter

dict1 = {
    1: ["Red", "Green", "Yellow", "Cyan"],
    2: ["Purple", "Orange", "Red", "Green"],
    3: ["Yellow", "Yellow", "Cyan", "Purple"],
    4: ["Green", "Red", "Orange", "Orange"],
    5: ["Cyan", "Purple", "Green", "Red"],
    6: ["Orange", "Yellow", "Red", "Purple"],
    7: ["Green", "Green", "Cyan", "Yellow"],
    8: ["Purple", "Red", "Orange", "Cyan"],
    9: ["Yellow", "Green", "Purple", "Red"],
    10: ["Orange", "Cyan", "Yellow", "Green"]
}


@pytest.mark.parametrize(
    "population, secret_code, sorted_population",
    [
        (
            dict1,
            ["Green", "Red", "Purple", "Cyan"],
            {
                "A": [],
                "B": [],
                "C": [["Purple", "Red", "Orange", "Cyan"]],
                "D": [
                    ["Red", "Green", "Yellow", "Cyan"],
                    ["Green", "Red", "Orange", "Orange"],
                    ["Cyan", "Purple", "Green", "Red"],
                    ["Yellow", "Green", "Purple", "Red"],
                ],
                "E": [
                    ["Purple", "Orange", "Red", "Green"],
                    ["Green", "Green", "Cyan", "Yellow"],
                ],
                "F": [
                    ["Yellow", "Yellow", "Cyan", "Purple"],
                    ["Orange", "Yellow", "Red", "Purple"],
                    ["Orange", "Cyan", "Yellow", "Green"],
                ],
                "G":[],
                "H": [],
            },
        ),
    ],
)
def test_population_sorter(population, secret_code, sorted_population):
    assert population_sorter(population, secret_code) == sorted_population
