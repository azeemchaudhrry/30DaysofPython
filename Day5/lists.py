from countries import * 

lst = list()
print('Length',  len(lst))
lst = []
print('Length',  len(lst))

lst = ['item1', 'item2', 'item3', 'item4', 'item5']
first_item, *remaining, last_item = lst
print(first_item)
print(last_item)
print(remaining)

print(lst[0:4])
print(lst[0:])
print(lst[0:1])
print(lst[::2])

fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[-4:]
skip_last = fruits[-3:-1]
reverse_fruits = fruits[::-1]

lst.append('One')
print(lst)
lst.insert(0, "zero")
print(lst)

# lst.remove('zero')
# lst.remove('One')
lst.pop()
lst.pop(0)
print(lst)

lstNew = lst.copy()
lstNew.append('Azeee')
print(lst)
print(lstNew)

lstOne = ['0','1', '1']
lstTwo = ['2','3']
lstOne.extend(lstTwo)
print(lstOne)
print(lstOne.count('1'))
print(lstOne.index('2'))
lstOne.reverse()
print(lstOne)

lstOne.sort()
print(sorted(lstOne))

# Exercise: Day 5
empty_list = list()
number_list = ['1','2','3','4','5']
print(len(number_list))
first_item, left_range, middle_item, right_range, last_item = number_list
print(first_item)
print(middle_item)
print(last_item)
mixed_data_types = ['Azeem', 31, 5.11, True, 'Pakistan']
print(mixed_data_types)
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle','Amazon']
print(it_companies)

print(len(it_companies))

print(it_companies[0])
print(it_companies[int(len(it_companies) / 2)])
print(it_companies[len(it_companies) - 1])

it_companies[2] = 'Macrosoft'
print(it_companies)

it_companies.append('SAP')
print(it_companies)

middle_index = int(len(it_companies) / 2)
it_companies.insert(middle_index, 'Mashworx')
print(it_companies)

it_companies[2] = it_companies[2].upper()
print(it_companies)

print(' #'.join(it_companies))

print('SAP is it_companies : ', 'SAP' in it_companies)
it_companies.sort()
print(it_companies)
it_companies.reverse()
print(it_companies)

first_three_names = it_companies[0:3]
print(first_three_names)

last_three_names = it_companies[-3:]
print(last_three_names)

it_companies.remove(it_companies[0])
print(it_companies)

it_companies.remove(it_companies[int(len(it_companies) / 2)])
print(it_companies)

it_companies.remove(it_companies[int(len(it_companies) - 1)])
print(it_companies)

it_companies.clear()
print(it_companies)

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

print(front_end + back_end)
front_end.extend(back_end)
print(front_end)

full_stack = front_end.copy()
redux_index = full_stack.index('Redux')
full_stack.insert(redux_index + 1, 'Python')
full_stack.insert(redux_index + 2, 'SQL')
print(full_stack)

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
minimum_age = ages[0]
maximum_age = ages[len(ages) - 1]
print(f'Minimum Age : {minimum_age}')
print(f'Maximum Age : {maximum_age}')
ages.append(minimum_age)
ages.append(maximum_age)
print(ages)
ages.sort()
print(ages)

middle_index = int(len(ages) / 2)
median_age = ages[middle_index]
print(f'Median age : {median_age}')
average_age = sum(ages) / len(ages)
print(f'Average age : {average_age}')

# Find the range of the ages (max minus min)
range = max(ages) - min(ages)
print(f'Range : {range}')

# Compare the value of (min - average) and (max - average), use abs() method
result = abs(minimum_age - average_age) == abs(maximum_age - average_age) 
print(f'Result : {result}')

middle_index = int(len(countries) / 2 + 0.5)
print('Middle index : ', middle_index)
print('Middle Countries : ', countries[middle_index])

another_countries_lst = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
china, russia, usa, *scandic = another_countries_lst
print('First Country : ', china)
print('Second Country : ', russia)
print('Third Country : ', usa)
print('Scandic Countries : ', scandic)