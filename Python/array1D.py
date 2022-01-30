import math
def ex211(n_vector):
    s = 0
    k = 0
    for i in range(len(n_vector)):
        if n_vector[i]>0:
            k+=1
            s+= n_vector[i]
    return s/k
print(ex211([1, 2, 3, 5]))

def ex241(n_vec, k):
    s = 0
    for i in range(len(n_vec)):
        if n_vec[i] % 3 == 0:
            s = s + n_vec[i]
    return s
print(ex241([2, 6, 3, 6], 3))

def ex271(n_vc):
    k=0
    for i in range(len(n_vc)):
        if n_vc[i] == 'a':
            k += 1
    return k
print(ex271(['a', 'v', 'a', 'h']))


def ex301(k):
    new_vector = []
    for i in range(10, 100):
        if i % k == 0:
            new_vector = new_vector + i
    return new_vector
ex301(10)