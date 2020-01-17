import matplotlib.pyplot as plt 

input_values = list(range(1,5000))
x_values = list(range(1,5000))
y_values = [x**3 for x in x_values]

plt.xlabel("Value", fontsize = 15)
plt.ylabel("Cube of Value", fontsize = 15)

plt.plot(x_values, y_values,)

plt.show()