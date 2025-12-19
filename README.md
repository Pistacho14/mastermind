Mastermind
==========

- [Introducción](#introducción)
    - [Scope](#scope)
- [Manual](#manual)
    - [Requisitos](#requisitos)
    - [Instalación](#instalacion)
    - [Uso](#uso)
- [Metodología](#metodología)
- [Descripción técnica](#descripcio-tecnica)
    - [Diagrama de casos de uso](#digrama-de-casos-de-uso)
    - [Arquitectura de la aplicación](#arquitectura-de-la-aplicacion)
    - [Posibles tecnologías](#posiles-tecnologias)
- [Diseño](#diseño)
    - [Módulos](#modulos)
- [Implementación](#implementacion)
    - [Uso de IA](#uso-de-IA)
- [Pruebas](#pruebas)
    - [Casos test](#casos-test)
    - [Coverage](#coverage)
- [Análisis del tiempo invertido](#analisis-del-tiempo-invertido)
    - [Posibles mejoras](#posibles-mejoras)
- [Conclusiones](#conclusiones)

## Introducción
Este proyecto ha sido creado por [<strong>Xián Morales</strong>](https://github.com/MetalAsugom) y [<strong>Pablo González</strong>](https://github.com/Pistacho14), dos alumnos del ciclo de 1º de DAM en centro escolar [<strong>IES de Teis</strong>](https://www.edu.xunta.gal/centros/iesteis/). Este software crea generaciones de individuos con el objetivo de solucionar el código secreto del juego [<strong>Mastermind</strong>](https://en.wikipedia.org/wiki/Mastermind_(board_game)), que consiste en tratar de adivinar un código secreto compuesto por 4 bolas de colores (a elegir entre 6) mientras un jugador trata de adivinarlo en un máximo de 14 intentos.

## Metodología

Este software se ha desarrollado utilizando [TDD](https://en.wikipedia.org/wiki/Test-driven_development) (Test Driven Development) que se basa en el uso de casos test para desarrollar los módulos y así minimizar los errores que se introducen en el código. El uso de este método de desarrollo nos ayudó a crear los módulos de forma mas eficiente a pesar de que en algunos de ellos no era posible utilizar casos test debido a la naturaleza aleatoria de dichos scripts.

A parte de la TDD la otra metodología utilizada fue el desarrollo en cascada, desarrollando los módulos nuevos de forma lineal y en el orden en el que eran necesarios para la evolución del software. Al principio pensamos en intentar adoptar una metodología prototipada pero creímos que no encajaba en este proyecto ya que el prototipo sería practicamente idéntico a el producto final.

## Diseño

Al comienzo del desarrollo, tuvimos que elegir que método de reproducción sería el mas eficiente para la tarea a la que someteríamos a los individuos. Para no favorecer unicamente la explotación decidimos dejar de lado el método elitista debido al riesgo de estancamiento al crear individuos muy similares entre si. 

Al final nos decantamos por una reproducción sexual mixta mediante selección por ruleta que favorece a los individuos con mejores puntuaciones pero da una posibilidad a los individuos con peores puntuaciones de poder reproducirse.

![Probabilidades](/assets/probabilidades.png)

