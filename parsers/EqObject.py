class Equation:
    def __init__(self, list):
        self.xco = list[0]
        self.yco = list[1]
        self.ans = list[2]

    def __repr__(self):
        return f'< {self.xco}x + {self.yco}y = {self.ans}'
