import math
def ex71():
    x = 2.4
    x1 = 0.2
    y = 0
    while x <= 7.6:
        y = math.tan(2*x + x**2)
        print(y)
        x = x + x1
ex71()