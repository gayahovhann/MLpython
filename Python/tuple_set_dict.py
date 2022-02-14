# first_set = {'a', 'b', 'a', 'c'}
# #print(first_set)
# first_set.append('f') # we can't to this
# print(first_set)
# print(len(first_set))



#exrecise1 -> Convert two lists into a dictionary

def ex_dict1():
    keys = ['Ten', 'Twenty', 'Thirty']
    values = [10, 20, 30]

    final_dict = {}
    for i in range(len(keys)):
        final_dict[keys[i]] = values[i]

    print(final_dict)