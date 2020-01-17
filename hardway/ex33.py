
def while_loop(number, increment):
    i =0 
    numbers = []
    while i < number:
        print(f"At the top i is {i}")
        numbers.append(i)

        i += increment
        print("Numbers now: ", numbers)

        print(f"At the bottom i is {i}")
    print("The numbers: ")
    for num in numbers:
        print(num)


while_loop(50,2)