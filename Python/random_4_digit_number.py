import random
list_of_number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list_of_number)
random.shuffle(list_of_number)
print(list_of_number)
a = 0
k=1000
if list_of_number[0] !=0:
    for i in range(0,3):
        a+=a +k*list_of_number[i]
        k= k/10
    print(a)

else:
    for i in range(0,3):
        a+=a +k*list_of_number[i+1]
        k=k/10
    print(a)
