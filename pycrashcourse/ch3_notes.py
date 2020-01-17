#List: A collection of items in a particular order. Lists can be numbers, strings, 
#       basically whatever you want. 
#       Square brackets indicate a list []. Items in a list are seperated by commas. 

drugs = ['weed', 'lsd', 'meth', 'mushrooms']

#Printing a list prints the full python representaion of a list, like so. 
 
print(drugs)

#To print individual items from the list, write the name of the list followed by the index
# number in square brackets. 

print(drugs[0])
print(drugs[3])
print(drugs[-2])

#String methods work on list items. 

print(drugs[3].title())

#You can use individual items from al ist just like any other variable. 

message = "My favorite drug is " + drugs[0].title + "."
print(message)


#You use the same syntax to change an item in a list.

#Original list.
drugs = ['weed', 'lsd', 'meth', 'mushrooms']
print(drugs)

#Changing the first item in the list.
drugs[0] = 'cocaine'
print(drugs)


#Adding elements to the end of a list: 
drugs.append('ecstacy')
#.append() adds an item to the list without effecting anything else.
print(drugs)

#Here we start with an empty list and built it dynamically.
drugs = [ ]

drugs.append('Weed')
drugs.append('LSD')
drugs.append('Cocaine')
drugs.append('mushrooms')
print(drugs)

#You can add a new item anywhere in the list using .insert()
drugs.insert(1, 'ecstasy')
#pass .insert() the position in the list and item you want to add.
print(drugs)

#You can remove items from the list using the del statement
del drugs[0]
print(drugs)

#Use .pop() if you need the value of an item after you delete it. 
favorite_drug = drugs.pop()

print("My favorite drug is " + favorite_drug)
print(drugs)

#You can use .pop() to remove any position in the list by giving it
#the list index. 

new_drug = drugs.pop(1)
print(new_drug)

drugs = ['weed', 'lsd', 'meth', 'mushrooms']
#You can use .remove() to delete an item by its value if you dont know the 
#index #. 
drugs.remove('meth')
print(drugs)

drugs = ['weed', 'lsd', 'meth', 'mushrooms']
#You can use .sort() to sort a list alphabetically. 
drugs.sort()
print(drugs)

#You can also .sort() in reverse like so. 
drugs.sort(reverse = True)
print(drugs)



