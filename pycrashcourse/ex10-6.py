def add_two():
    print("Enter two numbers to be added.")
    first_number = input("What's the first #? ")
    second_number = input("Whats the second?")
    try:
        result = int(first_number) + int(second_number)
    
    except ValueError:
        print("You must enter two numbers")
    else:
        print(result)


add_two()