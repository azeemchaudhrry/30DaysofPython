# Day 6 Exercise

# Create an empty tuple
empty_tuple = ()
# Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
brothers = ('david', 'john')
sisters = ('alex', 'rice')
# Join brothers and sisters tuples and assign it to siblings
joined_tuple = brothers + sisters
# How many siblings do you have?
print('How many siblings do you have : ', len(joined_tuple))
# Modify the siblings tuple and add the name of your father and mother and assign it to family_members
parents = ('John Snow', 'Martha')
family_members = parents + joined_tuple
print('Family Memebers : ', family_members)
# Unpack siblings and parents from family_members
parent = family_members[0:2]
siblings = family_members[2:]
print('Parent : ', parent)
print('Siblings : ', siblings)

# Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ('Apple', 'Banana', 'Cherry', 'Grapes')
vegetables = ('Beans','Broccoli','Beetroot')
animal_products = ('Milk','Eggs','Cheese')
food_stuff_tp = fruits + vegetables + animal_products
print(f'Food Stuff tp {food_stuff_tp}')

# Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
print(f'Food Stuff List : {food_stuff_lt}')

# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
middle_item = food_stuff_tp[4:6]
print('Tuple middle item : ', middle_item)

middle_item = food_stuff_lt[4:6]
print('List middle item : ', middle_item)

# Slice out the first three items and the last three items from food_staff_lt list
first_three_items = food_stuff_tp[0:3]
print('First three items : ', first_three_items)

last_three_items = food_stuff_lt[7:]
print('Last three items : ', last_three_items)

# Delete the food_staff_tp tuple completely
del food_stuff_tp

# Check if an item exists in tuple:
print('\'Apple\' in food_stuff_lt : ', 'Apple' in food_stuff_lt)

# Check if 'Estonia' is a nordic country
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Is \'Estonia\' a nordic country?', 'Estonia' in nordic_countries)

# Check if 'Iceland' is a nordic country
print('Is \'Iceland\' a nordic country?', 'Iceland' in nordic_countries)