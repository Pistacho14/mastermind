from .contants import COLOR_CIRCLE


def print_colors(genes):
    for allel in genes:
        print(COLOR_CIRCLE.get(allel), end=" ")
    print()
