class restaraunt():
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine = cuisine_type

    def describe_restaraunt(self):
        print("Name: " + self.name.title() + "\n Cuisine: " + self.cuisine) 

    def open_restaraunt(self): 
        print(self.name.title() + " is open, come on in!")

restaraunt = restaraunt("dominoes", "pizza",)

print(restaraunt.name)
print(restaraunt.cuisine)

restaraunt.describe_restaraunt()
restaraunt.open_restaraunt()



    
