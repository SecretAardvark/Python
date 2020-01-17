import pygal
from die import Die



die_1 = Die(8)
die_2 = Die(8)

results =[die_1.roll() + die_2.roll() for roll_num in range(60000000)]

max_result = die_1.num_sides + die_2.num_sides
frequencies = [results.count(value) for value in range(2, max_result+1)]


hist = pygal.Bar()
hist.title= f"Results of rolling two D8 {len(results)} times"
hist.x_labels = [str(i) for i in range(2,17)]
hist.x_title = "Result"
hist.y_title ="Frequency of Result"

hist.add('D8 + D8', frequencies)
hist.render_to_file('15-7visual.svg')    