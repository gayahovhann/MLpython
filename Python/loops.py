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

def ex85():
    x = -3.3
    x1 = 0.3
    while x<= 2.7:
        Y = abs(2*x + x**3)
        print(Y)
        x = x+ x1
ex85()

def ex98(n):
    x=1
    sum = x
    for i in range (n, 2*n):
        x = 3.4* abs(x-7)
        sum = sum + x
    print(sum)
ex98(5)