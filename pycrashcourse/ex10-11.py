import json

def get_new_number():
    username = input("What is your favorite number? ")   
    filename = 'favnumber.json'
    with open(filename, 'w') as f_obj:
       json.dump(username, f_obj)
    return username

def get_number():
    filename = 'favnumber.json'
    try:
        with open(filename) as f_obj:
            favnumber = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return favnumber

def tell_number():
    favnumber = get_number()
    if favnumber:
        print("I know your favorite number! It's... " + favnumber)
    else:
        favnumber = get_new_number()
        print("We'll remember for next time. ")


get_new_number()