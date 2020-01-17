def show_magicians(magicians):
    for magician in magicians: 
        print(magician.title())


def make_great(magicians):

    great_magicians = []
    while magicians:
        magician = magicians.pop()
        great_magician ="The Great " + magician
        great_magicians.append(great_magician)
    print(great_magicians)
      
    


magicians = ["david blaine", "criss angel", "derren brown", "Houdini"]

make_great(magicians[:])
show_magicians(magicians)
show_magicians(great_magicians)