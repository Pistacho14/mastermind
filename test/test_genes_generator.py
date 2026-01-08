from src.genetics.genes_generator import genes_generator


def test_lenght_genes():
    assert len(genes_generator()) == 4
