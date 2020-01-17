prompt = "\nEnter a topping for your Pizza: "
prompt += '\n Enter quit to end the program.'

while True:
    topping = input(prompt)

    if topping == 'quit':
        break
    else:
        print("I'll add " + topping.title()+ ' to your pizza.')