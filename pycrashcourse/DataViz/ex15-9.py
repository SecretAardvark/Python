import pygal
from die import Die



die_1 = Die()
die_2 = Die()

results =[die_1.roll() * die_2.roll() for roll_num in range(1000)]

max_result = die_1.num_sides * die_2.num_sides
frequencies = [results.count(value) for value in range(2, max_result+1)]


hist = pygal.Bar()
hist.title= "Results of multiplying two D6 50,000 times"
hist.x_labels = [str(i) for i in range(1,37)]
hist.x_title = "Result"
hist.y_title ="Frequency of Result"

hist.add('D6 * D6', frequencies)
hist.render_to_file('15-9visual.svg') 