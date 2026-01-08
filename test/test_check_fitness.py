import pytest
from src.utils.check_fitness import check_fitness


@pytest.mark.parametrize(
    "genes, secret_code, fitness_score",
    [
        (["Red", "Red", "Yellow", "Yellow"], ["Cyan", "Green", "Purple", "Orange"], 0),
        (["Red", "Green", "Yellow", "Cyan"], ["Red", "Green", "Yellow", "Cyan"], 40),
        (["Red", "Cyan", "Purple", "Orange"], ["Red", "Red", "Purple", "Purple"], 20),
        (["Red", "Red", "Red", "Red"], ["Red", "Cyan", "Purple", "Purple"], 10),
    ],
)
def test_check_fitness(genes, secret_code, fitness_score):
    assert check_fitness(genes, secret_code) == fitness_score
