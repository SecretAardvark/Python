import pandas as pd 
import matplotlib.pyplot as plt

def repmax(weight, reps):
    repmax = 100 * weight / 101.3-2.67123 * reps
    return repmax

df = pd.read_csv("employee_birthday.csv")
print(df)
#TODO: Seperate each lift into their own list 
fsq = []
#TODO: Calculate estimated 1rm for each lift, based on first set
for row in df:
    if df['lift'] == 'fsq':
        repmax = repmax(row['weight1'], row['set1'])
        fsq.append(repmax)

print(fsq)
