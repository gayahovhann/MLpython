
arr = [3, 6, 1, 0, 2, 7]

for i in range(0, len(arr)):
    max_index = i
    for j in range(i+1, len(arr)):
        if arr[max_index] < arr[j]:
            max_index = j
    
    arr[i], arr[max_index] = arr[max_index], arr[i]


print(arr)