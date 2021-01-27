empty_dict = {}
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct)

person = {
    'first_name' : 'Muhammad',
    'last_name' : 'Azeem',
    'age' : 250,
    'country' : 'UAE',
    'is_married' : True,
    'skills' : ['C#', 'iOS', 'Android', 'Python'],
    'address' : {
        'street' : 'Space street',
        'zipcode' : '02210'
    }
}
print(person)
print(len(dct))
print(len(person))
print(person.get('first_name'))
print(person.get('last_name'))
print(person.get('skills'))
print(person.get('address'))
print(dct)
dct['key5'] = 'value5'
print(dct)
dct['key2'] = 'value2 updates'
print(dct)
print(person.get('ages'))
print(person)
print('key2' in person)
print('key2' in dct)

# print(dct.popitem())
# print(dct)
# print(dct.pop('key4'))
# print(dct)
# key3 = dct.pop('key3')
# print(key3)
# print(dct)
# del dct['key2']
# print(dct)
# dct.pop('key1')
# print(dct)
# dct.clear()
# print(dct.items())
# print(dct.clear())
# del dct
# dct_copy = dct.copy()
# print(dct_copy)
# print(dct_copy.keys())
# print(dct.keys())
# print(dct_copy.keys())
# print(dct_copy.values())

# Create an empty dictionary called dog
dog = {}
print(dog)

# Add name, color, breed, legs, age to the dog dictionary
dog['name'] = 'Puppy'
dog['color'] = 'Gray'
dog['breed'] = 'Bully'
dog['legs'] = 4
dog['age'] = 1

# Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {
    'first_name': 'Muhammad', 
    'last_name':'Azeem', 
    'gender':'male', 
    'age': 31, 
    'marital_status':True, 
    'skills':['software development', 'C#', 'Swift'], 
    'country':'Pakistan', 
    'city':'Sharjah', 
    'address':{
        'flat':'1506, Tower 2',
        'area':'majaz 3'
        }
}
print(student)

# Get the length of the student dictionary
print(len(student))

# Get the value of skills and check the data type, it should be a list
skills = student.get('skills')
print(skills)
print(type(skills))

# Modify the skills values by adding one or two skills
skills.append('iOS')
skills.append('Android')
print(skills)

# Get the dictionary keys as a list
student_keys = list(student.keys())

# Get the dictionary values as a list
student_values = list(student.values())

# Change the dictionary to a list of tuples using items() method
student_tuple = tuple(student.items())
print(student_tuple)

# Delete one of the items in the dictionary
age = student.pop('age')
print(age)

# Delete one of the dictionaries
del student