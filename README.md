Mastermind
==========

- [Introducción](#introducción)
    - [Scope](#scope)
- [Manual](#manual)
    - [Requisitos](#requisitos)
    - [Instalación](#instalacion)
    - [Uso](#uso)
- [Metodología](#metodologia)
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