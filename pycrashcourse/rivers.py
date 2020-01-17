rivers = { 'Nile': 'Egypt','Mississippi': 'Louisiana', 'Volga': 'Russia', 'Rhine': 'Germany'}

for k, v in rivers.items(): 
    if 'Nile' in k:
        print('The Nile runs through %s'.format(k))

    if 'Mississippi' in k:
        print('The Mississippi runs through %s'.format(k))

    if 'Volga' in k:
        print('The Volga runs through %s'.format(k))


for key in rivers: 
    print(key)

for key in rivers.value(): 
    print(value)

