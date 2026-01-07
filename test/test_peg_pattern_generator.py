from src.peg_pattern_generator import genes_generator


def test_lenght_peg_patter():
    assert len(genes_generator()) == 4
