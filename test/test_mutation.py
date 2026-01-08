import pytest
from src.genetics.mutation import mutation


@pytest.mark.parametrize(
    "individuo",
    [
        ["Red", "Red", "Yellow", "Yellow"],
        ["Cyan", "Purple", "Orange", "Yellow"],
    ],
)
def test_mutation(genes):
    original_genes_copy = genes.copy()
    assert mutation(genes) != original_genes_copy
