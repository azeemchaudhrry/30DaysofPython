# Day 2: 30 Days of Programming

first_name = 'Hafiz Muhammad First'
last_name = 'Azeem Last'
full_name = last_name + first_name

country = 'Pakistan'
city = 'Okara'
age = 31
year = 2021
is_married = True
is_true = True
is_light_on = False

# print('First name:',first_name)
# print('First name type :', type(first_name))
# print('Last name:', last_name)
# print('Last name type:', type(last_name))
# print('Full name:', full_name)
# print('Type of full name:', type(full_name))


first_name, last_name, full_name = 'Hafiz Muhammad', 'Azeem', first_name + last_name

# print('First name:',first_name)
# print('First name type :', type(first_name))
# print('Last name:', last_name)
# print('Last name type:', type(last_name))
# print('Full name:', full_name)
# print('Type of full name:', type(full_name))

print('first_name is type of',type(first_name))
print('last_name is type of',type(last_name))
print('full_name is type of',type(full_name))
print('country is type of',type(country))
print('city is type of',type(city))
print('age is type of',type(age))
print('year is type of',type(year))
print('is_married is type of',type(is_married))
print('is_light_on is type of', type(is_light_on))

print('Length of first name', len(first_name))


def cmp(a, b):
    return (a < b) - (a > b)

print('Compare first and last name', cmp(len(first_name), len(last_name)))

num_one = 5
num_two = 4

_total = num_one + num_two
_diff = num_one - num_two
_product = num_two * num_one
_division = num_one / num_two
_remainder = num_two % num_one
_exp = num_two ** num_one
_floor_division = num_one // num_two

print('Total:', _total)
print('Difference:', _diff)
print('Product:', _product)
print('Division:', _division)
print('Remainder:',_remainder)
print('Exponential:', _exp)
print('Floor Division:', _floor_division)

print('---------------------------------------------')

radius = 30
area_of_circle = 2*3.14*radius
circum_of_circle = 2 * radius
print('Radius:', radius)
print('Area of Circle:', area_of_circle)
print('Circumference of Circle:', circum_of_circle)

print('---------------------------------------------')

user_input_radius = float(input('Enter radius:'))
area_of_circle_user = 2*3.14*user_input_radius
print('Radius:', user_input_radius)
print('Area of Circle User input:', area_of_circle_user)

print('---------------------------------------------')

first_name = str(input('Enter first name: '))
last_name = str(input('Enter last name: '))
country = str(input('Country: '))
age = int(input('Age: '))

print('First name:', first_name)
print('Last name:', last_name)
print('Country:', country)
print('Age:', age)

print('---------------------------------------------')

help('keywords')