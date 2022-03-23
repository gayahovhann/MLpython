import fractions

class MathFunc:
    def __init__(self, n1, n2, n3, n4):
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3
        self.n4 = n4
        self.frac1 = fractions.Fraction(self.n1, self.n2)
        self.frac2 = fractions.Fraction(self.n3, self.n4)

