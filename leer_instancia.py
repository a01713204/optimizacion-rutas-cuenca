import pandas as pd

def cargar_datos(archivo="PROBLEMA_TEC.xlsx"):

    # ==================================================
    # HOJA PARAMETROS
    # ==================================================

    parametros = pd.read_excel(
        archivo,
        sheet_name="parametros",
        header=None
    )

    Q = float(parametros.iloc[0, 1])
    num_vehiculos = int(parametros.iloc[1, 1])
    deposito = int(parametros.iloc[2, 1])

    # ==================================================
    # HOJA NODOS
    # ==================================================

    nodos_df = pd.read_excel(
        archivo,
        sheet_name="nodos",
        header=None
    )

    nodos = [
        int(n)
        for n in nodos_df.iloc[:, 0]
    ]

    demanda = {
        int(row[0]): float(row[1])
        for _, row in nodos_df.iterrows()
    }

    # ==================================================
    # HOJA DISTANCIA
    # ==================================================

    dist_df = pd.read_excel(
        archivo,
        sheet_name="distancia",
        index_col=0
    )

    # Convertir encabezados a enteros
    dist_df.columns = [
        int(c)
        for c in dist_df.columns
    ]

    dist_df.index = [
        int(i)
        for i in dist_df.index
    ]

    distancia = {}

    for i in dist_df.index:

        distancia[i] = {}

        for j in dist_df.columns:

            distancia[i][j] = float(
                dist_df.loc[i, j]
            )

    # ==================================================
    # VALIDACIONES
    # ==================================================

    print("\n===== INSTANCIA CARGADA =====")

    print(f"Nodos: {len(nodos)}")

    print(f"Vehículos: {num_vehiculos}")

    print(f"Capacidad por vehículo: {Q}")

    print(f"Depósito: {deposito}")

    print(
        f"Demanda total: "
        f"{sum(demanda.values()):.2f} kg"
    )

    print(
        f"Capacidad total: "
        f"{Q*num_vehiculos:.2f} kg"
    )

    print(
        f"Matriz: "
        f"{len(dist_df)} x {len(dist_df.columns)}"
    )

    return (
        nodos,
        demanda,
        distancia,
        Q,
        num_vehiculos,
        deposito
    )


# ==================================================
# PRUEBA
# ==================================================

if __name__ == "__main__":

    (
        nodos,
        demanda,
        distancia,
        Q,
        K,
        deposito
    ) = cargar_datos()