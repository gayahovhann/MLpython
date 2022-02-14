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

def ex_dict2():
    dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
    dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
    dict1.update(dict2)
    print(dict1)

def ex_dict3():
    sampleDict = {
        "class": {
            "student": {
                "name": "Mike",
                "marks": {
                    "physics": 70,
                    "history": 80
                }
            }
        }
    }
    print(sampleDict['class']['student']['marks']['history'])

