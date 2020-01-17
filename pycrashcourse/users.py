class User():
    def __init__(self, first_name, last_name, age, weight):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age 
        self.weight = weight
    
    def describe_user(self):
        print("Your first name is %s, your last name is %s, you are %s years old and weigh %s"%(self.first_name, self.last_name, self.age, self.weight))

    def greet_user(self):
        print("Hello " + self.first_name + " " + self.last_name + ", How are you today?")

