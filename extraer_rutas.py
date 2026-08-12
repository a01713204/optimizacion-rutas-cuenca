from pyomo.environ import value

def extraer_rutas(
        model,
        deposito,
        num_vehiculos,
        nodos):

    rutas = {}

    for k in range(1, num_vehiculos + 1):

        ruta = [deposito]

        actual = deposito

        visitados = set()

        while True:

            siguiente = None

            for j in nodos:

                if actual == j:
                    continue

                try:

                    if value(
                        model.x[
                            actual,
                            j,
                            k
                        ]
                    ) > 0.5:

                        siguiente = j
                        break

                except:
                    pass

            if siguiente is None:
                break

            ruta.append(siguiente)

            if siguiente == deposito:
                break

            if siguiente in visitados:
                break

            visitados.add(siguiente)

            actual = siguiente

        rutas[k] = ruta

    return rutas