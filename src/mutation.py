import random

def mutation(individuo, probabilidad_de_mutar, colores):
    individuo = individuo.copy()
    for i in range(4):
        if random.random() < probabilidad_de_mutar:
            nuevo = random.choice(colores)
            while nuevo == individuo[i]:
                nuevo = random.choice(colores)
            individuo[i] = nuevo
    return individuo
