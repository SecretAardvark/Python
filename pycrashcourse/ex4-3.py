def print20():
    list = [num + 1 for num in range(0,20)]
    return(list)

digits = print20()

def nthEven(num):
    return max([x for x in range(0, num*2, 2)])

print(nthEven(20))    
print(digits)