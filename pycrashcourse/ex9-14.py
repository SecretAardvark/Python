from random import randint

class Dice():
    def __init__(self, sides  = 6 ):
        self.sides = sides
   
    def roll_die(self):
        print("You rolled 1 die for:  " + str(randint(1, self.sides)))

die1 = Dice()
die2 = Dice()

die1.roll_die()
die2.roll_die()

die1.roll_die()
die2.roll_die()