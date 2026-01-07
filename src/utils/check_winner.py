def check_winner(current_population):
    winners = current_population.get("A")
    if winners != []:
        return True
    return False
