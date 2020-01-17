voteage = 18
age = int(input('How old are you? '))

if age >= voteage: 
    print('You are old enough to vote.')
else:
    print('You are old enough to vote in '+ str(voteage-age) + ' years.')