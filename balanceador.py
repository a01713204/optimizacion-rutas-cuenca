def carga_cluster(
        cluster,
        demanda):

    return sum(
        demanda[n]
        for n in cluster
    )


def balancear_clusters(
        clusters,
        demanda,
        capacidad=750):

    print("\nBALANCEANDO CLUSTERS...\n")

    cambio = True

    while cambio:

        cambio = False

        cargas = {

            c: carga_cluster(
                clusters[c],
                demanda
            )

            for c in clusters
        }

        cluster_exceso = None

        for c in cargas:

            if cargas[c] > capacidad:

                cluster_exceso = c
                break

        if cluster_exceso is None:

            break

        cluster_destino = min(
            cargas,
            key=cargas.get
        )

        exceso = (
            cargas[cluster_exceso]
            - capacidad
        )

        candidatos = sorted(

            clusters[cluster_exceso],

            key=lambda n:
                demanda[n],

            reverse=True

        )

        for nodo in candidatos:

            peso = demanda[nodo]

            if (
                cargas[cluster_destino]
                + peso
                <= capacidad
            ):

                clusters[
                    cluster_exceso
                ].remove(nodo)

                clusters[
                    cluster_destino
                ].append(nodo)

                cambio = True

                break

    return clusters