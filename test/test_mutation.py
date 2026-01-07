import pytest
from src.mutation import mutation


@pytest.mark.parametrize(
    "individuo",
    [
        ["Red", "Red", "Yellow", "Yellow"],
        ["Cyan", "Purple", "Orange", "Yellow"],
    ],
)
def test_mutation(individuo):
    copia_individuo = individuo.copy()
    assert mutation(individuo) != copia_individuo
