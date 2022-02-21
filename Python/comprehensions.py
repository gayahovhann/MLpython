#examples for learning
#list
input_list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_comp = [i for i in input_list1 if i % 2 ==0]
print(list_comp)


#dist
input_list2 = [1, 2, 3, 4, 5, 6, 7]
dict_comp = {i:i**2 for i in input_list2 if i %2!=0}
print(dict_comp)

#set
input_list3 = [1, 2, 3, 4, 4, 5, 6, 6, 7, 7]
set_comp = {i for i in input_list3 if i % 2 ==0}
print(set_comp)