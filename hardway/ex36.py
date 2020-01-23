from sys import exit
import random
import time
from story_objects import  player, Skeltal, Giant_rat, Dragon

#TODO:
#make monster classes x

# make weapon class  x 

#write functions for each room x

def front_door(knight):
    print("The door to the castle opens with a creak.")
    print("You find yourself in a large entry hall.")
    print("There is a chest in the room. Do you open it?")
    choice = input("(yes or no)> ")
    
    if choice == 'yes':
       
        
        knight.player_weapon()
        print(f"You have received a {knight.weapon_type}!")
        print("You continue onwards.")
    else:
        print("You ignore the chest and continue onwards.")
    
    print("There are two seperate staircases on each end of the Hall.")
    print("Do you take the right or the left one?")

    stair_choice = input("(right or left)> ")

    if stair_choice == 'right':
        bed_chambers(knight)
    elif stair_choice == 'left':
        kitchen(knight)
    else:
        front_door_again(knight)

def front_door_again(knight):
    print("You return to the entry hall.")
    print("There are two seperate staircases on each end of the Hall.")
    print("Do you take the right or the left one?")

    stair_choice = input("(right or left)> ")

    if stair_choice == 'right':
        bed_chambers(knight)
    elif stair_choice == 'left':
        kitchen(knight)
    else:
        front_door_again(knight)

def bed_chambers(knight): 
    print("You go up the right staircase and enter a long hallway with the servants quarters.")
    print("As you're exploring you hear one of the locked doors behind you open slowly...")
    print("You turn around and Oh No! Its a Spooky Skeltal! Doot doot!")
    print("What do you do? Fight the Skeltals or run away?")

    choice = input("(fight or flee)> ")

    if choice == 'fight':
        fight_monster(knight, Skeltal())
    else:
        print("You scream REEEEEEE and turn to run.")
        front_door_again(knight)

    

def walk_around(knight):
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
        throne_room(knight)
    else:
        print("You seem confused. You decide to return to the castle entrance.")
        start()


# write loops for each battle 

def fight_monster(knight, monster):
    not_dead = True
    if knight.weapon_type == 'bare fists':
        print("You don't have a weapon! Uh oh!")
    print(f"You draw your {knight.weapon_type} and prepare to fight the {monster.type}!")
    while not_dead:
        if monster.type == 'Dragon':
            if knight.has_potion == True:
                print("You remember you have a fancy potion and drink it!")
                print("Your hp is restored!")
                knight.hp = 100
                knight.has_potion = False
            else:
                pass

        damage = random.randint(knight.min_damage, knight.max_damage)
        print(f"You attack the {monster.type} for {damage} damage!")
        time.sleep(1)
        monster.hp -= damage
        print(f"The {monster.type}s HP is: {monster.hp}")
        time.sleep(1)
        

        m_damage = random.randint(monster.min_damage, monster.max_damage)
        print(f"The {monster.type} attacks you! It does {m_damage} damage!")
        time.sleep(1)
        knight.hp -= m_damage
        print(f"Your HP is: {knight.hp}")
        time.sleep(1)
        if knight.hp <= 0:
            not_dead = False
            dead(f"the {monster.type} killed you! Crap!")
        elif monster.hp <= 0:
            not_dead = False
            print(f"You defeated the {monster.type}!")
            print("You continue up the stairs.")
            if monster.type == 'Dragon':
                print("You rescue the princess and have crazy hawt sex!")
            else:
                throne_room(knight)


        
    


# write start function 
def start():
    print("You are a brave knight that has been given an important mission by the King!")
    print("You must defeat the evil Dragon and rescue his daughter, the Princess!")
    time.sleep(1)
    print("You approach the Dragons stronghold castle.")
    print("Do you enter through the front door or find another way in?") 
    print("(type 'front door' or 'look around')")
    
    knight = player()

    choice = input("> ")

    if choice == 'front door':
        front_door(knight)
    elif choice == 'look around':
        walk_around(knight)
    else:
        start()

def throne_room(knight):
    print("You have entered the throne room!")
    print("No sign of the Dragon yet. You proceed cautiously")
    time.sleep(1)
    print("Suddenly you notice the dragon sleeping on the other side of the room!")
    print("The Dragon awakens! What do you do?")
    
    choice = input('(fight or flee)> ')
    if choice == 'fight':
        fight_monster(knight, Dragon())
    else:
        print("You attempt to flee but find yourself quaking with fear.")
        print("Oh no!! You've soiled yourself.")
        dead('The dragon chomps you in half.')


def kitchen(knight):
    print("You go up the left side stairway.")
    time.sleep(1)
    print("You arrive in the castle kitchen. It's a mess!")
    print("Might as well search the cupboards while You're here!")
    knight.get_potion()
    print("You find a Magic Potion!")
    time.sleep(1)
    print("A rat emerges from the pantry. Its gotten huge from eating all the food!")
    print("It hisses and lunges to attack you! What do you do?")
    choice = input("('fight' or 'flee')> ")

    if choice == 'fight':
        fight_monster(knight, Giant_rat())
    else:
        print("You scream REEEEEEE and turn to run.")
        front_door_again(knight)

#write dead() function 
def dead(why):
    print(why, "Good Job!")
    exit(0)

start()