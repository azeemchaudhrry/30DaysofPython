#30 Days of Python

print(True)
print(False)

# Arithmetic Operations in Python
# Integers

print('Addition', 1+2)
print('Subtraction', 2-1)
print('Multiplication', 2*3)
print('Division',4/2)
print('Divison',6/2)
print('Division',7/2)
print('Division without the remainder', 7//2)
print('Modulus', 7%2)
print('Modulus', 3%2)
print('Division without the remainder', 7//3)
print('Exponentiation',3**2)
print('Exponentiation',3**200)

# Floats
print('Floating Point Number, PI', 3.14)
print('Floating Point Number, gravity', 9.81)

#Complex numbers
print('Complex number:',1+1j)
print('Multiplying complex numbers:',(1+1j) * (1-1j))

# Example for simple arithmetic 

print('== Addition, Subtraction, Multiplication, Division, Modulus ==')

number_one = 3
number_two = 4

total = number_one + number_two
difference = number_one - number_two
product = number_one * number_two
division = number_one / number_two
remainder = number_one % number_two
floor_division = number_one // number_two
exponential = number_one ** number_two

print('a = ', number_one)
print('b = ', number_two)
print('a + b = ', total)
print('a - b = ', difference)
print('a * b = ', product)
print('a / b = ', division)
print('a % b = ', remainder)
print('a // b = ', floor_division)
print('a ** b = ', exponential)

print('== Calculating area of a cirlce ==')
radius = 10
area_of_cicle = 3.14 * radius ** 2
print('Radius of circle:', radius)
print('Area of a circle:', area_of_cicle)

print('== Calculating area of a rectangle ==')
length = 10
width = 20
area_of_rectangle = length * width
print('Length of rectangle:', length)
print('Width of rectangle:', width)
print('Area of reactangle:', area_of_rectangle)

print('== Calculating a weight of an object ==')
mass = 75
gravity = 9.81
weight = mass * gravity
print(weight, 'N')

# Example: Comparison Operators

print(3 > 2)
print(3 < 2)
print(3 >= 2)
print(2 < 3)
print(2 <= 3)
print(3 == 2)
print(3 != 2)
print(len('milk') == len('meat'))
print('milk' == 'meat')
print('True == True', True == True)
print('True == False', True == False)
print('False == False', False == False)
print('True and True', True and True)
print('True or False', True or False)

print('1 is 1', 1 is 1)
print('1 is not 1', 1 is not 1)
print('A in Azeem', 'A' in 'Azeem')
print('M not in Azeem', 'M' not in 'Azeem')
print('m not in Azeem', 'm' not in 'Azeem')
print('4 is 2*2', 4 is 2*2)

# and, or, not

print(3 > 2 and 4 > 3)
print(3 < 2 or 4 < 2)
print(not 3 > 2)
print(not True)
print(not False)
print(not not True)
print(not not False)

# Exercises - Day 3

age = 31
height = 5.11
complex_number = 5j

# base = float(input('Enter base:'))
# height = float(input('Enter height:'))
# area_of_triangle = 0.5 * base * height
# print('The area of the triangle is ', area_of_triangle)

# side_a = input('Enter side a:')
# side_b = input('Enter side b:')
# side_c = input('Enter side c:')
# perimeter_triangle = side_a + side_b + side_c
# print('The perimeter of the triangle is ', perimeter_triangle)

# rectangle_length = int(input('Enter rectangle Length:'))
# rectangle_width = int(input('Enter rectangle Width:'))
# rectangle_area = rectangle_length * rectangle_width
# print('Rectangle Area is ', rectangle_area)
# rectangle_perimeter = 2 * (rectangle_length + rectangle_width)
# print('Rectangle perimeter is ', rectangle_perimeter)

# circle_radius = float(input('Enter radius of circle:'))
# circle_area = 3.14 * circle_radius ** 2
# circle_circumference = 2 * 3.14 * circle_radius
# print('Area of circle is ', circle_radius)
# print('Circumference of circle is ', circle_circumference)

x1 = 0
y1 = 0

x2 = (2 + y1) / 2
y2 = (2 * x1) - 2

print('x', x1, y1)
print('y', x2, y2)

first_slope = y2 -y1 / x2 - x1
print('first slope:', first_slope)

x1 = 2
x2 = 6
y1 = 2
y2 = 10
second_slope = y2 - y1 / x2 - x1
print('second slope', second_slope)

print('1st slope == 2nd slope ', first_slope == second_slope)

# Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is 0.

x = 0
y = x ** 2 + 6 * x + 9
print('Y : ', y)

x = 1
y = x ** 2 + 6 * x + 9
print('Y : ', y)

x = 2
y = x ** 2 + 6 * x + 9
print('Y : ', y)

x = -3
y = x ** 2 + 6 * x + 9
print('Y : ', y)

print('Length of python:',len('python'))
print('Length of jargon:',len('jargon'))

print(len('python') != len('jargon'))
print('on' in 'python' and 'on' in 'jargon')

print('jargon' in 'I hope this course is not full of jargon')

print('on' not in 'python' and 'on' not in 'jargon')

python_len = len('python')
print('Python length is ', python_len)
print('Python length as float is ', float(python_len))
print('Python length as string is ', str(python_len))

# entered_number = int(input('Enter Number: '))
# print('Is input number even : ', entered_number % 2 == 0)

print('Floor Division validation ', 7 // 3 is int(2.7))

print('is str(10) is equal to 10 : ', '10' is 10)

print('if int(\'9.8\') is equal to 10', int(9.8) is 10)

# hours = int(input('Enter hours: '))
# rate_per_hour = int(input('Enter rate per hour: '))
# print('Your weekly eaning is ', hours * rate_per_hour)

years_one_lived = int(input('Enter number of years you have lived: '))
seconds_lived = years_one_lived * 365 * 24 * 60 * 60
print('ou have lived for ' + str(seconds_lived) + ' seconds')

# Write a python script that displays the following table

print('1 1 1 1 1')
print('2 1 2 4 8')
print('3 1 3 9 27')
print('4 1 4 16 64')
print('5 1 5 25 125')