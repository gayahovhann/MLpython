import math
def ex421(matrix_m, k):
    a=0
    for i in range(len(matrix_m)):
        for j in range(i):
            if matrix_m[i][j] % k == 0:
                a +=1
    return a

def ex446(m_matrix, a, b):
    s=0
    for i in range(0, len(m_matrix)):
        for j in range(i, len(m_matrix)):
            if m_matrix[i][j] >= a and m_matrix[i][j]<= b:
                s+=m_matrix[i][j]
    return s 

def ex471(n_matrix):
    min_value = n_matrix[0][0]
    for i in range(0, len(n_matrix)):
        for j in range(0, i):
            if n_matrix[i][j] < min_value:
                min_value = n_matrix[i][j]
    return min_value

def ex496(matrix_nxn):
    max_val = matrix_nxn[0][0]
    for i in range(len(matrix_nxn)):
        for j in range(len(matrix_nxn)):
            if i == j and matrix_nxn[i][j] > max_val:
                matrix_nxn[i], matrix_nxn[j] = matrix_nxn[j], matrix_nxn[i]
    return matrix_nxn

