try:
    with open("cats.txt") as fileobject: 
        for line in fileobject:
            print(line)
except FileNotFoundError:
    print("File does not exist!")
try:
    with open("dogs.txt") as fileobject:
        for line in fileobject:
            print(line)
except FileNotFoundError:
    print("File does not exist!")
