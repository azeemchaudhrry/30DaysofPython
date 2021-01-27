# Exercise Day 7
# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Find the length of the set it_companies
print('Length of it_companies set : ', len(it_companies))

# Add 'Twitter' to it_companies
it_companies.add('Twitter')
print('it_companies : ', it_companies)

# Insert multiple IT companies at once to the set it_companies
it_companies.update(['SAP', 'Mashworx', 'Orange'])
print('it_companies : ', it_companies)

# Remove one of the companies from the set it_companies
it_companies.remove('Twitter')
print('it_companies : ', it_companies)

# What is the difference between remove and discard
# remove - raise error if item not found
# discard - does not 

# Join A and B
C = A.union(B)
print('Join A and B : ', C)

# Find A intersection B
A.intersection(B)
print('Intersection A and B : ', A)

# Is A subset of B
print('Is A subset of B : ', A.issubset(B))

# Are A and B disjoint sets
print('Are A and B disjoint sets : ', B.isdisjoint(A))

# Join A with B and B with A
C = A.union(B)
D = B.union(A)
print('Join A with B : ', C)
print('Join B with A : ', D)

# What is the symmetric difference between A and B
print('Symmetric difference between A and B : ', B.symmetric_difference(A))

# Delete the sets completely
del C

# Convert the ages to a set and compare the length of the list and the set, which one is bigger?
ageset = list(age)
print('Age list length : ', len(age))
print('Age set length : ', len(ageset))

# Explain the difference between the following data types: string, list, tuple and set
# string - immutables, only contain characters
# list - mutable, like arrays, any type of object
# tuple - immutables. like arrays, any type of object
# set - mutable, any type of object

# I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? You did not learn loops yet you can do it manually.
statement = 'I am a teacher and I love to inspire and teach people.'
words_set = set(statement.split(' '))
print('Set : ', words_set)