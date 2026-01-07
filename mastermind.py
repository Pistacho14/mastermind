from src.peg_pattern_generator import genes_generator
from src.first_population_generator import initial_population_generator
from src.offspring_generator import offspring_generator
from src.check_winner import check_winner
from src.population_sorter import population_sorter
from src.roulette_selection import roulette_selection
from src.print_colors import print_colors
from src.population_mixer import population_mixer
from src.contants import MAX_TURNS


# --- Required for the average fitness chart ---
def average_fitness(ranked_population):
    fitness_values = {
        "A": 40,
        "B": 30,
        "C": 25,
        "D": 20,
        "E": 15,
        "F": 10,
        "G": 5,
        "H": 0,
    }

    total_fitness = 0
    total_individuals = 0

    for rank, individuals in ranked_population.items():
        total_fitness += fitness_values[rank] * len(individuals)
        total_individuals += len(individuals)

    return total_fitness / total_individuals


# -------------------------------------------------


def mastermind():
    secret_code = genes_generator()
    current_population = initial_population_generator()
    turn = 0

    # --- Required for the average fitness chart ---
    fitness_history = []
    # -------------------------------------------------

    while turn < MAX_TURNS:
        ranked_population = population_sorter(current_population, secret_code)

        # --- Required for the average fitness chart ---
        fitness_history.append(average_fitness(ranked_population))
        # -------------------------------------------------

        for rank in ["A", "B", "C", "D", "E", "F", "G", "H"]:
            if ranked_population[rank]:
                print(f"Turn {turn + 1}: ", end="")
                print_colors(ranked_population[rank][0])
                break

        if check_winner(ranked_population):
            print("Winner, winner chicken dinner. Turn", turn + 1)
            print("Secret code:")
            print_colors(secret_code)

            # --- Required for the average fitness chart ---
            return turn + 1, fitness_history
            # -------------------------------------------------

        current_population = population_mixer(
            current_population,
            secret_code,
            offspring_generator(roulette_selection(ranked_population)),
        )
        turn += 1

    print("To the lobby champion")
    print("Secret Code:")
    print_colors(secret_code)

    # --- Required for the average fitness chart ---
    return fitness_history
    # -------------------------------------------------


if __name__ == "__main__":
    mastermind()
