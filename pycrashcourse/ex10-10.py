
with open('meditate.txt') as file: 
    text = str(file.readlines())
    print(text.lower().count('the'))
