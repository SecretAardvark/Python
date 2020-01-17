class restaraunt():
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine = cuisine_type
        self.number_served = 0

    def describe_restaraunt(self):
        print("Name: " + self.name.title() + "\n Cuisine: " 
            + self.cuisine) 

    def open_restaraunt(self): 
        print(self.name.title() + " is open, come on in!")
    
    def set_number_served(self, number):
        self.number_served = number
    
    def incremeent_number_served(self, customers):
        self.number_served += customers

class ice_cream_shop(restaraunt):
    def __init__(self, name, cuisine_type):
        super().__init__(name, cuisine_type)
        self.flavors = []
    def describe_flavors(self, ):
       for flavor in self.flavors:
           print("-" + flavor.title())