import matplotlib.pyplot as plt
from random_walk import RandomWalk
from random import choice


while True:
    rw = RandomWalk(5000)
    rw.fill_walk()
    point_numbers = list(range(rw.num_points))

    plt.figure(figsize =(10,6))
    
    plt.plot(rw.x_values, rw.y_values, linewidth=20, c=point_numbers, cmap=plt.cm.Spectral)
    plt.plot(0,0, c='green', )
    plt.plot(rw.x_values[-1], rw.y_values[-1], c ='red',  )


    plt.show()

    keep_running = input("Make another walk? y/n: ")
    if keep_running == 'n':
        break

    