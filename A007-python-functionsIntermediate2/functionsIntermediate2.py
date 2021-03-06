# 1. Update Values in Dictionaries and Lists
# ------------------------------------------
x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
x[1][0] = 15

# Change the last_name of the first student from 'Jordan' to 'Bryant'
students[0]['last_name'] = "Bryant"

# In the sports_directory, change 'Messi' to 'Andres'
sports_directory['soccer'][0] = "Andres"

# Change the value 20 in z to 30
z[0]['y'] = 30

# 2. Iterate Through a List of Dictionaries
# ------------------------------------------
# Create a function iterateDictionary(some_list) that, given a list of dictionaries, the function loops through 
# each dictionary in the list and prints each key and the associated value. 
# For example, iterateDictionary(students) should output: 
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(lst):
    for student in students:
        stringRecord = ""
        for key in student:
            value = student.get(key)
            stringRecord += key + " - " + value + ", "

        print(stringRecord)

# iterateDictionary(students)

# 3. Get Values From a List of Dictionaries
# ------------------------------------------
# Create a function iterateDictionary2(key_name, some_list) that, given a list of 
# dictionaries and a key name, the function prints the value stored in that key for 
# each dictionary. For example, iterateDictionary2('first_name', students) should output:
# Michael
# John
# Mark
# KB
# iterateDictionary2('last_name', students) should output:
# Jordan
# Rosales
# Guillen
# Tonel

def iterateDictionary2(key, lst):
    if not isinstance(key, str): 
        print("Key should be a string")
    else: # sanitized input
        for student in students:

            foundKey = student.get(key)
            if not foundKey:
                print("Key not found")
                break
            else:
                print(student.get(key))

# iterateDictionary2('first_name', students)
# iterateDictionary2('last_name', students)
# iterateDictionary2('name', students)
# iterateDictionary2(24, students)
# iterateDictionary2([], students)


# 4. Iterate Through a Dictionary with List Values
# ------------------------------------------
# Create a function printInfo(some_dict) that given a dictionary whose values are all lists, prints the name of each key 
# along with the size of its list, and then prints the associated values within each key's list. For example:
# output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
    
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(my_dict):
    if not isinstance(my_dict, dict):
        print("Input should be a dictionary")
    else: 
        for key in my_dict:
            listSize = len(my_dict.get(key))
            print(f"{listSize} " + key.upper())

            lst = my_dict.get(key)
            for item in lst:
                print(item)

            print() # blank line seperator between key traversals

# printInfo(dojo)                 
# printInfo("Hello World")        # String input test
# printInfo([])                   # empty list input test
# printInfo(None)                 # null input test
# printInfo(24)                   # int input test