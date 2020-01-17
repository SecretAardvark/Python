def print_two(*args):
    arg1, arg2 = args
    print(f"Arg 1: {arg1}, arg 2: {arg2}")

def print_two_again(arg1, arg2,):
    print(f"Arg1: {arg1} Arg2: {arg2}")

def print_one(arg1):
    print(f"Arg 1: {arg1}")

def print_none():
    print("I got nothing.")

print_two("Zed", "shaw")
print_two_again("Zed", "Shaw")

print_one("First!")

print_none()