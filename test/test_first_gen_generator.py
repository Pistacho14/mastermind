from src.first_gen_generator import first_population_generator

def test_length_first_population():
    population = 150
    assert len(first_population_generator(population)) == population
