from sys import exit
import random
from story_objects import Weapon 

#TODO:
#make monster classes x

# make weapon class  x 

#write functions for each room 

def front_door():
    print("The door to the castle opens with a creak.")
    print("You find yourself in a large entry hall.")
    print("There is a chest in the room. Do you open it?")
    choice = input("(yes or no)> ")
    
    if choice == 'yes':
       
        #choice = random.choice(weapons)
        player_weapon = Weapon()
        print(f"You have received a {player_weapon.type}!")
        print("You continue onwards.")
    else:
        print("You ignore the chest and continue onwards.")
    
    print("There are two seperate staircases on each end of the Hall.")
    print("Do you take the right or the left one?")

    stair_choice = input("(right or left)> ")

    if stair_choice == 'right':
        bed_chambers()
    elif stair_choice == 'left':
        kitchen()
    else:
        front_door_again()

def front_door_again():
    print("You return to the entry hall.")
    print("There are two seperate staircases on each end of the Hall.")
    print("Do you take the right or the left one?")

    stair_choice = input("(right or left)> ")

    if stair_choice == 'right':
        bed_chambers()
    elif stair_choice == 'left':
        kitchen()
    else:
        front_door_again()

def bed_chambers(): 
    print("You go up the right staircase and enter a long hallway with the servants quarters.")
    print("As you're exploring you hear one of the locked doors behind you open slowly...")
    print("You turn around and Oh No! Its two Spooky Skeltals! Doot doot!")
    print("What do you do? Fight the Skeltals or run away?")

    choice = input("(fight or flee)> ")

    if choice == 'fight':
        print("You brandish your {player_weapon} and turn to fight!")
        fight_monster('skeltals')
    else:
        print("You scream REEEEEEE and turn to run.")
        front_door()

    

def walk_around():
    print("You decide going in through the front is too obvious.")
    print("You walk around the outside of the castle.")
    print("You come to a dead end.")
    print("There is a large trellis that goes up the side. of the castle.")
    print("maybe you can climb it?")
    print("There is also a beautiful angel statue nearby. It deserves a closer look.")
    print("Which do you choose?")

    choice = input("('inspect statue' or climb trellis)")

    if choice == 'climb trellis':
        dead('You get halfway up the castle and the trellis breaks. You fall to your death. RIP.')
    elif choice == 'inspect statue':
        print("You take a closer look at the statue and find a hidden button! Press that shit.")
        print("You press the button and a hidden passage opens in the side of the castle!")
        print("You enter the hidden passage and emerge on the other side...")
        throne_room()
    else:
        print("You seem confused. You decide to return to the castle entrance.")
        start()


# write loops for each battle 

# write start function 
def start():
    print("You are a brave knight that has been given an important mission by the King!")
    print("You must defeat the evil Dragon and rescue his daughter, the Princess!")
    print("You approach the Dragons stronghold castle.")
    print("Do you enter through the front door or find another way in?") 
    print("(type 'front door' or 'look around')")

    choice = input("> ")

    if choice == 'front door':
        front_door()
    elif choice == 'look around':
        walk_around()
    else:
        start()

def throne_room():
    print("You have entered the throne room!")
    print("No sign of the Dragon yet. You proceed cautiously")
    print("Suddenly you notice the dragon sleeping on the other side of the room!")
    print("The Dragon awakens! What do you do?")
    
    choice = input('(fight or flee)> ')
    if choice == 'fight':
        fight_monster('dragon')
    else:
        print("You attempt to flee but find yourself quaking with fear.")
        print("Oh no!! You've soiled yourself.")
        dead('The dragon chomps you in half.')


def kitchen():
    print("You go up the left side stairway.")
    print("You arrive in the castle kitchen. It's a mess!")
    print("A rat emerges from the pantry. Its gotten huge from eating all the food!")
    print("It hisses and lunges to attack you! What do you do?")
    choice = input("('fight' or 'flee')> ")

    if choice == fight:
        fight_monster('giant rat')
    else:
        print("You scream REEEEEEE and turn to run.")
        front_door()

#write dead() function 
def dead(why):
    print(why, "Good Job!")
    exit(0)

start()