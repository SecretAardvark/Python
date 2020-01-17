languages = { 'jen': 'python', 'sarah': 'c', 'edward': 'ruby','phil': 'python',  
}


poll = ['Chad', 'Sabrina', 'Wiley', 'jen', 'sarah', 'phil']

for name in poll:
    if name in languages:
        print(name + ", thanks for taking the poll.")

    elif name not in languages:
        print(name + ", please take the poll.")
    
