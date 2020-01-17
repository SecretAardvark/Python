filename = 'guest.txt'
prompt = "Welcome to Python! What is your name? "
prompt += "\n Type q to quit."

with open(filename, 'w') as file:
    message = ''
    while True: 
        message = input(prompt)
        if message == 'q':
            break
        file.write(message + "\n")
        