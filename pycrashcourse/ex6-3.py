glossary = {'variable': 'A reserved memory location to store a given value',
     'string': 'A string in Python is an immutable sequence of characters.', 
    'dictionary': 'A dictionary in Python is a collection of key-value pairs.Each Key is connected to a Value, and you can use the key to access that value.',
    'comment': 'A note you can leave in your program for others to read, usually used to explain what lines of code do.',
    'float': 'a number used in Python with a decimal point', 
    'function': 'Python functions can be used to abstract pieces of vode to use elsewhere.',
    'lists': 'A Python data type that holds an unordered collection of values.',
    'FOR loop': 'Used in Python to iterate over a data set.',
    'WHILE loop': 'Lets code execute repeatedly until a certain condition is met.',
    'print()': 'A function that displays the output of a program.',


}

print("Variable: \n \t"  +   glossary['variable'] + "\n String: \n \t" + glossary['string'] + "\n Comment: \n \t" + glossary['comment']+ "\n Dictionary: \n \t" + glossary['dictionary'] 
    + "\n Float: \n \t" + glossary['float']
)

for key in glossary:
    print(key.title() + ": \n \t" + glossary[key]) 