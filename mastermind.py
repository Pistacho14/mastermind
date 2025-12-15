from src.peg_pattern_generator import peg_pattern_generator
from src.first_gen_generator import first_population_generator


secret_code = peg_pattern_generator()
first_generation = first_population_generator(150)
is_found = False

for individual, peg_pattern in first_generation.items():
    if secret_code == peg_pattern:
        is_found = True
        break
    else:
        continue

if is_found:
    print("Se econtró la solución")
else:
    print("No se encontró la solución")
