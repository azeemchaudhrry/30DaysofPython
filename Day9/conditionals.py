# # Day 9

# a = 0
# if a > 0:
#     print('A is a positive number')
# elif a < 0:
#     print('A is a negative number')
# else:
#     print('A is Zero')

# print('A is a positive number') if a > 0 else print('A is a negative number')

# if a == 0 and a % 2 == 0:
#     print('A is divisible by 2')

# user = 'admin'
# access_level = 3
# if user == 'admin' or access_level >= 4:
#     print('Access granted!')
# else:
#     print('Access denied!')

# age = int(input('Enter your age : '))
# if age >= 18:
#     print('you are old enough to learn and drive')
# else:
#     print(f'You need {18 - age} more years to learn to drive.')


# my_age = 31
# your_age = int(input('Enter your age : '))
# difference = my_age - your_age
# if my_age == your_age:
#     print('We are buddies.')
# elif my_age < your_age:
#     if my_age - your_age > 1:
#         print(f'You are {my_age - your_age} yours older than me')
#     else:
#         print(f'You are 1 your older than me')
# else:
#     print(f'You are younger than me')

# a = int(input('Enter number one : '))
# b = int(input('Enter number two : '))
# if a > b:
#      print(f'{a} is greater than {b}')
# elif a < b:
#     print(f'{a} is smaller than {b}')
# else:
#     print(f'{a} is equal to {b}')

# grade = int(input('Enter your marks : '))

# if 80 < grade < 100:
#     print('You got an A.')
# elif 70 < grade < 89:
#     print('Your grade is B.')
# elif 60 < grade < 69:
#     print('You secured C grade.')
# elif 50 < grade < 59:
#     print('You for D in your exams.')
# else:
#     print('You failed this subject.')


# autumn_months = ['september','october','november']
# winter_months = ['december','january','february']
# spring_months = ['march','april','may']
# summer_months = ['june','july','august']

# month = str(input('Enter month : '))

# if month.lower() in autumn_months:
#     print('Wow its charming day of Autumn.')
# elif month.lower() in winter_months:
#     print('Wow its cold day of Winter.')
# elif month.lower() in spring_months:
#     print('Wow its beautiful day of Spring.')
# elif month.lower() in summer_months:
#     print('Wow its sunny day of Summer.')
# else:
#     print('Month name is not correct.')

# fruits = ['banana', 'orange', 'mango', 'lemon']

# favorite_fruit = str(input('Enter your favorite fruit : '))
# if favorite_fruit not in fruits:
#     fruits.append(favorite_fruit.lower())
#     print(fruits)
# else:
#     print(f'{favorite_fruit} already exist in the list')

person={
'first_name': 'Asabeneh',
'last_name': 'Yetayeh',
'age': 250,
'country': 'Finland',
'is_married': True,
'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
'address': {
    'street': 'Space street',
    'zipcode': '02210'
}
}

# Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
skills = person.get('skills')

if 'skills' in person:
    skills = person.get('skills')
    print(skills[int(len(skills) /2)])

# Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
if 'skills' in person and 'Python' in person.get('skills'):
    print('Python is found!')
    
# If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
skills = person.get('skills')
if 'JavaScript' in skills and 'React' in skills:
    print('He is a front end developer')
elif 'Node' in skills and 'Python' in skills and 'MongoDB' in skills:
    print('He is a backend developer')
elif 'React' in skills and 'Node' in skills and 'MongoDB' in skills:
    print('He is a fullstack developer')
else:
    print('unknown title') 

# If the person is married and if he lives in Finland, print the information in the following format:
if person.get('is_married') and person.get('country') == 'Finland':
    first_name = person.get('first_name')
    last_name = person.get('last_name')
    country = person.get('country')
    print(f'{first_name} {last_name} lives in {country}. He is married.')

