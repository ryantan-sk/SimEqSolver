from parsers.EqObject import Equation


class SolverMethod:

    @staticmethod
    def multiply_both_equation(eq1, eq2):
        CoList = [eq1.xco, eq1.yco, eq1.ans]
        NewList = [i*eq2.xco for i in CoList]
        new_eq = Equation(NewList)
        return new_eq

    @staticmethod
    def solve_for_y(eq1, eq2):
        if eq1.xco - eq2.xco == 0:
            y = (eq1.ans - eq2.ans)/(eq1.yco - eq2.yco)
        else:
            y = (eq1.ans + eq2.ans)/(eq1.yco + eq2.yco)

        return y

    @staticmethod
    def solve_for_x(y: object, eq1: object) -> object:
        x = (eq1.ans - (y*eq1.yco))/eq1.xco
        return x

