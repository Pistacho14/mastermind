import matplotlib.pyplot as plt
from mastermind import mastermind
import os
import contextlib

NUM_RUNS = 100
MAX_TURNS = 14
LOSS_VALUE = MAX_TURNS + 1

results = []
all_fitness_histories = []

for i in range(NUM_RUNS):

    if i == 0:
        # Primera ejecución: se muestra por terminal
        result, fitness_history = mastermind()
    else:
        # Resto: salida silenciada (UTF-8 seguro)
        with open(os.devnull, 'w', encoding='utf-8') as fnull:
            with contextlib.redirect_stdout(fnull):
                result, fitness_history = mastermind()

    if isinstance(result, int):
        results.append(result)
    else:
        results.append(LOSS_VALUE)

    all_fitness_histories.append(fitness_history)

# 📊 Estadísticas
wins = [r for r in results if r != LOSS_VALUE]
losses = results.count(LOSS_VALUE)

avg_turn = sum(results) / len(results)
win_rate = len(wins) / NUM_RUNS * 100

print(f"Victorias: {len(wins)} / {NUM_RUNS}")
print(f"Derrotas: {losses}")
print(f"Win rate: {win_rate:.2f}%")
print(f"Turno medio (incluyendo derrotas): {avg_turn:.2f}")

# 📈 Gráfica 1: Histograma de resultados (100 ejecuciones)
plt.figure()
plt.hist(
    results,
    bins=range(1, LOSS_VALUE + 2),
    align="left"
)
plt.xlabel("Turno (15 = derrota)")
plt.ylabel("Número de partidas")
plt.title("Resultados de Mastermind (100 ejecuciones)")
plt.xticks(range(1, LOSS_VALUE + 1))
plt.grid(True)

# 📈 Gráfica 2: Fitness medio por generación (MEDIA DE 100 EJECUCIONES)
plt.figure()

max_generations = max(len(fh) for fh in all_fitness_histories)
avg_fitness_per_generation = []

for gen in range(max_generations):
    values = [
        fh[gen]
        for fh in all_fitness_histories
        if gen < len(fh)
    ]
    avg_fitness_per_generation.append(sum(values) / len(values))

plt.plot(
    range(1, len(avg_fitness_per_generation) + 1),
    avg_fitness_per_generation
)
plt.xlabel("Generación")
plt.ylabel("Fitness medio")
plt.title("Evolución del fitness medio por generación (100 ejecuciones)")
plt.grid(True)

plt.show()
