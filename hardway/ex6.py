types_of_people=10
x = f"There are {types_of_people} types of people."
#Sets a variable and then formats a string to use that variable

binary = "binary"
do_not = "dont"
y = f"Those who know {binary} and those who {do_not}"
#Sets a variable and then formats a string to use that variable


print(x)
print(y)
#prints the two formatted strings from before
print(f"I said: {x}")
print(f"I also said: '{y}'")
#more printing with those two variables 


hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation.format(hilarious))
#shows a different method of formatting a string with variables
w = "This is the left side of..."
e= "a string with a right side."

print(w+e)
#Prints both of the strings in the variables together
