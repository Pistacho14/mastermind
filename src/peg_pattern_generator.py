import random
from .contants import ALLELS

def genes_generator():
    genes_pattern = []
    for _ in range(4):
        genes_pattern.append(random.choice(ALLELS))

    assert isinstance(genes_pattern, list)
    return genes_pattern
