from pyomo.environ import SolverFactory, value
from pyomo.opt import SolverStatus, TerminationCondition
from pyomo.environ import value


def resolver_modelo(model):

    print("\n===================================")
    print("RESOLVIENDO MODELO CVRP")
    print("===================================\n")

    solver = SolverFactory("highs")
    solver.options["time_limit"] = 600
    solver.options["mip_rel_gap"] = 0.10

    resultado = solver.solve(
        model,
        tee=True
    )

    print("\n===================================")
    print("RESULTADOS")
    print("===================================\n")

    print("Status:", resultado.solver.status)

    print(
        "Termination:",
        resultado.solver.termination_condition
    )

    if (
        resultado.solver.status == SolverStatus.ok
        and
        resultado.solver.termination_condition
        == TerminationCondition.optimal
    ):

        print("\nSOLUCIÓN ÓPTIMA ENCONTRADA")

        print(
            "Valor objetivo:",
            value(model.obj)
        )

    elif (
        resultado.solver.termination_condition
        == TerminationCondition.infeasible
    ):

        print(
            "\nERROR: El modelo es INFACITBLE"
        )

    else:

        print(
            "\nEl solver terminó sin encontrar óptimo."
        )




    return resultado