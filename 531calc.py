#TODO: Write a function to calculate 1RM and training max 
def find_onerep(weight, reps):
    onerepmax = int(weight) * int(reps) * .0333 + int(weight)
    #training_max = onerepmax * .9
    return onerepmax #training_max


#TODO: Use that function and user input to calculate user's 1rm weights. 
lifts = ['ohp','squat', 'deadlift', 'bench']
#Get lift stats from the user.
for lift in lifts:
    weight = input(f"How much weight did you lift for {lift}? ")
    reps = input("How many reps did you do? ")
    #find the 1rm
    onerepmax = find_onerep(weight, reps)
    #find the 5/3/1 training max. 
    training_max = onerepmax * .9
    print(onerepmax)
    print(training_max)
    print(f"Your {lift} max is: " + str(training_max))
    print(f"Your {lift} training max is: " + str(training_max))
#TODO: Make a dictionary of training maxes for each lift.
    training_maxes = {'ohp': '', 'squat': '', 'deadlift': '', 'bench': '',}
    if lift == 'ohp':
        ohp_week1 = {'set1': training_max * .65, 'set2' : training_max *.75, 'set3': training_max * .85}
        ohp_week2 = {'set1': training_max * .7, 'set2' : training_max * .8, 'set3': training_max *.9}
        ohp_week3 = {'set1': training_max * .75, 'set2' : training_max * .85, 'set3': training_max *.95}

        ohp = [ohp_week1, ohp_week2, ohp_week3]
        training_maxes['ohp'] = training_max

    elif lift == 'squat':
        squat_week1 = {'set1': training_max * .65, 'set2' : training_max *.75, 'set3': training_max * .85}
        squat_week2 = {'set1': training_max * .7, 'set2' : training_max * .8, 'set3': training_max *.9}
        squat_week3 = {'set1': training_max * .75, 'set2' : training_max * .85, 'set3': training_max *.95}

        squat = [squat_week1, squat_week2, squat_week3]
        training_maxes['squat'] = training_max

    elif lift == 'deadlift':
        dead_week1 = {'set1': training_max * .65, 'set2' : training_max *.75, 'set3': training_max * .85}
        dead_week2 = {'set1': training_max * .7, 'set2' : training_max * .8, 'set3': training_max *.9}
        dead_week3 = {'set1': training_max * .75, 'set2' : training_max * .85, 'set3': training_max *.95}

        deadlift = [dead_week1, dead_week2, dead_week3]
        training_maxes['deadlift'] = training_max
    
    elif lift == 'bench':
        bench_week1 = {'set1': training_max * .65, 'set2' : training_max *.75, 'set3': training_max * .85}
        bench_week2 = {'set1': training_max * .7, 'set2' : training_max * .8, 'set3': training_max *.9}
        bench_week3 = {'set1': training_max * .75, 'set2' : training_max * .85, 'set3': training_max *.95}

        bench = [bench_week1, bench_week2, bench_week3]
        training_maxes['bench'] = training_max


#TODO: Make a list of smaller dictionaries that contain weights for each set, 
#   and each lift. 






print(ohp)
print(ohp[0]['set3'])
print(ohp[1]['set3'])
print(bench)
print(bench[0]['set3'])
print(squat)
print(squat[0]['set3'])
print(deadlift)
print(deadlift[0]['set3'])