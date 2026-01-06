from src.peg_pattern_generator import peg_pattern_generator
from src.first_population_generator import first_population_generator
from src.offspring_generator import offspring_generator
from src.check_winner import check_winner
from src.population_sorter import population_sorter
from src.roulette_selection import roulette_selection
from src.print_colours import print_colours
from src.population_mixer import population_mixer

def mastermind():
    secret_code = peg_pattern_generator()
    current_population = first_population_generator(100)
    turn = 0
    MAX_TURNS = 14

    while turn < MAX_TURNS:
        sorted_population = population_sorter(current_population, secret_code)

        for rank in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']:
            if sorted_population[rank]:
                print(f"Turno {turn + 1}: ", end="")
                print_colours(sorted_population[rank][0])
                break

        if check_winner(sorted_population):
            return print("Has ganado en el turno", turn + 1), print("Código secreto:"), print_colours(secret_code)

        current_population = population_mixer(current_population, secret_code, offspring_generator(roulette_selection(sorted_population)))
        turn += 1

    print("Pal lobby campeón")
    print("Código secreto:")
    print_colours(secret_code)

if __name__ == "__main__":
    mastermind()
