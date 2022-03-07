def ex3(c):
    array = []
    for i in range(c):
        array.append(str(i)+'ba')

    return array

def ex4(array):  
    array2 = []
    for i in range(0, len(array), 2):
        array2.append(array[i])
    return array2

def ex5(array):
    print(max(array))

# d=2
# n = ex1(d)

# h = ex2(d, n)

# arr1 = ex3(h)

# arr2 = ex4(arr1)

# ex5(arr1)


class MyClass:
    def __init__(self, a):
        self.a = a
        self.b = self.a ** 2
        self.c = self.a + self.b

    def ex1(self):
        for i in range(self.b):
            print("Hello")

    def ex2(self):
        
        for i in range(0, self.c, 2):
            print(i, 'lala')
        return self.c
    
# valodik = MyClass(2)
# print(type(valodik))
# valodik.ex1()
# valodik.ex2()

