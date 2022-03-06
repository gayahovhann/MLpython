#example1
def genfunc():
    yield 1
    yield 2
    yield 3

for i in genfunc():
    print(i)

