import re

from parsers.EqObject import Equation


class EquationParser:
    def __init__(self, input):
        self.input = input

    def __repr__(self):
        return f'<Equation: {self.input}, coefficients: {self.equation_coefficients}>'

    def get_equation(self):
        matcher = "[\d\.\-\+]+"
        coefficient_string = re.findall(matcher, self.input)
        coefficients = [float(e) for e in coefficient_string]
        return Equation(coefficients)
