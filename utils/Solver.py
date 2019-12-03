from parsers.EqParser import EquationParser
from utils.Method import SolverMethod


class EqSolver:
    def __init__(self, eq1, eq2):
        self.eq1 = EquationParser(eq1).get_equation()
        self.eq2 = EquationParser(eq2).get_equation()

    def solution(self):
        eq3 = SolverMethod.multiply_both_equation(self.eq1, self.eq2)
        eq4 = SolverMethod.multiply_both_equation(self.eq2, self.eq1)
        y = SolverMethod.solve_for_y(eq3, eq4)
        x = SolverMethod.solve_for_x(y, self.eq1)
        return x, y
