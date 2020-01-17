import random 

hair_color = ['brown', 'blonde', 'brunette', 'black']
hair_length = ['long', 'short']
skin_color = ['white', 'black', 'brown']

class face():

    def __init__(self, hair_length, hair_color, skin_color):
        self.hair_length = random.choice(hair_length)
        self.hair_color = random.choice(hair_color)
        self.skin_color = random.choice(skin_color)

    def about_self(self):
        print("My hair color is " + self.hair_color)
        print("My hair length is "+ self.hair_length)
        print("My skin color is " + self.skin_color)

        


chad = face(hair_length, hair_color, skin_color)
sabrina = face(hair_length, hair_color, skin_color)

chad.about_self()
sabrina.about_self()