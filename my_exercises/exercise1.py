import math


def exercise1():
    print("Enter integer")
    x = input()
    y = input()
    k = (int(y)+1) * (int(x) + pow((int(x)**2 + 1), 6) * math.sin(int(x)**2-3) - math.tan(int(y)))
    print(k)

def exercise11():
    print("Enter integers")
    x = int(input())
    a = int(input())
    b = int(input())
    if a ** 2 + b ** 2 > 5:
        y = 3 * math.exp(a - x) + log(a ** 2 + b ** 2 + 5, 3)
    elif int(a) ** 2 + b ** 2 < 1:
        y = pow(math.tan(a + b, 4))
    else:
        y = -3
    print(y)

def exercise21(x, y, z):
    k = max(x,y,z)
    return k


exercise1()
exercise11()
m = exercise21(5,6,8)
print(m)
