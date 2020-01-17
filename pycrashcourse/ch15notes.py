#Notes on the Matplotlib module

import matplotlib as plt

#Simple line Graph
squares = [1,4,9,16,25]
plt.plot(squares) #plt.plot() : Tries to plot given numbers in a meaningful way.
plt.show() #plt.show(): Opens Matplotlibs viewer and displays the plot. 


#formatting a plot
plt.plot(squares, linewidth=5) #'linewidth' parameter changes width of the line
plt.title("Square Numbers", fontsize =25) #plt.title(): Puts a title on the plot display. 'fontsize' parameter changes fontsize. 
plt.xlabel('Value', fontsize =14) #plt.xlabel(): Adds a label for the x axis
plt.ylabel("Square of Value",fontsize = 15) #plt.ylabel(): Adds a label for the y axis
plt.tick_params(axis='both', labelsize = 15) #plt.tick_params(): Sets the size of the tick labels


plt.scatter(2,4) #plots a single point on a graph

#You can plot multiple points with .scatter() like this: 

x_values = [1,2,3,4,5]
y_values = [1,4,9,16,25]

plt.scatter(x_values, y_values, s=100)

#Calculating data automatically (list comprehensions):

x_values = list(range(1,1001)) #This creates a list of numbers from 1 - 1001
y_values = [x**2 for x in x_values] #This creates a list by looping through the x_values. This lets you write a for loops in one line.
plt.scatter(x_values, y_values, edgecolor = 'none', s=40) #'edgecolor' attribute: lets you set the edgecolor of your points


plt.axis([0,1100, 0, 1100000]) #.axis(): Sets the range for each axis. 