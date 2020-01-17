class User():
    def __init__(self, first_name, last_name, age, weight):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age 
        self.weight = weight
        self.login_attempts = 0
    
    def describe_user(self):
        print("Your first name is %s, your last name is %s, you are %s years old and weigh %s"%(self.first_name, self.last_name, self.age, self.weight))

    def greet_user(self):
        print("Hello " + self.first_name + " " + self.last_name + ", How are you today?")
    
    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0 


Chad = User("Chad", "Tennent", 30, 184)

Chad.increment_login_attempts()
Chad.increment_login_attempts()
Chad.increment_login_attempts()


print(Chad.login_attempts)

Chad.reset_login_attempts()

print(Chad.login_attempts)