number = input("How many decimal places? ")

def format_e(decimal_place):
    e = 2.7182818284590452353602874713527 
    print("{:{}}".format(e, number))

format_e(number)