def show_magicians(magician_names):
    while magician_names:
        magician = magician_names.pop()
        print(magician)
    

magician_names = ["david blaine", "criss angel", "derren brown", "Houdini"]

show_magicians(magician_names)