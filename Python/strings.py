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
