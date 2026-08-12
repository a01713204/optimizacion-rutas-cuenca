def construir_solucion_inicial(
        nodos,
        demanda,
        distancia,
        deposito,
        capacidad=750,
        num_vehiculos=3):

    clientes = set(
        n for n in nodos
        if n != deposito
    )

    rutas = []

    for _ in range(num_vehiculos):

        ruta = [deposito]

        capacidad_restante = capacidad

        actual = deposito

        while True:

            candidatos = []

            for cliente in clientes:

                if (
                    demanda[cliente]
                    <= capacidad_restante
                ):

                    candidatos.append(
                        cliente
                    )

            if not candidatos:
                break

            siguiente = min(
                candidatos,
                key=lambda x:
                    distancia[actual][x]
            )

            ruta.append(
                siguiente
            )

            capacidad_restante -= (
                demanda[siguiente]
            )

            clientes.remove(
                siguiente
            )

            actual = siguiente

        ruta.append(
            deposito
        )

        rutas.append(
            ruta
        )

    # ==================================================
    # Si quedaron clientes sin asignar
    # ==================================================

    if len(clientes) > 0:

        print(
            "\nADVERTENCIA:"
        )

        print(
            len(clientes),
            "clientes quedaron sin asignar."
        )

        print(
            "Se requiere balanceo adicional."
        )

    return rutas


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