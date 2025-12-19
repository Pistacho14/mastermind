from src.peg_pattern_generator import peg_pattern_generator

def test_lenght_peg_patter():
    assert len(peg_pattern_generator()) == 4
