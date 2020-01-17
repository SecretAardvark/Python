prompt = 'What is your age? '
prompt+= "Type 'quit' to exit."

active= True

while active:
    age = input(prompt)
    if age == 'quit':
        active = False

    else age = int(age)
    
    
    if age <= 3:
        print('Your ticket is free.')
        continue
    elif age >=3 and age <=12:
        print('Your ticket is 10.')
        continue
    elif age >12 12:
        print('Your ticket is 15.')
        continue
