# Day 10 Loops
from countries import * 

# While Loop
# count = 0
# while count < 5:
#     if count == 3:
#         break
#     print(count)
#     count = count + 1

# numbers = [0,2,3,4,5,6,7,8,9,10]
# for number in numbers:
#     print(number)

# language = 'Python'
# for letter in language:
#     print(letter)

# tpl = ('python','updates','wow')
# for number in tpl:
#     print(number)

# person = {
#     'first_name':'Asabeneh',
#     'last_name':'Yetayeh',
#     'age':250,
#     'country':'Finland',
#     'is_marred':True,
#     'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
#     'address':{
#         'street':'Space street',
#         'zipcode':'02210'
#     }
# }

# print('------------------------------------')
# for key in person:
#     print(key)

# print('------------------------------------')
# for key,value in person.items():
#     print(key, value)

# print('--------------------------------------')
# it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
# for company in it_companies:
#     print(company)

# print('--------------------------------------')
# numbers = (0,1,2,3,4,5,6,7)
# for number in numbers:
#     print(number)
#     if(number == 3):
#         break

# print('--------------------------------------')
# for number in numbers:
#     print(number)
#     if(number == 3):
#         continue

# print('--------------------------------------')
# numbers = (0,1,2,3,4,5)
# for number in numbers:
#     print(number)
#     if number == 3:
#         continue
#     print('Next number should be ', number + 1) if number != 5 else print("loop's end") # for short hand conditions need both if and else statements
# print('outside the loop')

# print('--------------------------------------')
# lst = list(range(11))
# print(lst)
# st = set(range(1,11))
# print(st)

# lst = list(range(0,11,2))
# print(lst)
# st = set(range(0,11,2))
# print(st)

# Exercises: Day 10

# Iterate 0 to 10 using for loop, do the same using while loop.

# numbers = [0,1,2,3,4,5,6,7,8,9,10]
# for number in numbers:
#     print(number)

# count = 0
# while count < 10:
#     print(count)
#     count += 1 

# Iterate 10 to 0 using for loop, do the same using while loop.

# for number in range(10,-1,-1):
#     print(number)

# count = 10
# while count > -1:
#     print(count)
#     count -= 1 

# Write a loop that makes seven calls to print(), so we get on the output the following triangle:
for index in range(0,8):
    print(index * '#')

limit = 9
for i in range(0,limit):
    for j in range(0,limit):
        print('# ', end='')
    print('')

for i in range(0, 11):
    print(f'{i} x {i} = {i * i}')

frameworks = ['Python', 'Numpy','Pandas','Django', 'Flask'] 
for framework in frameworks:
    print(framework)

for i in range(0,101):
    if i % 2 == 0:
        print(i)

for i in range(0,101):
    if i % 2 != 0:
        print(i)

sum = 0
for i in range(0,101):
    sum += i

print('The sum of all numbers is : ', sum)

even_sum = odd_sum = 0
for i in range(0,101):
    if i % 2 == 0:
        even_sum += i
    elif i % 2 != 0:
        odd_sum += i

print(f'The sum of all evens is {even_sum}. And the sum of all odds is {odd_sum}.')

for country in countries:
    if 'land' in country:
        print(country)

fruits = ['banana', 'orange', 'mango', 'lemon']
total_elements = len(fruits) - 1
for i in range(0, int(len(fruits) / 2)):
    temp_element = fruits[i]
    fruits[i] = fruits[total_elements - i]
    fruits[total_elements - i] = temp_element

print(fruits)