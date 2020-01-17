from users import User

class Admin(User):
    def __init__(self, first_name, last_name, age, weight):
        super().__init__(self, last_name, age, weight)
        self.priviliges = Priviliges()
    

class Priviliges():
    def __init__(self, ):
        self.priviliges = ["Can add post", "Can delete post", "Can ban user"]

    def show_priviliges(self):
        print("Admin priviliges: ")
        for privilege in self.priviliges:
            print("-" + privilege)