lst = [1, 5, 7, 2, 8, 9]
def sequence(lst):
    k = True
    for i in range (0, len(lst)-1):
        poped = lst.pop(i)
        for j in range (0, len(lst)-3):
            if lst[j] > lst[j+1]:
                k = False
        lst.insert(i, poped)
    return k

print(sequence(lst))
