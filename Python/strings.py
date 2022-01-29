def ex646(s):
    k=0
    for e in s:
        if e == 'a':
            k+=1

    return k
print(ex646('hafewgfaaaablanih'))


def ex657(s):
    new_s = ''
    for i in range(0, len(s)-1, 2):
        if s[i] > s[i+1]:
            new_s = new_s + s[i]
        else:
            new_s = new_s + s[i+1]
    if len(s)%2==1:
        new_s = new_s + s[-1]

    return new_s
print(ex657('aaaaa'))

def ex668(n):
    new_s = ''
    for i in range(len(n)):
        if ord(n[i]) % 3 == 0:
            new_s = new_s + n[i]
    return new_s
print(ex668('adefceff'))

def ex679(N):
    for i in range(N):
        print(chr(97+i))
ex679(5)

def ex690(string1):
    new_string = ''
    for i in range(len(string1)):
        if ord(string1[i]) >=97 and ord(string1[i]) <=122:
            new_string = new_string + chr(ord(string1[i])-32)
        else:
            new_string = new_string + chr(ord(string1[i])+32)
ex690('hhAeQ')