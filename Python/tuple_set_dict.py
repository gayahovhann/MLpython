# first_set = {'a', 'b', 'a', 'c'}
# #print(first_set)
# first_set.append('f') # we can't to this
# print(first_set)
# print(len(first_set))



#Convert two lists into a dictionary
def ex_dict1():
    keys = ['Ten', 'Twenty', 'Thirty']
    values = [10, 20, 30]

    final_dict = {}
    for i in range(len(keys)):
        final_dict[keys[i]] = values[i]

    print(final_dict)

#Merge two Python dictionaries into one
def ex_dict2():
    dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
    dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
    dict1.update(dict2)
    print(dict1)

#Print the value of key ‘history’ from the below dict
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

#Initialize dictionary with default values
def ex_dict4():
    employees = ['Kelly', 'Emma']
    defaults = {"designation": 'Developer', "salary": 8000}
    final_dict = dict.fromkeys(employees, defaults)

ex_dict4()

#Create a dictionary by extracting 
# the keys from a given dictionary
def ex_dict5():
    sampleDict = { 
     "name": "Kelly",
     "age":25, 
     "salary": 8000, 
     "city": "New york" }

    keys = ["name", "salary"]
    final_dict = {}

    for k in keys:
        final_dict.update({k: sampleDict[k]})

    print(final_dict)


#Delete a list of keys from a dictionary
def ex_dict6():
    sample_dict = {
        "name": "Kelly",
        "age": 25,
        "salary": 8000,
        "city": "New York"
    }  
    keys = ["name", "salary"]
    for k in keys:
        sample_dict.pop(k)
    print(sample_dict)

ex_dict6()

#Check if a value exists in a dictionary
def ex_dict7(k):
    sample_dict = {'a': 100, 'b': 200, 'c': 300}
    if k in sample_dict.values():
        print (k, "is in the dict")


#Rename key of a dictionary
def ex_dict8():
    sample_dict = {
        "name": "Kelly",
        "age": 25,
        "salary": 8000,
        "city": "New York"
    }
    sample_dict["location"] = sample_dict.pop("city")
    return sample_dict

#Get the key of a minimum value
#from the following dictionary
def ex_dict9():
    sample_dict = {
        'Pysics': 82,
        'Math': 65,
        'History': 75
    }
    list_of_keys = sample_dict.values()
    return min(list_of_keys)


# Write a Python program to change Brad’s salary 
# to 8500 in the following dictionary.
def ex_dict10():

    sample_dict = {
        'emp1': {'name': 'Jhon', 'salary': 7500},
        'emp2': {'name': 'Emma', 'salary': 8000},
        'emp3': {'name': 'Brad', 'salary': 500}
    }
    sample_dict['emp3']['salary'] = 8500
    print(sample_dict)