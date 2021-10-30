import math
def exerciseA():
    print("Enter integer")
    x = input()
    y = input()
    k = (int(y)+1) * (int(x) + pow((int(x)**2 + 1), 6) * math.sin(int(x)**2-3) - math.tan(int(y)))
    print(k)

exerciseA()