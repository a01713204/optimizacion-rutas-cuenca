from leer_instancia import cargar_datos

from cvrp_inicial import (
    construir_solucion_inicial,
    carga_ruta,
    distancia_ruta,
    distancia_total

)

from tabu_search import (
    tabu_search
)

(
    nodos,
    demanda,
    distancia,
    Q,
    K,
    deposito
) = cargar_datos()

rutas = construir_solucion_inicial(
    nodos,
    demanda,
    distancia,
    deposito,
    Q,
    K
)

print("\nRUTAS INICIALES\n")

for i,ruta in enumerate(rutas):

    print(
        f"Camión {i+1}"
    )

    print(ruta)

    print(
        "Carga:",
        round(
            carga_ruta(
                ruta,
                demanda,
                deposito
            ),
            2
        )
    )

    print()

print(
    "Distancia total:",
    round(
        distancia_total(
            rutas,
            distancia
        ),
        2
    )
)


mejor_solucion,\
mejor_distancia = tabu_search(

    rutas,

    distancia,

    demanda,

    deposito,

    capacidad=Q,

    max_iter=500,

    tabu_tenure=20
)
print("\nRESULTADO FINAL\n")

for i,ruta in enumerate(
        mejor_solucion):

    print(
        f"Camión {i+1}"
    )

    print(ruta)

    print()

print(
    "Distancia total:",
    round(
        mejor_distancia,
        2
    )
)