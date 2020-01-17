class restaraunt():
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine = cuisine_type

    def describe_restaraunt(self):
        print("Name: " + self.name.title() + "\n Cuisine: " + self.cuisine) 

    def open_restaraunt(self): 
        print(self.name.title() + " is open, come on in!")

dominos = restaraunt("dominos", "pizza",)
mcdonalds = restaraunt("mcdonalds", "gross")
olive_garden = restaraunt("olive garden", "italian?")



dominos.describe_restaraunt()
mcdonalds.describe_restaraunt()
olive_garden.describe_restaraunt()

    
