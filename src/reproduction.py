def reproduction(father, mother, offspring, counter):

    offspring[counter] = father[0:2] + mother[2::]
    offspring[counter + 1] = mother[0:2] + father[2::]
    return offspring
