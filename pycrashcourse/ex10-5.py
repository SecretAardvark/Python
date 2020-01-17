filename = 'codereasons.txt'
prompt = "Why do you like programming? "
prompt += "\n Type q to quit."

with open(filename, 'w') as file:
    message = " "
    while True:
        message = input(prompt)
        if message == 'q':
            break
        file.write(message + '\n')

    
        



