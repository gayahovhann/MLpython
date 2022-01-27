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

def ex113(x, n):
    sum = 0
    for i in range (n):
        sum = sum + ((x-1)*(x**2+1))**(2*n +1)
    print(sum)
ex113()

def ex127():
    P=1
    for i in range(1, 17):
        if i % 2 != 0:
            x = math.sin(i)**2
        else:
            x = 0
        if i % 2 != 0:
            y = math.tan(i)
        else:
            y = 1 / math.tan(i)
        P = x*x*y
    print("lalal", P)
ex127()

def ex141(a):
    sum = 0
    for m in range(5):
        for n in range(6):
            sum = sum + a**(m+n)
ex141(1)

def ex155():
    sum =0
    for i in range(10, 100):
        if i % 3 ==0:
            sum = sum + i
    print("sum =", sum)
ex155()