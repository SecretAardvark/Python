

try:
    number = int(input("Enter a number: "))
    if number:
        if number % 3 ==0 and number % 5==0:
            print('fizz-buzz')
        elif number % 3 ==0:
            print('fizz')
        elif number % 5==0:
            print('buzz')
        else:
            print(number)
except ValueError:
    print("You didn't enter a number!")