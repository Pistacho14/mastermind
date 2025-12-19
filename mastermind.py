from src.peg_pattern_generator import peg_pattern_generator
from src.first_population_generator import first_population_generator
from src.offspring_generator import offspring_generator
from src.check_winner import check_winner
from src.population_sorter import population_sorter
from src.roulette_selection import roulette_selection

def mastermind():
    secret_code = peg_pattern_generator()
    current_population = first_population_generator(75)
    is_found = False
    turn = 1

    if check_winner(population_sorter(current_population.copy(), secret_code)):
        return print("Has ganado!")

    while not is_found and turn < 14:
        current_population = offspring_generator(roulette_selection(population_sorter(current_population, secret_code)))
        is_found = check_winner(population_sorter(current_population.copy(), secret_code))
        turn += 1
        print(turn)

    if turn == 14:
        return print("Probablemente hayas perdido, o no, ni idea")
    else:
        return print("Has ganado en el turno" + " " + str(turn))

if __name__ == "__main__":
    mastermind()
