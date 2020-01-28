#TODO: Write a function to calculate 1RM and training max 
def find_onerep(weight, reps):
    onerepmax = int(weight) * int(reps) * .0333 + int(weight)
    #training_max = onerepmax * .9
    return onerepmax, #training_max


#TODO: Use that function and user input to calculate user's 1rm weights. 
lifts = ['ohp','squat', 'deadlift', 'squat']
for lift in lifts:
    weight = input(f"How much weight did you lift for {lift}? ")
    reps = input("How many reps did you do? ")

    onerepmax = find_onerep(weight, reps)
    training_max = onerepmax * .9
    print(f"Your {lift} max is: " + str(training_max))
    print(f"Your {lift} training max is: " + str(training_max))

    if lift == 'ohp':
        ohp_week1 = {'set1': training_max * .65, 'set2' : training_max *.75, 'set3': training_max * .85}
        ohp_week2 = {'set1': training_max * .7, 'set2' : training_max * .8, 'set3': training_max *.9}
        ohp_week3 = {'set1': training_max * .75, 'set2' : training_max * .85, 'set3': training_max *.95}

        ohp = [ohp_week1, ohp_week2, ohp_week3]

#TODO: Make a dictionary of training maxes for each lift.

#TODO: Make a list of smaller dictionaries that contain weights for each set, 
#   and each lift. 






print(ohp)
print(ohp[0]['set3'])
print(ohp[1]['set3'])