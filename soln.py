##name = input(' what is ur name? ')##

##color = input('what is ur fav color')##
##print( name+ ' likes '  +color) ##
##birth_year = input('input ur yr of birth ')##
##age = 2023 - int(birth_year)##
##print(type(birth_year))##
##print(type(age))##
##print(age)##
##weight_lbs = input('weight in lbs ')##
##weight_kgs =int(weight_lbs)*0.45##
##print(weight_kgs)##

#Conditionals
is_hot = True
if is_hot:
 print('hot day')
elif is_cold:
 print('cold day')
else:
 print('beautiful day')


# for loop
 for i in range(1, 5):
    print(i)

# while loop
i = 1
while i < 5:
 print(i)
 i += 1


#LISTS
numbers = [1, 2, 3, 4, 5]
numbers[0] # returns the first item
numbers[1] # returns the second item
numbers[-1] # returns the first item from the end
numbers[-2] # returns the second item from the end
numbers.append(6) # adds 6 to the end
numbers.insert(0, 6) # adds 6 at index position of 0
numbers.remove(6) # removes 6
numbers.pop() # removes the last item
numbers.clear() # removes all the items
numbers.index(8) # returns the index of first occurrence of 8
numbers.sort() # sorts the list
numbers.reverse() # reverses the list
numbers.copy() # returns a copy of the list


#Dictionaries
customer = {
 'name': 'John Smith',
 'age': 30,
 'is_verified': True
}
customer['name'] # returns “John Smith”
customer['type'] # throws an error
customer.get('type', 'silver') # returns “silver”
customer['name'] = 'new name'

#Function
def greet_user(name):
    print(f'Hi {name}')
    greet_user('John')