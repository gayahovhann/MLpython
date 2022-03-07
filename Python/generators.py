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
