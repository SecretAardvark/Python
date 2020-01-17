from sys import argv

script, filename = argv

input(f"Were going to erase {filename}."
    "\nIf you dont want that to happen hit ctcl-c."
    "\nIf you do want that, hit return."
     "\n ?")


print("Opening the file...")

target = open(filename, 'w')

print("truncating the file. Goodbye.")

target.truncate()

print("Now i'm going to ask you for 3 new lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("i'm going to write these to the file.")

target.write(line1 + '\n' + line2 +  '\n' + line3 + '\n')

print("and finally, we close it.")
target.close()