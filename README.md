# Optimización de Rutas de Recolección de Basura 

Modelo de optimización para diseñar las rutas más eficientes de una flotilla de 3 camiones recolectores de basura en una ciudad.

Proyecto desarrollado como parte del curso **MA2001B - Optimización Determinista**, Tecnológico de Monterrey.

## Problema

66 puntos de recolección, 1 depósito (nodo 47), 3 camiones con capacidad máxima de 750 kg cada uno. Objetivo: minimizar la distancia total recorrida sin exceder la capacidad de ningún camión.

## Enfoque

Se modeló el problema como un **Vehicle Routing Problem Capacitado (CVRP)**, formulado primero en **FICO Xpress** y posteriormente traducido a Python con **Pyomo**. Dado que el problema es computacionalmente inviable por fuerza bruta a esta escala, se usó un algoritmo de clustering (*greedy*) para agrupar nodos por camión, seguido de **Tabu Search** para refinar las rutas.

## Resultado

Ruta óptima final de **14.67 km**, distribuida entre los 3 camiones:

| Camión | Carga |
| 1 | 722.64 kg |
| 2 | 747.84 kg |
| 3 | 685.49 kg |

## Estructura del repositorio
- CVRP.mos # Modelo original en FICO Xpress
- CVRP.txt # Modelo en formato de texto
- PROBLEMA_TEC.xlsx # Datos de la instancia (matriz de distancias y demandas)
- leer_instancia.py # Lectura y validación de los datos de entrada
- modelo.py # Formulación del modelo CVRP en Pyomo
- cvrp_inicial.py # Prueba del modelo con instancia reducida (10 nodos)
- balanceador.py # Algoritmo greedy de clustering por capacidad
- tabu_search.py # Metaheurística Tabu Search para refinar rutas
- resolver.py # Ejecución del solver
- extraer_rutas.py # Extracción y formato de las rutas finales
- main.py # Script principal que integra todo el proceso

## Herramientas

`Python` · `Pyomo` · `FICO Xpress` · `Tabu Search` · `Excel`

## Equipo

Celina Medina Bucio, Gael Ibáñez Yépez, Pablo Torres Dávila Galindo, Laura Thomas Godos, Patricio Barbosa Pérez Grovas

Tecnológico de Monterrey — Prof. Jorge Arturo Garza Venegas
