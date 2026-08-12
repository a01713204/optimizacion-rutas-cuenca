from pyomo.environ import *

def crear_modelo(
    nodos,
    demanda,
    distancia,
    Q,
    num_vehiculos,
    deposito
):

    model = ConcreteModel()

    # ==================================================
    # CONJUNTOS
    # ==================================================

    clientes = [
        i for i in nodos
        if i != deposito
    ]

    vehiculos = range(
        1,
        num_vehiculos + 1
    )

    model.N = Set(
        initialize=nodos
    )

    model.C = Set(
        initialize=clientes
    )

    model.K = Set(
        initialize=vehiculos
    )

    # ==================================================
    # VARIABLES
    # ==================================================

    # x_ijk
    model.x = Var(
        model.N,
        model.N,
        model.K,
        domain=Binary
    )

    # y_ik
    model.y = Var(
        model.C,
        model.K,
        domain=Binary
    )

    # z_k
    model.z = Var(
        model.K,
        domain=Binary
    )

    # u_ik
    model.u = Var(
        model.C,
        model.K,
        domain=NonNegativeReals
    )

    # ==================================================
    # PARAMETRO MTZ
    # ==================================================

    M = len(clientes)

    # ==================================================
    # FUNCION OBJETIVO
    # ==================================================

    def objetivo(model):

        return sum(
            distancia[i][j]
            * model.x[i, j, k]

            for k in model.K
            for i in model.N
            for j in model.N

            if i != j
        )

    model.obj = Objective(
        rule=objetivo,
        sense=minimize
    )

    # ==================================================
    # (4)
    # CADA CLIENTE SE VISITA UNA SOLA VEZ
    # ==================================================

    def visita_unica(model, i):

        return sum(
            model.y[i, k]
            for k in model.K
        ) == 1

    model.visita_unica = Constraint(
        model.C,
        rule=visita_unica
    )

    # ==================================================
    # (5)
    # ENTRADA A CLIENTE
    # ==================================================

    def entrada_cliente(model, i, k):

        return sum(
            model.x[j, i, k]

            for j in model.N

            if j != i

        ) == model.y[i, k]

    model.entrada_cliente = Constraint(
        model.C,
        model.K,
        rule=entrada_cliente
    )

    # ==================================================
    # (6)
    # SALIDA DE CLIENTE
    # ==================================================

    def salida_cliente(model, i, k):

        return sum(
            model.x[i, j, k]

            for j in model.N

            if j != i

        ) == model.y[i, k]

    model.salida_cliente = Constraint(
        model.C,
        model.K,
        rule=salida_cliente
    )

    # ==================================================
    # (7)
    # SALE DEL DEPOSITO
    # ==================================================

    def salida_deposito(model, k):

        return sum(
            model.x[deposito, j, k]

            for j in model.C

        ) == model.z[k]

    model.salida_deposito = Constraint(
        model.K,
        rule=salida_deposito
    )

    # ==================================================
    # (8)
    # REGRESA AL DEPOSITO
    # ==================================================

    def regreso_deposito(model, k):

        return sum(
            model.x[i, deposito, k]

            for i in model.C

        ) == model.z[k]

    model.regreso_deposito = Constraint(
        model.K,
        rule=regreso_deposito
    )

    # ==================================================
    # (9)
    # CAPACIDAD DEL VEHICULO
    # ==================================================

    def capacidad(model, k):

        return sum(
            demanda[i]
            * model.y[i, k]

            for i in model.C

        ) <= Q * model.z[k]

    model.capacidad = Constraint(
        model.K,
        rule=capacidad
    )

    # ==================================================
    # (10)
    # MTZ
    # ==================================================

    def eliminar_subtour(
        model,
        i,
        j,
        k
    ):

        if i == j:
            return Constraint.Skip

        return (

            model.u[i, k]
            - model.u[j, k]
            + M * model.x[i, j, k]

            <= M - 1

        )

    model.subtour = Constraint(
        model.C,
        model.C,
        model.K,
        rule=eliminar_subtour
    )

    # ==================================================
    # (11)
    # ACOTACION DE U
    # ==================================================

    def limite_inferior(
        model,
        i,
        k
    ):

        return model.u[i, k] >= model.y[i, k]

    model.lim_inf = Constraint(
        model.C,
        model.K,
        rule=limite_inferior
    )

    def limite_superior(
        model,
        i,
        k
    ):

        return model.u[i, k] <= M * model.y[i, k]

    model.lim_sup = Constraint(
        model.C,
        model.K,
        rule=limite_superior
    )

    # ==================================================
    # PROHIBIR BUCLES
    # ==================================================

    def no_loop(
        model,
        i,
        k
    ):

        return model.x[i, i, k] == 0

    model.no_loop = Constraint(
        model.N,
        model.K,
        rule=no_loop
    )

    return model