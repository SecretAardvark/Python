while True:
    print("Enter two numbers to be added.")
    print("type 'q' to quit.")
    first_number = input("First number? ")
    if first_number == 'q':
        break
    second_number = input("Second number? ")
    try:
       result = int(first_number) + int(second_number)
    except ValueError:
        print("You must enter two numbers.")
    else: 
        print(result)