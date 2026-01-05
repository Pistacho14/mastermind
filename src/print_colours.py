COLOR_CIRCLE = {
    'Red': "🔴",
    'Cyan': "🔵",
    'Green': "🟢",
    'Yellow': "🟡",
    'Orange': "🟠",
    'Purple': "🟣"
}

def print_colours(peg_pattern):
    for color in peg_pattern:
        print(COLOR_CIRCLE.get(color, "⚪"), end=" ")
    print()
