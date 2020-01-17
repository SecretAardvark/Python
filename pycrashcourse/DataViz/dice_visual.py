import pygal
from die import Die



die_1 = Die()
die_2 = Die(10)

results =[die_1.roll() + die_2.roll() for roll_num in range(50000)]

max_result = die_1.num_sides + die_2.num_sides
frequencies = [results.count(value) for value in range(2, max_result+1)]


hist = pygal.Bar()
hist.title= "Results of rolling a D6 and a D10 50,000 times"
hist.x_labels = [str(i) for i in range(2,17)]
hist.x_title = "Result"
hist.y_title ="Frequency of Result"

hist.add('D6 + D10', frequencies)
hist.render_to_file('dice_visual.svg')    