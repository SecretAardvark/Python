class restaraunt():
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine = cuisine_type
        self.number_served = 0

    def describe_restaraunt(self):
        print("Name: " + self.name.title() + "\n Cuisine: " + self.cuisine) 

    def open_restaraunt(self): 
        print(self.name.title() + " is open, come on in!")
    
    def set_number_served(self, number):
        self.number_served = number
    
    def incremeent_number_served(self, customers):
        self.number_served += customers


restaraunt = restaraunt("dominoes", "pizza",)

print(restaraunt.name)
print(restaraunt.cuisine)

restaraunt.describe_restaraunt()
restaraunt.open_restaraunt()


print(restaraunt.number_served)
restaraunt.number_served = 200
print(restaraunt.number_served)


restaraunt.set_number_served(300)
print(restaraunt.number_served)

restaraunt.incremeent_number_served(25)
print(restaraunt.number_served)

    
