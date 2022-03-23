import fractions

class MathFunc:
    def __init__(self, n1, n2, n3, n4):
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3
        self.n4 = n4
        self.frac1 = fractions.Fraction(self.n1, self.n2)
        self.frac2 = fractions.Fraction(self.n3, self.n4)

    def __add__(self):
        return self.frac1 + self.frac2

    def __sub__(self):
        return self.frac1 - self.frac2

    def __mul__(self):
        return self.frac1 * self.frac2

    def __divmod__(self):
        return self.frac1 / self.frac2


vle = MathFunc(1, 2, 1, 3)
print(vle.__divmod__())