import random 

hair_color = ['brown', 'blonde', 'brunette', 'black']
hair_length = ['long', 'short']
skin_color = ['white', 'black', 'brown']
has_beard = ['true', 'false']
smiling = ['true', 'false']


class face():

    def __init__(self, hair_length, hair_color, skin_color, has_beard, smiling):
        self.hair_length = random.choice(hair_length)
        self.hair_color = random.choice(hair_color)
        self.skin_color = random.choice(skin_color)
        self.smiling = random.choice(smiling)
        self.has_beard = random.choice(has_beard)


    def about_self(self):
        print("My hair color is " + self.hair_color)
        print("My hair length is "+ self.hair_length)
        print("My skin color is " + self.skin_color)
        print(self.has_beard)
        print(self.smiling)

        


chad = face(hair_length, hair_color, skin_color, smiling, has_beard)
sabrina = face(hair_length, hair_color, skin_color, smiling, has_beard)

chad.about_self()
sabrina.about_self()