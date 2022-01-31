import math
def ex421(matrix_m, k):
    a=0
    for i in range(len(matrix_m)):
        for j in range(i):
            if matrix_m[i][j] % k == 0:
                a +=1
    return a