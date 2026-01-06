from .contants import COLOR_CIRCLE

def print_colours(peg_pattern):
    for color in peg_pattern:
        print(COLOR_CIRCLE.get(color), end=" ")
