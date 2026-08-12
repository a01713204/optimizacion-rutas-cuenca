import copy
import random

def carga_ruta(
        ruta,
        demanda,
        deposito):

    return sum(
        demanda[n]
        for n in ruta
        if n != deposito
    )

def distancia_ruta(
        ruta,
        distancia):

    total = 0

    for i in range(
            len(ruta)-1):

        total += distancia[
            ruta[i]
        ][
            ruta[i+1]
        ]

    return total

def distancia_total(
        rutas,
        distancia):

    return sum(
        distancia_ruta(
            r,
            distancia
        )
        for r in rutas
    )

def generar_vecino(
        rutas,
        demanda,
        capacidad,
        deposito):

    vecino = copy.deepcopy(
        rutas
    )

    r1, r2 = random.sample(
        range(len(vecino)),
        2
    )

    if len(vecino[r1]) <= 3:
        return vecino, None

    if len(vecino[r2]) <= 3:
        return vecino, None

    i = random.randint(
        1,
        len(vecino[r1])-2
    )

    j = random.randint(
        1,
        len(vecino[r2])-2
    )

    cliente1 = vecino[r1][i]
    cliente2 = vecino[r2][j]

    vecino[r1][i] = cliente2
    vecino[r2][j] = cliente1

    carga1 = carga_ruta(
        vecino[r1],
        demanda,
        deposito
    )

    carga2 = carga_ruta(
        vecino[r2],
        demanda,
        deposito
    )

    if (
        carga1 > capacidad
        or
        carga2 > capacidad
    ):

        return None, None

    movimiento = (
        cliente1,
        cliente2
    )

    return vecino, movimiento

def tabu_search(
        rutas_iniciales,
        distancia,
        demanda,
        deposito,
        capacidad=750,
        max_iter=500,
        tabu_tenure=20):

    mejor_solucion = copy.deepcopy(
        rutas_iniciales
    )

    mejor_distancia = distancia_total(
        mejor_solucion,
        distancia
    )

    solucion_actual = copy.deepcopy(
        mejor_solucion
    )

    lista_tabu = []

    for it in range(max_iter):

        mejor_vecino = None

        mejor_movimiento = None

        mejor_valor = float("inf")

        for _ in range(100):

            vecino, movimiento = (
                generar_vecino(
                    solucion_actual,
                    demanda,
                    capacidad,
                    deposito
                )
            )

            if vecino is None:
                continue

            if movimiento in lista_tabu:
                continue

            valor = distancia_total(
                vecino,
                distancia
            )

            if valor < mejor_valor:

                mejor_valor = valor

                mejor_vecino = vecino

                mejor_movimiento = movimiento

        if mejor_vecino is None:
            continue

        solucion_actual = (
            mejor_vecino
        )

        lista_tabu.append(
            mejor_movimiento
        )

        if (
            len(lista_tabu)
            > tabu_tenure
        ):

            lista_tabu.pop(0)

        if (
            mejor_valor
            < mejor_distancia
        ):

            mejor_distancia = (
                mejor_valor
            )

            mejor_solucion = (
                copy.deepcopy(
                    mejor_vecino
                )
            )

        if it % 50 == 0:

            print(
                f"Iteración {it}"
            )

            print(
                "Mejor distancia:",
                round(
                    mejor_distancia,
                    2
                )
            )

    return (
        mejor_solucion,
        mejor_distancia
    )