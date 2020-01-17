with open("learning_python.txt") as file_object:
    contents = file_object.read()
    print(contents)
    
with open("learning_python.txt") as file_object:
    for line in file_object:
        print(line)

with open("learning_python.txt") as file_object:
    wordlist = file_object.readlines()
    for line in wordlist:
        print(line.rstrip())

with open("learning_python.txt") as file_object:
    contents = file_object.read()
    contents = contents.replace('python', 'Ruby')
    print(contents)