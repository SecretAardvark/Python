#print(): prints whatever is in the parentheses to the terminal window

print("Hello World!")

#variable: A word that represents a value, or information associated with 
# that variable. Variables can be strings, integers, floating point numbers,
#   lists, dictionaries, etc. You can change the value of a variable at 
#   any time, and python will keep track of the value. 

#   -Variable names can contain only letters, numbers, or underscores, 
#    but cannot start with a number. 
#   -Spaces are not allowed in variable names. 

message = "Hello World!"
#This creates a variable with the value "Hello World!"

print(message)
#This prints "Hello world!" same as above. 

#String: simply a series of characters. Anything inside quotes is considered
#   a string in python, single or double. 

"This is a string."
'This is also a string.'

#this lets you use both types of quotes in one string.

'I told my friend "Python is my favorite language!"'

#method: An action that python can perform on a piece of data. Methods 
#   are always followed by parantheses, because they usually require extra
#   info to do their job. That info is provided in the ().

.title() # A method that capitalizes the words in a string.

name = "ada lovelace"
print(name.title())
#output would be 'Ada Lovelace' (capitalized)

.upper(): #Prints in all uppercase 

print(name.upper())

#output 'ADA LOVELACE'

.lower() #prints in all lowercase

print(name.lower()) 

#output 'ada lovelace'

#Concatenating (combining) strings: strings can be combined by using the
#   + symbol

first_name = 'ada'
last_name = 'lovelace'
full_name = first_name + ''+ last_name

#output = ada lovelace
#   empty quotes are used to put a space inbetween the words.

#This can be used to compose full messages out of variables. 

print("Hello," +full_name.title() + "!")

#output "Hello, Ada Lovelace!"

#Or store this as a variable. 
message = "Hello, " + full_name.title() + "!"

print(message)

#Same output as above. 

\t 
#adds a tab to a string. 
print("\tpython")

\n 
#enters a newline to a string 
print("languages:\nPython\nC\nJavascript")

#output: 

"""languages: 
Python
C
Javascript"""

#\n and \t can be combined in a single string. 

.rstrip()

#takes away whitespace on the right side of a string

.lstrip()
#takes away whitespace on the left 

#integers: You can add + subtract - multiply * divide / numbers in python

2+3 
3-2 
2*3 
3/2 

#this works like regular math 

# ** two multiplications for exponents 

3**2 #9 
3**3 #27 

#float: any number with a decimal point. Largely behave like you would expect.

0.1 + 0.1 #0.2
2*0.1 #.2

.str() #Method that converts numbers to a string. 

age = 23 
message = "Happy " + age + "rd Birthday!"
#This results in a typeError, python cant combine strings and numbers in a
#   print call.

message = "Happy " + str(age) + "rd Birthday!"
#This will work as expected because it converts the age variable to a string.