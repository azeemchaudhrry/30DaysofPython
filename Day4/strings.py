
# a = 4
# b = 3

# print('%d + %d = %d' % (a, b, a + b))
# print('{} + {} = {}'.format(a, b, a + b))
# print(f'{a} + {b} = {a + b}')

# language = 'Python'
# print(language[0])
# print(language[-1])
# print(language[0:3])
# print(language[-3:])
# print(language[::-1])
# print(language.capitalize())
# print(language.count('o'))
# print(language.index('th'))
# print(language.rindex('th'))
# print(language.isalnum())

# Exercise
title = ['Thirty', 'Days', 'Of', 'Python']
print(' '.join(title))

coding_for_all = ['Coding', 'For', 'All']
print(' '.join(coding_for_all))

company = 'Coding For All'
print(company)
print('Length of \'%s\' is %d' % (company, len(company)))
print(company.upper())
print(company.lower())
print('Coding For All'.capitalize())
print('Coding For All'.title())
print('Coding For All'.swapcase())
# Cut(slice) out the first word of Coding For All string.
# Check if Coding For All string contains a word Coding using the method index, find or other methods.
coding_for_all = 'Coding For All'
print('check Coding contains index : ', coding_for_all.find('Coding'))
print('check Coding contains index : ', coding_for_all.index('Coding'))
# Replace the word coding in the string 'Coding For All' to Python.
coding_for_all = coding_for_all.replace('Coding', 'Python')
print(coding_for_all)
# Change Python for Everyone to Python for All using the replace method or other methods.
coding_for_all = coding_for_all.replace('All', 'Everyone')
print(coding_for_all)
# Split the string 'Coding For All' using space as the seperator(split())
splits = coding_for_all.split(' ')
print(splits[0])
print(splits[1])
print(splits[2])
# "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
splits = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(',')
print(splits[4])
# What is the character at index 0 in the string Coding For All.
coding_for_all = 'Coding For All'
print(coding_for_all[0])
# What is the last index of the string Coding For All.
print(len(coding_for_all) - 1)
# What character is at index 10 in 'Coding For All' string.
print(coding_for_all[10])
# Creae an acronym or an abbreviation for the name 'Python For Everyone'.
# Create an acronym or an abbreviation for the name 'Coding For All'.
# Use index to determine the position of the first occurrence of C in Coding For All.
print('Position of first C occurrence : ', coding_for_all.index('C'))
# Use index to determine the position of the first occurrence of F in Coding For All.
print('Position of first F occurrence : ', coding_for_all.index('F'))
# Use index of find to find the position of the first occurrence of I Coding For All.
print(f'Position of last l in {coding_for_all} : ', coding_for_all.rfind('l'))
# Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print('Position of first occurrence of \'because\' : ', 'You cannot end a sentence with because because because is a conjunction'.find('because'))

print(' Last Occurrence of word \'because\' : ', 'You cannot end a sentence with because because because is a conjunction'.rfind('becuase'))

spaced_coding_for_all = '   Coding For All      '
print(spaced_coding_for_all.strip(' '))
thirtyDaysOfPython = '30DaysOfPython'
thirty_days_of_python = 'thirty_days_of_python'
print('Is 30DaysOfPython a valid identifier: ', thirtyDaysOfPython.isidentifier())
print('Is thirty_days_of_python a valid identifier: ', thirty_days_of_python.isidentifier())

python_libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
python_libraries_str = '# '.join(python_libraries)
print(python_libraries_str)

print('I am enjoying this challenge.\nI just wonder what is next.')

print('Name\tAge\tCountry')
print('Azeem\t31\tPakistan')

radius = 10
area = 3.14 * radius ** 2
print(f'The area of a cricle with radius {radius} is {int(area)} meters square.')

print(F'{8} + {6} = {8+6}')
print(F'{8} - {6} = {8-2}')
print(F'{8} * {6} = {8*6}')
print(F'{8} / {6} = {8/6}')
print(F'{8} % {6} = {8%6}')
print(F'{8} // {6} = {8//6}')
print(F'{8} ** {6} = {8**6}')