from .mutation import mutation


def reproduction(father, mother, offspring, child_id):
    first_child = father[0:2] + mother[2:]
    second_child = mother[0:2] + father[2:]

    first_child = mutation(first_child)
    second_child = mutation(second_child)

    offspring[child_id] = first_child
    offspring[child_id + 1] = second_child

    return offspring
