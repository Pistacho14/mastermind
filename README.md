Mastermind
==========

- [Introducción](#introducción)
- [Manual](#manual)
    - [Requisitos](#requisitos)
    - [Instalación](#instalación)
    - [Uso](#uso)
- [Metodología](#metodología)
- [Descripción técnica](#descripción-técnica)
    - [Diagrama de casos de uso](#diagrama-de-casos-de-uso)
    - [Arquitectura de la aplicación](#arquitectura-de-la-aplicación)
    - [Diagrama de dependencias](#diagrama-de-dependencias)
- [Diseño](#diseño)
    - [Módulos](#modulos)
- [Implementación](#implementación)
    - [Uso de IA](#uso-de-ia)
- [Pruebas](#pruebas)
    - [Casos test](#casos-test)
    - [Coverage](#coverage)
- [Análisis del tiempo invertido](#analisis-del-tiempo-invertido)
    - [Posibles mejoras](#posibles-mejoras)
- [Conclusiones](#conclusiones)

## Introducción
Este proyecto ha sido creado por [**Xián Morales**](https://github.com/MetalAsugom) y [**Pablo González**](https://github.com/Pistacho14), dos alumnos del ciclo de 1º de DAM en centro escolar [**IES de Teis**](https://www.edu.xunta.gal/centros/iesteis/). Este software crea generaciones de individuos con el objetivo de solucionar el código secreto del juego [**Mastermind**](https://en.wikipedia.org/wiki/Mastermind_(board_game)), que consiste en tratar de adivinar un código secreto compuesto por 4 bolas de colores (a elegir entre 6) mientras un jugador trata de adivinarlo en un máximo de 14 intentos.

## Manual
### Requisitos

Los requisitos para el funcionamiento son
- [Python](https://www.python.org)
- [Git](https://git-scm.com/)
- [Uv](https://docs.astral.sh/uv/)

### Instalación

### Linux 

Para instalar los requisitos en Linux sigue los siguientes pasos:

Clona el repositorio de github (en caso de no tener [Git](https://git-scm.com/), debes instalarlo).

`git clone https://github.com/Pistacho14/mastermind.git`

Instala Python:

`$ sudo apt install python3`

Instala uv:

`curl -LsSf https://astral.sh/uv/install.sh | less`

Instala las dependencias:

`uv sync --all-groups`

Inicia el entorno virtual:

`source venv/bin/activate`

### Windows

Para instalar los requisitos en Windows sigue los siguientes pasos:

Clona el repositorio de github (en caso de no tener [Git](https://git-scm.com/), debes instalarlo).

`git clone https://github.com/Pistacho14/mastermind.git`

Para instalar Python puedes instalarlo desde la web de [<ins>*Python*</ins>](https://www.python.org/downloads/) y seguir los pasos de la instalación.

Instala uv:

`powershell -c "irm https://astral.sh/uv/install.ps1 | more"`

Instala las dependencias:

`uv sync --all-groups`

Instala el entorno virtual:

`.\.venv\Scripts\activate.ps1`


### Uso

Para utilizar este software el usuario debe introducir uno de estos dos comandos:

`uv run .\benchmark.py`

o bien:

`uv run .\benchmark.py`

## Metodología

Este software se ha desarrollado utilizando [TDD](https://en.wikipedia.org/wiki/Test-driven_development) (Test Driven Development) que se basa en el uso de casos test para desarrollar los módulos y así minimizar los errores que se introducen en el código. El uso de este método de desarrollo nos ayudó a crear los módulos de forma mas eficiente a pesar de que en algunos de ellos no era posible la implementación debido a la naturaleza aleatoria de dichos scripts.

A parte de la TDD la otra metodología utilizada fue el desarrollo en cascada, desarrollando los módulos nuevos de forma lineal y en el orden en el que eran necesarios para la evolución del software. Al principio pensamos en intentar adoptar una metodología prototipada pero creímos que no encajaba en este proyecto ya que el prototipo sería practicamente idéntico al producto final.

## Descripción técnica

### Diagrama de casos de uso

![diagrama de casos de uso](/assets/useCases.jpg)

### Arquitectura de la aplicación

![arquitectura](/assets/arquitecture.png)

### Diagrama de dependencias

![diagrama de dependencias](/assets/diagramaDependencias.png)

## Diseño

Al comienzo del desarrollo, tuvimos que elegir que método de reproducción sería el mas eficiente para la tarea a la que someteríamos a los individuos. Para no favorecer unicamente la explotación decidimos dejar de lado el método elitista debido al riesgo de estancamiento al crear individuos muy similares entre si. 

Terminamos por decantarnos por la reproducción sexual mixta mediante selección por ruleta que favorece a los individuos con mejores puntuaciones pero da una posibilidad a los individuos con peores puntuaciones de poder reproducirse. Aun así elegimos reproducir solo una parte de la población y conservar otra, dando lugar a algo de exploración.


### Modulos

<strong>genes_generator.py:</strong> Selecciona entre seis alelos diferentes y genera un gen aleatorio con un tamaño máximo de cuatro colores que se pueden repetir.

<strong>initial_population_generator.py:</strong> Crea una generación inicial de 100 individuos aleatorios.

<strong>check_fitness.py:</strong> Calcula el fitness de cada gen.

<strong>fitness_rank_assigner.py:</strong> Asigna un ranking a cada gen de la población.

<strong>population_sorter.py:</strong> Crea el diccionario con los genes de la población y sus respectivos rankings.

<strong>roulette_selection.py:</strong> Elige mediante una ruleta ponderada parta seleccionar los individuos que se van a reproducir.

<strong>offspring_generator:</strong> Selecciona los padres y las madres y crea la descendencia.

<strong>reproduction.py:</strong> Con los padres y las madres se reproducen se reproducen nuevos individuos.

<strong>mutation.py:</strong> Da una probabilidad de mutar a los hijos.

<strong>population_mixer.py</strong> Crea la nueva generación con los hijos y mediante una rulta ponderada los sobrevivientes de la anterior generación.

<strong>constants.py:</strong> Archivo con todas las constantes usadas.

<strong>print_colors.py:</strong> Dibuja cada alelo del gen.

<strong>check_winner.py:</strong> Comprueba si algún gen es el ganador.

## Implementación

En este proyecto se ha usado:
- [Python](https://www.python.org)
- [Pytest](https://docs.pytest.org/en/stable/#): Utilizado para hacer los casos test.
- [Matplotlib](https://matplotlib.org/): Utilizado para crear las gráficas.
- [Random](https://docs.python.org/3/library/random.html): Utilizado en la generación de genes, las mutaciones de alelos, la selección de los padres y las ruletas ponderadas.
- [Git](https://git-scm.com/)
- [Markdown](https://www.markdownguide.org/)

### Uso-de-IA

- [ChatGPT](https://chatgpt.com/): Utilizado para proporcionar ejemplos de pseudo código, explicar concepto de genética y pedir ideas a la hora de refactorizar el código. Se usó para crear el archivo benchmark y print_colors.
- [Copilot](https://copilot.microsoft.com/): Utilizado para resolver dudas de código y problemas de ruta a la hora de hacer debugging.

Los fragmentos de código utilizados no se implementaron sin previamente saber que ha hacen, a excepción de benchmark.py debido al uso de [Matplotlib](https://matplotlib.org/).

## Pruebas

### Casos test

Se hicieron casos test para todas las funciones. Actualmente algunos casos test no pasan, pero se comprobaron y testearon antes de añadir los elementos aleatorios.

### Coverage

![Reporte de coverage](/assets/coverage.png)

## Analisis del tiempo invertido

Se ha invertido en el proyecto al rededor de 42 horas de trabajo sumando el resultado de [Wakatime](https://wakatime.com/dashboard) tenemos alrededor de las 42h de trabajo en el proyecto.
![wakatime1](/assets/wakatimeXian.png)

![wakatime2](/assets/wakatimePablo.png)
Este tiempo se invirtió en diferentes funciones (programación, documentación, debugging...) y el trabajo a lo largo del tiempo fue bastante dispar debido a las navidades, ya que a mayores de ser fechas concurridas en cuanto a eventos sociales estábamos un poco quemados de la rutina escolar así que decidimos tomarnos un descanso y retomarlo la semana previa a la entrega.

### Posibles mejoras

Tenemos pensado añadir precondiciones y postcondiciones a las funciones. Mejorar el rendimiento del código para cuando se lanzan las 100 ejecuciones para agilizarlo. Añadir markers a los casos test para poder hacer testing de manera independiente.

## Conclusiones

Este proyecto ha sido una iniciación de lo mas interesante al mundo de los algoritmos reproductivos y aunque hemos tenido que pelearnos bastante con la lógica, estamos muy contentos con el resultado final. Creemos que ajustando ciertas variables numéricas como los pesos, la probabilidad de mutación o la cantidad de la población que se reproduce frente a la que continua se podría optimizar la media de turnos que lleva encontrar el código secreto.