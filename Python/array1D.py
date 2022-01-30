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

def ex331(x_vector):
    y_vector = []
    for i in range (len(x_vector)):
        for j in range (math.sqrt(x_vector[i])): #կլորացում դեպի վերև
            if j == math.sqrt(x_vector[i]):
                y_vector += x_vector[i]
    return y_vector
print(ex331([2, 4, 6, 8, 16]))

def ex361(m):
    s=0
    k=0
    for i in range(1, m+1):
        if i % 5 == 0 and i % 7 != 0:
            k+=1
            s+= i
    return k,s
print(ex361(15))

def ex391(x_vector, y_vector):
    # we have condition that len(x_vector) = len(y_vector) 
    s=0
    k=0
    new_vector = []
    for i in range(len(y_vector)):
        s+=y_vector[i]
        k+=1
    m = s / k
    for i in range(len(x_vector)):
        if x_vector[i] < m:
            new_vector += x_vector[i]

    return new_vector
print(ex391([2, 4, 1, 2], [12, 89, 44, 97]))