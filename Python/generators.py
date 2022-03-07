#example1
def genfunc():
    yield 1
    yield 2
    yield 3

for i in genfunc():
    print(i)

#example2
def square():
    i = 1
    while True:
        yield i*i
        i += 1

for k in square():
    if k > 200:
        break
    print(k)

#example3
str1 = 'onestring'
str_obj = iter(str1)

while True:
    try:
        item = next(str_obj)
        print(item)
    except StopIteration:
        break

#example4 map(), filter(), reduce()
def greet(name):
    return "Hello, {}! {}".format(name, "uhgiygiuhiu")

def greet_upper(name):
    return "Hello, {}!".format(name).upper()


def pr_greet(f, n):
    print(f(n))

pr_greet(greet, 'gh')


#example 5 map()
def func(a):
    return a*a

b = map(func, (1, 3, 2, 4)) 
print(b)
print(set(b))


#example 6 map()
tuple11 =  (4, 65, 3, 1, 12, 8, 19)
new_tuple = tuple(map(lambda x: x+2, tuple11))

print(new_tuple)


#example7 filter()
def func6(k):
    if k > 10:
        return k

x = filter(func6, (10, 12, 54, 9))
print(x)
print(list(x))

#we can crite same code like this
y = filter(lambda k: (k>10), (10, 12, 54, 9))
print(y)
print(list(y))

#example8 reduce()
from functools import reduce

print(reduce(lambda a,b: a+b, [1, 2, 3, 4]))
