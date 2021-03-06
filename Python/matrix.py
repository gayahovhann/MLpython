import math
def ex421(matrix_m, k):
    a=0
    for i in range(len(matrix_m)):
        for j in range(i):
            if matrix_m[i][j] % k == 0:
                a +=1
    return a

def ex446(m_arr, a, b):
    s=0
    for i in range(0, len(m_arr)):
        for j in range(i, len(m_arr)):
            if m_arr[i][j] >= a and m_arr[i][j]<= b:
                s+=m_arr[i][j]
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

def ex521(D, n, m_arr):
    list_new_matrix = [m_arr.copy()]
    for j in range(n):
        for i in range(len(m_arr)):
            m_arr[i] = D * m_arr[i]
        list_new_matrix.append(m_arr.copy())
    return list_new_matrix

def ex546(m_matrix):
    k=0
    for l in range(len(m_matrix[0])):
        for i in range(len(m_matrix)):
            for j in range(i+1, len(m_matrix)):
                if m_matrix[i][l]==m_matrix[j][l]:
                    k += 1
                    break 
    k = len(m_matrix)-k+1
    return k 
   

def ex571(m_matrix, k):
    zero_vec = [0]*len(m_matrix)
    new_matrix = m_matrix.copy()
    new_matrix.insert(k-1, zero_vec)
    return new_matrix



def example(vec_m):
    a = True
    for i in range(len(vec_m)):
        for j in range(i+1, len(vec_m)):
            if vec_m[i]==vec_m[j]:
                a = False
        break 
    return a   



print(example([1, 2, 5, 6])) 


print(ex571([[1, 5, 2], [4, 5, 7], [7, 9, 2]], 2))


arr =  [1, 2, 3, 4]
print(ex521(3, 3,arr))
print(arr) 


print(ex546([[1, 2, 3, 5], 
             [3, 1, 2, 6],
             [2, 3, 4, 5]])) 