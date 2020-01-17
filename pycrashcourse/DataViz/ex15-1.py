import matplotlib.pyplot as plt 

input_values = list(range(1,5001))
cubes = [x**3 for x in input_values]


plt.title("Cubed Numbers")
plt.xlabel("Value", fontsize= 14)
plt.ylabel("Cube of Value", fontsize =14)

plt.scatter(input_values, cubes, c=cubes, cmap=plt.cm.rainbow, 
    s= 40) 

plt.show()