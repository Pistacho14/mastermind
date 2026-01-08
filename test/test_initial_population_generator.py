from src.population.initial_population_generator import initial_population_generator


def test_length_first_population():
    population_amount = 100
    assert len(initial_population_generator()) == population_amount
